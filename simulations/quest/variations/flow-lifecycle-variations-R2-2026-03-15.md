Good context. I have R1 (5 variations using v1 rubric C-01-C-10) and can see R10 shows how deep this series can go. The v2 rubric adds C-11-C-14 (role-first anchoring, anti-pattern negation, sequential gate locking, terminal verification pass). Round 2 variations should hold the R1 floor and each target one or more new aspirational criteria.

---

# flow-lifecycle — Round 2 Variations (v2 rubric: C-11, C-12, C-13, C-14)

**R1 floor held in all five variations.** Single-axis: V-01 (output format: terminal verification pass / C-14), V-02 (role-first anchoring / C-11), V-03 (anti-pattern negation / C-12). Combined: V-04 (role-first + sequential gate locking / C-11 + C-13), V-05 (all four new aspirational / C-11 + C-12 + C-13 + C-14).

**Round 2 hypothesis matrix:**

| Variation | C-11 Role-First | C-12 Anti-Pattern | C-13 Gate Locking | C-14 Terminal Pass | Primary axis |
|-----------|:---------------:|:-----------------:|:-----------------:|:-----------------:|-------------|
| V-01 | HOLD (implicit) | NONE | NONE | TARGET | Output format: dedicated verification section forces per-path terminal check |
| V-02 | TARGET | NONE | HOLD | NONE | Role anchor before first state; concrete title example gates all downstream vocabulary |
| V-03 | NONE | TARGET | NONE | NONE | Named failure modes with counter-examples block most common rubric miss |
| V-04 | TARGET | NONE | TARGET | NONE | Role anchor + sequential gate naming protected criterion |
| V-05 | TARGET | TARGET | TARGET | TARGET | Full v2 aspirational ceiling; four mechanisms, four failure modes, four structural levels |

---

## V-01 — Output Format Axis: Terminal Verification Pass

**Variation axis:** Output format — a mandatory TERMINAL VERIFICATION PASS section replaces the implicit expectation that every path reaches a terminal. The pass is structural: each traced path (happy + every exception) is listed individually and its terminal declared. Missing entries are open paths, not judgment calls.

**Hypothesis:** The most common C-03 failure is listing terminal states without confirming which paths reach them. A count-based terminal declaration ("T-01: success, T-02: failure") passes the count check while leaving exception branches dangling. A per-path verification section forces the author to name each path and its terminal, making dangling branches visible as blank rows rather than invisible omissions. C-14 passes by structure, not by review.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

---

**ROLE REGISTRY**

Identify all domain-qualified roles. A role name must be specific to the domain context of this process. "Approver" is not a role name — "Senior Credit Analyst" is.

| R-ID | Role Name (domain-qualified) | Department | Primary Responsibility in This Lifecycle |
|------|------------------------------|------------|------------------------------------------|
| R-01 | | | |
| R-02 | | | |
| ... | | | |

---

**LIFECYCLE PHASES**

Name the phases before tracing any states. Every state belongs to exactly one phase.

| Ph-ID | Phase Name | Entry Trigger | Completion Condition | SLA Envelope |
|-------|-----------|--------------|---------------------|--------------|
| PH-01 | | | | |
| PH-02 | | | | |
| ... | | | | |

---

**STATE TRACE**

For each phase, trace all states in sequence. Every state must have a named entry condition and a named exit condition. "Then X happens" is not an exit condition — name the trigger event and the target state.

| S-ID | Phase (Ph-ID) | State Name | Owner (R-ID) | Entry Condition | Exit Condition | Exits To (S-ID or T-ID) |
|------|--------------|------------|-------------|-----------------|----------------|------------------------|
| S-01 | | | | | | |
| S-02 | | | | | | |
| ... | | | | | | |

Minimum 6 states required. Every state must have a named owner.

---

**DECISION POINTS**

For each fork in the state trace:

```
Decision:   [the condition being resolved — phrased as a question]
Owner:      [R-ID from the role registry]
Condition:  [what is evaluated to reach this decision]
Branch A:   [outcome label + target S-ID or T-ID if condition is true]
Branch B:   [outcome label + target S-ID or T-ID if condition is false]
Fallback:   [what happens if the decision cannot be resolved — timeout, escalation, terminal]
```

Minimum 3 decision points required.

---

**PARALLEL PATHS**

Identify concurrent execution paths. For each:

```
Fork state:     [S-ID where concurrent execution begins]
Branch A:       [activity label + R-ID]
Branch B:       [activity label + R-ID]
Join condition: [what must be true before the branches merge]
Join owner:     [R-ID who validates the merge]
Downstream:     [S-ID or T-ID that follows the join]
```

If no parallel paths exist in this process, declare that explicitly and propose one parallelization that would reduce elapsed time, naming the states and roles affected.

---

**EXCEPTION FLOW CATALOG**

Trace at least 3 exception flows. Each must be specific to this process — not a generic system error.

For each exception:

```
E-ID:        [E-01, E-02, ...]
Name:        [exception name]
Origin:      [S-ID where the exception arises]
Trigger:     [specific condition in domain terms — what observable event causes this]
Phase:       [Ph-ID]
Divergence:  [how this path differs from the happy path at the origin state]
Recovery:    [S-ID if recoverable, T-ID if this exception terminates the process]
```

