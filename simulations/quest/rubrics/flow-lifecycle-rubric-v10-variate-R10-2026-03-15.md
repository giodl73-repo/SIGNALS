# flow-lifecycle — Round 10 Variations (Rubric v10)

**Rubric**: v10 · 36 criteria (28 aspirational) · Ceiling entering R10: 28/28 (R9 V-04 and V-05 cracked C-34, C-35, C-36)
**Open criteria entering R10**: None — C-34, C-35, C-36 all cracked by R9 architecture.
**R10 objective**: All five variations carry the full R9 ceiling (28/28). Variation axes probe
potential C-37+ territory. Single-axis first (V-01 through V-03), then combine.

**Evidence from R9 excellence (C-34, C-35, C-36):**
- C-34 signal: INCUMBENT BASELINE table assigns IM-IDs to failure modes; B-NN Cause field
  cites IM-ID by literal string — "IM-01" in baseline table matches "IM-01" in B-01 Cause field.
  Traceability is verifiable by string comparison in the Baseline→B-NN direction.
- C-35 signal: Quantified metric declared in INCUMBENT BASELINE before first phase block in
  document order ("Rejection rate: 18%", "Average delay per rejection: 3.2 days"). Pre-phase
  position is the structural property — metric after first phase block fails.
- C-36 signal: PHASE ENTRY CONTRACT and PHASE EXIT GATE blocks named per phase with explicit
  sub-fields: Entry Condition / Pre-condition check / Blocking condition (entry) and Exit
  Condition / Required outputs / Exit verification / Blocking condition (exit). Named sub-fields
  are the structural property — unnamed prose descriptions fail.

**Rubric note (C-37 probe):**
The C-36 rubric note reads: "an explicit bottleneck forward-reference field is not required for
C-36 — that is a higher criterion introduced when V-04/V-05 are scored in R10." V-02, V-04,
and V-05 below add a `Blocked bottleneck: B-NN or NONE` sub-field to the PHASE EXIT GATE to
probe this C-37 territory.

**Variation axes chosen:**

- **Axis A — Role sequence**: A ROLE SEQUENCE SCHEDULE is declared after the Role Registry Gate
  and before the first phase. It maps each role (R-ID) to the phases they own, the handoff
  trigger to the next phase owner, and parallel approval timing. B-NN Cause fields cite IM-ID
  AND blocking role.
- **Axis B — Phase-exit gate bottleneck linkage**: A `Blocked bottleneck: B-NN or NONE` sub-field
  is added to every PHASE EXIT GATE block, naming the B-ID when a declared bottleneck can delay
  phase exit, or NONE when no bottleneck blocks it. Probes C-37.
- **Axis C — BOTTLENECK IMPACT MATRIX (output format)**: After Gap Identification, a
  BOTTLENECK IMPACT MATRIX table consolidates all B-NN→IM-ID→SLA→Phase linkages into a single
  cross-reference artifact. Tests whether tabular consolidation surfaces a C-37+ density criterion.

| Variation | Axis | Hypothesis |
|-----------|------|-----------|
| V-01 | A only: Role sequence schedule | Pre-declaring role-to-phase ownership as a named table makes phase-ownership traceable from Role Registry to bottleneck cause — may surface Role→Phase→B-NN as a new cross-section traceability direction |
| V-02 | B only: Phase-exit gate bottleneck linkage | Adding `Blocked bottleneck:` as a named sub-field in PHASE EXIT GATE creates a Phase→B-NN traceability slot verifiable by string comparison — "B-02" in exit gate and "B-02" in bottleneck block are consistent by inspection |
| V-03 | C only: BOTTLENECK IMPACT MATRIX | A consolidated matrix of all B-NN→IM-ID→SLA→Phase linkages makes cross-section traceability density scannable at a glance — may surface a C-37+ quantified-impact criterion distinct from per-block Evidence fields |
| V-04 | A + B: Role sequence + exit gate bottleneck linkage | Role sequence anchors ownership; exit gate bottleneck linkage anchors phase-delay causation; compound structural pressure on Role→Phase→B-NN traceability |
| V-05 | A + B + C: all three axes | Maximum traceability density: role schedule + exit gate B-ID + impact matrix; tests whether the three new artifacts compose into a coherent multi-directional cross-reference system |

---

## V-01 — Axis A: Role Sequence Schedule

**Variation axis**: Role sequence — a ROLE SEQUENCE SCHEDULE is declared as a named structural
element after the Role Registry Gate and before the first phase block. It maps each R-ID to the
phases they own, the handoff trigger that activates the next owner, and any parallel approval
windows. Every B-NN Cause field must cite both the incumbent failure mode (IM-ID) and the role
that is absent or blocked when the failure occurs.

**Hypothesis**: Role Registry (C-12) declares who exists; ROLE SEQUENCE SCHEDULE declares when
each role is active. When a bottleneck's Cause field cites both "IM-01" (from the baseline table)
and "R-02 unavailable during peak period" (from the schedule), a reviewer can trace the failure
mode across three artifacts: INCUMBENT BASELINE → ROLE SEQUENCE SCHEDULE → B-NN Cause. This
multi-directional chain is verifiable by string comparison and may surface a C-37+ signal around
Role→Phase→B-NN as a new traceability direction orthogonal to the Baseline→B-NN chain (C-34) and
the SLA↔B-NN chain (C-14/C-16).

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete this section before the Role Registry Gate. It establishes the manual or status-quo
> version of this process — how it is executed today without the system under analysis. Every
> bottleneck cause in subsequent sections must cite at least one named incumbent failure mode
> (IM-ID) from this table.

**Process type**: [L2O / P2P / Period Close / Case Lifecycle — auto-detect from {Topic}]

**Incumbent description**: [1–3 sentences: tools used (spreadsheets, email, phone), handoff
mechanisms, where records are stored, who initiates the process manually]

**Incumbent failure modes** (assign IM-ID to each):

| IM-ID | Failure Mode | Frequency | Downstream Effect |
|-------|-------------|-----------|------------------|
| IM-01 | [specific recurring failure in the manual process] | [daily / per-cycle / per-exception] | [what breaks downstream when this occurs] |
| IM-02 | [second distinct failure mode] | [frequency] | [downstream effect] |

**Cost of no action**: [Name a specific accumulating metric — queue depth, error rate, cycle
time, reconciliation backlog. Example: "Average delay per rejected invoice: 3.2 days" or
"Credit approval rework rate: 18%". This metric must appear before the first PHASE block
in document order. A metric declared after PHASE 1 begins fails C-35.]

---

### Role Registry Gate

> GATE BLOCK: Complete this section before the Role Sequence Schedule and before tracing any
> state. Do not proceed until all R-ID entries are filled and all three anti-generic checks pass.

