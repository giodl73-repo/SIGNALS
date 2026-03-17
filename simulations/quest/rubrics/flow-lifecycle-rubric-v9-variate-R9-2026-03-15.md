# flow-lifecycle — Round 9 Variations (Rubric v9)

**Rubric**: v9 · 33 aspirational criteria · Ceiling entering R9: 25/25 (R8 V-02 and V-05)
**Open criteria entering R9**: None — C-31, C-32, C-33 all cracked by R8 V-02 architecture.
**R9 objective**: All five variations carry the full R8 ceiling (25/25). Variation axes probe
potential C-34+ territory. Single-axis first (V-01 through V-03), then combine.

**Evidence from R8 excellence (C-31, C-32, C-33):**
- C-31 signal: "SCAFFOLD REQUIREMENT: ALL B-NN blocks **declared below** must carry an Evidence
  field" — "declared below" is forward-reference language; gate positioned before B-01 block.
- C-32 signal: Consolidated block cites `` `Required format:` ``/`` `Fail condition:` `` by
  exact canonical labels, not paraphrases like "format specification" / "contract line".
- C-33 signal: Preamble concrete example uses `B-01` as `causal source:` value, matching the
  first declared B-NN block's identifier; preamble-to-per-block chain is consistent by
  string comparison.

**Variation axes chosen:**

- **Axis A — Inertia framing**: Status-quo (process executed manually, without the system)
  declared as a named INCUMBENT BASELINE section before the Role Registry Gate. Forces the
  cost-of-no-action to be established before any phase is traced. Bottleneck and gap
  findings are anchored to the incumbent baseline, not just to abstract process ideals.
- **Axis B — Lifecycle emphasis**: Explicit PHASE ENTRY CONTRACT and PHASE EXIT GATE per
  phase block — named structural elements declaring what conditions must hold before the
  phase begins and what outputs must exist before the next phase may start. Tests whether
  hard phase-boundary contracts improve C-01 coverage and reduce implicit-exit risk.
- **Axis C — Phrasing register**: Question-driven SECTION A format — each exception slot is
  opened by a numbered explicit question ("What causes this phase to fail before completing?")
  with a required answer stub. Replaces sub-field label prompts with interrogative framing
  that requires synthesis before filling.

| Variation | Axis | Hypothesis |
|-----------|------|-----------|
| V-01 | A only: Inertia framing first | Declaring the manual baseline before tracing any state anchors bottleneck causes to observable incumbent failure modes rather than inferred process theory |
| V-02 | B only: Phase-entry/exit gate contracts | Hard phase-boundary contracts make implicit entry conditions and dangling exits structurally visible as unanswered gate fields — should tighten C-01 coverage |
| V-03 | C only: Question-driven Section A | Interrogative prompts require the model to answer a named question per exception slot; unanswered questions are structurally visible in a way unfilled sub-field labels are not |
| V-04 | A + B: Inertia framing + phase gates | Incumbent baseline anchors bottleneck findings; phase gates enforce boundary discipline; compound structural pressure on state coverage and causal specificity |
| V-05 | A + B + C: all three axes | Maximum structural scaffolding: incumbent baseline + phase gate contracts + question-driven exception format |

---

## V-01 — Axis A: Inertia Framing First

**Variation axis**: Inertia framing — a named INCUMBENT BASELINE section is declared before
the Role Registry Gate. The baseline establishes the manual / status-quo version of the
process: who does it today, what tools are used, where delays accumulate. Every bottleneck
entry in the Bottleneck Analysis must cite at least one incumbent failure mode by name.

**Hypothesis**: When the "do nothing / manual today" baseline is declared before any phase is
traced, bottleneck causes are grounded in observable incumbent behavior rather than in
abstract process theory. The B-NN `Cause` fields become richer and more specific because
they can reference named incumbent failure modes; the Gap analysis gains a concrete
comparator. This may surface C-34+ signals around baseline-to-finding traceability.

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete this section before the Role Registry Gate. It establishes the manual or
> status-quo version of this process — how it is done today without the system under
> analysis. Every bottleneck cause and gap rationale in subsequent sections must
> reference at least one named incumbent failure mode from this section.

**Process type**: [L2O / P2P / Period Close / Case Lifecycle — auto-detect from {Topic}]

**Incumbent description**: [1–3 sentences describing how this process is executed manually
today: tools used (spreadsheets, email, phone calls), handoff mechanisms, storage location
of records]

**Incumbent failure modes** (label each IM-NN):

| IM-ID | Failure Mode | Frequency | Downstream Effect |
|-------|-------------|-----------|------------------|
| IM-01 | [name the specific recurring failure in the manual process] | [daily / per-cycle / per-exception] | [what breaks downstream] |
| IM-02 | [second failure mode] | [frequency] | [downstream effect] |

