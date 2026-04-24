Written to `simulations/quest/variations/trace-state-variations-R2-2026-03-14.md`.

---

## Round 2 Variations — trace-state

**Baseline:** V-04 from R1 (score: 100). All 5 R2 variations descend from that structure.

### Variation map

| V | Axis | Primary target | Key mechanism |
|---|------|----------------|---------------|
| **V-01** | C-11 minimum-found threshold | C-09, C-11 | Sweep table requires ≥2 "found" rows; fully-negative sweep is blocked |
| **V-02** | C-05 domain example bank | C-05 | 9 concrete entity name examples (3 per domain) anchor the Domain Expert gate |
| **V-03** | C-08 minimum interleave depth | C-08 | Race condition requires ≥3 labeled interleave steps (I-1, I-2, I-3+) with actor/action/field/condition per step |
| **V-04** | Full ID referencing + min-found | C-12, C-11 | State IDs, Op IDs, INV IDs all cross-referenced throughout; undeclared reference is a flagged anomaly; ≥2 found rows |
| **V-05** | Entry Condition separation + example bank | C-13, C-05 | Entry Condition made structurally active in Compiler (checked at every state transition, not just declared); two-level anomaly column distinguishes operation-precondition from state-entry-condition |

### R1 research questions addressed

| RQ | V |
|----|---|
| C-09/C-11 ceiling: minimum-found threshold? | V-01, V-04 |
| C-05 gate: concrete example bank? | V-02, V-05 |
| C-08 interleave depth: minimum 3 points? | V-03 |
| Op ID scope: extend to state/invariant IDs? | V-04 |
| C-02/C-13 separation: Entry Condition as active check? | V-05 |

### Key design choices

**V-01/V-04 minimum-found tension**: the gate instruction explicitly says "do not fabricate findings to meet the threshold" — if the domain genuinely yields fewer than 2, the trace must be enriched before closing. This is the primary R3 measurement question.

**V-03 interleave gate**: each of the ≥3 steps must name actor (OP-A/B), action (reads/writes), field or state attribute, and resulting condition. A one-sentence interleave no longer passes.

**V-05 two-level model**: Entry Condition is active during the Compiler trace (checked at every state transition) and the anomaly register has a `Level` column distinguishing `operation-precondition` from `state-entry-condition` findings. This is the most structurally novel change from R1.
-printed tables, Op IDs, Entry Condition column, sweep table). R2 research questions are about ceiling-raising within a proven structure, not about finding a better structure.

**The minimum-found threshold** (V-01, V-04) is the primary R2 experiment. V-04's sweep table was excellent at forcing explicit negatives, but a model can satisfy C-11 by filling in "none" for all four rows. A minimum-found threshold converts the sweep from a coverage gate to a depth gate.

**The domain example bank** (V-02, V-05) tests whether concrete anchors outperform abstract checklist items. The R1 C-05 gate said "no generic placeholders" -- that is a rejection criterion. The R2 example bank is an affirmative anchor: here are three real names; use these or names at this specificity level.

**Minimum interleave depth** (V-03) is the most targeted of the single-axis variations. R1's race condition analysis was structurally enforced (non-optional section, dedicated table row) but semantically shallow (one interleave line passed). Three interleave steps forces a real temporal sequence.

---

## V-01: C-11 Minimum-Found Threshold (Single-axis)

**Axis:** C-09/C-11 ceiling -- the sweep table requires at least 2 anomaly types confirmed as
"found". A fully-negative sweep table (all four "none") does not pass.

**Hypothesis:** V-04's sweep table forces explicit verdicts but allows all-negative completions.
Requiring a minimum of 2 "found" rows blocks the easy-path completion and forces the model to
actually construct anomalies, not just evaluate and dismiss them. The trade-off: more aggressive
forcing may produce invented anomalies on thin domains. The gate instruction must make clear that
"found" verdicts require genuine findings, not fabrications.