---

**BOTTLENECK AND GAP REGISTER**

| B-ID | Type | Name | Cause (domain-specific) | Downstream Impact |
|------|------|------|------------------------|-------------------|
| B-01 | bottleneck | | | |
| B-02 | bottleneck | | | |
| G-01 | gap | | [missing step name + why it is absent] | [consequence if never addressed] |

Minimum 2 bottlenecks with cause and impact. Minimum 1 gap with missing step named and consequence stated.

---

**EDGE CASE REGISTER**

At least 2 edge cases distinct from the exception flows. For each:

```
Edge case:    [name]
Scenario:     [what triggers this path — be specific]
Gap reason:   [why the normal process does not handle this case]
Consequence:  [what fails or degrades if this case is not addressed]
```

---

**SLA AND TIMING ANNOTATION**

Annotate at least 3 states from the State Trace with timing:

| S-ID | Expected Duration | At-Risk Threshold | AT-RISK? | Bottleneck Reference (B-ID) |
|------|------------------|-------------------|----------|-----------------------------|
| | | | Y / N | |
| | | | Y / N | |
| | | | Y / N | |

At least 1 state must be marked AT-RISK with a causal bottleneck reference.

---

**CROSS-LIFECYCLE HANDOFF**

If this lifecycle hands off to an adjacent lifecycle at any terminal:

| T-ID (source) | Recipient Lifecycle | Handoff Trigger | Fields Passed | Coupling State |
|---------------|---------------------|-----------------|---------------|---------------|
| | | | | |

---

**TERMINAL DECLARATION**

List every terminal state reachable from the state trace and exception flows:

| T-ID | Terminal Name | Type | Last Owner (R-ID) |
|------|--------------|------|------------------|
| T-01 | | success / failure / cancel | |
| T-02 | | | |
| ... | | | |

---

**TERMINAL VERIFICATION PASS**

For every traced path — happy path and each named exception — declare which terminal it reaches. This is a per-path check. A path with no entry in this table is an open path and a structural fail.

| Path | Type | Final State Before Terminal (S-ID) | Terminal Reached (T-ID) | Verified? |
|------|------|------------------------------------|------------------------|-----------|
| Happy path | happy | | | Y / OPEN |
| E-01: [name] | exception | | | Y / OPEN |
| E-02: [name] | exception | | | Y / OPEN |
| E-03: [name] | exception | | | Y / OPEN |
| [parallel join failure] | exception | | | Y / OPEN |

**Verification rule:** Every E-ID from the exception catalog must appear as a row in this table. Every S-ID in the State Trace with no outbound transition must appear as a "Final State Before Terminal" in this table. Any row marked OPEN is an incomplete trace — add the missing states before completing the artifact.

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Role Registry > Lifecycle Phases > State Trace > Decision Points > Parallel Paths > Exception Flow Catalog > Bottleneck and Gap Register > Edge Case Register > SLA and Timing Annotation > Cross-Lifecycle Handoff > Terminal Declaration > **Terminal Verification Pass**.

The Terminal Verification Pass is the final section and must be completed last. Every traced path must appear as a verified row before the artifact is complete.

---

## V-02 — Role-First Anchoring Axis

**Variation axis:** Role-first anchoring — domain-qualified roles are established in a dedicated ROLE ANCHOR section before any state is named. The section requires at least one concrete domain-title example (e.g., "Senior Revenue Accountant" not "Finance Analyst") that anchors the vocabulary for all downstream content. A hard gate blocks state authoring until the Role Anchor is complete.

**Hypothesis:** C-05 failures (generic role placeholders) arise when role assignment is deferred to the state trace, where the author fills "Owner" with the nearest available category noun. Pre-committing to a concrete domain-title vocabulary before any state is named makes generic substitution visible as a gate violation rather than a style choice. The concrete example in the Role Anchor also ensures C-11's domain-specificity requirement is met structurally — the model has a named exemplar to match, not an abstract standard to infer.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

---

**ROLE ANCHOR**

> **Do not name any state, phase, or decision point until this section is complete.**
>
> This section establishes the role vocabulary for the entire artifact. Every R-ID defined here must be used in at least one state. Any role named in a later section that does not appear here is an undeclared actor — add it to this table before continuing.

Identify all roles that participate in this lifecycle. Each role must satisfy two conditions:

1. **Domain-qualified title** — the title must identify the specific function and seniority within the process domain. "Approver" fails. "Senior Credit Analyst" passes. "Finance" fails. "Revenue Accounting Manager" passes.
2. **First-touch point** — the name of the state or event where this role first acts. A role with no first-touch point has no structural purpose in this lifecycle.

Provide at least one concrete domain-title example in the Notes column — an example of the actual job title a practitioner in this role would carry (e.g., "Typical title: Senior Accounts Payable Specialist").

| R-ID | Domain-Qualified Role Name | Department | First-Touch Point | Primary Decision Authority | Notes (concrete title example) |
|------|---------------------------|------------|------------------|---------------------------|-------------------------------|
| R-01 | | | | | Typical title: |
| R-02 | | | | | Typical title: |
| R-03 | | | | | Typical title: |
| ... | | | | | |