**Cost of no action**: [What accumulates if this process is never improved? Name a specific
metric: queue depth, error rate, cycle time, reconciliation backlog.]

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
- [ ] No R-ID entry uses the word "Approver" without a domain qualifier
- [ ] No R-ID entry uses "Owner" without a named responsibility
- [ ] Each R-ID is referenced by at least one Decision Supplement block in the phases below

Role set by process type:
- L2O → Sales Rep / Sales Manager / Finance Credit Analyst / Legal Counsel / Fulfillment Coordinator
- P2P → Procurement Officer / Accounts Payable Specialist / Receiving Dock Supervisor / Finance Controller
- Period Close → Finance Analyst / GL Manager / Controller / External Auditor
- Case Lifecycle → Support Engineer / Case Manager / Legal Counsel / Operations Coordinator

---

### Phase Structure

For each phase in the lifecycle, produce the following blocks in order:

---

**PHASE [N] — [PHASE NAME]**

**SECTION A — EXCEPTION TRACES**

For each exception trace originating in this phase:

> **EX-[Phase#][Letter] — [Exception Name]**
> - Trigger: [specific condition that causes deviation from the happy path]
> - Trace: [path of states traversed from trigger to resolution or terminal; cite S-IDs]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state name — SUCCESS / FAILURE / CANCEL] or [continues via [state]]
> - Why Problematic: [specific operational or compliance reason this failure mode matters]

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
> - Owner: R-[ID] ([role name])
> - Branch A ([condition outcome]): → S-[ID] ([state name])
> - Branch B ([condition outcome]): → S-[ID] ([state name]) or TERMINAL
> - Fallback: [action if condition cannot be evaluated — who is notified, what state is entered]

---

[Repeat Phase Structure for each phase. Minimum 2 phases required.]

---

### Parallel Path Modeling

Identify at least one point where parallel work streams exist and trace them to their join:

- **FORK at**: S-[ID] ([state name])
- **Branch 1**: [path description — states traversed]
- **Branch 2**: [path description — states traversed]
- **Synchronization (JOIN) at**: S-[ID] ([join state name])
- **Join Condition**: AND-join (both branches must complete) / OR-join (first branch to
  complete is sufficient) — specify which applies and explain why

---

### Edge Case Enumeration

Identify at least three edge cases that are never handled or handled inconsistently.
Each must be distinct from the exception flows declared in SECTION A above.

> **EC-[N] — [Edge Case Name]**
> - Triggering Condition: [specific scenario that produces this edge case]
> - Why Problematic: [specific reason this falls outside documented handling]
> - Correct Response: [what a compliant implementation should do; name the responsible role]

---

### Cross-Process Interaction Modeling

Identify at least one point where this lifecycle touches an adjacent process:

> **CROSS-PROCESS HANDOFF — {Topic} lifecycle → [adjacent process name]**
> - Sending State: S-[ID] ([state name])
> - Receiving Process: [adjacent process name]
> - Data Payload: [named fields or record types transferred]
> - Expected Acknowledgment: [signal or confirmation message from receiving process]
> - Failure Mode: [what happens if acknowledgment is not received within SLA]
> - Owner: R-[ID] ([role name])

---

### SLA and Timing Analysis

Annotate at least three states or transitions with SLA targets and typical durations:

| S-ID | State Name | SLA Target | Typical Duration | Status | Bottleneck Ref |
|------|-----------|------------|------------------|--------|----------------|
| | | | | AT-RISK / ON-TRACK | B-NN (if AT-RISK) |

Rules:
- AT-RISK = typical duration exceeds SLA target
- Every AT-RISK row must carry a Bottleneck Ref citing a B-NN from Bottleneck Analysis below
- Minimum 3 annotated rows; at least 1 must be AT-RISK

---

### Bottleneck Analysis

> **PREAMBLE**: This section identifies where delays accumulate (bottlenecks) and steps
> missing from the current model (gaps). Each bottleneck cause must reference at least one
> named incumbent failure mode (IM-ID) from the INCUMBENT BASELINE section.
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

- Cause: [specific cause of delay — cite the incumbent failure mode (IM-ID) that this
  bottleneck perpetuates or worsens]
- Impact: [downstream state, SLA node, or adjacent process affected]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row that cites B-01 as causal source, using the format above.
    Example: `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`]

---

**B-02 — [Bottleneck Name]**

- Cause: [specific cause — cite the incumbent failure mode (IM-ID) that this bottleneck
  perpetuates or worsens]
- Impact: [downstream state, SLA node, or adjacent process affected]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row that cites B-02 as causal source, using the format above.
    Example: `"S-07: Invoice Matching -- AT-RISK, causal source: B-02"`]