| R-ID | Role | Function |
|------|------|----------|
| R-01 | [domain-specific role] | [named responsibility] |
| R-02 | [domain-specific role] | [named responsibility] |
| R-03 | [domain-specific role] | [named responsibility] |

Anti-generic validation (all three must clear before proceeding):
- [ ] No R-ID entry uses "Approver" without a domain qualifier
- [ ] No R-ID entry uses "Owner" without a named responsibility
- [ ] Each R-ID is referenced by at least one Decision Supplement block and by the Role Sequence Schedule below

Role set by process type:
- L2O → Sales Rep / Sales Manager / Finance Credit Analyst / Legal Counsel / Fulfillment Coordinator
- P2P → Procurement Officer / Accounts Payable Specialist / Receiving Dock Supervisor / Finance Controller
- Period Close → Finance Analyst / GL Manager / Controller / External Auditor
- Case Lifecycle → Support Engineer / Case Manager / Legal Counsel / Operations Coordinator

---

### Role Sequence Schedule

> Complete this section after the Role Registry Gate and before PHASE 1. It declares when each
> role is active, what handoff trigger activates the next owner, and whether any roles operate
> in parallel. Every B-NN Cause field below must cite the blocking role from this schedule.

| Phase | Primary Owner (R-ID) | Activation Trigger | Handoff Trigger | Parallel Role (R-ID) | Parallel Window |
|-------|---------------------|-------------------|-----------------|----------------------|----------------|
| Phase 1 | R-[ID] | [what starts this phase — prior artifact or system event] | [what completes phase 1 and hands off to phase 2 owner] | R-[ID] or NONE | [concurrent activity during phase 1, or NONE] |
| Phase 2 | R-[ID] | [handoff received from phase 1] | [completion condition] | R-[ID] or NONE | [concurrent activity or NONE] |

Rules:
- Every phase must have a Primary Owner.
- Activation Trigger for Phase 1 must name an external event or prior-process artifact, not "Start".
- Handoff Trigger must be specific — "approval received" fails; "Credit Limit Approved with attached credit memo" passes.
- Parallel windows must declare start and end states (S-IDs) when known.

---

### Phase Structure

For each phase in the lifecycle, produce the following five blocks in document order:

---

**PHASE [N] — [PHASE NAME]**

**PHASE ENTRY CONTRACT**

> This gate must be completed before SECTION A or SECTION B for this phase.
> Entry Condition must reference the prior phase's PHASE EXIT GATE "Required outputs" field
> by name — a generic "previous phase complete" fails.

- Entry Condition: [specific output from the prior phase's exit gate that must exist before this phase begins; name the artifact or state record]
- Pre-condition check: R-[ID] ([role name]) — [how they verify the entry condition is met]
- Blocking condition: [if entry condition is not met: which state is entered, which role is notified, and what re-entry path applies]

**SECTION A — EXCEPTION TRACES**

For each exception trace originating in this phase:

> **EX-[Phase#][Letter] — [Exception Name]**
> - Trigger: [specific condition that causes deviation from the happy path — name the state, threshold breach, or missing input]
> - Trace: [path of states traversed from trigger to resolution or terminal; cite S-IDs in sequence]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state name — SUCCESS / FAILURE / CANCEL] or [continues-via: S-[ID]]
> - Why Problematic: [specific operational or compliance reason this failure mode matters for this process type]

Minimum 1 exception trace per phase. Minimum 3 exception traces in total across all phases.

**SECTION B — STATE TRANSITION TABLE**

| S-ID | State Name | Entry Condition | Exits | Owner (R-ID) | Type |
|------|-----------|-----------------|-------|--------------|------|

Rules:
- Every state must have a named Entry Condition. "Ready" or "Previous step complete" fails.
- Every Exit must reference a destination S-ID or carry the label TERMINAL.
- Type values: NORMAL / DECISION / PARALLEL-FORK / PARALLEL-JOIN / EXCEPTION / TERMINAL

**Decision Supplement Blocks** (one per DECISION-type state in this phase):

> **DS-[S-ID] — [State Name]**
> - Condition: [the rule or threshold being evaluated at this decision point]
> - Owner: R-[ID] ([role name from Role Registry])
> - Branch A ([condition outcome]): → S-[ID] ([state name])
> - Branch B ([condition outcome]): → S-[ID] ([state name]) or TERMINAL
> - Fallback: [action if condition cannot be evaluated — who is notified, what state is entered]

**PHASE EXIT GATE**

> This gate must be completed before the next phase begins. Required outputs listed here
> become the Entry Condition prerequisites for PHASE [N+1]'s PHASE ENTRY CONTRACT.

- Exit Condition: [what the phase must have produced to be considered complete]
- Required outputs: [named artifacts, decisions, or state records that must exist]
- Exit verification: R-[ID] ([role name]) confirms all required outputs are present
- Blocking condition: [if required outputs are absent — re-entry path or escalation]

---

[Repeat Phase Structure for each phase. Minimum 2 phases required.]

---

### Parallel Path Modeling

Identify at least one fork/join with labeled join condition:

- **FORK at**: S-[ID] ([state name])
- **Branch 1**: [path description — states traversed in sequence]
- **Branch 2**: [path description — states traversed in sequence]
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
- Every AT-RISK row must carry a Bottleneck Ref citing a B-NN from Bottleneck Analysis below
- Minimum 3 annotated rows; at least 1 must be AT-RISK

---

### Bottleneck Analysis

> **PREAMBLE**: This section identifies where delays accumulate (bottlenecks) and steps missing
> from the current model (gaps). Each bottleneck Cause field must cite (1) at least one incumbent
> failure mode (IM-ID) from INCUMBENT BASELINE and (2) the blocking role (R-ID) from the Role
> Sequence Schedule when role unavailability contributes to the delay.
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
> Anti-embedding: Do not embed CHAIN STATUS as a line inside the SLA ANALYSIS section.
> Declare CHAIN STATUS in its own dedicated top-level section after SLA ANALYSIS.

**SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field.**

---

**B-01 — [Bottleneck Name]**

- Cause: [specific cause of delay — cite the incumbent failure mode (IM-ID) that this bottleneck
  perpetuates or worsens, and the blocking role (R-ID) from the Role Sequence Schedule if
  role unavailability contributes. Example: "IM-01 (manual spreadsheet reconciliation) combined
  with R-02 unavailable during period-close peak — causes queue accumulation at S-05"]
- Impact: [downstream state, SLA node, or adjacent process affected]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row that cites B-01 as causal source. Example: `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`]

---

**B-02 — [Bottleneck Name]**

- Cause: [specific cause — cite IM-ID and blocking R-ID from Role Sequence Schedule]
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row citing B-02. Example: `"S-07: Invoice Matching -- AT-RISK, causal source: B-02"`]

---

**Gap Identification**

> MISSING: [step name] — [rationale: why it belongs in this process model; what failure mode its
> absence enables; which phase it belongs in; whether it would reduce an IM-ID failure mode if present]

