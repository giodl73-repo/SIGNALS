Now I have everything I need. I'll construct all 5 complete variations from the accumulated rubric knowledge (C-01 through C-27, all scorecard history). Writing now.

---

# /quest:variate — flow-lifecycle R7

## V-01 — Axis: Lifecycle Emphasis — Phase-Boundary-First Declaration

**Hypothesis**: Declaring all phase boundaries in a PHASE MAP before any tracing begins makes terminal state coverage (C-05) structural rather than emergent, and narrows gap identification (C-04) to phase-transition seams. C-27 hypothesis: per-block B-NN hint carries "using the format above" back-reference only — no restated labeled axes → **C-27 FAIL**.

---

```
You are a domain process analyst. Simulate the named business document lifecycle end-to-end,
walking every state transition, exception path, and decision point from initial trigger to
terminal state.

Topic: {Topic}
Artifact: simulations/flow/lifecycle/{topic}-lifecycle-{date}.md

─────────────────────────────────────────────────────────
STEP 1 — ROLE REGISTRY  (complete before any state is traced)
─────────────────────────────────────────────────────────

Auto-select domain roles from the declared process type.
Generic names (Approver, Manager, Owner, Actor, User) are prohibited.

Process-type defaults:
  L2O         → Account Executive, Sales Dev Rep, CRM Administrator,
                 Finance Controller, Legal Counsel
  P2P         → Procurement Officer, Receiving Clerk,
                 Accounts Payable Analyst, Finance Controller
  Period Close → General Ledger Accountant, Finance Controller,
                 Internal Auditor, CFO
  Case        → Support Analyst, Case Manager, Operations Lead,
                 Legal Counsel

| R-ID | Role Name | Domain | Decision Authority | Anti-Generic Check |
|------|-----------|--------|-------------------|-------------------|
| R-01 | [domain-specific name] | [Sales/Finance/Ops] | [which gates this role owns] | NOT "Approver" |
| R-02 | | | | |
| R-03 | | | | |
| R-04 | | | | |

Registry gate — do not trace any state until all three are checked:
  [ ] Minimum 3 roles declared
  [ ] All role names domain-specific (no generic names)
  [ ] Every decision point and approval gate has an assigned R-ID

─────────────────────────────────────────────────────────
STEP 2 — PROCESS PROFILE
─────────────────────────────────────────────────────────

Process name: [e.g., Lead-to-Opportunity, Procure-to-Pay, Period Close, Case Lifecycle]
Start state:  [entity + field values at process entry]
End state:    [expected terminal state + required field values]
BPF:          [BPF name and stages, or "None detected"]

─────────────────────────────────────────────────────────
STEP 3 — PHASE MAP  (declare all phases before tracing)
─────────────────────────────────────────────────────────

Declare every phase upfront. The final phase Downstream Handoff must reference a TERMINAL
state. No phase may have an empty Downstream Handoff field.

| Phase | Entry Trigger | Exit Condition | Downstream Handoff | Owner (R-ID) |
|-------|--------------|----------------|-------------------|-------------|
| Phase 1: [name] | [condition that opens this phase] | [condition that closes it] | → Phase 2 | R-[N] |
| Phase 2: [name] | | | → Phase 3 | R-[N] |
| Phase N: [name] | | | → TERMINAL:[name] | R-[N] |

─────────────────────────────────────────────────────────
STEP 4 — TERMINAL STATES  (declare before phase tracing)
─────────────────────────────────────────────────────────

At least one SUCCESS and one FAILURE/CANCEL terminal required.

| Terminal Name | Type | Entered When |
|---------------|------|-------------|
| [e.g., Opportunity Won] | SUCCESS | [condition] |
| [e.g., Lead Disqualified] | FAILURE | [condition] |
| [e.g., Order Cancelled] | CANCEL | [condition] |

─────────────────────────────────────────────────────────
STEP 5 — PHASE TRACES  (repeat for each phase in PHASE MAP)
─────────────────────────────────────────────────────────

━━━ PHASE [N]: [Name] ━━━

Entry trigger: [from PHASE MAP]
Phase owner: R-[N]

### SECTION A — EXCEPTIONS IN THIS PHASE

Generate 2+ exception traces specific to this phase. Each trace originates here
and terminates. "None plausible" is not acceptable if the phase has decision points
or wait states.

**EX-[N]A**
Trigger: [specific condition in this phase that causes the exception]
Trace: [sequence: S-[N]01 → S-[N]02 → TERMINAL:[name]]
Handling Role (R-ID): R-[N]
Terminal: [TERMINAL name]
Why Problematic: [impact on process outcome, downstream phase, or SLA]

**EX-[N]B**
Trigger:
Trace:
Handling Role (R-ID):
Terminal:
Why Problematic:

### SECTION B — STATES IN THIS PHASE

| S-ID | State Name | Type | Entry Condition | Exits | Owner (R-ID) |
|------|-----------|------|----------------|-------|-------------|
| S-[N]01 | [name] | NORMAL | [condition that causes entry] | [cond] → S-[N]02 | R-[N] |
| S-[N]02 | [name] | DECISION | [condition] | YES → S-[N]03 / NO → S-[N]04 | R-[N] |
| S-[N]03 | [name] | TERMINAL | [condition] | TERMINAL:[name] | — |

For each DECISION-type state, add a Decision Supplement Block:

**D-[S-ID]**
Condition evaluated: [the rule or field value being checked]
Owner: R-[N]
Branch YES: → S-[ID] — [outcome description]
Branch NO: → S-[ID] — [outcome description]
Fallback (required — do not omit): → [what happens if neither branch applies]

Parallel Work Streams in This Phase:

| Fork State | Branch A (R-ID) | Branch B (R-ID) | Join Type | Join Condition |
|-----------|----------------|----------------|----------|---------------|
| S-[ID] | [path] (R-[N]) | [path] (R-[N]) | AND / OR | [condition to proceed] |

If sequential: "Sequential — no concurrent branches in this phase. Rationale: [why]"

Phase end: [exit condition from PHASE MAP] → [Next Phase or TERMINAL:[name]]

─────────────────────────────────────────────────────────
STEP 6 — BOTTLENECK AND GAP ANALYSIS
─────────────────────────────────────────────────────────

Evidence field format contract — applies to all B-NN Evidence fields below:

Each B-NN block contains an Evidence sub-field. List every AT-RISK SLA row that
cites this B-ID.

  Required format: [State name -- S-ID]: AT-RISK, causal source: B-[ID]
  Fail condition:  An Evidence field containing only "see SLA ANALYSIS",
                   a summary statement, or state names without S-ID and AT-RISK
                   tag does not satisfy. Each entry must name the state, its S-ID,
                   the AT-RISK label, and the B-ID as causal source.
  Example:         S-05: Credit Hold Review -- AT-RISK, causal source: B-01

**B-01 — [Bottleneck name]**
Cause: [what creates the bottleneck — specific state, role, or system constraint]
Downstream Impact: [delays or failures that cascade from this bottleneck]
SLA Nodes Affected: [which states have AT-RISK timing because of B-01]
Evidence: [list each AT-RISK SLA row citing B-01 — using the format above]

**B-02 — [Bottleneck name]**
Cause:
Downstream Impact:
SLA Nodes Affected:
Evidence: [list each AT-RISK SLA row citing B-02 — using the format above]

Gaps (steps present in real-world practice but missing from the flow):

| G-ID | Missing Step | Phase Where It Belongs | Rationale | Would-Own (R-ID) |
|------|-------------|----------------------|-----------|-----------------|
| G-01 | MISSING: [step description] | Phase [N] | [why this step is required in practice] | R-[N] |

─────────────────────────────────────────────────────────
STEP 7 — SLA ANALYSIS
─────────────────────────────────────────────────────────

Annotate 3+ states or transitions with timing expectations.
Do not embed CHAIN STATUS in this section — it belongs in STEP 8.

| State / Transition | SLA Target | Typical | At-Risk? | Bottleneck Cross-Ref | AT-RISK Note |
|-------------------|-----------|--------|---------|---------------------|-------------|
| S-[ID]: [name] | [e.g., 4h] | [e.g., 6h] | YES | B-01 | S-[ID]: [name] -- AT-RISK, causal source: B-01 |
| S-[ID]: [name] | | | NO | — | — |

─────────────────────────────────────────────────────────
STEP 8 — CHAIN STATUS
─────────────────────────────────────────────────────────

STRUCTURAL CONSTRAINT: Do not embed CHAIN STATUS as a line, annotation, or
sub-block inside the SLA ANALYSIS section. Declare it here as the first output
element of this section.

CHAIN STATUS: [CLOSED / OPEN]

Forward (SLA → Bottleneck):
  [List each AT-RISK SLA row and the B-ID it cites]

Backward (Bottleneck → SLA):
  [List each B-ID and the AT-RISK rows named in its Evidence field]

Gap (if OPEN): [direction incomplete + unresolved ID]

─────────────────────────────────────────────────────────
STEP 9 — CROSS-PROCESS INTERACTIONS
─────────────────────────────────────────────────────────

| Sending Phase / State | Receiving Process | Data Payload | Expected Acknowledgment | Handoff Owner (R-ID) |
|----------------------|-----------------|-------------|------------------------|---------------------|
| Phase [N] / S-[ID] | [process name] | [fields sent] | [expected response or record] | R-[N] |

─────────────────────────────────────────────────────────
STEP 10 — EDGE CASES
─────────────────────────────────────────────────────────

Enumerate 3+ edge cases not already traced in any SECTION A block. Each must have
a distinct trigger and must not duplicate any EX-NN trace.

**EC-01**
Trigger: [condition that creates this edge case]
Why Problematic: [why existing exception flows do not cover it]
Correct Response: [what the process should do]

**EC-02**
Trigger:
Why Problematic:
Correct Response:

**EC-03**
Trigger:
Why Problematic:
Correct Response:

─────────────────────────────────────────────────────────
ARTIFACT
─────────────────────────────────────────────────────────

Write the completed simulation to:
  simulations/flow/lifecycle/{topic}-lifecycle-{date}.md
```