**Role Anchor gate:** Every R-ID used in the State Trace, Decision Points, Exception Flows, or any other section must appear in this table. A state owned by an R-ID not in this table is a gate violation — insert the missing role before advancing.

---

**LIFECYCLE PHASES**

Identify phases before tracing states. Every state belongs to exactly one phase.

| Ph-ID | Phase Name | Entry Trigger | Completion Condition | Primary Role (R-ID) | SLA Envelope |
|-------|-----------|--------------|---------------------|---------------------|--------------|
| PH-01 | | | | | |
| PH-02 | | | | | |
| ... | | | | | |

---

**STATE TRACE**

Trace all lifecycle states. For every state, the Owner must be an R-ID from the Role Anchor table. "Then X happens" is not a valid exit condition — name the observable trigger event.

| S-ID | Phase (Ph-ID) | State Name | Owner (R-ID) | Entry Condition | Exit Condition | Exits To |
|------|--------------|------------|-------------|-----------------|----------------|---------|
| S-01 | | | | | | |
| S-02 | | | | | | |
| ... | | | | | | |

Minimum 6 states. Orphan check: every R-ID in the Role Anchor must appear as Owner in at least one row. An R-ID with no owned state is a phantom role — either remove it from the Role Anchor or add the state it owns.

---

**DECISION POINTS**

For each decision fork in the lifecycle:

```
Decision:   [question being resolved]
Owner:      [R-ID — must exist in Role Anchor]
Condition:  [what is evaluated]
Branch A:   [outcome + target S-ID or T-ID]
Branch B:   [outcome + target S-ID or T-ID]
Fallback:   [what happens if unresolved]
```

Minimum 3 decision points. Each owner must be a specific R-ID from the Role Anchor — not a department or category name.

---

**PARALLEL PATHS**

Identify at least one concurrent execution path. For each:

```
Fork state:     [S-ID]
Branch A:       [activity + R-ID from Role Anchor]
Branch B:       [activity + R-ID from Role Anchor]
Join condition: [what must be true to merge]
Join owner:     [R-ID from Role Anchor]
Downstream:     [S-ID or T-ID]
```

If the process is purely sequential, state that explicitly and propose one parallelization, naming the R-IDs and states involved.

---

**EXCEPTION FLOW CATALOG**

Trace at least 3 exception flows. Each handler must be identified by R-ID from the Role Anchor.

```
E-ID:        [E-01, E-02, ...]
Name:        [exception name]
Origin:      [S-ID]
Trigger:     [specific domain-level condition]
Handler:     [R-ID from Role Anchor — the role who detects or acts on this exception]
Divergence:  [how this path diverges from the happy path]
Recovery:    [S-ID if recoverable, T-ID if terminal]
```

---

**BOTTLENECK AND GAP REGISTER**

| B-ID | Type | Name | Cause | Downstream Impact |
|------|------|------|-------|-------------------|
| B-01 | bottleneck | | | |
| B-02 | bottleneck | | | |
| G-01 | gap | | [missing step name + consequence] | |

---

**EDGE CASE REGISTER**

At least 2 edge cases, each distinct from the exception flows:

```
Edge case:    [name]
Scenario:     [specific trigger]
Gap reason:   [why the process does not handle this]
Consequence:  [what fails]
```

---

**SLA AND TIMING ANNOTATION**

| S-ID | State Name | Expected Duration | At-Risk Threshold | AT-RISK? | Bottleneck Ref |
|------|-----------|------------------|-------------------|----------|----------------|
| | | | | Y / N | |
| | | | | Y / N | |
| | | | | Y / N | |

At least 3 states annotated. At least 1 marked AT-RISK.

---

**CROSS-LIFECYCLE HANDOFF**

| T-ID | Recipient Lifecycle | Trigger | Fields Passed | Coupling State |
|------|--------------------|---------|--------------|--------------------|
| | | | | |

---

**TERMINAL DECLARATION**

| T-ID | Terminal Name | Type | Last Owner (R-ID) | Reached From (S-IDs / E-IDs) |
|------|--------------|------|--------------------|------------------------------|
| T-01 | | success / failure / cancel | | |
| ... | | | | |

Every path traced above must land on a T-ID in this table. Any S-ID or E-ID not accounted for in "Reached From" or continuing to another state is an open path.

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: **Role Anchor** (complete first, gate before state authoring) > Lifecycle Phases > State Trace > Decision Points > Parallel Paths > Exception Flow Catalog > Bottleneck and Gap Register > Edge Case Register > SLA and Timing Annotation > Cross-Lifecycle Handoff > Terminal Declaration.

Every R-ID used anywhere in the artifact must appear in the Role Anchor. Every domain-qualified role must include a concrete-title example in the Notes column.

---

## V-03 — Anti-Pattern Negation Axis

**Variation axis:** Anti-pattern negation — an ANTI-PATTERN BLOCK is embedded in the prompt before the main trace sections. Each anti-pattern names a specific failure mode by its structural symptom in output (what the artifact looks like when it goes wrong), followed by a concrete counter-example of the correct form. The block targets the three most common rubric misses for this skill: vague transitions, generic role names, and implicit exception flows.