---

### CHAIN STATUS

> Anti-embedding: Do not embed CHAIN STATUS as a line inside the SLA ANALYSIS section.
> This section is a dedicated top-level output element declared after SLA ANALYSIS.

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA→B): [confirm that every AT-RISK SLA row cites a B-ID; list the AT-RISK rows and their cited B-IDs, or name the unresolved row if OPEN]
- Backward (B→SLA): [confirm that every B-NN entry names affected SLA nodes; list each B-ID and the AT-RISK rows it affects, or name the missing citation if OPEN]
- Gap (if OPEN): [name the specific unresolved direction and the unlinked entry]

---

### Terminal States

| Terminal | Type | Reached From |
|----------|------|-------------|
| [success terminal name] | SUCCESS | [branch/state that reaches it] |
| [failure terminal name] | FAILURE | [branch/state that reaches it] |
| [cancel terminal name] | CANCEL | [branch/state that reaches it] |

> Completeness check: Every exit branch in every SECTION B state table must reach one of the
> declared terminals above. No branch may end at a non-terminal state without an explicit
> `continues-via: S-[ID]` pointer. Fail if any branch ends mid-flow.

---
---

## V-02 — Axis B: Phase-Exit Gate Bottleneck Linkage

**Variation axis**: Lifecycle emphasis — each PHASE EXIT GATE block adds a `Blocked bottleneck:`
sub-field that names the B-ID when a declared bottleneck can delay phase exit, or NONE when no
declared bottleneck blocks it. This is a structural forward-reference field: the exit gate is
produced before the Bottleneck Analysis section, so the B-ID cited in the gate creates a
verifiable linkage point that a reviewer can string-compare against the Bottleneck Analysis.

**Hypothesis**: C-36 requires the PHASE EXIT GATE to exist with named sub-fields, but does not
require those sub-fields to reference B-IDs. Adding `Blocked bottleneck: B-02 or NONE` as a
named sub-field creates a Phase→B-NN traceability direction: "B-02" in the exit gate's Blocking
condition and "B-02" in the bottleneck block's identifier are consistent by string comparison.
When the exit gate's Required outputs field names an artifact and the Blocking condition names
the B-ID that delays it, a reviewer can trace: phase-exit requirement → blocking bottleneck →
SLA at-risk node → incumbent failure mode root cause. This four-link chain is the C-37 probe.

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete this section before the Role Registry Gate. Establishes the manual / status-quo
> version of this process. Every B-NN Cause field below must cite at least one IM-ID from
> this table. The quantified metric must appear before the first PHASE block in document order.

**Process type**: [L2O / P2P / Period Close / Case Lifecycle — auto-detect from {Topic}]

**Incumbent description**: [1–3 sentences: tools, handoff mechanisms, storage, initiator]

**Incumbent failure modes** (assign IM-ID to each):

| IM-ID | Failure Mode | Frequency | Downstream Effect |
|-------|-------------|-----------|------------------|
| IM-01 | [specific recurring failure in the manual process] | [daily / per-cycle / per-exception] | [what breaks downstream] |
| IM-02 | [second distinct failure mode] | [frequency] | [downstream effect] |

**Cost of no action**: [Quantified metric — name the measure with its current-state value or
rate. Must appear before PHASE 1 begins. Example: "Average approval cycle time: 5.8 days vs
3-day SLA target" or "Duplicate invoice rate: 7.3% per period".]

---

### Role Registry Gate

> GATE BLOCK: Complete this section before tracing any state. Do not begin any phase until
> all R-ID entries are filled and all three anti-generic checks are satisfied.

| R-ID | Role | Function |
|------|------|----------|
| R-01 | [domain-specific role] | [named responsibility] |
| R-02 | [domain-specific role] | [named responsibility] |
| R-03 | [domain-specific role] | [named responsibility] |

Anti-generic validation (all three must clear before proceeding):
- [ ] No entry uses "Approver" without a domain qualifier
- [ ] No entry uses "Owner" without a named responsibility
- [ ] Each R-ID appears in at least one Decision Supplement block and in at least one PHASE EXIT GATE Exit verification field below

Role set by process type:
- L2O → Sales Rep / Sales Manager / Finance Credit Analyst / Legal Counsel / Fulfillment Coordinator
- P2P → Procurement Officer / Accounts Payable Specialist / Receiving Dock Supervisor / Finance Controller
- Period Close → Finance Analyst / GL Manager / Controller / External Auditor
- Case Lifecycle → Support Engineer / Case Manager / Legal Counsel / Operations Coordinator

---

### Phase Structure

For each phase in the lifecycle, produce the following five blocks in document order:

---

**PHASE [N] — [PHASE NAME]**

**PHASE ENTRY CONTRACT**

> This gate must be completed before SECTION A or SECTION B for this phase.
> Entry Condition must reference the prior phase's PHASE EXIT GATE "Required outputs" by name.

- Entry Condition: [specific output from prior phase exit gate that must exist; name the artifact]
- Pre-condition check: R-[ID] ([role name]) — [how they verify the entry condition is met]
- Blocking condition: [if entry condition is not met: state entered, role notified, re-entry path]

**SECTION A — EXCEPTION TRACES**

For each exception trace originating in this phase:

> **EX-[Phase#][Letter] — [Exception Name]**
> - Trigger: [specific condition that causes deviation — name the state, threshold, or missing input]
> - Trace: [path of states traversed from trigger to resolution or terminal; cite S-IDs in sequence]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state name] or [continues-via: S-[ID]]
> - Why Problematic: [specific operational or compliance reason for this process type]

Minimum 1 exception per phase. Minimum 3 total across all phases.

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
> - Owner: R-[ID] ([role name])
> - Branch A ([outcome]): → S-[ID] ([state name])
> - Branch B ([outcome]): → S-[ID] ([state name]) or TERMINAL
> - Fallback: [action if condition cannot be evaluated]

**PHASE EXIT GATE**

> This gate must be completed before the next phase begins. Required outputs become Entry
> Condition prerequisites for PHASE [N+1]. The `Blocked bottleneck:` field names the B-ID
> that can delay phase exit, or NONE if no declared bottleneck blocks it. Use the B-ID that
> will be assigned in Bottleneck Analysis below — this is a forward reference.

- Exit Condition: [what the phase must have produced to be considered complete]
- Required outputs: [named artifacts, decisions, or state records that must exist]
- Exit verification: R-[ID] ([role name]) confirms all required outputs are present
- Blocking condition: [if required outputs are absent — re-entry path or escalation]
- Blocked bottleneck: [B-NN that can delay this phase's exit, or NONE. Example: "B-02 — invoice matching queue blocks exit until matching state completes." String must match the B-ID declared in Bottleneck Analysis below.]

---

[Repeat Phase Structure for each phase. Minimum 2 phases required.]

---

### Parallel Path Modeling

- **FORK at**: S-[ID] ([state name])
- **Branch 1**: [states traversed]
- **Branch 2**: [states traversed]
- **JOIN at**: S-[ID] ([join state name])
- **Join Condition**: AND-join / OR-join — specify which and explain why

---

### Edge Case Enumeration

At least three edge cases distinct from SECTION A exception flows:

> **EC-[N] — [Edge Case Name]**
> - Triggering Condition: [specific scenario]
> - Why Problematic: [specific reason outside documented handling]
> - Correct Response: R-[ID] ([role name]) — [specific correct action]

---

### Cross-Process Interaction Modeling

> **CROSS-PROCESS HANDOFF — {Topic} lifecycle → [adjacent process name]**
> - Sending State: S-[ID] ([state name])
> - Receiving Process: [adjacent process name]
> - Data Payload: [named fields or record types]
> - Expected Acknowledgment: [confirmation signal]
> - Failure Mode: [what happens if acknowledgment is not received]
> - Owner: R-[ID] ([role name])

---

### SLA and Timing Analysis

| S-ID | State Name | SLA Target | Typical Duration | Status | Bottleneck Ref |
|------|-----------|------------|------------------|--------|----------------|
| | | | | AT-RISK / ON-TRACK | B-NN (if AT-RISK) |

Minimum 3 annotated rows; at least 1 AT-RISK. Every AT-RISK row must cite a B-NN.

---

### Bottleneck Analysis

> **PREAMBLE**: Each bottleneck Cause field must cite at least one IM-ID from INCUMBENT BASELINE.
> The B-IDs assigned here (B-01, B-02, ...) must match the B-IDs cited in the PHASE EXIT GATE
> `Blocked bottleneck:` fields above — string consistency is the verification property.
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
> Anti-embedding: Do not embed CHAIN STATUS as a line inside the SLA ANALYSIS section.
> Declare CHAIN STATUS in its own dedicated top-level section after SLA ANALYSIS.

**SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field.**

---

**B-01 — [Bottleneck Name]**

- Cause: [specific cause — cite IM-ID from INCUMBENT BASELINE. Example: "IM-01 (manual GL
  reconciliation without automated matching) causes queue accumulation at period-close review"]
- Impact: [downstream state, SLA node, or adjacent process affected]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row citing B-01. Example: `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`]

---

**B-02 — [Bottleneck Name]**

- Cause: [specific cause — cite IM-ID from INCUMBENT BASELINE]
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row citing B-02. Example: `"S-07: Invoice Matching -- AT-RISK, causal source: B-02"`]