---

## V-02 — Axis: Phrasing Register — Conversational Question Format

**Hypothesis**: Replacing template-slot instructions with direct numbered questions ("For each bottleneck you identify, answer:") lowers formality while retaining structural constraints, and produces more domain-authentic content by forcing constructed answers rather than cell-fill. C-27 hypothesis: Each B-NN question block restates `Required format:` and `Fail condition:` as labeled sub-questions → **C-27 PASS**.

---

```
You are a domain process analyst. Your task: simulate a named business document lifecycle
end-to-end. Answer every numbered question in sequence. Do not skip.

Topic: {Topic}
Artifact: simulations/flow/lifecycle/{topic}-lifecycle-{date}.md

─────────────────────────────────────────────────────────
Q1 — WHO ARE THE DOMAIN ROLES?
─────────────────────────────────────────────────────────

Before you trace a single state, name every domain-specific role involved in this process.
Do not use generic names (Approver, Manager, Owner, Actor). Each role needs an R-ID.

Auto-select from process type:
  L2O → Account Executive, Sales Dev Rep, CRM Administrator, Finance Controller, Legal
  P2P → Procurement Officer, Receiving Clerk, AP Analyst, Finance Controller
  Period Close → GL Accountant, Finance Controller, Internal Auditor, CFO
  Case → Support Analyst, Case Manager, Operations Lead, Legal Counsel

| R-ID | Role Name | Domain | Decision Gates Owned | Anti-Generic Check |
|------|-----------|--------|--------------------|-------------------|
| R-01 | | | | NOT "Approver" |
| R-02 | | | | |
| R-03 | | | | |

Registry gate — check all before proceeding to Q2:
  [ ] 3+ roles declared
  [ ] No generic names
  [ ] Every decision point and approval gate has an R-ID assigned

─────────────────────────────────────────────────────────
Q2 — WHAT IS THE PROCESS?
─────────────────────────────────────────────────────────

Name the process and describe its boundaries.

Process name:
Start state (entity + initial field values):
End state (expected terminal + required fields set):
BPF governing stages (name + stage list, or "None detected"):

─────────────────────────────────────────────────────────
Q3 — WHAT ARE THE TERMINAL STATES?
─────────────────────────────────────────────────────────

Declare all terminal states before tracing phases.

| Terminal Name | Type (SUCCESS / FAILURE / CANCEL) | Entered When |
|--------------|----------------------------------|-------------|
| | SUCCESS | |
| | FAILURE | |
| | CANCEL | |

─────────────────────────────────────────────────────────
Q4 — WHAT HAPPENS IN EACH PHASE?
─────────────────────────────────────────────────────────

Repeat the following block for each process phase.

━━━ PHASE [N]: [Name] ━━━

Q4a: What triggers entry to this phase?
Entry trigger:

Q4b: What are the exception traces specific to this phase?
      (Required: 2+ per phase. Trace from trigger to TERMINAL.)

      1. EXCEPTIONS IN THIS PHASE (SECTION A)

      EX-[N]A
      Trigger: [specific failure condition in this phase]
      Trace: [S-[N]01 → ... → TERMINAL:[name]]
      Handling Role (R-ID): R-[N]
      Terminal: [TERMINAL name]
      Why Problematic: [process impact]

      EX-[N]B
      Trigger:
      Trace:
      Handling Role (R-ID):
      Terminal:
      Why Problematic:

Q4c: What are the states in this phase?

      2. STATES IN THIS PHASE (SECTION B)

      | S-ID | State Name | Type | Entry Condition | Exits | Owner (R-ID) |
      |------|-----------|------|----------------|-------|-------------|
      | | | | | | |

      For each DECISION-type state, answer these five questions:

      D-[S-ID]
      Q1: What condition is being evaluated?
          Condition evaluated:
      Q2: Who evaluates it (R-ID)?
          Owner: R-[N]
      Q3: What happens when the condition is true?
          Branch YES: → S-[ID]
      Q4: What happens when the condition is false?
          Branch NO: → S-[ID]
      Q5: What happens if neither branch applies? (Required — do not skip.)
          Fallback: [explicit fallback path]

Q4d: Are there parallel work streams in this phase?

      | Fork State | Branch A (R-ID) | Branch B (R-ID) | Join Type | Join Condition |
      |-----------|----------------|----------------|----------|---------------|
      | | | | AND / OR | |

      If sequential: "Sequential — no concurrent branches. Rationale: [why]"

Q4e: How does this phase end?
      Phase end condition → [Next Phase or TERMINAL:[name]]

─────────────────────────────────────────────────────────
Q5 — WHERE DO DELAYS ACCUMULATE?  (BOTTLENECK ANALYSIS)
─────────────────────────────────────────────────────────

Identify 2+ bottlenecks. For each, answer the following.

Before completing each B-NN block, read the Evidence field contract:

  Required format:   [State name -- S-ID]: AT-RISK, causal source: B-[ID]
  Fail condition:    An Evidence answer containing only "see SLA ANALYSIS",
                     a general description, or state names without S-ID and
                     AT-RISK tag does not satisfy. Every entry must include:
                     state name, S-ID, AT-RISK label, B-ID as causal source.
  Example:           S-05: Credit Hold Review -- AT-RISK, causal source: B-01

B-01 — [Name this bottleneck]

  Q5a: What causes this bottleneck?
       Cause:
  Q5b: What are the downstream effects?
       Downstream Impact:
  Q5c: Which states have AT-RISK timing because of B-01?
       SLA Nodes Affected:
  Q5d: Which AT-RISK SLA rows cite B-01 as their causal source?
       Evidence:
         Required format:  [State name -- S-ID]: AT-RISK, causal source: B-01
         Fail condition:   Entries without S-ID, AT-RISK label, and "causal
                           source: B-01" do not satisfy.
         [List each qualifying row here]

B-02 — [Name this bottleneck]

  Q5a: Cause:
  Q5b: Downstream Impact:
  Q5c: SLA Nodes Affected:
  Q5d: Evidence:
         Required format:  [State name -- S-ID]: AT-RISK, causal source: B-02
         Fail condition:   Entries without S-ID, AT-RISK label, and "causal
                           source: B-02" do not satisfy.
         [List each qualifying row here]

Q5e: What steps are missing from the documented process?

| G-ID | Missing Step | Phase | Rationale | Would-Own (R-ID) |
|------|-------------|-------|-----------|-----------------|
| G-01 | MISSING: [step] | Phase [N] | [real-world reason this step is needed] | R-[N] |

─────────────────────────────────────────────────────────
Q6 — WHAT IS THE TIMING RISK?  (SLA ANALYSIS)
─────────────────────────────────────────────────────────

Do not declare CHAIN STATUS here — that belongs in Q7.

Annotate 3+ states/transitions with SLA targets vs. typical durations.
Mark AT-RISK where typical exceeds target. Cross-reference to B-ID.

| State / Transition | SLA Target | Typical | At-Risk? | Bottleneck Cross-Ref | AT-RISK Note |
|-------------------|-----------|--------|---------|---------------------|-------------|
| S-[ID]: [name] | | | YES/NO | B-[ID] or — | [State name -- S-ID]: AT-RISK, causal source: B-[ID] |

─────────────────────────────────────────────────────────
Q7 — IS THE EVIDENCE CHAIN CLOSED?  (CHAIN STATUS)
─────────────────────────────────────────────────────────

STRUCTURAL CONSTRAINT: Do not embed CHAIN STATUS inside the SLA ANALYSIS section.
Declare it here as the first answer in this section.

CHAIN STATUS: [CLOSED / OPEN]

Forward (each AT-RISK SLA row → B-ID cited):
  [List each AT-RISK row and the B-ID it references]

Backward (each B-ID → AT-RISK rows in its Evidence field):
  [List each B-ID and the rows named in its Evidence answer]

Gap (if OPEN):
  [Which direction is incomplete and which ID is unresolved]

─────────────────────────────────────────────────────────
Q8 — WHAT CROSSES A PROCESS BOUNDARY?
─────────────────────────────────────────────────────────

| Sending Phase / State | Receiving Process | Data Payload | Expected Acknowledgment | Handoff Owner (R-ID) |
|----------------------|-----------------|-------------|------------------------|---------------------|
| Phase [N] / S-[ID] | | | | R-[N] |

─────────────────────────────────────────────────────────
Q9 — WHAT FALLS THROUGH THE CRACKS?  (EDGE CASES)
─────────────────────────────────────────────────────────

List 3+ edge cases. Each must be distinct from every SECTION A exception trace and have
its own unique trigger.

EC-01
  Trigger: [condition creating this edge case]
  Why Problematic: [why existing exception flows do not cover it]
  Correct Response: [what the process should do when this occurs]

EC-02
  Trigger:
  Why Problematic:
  Correct Response:

EC-03
  Trigger:
  Why Problematic:
  Correct Response:

─────────────────────────────────────────────────────────
ARTIFACT
─────────────────────────────────────────────────────────

Write the completed simulation to:
  simulations/flow/lifecycle/{topic}-lifecycle-{date}.md
```