---

**Gap Identification**

> MISSING: [Step or control that exists in real-world practice of this process but is absent
> from the current model. Format: MISSING: [step name] — [rationale: why it belongs, what
> failure mode its absence enables, and reference to the incumbent baseline if applicable]]

---

### CHAIN STATUS

> Anti-embedding: Do not embed CHAIN STATUS as a line inside the SLA ANALYSIS section.
> This section is a dedicated top-level output element declared after SLA ANALYSIS.

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA→B): [confirm that every AT-RISK SLA row cites a B-ID; list the AT-RISK
  rows and their cited B-IDs, or name the unresolved row if OPEN]
- Backward (B→SLA): [confirm that every B-NN entry names affected SLA nodes; list each
  B-ID and the AT-RISK rows it affects, or name the missing citation if OPEN]
- Gap (if OPEN): [name the specific unresolved direction and the unlinked entry]

---

### Terminal States

| Terminal | Type | Reached From |
|----------|------|-------------|
| [success terminal name] | SUCCESS | [branch/state that reaches it] |
| [failure terminal name] | FAILURE | [branch/state that reaches it] |
| [cancel terminal name] | CANCEL | [branch/state that reaches it] |

> Completeness check: Every exit branch in every SECTION B state table must reach one of
> the declared terminals above. No branch may end at a non-terminal state without an
> explicit `continues-via: S-[ID]` pointer. Fail if any branch ends mid-flow.

---
---

## V-02 — Axis B: Phase-Entry/Exit Gate Contracts

**Variation axis**: Lifecycle emphasis — each phase block opens with an explicit PHASE ENTRY
CONTRACT (what must be true for this phase to begin) and closes with a PHASE EXIT GATE (what
outputs must exist before the next phase may start). These are named structural elements with
required fields, not prose instructions.

**Hypothesis**: When entry conditions and exit outputs are declared as named gate contracts
rather than left implicit in the state table's Entry Condition column, two structural
improvements emerge: (1) missing entry conditions become visible as blank gate fields rather
than absent column values; (2) phase-level completeness becomes checkable by reading the exit
gate rather than scanning all state exits for terminal labels. This may surface a C-34+ signal
around phase-level completeness verification as a named structural artifact.

---

You are running **flow-lifecycle** for topic: {Topic}.

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
- [ ] Each R-ID appears in at least one Decision Supplement block below

Role set by process type:
- L2O → Sales Rep / Sales Manager / Finance Credit Analyst / Legal Counsel / Fulfillment Coordinator
- P2P → Procurement Officer / Accounts Payable Specialist / Receiving Dock Supervisor / Finance Controller
- Period Close → Finance Analyst / GL Manager / Controller / External Auditor
- Case Lifecycle → Support Engineer / Case Manager / Legal Counsel / Operations Coordinator

---

### Phase Structure

For each phase, produce the following four blocks in document order:

---

**PHASE [N] — [PHASE NAME]**

**PHASE ENTRY CONTRACT**

> This gate must be completed before SECTION A or SECTION B for this phase.
> Do not trace any state in this phase until all fields are filled.

- Entry Condition: [specific state or output from the previous phase that must exist for
  this phase to begin; reference the prior phase's exit gate output by name]
- Pre-condition check: [the role responsible for verifying that the entry condition is met]
- Blocking condition: [what happens if the entry condition is not met — which state is
  entered and which role is notified]

**SECTION A — EXCEPTION TRACES**

For each exception trace originating in this phase:

> **EX-[Phase#][Letter] — [Exception Name]**
> - Trigger: [specific condition that causes deviation]
> - Trace: [state path from trigger to resolution or terminal; cite S-IDs]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state] or [continues via S-[ID]]
> - Why Problematic: [specific reason this failure mode matters]

Minimum 1 exception per phase; minimum 3 total across all phases.

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

> This gate must be completed before the next phase begins.
> Outputs listed here are the entry-condition prerequisites for PHASE [N+1].

- Exit Condition: [what the phase must have produced to be considered complete]
- Required outputs: [named artifacts, decisions, or state records that must exist]
- Exit verification: R-[ID] ([role name]) confirms all required outputs are present
- Blocking condition: [if required outputs are absent, what re-entry or escalation path applies]

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
> - Correct Response: [what a compliant implementation should do; name the responsible role]

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

> **PREAMBLE**: Bottlenecks are states or transitions where delays accumulate; gaps are
> steps missing from the model that exist in real-world practice.
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

- Cause: [specific cause of delay or congestion]
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row citing B-01 as causal source. Example: `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`]

---

**B-02 — [Bottleneck Name]**