---

**Gap Identification**

> MISSING: [step name] — [rationale: why it belongs; what failure mode its absence enables;
> which phase it belongs in]

---

### CHAIN STATUS

> Anti-embedding: Do not embed CHAIN STATUS as a line inside the SLA ANALYSIS section.
> This section is a dedicated top-level output element declared after SLA ANALYSIS.

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA→B): [every AT-RISK SLA row cites a B-ID; list rows and B-IDs or name gap]
- Backward (B→SLA): [every B-NN entry names affected SLA nodes; list or name gap]
- Gap (if OPEN): [name unresolved direction and unlinked entry]

---

### Terminal States

| Terminal | Type | Reached From |
|----------|------|-------------|
| [success terminal name] | SUCCESS | [branch/state] |
| [failure terminal name] | FAILURE | [branch/state] |
| [cancel terminal name] | CANCEL | [branch/state] |

> Every exit in every SECTION B state table must reach a declared terminal. No branch may end
> at a non-terminal state without an explicit `continues-via: S-[ID]` pointer.

---
---

## V-03 — Axis C: BOTTLENECK IMPACT MATRIX (Output Format)

**Variation axis**: Output format — after Gap Identification, a BOTTLENECK IMPACT MATRIX is
declared as a named structural element. It consolidates all B-NN→IM-ID→SLA→Phase linkages into
a single cross-reference table with columns [B-ID | Phase Affected | IM-ID Source | SLA Node |
Time Cost | Mitigation Owner (R-ID)]. The matrix is a second-order artifact: it does not replace
per-block Evidence fields, but assembles their citations into a dense, scannable form.

**Hypothesis**: Per-block Evidence fields (C-19, C-28) and the Baseline→B-NN Cause citations
(C-34) are distributed across individual B-NN blocks. A reviewer validating C-14/C-16 must
scan all blocks to verify bidirectionality. A consolidated matrix that lists every
[B-ID | IM-ID | SLA node] in one table makes cross-section traceability density visible at a
glance — a single wrong or missing row is immediately apparent. This may surface a C-37+ signal
around consolidated cross-reference density as a named structural artifact distinct from
per-block citations: the matrix exists as a completeness contract, not just a format convenience.

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete this section before the Role Registry Gate. Every B-NN Cause field and every row
> in the BOTTLENECK IMPACT MATRIX must cite at least one IM-ID from this table.
> Quantified metric must appear before PHASE 1 in document order.

**Process type**: [L2O / P2P / Period Close / Case Lifecycle — auto-detect from {Topic}]

**Incumbent description**: [1–3 sentences: tools, handoff mechanisms, storage, initiator]

**Incumbent failure modes** (assign IM-ID to each):

| IM-ID | Failure Mode | Frequency | Downstream Effect |
|-------|-------------|-----------|------------------|
| IM-01 | [specific recurring failure] | [frequency] | [downstream effect] |
| IM-02 | [second failure mode] | [frequency] | [downstream effect] |

**Cost of no action**: [Quantified metric with current-state value or rate, declared before
PHASE 1 begins. Example: "Purchase order cycle time: 8.1 days against 5-day target" or
"Manual matching error rate: 12% per period, generating 40+ exception tickets."]

---

### Role Registry Gate

> GATE BLOCK: Complete before tracing any state. All R-ID entries filled; anti-generic checks passed.

| R-ID | Role | Function |
|------|------|----------|
| R-01 | [domain-specific role] | [named responsibility] |
| R-02 | [domain-specific role] | [named responsibility] |
| R-03 | [domain-specific role] | [named responsibility] |

Anti-generic validation:
- [ ] No entry uses "Approver" without a domain qualifier
- [ ] No entry uses "Owner" without a named responsibility
- [ ] Each R-ID appears in at least one Decision Supplement block and in the BOTTLENECK IMPACT MATRIX Mitigation Owner column below

Role set by process type:
- L2O → Sales Rep / Sales Manager / Finance Credit Analyst / Legal Counsel / Fulfillment Coordinator
- P2P → Procurement Officer / Accounts Payable Specialist / Receiving Dock Supervisor / Finance Controller
- Period Close → Finance Analyst / GL Manager / Controller / External Auditor
- Case Lifecycle → Support Engineer / Case Manager / Legal Counsel / Operations Coordinator

---

### Phase Structure