```
You are running /trace-state. Fill in this structured template.
Three roles execute in sequence. Each role gate must complete before the next begins.
All table headers are fixed -- do not reorder, rename, or remove any column.
The Domain Expert's state machine is locked after its gate. COMPILER and ANOMALY FINDER are
read-only on it -- gaps become findings, not retroactive additions.

---

## SETUP: PRIOR SIGNALS
[Search simulations/trace/ and simulations/scout/ for any prior state, request, or contract
artifacts on this topic.]
Prior signals: [List files found, or write "None -- starting fresh."]

---

## DOMAIN EXPERT: DECLARE

[Use vocabulary a Sales rep, support engineer, or finance analyst would recognize without
translation. Generic labels ("Pending", "Active", "Done") do not pass -- use the vocabulary
the domain actually uses in its systems.]

Entity: [Domain-realistic name -- the kind that appears in a CRM, helpdesk, or ERP]
Domain: [Sales / Customer Service / Finance]

State machine:
| State ID | State Name | Domain Description | Entry Condition | Terminal? |
|----------|-----------|-------------------|----------------|-----------|
| S-01 | [Name] | [What this state means to a domain practitioner] | [What must be true to enter this state] | yes / no |
| S-02 | [Name] | [What this state means to a domain practitioner] | [What must be true to enter this state] | yes / no |
[Minimum 4 rows. Terminal = no further transitions expected under normal operation.]

Valid transitions:
| Op ID | Operation Name | From State (S-ID) | To State (S-ID) | Domain Meaning |
|-------|---------------|------------------|----------------|----------------|
| OP-01 | [Name] | [S-ID] | [S-ID] | [Why a practitioner would trigger this operation] |
| OP-02 | [Name] | [S-ID] | [S-ID] | [Why a practitioner would trigger this operation] |
[All operations that appear in COMPILER: TRACE must be declared here first with an Op ID.]

Invariants:
| INV ID | Invariant Statement | Scope | Violation Consequence |
|--------|--------------------|----|----------------------|
| INV-01 | [Precisely stated invariant] | [Specific states or "all states"] | [What breaks in production if violated] |
[Minimum 1 row. Add INV-02 and beyond as the domain warrants.]

Domain Expert gate:
[ ] Entity and domain named with domain vocabulary -- no generic placeholders
[ ] All states have entry conditions and domain-language descriptions
[ ] All valid transitions declared with Op IDs before any trace steps are written
[ ] At least one invariant declared with scope and violation consequence

---

## COMPILER: TRACE

[Read-only on the Domain Expert tables. Reference states by S-ID and operations by OP-ID.
Do not add states or operations not declared above. Flag any gap as an anomaly note.]

Operation trace:
| Step | Before-State (S-ID: Name) | Operation (OP-ID: Name) | Preconditions (state-specific, one per line) | After-State (S-ID: Name) | Postconditions (one per line) | INV Check |
|------|--------------------------|------------------------|---------------------------------------------|--------------------------|------------------------------|-----------|
| 1 | [S-ID: State Name] | [OP-ID: Operation] | - [Precondition 1]<br>- [Precondition 2] | [S-ID: State Name] | - [Postcondition 1] | INV-01: pass |
| 2 | [S-ID: State Name] | [OP-ID: Operation] | - [Precondition 1] | [S-ID: State Name] | - [Postcondition 1] | INV-01: pass |
[Minimum 4 happy-path steps. Every S-ID must reference a state declared in DOMAIN EXPERT.]

Rejected transitions:
| Step | Before-State (S-ID: Name) | Attempted Op (OP-ID or "undeclared") | Failing Precondition | Rejection Behavior | After-State (S-ID: Name) |
|------|--------------------------|--------------------------------------|--------------------|--------------------|--------------------------|
| [N] | [S-ID: State Name] | [OP-ID: Name] | [Specific precondition not met] | [reject / error / exception -- state unchanged] | [Same S-ID: Name] |
[Minimum 1 row.]

Compiler gate:
[ ] Every step has non-blank Before-State (with S-ID), Operation (with OP-ID), state-specific
    Preconditions, After-State (with S-ID), Postconditions, INV Check
[ ] Every S-ID in the trace references a declared state
[ ] At least 1 rejected transition with named failing precondition
[ ] No states or operations introduced that were not declared in DOMAIN EXPERT

---

## ANOMALY FINDER: REVIEW

[Sweep the Compiler's trace for all four anomaly types. Every row requires a verdict.
MINIMUM-FOUND REQUIREMENT: At least 2 of the 4 anomaly type rows must have verdict = "found".
A fully-negative sweep ("none" in all 4 rows) does not satisfy this requirement.
If a domain genuinely has fewer than 2 anomaly types present, document the construction gap --
the trace scenario must be enriched to surface additional coverage before this skill completes.
"Found" verdicts must be genuine findings from the trace, not fabricated to satisfy the threshold.]

Anomaly sweep:
| Anomaly Type | Sweep Question | Verdict | Op + State (if found) | Production Consequence (if found) |
|-------------|---------------|---------|----------------------|----------------------------------|
| Invalid transition | Does any step cross a transition not in DOMAIN EXPERT valid-transitions? | found / none | [OP-ID at S-ID, or --] | [Consequence, or --] |
| Missing precondition check | Is any step's precondition unlikely to be enforced at the system boundary? | found / none | [OP-ID at S-ID, or --] | [Consequence, or --] |
| Invariant violation | Does any step or sequence produce an INV Check: VIOLATION, or could it under any ordering? | found / none | [INV-ID + OP-ID, or --] | [Consequence, or --] |
| Race condition | Can two operations on the same entity conflict if concurrent? | found / none | [OP-A + OP-B at S-ID, or --] | [Consequence, or --] |

Minimum-found check:
[ ] At least 2 rows above have verdict = "found"
[ ] Each "found" verdict references a real trace step, not a hypothetical addition
[If fewer than 2 rows are "found", note: "Trace scenario insufficient -- enrich before closing."]

Race condition detail (complete if verdict = found):
  Concurrent ops:  [OP-A (OP-ID)] and [OP-B (OP-ID)] on entity in state [S-ID: Name]
  Interleave:      [Sequence -- which reads and writes happen in which order, and where they conflict]
  Resolution:      [Which operation wins, or how the conflict is detected and the entity's final state]

Anomaly register:
| ID | Type | Op + State | Description | Severity |
|----|------|-----------|-------------|---------|
| A-01 | [invalid-transition / missing-precondition-check / invariant-violation / race-condition] | [OP-ID at S-ID] | [Specific description] | HIGH / MEDIUM / LOW |
[Minimum 2 rows -- one per "found" verdict in the sweep table.]

---

Write artifact: simulations/trace/state/{topic}-state-{date}.md
Frontmatter: skill, topic, date, domain, entity, state_count, operation_count, anomaly_count,
             anomaly_types (list), invariant_count, race_condition_analyzed (true/false),
             rejected_transitions (count), anomaly_types_found (count).
```

---

## V-02: C-05 Domain Example Bank (Single-axis)

**Axis:** C-05 gate strength -- the Domain Expert gate is prefaced with a concrete name bank:
3 example entity names per domain, showing the specificity level required. The model anchors
to these examples or must name entities at equivalent specificity.

**Hypothesis:** R1's C-05 gate used rejection language ("no generic placeholders"). R2's example
bank is affirmative: here are three names that pass, here is why they pass. Concrete positive
examples are a stronger anchor than abstract negative criteria for vocabulary grounding.
Specificity at declaration time propagates forward through the trace -- a well-named entity
makes generic state labels feel incongruent.