- Cause: [specific cause]
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row citing B-02 as causal source. Example: `"S-07: Invoice Matching -- AT-RISK, causal source: B-02"`]

---

**Gap Identification**

> MISSING: [step name] — [rationale: why it belongs in this process model; what failure
> mode its absence enables; which phase it belongs in]

---

### CHAIN STATUS

> Anti-embedding: Do not embed CHAIN STATUS as a line inside the SLA ANALYSIS section.
> This section is a dedicated top-level output element declared after SLA ANALYSIS.

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA→B): [every AT-RISK SLA row cites a B-ID; enumerate or name the gap]
- Backward (B→SLA): [every B-NN entry names affected SLA nodes; enumerate or name the gap]
- Gap (if OPEN): [name the unresolved direction and unlinked entry]

---

### Terminal States

| Terminal | Type | Reached From |
|----------|------|-------------|
| [success terminal] | SUCCESS | [branch/state] |
| [failure terminal] | FAILURE | [branch/state] |
| [cancel terminal] | CANCEL | [branch/state] |

> Every exit in every SECTION B state table must reach a declared terminal above. No branch
> may end at a non-terminal state without an explicit `continues-via: S-[ID]` pointer.

---
---

## V-03 — Axis C: Question-Driven Section A Format

**Variation axis**: Phrasing register — SECTION A exception traces are presented as numbered
questions with explicit answer stubs. Each exception slot opens with a numbered interrogative
("Q1: What causes this phase to fail before completing?") that the model must answer, not just
fill. Unanswered questions are structurally visible as un-answered question stubs, not as
blank sub-field labels.

**Hypothesis**: Sub-field label prompts ("Trigger:", "Trace:") invite value insertion without
requiring synthesis; a model can populate labels with generic placeholders that pass column
checks. Interrogative prompts require the model to answer a named question with process-
specific content — an unanswered question is a visible response failure, not a blank field.
This may improve exception specificity (C-02) and edge case quality (C-07) by raising the
cost of generic placeholder answers, and may surface a C-34+ signal around interrogative
anchoring as a format-level completeness mechanism.

---

You are running **flow-lifecycle** for topic: {Topic}.

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
- [ ] Each R-ID appears in at least one Decision Supplement block below

Role set by process type:
- L2O → Sales Rep / Sales Manager / Finance Credit Analyst / Legal Counsel / Fulfillment Coordinator
- P2P → Procurement Officer / Accounts Payable Specialist / Receiving Dock Supervisor / Finance Controller
- Period Close → Finance Analyst / GL Manager / Controller / External Auditor
- Case Lifecycle → Support Engineer / Case Manager / Legal Counsel / Operations Coordinator

---

### Phase Structure

---

**PHASE [N] — [PHASE NAME]**

**SECTION A — EXCEPTION TRACES**

For each exception trace originating in this phase, answer all four questions. An exception
slot with any question left unanswered is incomplete and fails.

> **EX-[Phase#][Letter] — [Exception Name]**
>
> Q1: What specific condition causes this phase to fail or deviate before completing?
> A1: [specific trigger — name the state, input, or threshold breach; do not use "error occurs"]
>
> Q2: What is the exact path this failure takes from its trigger to a terminal state?
> A2: [enumerate the states traversed, citing S-IDs; end with a named terminal state or continues-via pointer]
>
> Q3: Which role handles this exception, and what action do they take?
> A3: R-[ID] ([role name]) — [specific action; do not use "handles the exception" generically]
>
> Q4: Why is this failure mode operationally or compliance-relevant to this specific process?
> A4: [specific reason; reference process type (L2O / P2P / Period Close / Case) and name the stake at risk]

Minimum 1 exception per phase. Minimum 3 exception traces in total across all phases.
Each must be process-specific to {Topic}; generic boilerplate answers fail Q4.

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

Identify at least three edge cases distinct from SECTION A exception flows. For each,
answer all three questions. An edge case slot with any question unanswered is incomplete.

> **EC-[N] — [Edge Case Name]**
>
> Q1: What specific scenario triggers this edge case, and why does it fall outside the
> documented happy path and exception flows?
> A1: [specific triggering scenario; explain why existing exception flows do not cover it]
>
> Q2: Why is this case problematic — what breaks, and for whom?
> A2: [specific operational or data-integrity consequence; name the affected role or downstream process]
>
> Q3: What is the correct response, and which role owns it?
> A3: R-[ID] ([role name]) — [specific correct action; name the target state or resolution path]

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

> **PREAMBLE**: Bottlenecks are states where delays accumulate; gaps are steps missing from
> the model.
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

- Cause: [specific cause]
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row citing B-01. Example: `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`]

---

**B-02 — [Bottleneck Name]**