For each phase, produce the following five blocks in document order:

---

**PHASE [N] — [PHASE NAME]**

**PHASE ENTRY CONTRACT**

- Entry Condition: [specific output from prior phase exit gate; name the artifact]
- Pre-condition check: R-[ID] ([role name]) — [verification method]
- Blocking condition: [state entered and role notified if entry condition is not met]

**SECTION A — EXCEPTION TRACES**

> **EX-[Phase#][Letter] — [Exception Name]**
> - Trigger: [specific deviation condition]
> - Trace: [state path; cite S-IDs]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state] or [continues-via: S-[ID]]
> - Why Problematic: [process-specific operational or compliance reason]

Minimum 1 per phase; 3 total minimum.

**SECTION B — STATE TRANSITION TABLE**

| S-ID | State Name | Entry Condition | Exits | Owner (R-ID) | Type |
|------|-----------|-----------------|-------|--------------|------|

Rules:
- Named Entry Condition required. "Ready" fails.
- Every Exit → destination S-ID or TERMINAL.
- Type: NORMAL / DECISION / PARALLEL-FORK / PARALLEL-JOIN / EXCEPTION / TERMINAL

**Decision Supplement Blocks** (one per DECISION-type state):

> **DS-[S-ID] — [State Name]**
> - Condition: [rule or threshold]
> - Owner: R-[ID] ([role name])
> - Branch A ([outcome]): → S-[ID]
> - Branch B ([outcome]): → S-[ID] or TERMINAL
> - Fallback: [action if condition cannot be evaluated]

**PHASE EXIT GATE**

- Exit Condition: [what the phase must have produced]
- Required outputs: [named artifacts or state records]
- Exit verification: R-[ID] ([role name]) confirms all required outputs are present
- Blocking condition: [re-entry path or escalation if outputs are absent]

---

[Repeat Phase Structure for each phase. Minimum 2 phases required.]

---

### Parallel Path Modeling

- **FORK at**: S-[ID] ([state name])
- **Branch 1**: [states traversed]
- **Branch 2**: [states traversed]
- **JOIN at**: S-[ID] ([join state name])
- **Join Condition**: AND-join / OR-join — specify and explain why

---

### Edge Case Enumeration

Three or more edge cases distinct from SECTION A:

> **EC-[N] — [Edge Case Name]**
> - Triggering Condition: [specific scenario]
> - Why Problematic: [specific reason outside documented handling]
> - Correct Response: R-[ID] ([role name]) — [specific action]

---

### Cross-Process Interaction Modeling

> **CROSS-PROCESS HANDOFF — {Topic} lifecycle → [adjacent process name]**
> - Sending State: S-[ID]
> - Receiving Process: [name]
> - Data Payload: [fields or record types]
> - Expected Acknowledgment: [confirmation signal]
> - Failure Mode: [if acknowledgment not received]
> - Owner: R-[ID]

---

### SLA and Timing Analysis

| S-ID | State Name | SLA Target | Typical Duration | Status | Bottleneck Ref |
|------|-----------|------------|------------------|--------|----------------|
| | | | | AT-RISK / ON-TRACK | B-NN (if AT-RISK) |

Minimum 3 rows; at least 1 AT-RISK citing a B-NN.

---

### Bottleneck Analysis

> **PREAMBLE**: Each B-NN Cause field must cite at least one IM-ID from INCUMBENT BASELINE.
> After Gap Identification, produce a BOTTLENECK IMPACT MATRIX — a consolidated cross-reference
> table assembling every B-NN→IM-ID→SLA→Phase linkage. The matrix must be consistent with the
> per-block Evidence fields: every row in the matrix corresponds to a declared B-NN block, and
> every IM-ID in the matrix appears in that block's Cause field.
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
> Anti-embedding: Do not embed CHAIN STATUS as a line inside the SLA ANALYSIS section.
> Declare CHAIN STATUS in its own dedicated top-level section after SLA ANALYSIS.

**SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field.**

---

**B-01 — [Bottleneck Name]**

- Cause: [specific cause — cite IM-ID. Example: "IM-02 (email-based approval routing) delays
  credit review because approvals arrive without SLA timestamp, causing queue prioritization
  failure at S-05"]
- Impact: [downstream state, SLA node, or adjacent process]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List AT-RISK SLA rows citing B-01. Example: `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`]

---

**B-02 — [Bottleneck Name]**

- Cause: [specific cause — cite IM-ID]
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List AT-RISK SLA rows citing B-02. Example: `"S-07: Invoice Matching -- AT-RISK, causal source: B-02"`]

---

**Gap Identification**

> MISSING: [step name] — [rationale: why it belongs; failure mode enabled by absence; which phase]

---

**BOTTLENECK IMPACT MATRIX**

> This matrix assembles every B-NN→IM-ID→SLA→Phase linkage into a consolidated cross-reference
> artifact. Every row corresponds to a declared B-NN block. Every IM-ID in this matrix must
> appear in that block's Cause field (string consistency required). Every SLA node in this
> matrix must appear in the SLA Analysis table with AT-RISK status (string consistency required).
>
> This matrix is a completeness contract, not a summary: if a B-NN block's IM-ID citation is
> absent from this matrix, the matrix fails. If an AT-RISK SLA node is not represented, the
> matrix fails.

| B-ID | Phase Affected | IM-ID Source | SLA Node (S-ID) | Time Cost | Mitigation Owner (R-ID) |
|------|---------------|-------------|-----------------|-----------|------------------------|
| B-01 | Phase [N] | IM-[NN] | S-[ID] ([state name]) | [quantified delay, e.g., +2.1 days] | R-[ID] ([role name]) |
| B-02 | Phase [N] | IM-[NN] | S-[ID] ([state name]) | [quantified delay] | R-[ID] ([role name]) |

Rules:
- Every declared B-NN block must appear as a row.
- IM-ID must match the literal string in that B-NN's Cause field.
- SLA Node must match an AT-RISK row in SLA Analysis by S-ID string.
- Time Cost must be quantified (days, hours, or % of SLA target); "significant" fails.
- Mitigation Owner must be an R-ID from the Role Registry.

---

### CHAIN STATUS

> Anti-embedding: Dedicated top-level section. Not embedded in SLA ANALYSIS.

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA→B): [every AT-RISK row cites a B-ID; list or name gap]
- Backward (B→SLA): [every B-NN names affected SLA nodes; list or name gap]
- Matrix consistency: [BOTTLENECK IMPACT MATRIX IM-ID and SLA-node columns consistent with per-block fields; name any inconsistency]
- Gap (if OPEN): [unresolved direction and unlinked entry]

---

### Terminal States

| Terminal | Type | Reached From |
|----------|------|-------------|
| [success terminal] | SUCCESS | [branch/state] |
| [failure terminal] | FAILURE | [branch/state] |
| [cancel terminal] | CANCEL | [branch/state] |

