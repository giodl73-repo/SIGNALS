---

# /quest:variate — flow-lifecycle Round 6

**Rubric**: v6 (C-01–C-26, 18 aspirational, /18 denominator)
**New criteria under test**: C-24 (Evidence Field Format Dual Redundancy), C-25 (Anti-Embedding Dual Enforcement), C-26 (Evidence Field Axis Separation)

**Variation design summary:**

| V | Single axis | Hypothesis |
|---|-------------|------------|
| V-01 | C-26 isolation — merged Evidence field axes (prose, no separate labels) | passes C-24, C-25; fails C-26 |
| V-02 | C-26 isolation — separated labeled Evidence axes (`Required format:` / `Fail condition:`) | passes C-24, C-25, C-26 |
| V-03 | C-24 isolation — preamble-only concrete example; per-block minimal reference | passes C-22; fails C-24 |
| V-04 | C-24 isolation — per-block concrete example only; preamble bracket template | fails C-22, C-24 by dependency |
| V-05 | Full R6 synthesis — dual-location labeled axes + dual concrete example + dual anti-embedding | passes C-24, C-25, C-26 |

---

## V-01 — C-26 Isolation: Merged Evidence Axes

**Axis**: C-26 — Evidence field instruction merges `Required format:` and `Fail condition:` into a single prose sentence without separate labels.
**Hypothesis**: C-24 passes (concrete example in preamble AND per-block). C-25 passes (anti-embedding in preamble AND section opening). C-26 fails (axes bundled into one prose hint, not independently labeled).

---

You are simulating a multi-step business document lifecycle for the topic: **{topic}**.

---

### PREAMBLE — Read before generating any content

**Process auto-detection.** Identify the process type from {topic} (L2O = Lead-to-Order; P2P = Procure-to-Pay; PC = Period Close; CL = Case Lifecycle; or declare the closest match). All roles, states, and exception flows must be specific to that process type.

**Anti-embedding constraint.** Do not embed the CHAIN STATUS declaration as a line or annotation inside the SLA ANALYSIS section. CHAIN STATUS must appear as the first line of a dedicated `## CHAIN STATUS` section.

**Evidence field format contract.** In the BOTTLENECK AND GAP ANALYSIS section, each B-NN block must include an Evidence sub-field listing the specific AT-RISK SLA rows that cite that B-ID. Use the format `[State name -- S-ID]: AT-RISK, causal source: B-[ID]` — for example, `S-05: Credit Hold Review -- AT-RISK, causal source: B-01`. A field containing only "see SLA ANALYSIS" or state names without S-ID and AT-RISK row-level specificity does not satisfy this requirement.

**Exception-first ordering.** Within every phase block, exceptions must appear in SECTION A before states appear in SECTION B. SECTION A carries the lower ordinal label and must be generated before SECTION B.

---

### ROLE REGISTRY

Declare all domain-specific roles before tracing any state. For each role:

| R-ID | Role Name | Function | Anti-Generic Check |
|------|-----------|----------|--------------------|
| R-01 | [domain-specific role name — no generic "Approver"] | [what this role does in this process] | [confirm not generic] |
| R-02 | ... | ... | ... |
| ... | ... | ... | ... |

*Add one role per decision point or approval gate. Role names must match the declared process type: L2O → Account Executive, Credit Analyst, Contract Manager, Sales Operations, Finance Controller; P2P → Procurement Specialist, Vendor Manager, Accounts Payable Clerk, Receiving Inspector, Finance Controller; PC → GL Accountant, Controller, Audit Lead, CFO; CL → Case Manager, Legal Counsel, Support Analyst, Operations Lead.*

---

### PHASE 1 — [Auto-name from process context]

#### SECTION A — EXCEPTIONS

*Generate all exception flows that originate in this phase before listing any states. Write one constructed-answer block per exception flow. Minimum 2 exception flows per phase.*

**EX-1A**
- Trigger: [specific entry condition that initiates this failure mode — name the state and field/event]
- Trace: [ordered list of states traversed from trigger to terminal: State-name → State-name → TERMINAL]
- Handling Role: [R-ID: Role Name]
- Terminal: [terminal state reached]
- Why Problematic: [operational and business impact — specific to this phase and process type]

**EX-1B**
- Trigger:
- Trace:
- Handling Role:
- Terminal:
- Why Problematic:

*(Add EX-1C and beyond as needed for this phase's failure modes.)*

#### SECTION B — STATES

| State Name -- S-ID | Type | Entry Condition | Exits |
|--------------------|------|-----------------|-------|
| [Name] -- S-01 | START / PROCESSING / DECISION / WAIT / TERMINAL | [named condition that must be true for this state to be entered] | → S-02 on [condition]; → S-NN on [condition] |
| [Name] -- S-02 | ... | ... | ... |

*Types: START (one per process), PROCESSING, DECISION (triggers a Decision Supplement Block), WAIT, PARALLEL-FORK, PARALLEL-JOIN, TERMINAL. Every state must have a named entry condition. Every exit must name a destination state or be labeled TERMINAL.*

**Decision Supplement Block — D-[S-ID]** *(write one block for each DECISION-type state)*
- Condition: [rule or field value being evaluated]
- Owner: [R-ID: Role Name]
- Branch YES: → [State name -- S-ID]
- Branch NO: → [State name -- S-ID]
- Fallback: → [State name -- S-ID] *(if neither branch resolves; required — do not omit)*

**Parallel Work Streams** *(if this phase has concurrent paths)*
- Fork at: [S-ID] — Fork type: [AND-fork / OR-fork]
- Stream 1: [name] — States: [S-ID list]
- Stream 2: [name] — States: [S-ID list]
- Join at: [S-ID] — Join condition: [AND-join: both streams must complete / OR-join: first stream to complete unblocks]

---

### PHASE 2 — [Auto-name from process context]

#### SECTION A — EXCEPTIONS

**EX-2A**
- Trigger:
- Trace:
- Handling Role:
- Terminal:
- Why Problematic:

**EX-2B**
- Trigger:
- Trace:
- Handling Role:
- Terminal:
- Why Problematic:

#### SECTION B — STATES

| State Name -- S-ID | Type | Entry Condition | Exits |
|--------------------|------|-----------------|-------|

*(Continue Decision Supplement Blocks and Parallel Work Streams as needed.)*

---

*(Continue adding phases until all states are traced to terminal states.)*

---

### EDGE CASES

*Write at least 3 edge cases. Each must be distinct from the exception flows above — an edge case is a scenario that exists in practice but is not handled or is handled inconsistently, not a named failure mode already traced in SECTION A.*

**EC-01**
- Trigger: [specific condition that creates this edge case]
- Why Problematic: [why the normal flow cannot handle this correctly]
- Correct Response: [what the correct handling should be]

**EC-02**
- Trigger:
- Why Problematic:
- Correct Response:

**EC-03**
- Trigger:
- Why Problematic:
- Correct Response:

---

### CROSS-PROCESS INTERACTIONS

*Identify at least one point where this lifecycle hands off to or receives from an adjacent process.*

| Sending Phase | Sending State -- S-ID | Receiving Process | Data Payload | Expected Acknowledgment |
|---------------|-----------------------|-------------------|--------------|------------------------|
| | | | | |

---

### SLA ANALYSIS

*Annotate at least 3 states or transitions with SLA targets and typical durations. Mark any node where typical duration exceeds or approaches the SLA target as AT-RISK. Cross-reference each AT-RISK row to the bottleneck ID (B-NN) that causes the delay.*

| State Name -- S-ID | SLA Target | Typical Duration | Status | Bottleneck Cross-Ref |
|--------------------|------------|-----------------|--------|---------------------|
| | | | AT-RISK / ON-TRACK | B-NN |

---

## CHAIN STATUS

*STRUCTURAL CONSTRAINT: Do not embed chain status as a line or annotation inside the SLA ANALYSIS section. This section must be a dedicated top-level section with CHAIN STATUS as its first output element.*

CHAIN STATUS: [CLOSED / OPEN]

Forward (SLA → B): [For each AT-RISK row in SLA ANALYSIS, confirm it cites a B-ID. List: "S-NN [State name] cites B-NN". If any AT-RISK row lacks a B-ID cross-reference, declare OPEN and name the gap.]

Backward (B → SLA): [For each B-NN in the bottleneck section, confirm its SLA Nodes Affected field names a state that appears as AT-RISK in SLA ANALYSIS. List: "B-NN cites S-NN [State name], confirmed AT-RISK in SLA". If any B-NN cites a state that is not AT-RISK in SLA ANALYSIS, declare OPEN and name the gap.]

---

### BOTTLENECK AND GAP ANALYSIS

*The Evidence field in each B-NN block must list the specific AT-RISK SLA rows that cite this B-ID, using the format `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`. A field containing only "see SLA ANALYSIS" or state names without S-ID and AT-RISK row-level specificity does not satisfy. Concrete example: `S-05: Credit Hold Review -- AT-RISK, causal source: B-01`.*

**B-01**
- Cause: [what structural or operational condition causes delay to accumulate here]
- Downstream Impact: [which subsequent states or phases are blocked or delayed]
- SLA Nodes Affected: [state names and S-IDs from SLA ANALYSIS whose AT-RISK flags are caused by this bottleneck]
- Evidence: [list each AT-RISK SLA row that cites B-01, using the format above — e.g., `S-05: Credit Hold Review -- AT-RISK, causal source: B-01`; a field containing only "see SLA ANALYSIS" or state names without AT-RISK row-level S-ID specificity does not satisfy]

**B-02**
- Cause:
- Downstream Impact:
- SLA Nodes Affected:
- Evidence: [list each AT-RISK SLA row that cites B-02 — e.g., `S-09: Invoice Approval -- AT-RISK, causal source: B-02`; do not write only "see SLA ANALYSIS"]

**Gaps:**

**G-01 — MISSING:** [name of the missing step] — [rationale: why this step exists in real-world practice and what risks arise from its absence in the simulated flow]

*(Add G-NN entries for each gap found.)*

---

### TERMINAL STATES

| Terminal State | Type | Reached From |
|----------------|------|-------------|
| [Name] | SUCCESS | [state name(s) that transition here] |
| [Name] | FAILURE | [state name(s) that transition here] |
| [Name] | CANCELLED | [state name(s) that transition here] |

*Every branch in every phase must reach one of these declared terminal states. No path may end in a non-terminal state without a continuation or loop marker.*

---

---

## V-02 — C-26 Isolation: Separated Labeled Evidence Axes

**Axis**: C-26 — Evidence field instruction presents `Required format:` and `Fail condition:` as explicitly labeled, visually distinct sub-fields in both the preamble and each B-NN per-block hint.
**Hypothesis**: C-24 passes (concrete example in both locations). C-25 passes (anti-embedding in both locations). C-26 passes (both axes independently labeled).

---

You are simulating a multi-step business document lifecycle for the topic: **{topic}**.

---

### PREAMBLE — Read before generating any content

**Process auto-detection.** Identify the process type from {topic} (L2O = Lead-to-Order; P2P = Procure-to-Pay; PC = Period Close; CL = Case Lifecycle). All roles, states, and exception flows must be specific to that process type.

**Anti-embedding constraint.** Do not embed the CHAIN STATUS declaration as a line or annotation inside the SLA ANALYSIS section. CHAIN STATUS must appear as the first line of a dedicated `## CHAIN STATUS` section that is not nested under SLA ANALYSIS or any other section.

**Evidence field format contract.** Each B-NN answer block in BOTTLENECK AND GAP ANALYSIS contains an Evidence sub-field. That field must list the specific AT-RISK SLA rows that cite the B-ID.

Required format: `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`

Fail condition: A field containing only "see SLA ANALYSIS", a general statement like "multiple AT-RISK rows", or state names without S-ID and AT-RISK row-level specificity does not satisfy. Example of a passing entry: `S-05: Credit Hold Review -- AT-RISK, causal source: B-01`.

**Exception-first ordering.** Within every phase block, SECTION A (exceptions) must appear before SECTION B (states). The ordinal label encodes this ordering as a structural constraint.

---

### ROLE REGISTRY

Declare all domain-specific roles before tracing any state.

| R-ID | Role Name | Function | Anti-Generic Check |
|------|-----------|----------|--------------------|
| R-01 | [process-specific role — no generic "Approver"] | [function] | [confirm non-generic] |
| R-02 | ... | ... | ... |

*L2O roles: Account Executive, Credit Analyst, Contract Manager, Sales Operations, Finance Controller. P2P roles: Procurement Specialist, Vendor Manager, AP Clerk, Receiving Inspector, Finance Controller. PC roles: GL Accountant, Controller, Audit Lead, CFO. CL roles: Case Manager, Legal Counsel, Support Analyst, Operations Lead.*

---

### PHASE 1 — [Auto-name from process context]

#### SECTION A — EXCEPTIONS

*Generate all exception flows originating in this phase before any states. One constructed-answer block per exception flow. Minimum 2 per phase.*

**EX-1A**
- Trigger: [specific entry condition — name the state and triggering field/event]
- Trace: [state sequence from trigger to terminal]
- Handling Role: [R-ID: Role Name]
- Terminal: [terminal state name]
- Why Problematic: [specific operational and business impact]

**EX-1B**
- Trigger:
- Trace:
- Handling Role:
- Terminal:
- Why Problematic:

#### SECTION B — STATES

| State Name -- S-ID | Type | Entry Condition | Exits |
|--------------------|------|-----------------|-------|
| | START / PROCESSING / DECISION / WAIT / PARALLEL-FORK / PARALLEL-JOIN / TERMINAL | [named entry condition] | → S-NN on [condition] |

**Decision Supplement Block — D-[S-ID]** *(one per DECISION-type state)*
- Condition: [rule evaluated at this decision point]
- Owner: [R-ID: Role Name]
- Branch YES: → [State name -- S-ID]
- Branch NO: → [State name -- S-ID]
- Fallback: → [State name -- S-ID] *(required; do not omit)*

**Parallel Work Streams** *(if applicable)*
- Fork at: [S-ID] — Fork type: AND-fork / OR-fork
- Stream 1: [name] — States: [S-ID list]
- Stream 2: [name] — States: [S-ID list]
- Join at: [S-ID] — Join condition: AND-join / OR-join

---

### PHASE 2 — [Auto-name]

#### SECTION A — EXCEPTIONS

**EX-2A**
- Trigger:
- Trace:
- Handling Role:
- Terminal:
- Why Problematic:

**EX-2B**
- Trigger:
- Trace:
- Handling Role:
- Terminal:
- Why Problematic:

#### SECTION B — STATES

| State Name -- S-ID | Type | Entry Condition | Exits |
|--------------------|------|-----------------|-------|

*(Continue phases until all paths reach terminal states.)*

---

### EDGE CASES

*At least 3 edge cases, each distinct from the exception flows above.*

**EC-01**
- Trigger:
- Why Problematic:
- Correct Response:

**EC-02**
- Trigger:
- Why Problematic:
- Correct Response:

**EC-03**
- Trigger:
- Why Problematic:
- Correct Response:

---

### CROSS-PROCESS INTERACTIONS

| Sending Phase | Sending State -- S-ID | Receiving Process | Data Payload | Expected Acknowledgment |
|---------------|-----------------------|-------------------|--------------|------------------------|

---

### SLA ANALYSIS

*At least 3 nodes annotated with SLA target, typical duration, status (AT-RISK / ON-TRACK), and bottleneck cross-reference. AT-RISK rows must cite a B-ID from BOTTLENECK AND GAP ANALYSIS.*

| State Name -- S-ID | SLA Target | Typical Duration | Status | Bottleneck Cross-Ref |
|--------------------|------------|-----------------|--------|---------------------|

---

## CHAIN STATUS

*STRUCTURAL CONSTRAINT: Do not embed the CHAIN STATUS declaration as a sub-element of SLA ANALYSIS or any other section. This section is a first-class top-level section. CHAIN STATUS is the first output element below this heading.*

CHAIN STATUS: [CLOSED / OPEN]

Forward (SLA → B): [Each AT-RISK row in SLA ANALYSIS cites a B-ID — enumerate each: "S-NN [State] cites B-NN". Declare OPEN if any AT-RISK row lacks a B-ID.]

Backward (B → SLA): [Each B-NN entry's SLA Nodes Affected field names a state confirmed AT-RISK in SLA ANALYSIS — enumerate each: "B-NN cites S-NN [State], AT-RISK confirmed". Declare OPEN if any B-NN's cited state is absent from AT-RISK rows.]

---

### BOTTLENECK AND GAP ANALYSIS

*Each B-NN block's Evidence sub-field must satisfy both axes independently. The format specification and the fail condition are listed as separate labeled elements below.*

Required format (Evidence field): `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`

Fail condition (Evidence field): A field entry of "see SLA ANALYSIS", an unlabeled state name, or a state reference without an explicit AT-RISK tag and S-ID does not satisfy. Passing example: `S-05: Credit Hold Review -- AT-RISK, causal source: B-01`.

---

**B-01**
- Cause: [structural or operational cause of delay]
- Downstream Impact: [which states/phases are blocked or degraded]
- SLA Nodes Affected: [state name(s) and S-ID(s) from SLA ANALYSIS affected by this bottleneck]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: A field with "see SLA ANALYSIS" or state names without AT-RISK row-level S-ID specificity does not satisfy.
  - [List each qualifying row, e.g.: `S-05: Credit Hold Review -- AT-RISK, causal source: B-01`]

**B-02**
- Cause:
- Downstream Impact:
- SLA Nodes Affected:
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: A field with "see SLA ANALYSIS" or state names without S-ID and AT-RISK row-level specificity does not satisfy.
  - [List each qualifying row, e.g.: `S-09: Invoice Approval -- AT-RISK, causal source: B-02`]

**Gaps:**

**G-01 — MISSING:** [step name] — [rationale: why this step exists in practice and what operational risk its absence creates]

---

### TERMINAL STATES

| Terminal State | Type | Reached From |
|----------------|------|-------------|
| [Name] | SUCCESS | |
| [Name] | FAILURE | |
| [Name] | CANCELLED | |

---

---

## V-03 — C-24 Isolation: Preamble-Only Concrete Example

**Axis**: C-24 — The preamble carries the full concrete named domain example and labeled fail condition. Per-block Evidence hints reference the preamble without repeating a concrete filled-in example.
**Hypothesis**: C-22 passes (preamble has concrete example + fail condition). C-24 fails (per-block lacks an independent concrete filled-in example; only a reference to preamble). C-25 passes (anti-embedding in both locations). C-26 passes in preamble (labeled axes); per-block reference inherits but does not independently satisfy.

---

You are simulating a multi-step business document lifecycle for the topic: **{topic}**.

---

### PREAMBLE — Read before generating any content

**Process auto-detection.** Identify the process type from {topic}. All roles, states, and exception flows must be specific to that process type.

**Anti-embedding constraint.** Do not embed the CHAIN STATUS declaration as a line or annotation inside the SLA ANALYSIS section. CHAIN STATUS must appear as the first line of a dedicated `## CHAIN STATUS` top-level section.

**Evidence field format contract.** Each B-NN answer block in BOTTLENECK AND GAP ANALYSIS must include a named Evidence sub-field listing the specific AT-RISK SLA rows that cite that B-ID.

Required format: `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`

Fail condition: A field containing only "see SLA ANALYSIS", a general phrase like "multiple AT-RISK entries", or state names without S-ID and AT-RISK row-level specificity does not satisfy. Passing example: `S-05: Credit Hold Review -- AT-RISK, causal source: B-01`.

When generating each B-NN Evidence field, follow the format and example declared above.

**Exception-first ordering.** SECTION A (exceptions) must appear before SECTION B (states) within every phase block.

---

### ROLE REGISTRY

| R-ID | Role Name | Function | Anti-Generic Check |
|------|-----------|----------|--------------------|
| R-01 | [process-specific role] | [function] | [non-generic confirmed] |
| R-02 | ... | ... | ... |

---

### PHASE 1 — [Auto-name]

#### SECTION A — EXCEPTIONS

**EX-1A**
- Trigger:
- Trace:
- Handling Role:
- Terminal:
- Why Problematic:

**EX-1B**
- Trigger:
- Trace:
- Handling Role:
- Terminal:
- Why Problematic:

#### SECTION B — STATES

| State Name -- S-ID | Type | Entry Condition | Exits |
|--------------------|------|-----------------|-------|

**Decision Supplement Block — D-[S-ID]**
- Condition:
- Owner: [R-ID: Role Name]
- Branch YES: →
- Branch NO: →
- Fallback: → *(required)*

**Parallel Work Streams** *(if applicable)*
- Fork at: [S-ID] — Fork type:
- Stream 1: — States:
- Stream 2: — States:
- Join at: [S-ID] — Join condition:

---

### PHASE 2 — [Auto-name]

#### SECTION A — EXCEPTIONS

**EX-2A**
- Trigger:
- Trace:
- Handling Role:
- Terminal:
- Why Problematic:

**EX-2B**
- Trigger:
- Trace:
- Handling Role:
- Terminal:
- Why Problematic:

#### SECTION B — STATES

| State Name -- S-ID | Type | Entry Condition | Exits |
|--------------------|------|-----------------|-------|

*(Continue phases until all paths reach terminal states.)*

---

### EDGE CASES

**EC-01**
- Trigger:
- Why Problematic:
- Correct Response:

**EC-02**
- Trigger:
- Why Problematic:
- Correct Response:

**EC-03**
- Trigger:
- Why Problematic:
- Correct Response:

---

### CROSS-PROCESS INTERACTIONS

| Sending Phase | Sending State -- S-ID | Receiving Process | Data Payload | Expected Acknowledgment |
|---------------|-----------------------|-------------------|--------------|------------------------|

---

### SLA ANALYSIS

| State Name -- S-ID | SLA Target | Typical Duration | Status | Bottleneck Cross-Ref |
|--------------------|------------|-----------------|--------|---------------------|

---

## CHAIN STATUS

*STRUCTURAL CONSTRAINT: Do not embed chain status inside the SLA ANALYSIS section. This is a dedicated top-level section. CHAIN STATUS is declared as the first output element of this section.*

CHAIN STATUS: [CLOSED / OPEN]

Forward (SLA → B): [Enumerate each AT-RISK row and the B-ID it cites.]

Backward (B → SLA): [Enumerate each B-NN entry and confirm its cited SLA states appear as AT-RISK rows.]

---

### BOTTLENECK AND GAP ANALYSIS

*For the Evidence sub-field in each B-NN block, follow the format contract declared in the preamble above: `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`. See the preamble for the full contract and passing example.*

**B-01**
- Cause:
- Downstream Impact:
- SLA Nodes Affected: [state name(s) and S-IDs from SLA ANALYSIS affected by this bottleneck]
- Evidence: [list each AT-RISK SLA row citing B-01 using the preamble format — follow the format contract above]

**B-02**
- Cause:
- Downstream Impact:
- SLA Nodes Affected:
- Evidence: [list each AT-RISK SLA row citing B-02 using the preamble format — follow the format contract above]

**Gaps:**

**G-01 — MISSING:** [step name] — [rationale]

---

### TERMINAL STATES

| Terminal State | Type | Reached From |
|----------------|------|-------------|
| [Name] | SUCCESS | |
| [Name] | FAILURE | |
| [Name] | CANCELLED | |

---

---

## V-04 — C-24 Isolation: Per-Block-Only Concrete Example

**Axis**: C-24 — Per-block Evidence hints carry the full concrete named domain example, labeled axes, and explicit fail condition. The preamble carries only a bracket template without a filled-in domain example.
**Hypothesis**: C-22 fails (preamble has no concrete named domain example — bracket template only). C-24 fails by C-22 dependency (preamble location cannot be satisfied with a bracket template). C-25 passes (anti-embedding in both locations). C-26 passes in per-block (labeled axes present); but C-26 also depends on C-22 and therefore fails.

---

You are simulating a multi-step business document lifecycle for the topic: **{topic}**.

---

### PREAMBLE — Read before generating any content

**Process auto-detection.** Identify the process type from {topic}. All output must be specific to that process type.

**Anti-embedding constraint.** Do not embed the CHAIN STATUS declaration as a line or annotation inside the SLA ANALYSIS section. CHAIN STATUS must appear as the first line of a dedicated `## CHAIN STATUS` top-level section.

**Evidence field format.** Each B-NN block in BOTTLENECK AND GAP ANALYSIS must include an Evidence sub-field. The field must list specific AT-RISK SLA rows that cite that B-ID using the pattern `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`.

**Exception-first ordering.** SECTION A (exceptions) must appear before SECTION B (states) within each phase block.

---

### ROLE REGISTRY

| R-ID | Role Name | Function | Anti-Generic Check |
|------|-----------|----------|--------------------|
| R-01 | [process-specific role] | [function] | [non-generic confirmed] |
| R-02 | ... | ... | ... |

---

### PHASE 1 — [Auto-name]

#### SECTION A — EXCEPTIONS

**EX-1A**
- Trigger:
- Trace:
- Handling Role:
- Terminal:
- Why Problematic:

**EX-1B**
- Trigger:
- Trace:
- Handling Role:
- Terminal:
- Why Problematic:

#### SECTION B — STATES

| State Name -- S-ID | Type | Entry Condition | Exits |
|--------------------|------|-----------------|-------|

**Decision Supplement Block — D-[S-ID]**
- Condition:
- Owner: [R-ID: Role Name]
- Branch YES: →
- Branch NO: →
- Fallback: → *(required)*

**Parallel Work Streams** *(if applicable)*
- Fork at: — Fork type:
- Stream 1: — States:
- Stream 2: — States:
- Join at: — Join condition:

---

### PHASE 2 — [Auto-name]

#### SECTION A — EXCEPTIONS

**EX-2A**
- Trigger:
- Trace:
- Handling Role:
- Terminal:
- Why Problematic:

**EX-2B**
- Trigger:
- Trace:
- Handling Role:
- Terminal:
- Why Problematic:

#### SECTION B — STATES

| State Name -- S-ID | Type | Entry Condition | Exits |
|--------------------|------|-----------------|-------|

*(Continue phases until all paths reach terminal states.)*

---

### EDGE CASES

**EC-01**
- Trigger:
- Why Problematic:
- Correct Response:

**EC-02**
- Trigger:
- Why Problematic:
- Correct Response:

**EC-03**
- Trigger:
- Why Problematic:
- Correct Response:

---

### CROSS-PROCESS INTERACTIONS

| Sending Phase | Sending State -- S-ID | Receiving Process | Data Payload | Expected Acknowledgment |
|---------------|-----------------------|-------------------|--------------|------------------------|

---

### SLA ANALYSIS

| State Name -- S-ID | SLA Target | Typical Duration | Status | Bottleneck Cross-Ref |
|--------------------|------------|-----------------|--------|---------------------|

---

## CHAIN STATUS

*STRUCTURAL CONSTRAINT: Do not embed chain status inside the SLA ANALYSIS section or any other section. This is a dedicated top-level section. CHAIN STATUS is the first output element of this section.*

CHAIN STATUS: [CLOSED / OPEN]

Forward (SLA → B): [Enumerate each AT-RISK row and the B-ID cited.]

Backward (B → SLA): [Enumerate each B-NN and confirm its SLA impact states appear AT-RISK in SLA ANALYSIS.]

---

### BOTTLENECK AND GAP ANALYSIS

**B-01**
- Cause:
- Downstream Impact:
- SLA Nodes Affected:
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without explicit AT-RISK and S-ID row-level specificity does not satisfy. Passing example: `S-05: Credit Hold Review -- AT-RISK, causal source: B-01`.
  - [List each qualifying AT-RISK row citing B-01]

**B-02**
- Cause:
- Downstream Impact:
- SLA Nodes Affected:
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without S-ID and AT-RISK row-level specificity does not satisfy. Passing example: `S-09: Invoice Approval -- AT-RISK, causal source: B-02`.
  - [List each qualifying AT-RISK row citing B-02]

**Gaps:**

**G-01 — MISSING:** [step name] — [rationale]

---

### TERMINAL STATES

| Terminal State | Type | Reached From |
|----------------|------|-------------|
| [Name] | SUCCESS | |
| [Name] | FAILURE | |
| [Name] | CANCELLED | |

---

---

## V-05 — Full R6 Synthesis: Dual-Location Labeled Axes

**Axis**: Combination — All three new criteria enforced at both locations simultaneously: labeled Evidence axes (`Required format:` / `Fail condition:` as distinct labeled sub-fields) in preamble AND per-block; concrete domain example in preamble AND per-block; anti-embedding prohibition in preamble AND CHAIN STATUS section opening.
**Hypothesis**: C-24 passes (concrete example at both locations). C-25 passes (anti-embedding at both locations). C-26 passes (both axes independently labeled at both locations). All C-01–C-26 pass. Golden candidate for R6.

---

You are simulating a multi-step business document lifecycle for the topic: **{topic}**.

---

### PREAMBLE — Read before generating any content

**Process auto-detection.** Identify the process type from {topic} (L2O = Lead-to-Order; P2P = Procure-to-Pay; PC = Period Close; CL = Case Lifecycle). All roles, states, decision points, and exception flows must be specific to that process type. Reject any generic role name (Approver, Owner, Actor) not qualified by domain function.

**Anti-embedding constraint.** Do not embed the CHAIN STATUS declaration as a line or annotation inside the SLA ANALYSIS section. CHAIN STATUS must appear as the first line of a dedicated `## CHAIN STATUS` top-level section that is structurally independent of SLA ANALYSIS.

**Evidence field format contract.** Each B-NN answer block in BOTTLENECK AND GAP ANALYSIS must include a named Evidence sub-field listing the specific AT-RISK SLA rows that cite that B-ID. The format contract has two independently verifiable axes:

Required format: `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`

Fail condition: A field containing only "see SLA ANALYSIS", a general phrase such as "multiple AT-RISK entries", or state names without an explicit AT-RISK tag and S-ID specificity does not satisfy. Passing example: `S-05: Credit Hold Review -- AT-RISK, causal source: B-01`.

**Exception-first ordering.** Within every phase block, SECTION A (exceptions) must appear before SECTION B (states). The ordinal label is the structural enforcement: SECTION A cannot follow SECTION B within the same phase.

---

### ROLE REGISTRY

*Declare before the first PHASE block. No decision point or approval gate may be assigned a role name not declared in this registry.*

| R-ID | Role Name | Function | Anti-Generic Check |
|------|-----------|----------|--------------------|
| R-01 | [process-specific role — e.g., Credit Analyst for L2O] | [what this role does in this process] | [confirm not generic: "Approver" → FAIL; "Credit Analyst" → PASS] |
| R-02 | ... | ... | ... |
| R-03 | ... | ... | ... |

*Minimum roles by process type: L2O → Account Executive (R-01), Credit Analyst (R-02), Contract Manager (R-03), Finance Controller (R-04); P2P → Procurement Specialist (R-01), AP Clerk (R-02), Receiving Inspector (R-03), Finance Controller (R-04); PC → GL Accountant (R-01), Controller (R-02), Audit Lead (R-03), CFO (R-04); CL → Case Manager (R-01), Legal Counsel (R-02), Support Analyst (R-03), Operations Lead (R-04).*

---

### PHASE 1 — [Auto-name from process context]

#### SECTION A — EXCEPTIONS

*Generate all exception flows originating in this phase before listing any states. One constructed-answer block per exception flow. Minimum 2 per phase. Exception trace must be anchored to this phase.*

**EX-1A**
- Trigger: [specific entry condition — name the state and the field/event that triggers this failure mode]
- Trace: [ordered list of states traversed from trigger to terminal — e.g., S-03 → S-07 → TERMINAL: Order Rejected]
- Handling Role: [R-ID: Role Name]
- Terminal: [terminal state name and type: FAILURE / CANCELLED]
- Why Problematic: [specific operational and business impact for this process type]

**EX-1B**
- Trigger:
- Trace:
- Handling Role:
- Terminal:
- Why Problematic:

*(Add EX-1C and beyond as needed.)*

#### SECTION B — STATES

| State Name -- S-ID | Type | Entry Condition | Exits |
|--------------------|------|-----------------|-------|
| [Name] -- S-01 | START | [named condition that activates the process] | → S-02 on [condition] |
| [Name] -- S-02 | PROCESSING / DECISION / WAIT / PARALLEL-FORK / PARALLEL-JOIN | [condition for entering this state] | → S-NN on [condition]; → S-NN on [exception condition] |

*Every state must have a named entry condition. Every exit must name a destination state or declare TERMINAL.*

**Decision Supplement Block — D-[S-ID]** *(one per DECISION-type state)*
- Condition: [exact rule or field value evaluated at this branch point]
- Owner: [R-ID: Role Name]
- Branch YES: → [State name -- S-ID]
- Branch NO: → [State name -- S-ID]
- Fallback: → [State name -- S-ID] *(required — write this field even if the fallback is an escalation path or error state)*

**Parallel Work Streams** *(if this phase has concurrent paths)*
- Fork at: [S-ID] — Fork type: AND-fork / OR-fork
- Stream 1: [name] — States: [S-ID list]
- Stream 2: [name] — States: [S-ID list]
- Join at: [S-ID] — Join condition: AND-join (both complete) / OR-join (first to complete)

---

### PHASE 2 — [Auto-name]

#### SECTION A — EXCEPTIONS

**EX-2A**
- Trigger:
- Trace:
- Handling Role:
- Terminal:
- Why Problematic:

**EX-2B**
- Trigger:
- Trace:
- Handling Role:
- Terminal:
- Why Problematic:

#### SECTION B — STATES

| State Name -- S-ID | Type | Entry Condition | Exits |
|--------------------|------|-----------------|-------|

*(Decision Supplement Blocks and Parallel Work Streams as needed.)*

---

*(Continue adding phase blocks — SECTION A before SECTION B — until all paths reach declared terminal states.)*

---

### EDGE CASES

*At least 3 edge cases, each distinct from the named exception flows above. An edge case is a scenario that exists in practice but is handled inconsistently or not at all, not a named failure mode already traced in SECTION A.*

**EC-01**
- Trigger: [specific condition that creates this edge case]
- Why Problematic: [why the normal flow cannot handle this correctly; what breaks or gets ignored]
- Correct Response: [what the correct handling should produce — state, role, action, outcome]

**EC-02**
- Trigger:
- Why Problematic:
- Correct Response:

**EC-03**
- Trigger:
- Why Problematic:
- Correct Response:

---

### CROSS-PROCESS INTERACTIONS

*At least one inter-process handoff.*

| Sending Phase | Sending State -- S-ID | Receiving Process | Data Payload | Expected Acknowledgment |
|---------------|-----------------------|-------------------|--------------|------------------------|
| | | | | |

---

### SLA ANALYSIS

*At least 3 nodes annotated with SLA target and typical duration. AT-RISK status where typical duration exceeds or approaches SLA. Each AT-RISK row must cite a B-ID from BOTTLENECK AND GAP ANALYSIS.*

| State Name -- S-ID | SLA Target | Typical Duration | Status | Bottleneck Cross-Ref |
|--------------------|------------|-----------------|--------|---------------------|
| | | | AT-RISK / ON-TRACK | B-NN |

---

## CHAIN STATUS

*STRUCTURAL CONSTRAINT: Do not embed the CHAIN STATUS declaration as a sub-element, line, or annotation inside the SLA ANALYSIS section or any other section. This section is a dedicated first-class top-level section. CHAIN STATUS: [CLOSED / OPEN] is the first output element of this section.*

CHAIN STATUS: [CLOSED / OPEN]

Forward (SLA → B): [For each AT-RISK row in SLA ANALYSIS, confirm it cites a B-ID from BOTTLENECK AND GAP ANALYSIS. List each: "S-NN [State name] cites B-NN". If any AT-RISK row lacks a B-ID cross-reference, declare OPEN and name the specific row.]

Backward (B → SLA): [For each B-NN entry in BOTTLENECK AND GAP ANALYSIS, confirm that its SLA Nodes Affected field names a state that appears as AT-RISK in SLA ANALYSIS. List each: "B-NN cites S-NN [State name], confirmed AT-RISK in SLA". If any B-NN cites a state that is not marked AT-RISK in SLA ANALYSIS, declare OPEN and name the specific B-NN.]

---

### BOTTLENECK AND GAP ANALYSIS

*Each B-NN block's Evidence sub-field enforces the format contract on both axes independently. The two axes are labeled below and must appear as separate labeled elements in each B-NN block.*

Required format (Evidence field): `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`

Fail condition (Evidence field): A field entry of "see SLA ANALYSIS", an unlabeled state name, or a state reference without an explicit AT-RISK tag and S-ID does not satisfy. Passing example: `S-05: Credit Hold Review -- AT-RISK, causal source: B-01`.

---

**B-01**
- Cause: [structural or operational condition causing delay to accumulate at this node]
- Downstream Impact: [which subsequent states or phases are blocked, degraded, or delayed by this bottleneck]
- SLA Nodes Affected: [state name(s) and S-IDs from SLA ANALYSIS whose AT-RISK flags are caused by this bottleneck]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without AT-RISK tag and S-ID row-level specificity does not satisfy. Passing example: `S-05: Credit Hold Review -- AT-RISK, causal source: B-01`.
  - [List each qualifying AT-RISK SLA row that cites B-01, one entry per line]

**B-02**
- Cause:
- Downstream Impact:
- SLA Nodes Affected:
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without S-ID and AT-RISK row-level specificity does not satisfy. Passing example: `S-09: Invoice Approval -- AT-RISK, causal source: B-02`.
  - [List each qualifying AT-RISK SLA row that cites B-02]

**Gaps:**

**G-01 — MISSING:** [step name] — [rationale: why this step exists in real-world process practice and what operational or compliance risk its absence in the simulated flow creates]

*(Add G-NN entries for each additional gap.)*

---

### TERMINAL STATES

| Terminal State | Type | Reached From |
|----------------|------|-------------|
| [Name] | SUCCESS | [state name(s) that transition to this terminal] |
| [Name] | FAILURE | [state name(s) that transition to this terminal] |
| [Name] | CANCELLED | [state name(s) that transition to this terminal] |

*Every branch in every phase must reach one of these declared terminal states. No path may end in a non-terminal state without an explicit continuation marker or loop-back label.*

---

---

## Predicted Criterion Matrix

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 through C-21 | PASS | PASS | PASS | PASS | PASS |
| **C-22** Evidence Field Format Contract | PASS | PASS | PASS | **FAIL** (preamble bracket-only) | PASS |
| **C-23** Chain Status Section Isolation | PASS | PASS | PASS | PASS | PASS |
| **C-24** Evidence Field Format Dual Redundancy | PASS | PASS | **FAIL** (per-block reference only, no concrete example) | **FAIL** (→C-22) | PASS |
| **C-25** Anti-Embedding Dual Enforcement | PASS | PASS | PASS | PASS | PASS |
| **C-26** Evidence Field Axis Separation | **FAIL** (merged prose) | PASS | PASS (preamble labeled) | **FAIL** (→C-22) | PASS |

**Ranking prediction:**

| Rank | V | Composite | Expected fails |
|------|---|-----------|---------------|
| 1 | **V-05** | 100.00 | none — golden |
| 2 (tie) | **V-02** | 100.00 | none |
| 3 (tie) | **V-03** | 99.44 | C-24 only |
| 4 | V-01 | 99.44 | C-26 only |
| 5 | V-04 | 98.89 | C-22, C-24, C-26 |

**Key diagnostic:**

- **V-01 vs V-02** isolates C-26: whether merged-prose Evidence axes (one sentence combining format + fail) vs separately labeled sub-fields (`Required format:` / `Fail condition:`) changes the outcome.
- **V-03 vs V-05** isolates C-24 preamble-only: whether per-block Evidence hints that reference preamble without repeating a concrete domain example satisfy C-24's dual-location requirement.
- **V-04** tests the reverse C-24 direction: per-block carries everything but preamble is bracket-template-only. Expected to fail C-22 and cascade-fail C-24 and C-26 by dependency — confirming the preamble remains the load-bearing location established in R5.