- Cause: [specific cause]
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row citing B-02. Example: `"S-07: Invoice Matching -- AT-RISK, causal source: B-02"`]

---

**Gap Identification**

> MISSING: [step name] — [rationale: why it belongs; what failure mode its absence enables]

---

### CHAIN STATUS

> Anti-embedding: Do not embed CHAIN STATUS as a line inside the SLA ANALYSIS section.
> This section is a dedicated top-level output element declared after SLA ANALYSIS.

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA→B): [every AT-RISK row cites a B-ID; enumerate or name gap]
- Backward (B→SLA): [every B-NN entry names affected SLA nodes; enumerate or name gap]
- Gap (if OPEN): [name the unresolved direction and unlinked entry]

---

### Terminal States

| Terminal | Type | Reached From |
|----------|------|-------------|
| [success terminal] | SUCCESS | [branch/state] |
| [failure terminal] | FAILURE | [branch/state] |
| [cancel terminal] | CANCEL | [branch/state] |

> Every exit in every SECTION B state table must reach a declared terminal above. No branch
> may end at a non-terminal state without an explicit `continues-via: S-[ID]` pointer.

---
---

## V-04 — Axes A + B: Inertia Framing + Phase Gate Contracts

**Variation axis**: Inertia framing (A) combined with phase-entry/exit gate contracts (B).
The INCUMBENT BASELINE is declared before the Role Registry Gate; each phase block opens
with a PHASE ENTRY CONTRACT that cites the incumbent baseline where relevant, and closes
with a PHASE EXIT GATE. Bottleneck causes must reference both the incumbent failure mode
(IM-ID) and the phase exit gate that the bottleneck blocks.

**Hypothesis**: Compound structural pressure: incumbent baseline anchors causal specificity
(Axis A) while phase gate contracts enforce boundary discipline (Axis B). The bottleneck
`Cause` fields have two named obligations — incumbent IM-ID and blocked phase exit gate —
which may produce richer evidence chains. The EXIT GATE also creates a new potential
target: a C-34+ signal around exit-gate-to-bottleneck cross-reference as a closing
structural artifact.

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete this section before the Role Registry Gate. Do not begin phase tracing until
> all fields are filled. Every B-NN Cause field below must cite at least one IM-ID from
> this section.

**Process type**: [L2O / P2P / Period Close / Case Lifecycle — auto-detect from {Topic}]

**Incumbent description**: [1–3 sentences: how the process is done manually today; tools,
handoffs, record storage]

**Incumbent failure modes**:

| IM-ID | Failure Mode | Frequency | Downstream Effect |
|-------|-------------|-----------|------------------|
| IM-01 | [specific recurring failure in the manual process] | [frequency] | [downstream effect] |
| IM-02 | [second failure mode] | [frequency] | [downstream effect] |

**Cost of no action**: [specific accumulating metric if the process is never improved]

---

### Role Registry Gate

> GATE BLOCK: Complete before tracing any state. All R-ID entries filled; all
> anti-generic checks satisfied.

| R-ID | Role | Function |
|------|------|----------|
| R-01 | [domain-specific role] | [named responsibility] |
| R-02 | [domain-specific role] | [named responsibility] |
| R-03 | [domain-specific role] | [named responsibility] |

Anti-generic validation:
- [ ] No entry uses "Approver" without a domain qualifier
- [ ] No entry uses "Owner" without a named responsibility
- [ ] Each R-ID appears in at least one Decision Supplement block

Role set by process type:
- L2O → Sales Rep / Sales Manager / Finance Credit Analyst / Legal Counsel / Fulfillment Coordinator
- P2P → Procurement Officer / Accounts Payable Specialist / Receiving Dock Supervisor / Finance Controller
- Period Close → Finance Analyst / GL Manager / Controller / External Auditor
- Case Lifecycle → Support Engineer / Case Manager / Legal Counsel / Operations Coordinator

---

### Phase Structure

---

**PHASE [N] — [PHASE NAME]**

**PHASE ENTRY CONTRACT**

> Complete before SECTION A and SECTION B. Do not trace states until all fields are filled.

- Entry Condition: [what must exist from the prior phase or the INCUMBENT BASELINE for
  this phase to begin — reference prior exit gate output by name if applicable]
- Pre-condition check: R-[ID] ([role name]) verifies entry condition
- Blocking condition: if entry condition is not met → [state entered] / R-[ID] notified

**SECTION A — EXCEPTION TRACES**

> **EX-[Phase#][Letter] — [Exception Name]**
> - Trigger: [specific condition]
> - Trace: [state path; cite S-IDs]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state] or [continues via S-[ID]]
> - Why Problematic: [process-specific reason]
> - Incumbent Link: [optional — does this exception also occur in the manual process?
>   If yes, cite IM-ID]