> Every exit in every SECTION B state table must reach a declared terminal. No branch may end
> at a non-terminal state without `continues-via: S-[ID]`.

---
---

## V-04 — Axes A + B: Role Sequence + Exit Gate Bottleneck Linkage

**Variation axes**: A (Role Sequence Schedule) + B (Phase-exit gate `Blocked bottleneck:` field)

**Hypothesis**: Role sequence anchors when each role is active; the exit gate bottleneck field
anchors which B-ID delays each phase's exit. Together they create a compound traceability chain:
Role Sequence Schedule shows R-02 is the phase-2 owner; PHASE EXIT GATE's Blocked bottleneck
field shows B-02 delays phase-2 exit; B-02's Cause field cites IM-01 as root cause. The three
artifacts form a Role→Phase→B-NN→IM-ID chain verifiable by string comparison at each link.
This is the maximum traceability configuration short of the impact matrix, and the most direct
probe for C-37 (exit gate B-ID forward reference) in combination with the role-sequence direction.

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete before the Role Registry Gate. Every B-NN Cause field must cite IM-ID and blocking
> R-ID (from Role Sequence Schedule). Quantified metric must precede PHASE 1 in document order.

**Process type**: [L2O / P2P / Period Close / Case Lifecycle — auto-detect from {Topic}]

**Incumbent description**: [1–3 sentences: tools, handoffs, storage, initiator]

**Incumbent failure modes**:

| IM-ID | Failure Mode | Frequency | Downstream Effect |
|-------|-------------|-----------|------------------|
| IM-01 | [specific failure] | [frequency] | [downstream effect] |
| IM-02 | [second failure] | [frequency] | [downstream effect] |

**Cost of no action**: [Named measure with current-state value or rate, declared before PHASE 1.
Both IM-IDs above must be reachable from at least one B-NN Cause field below.]

---

### Role Registry Gate

> GATE BLOCK: Complete before Role Sequence Schedule and before tracing any state.

| R-ID | Role | Function |
|------|------|----------|
| R-01 | [domain-specific role] | [named responsibility] |
| R-02 | [domain-specific role] | [named responsibility] |
| R-03 | [domain-specific role] | [named responsibility] |

Anti-generic validation:
- [ ] No entry uses "Approver" without a domain qualifier
- [ ] No entry uses "Owner" without a named responsibility
- [ ] Each R-ID appears in at least one Decision Supplement block, the Role Sequence Schedule, and at least one PHASE EXIT GATE Exit verification or Blocked bottleneck field

Role set by process type:
- L2O → Sales Rep / Sales Manager / Finance Credit Analyst / Legal Counsel / Fulfillment Coordinator
- P2P → Procurement Officer / Accounts Payable Specialist / Receiving Dock Supervisor / Finance Controller
- Period Close → Finance Analyst / GL Manager / Controller / External Auditor
- Case Lifecycle → Support Engineer / Case Manager / Legal Counsel / Operations Coordinator

---

### Role Sequence Schedule

> Declared after Role Registry Gate and before PHASE 1. Maps each R-ID to its active phases,
> activation trigger, handoff trigger, and any parallel windows. B-NN Cause fields must cite
> both IM-ID and the blocking R-ID from this schedule when role unavailability contributes.

| Phase | Primary Owner (R-ID) | Activation Trigger | Handoff Trigger | Parallel Role (R-ID) | Parallel Window |
|-------|---------------------|-------------------|-----------------|----------------------|----------------|
| Phase 1 | R-[ID] | [external event or prior artifact] | [specific completion condition] | R-[ID] or NONE | [concurrent window or NONE] |
| Phase 2 | R-[ID] | [handoff from phase 1] | [completion condition] | R-[ID] or NONE | [concurrent window or NONE] |

Rules:
- Primary Owner required per phase; activation and handoff triggers must be specific.
- Parallel windows must state start/end states (S-IDs) when known.
- Every R-ID in this schedule must match an entry in the Role Registry Gate.

---

### Phase Structure

For each phase, produce the following five blocks in document order:

---

**PHASE [N] — [PHASE NAME]**

**PHASE ENTRY CONTRACT**

> Entry Condition must reference the prior phase's PHASE EXIT GATE "Required outputs" by name.

- Entry Condition: [named artifact from prior phase exit gate]
- Pre-condition check: R-[ID] ([role name from Role Sequence Schedule]) — [verification method]
- Blocking condition: [state entered and role notified if entry condition not met]

**SECTION A — EXCEPTION TRACES**

> **EX-[Phase#][Letter] — [Exception Name]**
> - Trigger: [specific deviation condition]
> - Trace: [state path; cite S-IDs]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state] or [continues-via: S-[ID]]
> - Why Problematic: [process-specific reason]

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

> `Blocked bottleneck:` names the B-ID that can delay this exit, or NONE. The B-ID must
> string-match the identifier declared in Bottleneck Analysis below. This is a forward reference:
> assign the B-ID now and ensure the Bottleneck Analysis block uses the same identifier.

- Exit Condition: [what the phase must produce to be complete]
- Required outputs: [named artifacts, decisions, or state records]
- Exit verification: R-[ID] ([role name from Role Sequence Schedule, primary owner of this phase]) confirms all outputs present
- Blocking condition: [re-entry or escalation if outputs are absent]
- Blocked bottleneck: [B-NN that can delay this phase's exit, or NONE. Cite the B-ID that will appear in Bottleneck Analysis. Example: "B-01 — manual credit spreadsheet delays approval exit until R-02 manually reconciles."]

---

[Repeat Phase Structure for each phase. Minimum 2 phases required.]

---

### Parallel Path Modeling

- **FORK at**: S-[ID]
- **Branch 1**: [states traversed]
- **Branch 2**: [states traversed]
- **JOIN at**: S-[ID]
- **Join Condition**: AND-join / OR-join — specify and explain

---

### Edge Case Enumeration

Three or more, distinct from SECTION A:

> **EC-[N] — [Edge Case Name]**
> - Triggering Condition: [specific scenario]
> - Why Problematic: [specific consequence]
> - Correct Response: R-[ID] — [specific action]

---

### Cross-Process Interaction Modeling

> **CROSS-PROCESS HANDOFF — {Topic} → [adjacent process]**
> - Sending State: S-[ID]; Receiving Process: [name]; Data Payload: [fields]; Expected Acknowledgment: [signal]
> - Failure Mode: [if no acknowledgment]; Owner: R-[ID]

---

### SLA and Timing Analysis

| S-ID | State Name | SLA Target | Typical Duration | Status | Bottleneck Ref |
|------|-----------|------------|------------------|--------|----------------|
| | | | | AT-RISK / ON-TRACK | B-NN (if AT-RISK) |

Minimum 3 rows; at least 1 AT-RISK citing a B-NN.

---

### Bottleneck Analysis

> **PREAMBLE**: Each B-NN Cause field must cite (1) the IM-ID from INCUMBENT BASELINE and (2)
> the blocking R-ID from the Role Sequence Schedule when role unavailability contributes.
> B-IDs assigned here must match the `Blocked bottleneck:` fields in PHASE EXIT GATEs above.
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

- Cause: [specific cause — cite IM-ID AND blocking R-ID from Role Sequence Schedule when
  applicable. Example: "IM-01 (spreadsheet-based GL reconciliation) combined with R-02 (GL
  Manager) peak-period unavailability — causes queue accumulation at S-05. R-02 is Phase 2
  primary owner (Role Sequence Schedule); their unavailability directly delays the phase-2 exit."]
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List AT-RISK SLA rows citing B-01. Example: `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`]