---

## V-03 — Axis: Role Sequence — Domain-Grouped Registry

**Hypothesis**: Organizing the role registry into domain buckets (Sales / Finance / Operations / Legal) rather than a flat sequential list produces a more accurate process-type match — the model selects from domain buckets rather than generating a homogeneous list, reducing cross-domain role collisions. C-27 hypothesis: B-01 scaffold carries full labeled axes; B-02 scaffold uses minimal back-reference — scaffold asymmetry from R6 Pattern 3 → **C-27 FAIL** (B-02 per-block missing labeled axes).

---

```
You are a domain process analyst. Simulate the named business document lifecycle end-to-end,
tracing every state, exception path, decision point, and parallel stream from initial trigger
to terminal state.

Topic: {Topic}
Artifact: simulations/flow/lifecycle/{topic}-lifecycle-{date}.md

─────────────────────────────────────────────────────────
STEP 1 — DOMAIN-GROUPED ROLE REGISTRY
(complete before any state is traced)
─────────────────────────────────────────────────────────

Declare roles by domain group. Generic names (Approver, Manager, Owner, Actor) are
prohibited in any group. Auto-assign R-IDs sequentially across all groups.

Process-type domain map:
  L2O         → Sales: Account Executive, Sales Dev Rep
                Finance: Finance Controller, Revenue Analyst
                Legal: Legal Counsel
                Operations: CRM Administrator
  P2P         → Procurement: Procurement Officer, Purchase Order Analyst
                Finance: Accounts Payable Analyst, Finance Controller
                Operations: Receiving Clerk, Warehouse Manager
  Period Close → Finance: GL Accountant, Finance Controller, CFO
                Audit: Internal Auditor
                IT: ERP Administrator
  Case        → Support: Support Analyst, Tier 2 Specialist
                Operations: Case Manager, Operations Lead
                Legal: Legal Counsel

GROUP: [Domain A — e.g., Sales]
| R-ID | Role Name | Function | Decision Gates Owned | Anti-Generic Check |
|------|-----------|----------|---------------------|-------------------|
| R-01 | [name] | [function] | [specific gates] | NOT "Approver" |

GROUP: [Domain B — e.g., Finance]
| R-ID | Role Name | Function | Decision Gates Owned | Anti-Generic Check |
|------|-----------|----------|---------------------|-------------------|
| R-02 | [name] | [function] | [specific gates] | NOT "Manager" |

GROUP: [Domain C — e.g., Operations / Legal]
| R-ID | Role Name | Function | Decision Gates Owned | Anti-Generic Check |
|------|-----------|----------|---------------------|-------------------|
| R-03 | [name] | [function] | [specific gates] | NOT "Owner" |

Registry gate — complete before Step 2:
  [ ] All domain groups populated
  [ ] Minimum 3 roles across all groups
  [ ] No generic names in any group
  [ ] All decision points and approval gates have an R-ID assigned

─────────────────────────────────────────────────────────
STEP 2 — PROCESS PROFILE AND TERMINAL STATES
─────────────────────────────────────────────────────────

Process name:
Start state (entity + field values):
End state (expected terminal + required fields):
BPF: [name and stages, or "None detected"]

Active roles in each phase (list R-IDs from registry for each phase):
  Phase 1: R-[N], R-[N]
  Phase 2: R-[N], R-[N]
  Phase N: R-[N], R-[N]

Terminal states (declare before phase tracing):

| Terminal Name | Type | Entered When |
|--------------|------|-------------|
| | SUCCESS | |
| | FAILURE | |
| | CANCEL | |

─────────────────────────────────────────────────────────
STEP 3 — PHASE TRACES  (repeat for each phase)
─────────────────────────────────────────────────────────

━━━ PHASE [N]: [Name] ━━━

Entry trigger: [condition that opens this phase]
Active roles (from registry): R-[N] (primary), R-[N] (supporting)

### SECTION A — EXCEPTIONS IN THIS PHASE

Generate 2+ exception traces specific to this phase.

**EX-[N]A**
Trigger: [specific failure condition in this phase]
Trace: [S-[N]01 → ... → TERMINAL:[name]]
Handling Role (R-ID): R-[N]
Terminal: [TERMINAL name]
Why Problematic: [impact on outcome or downstream phase]

**EX-[N]B**
Trigger:
Trace:
Handling Role (R-ID):
Terminal:
Why Problematic:

### SECTION B — STATES IN THIS PHASE

| S-ID | State Name | Type | Entry Condition | Exits | Owner (R-ID) |
|------|-----------|------|----------------|-------|-------------|
| S-[N]01 | [name] | NORMAL | [entry condition] | [cond] → S-[N]02 | R-[N] |
| S-[N]02 | [name] | DECISION | [entry condition] | YES → S-[N]03 / NO → S-[N]04 | R-[N] |

For each DECISION-type state, add a Decision Supplement Block:

**D-[S-ID]**
Condition evaluated: [rule being checked]
Owner: R-[N]
Branch YES: → S-[ID] [outcome]
Branch NO: → S-[ID] [outcome]
Fallback (required — do not omit): [explicit fallback path]

Parallel Work Streams in This Phase:

| Fork State | Branch A (R-ID) | Branch B (R-ID) | Join Type | Join Condition |
|-----------|----------------|----------------|----------|---------------|
| S-[ID] | [path] (R-[N]) | [path] (R-[N]) | AND / OR | [condition] |

If sequential: "Sequential — no concurrent branches. Rationale: [why]"

Phase end: [exit condition] → [Next Phase or TERMINAL:[name]]

─────────────────────────────────────────────────────────
STEP 4 — BOTTLENECK AND GAP ANALYSIS
─────────────────────────────────────────────────────────

Evidence field format contract — applies to all B-NN blocks:

Each B-NN block must include an Evidence sub-field listing the specific AT-RISK
SLA rows that cite this B-ID.

  Required format: [State name -- S-ID]: AT-RISK, causal source: B-[ID]
  Fail condition:  An Evidence field containing only "see SLA ANALYSIS",
                   state names without S-ID, or a general summary does not
                   satisfy. Each entry must include state name, S-ID, the
                   AT-RISK tag, and B-ID as causal source.
  Example:         S-05: Credit Hold Review -- AT-RISK, causal source: B-01

**B-01 — [Bottleneck name]**
Cause: [what creates the bottleneck — specific state, role, or system]
Downstream Impact: [cascading delays or failure modes]
SLA Nodes Affected: [states with AT-RISK timing caused by B-01]
Evidence:
  Required format: [State name -- S-ID]: AT-RISK, causal source: B-01
  Fail condition:  Entries without S-ID and AT-RISK tag do not satisfy.
  [List each qualifying AT-RISK SLA row here]

**B-02 — [Bottleneck name]**
Cause:
Downstream Impact:
SLA Nodes Affected:
Evidence: [list each AT-RISK SLA row citing B-02 — using the format above]

Gaps (steps present in real-world practice, absent from the documented flow):

| G-ID | Missing Step | Phase | Rationale | Would-Own (R-ID) |
|------|-------------|-------|-----------|-----------------|
| G-01 | MISSING: [step] | Phase [N] | [why this step exists in practice] | R-[N] |

─────────────────────────────────────────────────────────
STEP 5 — SLA ANALYSIS
─────────────────────────────────────────────────────────

Annotate 3+ states or transitions with timing expectations.
Do not embed CHAIN STATUS here.

| State / Transition | SLA Target | Typical | At-Risk? | Bottleneck Cross-Ref | AT-RISK Note |
|-------------------|-----------|--------|---------|---------------------|-------------|
| S-[ID]: [name] | | | YES/NO | B-[ID] or — | [State name -- S-ID]: AT-RISK, causal source: B-[ID] |

─────────────────────────────────────────────────────────
STEP 6 — CHAIN STATUS
─────────────────────────────────────────────────────────

STRUCTURAL CONSTRAINT: Do not embed CHAIN STATUS inside the SLA ANALYSIS section.
This is its own dedicated section. Declare it as the first element here.

CHAIN STATUS: [CLOSED / OPEN]

Forward (SLA → Bottleneck):
  [Each AT-RISK row and the B-ID it cites]

Backward (Bottleneck → SLA):
  [Each B-ID and the AT-RISK rows in its Evidence field]

Gap (if OPEN): [incomplete direction + unresolved ID]

─────────────────────────────────────────────────────────
STEP 7 — CROSS-PROCESS INTERACTIONS
─────────────────────────────────────────────────────────

| Sending Phase / State | Receiving Process | Data Payload | Expected Acknowledgment | Handoff Owner (R-ID) |
|----------------------|-----------------|-------------|------------------------|---------------------|
| Phase [N] / S-[ID] | [process name] | [fields sent] | [expected response] | R-[N] |

─────────────────────────────────────────────────────────
STEP 8 — EDGE CASES
─────────────────────────────────────────────────────────

Enumerate 3+ edge cases not covered by any SECTION A exception trace.
Each must have a distinct trigger.

**EC-01**
Trigger: [condition creating this edge case]
Why Problematic: [why existing exception flows do not cover it]
Correct Response: [what the process should do]

**EC-02**
Trigger:
Why Problematic:
Correct Response:

**EC-03**
Trigger:
Why Problematic:
Correct Response:

─────────────────────────────────────────────────────────
ARTIFACT
─────────────────────────────────────────────────────────

Write the completed simulation to:
  simulations/flow/lifecycle/{topic}-lifecycle-{date}.md
```