Minimum 1 per phase; minimum 3 total across all phases.

**SECTION B — STATE TRANSITION TABLE**

| S-ID | State Name | Entry Condition | Exits | Owner (R-ID) | Type |
|------|-----------|-----------------|-------|--------------|------|

Rules:
- Named Entry Condition required; "Ready" fails.
- Every Exit: destination S-ID or TERMINAL.
- Type values: NORMAL / DECISION / PARALLEL-FORK / PARALLEL-JOIN / EXCEPTION / TERMINAL

**Decision Supplement Blocks**:

> **DS-[S-ID] — [State Name]**
> - Condition: [rule or threshold]
> - Owner: R-[ID] ([role name])
> - Branch A ([outcome]): → S-[ID]
> - Branch B ([outcome]): → S-[ID] or TERMINAL
> - Fallback: [action if condition cannot be evaluated]

**PHASE EXIT GATE**

> Complete before advancing to the next phase. Outputs listed here are the entry-condition
> prerequisites for PHASE [N+1].

- Exit Condition: [what this phase must have produced to be complete]
- Required outputs: [named artifacts, decisions, or state records]
- Exit verification: R-[ID] ([role name]) confirms outputs present
- Blocked bottleneck: [if a B-NN bottleneck in the analysis below delays this exit,
  name the B-ID here — creates a forward-reference for phase-gate-to-bottleneck linking]
- Blocking condition: if required outputs absent → [re-entry path or escalation]

---

[Repeat Phase Structure. Minimum 2 phases.]

---

### Parallel Path Modeling

- **FORK at**: S-[ID] ([state name])
- **Branch 1**: [states traversed]
- **Branch 2**: [states traversed]
- **JOIN at**: S-[ID] ([join state name])
- **Join Condition**: AND-join / OR-join — specify which and explain why

---

### Edge Case Enumeration

> **EC-[N] — [Edge Case Name]**
> - Triggering Condition: [specific scenario]
> - Why Problematic: [specific reason outside documented handling]
> - Correct Response: R-[ID] ([role]) — [specific action]

Three or more; each distinct from SECTION A flows.

---

### Cross-Process Interaction Modeling

> **CROSS-PROCESS HANDOFF — {Topic} lifecycle → [adjacent process]**
> - Sending State: S-[ID] ([state name])
> - Receiving Process: [name]
> - Data Payload: [named fields]
> - Expected Acknowledgment: [signal]
> - Failure Mode: [consequence if not received]
> - Owner: R-[ID] ([role])

---

### SLA and Timing Analysis

| S-ID | State Name | SLA Target | Typical Duration | Status | Bottleneck Ref |
|------|-----------|------------|------------------|--------|----------------|

Minimum 3 rows; at least 1 AT-RISK with B-NN citation.

---

### Bottleneck Analysis

> **PREAMBLE**: Each B-NN `Cause` field must cite: (a) the incumbent failure mode (IM-ID)
> that this bottleneck perpetuates or worsens, AND (b) the phase exit gate it delays (by
> phase number and gate output name). This creates a three-way evidence chain: IM-ID →
> B-NN → blocked phase exit gate.
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

- Cause: [specific cause — cite IM-ID from INCUMBENT BASELINE and the phase exit gate delayed]
- Impact: [downstream state and SLA node affected]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row citing B-01. Example: `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`]

---

**B-02 — [Bottleneck Name]**

- Cause: [specific cause — cite IM-ID and phase exit gate delayed]
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row citing B-02. Example: `"S-07: Invoice Matching -- AT-RISK, causal source: B-02"`]

---

**Gap Identification**

> MISSING: [step name] — [rationale; cite the IM-ID whose absence this step would have
> prevented if it were present]

---

### CHAIN STATUS

> Anti-embedding: Do not embed CHAIN STATUS as a line inside the SLA ANALYSIS section.
> This section is a dedicated top-level output element declared after SLA ANALYSIS.

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA→B): [every AT-RISK row cites a B-ID; enumerate or name gap]
- Backward (B→SLA): [every B-NN entry names affected SLA nodes; enumerate or name gap]
- Gap (if OPEN): [name the unresolved direction and unlinked entry]

---

### Terminal States

| Terminal | Type | Reached From |
|----------|------|-------------|
| [success terminal] | SUCCESS | [branch/state] |
| [failure terminal] | FAILURE | [branch/state] |
| [cancel terminal] | CANCEL | [branch/state] |

> Every exit in every SECTION B state table must reach a declared terminal above. No
> branch may end at a non-terminal state without a `continues-via: S-[ID]` pointer.

---
---

## V-05 — Axes A + B + C: Inertia Framing + Phase Gate Contracts + Question-Driven Section A