**Hypothesis:** Abstract quality instructions ("be specific", "use domain language") fail because they do not tell the model what the weak form looks like — only that weakness is bad. A model that has never produced a bad transition cannot recognize its own weak transitions without a named reference. Naming the failure mode by its output symptom ("a transition that says 'then approval happens' is a fail") plus a concrete correct counter-example ("a transition names the triggering event, the owner, and the target state: 'Credit Analyst marks PO compliant → S-04: Approved for Payment'") blocks the miss without requiring inference. C-12 passes because the failure mode is explicitly named with a concrete counter-example blocking the most common rubric miss.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

---

**ANTI-PATTERN BLOCK**

The following failure modes appear in weak lifecycle simulations. Each is named by its output symptom and followed by a correct form. Do not produce the anti-pattern forms in any section of this artifact.

---

**Anti-Pattern 1 — Vague State Transition**

*Weak form:* An exit condition that says "then the document moves to the next step" or "approval happens" without naming an observable trigger event, a target state ID, or a responsible role. This form makes the transition unverifiable — a reader cannot determine when the transition fires or who owns it.

*Correct form:* "Exit condition: **Accounts Payable Supervisor confirms three-way match (PO / receipt / invoice) complete.** Exits to S-05: Approved for Payment. If match fails, exits to S-09: Exception — Discrepancy Hold."

Every transition in the State Trace must follow the correct form: observable trigger + named target state + named owner.

---

**Anti-Pattern 2 — Generic Role Name**

*Weak form:* A role name that is a category noun rather than a domain-qualified title: "Approver", "Manager", "Finance", "User", "Requester", "the team". These names do not identify who in the organization owns a decision, which means the artifact cannot be used to assign or audit responsibility.

*Correct form:* "R-03: **Senior Accounts Payable Specialist** — owns three-way match validation at S-04 and exception routing at decision D-02." Every role name must identify the specific function and level within the domain of this process.

Every R-ID in this artifact must have a domain-qualified title following the correct form.

---

**Anti-Pattern 3 — Implicit Exception Flow**

*Weak form:* An exception that is mentioned in prose ("if the invoice is rejected, it goes back for correction") without a named trigger, a divergence step, a named handler role, and a terminal or recovery state. An exception mentioned but not traced is a coverage gap, not an exception flow.

*Correct form:*
```
E-02: Invoice Rejection — Three-Way Match Failure
Origin:     S-04: Pending Match Validation
Trigger:    Invoice line-item total deviates from PO by >2% OR receipt quantity differs
Handler:    R-03: Senior Accounts Payable Specialist
Divergence: Process exits normal approval sequence; invoice flagged for vendor dispute
Recovery:   S-10: Vendor Dispute Resolution → S-04 (rematched) or T-02: Cancelled (aged >90 days)
```

Every exception cited anywhere in the artifact must be fully traced following this form.

---

**ROLE REGISTRY**

Identify all roles. Every role name must follow Anti-Pattern 2's correct form — domain-qualified, no category nouns.

| R-ID | Domain-Qualified Role Name | Department | Primary Responsibility |
|------|---------------------------|------------|------------------------|
| R-01 | | | |
| R-02 | | | |
| R-03 | | | |
| ... | | | |

---

**LIFECYCLE PHASES**

| Ph-ID | Phase Name | Entry Trigger | Completion Condition | SLA Envelope |
|-------|-----------|--------------|---------------------|--------------|
| PH-01 | | | | |
| PH-02 | | | | |
| ... | | | | |

---

**STATE TRACE**

Trace all states. Every entry and exit condition must follow Anti-Pattern 1's correct form — observable trigger, named target, named owner. Minimum 6 states.

| S-ID | Phase | State Name | Owner (R-ID) | Entry Condition | Exit Condition | Exits To |
|------|-------|-----------|-------------|-----------------|----------------|---------|
| S-01 | | | | | | |
| S-02 | | | | | | |
| ... | | | | | | |

---

**DECISION POINTS**

For each fork:

```
Decision:   [question, phrased so the answer determines the branch]
Owner:      [R-ID — domain-qualified, no category nouns]
Condition:  [observable evaluation criterion]
Branch A:   [outcome label + target S-ID or T-ID]
Branch B:   [outcome label + target S-ID or T-ID]
Fallback:   [unresolved path — timeout, escalation, or terminal]
```

Minimum 3 decision points.

---

**PARALLEL PATHS**

```
Fork state:     [S-ID]
Branch A:       [activity + R-ID]
Branch B:       [activity + R-ID]
Join condition: [merge trigger]
Join owner:     [R-ID]
Downstream:     [S-ID or T-ID]
```

If none exist, declare explicitly and propose one.

---

**EXCEPTION FLOW CATALOG**

Trace at least 3 exception flows. Every exception must follow Anti-Pattern 3's correct form — named trigger, handler role (R-ID), divergence step, recovery or terminal. An exception mentioned in prose without a full trace is incomplete.

For each exception:

```
E-ID:        [E-01, E-02, ...]
Name:        [exception name]
Origin:      [S-ID]
Trigger:     [observable condition — quantified if possible]
Handler:     [R-ID]
Divergence:  [how this diverges from the happy path at origin]
Recovery:    [recovery S-ID or terminal T-ID]
```

---

**BOTTLENECK AND GAP REGISTER**