---

## V-04 — Combination: Lifecycle Emphasis + Role Sequence

**Hypothesis**: Combining a PHASE MAP upfront (V-01 axis) with a domain-grouped role registry (V-03 axis) and adding per-phase role activation lists produces the strongest terminal state and role coverage without structural conflict. Both B-01 and B-02 scaffolds carry full labeled axes → **C-27 PASS**.

---

```
You are a domain process analyst. Simulate the named business document lifecycle end-to-end.
The simulation traces every state, exception path, decision point, parallel stream, and
timing risk from initial trigger to declared terminal state.

Topic: {Topic}
Artifact: simulations/flow/lifecycle/{topic}-lifecycle-{date}.md

─────────────────────────────────────────────────────────
STEP 1 — DOMAIN-GROUPED ROLE REGISTRY
(complete before any state is traced)
─────────────────────────────────────────────────────────

Organize roles by domain group. No generic names (Approver, Manager, Owner, Actor).
Each role must own at least one named decision point or approval gate.

Process-type domain map:
  L2O         → Sales: Account Executive, Sales Dev Rep
                Finance: Finance Controller, Revenue Analyst
                Legal/Compliance: Legal Counsel
                Platform: CRM Administrator
  P2P         → Procurement: Procurement Officer, PO Analyst
                Finance: AP Analyst, Finance Controller
                Operations: Receiving Clerk, Warehouse Manager
  Period Close → Finance: GL Accountant, Finance Controller, CFO
                Audit: Internal Auditor
                IT/Platform: ERP Administrator
  Case        → Support: Support Analyst, Tier 2 Specialist
                Operations: Case Manager, Operations Lead
                Legal: Legal Counsel

GROUP: [Domain A]
| R-ID | Role Name | Domain | Decision Gates Owned | Anti-Generic Check |
|------|-----------|--------|---------------------|-------------------|
| R-01 | [name] | [domain] | [gates] | NOT "Approver" |

GROUP: [Domain B]
| R-ID | Role Name | Domain | Decision Gates Owned | Anti-Generic Check |
|------|-----------|--------|---------------------|-------------------|
| R-02 | [name] | [domain] | [gates] | NOT "Manager" |

GROUP: [Domain C]
| R-ID | Role Name | Domain | Decision Gates Owned | Anti-Generic Check |
|------|-----------|--------|---------------------|-------------------|
| R-03 | [name] | [domain] | [gates] | NOT "Owner" |

Registry gate — complete before Step 2:
  [ ] All domain groups populated
  [ ] Minimum 3 roles, no generic names
  [ ] Every decision point and approval gate assigned an R-ID

─────────────────────────────────────────────────────────
STEP 2 — PROCESS PROFILE
─────────────────────────────────────────────────────────

Process name:
Start state (entity + field values):
End state (expected terminal + fields set):
BPF: [name + stages, or "None detected"]

─────────────────────────────────────────────────────────
STEP 3 — PHASE MAP  (declare all phases before tracing)
─────────────────────────────────────────────────────────

Every phase must have an Entry Trigger, Exit Condition, and Downstream Handoff.
Final phase Downstream Handoff must reference a TERMINAL state by name.
Specify active roles (R-IDs) for each phase — drives per-phase role activation.

| Phase | Entry Trigger | Exit Condition | Downstream Handoff | Active Roles (R-IDs) |
|-------|--------------|----------------|-------------------|---------------------|
| Phase 1: [name] | [condition] | [condition] | → Phase 2 | R-01, R-02 |
| Phase 2: [name] | | | → Phase 3 | R-02, R-03 |
| Phase N: [name] | | | → TERMINAL:[name] | R-[N] |

─────────────────────────────────────────────────────────
STEP 4 — TERMINAL STATES
─────────────────────────────────────────────────────────

Declare before phase tracing. At least one SUCCESS and one FAILURE/CANCEL required.
Every branch in every phase section must reach a declared terminal state.

| Terminal Name | Type | Entered When |
|--------------|------|-------------|
| | SUCCESS | |
| | FAILURE | |
| | CANCEL | |

─────────────────────────────────────────────────────────
STEP 5 — PHASE TRACES  (repeat for each phase in PHASE MAP)
─────────────────────────────────────────────────────────

━━━ PHASE [N]: [Name] ━━━

Entry trigger: [from PHASE MAP]
Active roles: R-[N] (primary), R-[N] (supporting)  ← from PHASE MAP

### SECTION A — EXCEPTIONS IN THIS PHASE

Generate 2+ exception traces specific to this phase. "None plausible" is not acceptable
if the phase contains a decision point or wait state.

**EX-[N]A**
Trigger: [specific failure condition in this phase]
Trace: [S-[N]01 → ... → TERMINAL:[name]]
Handling Role (R-ID): R-[N]
Terminal: [TERMINAL name]
Why Problematic: [impact on downstream phase or SLA]

**EX-[N]B**
Trigger:
Trace:
Handling Role (R-ID):
Terminal:
Why Problematic:

### SECTION B — STATES IN THIS PHASE

| S-ID | State Name | Type | Entry Condition | Exits | Owner (R-ID) |
|------|-----------|------|----------------|-------|-------------|
| S-[N]01 | [name] | NORMAL | [condition] | [cond] → S-[N]02 | R-[N] |
| S-[N]02 | [name] | DECISION | [condition] | YES → S-[N]03 / NO → S-[N]04 | R-[N] |
| S-[N]03 | [name] | TERMINAL | [condition] | TERMINAL:[name] | — |

For each DECISION-type state, add a Decision Supplement Block immediately below:

**D-[S-ID]**
Condition evaluated: [rule or field value checked]
Owner: R-[N]
Branch YES: → S-[ID] — [outcome description]
Branch NO: → S-[ID] — [outcome description]
Fallback (required — do not omit): [explicit path for unhandled conditions]

Parallel Work Streams in This Phase:

| Fork State | Branch A (R-ID) | Branch B (R-ID) | Join Type | Join Condition |
|-----------|----------------|----------------|----------|---------------|
| S-[ID] | [path] (R-[N]) | [path] (R-[N]) | AND / OR | [condition to proceed] |

If sequential: "Sequential — no concurrent branches. Rationale: [why]"

Phase end: [exit condition from PHASE MAP] → [Next Phase or TERMINAL:[name]]

─────────────────────────────────────────────────────────
STEP 6 — BOTTLENECK AND GAP ANALYSIS
─────────────────────────────────────────────────────────

Evidence field format contract — read before completing any B-NN block:

Each B-NN block must include an Evidence sub-field listing the specific AT-RISK
SLA rows that cite this B-ID as causal source.

  Required format: [State name -- S-ID]: AT-RISK, causal source: B-[ID]
  Fail condition:  An Evidence field containing only "see SLA ANALYSIS",
                   a general description, or state names without the S-ID
                   prefix and AT-RISK label does not satisfy. Every entry
                   must name the state, include its S-ID, carry the AT-RISK
                   tag, and identify the B-ID as causal source.
  Example:         S-05: Credit Hold Review -- AT-RISK, causal source: B-01

**B-01 — [Bottleneck name]**
Cause: [what creates the bottleneck — specific state, role, or system]
Downstream Impact: [cascading delays or failure modes from this bottleneck]
SLA Nodes Affected: [states with AT-RISK timing caused by B-01]
Evidence:
  Required format: [State name -- S-ID]: AT-RISK, causal source: B-01
  Fail condition:  Entries lacking S-ID, AT-RISK label, or "causal source:
                   B-01" do not satisfy.
  [List each qualifying AT-RISK SLA row here]

**B-02 — [Bottleneck name]**
Cause:
Downstream Impact:
SLA Nodes Affected:
Evidence:
  Required format: [State name -- S-ID]: AT-RISK, causal source: B-02
  Fail condition:  Entries lacking S-ID, AT-RISK label, or "causal source:
                   B-02" do not satisfy.
  [List each qualifying AT-RISK SLA row here]

Gaps (steps present in real-world practice, absent from the documented flow):

| G-ID | Missing Step | Phase | Rationale | Would-Own (R-ID) |
|------|-------------|-------|-----------|-----------------|
| G-01 | MISSING: [step] | Phase [N] | [why this step is required in practice] | R-[N] |

─────────────────────────────────────────────────────────
STEP 7 — SLA ANALYSIS
─────────────────────────────────────────────────────────

Annotate 3+ states or transitions with timing expectations.
Do not embed CHAIN STATUS in this section — it belongs in Step 8.

| State / Transition | SLA Target | Typical | At-Risk? | Bottleneck Cross-Ref | AT-RISK Note |
|-------------------|-----------|--------|---------|---------------------|-------------|
| S-[ID]: [name] | [target] | [typical] | YES/NO | B-[ID] or — | [name -- S-ID]: AT-RISK, causal source: B-[ID] |

─────────────────────────────────────────────────────────
STEP 8 — CHAIN STATUS
─────────────────────────────────────────────────────────

STRUCTURAL CONSTRAINT: Do not embed CHAIN STATUS as a line, annotation, or
sub-block inside the SLA ANALYSIS section. Declare it here as the first
output element of this dedicated section.

CHAIN STATUS: [CLOSED / OPEN]

Forward (SLA → Bottleneck):
  [Each AT-RISK SLA row and the B-ID it cites]

Backward (Bottleneck → SLA):
  [Each B-ID and the AT-RISK rows in its Evidence field]

Gap (if OPEN): [incomplete direction + unresolved ID]

─────────────────────────────────────────────────────────
STEP 9 — CROSS-PROCESS INTERACTIONS
─────────────────────────────────────────────────────────

| Sending Phase / State | Receiving Process | Data Payload | Expected Acknowledgment | Handoff Owner (R-ID) |
|----------------------|-----------------|-------------|------------------------|---------------------|
| Phase [N] / S-[ID] | [process name] | [fields sent] | [expected record or response] | R-[N] |

─────────────────────────────────────────────────────────
STEP 10 — EDGE CASES
─────────────────────────────────────────────────────────

Enumerate 3+ edge cases not covered by any SECTION A exception trace.
Each must have a distinct trigger and must not duplicate any EX-NN trace.

**EC-01**
Trigger: [condition creating this edge case]
Why Problematic: [why existing flows do not cover it]
Correct Response: [what the process should do]

**EC-02**
Trigger:
Why Problematic:
Correct Response:

**EC-03**
Trigger:
Why Problematic:
Correct Response:

─────────────────────────────────────────────────────────
ARTIFACT
─────────────────────────────────────────────────────────

Write the completed simulation to:
  simulations/flow/lifecycle/{topic}-lifecycle-{date}.md
```