**Variation axis**: All three axes active simultaneously.
- Axis A: INCUMBENT BASELINE declared before Role Registry Gate
- Axis B: PHASE ENTRY CONTRACT + PHASE EXIT GATE per phase; bottleneck causes cite IM-ID
  and blocked phase exit gate
- Axis C: SECTION A uses numbered Q&A format; EDGE CASE ENUMERATION uses numbered Q&A format

**Hypothesis**: Maximum structural scaffolding. The incumbent baseline anchors causal
specificity (A); phase gate contracts enforce boundary discipline (B); interrogative prompts
raise the cost of generic exception answers (C). These three axes interact: the SECTION A
question "Why is this operationally relevant?" (Q4) can reference the INCUMBENT BASELINE by
IM-ID, creating a cross-section traceability chain that none of the single-axis variations
can produce. This may produce C-34+ signals around multi-section traceability — the ability
to string-compare IM-IDs across INCUMBENT BASELINE, SECTION A Q4 answers, and B-NN Cause
fields as a closed evidence chain.

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete before the Role Registry Gate. Do not begin phase tracing until all fields are
> filled. B-NN Cause fields must cite IM-IDs; SECTION A Q4 answers may cite IM-IDs.

**Process type**: [L2O / P2P / Period Close / Case Lifecycle — auto-detect from {Topic}]

**Incumbent description**: [1–3 sentences: manual process today; tools, handoffs, record storage]

**Incumbent failure modes**:

| IM-ID | Failure Mode | Frequency | Downstream Effect |
|-------|-------------|-----------|------------------|
| IM-01 | [specific recurring failure] | [frequency] | [downstream effect] |
| IM-02 | [second failure mode] | [frequency] | [downstream effect] |

**Cost of no action**: [specific accumulating metric if the process is never improved]

---

### Role Registry Gate

> GATE BLOCK: Complete before any phase. All R-ID entries filled; anti-generic checks
> satisfied.

| R-ID | Role | Function |
|------|------|----------|
| R-01 | [domain-specific role] | [named responsibility] |
| R-02 | [domain-specific role] | [named responsibility] |
| R-03 | [domain-specific role] | [named responsibility] |

Anti-generic validation:
- [ ] No entry uses "Approver" without a domain qualifier
- [ ] No entry uses "Owner" without a named responsibility
- [ ] Each R-ID appears in at least one Decision Supplement block

Role set by process type:
- L2O → Sales Rep / Sales Manager / Finance Credit Analyst / Legal Counsel / Fulfillment Coordinator
- P2P → Procurement Officer / Accounts Payable Specialist / Receiving Dock Supervisor / Finance Controller
- Period Close → Finance Analyst / GL Manager / Controller / External Auditor
- Case Lifecycle → Support Engineer / Case Manager / Legal Counsel / Operations Coordinator

---

### Phase Structure

---

**PHASE [N] — [PHASE NAME]**

**PHASE ENTRY CONTRACT**

> Complete before SECTION A and SECTION B. Do not trace states until all fields are filled.

- Entry Condition: [what must exist from prior phase or INCUMBENT BASELINE for this
  phase to begin]
- Pre-condition check: R-[ID] ([role name]) verifies
- Blocking condition: if entry condition not met → [state entered] / R-[ID] notified

**SECTION A — EXCEPTION TRACES**

For each exception trace originating in this phase, answer all four questions. An
unanswered question is an incomplete exception slot.