| B-ID | Type | Name | Cause (domain-specific) | Downstream Impact |
|------|------|------|------------------------|-------------------|
| B-01 | bottleneck | | | |
| B-02 | bottleneck | | | |
| G-01 | gap | | [missing step + consequence] | |

---

**EDGE CASE REGISTER**

At least 2 edge cases, each distinct from the exception flows and from each other:

```
Edge case:    [name — not a restatement of an exception flow]
Scenario:     [specific trigger condition]
Gap reason:   [why the process has no rule for this case]
Consequence:  [what fails or degrades]
```

---

**SLA AND TIMING ANNOTATION**

| S-ID | Expected Duration | At-Risk Threshold | AT-RISK? | Bottleneck Ref |
|------|------------------|-------------------|----------|----------------|
| | | | Y / N | |
| | | | Y / N | |
| | | | Y / N | |

Minimum 3 states. At least 1 AT-RISK with bottleneck reference.

---

**CROSS-LIFECYCLE HANDOFF**

| T-ID | Recipient Lifecycle | Trigger | Fields Passed | Coupling State |
|------|--------------------|---------|--------------|----|
| | | | | |

---

**TERMINAL DECLARATION**

| T-ID | Terminal Name | Type | Last Owner | Reached From |
|------|--------------|------|-----------|-------------|
| T-01 | | success / failure / cancel | | |
| ... | | | | |

Every path traced in the State Trace and every E-ID in the Exception Flow Catalog must either continue to another state or appear in "Reached From."

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Anti-Pattern Block > Role Registry > Lifecycle Phases > State Trace > Decision Points > Parallel Paths > Exception Flow Catalog > Bottleneck and Gap Register > Edge Case Register > SLA and Timing Annotation > Cross-Lifecycle Handoff > Terminal Declaration.

The Anti-Pattern Block governs the entire artifact. Reread it before filling any section. Any role, transition, or exception that matches the weak form is a structural failure.

---

## V-04 — Combined (Role-First Anchoring + Sequential Gate Locking)

**Variation axes combined:**
1. Role-First Anchoring — concrete domain-qualified roles established before any state is named; ≥1 concrete domain-title example per role anchors all downstream vocabulary
2. Sequential Gate Locking — explicit dependency gates enforce ordering on the hardest criteria; each gate names the criterion it protects

**Hypothesis:** Role-first anchoring (C-11) prevents generic placeholders at the point of role definition. Sequential gate locking (C-13) prevents premature state authoring that bypasses the role vocabulary commitment. Together: the role anchor is the vocabulary contract, and the gate is the enforcement mechanism. The gate naming its criterion ("this gate protects C-01: State Transition Coverage — no state may be named without an anchored R-ID") makes the structural relationship self-documenting and prevents the gate from being satisfied by a partial Role Anchor.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

---

**PHASE 0 — ROLE ANCHOR**

> **Sequential Gate A — Criterion protected: C-01 (State Transition Coverage) and C-05 (Domain Role Assignment)**
>
> **Do not author any lifecycle phase, state, decision point, parallel path, exception flow, or terminal until this Role Anchor section is complete and every R-ID below has a domain-qualified title and a concrete example.**
>
> If you begin tracing states before this table is fully populated, the artifact fails C-01 because no state can satisfy "named owner" without a pre-declared role. Come back to this section if a new role is needed mid-trace — but add the row here first.

Declare every role that will appear anywhere in this artifact. Each role must meet both conditions:

1. **Domain-qualified title**: The title names the function and level within the domain of this process. Generic nouns ("Approver", "Manager", "User") do not qualify — they name categories, not roles. Examples that pass: "Revenue Accounting Manager", "Senior Credit Analyst", "Regional Sales Operations Coordinator". Examples that fail: "Finance", "Sales Team", "Approver".

2. **Concrete title example**: The Notes field must contain the actual job title a practitioner in this role would carry on their badge or org chart. This example anchors the vocabulary — every state, decision, and exception that names this role must be consistent with the concrete title.

| R-ID | Domain-Qualified Role Name | Department | First-Touch Point (name or PENDING) | Primary Decision Authority | Notes — Concrete Title Example |
|------|---------------------------|------------|------------------------------------|---------------------------|-------------------------------|
| R-01 | | | | | e.g., "Title on badge: Senior Accounts Payable Specialist" |
| R-02 | | | | | |
| R-03 | | | | | |
| ... | | | | | |

**Gate A verification:** Before advancing to Phase 1, confirm: (a) every R-ID has a non-generic domain-qualified title; (b) every R-ID has a concrete title example in the Notes column; (c) every First-Touch Point is named (not PENDING). Any PENDING or blank First-Touch Point means the role is declared without structural purpose — either name the first-touch point or remove the role.

---

**PHASE 1 — PROCESS SCHEMA**

> **Sequential Gate B — Criterion protected: C-01 (State Transition Coverage)**
>
> **Do not author any state trace until the Lifecycle Phases table is complete.** Every state in the State Trace must belong to a phase declared here. A state whose phase is not in this table is an out-of-scope state — either add the phase or remove the state.

Identify all lifecycle phases:

| Ph-ID | Phase Name | Entry Trigger | Completion Condition | Primary Role (R-ID) | SLA Envelope |
|-------|-----------|--------------|---------------------|---------------------|--------------|
| PH-01 | | | | | |
| PH-02 | | | | | |
| ... | | | | | |

---

**PHASE 2 — STATE TRACE**

Trace all lifecycle states. Every Owner must be an R-ID from the Role Anchor (Phase 0). Every entry and exit condition must name an observable trigger event — not "then X happens."

| S-ID | Phase (Ph-ID) | State Name | Owner (R-ID) | Entry Condition | Exit Condition | Exits To (S-ID or T-ID) |
|------|--------------|------------|-------------|-----------------|----------------|------------------------|
| S-01 | | | | | | |
| S-02 | | | | | | |
| ... | | | | | | |

Minimum 6 states. Orphan check: every R-ID in Phase 0 must own at least one state. An R-ID with no owned state is a phantom role — return to Phase 0 and either assign a state or remove the role.

---

**PHASE 3 — DECISION AND FORK POINTS**

For each decision fork:

```
Decision:   [question being resolved]
Owner:      [R-ID from Phase 0 — domain-qualified title required]
Condition:  [observable evaluation criterion]
Branch A:   [outcome label + target S-ID or T-ID]
Branch B:   [outcome label + target S-ID or T-ID]
Fallback:   [path if decision cannot be resolved]
```

Minimum 3 decision points.

---

**PHASE 4 — PARALLEL PATHS**

For each concurrent path:

```
Fork state:     [S-ID from Phase 2]
Branch A:       [activity + R-ID from Phase 0]
Branch B:       [activity + R-ID from Phase 0]
Join condition: [what must be true before merging]
Join owner:     [R-ID from Phase 0]
Downstream:     [S-ID or T-ID]
```

If none exist, declare that explicitly and propose one parallelization.

---

**PHASE 5 — EXCEPTION FLOW CATALOG**

Trace at least 3 exception flows. Every handler must be an R-ID from Phase 0.

```
E-ID:        [E-01, E-02, ...]
Name:        [exception name]
Origin:      [S-ID from Phase 2]
Trigger:     [specific domain-level condition]
Handler:     [R-ID from Phase 0]
Divergence:  [how this path diverges from the happy path]
Recovery:    [recovery S-ID or terminal T-ID]
```

---

**PHASE 6 — BOTTLENECK AND GAP REGISTER**

| B-ID | Type | Name | Cause | Downstream Impact |
|------|------|------|-------|-------------------|
| B-01 | bottleneck | | | |
| B-02 | bottleneck | | | |
| G-01 | gap | | [missing step + consequence] | |

At least 2 bottlenecks with cause and impact. At least 1 gap with missing step named.

---

**PHASE 7 — EDGE CASE REGISTER**

At least 2 edge cases distinct from exception flows:

```
Edge case:    [name]
Scenario:     [specific trigger]
Gap reason:   [why the process has no handling for this case]
Consequence:  [what fails]
```

---

**PHASE 8 — SLA AND TIMING ANNOTATION**

| S-ID | State Name | Expected Duration | At-Risk Threshold | AT-RISK? | Bottleneck Ref (B-ID) |
|------|-----------|------------------|-------------------|----------|-----------------------|
| | | | | Y / N | |
| | | | | Y / N | |
| | | | | Y / N | |

Minimum 3 states annotated. At least 1 AT-RISK with causal bottleneck reference.

---

**PHASE 9 — CROSS-LIFECYCLE HANDOFF**

| T-ID | Recipient Lifecycle | Trigger | Fields Passed | Coupling State |
|------|--------------------|---------|--------------|----|
| | | | | |

---

**PHASE 10 — TERMINAL DECLARATION**

> **Sequential Gate C — Criterion protected: C-03 (Terminal State Completeness)**
>
> **Do not mark the artifact complete until this table accounts for every path traced in Phases 2-5.** Scan the Exits To column of the State Trace and the Recovery field of every exception flow. Every value must appear either in this terminal table or as a continuing S-ID in the State Trace. Any value that does neither is an open path — the artifact is incomplete until it is resolved.

| T-ID | Terminal Name | Type | Last Owner (R-ID) | Reached From (S-IDs / E-IDs) |
|------|--------------|------|--------------------|------------------------------|
| T-01 | | success / failure / cancel | | |
| ... | | | | |

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure follows the phase order: Phase 0 (Role Anchor) → Phase 1 (Process Schema) → Phases 2-9 (trace and analysis sections) → Phase 10 (Terminal Declaration with Gate C verification).

Gates A, B, and C are hard sequencing constraints — not style preferences. Gate A must pass before Phase 2 begins. Gate B must pass before State Trace rows are filled. Gate C must pass before the artifact is submitted.

---

## V-05 — Combined (C-11 + C-12 + C-13 + C-14): Full v2 Aspirational Ceiling

**Variation axes combined:**
1. Role-First Anchoring (C-11) — Role Anchor with concrete title examples, hard gate before state authoring
2. Anti-Pattern Negation (C-12) — Named failure modes with concrete counter-examples blocking the three most common misses
3. Sequential Gate Locking (C-13) — Three explicit gates; each names the criterion it protects
4. Terminal Verification Pass (C-14) — Per-path structural confirmation that every traced path reaches a named terminal