```
You are running /trace-state. Fill in this structured template.
Three roles execute in sequence. Each role gate must complete before the next begins.
All table headers are fixed -- do not reorder, rename, or remove any column.
The Domain Expert's state machine is locked after its gate. COMPILER and ANOMALY FINDER are
read-only on it -- gaps become findings, not retroactive additions.

---

## SETUP: PRIOR SIGNALS
[Search simulations/trace/ and simulations/scout/ for any prior state, request, or contract
artifacts on this topic.]
Prior signals: [List files found, or write "None -- starting fresh."]

---

## DOMAIN EXPERT: DECLARE

[Domain vocabulary standard -- use names at this level of specificity, not higher abstraction:]

Sales domain entity examples:
  - SalesOpportunity (CRM pipeline object with stage-gated progression)
  - QuoteRevision (versioned pricing document requiring approval before customer delivery)
  - AccountEngagement (account-level relationship state tracking touches and commitments)

Customer Service domain entity examples:
  - SupportTicket (issue lifecycle from open through resolution and closure)
  - EscalationCase (elevated-priority ticket with SLA clock and manager ownership)
  - WarrantyClaimRequest (customer-initiated claim requiring product verification and disposition)

Finance domain entity examples:
  - PurchaseRequisition (internal spend approval workflow with budget validation)
  - VendorInvoice (payable document lifecycle from receipt through payment confirmation)
  - ExpenseReport (submitted employee expense requiring manager and finance sign-off)

Use names at this specificity. "Order", "Request", "Item" do not pass -- they are category labels,
not domain entities. The entity name should tell a practitioner exactly what business object they
are working with.

Entity: [Domain-realistic name at the specificity level shown above]
Domain: [Sales / Customer Service / Finance]

State machine:
| State ID | State Name | Domain Description | Entry Condition | Terminal? |
|----------|-----------|-------------------|----------------|-----------|
| S-01 | [Name] | [What this state means to a domain practitioner] | [What must be true to enter this state] | yes / no |
| S-02 | [Name] | [What this state means to a domain practitioner] | [What must be true to enter this state] | yes / no |
[Minimum 4 rows. Terminal = no further transitions expected under normal operation.]
[State names: use the label a practitioner sees in a status field ("Pending Manager Approval",
 "Sent to Customer", "Awaiting Disposition") -- not architectural labels ("State_B", "Processing").]

Valid transitions:
| Op ID | Operation Name | From State (S-ID) | To State (S-ID) | Domain Meaning |
|-------|---------------|------------------|----------------|----------------|
| OP-01 | [Name] | [S-ID] | [S-ID] | [Why a practitioner would trigger this operation] |
| OP-02 | [Name] | [S-ID] | [S-ID] | [Why a practitioner would trigger this operation] |
[All operations that appear in COMPILER: TRACE must be declared here first with an Op ID.]
[Operation names: use verb forms practitioners use ("Submit for Approval", "Approve and Release",
 "Reject with Comment") -- not implementation labels ("process()", "update_status", "handle").]

Invariants:
| INV ID | Invariant Statement | Scope | Violation Consequence |
|--------|--------------------|----|----------------------|
| INV-01 | [Precisely stated invariant] | [Specific states or "all states"] | [What breaks in production if violated] |
[Minimum 1 row. Add INV-02 and beyond as the domain warrants.]

Domain Expert gate:
[ ] Entity name matches or exceeds specificity of the example bank above
[ ] All state names use domain-language labels (status field vocabulary, not architectural labels)
[ ] All operation names use practitioner verb forms, not implementation identifiers
[ ] All states have entry conditions and domain-language descriptions
[ ] All valid transitions declared with Op IDs before any trace steps are written
[ ] At least one invariant declared with scope and violation consequence

---

## COMPILER: TRACE

[Read-only on the Domain Expert tables. Reference states by S-ID and operations by OP-ID.
Do not add states or operations not declared above. Flag any gap as an anomaly note.]

Operation trace:
| Step | Before-State (S-ID: Name) | Operation (OP-ID: Name) | Preconditions (state-specific, one per line) | After-State (S-ID: Name) | Postconditions (one per line) | INV Check |
|------|--------------------------|------------------------|---------------------------------------------|--------------------------|------------------------------|-----------|
| 1 | [S-ID: State Name] | [OP-ID: Operation] | - [Precondition 1]<br>- [Precondition 2] | [S-ID: State Name] | - [Postcondition 1] | INV-01: pass |
| 2 | [S-ID: State Name] | [OP-ID: Operation] | - [Precondition 1] | [S-ID: State Name] | - [Postcondition 1] | INV-01: pass |
[Minimum 4 happy-path steps. Every S-ID must reference a state declared in DOMAIN EXPERT.]

Rejected transitions:
| Step | Before-State (S-ID: Name) | Attempted Op (OP-ID or "undeclared") | Failing Precondition | Rejection Behavior | After-State (S-ID: Name) |
|------|--------------------------|--------------------------------------|--------------------|--------------------|--------------------------|
| [N] | [S-ID: State Name] | [OP-ID: Name] | [Specific precondition not met] | [reject / error / exception -- state unchanged] | [Same S-ID: Name] |
[Minimum 1 row.]

Compiler gate:
[ ] Every step has non-blank Before-State (with S-ID), Operation (with OP-ID), state-specific
    Preconditions, After-State (with S-ID), Postconditions, INV Check
[ ] Every S-ID in the trace references a declared state
[ ] At least 1 rejected transition with named failing precondition
[ ] No states or operations introduced that were not declared in DOMAIN EXPERT

---

## ANOMALY FINDER: REVIEW

[Sweep the Compiler's trace for all four anomaly types. Every row requires a verdict.
"None found" is a valid verdict -- but the row must be present and the evaluation must have
occurred.]

Anomaly sweep:
| Anomaly Type | Sweep Question | Verdict | Op + State (if found) | Production Consequence (if found) |
|-------------|---------------|---------|----------------------|----------------------------------|
| Invalid transition | Does any step cross a transition not in DOMAIN EXPERT valid-transitions? | found / none | [OP-ID at S-ID, or --] | [Consequence, or --] |
| Missing precondition check | Is any step's precondition unlikely to be enforced at the system boundary? | found / none | [OP-ID at S-ID, or --] | [Consequence, or --] |
| Invariant violation | Does any step or sequence produce an INV Check: VIOLATION, or could it under any ordering? | found / none | [INV-ID + OP-ID, or --] | [Consequence, or --] |
| Race condition | Can two operations on the same entity conflict if concurrent? | found / none | [OP-A + OP-B at S-ID, or --] | [Consequence, or --] |

Race condition detail (complete if verdict = found):
  Concurrent ops:  [OP-A (OP-ID)] and [OP-B (OP-ID)] on entity in state [S-ID: Name]
  Interleave:      [Sequence -- which reads and writes happen in which order, and where they conflict]
  Resolution:      [Which operation wins, or how the conflict is detected and the entity's final state]

Anomaly register:
| ID | Type | Op + State | Description | Severity |
|----|------|-----------|-------------|---------|
| A-01 | [invalid-transition / missing-precondition-check / invariant-violation / race-condition] | [OP-ID at S-ID] | [Specific description] | HIGH / MEDIUM / LOW |
[Minimum 1 row. Every row from the sweep table where verdict = "found" must appear here.]

---

Write artifact: simulations/trace/state/{topic}-state-{date}.md
Frontmatter: skill, topic, date, domain, entity, state_count, operation_count, anomaly_count,
             anomaly_types (list), invariant_count, race_condition_analyzed (true/false),
             rejected_transitions (count).
```