---

**B-02 — [Bottleneck Name]**

- Cause: [specific cause — cite IM-ID and blocking R-ID if applicable]
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List AT-RISK SLA rows citing B-02. Example: `"S-07: Invoice Matching -- AT-RISK, causal source: B-02"`]

---

**Gap Identification**

> MISSING: [step name] — [rationale: why it belongs; failure mode enabled; which phase;
> which IM-ID its absence perpetuates]

---

### CHAIN STATUS

> Anti-embedding: Dedicated top-level section. Not embedded in SLA ANALYSIS.

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA→B): [every AT-RISK row cites B-ID; enumerate or name gap]
- Backward (B→SLA): [every B-NN names SLA nodes; enumerate or name gap]
- Exit gate consistency: [every PHASE EXIT GATE `Blocked bottleneck:` B-ID matches a declared B-NN block; name any mismatch]
- Gap (if OPEN): [unresolved direction and unlinked entry]

---

### Terminal States

| Terminal | Type | Reached From |
|----------|------|-------------|
| [success terminal] | SUCCESS | [branch/state] |
| [failure terminal] | FAILURE | [branch/state] |
| [cancel terminal] | CANCEL | [branch/state] |

> Every exit branch must reach a declared terminal. No mid-flow endings without `continues-via:`.

---
---

## V-05 — Axes A + B + C: Role Sequence + Exit Gate Bottleneck Linkage + BOTTLENECK IMPACT MATRIX

**Variation axes**: A (Role Sequence Schedule) + B (Phase-exit gate `Blocked bottleneck:`) + C (BOTTLENECK IMPACT MATRIX)

**Hypothesis**: All three new structural mechanisms compose into a multi-directional cross-reference
system: (1) Role Sequence Schedule makes Role→Phase ownership traceable; (2) PHASE EXIT GATE
`Blocked bottleneck:` makes Phase→B-NN linkage traceable; (3) BOTTLENECK IMPACT MATRIX makes
B-NN→IM-ID→SLA→Phase density scannable in one artifact. Together, a reviewer can traverse the
full chain — Role → Phase → B-NN → IM-ID → SLA node — without inference at any step, each link
verifiable by string comparison. If any of the three new axes independently surfaces a C-37+ signal,
their combination should saturate it; if they compose into a new signal requiring all three, V-05
is the only variation that can crack it.

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete before Role Registry Gate. Every B-NN Cause field and every BOTTLENECK IMPACT MATRIX
> row must cite at least one IM-ID from this table. Quantified metric must precede PHASE 1.

**Process type**: [L2O / P2P / Period Close / Case Lifecycle — auto-detect from {Topic}]

**Incumbent description**: [1–3 sentences: tools, handoffs, storage, initiator]

**Incumbent failure modes**:

| IM-ID | Failure Mode | Frequency | Downstream Effect |
|-------|-------------|-----------|------------------|
| IM-01 | [specific failure] | [frequency] | [downstream effect] |
| IM-02 | [second failure] | [frequency] | [downstream effect] |

**Cost of no action**: [Named measure with current-state value or rate. Must precede PHASE 1.
Example: "Support case mean-time-to-resolve: 11.4 days vs 7-day SLA target" or
"Invoice exception rate: 9.2% per period, each exception averaging 4.3 days to resolve."]

---

### Role Registry Gate

> GATE BLOCK: Complete before Role Sequence Schedule and all phase tracing.

| R-ID | Role | Function |
|------|------|----------|
| R-01 | [domain-specific role] | [named responsibility] |
| R-02 | [domain-specific role] | [named responsibility] |
| R-03 | [domain-specific role] | [named responsibility] |

Anti-generic validation:
- [ ] No entry uses "Approver" without a domain qualifier
- [ ] No entry uses "Owner" without a named responsibility
- [ ] Each R-ID appears in at least one Decision Supplement block, the Role Sequence Schedule, a PHASE EXIT GATE Exit verification or Blocked bottleneck field, and the BOTTLENECK IMPACT MATRIX Mitigation Owner column

Role set by process type:
- L2O → Sales Rep / Sales Manager / Finance Credit Analyst / Legal Counsel / Fulfillment Coordinator
- P2P → Procurement Officer / Accounts Payable Specialist / Receiving Dock Supervisor / Finance Controller
- Period Close → Finance Analyst / GL Manager / Controller / External Auditor
- Case Lifecycle → Support Engineer / Case Manager / Legal Counsel / Operations Coordinator

---

### Role Sequence Schedule

> Declared after Role Registry Gate, before PHASE 1. Maps each R-ID to active phases,
> activation trigger, handoff trigger, and parallel windows. B-NN Cause fields and the
> BOTTLENECK IMPACT MATRIX must cite the blocking R-ID from this schedule when role
> unavailability contributes to delay.

| Phase | Primary Owner (R-ID) | Activation Trigger | Handoff Trigger | Parallel Role (R-ID) | Parallel Window |
|-------|---------------------|-------------------|-----------------|----------------------|----------------|
| Phase 1 | R-[ID] | [external event or artifact] | [specific completion condition] | R-[ID] or NONE | [concurrent window or NONE] |
| Phase 2 | R-[ID] | [handoff from phase 1] | [completion condition] | R-[ID] or NONE | [concurrent window or NONE] |

Rules:
- Primary Owner required per phase; triggers must be specific.
- Every R-ID here must match an entry in the Role Registry Gate.

---

### Phase Structure

For each phase, produce the following five blocks in document order:

---

**PHASE [N] — [PHASE NAME]**

**PHASE ENTRY CONTRACT**