**Hypothesis:** The four new aspirational criteria target four distinct failure modes at four structural points in the artifact: vocabulary failure (C-11, before first state), form failure (C-12, before trace begins), ordering failure (C-13, at each phase boundary), and completeness failure (C-14, at submission). A prompt that addresses all four creates a self-auditing structure — the model must satisfy each mechanism in sequence and cannot satisfy a later mechanism without having satisfied the earlier ones. V-05 is the ceiling variation for the v2 rubric.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

---

**SECTION 0 — ANTI-PATTERN BLOCK**

The following failure modes produce rubric misses. Each is named by its output symptom and blocked by a concrete correct form. These rules govern the entire artifact.

**Failure Mode 1 — Vague State Transition**

*What it looks like in output:* An exit condition written as "then the document moves forward", "approval happens", "the next step runs." These forms have no trigger event, no named state target, and no owner — they cannot be verified or tested.

*Correct form:* Exit condition names (a) the observable event that triggers the transition, (b) the role who owns or detects the event, and (c) the target state ID. Example: "**AR Specialist confirms payment receipt logged in ERP. → S-07: Closed - Paid.** If payment not logged within 5 business days, exit to E-03: Payment Overdue."

**Failure Mode 2 — Generic Role Name**

*What it looks like in output:* "Approver", "Finance", "the Sales team", "User", "Manager" as a role name in any ownership field. These are category nouns — they cannot be assigned, held accountable, or used to trace responsibility through a real org.

*Correct form:* Role name identifies function and level: "**Senior Revenue Accountant**", "**Regional Sales Operations Manager**", "**Credit and Collections Analyst**". The role is specific enough that two people familiar with the domain would agree on who holds it.

**Failure Mode 3 — Phantom Exception**

*What it looks like in output:* An exception mentioned in prose or as a parenthetical ("unless the invoice is rejected") without a named trigger, a divergence step, a handler role, and a terminal or recovery state. A phantom exception creates the illusion of coverage without tracing the path.

*Correct form:* Every exception is fully traced as a named E-ID entry with trigger, handler R-ID, divergence from happy path, and recovery or terminal state. An exception not given an E-ID does not exist in this artifact.

> **These three failure modes are blocked as of this section. Any state, role name, or exception that matches the weak form is a structural fail — stop and correct before advancing.**

---

**SECTION 1 — ROLE ANCHOR**

> **Gate 1 — Criterion protected: C-05 (Domain Role Assignment) and C-01 (State Transition Coverage)**
>
> **Do not advance to Section 2 until every R-ID in this table has: (a) a domain-qualified title that does not match Failure Mode 2, (b) a concrete title example in the Notes column, and (c) a named First-Touch Point.**

Declare every role that acts in this lifecycle. Apply the correct form from Anti-Pattern Block Failure Mode 2 to every role name.

| R-ID | Domain-Qualified Role Name | Dept | First-Touch Point | Decision Authority | Notes — Concrete Title Example |
|------|---------------------------|------|------------------|--------------------|-------------------------------|
| R-01 | | | | | Typical title on badge: |
| R-02 | | | | | |
| R-03 | | | | | |
| ... | | | | | |

**Gate 1 check:** Before writing Section 2, scan: (1) no role name matches Failure Mode 2; (2) every role has a concrete title example; (3) every role has a named first-touch point; (4) at least 3 roles are declared. If any condition fails, correct it before proceeding.

---

**SECTION 2 — LIFECYCLE SCHEMA**

> **Gate 2 — Criterion protected: C-01 (State Transition Coverage)**
>
> **Do not author any state trace row until this phase table is complete.** Every state in Section 3 must belong to a phase declared here. A state outside a declared phase is an out-of-scope state.

| Ph-ID | Phase Name | Entry Trigger | Completion Condition | Primary Owner (R-ID) | SLA Envelope |
|-------|-----------|--------------|---------------------|----------------------|--------------|
| PH-01 | | | | | |
| PH-02 | | | | | |
| ... | | | | | |

---

**SECTION 3 — STATE TRACE**

Trace all lifecycle states in phase order. Apply Anti-Pattern Block Failure Mode 1 to every entry and exit condition. Every Owner must be an R-ID from Section 1.

| S-ID | Phase (Ph-ID) | State Name | Owner (R-ID) | Entry Condition | Exit Condition | Exits To (S-ID or T-ID) |
|------|--------------|------------|-------------|-----------------|----------------|------------------------|
| S-01 | | | | | | |
| S-02 | | | | | | |
| ... | | | | | | |

Minimum 6 states. Orphan check: every R-ID in Section 1 must own at least one state. Phantom role check: any R-ID with no owned state must be removed from Section 1 or assigned a state here.

---

**SECTION 4 — DECISION POINTS**

For each fork in the state trace:

```
Decision:   [question — phrased so the answer determines the branch]
Owner:      [R-ID from Section 1 — not a department or category name]
Condition:  [observable evaluation criterion]
Branch A:   [outcome label + target S-ID or T-ID]
Branch B:   [outcome label + target S-ID or T-ID]
Fallback:   [path if decision cannot be resolved — name the escalation owner and terminal]
```

Minimum 3 decision points. Every owner must have a First-Touch Point in Section 1.