---

## V-03: C-08 Minimum Interleave Depth (Single-axis)

**Axis:** C-08 interleave specificity -- the race condition analysis mandates a minimum of 3
interleave steps (distinct read/write events), each labeled with the operation, the field
accessed, and the resulting conflict. A one-line "Op-A reads, Op-B writes, conflict" description
does not pass.

**Hypothesis:** R1 race condition sections required concurrent op identification and an interleave
description, but the interleave could be satisfied in one sentence. Three labeled interleave steps
force the model to actually sequence the temporal conflict: what does each operation read and write,
in what order, and where the invariant breaks. This distinguishes "race condition identified" from
"race condition analyzed."

```
You are running /trace-state. Fill in this structured template.
Three roles execute in sequence. Each role gate must complete before the next begins.
All table headers are fixed -- do not reorder, rename, or remove any column.
The Domain Expert's state machine is locked after its gate. COMPILER and ANOMALY FINDER are
read-only on it -- gaps become findings, not retroactive additions.

---

## SETUP: PRIOR SIGNALS
[Search simulations/trace/ and simulations/scout/ for any prior state, request, or contract
artifacts on this topic.]
Prior signals: [List files found, or write "None -- starting fresh."]

---

## DOMAIN EXPERT: DECLARE

[Use vocabulary a Sales rep, support engineer, or finance analyst would recognize without
translation. Generic labels ("Pending", "Active", "Done") do not pass -- use the vocabulary
the domain actually uses in its systems.]

Entity: [Domain-realistic name -- the kind that appears in a CRM, helpdesk, or ERP]
Domain: [Sales / Customer Service / Finance]

State machine:
| State ID | State Name | Domain Description | Entry Condition | Terminal? |
|----------|-----------|-------------------|----------------|-----------|
| S-01 | [Name] | [What this state means to a domain practitioner] | [What must be true to enter this state] | yes / no |
| S-02 | [Name] | [What this state means to a domain practitioner] | [What must be true to enter this state] | yes / no |
[Minimum 4 rows. Terminal = no further transitions expected under normal operation.]

Valid transitions:
| Op ID | Operation Name | From State (S-ID) | To State (S-ID) | Domain Meaning |
|-------|---------------|------------------|----------------|----------------|
| OP-01 | [Name] | [S-ID] | [S-ID] | [Why a practitioner would trigger this operation] |
| OP-02 | [Name] | [S-ID] | [S-ID] | [Why a practitioner would trigger this operation] |
[All operations that appear in COMPILER: TRACE must be declared here first with an Op ID.]

Invariants:
| INV ID | Invariant Statement | Scope | Violation Consequence |
|--------|--------------------|----|----------------------|
| INV-01 | [Precisely stated invariant] | [Specific states or "all states"] | [What breaks in production if violated] |
[Minimum 1 row. Add INV-02 and beyond as the domain warrants.]

Domain Expert gate:
[ ] Entity and domain named with domain vocabulary -- no generic placeholders
[ ] All states have entry conditions and domain-language descriptions
[ ] All valid transitions declared with Op IDs before any trace steps are written
[ ] At least one invariant declared with scope and violation consequence

---

## COMPILER: TRACE

[Read-only on the Domain Expert tables. Reference states by S-ID and operations by OP-ID.
Do not add states or operations not declared above. Flag any gap as an anomaly note.]

Operation trace:
| Step | Before-State (S-ID: Name) | Operation (OP-ID: Name) | Preconditions (state-specific, one per line) | After-State (S-ID: Name) | Postconditions (one per line) | INV Check |
|------|--------------------------|------------------------|---------------------------------------------|--------------------------|------------------------------|-----------|
| 1 | [S-ID: State Name] | [OP-ID: Operation] | - [Precondition 1]<br>- [Precondition 2] | [S-ID: State Name] | - [Postcondition 1] | INV-01: pass |
| 2 | [S-ID: State Name] | [OP-ID: Operation] | - [Precondition 1] | [S-ID: State Name] | - [Postcondition 1] | INV-01: pass |
[Minimum 4 happy-path steps. Every S-ID must reference a state declared in DOMAIN EXPERT.]

Rejected transitions:
| Step | Before-State (S-ID: Name) | Attempted Op (OP-ID or "undeclared") | Failing Precondition | Rejection Behavior | After-State (S-ID: Name) |
|------|--------------------------|--------------------------------------|--------------------|--------------------|--------------------------|
| [N] | [S-ID: State Name] | [OP-ID: Name] | [Specific precondition not met] | [reject / error / exception -- state unchanged] | [Same S-ID: Name] |
[Minimum 1 row.]

Compiler gate:
[ ] Every step has non-blank Before-State (with S-ID), Operation (with OP-ID), state-specific
    Preconditions, After-State (with S-ID), Postconditions, INV Check
[ ] Every S-ID in the trace references a declared state
[ ] At least 1 rejected transition with named failing precondition
[ ] No states or operations introduced that were not declared in DOMAIN EXPERT

---

## ANOMALY FINDER: REVIEW

[Sweep the Compiler's trace for all four anomaly types. Every row requires a verdict.
"None found" is a valid verdict -- but the row must be present and the evaluation must have
occurred.]

Anomaly sweep:
| Anomaly Type | Sweep Question | Verdict | Op + State (if found) | Production Consequence (if found) |
|-------------|---------------|---------|----------------------|----------------------------------|
| Invalid transition | Does any step cross a transition not in DOMAIN EXPERT valid-transitions? | found / none | [OP-ID at S-ID, or --] | [Consequence, or --] |
| Missing precondition check | Is any step's precondition unlikely to be enforced at the system boundary? | found / none | [OP-ID at S-ID, or --] | [Consequence, or --] |
| Invariant violation | Does any step or sequence produce an INV Check: VIOLATION, or could it under any ordering? | found / none | [INV-ID + OP-ID, or --] | [Consequence, or --] |
| Race condition | Can two operations on the same entity conflict if concurrent? | found / none | [OP-A + OP-B at S-ID, or --] | [Consequence, or --] |

Race condition detail -- REQUIRED when verdict = found. MINIMUM INTERLEAVE DEPTH: 3 steps.
[Label each interleave step as I-1, I-2, I-3+. Each step names: the actor (OP-A or OP-B),
the action (reads / writes), the field or state attribute accessed, and the resulting condition.]

  Concurrent ops:  [OP-A (OP-ID)] and [OP-B (OP-ID)], both operating on entity in state [S-ID: Name]
  Starting state:  [S-ID: Name] -- [what both operations see when they begin]

  I-1: [OP-A / OP-B] [reads / writes] [field or state attribute] -- [condition after this step]
  I-2: [OP-A / OP-B] [reads / writes] [field or state attribute] -- [condition after this step]
  I-3: [OP-A / OP-B] [reads / writes] [field or state attribute] -- [conflict: describe what is now wrong]
  [Add I-4+ if the conflict requires additional steps to fully characterize]

  Conflict summary:  [What invariant or postcondition is now violated after I-3+]
  Resolution:        [Which operation wins, how the conflict is detected, and the entity's final state]

  Interleave gate:
  [ ] At least 3 interleave steps present and labeled (I-1, I-2, I-3)
  [ ] Each step names actor, action, field, and resulting condition
  [ ] Conflict is identified at a specific interleave step (not just stated in the summary)

Anomaly register:
| ID | Type | Op + State | Description | Severity |
|----|------|-----------|-------------|---------|
| A-01 | [invalid-transition / missing-precondition-check / invariant-violation / race-condition] | [OP-ID at S-ID] | [Specific description] | HIGH / MEDIUM / LOW |
[Minimum 1 row. Every row from the sweep table where verdict = "found" must appear here.]

---

Write artifact: simulations/trace/state/{topic}-state-{date}.md
Frontmatter: skill, topic, date, domain, entity, state_count, operation_count, anomaly_count,
             anomaly_types (list), invariant_count, race_condition_analyzed (true/false),
             race_condition_interleave_depth (int or 0), rejected_transitions (count).
```