---

## V-05 — Full Synthesis: All Axes

**Hypothesis**: Combining PHASE MAP upfront (lifecycle emphasis), domain-grouped role registry with per-phase activation (role sequence), question-based discovery sections for exceptions and edge cases (phrasing register), table format for states and SLA (output format), and inertia framing ("the existing process map is the baseline — simulation surfaces what it misses") into a single prompt satisfies all 27 criteria without structural conflict. C-27 hypothesis: `Required format:` and `Fail condition:` labeled axes in preamble AND in every B-NN per-block → **C-27 PASS**.

---

```
You are a domain process analyst. Your simulation extends beyond the existing process
documentation. The current process map, SOP, or BPF definition describes the happy path.
Your job is to find what it omits: exception paths the documentation never addresses,
bottlenecks the diagrams don't show, and edge cases that only appear in production.

Topic: {Topic}
Artifact: simulations/flow/lifecycle/{topic}-lifecycle-{date}.md

─────────────────────────────────────────────────────────
STEP 1 — DOMAIN-GROUPED ROLE REGISTRY
(complete before any state is traced)
─────────────────────────────────────────────────────────

Who owns this process? Declare domain-specific roles by group before tracing anything.
Generic names (Approver, Manager, Owner, Actor, User) are not roles — replace them.

Auto-select from process type:
  L2O         → Sales: Account Executive, Sales Dev Rep
                Finance: Finance Controller, Revenue Analyst
                Legal: Legal Counsel | Platform: CRM Administrator
  P2P         → Procurement: Procurement Officer, PO Analyst
                Finance: AP Analyst, Finance Controller
                Operations: Receiving Clerk, Warehouse Manager
  Period Close → Finance: GL Accountant, Finance Controller, CFO
                Audit: Internal Auditor | IT: ERP Administrator
  Case        → Support: Support Analyst, Tier 2 Specialist
                Operations: Case Manager, Operations Lead | Legal: Legal Counsel

GROUP: [Domain A — e.g., Sales / Procurement / Finance]
| R-ID | Role Name | Domain | Decision Gates Owned | Anti-Generic Check |
|------|-----------|--------|---------------------|-------------------|
| R-01 | [specific name] | [domain] | [specific gates] | NOT "Approver" |

GROUP: [Domain B]
| R-ID | Role Name | Domain | Decision Gates Owned | Anti-Generic Check |
|------|-----------|--------|---------------------|-------------------|
| R-02 | [specific name] | [domain] | [specific gates] | NOT "Manager" |

GROUP: [Domain C]
| R-ID | Role Name | Domain | Decision Gates Owned | Anti-Generic Check |
|------|-----------|--------|---------------------|-------------------|
| R-03 | [specific name] | [domain] | [specific gates] | NOT "Owner" |

Registry gate — check all before Step 2:
  [ ] All domain groups populated
  [ ] Minimum 3 roles, no generic names in any group
  [ ] Every decision point and approval gate has an R-ID assigned

─────────────────────────────────────────────────────────
STEP 2 — PROCESS PROFILE
─────────────────────────────────────────────────────────

What does this process do, where does it start, and where does it end?

Process name:
Start state (entity + field values at process entry):
End state (expected terminal state + required fields set):
Existing documentation baseline: [process map name, SOP version, BPF definition — or "None"]
BPF: [name + stages, or "None detected"]

─────────────────────────────────────────────────────────
STEP 3 — PHASE MAP  (declare all phases before tracing)
─────────────────────────────────────────────────────────

Lay out the full process lifecycle before tracing any individual state. Every phase needs
its entry trigger, exit condition, downstream handoff, and the roles active in it.

The final phase Downstream Handoff must reference a TERMINAL state. No phase may have
an empty Downstream Handoff field.

| Phase | Entry Trigger | Exit Condition | Downstream Handoff | Active Roles (R-IDs) |
|-------|--------------|----------------|-------------------|---------------------|
| Phase 1: [name] | [what opens it] | [what closes it] | → Phase 2 | R-01, R-02 |
| Phase 2: [name] | | | → Phase 3 | R-02, R-03 |
| Phase N: [name] | | | → TERMINAL:[name] | R-[N] |

─────────────────────────────────────────────────────────
STEP 4 — TERMINAL STATES  (declare before phase tracing)
─────────────────────────────────────────────────────────

At least one SUCCESS and one FAILURE/CANCEL terminal required.
Every exception trace and every phase-end path must reach a terminal declared here.

| Terminal Name | Type | Entered When |
|--------------|------|-------------|
| | SUCCESS | |
| | FAILURE | |
| | CANCEL | |

─────────────────────────────────────────────────────────
STEP 5 — PHASE TRACES  (repeat for each phase in PHASE MAP)
─────────────────────────────────────────────────────────

━━━ PHASE [N]: [Name] ━━━

Entry trigger: [from PHASE MAP]
Active roles: R-[N] (primary decision owner), R-[N] (supporting)

### SECTION A — EXCEPTIONS IN THIS PHASE

What goes wrong in this phase? Answer the following for each exception trace.
Generate 2+ traces. Each starts in this phase and ends at a terminal state.

**EX-[N]A — What specific failure can happen here?**
Trigger: [condition in this phase that causes the exception]
Trace: [S-[N]01 → S-[N]02 → TERMINAL:[name]]
Handling Role (R-ID): R-[N]
Terminal: [TERMINAL name]
Why Problematic: [impact on outcome, downstream phases, or SLA]

**EX-[N]B — What else can fail here?**
Trigger:
Trace:
Handling Role (R-ID):
Terminal:
Why Problematic:

### SECTION B — STATES IN THIS PHASE

| S-ID | State Name | Type | Entry Condition | Exits | Owner (R-ID) |
|------|-----------|------|----------------|-------|-------------|
| S-[N]01 | [name] | NORMAL | [condition that enters this state] | [cond] → S-[N]02 | R-[N] |
| S-[N]02 | [name] | DECISION | [condition] | YES → S-[N]03 / NO → S-[N]04 | R-[N] |
| S-[N]03 | [name] | TERMINAL | [condition] | TERMINAL:[name] | — |

For each DECISION-type state, answer these five questions:

**D-[S-ID] — Decision point at [State Name]**
What is being decided?
  Condition evaluated: [the rule or field value being checked]
Who decides?
  Owner: R-[N]
What happens if true?
  Branch YES: → S-[ID] — [outcome]
What happens if false?
  Branch NO: → S-[ID] — [outcome]
What happens if neither applies? (Required — do not skip.)
  Fallback: [explicit path for unhandled conditions]

Parallel work streams in this phase?

| Fork State | Branch A (R-ID) | Branch B (R-ID) | Join Type | Join Condition |
|-----------|----------------|----------------|----------|---------------|
| S-[ID] | [path description] (R-[N]) | [path description] (R-[N]) | AND / OR | [condition to proceed] |

If sequential: "Sequential — no concurrent branches. Rationale: [why]"

Phase end: [exit condition from PHASE MAP] → [Next Phase or TERMINAL:[name]]

─────────────────────────────────────────────────────────
STEP 6 — BOTTLENECK AND GAP ANALYSIS
─────────────────────────────────────────────────────────

Where does the existing process documentation underestimate delay?
What steps exist in real-world practice but are absent from the documented flow?

Evidence field format contract — read before completing any B-NN block.
This contract applies to the Evidence sub-field in each bottleneck block below.

  Required format: [State name -- S-ID]: AT-RISK, causal source: B-[ID]
  Fail condition:  An Evidence field containing only "see SLA ANALYSIS",
                   a general summary, or state names without the S-ID prefix
                   and AT-RISK label does not satisfy. Each entry must name
                   the state, include its S-ID, carry the AT-RISK tag, and
                   identify the B-ID as causal source.
  Example:         S-05: Credit Hold Review -- AT-RISK, causal source: B-01

**B-01 — [Name: what is the bottleneck?]**

Where does delay accumulate?
  Cause: [specific state, role, or system constraint creating the bottleneck]
What are the downstream effects?
  Downstream Impact: [cascading delays or failure modes]
Which states carry AT-RISK timing because of B-01?
  SLA Nodes Affected: [state names]
Which AT-RISK SLA rows list B-01 as their causal source?
  Evidence:
    Required format: [State name -- S-ID]: AT-RISK, causal source: B-01
    Fail condition:  Entries without S-ID, AT-RISK label, and "causal
                     source: B-01" do not satisfy.
    [List each qualifying row here]

**B-02 — [Name: what is the bottleneck?]**

Cause:
Downstream Impact:
SLA Nodes Affected:
Evidence:
  Required format: [State name -- S-ID]: AT-RISK, causal source: B-02
  Fail condition:  Entries without S-ID, AT-RISK label, and "causal
                   source: B-02" do not satisfy.
  [List each qualifying row here]

Gaps (the existing documentation's silent omissions):

| G-ID | Missing Step | Phase Where It Belongs | Why the Documented Flow Omits It | Would-Own (R-ID) |
|------|-------------|----------------------|---------------------------------|-----------------|
| G-01 | MISSING: [step] | Phase [N] | [rationale for why it's real but undocumented] | R-[N] |

─────────────────────────────────────────────────────────
STEP 7 — SLA ANALYSIS
─────────────────────────────────────────────────────────

Where does the documented process underestimate timing risk?
Annotate 3+ states or transitions with expected SLA targets vs. typical duration.
Flag AT-RISK where typical exceeds target. Cross-reference to bottleneck B-IDs.
Do not embed CHAIN STATUS in this section — it belongs in Step 8.

| State / Transition | SLA Target | Typical | At-Risk? | Bottleneck Cross-Ref | AT-RISK Note |
|-------------------|-----------|--------|---------|---------------------|-------------|
| S-[ID]: [name] | [target] | [typical] | YES | B-[ID] | [name -- S-ID]: AT-RISK, causal source: B-[ID] |
| S-[ID]: [name] | | | NO | — | — |

─────────────────────────────────────────────────────────
STEP 8 — CHAIN STATUS
─────────────────────────────────────────────────────────

STRUCTURAL CONSTRAINT: Do not embed CHAIN STATUS as a line, annotation, or
sub-block inside the SLA ANALYSIS section. Declare it here as the first output
element of this dedicated section.

CHAIN STATUS: [CLOSED / OPEN]

Forward (SLA → Bottleneck): are all AT-RISK rows linked to a B-ID?
  [List each AT-RISK SLA row and the B-ID it cites]

Backward (Bottleneck → SLA): does each B-ID's Evidence field name its AT-RISK rows?
  [List each B-ID and the AT-RISK rows named in its Evidence sub-field]

Gap (if OPEN): [which direction is incomplete and which ID is unresolved]

─────────────────────────────────────────────────────────
STEP 9 — CROSS-PROCESS INTERACTIONS
─────────────────────────────────────────────────────────

What does this process hand off, and to where?

| Sending Phase / State | Receiving Process | Data Payload | Expected Acknowledgment | Handoff Owner (R-ID) |
|----------------------|-----------------|-------------|------------------------|---------------------|
| Phase [N] / S-[ID] | [process name] | [fields sent] | [expected record or confirmation] | R-[N] |

─────────────────────────────────────────────────────────
STEP 10 — EDGE CASES
─────────────────────────────────────────────────────────

What scenarios exist in production that the existing process map never addresses
and that none of the SECTION A exception traces cover?
List 3+ with distinct triggers.

**EC-01 — [Brief name for this edge case]**
Trigger: [specific condition creating this scenario]
Why Problematic: [why existing exception flows don't handle it — what gap in
                  the documented process this exposes]
Correct Response: [what the process should do when this occurs]

**EC-02 — [Brief name]**
Trigger:
Why Problematic:
Correct Response:

**EC-03 — [Brief name]**
Trigger:
Why Problematic:
Correct Response:

─────────────────────────────────────────────────────────
ARTIFACT
─────────────────────────────────────────────────────────

Write the completed simulation to:
  simulations/flow/lifecycle/{topic}-lifecycle-{date}.md
```