---

**SECTION 5 — PARALLEL PATHS**

For each concurrent execution path:

```
Fork state:     [S-ID from Section 3]
Branch A:       [activity + R-ID from Section 1]
Branch B:       [activity + R-ID from Section 1]
Join condition: [what must be true before threads merge]
Join owner:     [R-ID from Section 1]
Downstream:     [S-ID or T-ID]
```

If no parallel paths exist, declare that explicitly. Propose one parallelization: name the S-IDs it would affect, the roles involved, and the estimated elapsed-time reduction.

---

**SECTION 6 — EXCEPTION FLOW CATALOG**

Trace at least 3 exception flows. Apply Anti-Pattern Block Failure Mode 3: every exception cited anywhere in this artifact must have a full E-ID entry here. An exception mentioned in prose without an E-ID is a phantom exception — a structural fail.

```
E-ID:        [E-01, E-02, ...]
Name:        [exception name — specific, not generic]
Origin:      [S-ID from Section 3]
Trigger:     [observable domain-level condition — quantified if possible]
Handler:     [R-ID from Section 1]
Divergence:  [how this path diverges from the happy path at Origin]
Recovery:    [recovery S-ID from Section 3 if resolvable, T-ID if terminal]
```

---

**SECTION 7 — BOTTLENECK AND GAP REGISTER**

| B-ID | Type | Name | Cause (domain-specific) | Downstream Impact |
|------|------|------|------------------------|-------------------|
| B-01 | bottleneck | | | |
| B-02 | bottleneck | | | |
| G-01 | gap | | [missing step name + why absent] | [consequence if unaddressed] |

At least 2 bottlenecks (cause + impact). At least 1 gap (missing step named + consequence stated).

---

**SECTION 8 — EDGE CASE REGISTER**

At least 2 edge cases, each distinct from the exception flows in Section 6 and from each other:

```
Edge case:    [name — must not restate an E-ID exception]
Scenario:     [specific, observable trigger condition]
Gap reason:   [why the lifecycle has no rule for this case]
Consequence:  [what fails or accumulates if unaddressed]
```

---

**SECTION 9 — SLA AND TIMING ANNOTATION**

Annotate at least 3 states from Section 3 with timing. At least 1 must be marked AT-RISK with a causal bottleneck reference from Section 7.

| S-ID | State Name | Expected Duration | At-Risk Threshold | AT-RISK? | Bottleneck Ref (B-ID) |
|------|-----------|------------------|-------------------|----------|-----------------------|
| | | | | Y / N | |
| | | | | Y / N | |
| | | | | Y / N | |

---

**SECTION 10 — CROSS-LIFECYCLE HANDOFF**

| T-ID (source) | Recipient Lifecycle | Handoff Trigger | Fields Passed | Coupling State |
|---------------|---------------------|-----------------|---------------|---------------|
| | | | | |

---

**SECTION 11 — TERMINAL DECLARATION**

| T-ID | Terminal Name | Type | Last Owner (R-ID) | Reached From |
|------|--------------|------|--------------------|-------------|
| T-01 | | success / failure / cancel | | |
| T-02 | | | | |
| ... | | | | |

---

**SECTION 12 — TERMINAL VERIFICATION PASS**

> **Gate 3 — Criterion protected: C-03 (Terminal State Completeness)**
>
> **Do not submit this artifact until every row in this table is marked VERIFIED.** This section is a per-path structural confirmation — not a count. Every named path (happy path + every E-ID + every parallel join failure path) must be listed individually and its terminal declared. A path not listed here is an open path. An open path is a structural fail that must be resolved before the artifact is complete.

| Path ID | Path Type | Final State Before Terminal (S-ID) | Terminal Reached (T-ID) | Status |
|---------|-----------|------------------------------------|------------------------|--------|
| Happy path | happy | | | VERIFIED / OPEN |
| E-01: [name] | exception | | | VERIFIED / OPEN |
| E-02: [name] | exception | | | VERIFIED / OPEN |
| E-03: [name] | exception | | | VERIFIED / OPEN |
| Parallel join failure (if applicable) | exception | | | VERIFIED / OPEN |

**Verification rule:** Scan the Exits To column in Section 3 (State Trace) and the Recovery field in Section 6 (Exception Flows). Every T-ID reference must appear as "Terminal Reached" in one row of this table. Every E-ID in Section 6 must appear as a row here. Any OPEN row indicates a traced path that does not reach a declared terminal — add the missing states and re-verify.

**Gate 3 final check:** Count OPEN rows. If count > 0, the artifact is incomplete. Return to the relevant section, add the missing states or terminals, and re-verify before advancing to the output instruction.

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Section order is enforced:
- Section 0 (Anti-Pattern Block) governs all sections — read before authoring any section
- Section 1 (Role Anchor) must pass Gate 1 before Section 3 is authored
- Section 2 (Lifecycle Schema) must pass Gate 2 before Section 3 rows are filled
- Section 12 (Terminal Verification Pass) must pass Gate 3 before the artifact is submitted

The artifact is complete only when: all four gates pass, no role matches Failure Mode 2, no transition matches Failure Mode 1, no exception is a phantom, and every path in Section 12 is VERIFIED.