---

## V-04: Full ID Referencing + Minimum-Found Threshold (Combination)

**Axes:** Full ID referencing (state IDs, invariant IDs, Op IDs, and anomaly IDs all
cross-referenced throughout -- any undeclared reference is a flagged anomaly) + minimum-found
threshold (at least 2 anomaly types confirmed as "found" in sweep table).

**Hypothesis:** V-04 from R1 introduced Op ID cross-referencing as an excellence signal.
Extending that discipline to state IDs and invariant IDs completes the audit trail: every
reference in the trace body can be traced back to a declaration row. Combined with the
minimum-found threshold, this variation is the highest-rigor option: structural completeness
(full cross-reference) + coverage depth (minimum anomaly findings). The expected cost is
additional cognitive overhead on the Anomaly Finder's sweep -- the sweep must reference
INV-IDs and S-IDs, not just OP-IDs.

```
You are running /trace-state. Fill in this structured template.
Three roles execute in sequence. Each role gate must complete before the next begins.
All table headers are fixed -- do not reorder, rename, or remove any column.
The Domain Expert's state machine is locked after its gate. COMPILER and ANOMALY FINDER are
read-only on it -- gaps become findings, not retroactive additions.

CROSS-REFERENCE DISCIPLINE: Every entity (state, operation, invariant, anomaly) is declared
once and referenced everywhere by ID. An S-ID, OP-ID, or INV-ID used in the trace body that
was not declared in the Domain Expert tables is an anomaly finding, not a silent addition.

---

## SETUP: PRIOR SIGNALS
[Search simulations/trace/ and simulations/scout/ for any prior state, request, or contract
artifacts on this topic.]
Prior signals: [List files found, or write "None -- starting fresh."]

---

## DOMAIN EXPERT: DECLARE

[Use vocabulary a Sales rep, support engineer, or finance analyst would recognize without
translation. Generic labels ("Pending", "Active", "Done") do not pass -- use the vocabulary
the domain actually uses in its systems.]

Entity: [Domain-realistic name -- the kind that appears in a CRM, helpdesk, or ERP]
Domain: [Sales / Customer Service / Finance]

State machine:
| State ID | State Name | Domain Description | Entry Condition | Terminal? |
|----------|-----------|-------------------|----------------|-----------|
| S-01 | [Name] | [What this state means to a domain practitioner] | [What must be true to enter this state] | yes / no |
| S-02 | [Name] | [What this state means to a domain practitioner] | [What must be true to enter this state] | yes / no |
[Minimum 4 rows. All state references in COMPILER and ANOMALY FINDER must use S-IDs declared here.]

Valid transitions:
| Op ID | Operation Name | From State (S-ID) | To State (S-ID) | Domain Meaning |
|-------|---------------|------------------|----------------|----------------|
| OP-01 | [Name] | [S-ID] | [S-ID] | [Why a practitioner would trigger this operation] |
| OP-02 | [Name] | [S-ID] | [S-ID] | [Why a practitioner would trigger this operation] |
[All Op IDs declared here. Any OP-ID used in COMPILER not declared here is an undeclared-op anomaly.]

Invariants:
| INV ID | Invariant Statement | Scope (S-IDs) | Violation Consequence |
|--------|--------------------|----|----------------------|
| INV-01 | [Precisely stated invariant] | [S-01, S-02, ... or "all states"] | [What breaks in production if violated] |
[Minimum 1 row. All invariant references in COMPILER and ANOMALY FINDER must use INV-IDs declared here.]

Domain Expert gate:
[ ] Entity and domain named with domain vocabulary -- no generic placeholders
[ ] All states have S-IDs, entry conditions, and domain-language descriptions
[ ] All valid transitions declared with Op IDs before any trace steps are written
[ ] All invariants declared with INV-IDs, scope listed as S-IDs, and violation consequence
[ ] No duplicate IDs (each S-ID, OP-ID, INV-ID appears exactly once)

---

## COMPILER: TRACE

[Read-only on the Domain Expert tables. All references must use declared IDs.
Undeclared reference rule: if a state, operation, or invariant is referenced that was not
declared in DOMAIN EXPERT, do not add it retroactively -- flag it as an anomaly note at the
bottom of this section with the ID you attempted to use.]

Operation trace:
| Step | Before-State (S-ID: Name) | Operation (OP-ID: Name) | Preconditions (state-specific, one per line) | After-State (S-ID: Name) | Postconditions (one per line) | INV Check |
|------|--------------------------|------------------------|---------------------------------------------|--------------------------|------------------------------|-----------|
| 1 | [S-ID: State Name] | [OP-ID: Operation] | - [Precondition 1 -- reference S-ID or OP-ID where relevant]<br>- [Precondition 2] | [S-ID: State Name] | - [Postcondition 1] | INV-01: pass |
| 2 | [S-ID: State Name] | [OP-ID: Operation] | - [Precondition 1] | [S-ID: State Name] | - [Postcondition 1] | INV-01: pass |
[Minimum 4 happy-path steps.]
[INV Check column: reference invariants by INV-ID. Format: "INV-01: pass" or "INV-01: VIOLATION -- [reason]"]

Rejected transitions:
| Step | Before-State (S-ID: Name) | Attempted Op (OP-ID or "undeclared") | Failing Precondition | Rejection Behavior | After-State (S-ID: Name) |
|------|--------------------------|--------------------------------------|--------------------|--------------------|--------------------------|
| [N] | [S-ID: State Name] | [OP-ID or "undeclared: [name]"] | [Specific precondition not met] | [reject / error / exception -- state unchanged] | [Same S-ID: Name] |
[Minimum 1 row. Undeclared operations must appear with "undeclared:" prefix -- they are anomaly candidates.]

Undeclared reference log (if any):
[List any S-ID, OP-ID, or INV-ID referenced but not declared in DOMAIN EXPERT. Each becomes an anomaly candidate.]
- [Type: S/OP/INV] [ID attempted] -- [what was needed and why it was not in the declaration]
[Write "None -- all references resolved to declared IDs." if no undeclared references occurred.]

Compiler gate:
[ ] Every step references only declared S-IDs and OP-IDs
[ ] INV Check at every step references a declared INV-ID
[ ] At least 1 rejected transition with named failing precondition
[ ] Undeclared reference log is present (even if empty)

---

## ANOMALY FINDER: REVIEW

[Sweep the Compiler's trace for all four anomaly types. Every row requires a verdict.
MINIMUM-FOUND REQUIREMENT: At least 2 of the 4 rows must have verdict = "found".
If genuinely fewer than 2 anomaly types are present, write "Trace insufficient: [reason]"
and recommend scenario enrichment. Do not fabricate findings to meet the threshold.
All findings must reference their triggering OP-ID, S-ID, and INV-ID (if applicable).]

Anomaly sweep:
| Anomaly Type | Sweep Question | Verdict | Op (OP-ID) + State (S-ID) | INV-ID (if applicable) | Production Consequence (if found) |
|-------------|---------------|---------|--------------------------|----------------------|----------------------------------|
| Invalid transition | Does any step cross a transition not in the valid-transitions table? | found / none | [OP-ID at S-ID, or --] | -- | [Consequence, or --] |
| Missing precondition check | Is any precondition unlikely to be enforced at the system boundary? | found / none | [OP-ID at S-ID, or --] | -- | [Consequence, or --] |
| Invariant violation | Does any step or sequence produce an INV Check: VIOLATION? | found / none | [OP-ID at S-ID, or --] | [INV-ID, or --] | [Consequence, or --] |
| Race condition | Can two OP-IDs conflict if concurrent on the same entity? | found / none | [OP-A + OP-B at S-ID, or --] | [INV-ID if violated, or --] | [Consequence, or --] |
| Undeclared reference | Does the Compiler's log contain any undeclared S/OP/INV reference? | found / none | [ID attempted, or --] | -- | [Scope creep / silent drift] |

Minimum-found check:
[ ] At least 2 rows above (excluding the Undeclared reference row) have verdict = "found"
[ ] Each "found" verdict cites declared IDs -- no unreferenced names in any finding

Race condition detail (complete if verdict = found):
  Concurrent ops:  [OP-A (OP-ID)] and [OP-B (OP-ID)] on entity in state [S-ID: Name]
  Interleave:      [Sequence of reads and writes -- which operation reads what, which writes what, where they conflict]
  Resolution:      [Which operation wins, or how the conflict is detected and the entity's final state]

Anomaly register:
| A-ID | Type | OP-ID | S-ID | INV-ID | Description | Severity |
|------|------|-------|------|--------|-------------|---------|
| A-01 | [type] | [OP-ID or --] | [S-ID] | [INV-ID or --] | [Specific description] | HIGH / MEDIUM / LOW |
[Minimum 2 rows. Full ID columns -- any blank ID in a "found" row is a cross-reference gap.]

---

Write artifact: simulations/trace/state/{topic}-state-{date}.md
Frontmatter: skill, topic, date, domain, entity, state_count, operation_count, anomaly_count,
             anomaly_types (list), invariant_count, race_condition_analyzed (true/false),
             rejected_transitions (count), anomaly_types_found (count),
             undeclared_references (count).
```