> **EX-[Phase#][Letter] — [Exception Name]**
>
> Q1: What specific condition causes this phase to fail or deviate before completing?
> A1: [specific trigger — name the state, input, or threshold breach; do not use "error occurs"]
>
> Q2: What is the exact path this failure takes from its trigger to a terminal state?
> A2: [enumerate states traversed, citing S-IDs; end with a named terminal or continues-via pointer]
>
> Q3: Which role handles this exception, and what specific action do they take?
> A3: R-[ID] ([role name]) — [specific action; do not use "handles the exception" generically]
>
> Q4: Why is this failure mode operationally or compliance-relevant to this specific process?
>     If this failure mode also occurs in the manual process, cite the IM-ID.
> A4: [specific reason; reference process type and stake at risk; cite IM-ID if applicable]

Minimum 1 per phase; minimum 3 total; each process-specific to {Topic}.

**SECTION B — STATE TRANSITION TABLE**

| S-ID | State Name | Entry Condition | Exits | Owner (R-ID) | Type |
|------|-----------|-----------------|-------|--------------|------|

Rules:
- Named Entry Condition required; "Ready" fails.
- Every Exit: destination S-ID or TERMINAL.
- Type values: NORMAL / DECISION / PARALLEL-FORK / PARALLEL-JOIN / EXCEPTION / TERMINAL

**Decision Supplement Blocks**:

> **DS-[S-ID] — [State Name]**
> - Condition: [rule or threshold]
> - Owner: R-[ID] ([role name])
> - Branch A ([outcome]): → S-[ID]
> - Branch B ([outcome]): → S-[ID] or TERMINAL
> - Fallback: [action if condition cannot be evaluated]

**PHASE EXIT GATE**

> Complete before advancing to the next phase.

- Exit Condition: [what this phase must have produced]
- Required outputs: [named artifacts, decisions, records]
- Exit verification: R-[ID] ([role name]) confirms outputs present
- Blocked bottleneck: [B-ID if a bottleneck delays this exit — forward-reference to B-NN
  block below; creates phase-gate-to-bottleneck traceability]
- Blocking condition: if required outputs absent → [re-entry or escalation path]

---

[Repeat Phase Structure. Minimum 2 phases.]

---

### Parallel Path Modeling

- **FORK at**: S-[ID] ([state name])
- **Branch 1**: [states traversed]
- **Branch 2**: [states traversed]
- **JOIN at**: S-[ID] ([join state name])
- **Join Condition**: AND-join / OR-join — specify which and explain why

---

### Edge Case Enumeration

At least three edge cases distinct from SECTION A flows. Answer all three questions per
slot. An unanswered question is an incomplete edge case slot.

> **EC-[N] — [Edge Case Name]**
>
> Q1: What specific scenario triggers this edge case, and why does it fall outside the
> documented happy path and exception flows?
> A1: [specific scenario; explain why existing flows do not cover it; cite IM-ID if the
>     scenario also occurs in the manual baseline]
>
> Q2: Why is this case problematic — what breaks, and for whom?
> A2: [specific operational or data-integrity consequence; name the affected role or process]
>
> Q3: What is the correct response, and which role owns it?
> A3: R-[ID] ([role name]) — [specific action; name the target state or resolution path]

---

### Cross-Process Interaction Modeling

> **CROSS-PROCESS HANDOFF — {Topic} lifecycle → [adjacent process]**
> - Sending State: S-[ID] ([state name])
> - Receiving Process: [name]
> - Data Payload: [named fields]
> - Expected Acknowledgment: [signal]
> - Failure Mode: [consequence if not received]
> - Owner: R-[ID] ([role])

---

### SLA and Timing Analysis

| S-ID | State Name | SLA Target | Typical Duration | Status | Bottleneck Ref |
|------|-----------|------------|------------------|--------|----------------|

Minimum 3 rows; at least 1 AT-RISK with B-NN citation.

---

### Bottleneck Analysis

> **PREAMBLE**: Each B-NN `Cause` field must cite: (a) the incumbent failure mode (IM-ID)
> that this bottleneck perpetuates, AND (b) the phase exit gate it delays. SECTION A Q4
> answers may also reference IM-IDs, creating a traceability chain: IM-ID (INCUMBENT
> BASELINE) → EX Q4 reference → B-NN Cause citation → blocked phase exit gate.
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

- Cause: [specific cause — cite IM-ID from INCUMBENT BASELINE; cite phase exit gate delayed]
- Impact: [downstream state and SLA node affected]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row citing B-01. Example: `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`]

---

**B-02 — [Bottleneck Name]**

- Cause: [specific cause — cite IM-ID; cite phase exit gate delayed]
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row citing B-02. Example: `"S-07: Invoice Matching -- AT-RISK, causal source: B-02"`]

---

**Gap Identification**

> MISSING: [step name] — [rationale; cite the IM-ID whose absence this step would have
> prevented; cite the phase exit gate that lacks this step as a required output]

---

### CHAIN STATUS

> Anti-embedding: Do not embed CHAIN STATUS as a line inside the SLA ANALYSIS section.
> This section is a dedicated top-level output element declared after SLA ANALYSIS.

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA→B): [every AT-RISK row cites a B-ID; enumerate or name gap]
- Backward (B→SLA): [every B-NN entry names affected SLA nodes; enumerate or name gap]
- IM-trace (optional): [confirm that every B-NN Cause field cites an IM-ID; list
  IM-ID → B-NN → blocked phase exit gate triples if the traceability chain is complete]
- Gap (if OPEN): [name the unresolved direction and unlinked entry]

---

### Terminal States

| Terminal | Type | Reached From |
|----------|------|-------------|
| [success terminal] | SUCCESS | [branch/state] |
| [failure terminal] | FAILURE | [branch/state] |
| [cancel terminal] | CANCEL | [branch/state] |

> Every exit in every SECTION B state table must reach a declared terminal above. No
> branch may end at a non-terminal state without a `continues-via: S-[ID]` pointer.