- Entry Condition: [named artifact from prior phase exit gate's Required outputs field]
- Pre-condition check: R-[ID] ([role name from Role Sequence Schedule, primary owner]) — [verification method]
- Blocking condition: [state entered and role notified if entry condition not met]

**SECTION A — EXCEPTION TRACES**

> **EX-[Phase#][Letter] — [Exception Name]**
> - Trigger: [specific deviation condition — name state, threshold, or missing input]
> - Trace: [state path; cite S-IDs in sequence]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state] or [continues-via: S-[ID]]
> - Why Problematic: [process-specific operational or compliance reason]

Minimum 1 per phase; 3 total minimum.

**SECTION B — STATE TRANSITION TABLE**

| S-ID | State Name | Entry Condition | Exits | Owner (R-ID) | Type |
|------|-----------|-----------------|-------|--------------|------|

Rules: Named Entry Condition required; Exits → S-ID or TERMINAL; standard Type values.

**Decision Supplement Blocks** (one per DECISION-type state):

> **DS-[S-ID] — [State Name]**
> - Condition: [rule or threshold]
> - Owner: R-[ID] ([role from Role Registry])
> - Branch A ([outcome]): → S-[ID]
> - Branch B ([outcome]): → S-[ID] or TERMINAL
> - Fallback: [action if undecidable]

**PHASE EXIT GATE**

> `Blocked bottleneck:` cites the B-ID that can delay this exit (or NONE). B-ID must
> string-match Bottleneck Analysis identifier and BOTTLENECK IMPACT MATRIX B-ID column.
> `Exit verification` role must match the Phase Primary Owner from the Role Sequence Schedule.

- Exit Condition: [what the phase must produce to be complete]
- Required outputs: [named artifacts, decisions, or state records]
- Exit verification: R-[ID] ([role name — must match Role Sequence Schedule primary owner for this phase]) confirms all outputs present
- Blocking condition: [re-entry or escalation if outputs absent]
- Blocked bottleneck: [B-NN or NONE. B-ID must appear in Bottleneck Analysis and BOTTLENECK IMPACT MATRIX. Example: "B-02 — manual three-way match delay blocks receipt confirmation exit until R-03 resolves discrepancy."]

---

[Repeat Phase Structure for each phase. Minimum 2 phases required.]

---

### Parallel Path Modeling

- **FORK at**: S-[ID]
- **Branch 1**: [states traversed]
- **Branch 2**: [states traversed]
- **JOIN at**: S-[ID]
- **Join Condition**: AND-join / OR-join — specify and explain

---

### Edge Case Enumeration

Three or more, distinct from SECTION A:

> **EC-[N] — [Edge Case Name]**
> - Triggering Condition: [specific scenario]
> - Why Problematic: [specific consequence]
> - Correct Response: R-[ID] — [specific action]

---

### Cross-Process Interaction Modeling

> **CROSS-PROCESS HANDOFF — {Topic} → [adjacent process]**
> - Sending State: S-[ID]; Receiving Process: [name]; Data Payload: [fields]; Expected Acknowledgment: [signal]
> - Failure Mode: [if acknowledgment absent]; Owner: R-[ID]

---

### SLA and Timing Analysis

| S-ID | State Name | SLA Target | Typical Duration | Status | Bottleneck Ref |
|------|-----------|------------|------------------|--------|----------------|
| | | | | AT-RISK / ON-TRACK | B-NN (if AT-RISK) |

Minimum 3 rows; at least 1 AT-RISK citing a B-NN.

---

### Bottleneck Analysis

> **PREAMBLE**: Each B-NN Cause field must cite (1) IM-ID from INCUMBENT BASELINE and (2) blocking
> R-ID from Role Sequence Schedule when applicable. B-IDs here must match PHASE EXIT GATE
> `Blocked bottleneck:` fields AND BOTTLENECK IMPACT MATRIX B-ID column — all three must be
> consistent by string comparison.
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

- Cause: [specific cause — cite IM-ID AND blocking R-ID from Role Sequence Schedule.
  Example: "IM-01 (paper-based goods receipt) combined with R-03 (Receiving Dock Supervisor)
  single-point-of-failure during shift transitions — causes three-way match queue at S-06.
  R-03 is Phase 2 primary owner (Role Sequence Schedule); shift handoff gap is the delay mechanism."]
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List AT-RISK SLA rows citing B-01. Example: `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`]

---

**B-02 — [Bottleneck Name]**

- Cause: [specific cause — cite IM-ID and blocking R-ID if applicable]
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List AT-RISK SLA rows citing B-02. Example: `"S-07: Invoice Matching -- AT-RISK, causal source: B-02"`]

---

**Gap Identification**

> MISSING: [step name] — [rationale: why it belongs; failure mode enabled; which phase;
> which IM-ID its absence perpetuates; which R-ID is accountable once added]

---

**BOTTLENECK IMPACT MATRIX**

> Consolidated cross-reference assembling every B-NN→IM-ID→SLA→Phase→Role linkage.
> Consistency requirements: B-ID must match Bottleneck Analysis block identifier AND
> PHASE EXIT GATE `Blocked bottleneck:` field (if that phase is blocked by this B-NN).
> IM-ID must match that B-NN's Cause field by string. SLA Node must match an AT-RISK row
> in SLA Analysis by S-ID string. Mitigation Owner must match Role Sequence Schedule.
>
> This matrix is a completeness contract: a missing B-NN row fails; an IM-ID mismatch fails;
> an unquantified Time Cost ("significant") fails.

| B-ID | Phase Affected | IM-ID Source | SLA Node (S-ID) | Time Cost | Mitigation Owner (R-ID) |
|------|---------------|-------------|-----------------|-----------|------------------------|
| B-01 | Phase [N] | IM-[NN] | S-[ID] ([state name]) | [quantified, e.g., +3.1 days] | R-[ID] ([role name]) |
| B-02 | Phase [N] | IM-[NN] | S-[ID] ([state name]) | [quantified] | R-[ID] ([role name]) |

Rules:
- Every declared B-NN block must appear as a row.
- IM-ID must literally match that B-NN Cause field's citation.
- SLA Node S-ID must match an AT-RISK row in SLA Analysis.
- Time Cost must be quantified.
- Mitigation Owner R-ID must match the Role Sequence Schedule primary or parallel owner for that phase.

---

### CHAIN STATUS

> Anti-embedding: Dedicated top-level section declared after SLA ANALYSIS.

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA→B): [every AT-RISK row cites a B-ID; enumerate or name gap]
- Backward (B→SLA): [every B-NN names affected SLA nodes; enumerate or name gap]
- Exit gate consistency: [every PHASE EXIT GATE `Blocked bottleneck:` B-ID matches a declared B-NN; name any mismatch]
- Matrix consistency: [BOTTLENECK IMPACT MATRIX IM-ID, SLA-node, and B-ID columns consistent with per-block fields and exit gate fields; name any inconsistency]
- Gap (if OPEN): [unresolved direction and unlinked entry]

---

### Terminal States

| Terminal | Type | Reached From |
|----------|------|-------------|
| [success terminal] | SUCCESS | [branch/state] |
| [failure terminal] | FAILURE | [branch/state] |
| [cancel terminal] | CANCEL | [branch/state] |

> Every exit branch must reach a declared terminal. No mid-flow endings without `continues-via:`.