---

## V-05: Entry Condition Separation + Domain Example Bank (Combination)

**Axes:** C-13 strengthened (Entry Condition and Precondition are always structurally separate
fields, enabling two-level anomaly detection: state-entry violations and operation-initiation
violations) + C-05 domain example bank (concrete name anchors at declaration time, propagates
domain specificity through the trace).

**Hypothesis:** V-04 (R1) added Entry Condition as a column in the state machine table, but
the Compiler's trace only checks preconditions at operation initiation -- Entry Condition
remained a declaration artifact that the Anomaly Finder could sweep but rarely did. Making
Entry Condition structurally active in the Compiler (explicit entry-condition check when a step
moves into a new state) forces the model to apply C-13 at two distinct moments: when entering
a state AND when initiating an operation. Combined with the domain example bank, this variation
anchors vocabulary early and enforces it structurally throughout the trace.

```
You are running /trace-state. Fill in this structured template.
Three roles execute in sequence. Each role gate must complete before the next begins.
All table headers are fixed -- do not reorder, rename, or remove any column.
The Domain Expert's state machine is locked after its gate. COMPILER and ANOMALY FINDER are
read-only on it -- gaps become findings, not retroactive additions.

TWO-LEVEL PRECONDITION MODEL:
  Entry Condition: what must be true to ENTER a state (checked by the Compiler when a step
  transitions into that state, not just when an operation begins).
  Operation Precondition: what must be true to INITIATE an operation from the current state.
  These are always distinct checks. A state entry may fail even if the preceding operation's
  postconditions were met. Both levels are anomaly surfaces.

---

## SETUP: PRIOR SIGNALS
[Search simulations/trace/ and simulations/scout/ for any prior state, request, or contract
artifacts on this topic.]
Prior signals: [List files found, or write "None -- starting fresh."]

---

## DOMAIN EXPERT: DECLARE

[Domain vocabulary standard -- entity and state names at this specificity:]

Sales examples:   SalesOpportunity, QuoteRevision, AccountEngagement
CS examples:      SupportTicket, EscalationCase, WarrantyClaimRequest
Finance examples: PurchaseRequisition, VendorInvoice, ExpenseReport

Use names at this specificity. Category labels ("Order", "Item", "Request") do not pass.

Entity: [Domain-realistic name at the specificity level above]
Domain: [Sales / Customer Service / Finance]

State machine:
[Entry Condition column declares what must be true for the entity TO BE in this state at
declaration time -- not what triggers entry, but what must hold while the entity is there.
This is distinct from operation preconditions in the Compiler trace.]
| State ID | State Name | Domain Description | Entry Condition | Terminal? |
|----------|-----------|-------------------|----------------|-----------|
| S-01 | [Name] | [Practitioner-facing description] | [What must be true to be in this state -- not how you got here, but what must hold now] | yes / no |
| S-02 | [Name] | [Practitioner-facing description] | [What must be true to be in this state] | yes / no |
[Minimum 4 rows. Entry Conditions must be state-specific -- "record exists" does not pass.]

Valid transitions:
| Op ID | Operation Name | From State (S-ID) | To State (S-ID) | Domain Meaning |
|-------|---------------|------------------|----------------|----------------|
| OP-01 | [Name] | [S-ID] | [S-ID] | [Why a practitioner would trigger this] |
| OP-02 | [Name] | [S-ID] | [S-ID] | [Why a practitioner would trigger this] |
[All Op IDs declared here before any trace steps.]

Invariants:
| INV ID | Invariant Statement | Scope | Violation Consequence |
|--------|--------------------|----|----------------------|
| INV-01 | [Precisely stated invariant] | [Specific states or "all states"] | [Production risk if violated] |
[Minimum 1 row.]

Domain Expert gate:
[ ] Entity name matches or exceeds specificity of the example bank above
[ ] All state names use practitioner-facing vocabulary (status field language)
[ ] All Entry Conditions are state-specific and distinct from "record exists" or "valid data"
[ ] All valid transitions declared with Op IDs before any trace steps are written
[ ] At least one invariant declared with scope and violation consequence

---

## COMPILER: TRACE

[Read-only on the Domain Expert tables. Reference states by S-ID and operations by OP-ID.
Do not add states or operations not declared above. Flag any gap as an anomaly note.

TWO-LEVEL CHECK AT EACH STEP:
  (1) Entry Condition check: when this step transitions INTO After-State, does the entity
      satisfy the After-State's Entry Condition? Flag any violation.
  (2) Precondition check: what must be true to INITIATE this operation from Before-State?
  These are always separate rows in the step format.]

Step 1:
  Before-State:       [S-ID: State Name]
  Operation:          [OP-ID: Operation Name]
  Preconditions:      [What must be true to initiate this operation from Before-State]
                      - [Precondition 1 -- operation-level, state-specific]
                      - [Precondition 2]
  After-State:        [S-ID: State Name]
  Entry Condition:    [Does the entity satisfy After-State's declared Entry Condition?]
                      [S-ID Entry Condition: "[exact text from state machine table]"]
                      Check: pass / VIOLATION -- [describe what is not satisfied]
  Postconditions:     [What is guaranteed to be true about the entity after the operation]
                      - [Postcondition 1]
  Invariant check:    [INV-01: pass / VIOLATION -- if violation, describe what was broken]

[Repeat for each step. Minimum 4 happy-path steps.
Entry Condition check is required at every step that changes state. Same-state operations
(if any) skip the Entry Condition check but must note "state unchanged, no entry check."]

Rejected transitions:
  Before-State:    [S-ID: State Name]
  Attempted op:    [OP-ID or "undeclared: [name]"]
  Failing check:   [Is this a failing Precondition or a failing Entry Condition?]
                   Type: operation-precondition / state-entry-condition
                   Specific failure: [exact text of the condition that is not met]
  Rejection:       [Operation fails; state is unchanged. System response?]
  After-State:     [Same S-ID: State Name -- no change on rejection]

Compiler gate:
[ ] Every step has Precondition check AND Entry Condition check (where state changes)
[ ] Entry Condition checks reference the exact text from the DOMAIN EXPERT state machine table
[ ] At least 1 rejected transition with named failing check (precondition or entry condition)
[ ] No states or operations introduced that were not declared in DOMAIN EXPERT

---

## ANOMALY FINDER: REVIEW

[Sweep the Compiler's trace for all four anomaly types. Every row requires a verdict.
At each anomaly type, evaluate BOTH levels: operation-initiation failures AND state-entry
failures. An Entry Condition VIOLATION in the Compiler trace is the primary surface for
state-entry anomaly detection.]

Anomaly sweep:
| Anomaly Type | Sweep Question (both levels) | Verdict | Op + State (if found) | Production Consequence (if found) |
|-------------|------------------------------|---------|----------------------|----------------------------------|
| Invalid transition | Does any step cross a transition not in valid-transitions? OR does any Entry Condition VIOLATION indicate the entity should not be in After-State? | found / none | [OP-ID at S-ID, or --] | [Consequence, or --] |
| Missing precondition check | Is any operation Precondition unlikely to be enforced? OR is any Entry Condition unlikely to be verified at state entry? | found / none | [OP-ID at S-ID, or --] | [Consequence, or --] |
| Invariant violation | Does any step produce INV Check: VIOLATION? Does any Entry Condition VIOLATION imply an invariant is also broken? | found / none | [INV-ID + OP-ID, or --] | [Consequence, or --] |
| Race condition | Can two operations conflict if concurrent? Does a concurrent entry into the same state violate an entry condition? | found / none | [OP-A + OP-B at S-ID, or --] | [Consequence, or --] |

Entry Condition anomaly summary (if any Entry Condition VIOLATION occurred in Compiler trace):
| Step | After-State (S-ID) | Entry Condition Text | Why It Failed | Anomaly Type | A-ID |
|------|--------------------|---------------------|---------------|-------------|------|
| [N] | [S-ID: Name] | [exact text] | [specific reason condition is not met] | [type] | [A-ID] |
[Write "None -- all Entry Condition checks passed." if no violations occurred.]

Race condition detail (complete if verdict = found):
  Concurrent ops:  [OP-A (OP-ID)] and [OP-B (OP-ID)] on entity in state [S-ID: Name]
  Interleave:      [Sequence of reads and writes -- where they conflict]
  Resolution:      [Which operation wins, or how conflict is detected]

Anomaly register:
| ID | Type | Level | Op + State | Description | Severity |
|----|------|-------|-----------|-------------|---------|
| A-01 | [type] | operation-precondition / state-entry-condition | [OP-ID at S-ID] | [Specific description] | HIGH / MEDIUM / LOW |
[Level column distinguishes operation-level from state-entry-level findings. Minimum 1 row.]

---

Write artifact: simulations/trace/state/{topic}-state-{date}.md
Frontmatter: skill, topic, date, domain, entity, state_count, operation_count, anomaly_count,
             anomaly_types (list), invariant_count, race_condition_analyzed (true/false),
             rejected_transitions (count), entry_condition_violations (count).
```