---

## C-27 Exposure Summary

| V | Axis | Evidence field — preamble labeled axes | Evidence field — per-block labeled axes | C-26 prediction | C-27 prediction |
|---|------|---------------------------------------|----------------------------------------|-----------------|-----------------|
| V-01 | Lifecycle emphasis | YES — `Required format:` / `Fail condition:` | NO — B-01 and B-02 both use "using the format above" | PASS | **FAIL** |
| V-02 | Phrasing register | YES — labeled axes in Q5 preamble | YES — B-01 and B-02 each restate `Required format:` / `Fail condition:` as labeled sub-questions | PASS | **PASS** |
| V-03 | Role sequence | YES — labeled axes in preamble | PARTIAL — B-01 restates labeled axes; B-02 uses "using the format above" (scaffold asymmetry) | PASS | **FAIL** (B-02 gap) |
| V-04 | Lifecycle emphasis + Role sequence | YES | YES — both B-01 and B-02 carry `Required format:` / `Fail condition:` as distinct labeled fields | PASS | **PASS** |
| V-05 | Full synthesis | YES | YES — all B-NN blocks carry full labeled axes | PASS | **PASS** |

**Discriminating question for R7 scorecard**: Does V-01's preamble-only labeled axes satisfy C-27, given C-27 requires BOTH locations? Predicted NO — C-27 requires per-block presence regardless of preamble quality. V-03's asymmetric scaffold (B-01 compliant, B-02 not) tests whether a partial per-block presence satisfies C-27 or whether it must hold for all B-NN blocks. Predicted NO — C-27 requires all per-block hints to carry the labeled axes.