---

## Scoring predictions

| Variation | Axis | C-11 | C-12 | C-13 | C-05 | C-08 | Predicted gap |
|-----------|------|------|------|------|------|------|---------------|
| V-01 | C-11 min-found threshold | PASS+ | same as V-04-R1 | same as V-04-R1 | same as V-04-R1 | same as V-04-R1 | Risk: fabricated findings to meet threshold |
| V-02 | C-05 example bank | same as V-04-R1 | same as V-04-R1 | same as V-04-R1 | PASS+ | same as V-04-R1 | Risk: over-constraining domain for novel topics |
| V-03 | C-08 interleave depth | same as V-04-R1 | same as V-04-R1 | same as V-04-R1 | same as V-04-R1 | PASS+ | Risk: inflated interleave on thin concurrency scenarios |
| V-04 | Full ID + min-found | PASS+ | PASS+ | same as V-04-R1 | same as V-04-R1 | same as V-04-R1 | Risk: ID-column overhead collapses sweep readability |
| V-05 | Entry Condition sep + example bank | same as V-04-R1 | same as V-04-R1 | PASS+ | PASS+ | same as V-04-R1 | Risk: two-level check makes Compiler section too long |

### Research questions for R3

1. **Minimum-found fabrication risk**: V-01 and V-04 require at least 2 "found" rows. Does the minimum-found instruction produce genuine findings or does the model fabricate thin anomalies to satisfy the count? Measure: are "found" verdicts in V-01/V-04 outputs independently verifiable from the trace steps they cite?

2. **Example bank specificity propagation**: Does V-02's example bank produce state labels at equivalent specificity (e.g., "Pending Manager Approval" vs "Pending"), or does the anchor affect entity naming only? Measure: compare state label specificity scores between V-02 and V-04 R1 outputs.

3. **Interleave depth vs. interleave accuracy**: V-03 requires 3 labeled interleave steps. Does the depth requirement produce more accurate race condition analysis, or does it produce verbose sequences where only one or two steps are substantive? Measure: count interleave steps that identify the actual conflict point vs. setup steps.

4. **Full ID overhead**: V-04's ID column in the anomaly sweep adds OP-ID and INV-ID columns. Does this produce cleaner cross-referencing or does it add mechanical overhead that degrades the sweep's readability? Measure: reviewer time to verify a V-04 output vs. V-04-R1 output.

5. **Entry Condition activation**: V-05 makes Entry Condition an active check in the Compiler. Does this surface new anomaly types (state-entry-level findings that were invisible before) or does it produce redundant checks that duplicate operation preconditions? Measure: count findings in the "Entry Condition anomaly summary" that are distinct from operation-precondition findings.

---

## JSON

```json
{"baseline": "V-04-R1 (score 100)", "r2_research_questions": ["C-09/C-11 ceiling: minimum-found threshold", "C-05 gate: domain example bank", "C-08 interleave depth", "Full ID referencing extension", "Entry Condition two-level activation"], "single_axis": ["V-01 C-11 min-found threshold", "V-02 C-05 example bank", "V-03 C-08 interleave depth"], "combination": ["V-04 full ID + min-found", "V-05 entry condition sep + example bank"]}
```
