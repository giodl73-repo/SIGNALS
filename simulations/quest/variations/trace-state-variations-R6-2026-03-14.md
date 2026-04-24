R6 variations written to `simulations/quest/variations/trace-state-variations-R6-2026-03-14.md`.

---

## trace-state R6 Variations — Summary

**The R6 structural bet**: every R5 variation scored 99 because it allowed "None" for any anomaly type. R6 breaks that escape hatch. Each variation implements a different forcing mechanism for C-09.

| Variation | Axis | Domain | C-09 Mechanism |
|-----------|------|--------|----------------|
| **V-01** | Output format | Finance | Per-type subsections (5A–5D); blank subsection is a structural gap; "None" requires written acquittal + trace extension instruction |
| **V-02** | Role sequence | Customer Service | Four dedicated Auditor roles, one per type; unfilled role = visible failure; each role must deliver or extend Part 3 |
| **V-03** | Phrasing register | Sales | Imperative commitment per type: "Find the [type]. There is one."; "None" requires writing two additional trace steps, then finding it |
| **V-04** | Lifecycle + Output format | Finance | Phase-per-anomaly-type (4A/4B/4C/4D); each sub-phase has exit gate requiring a finding; phase cannot close until finding or trace extension is complete |
| **V-05** | Role sequence + Inertia framing | Sales | Four formal charges; "Not Guilty" requires a named structural defense; doc-vs-trace prosecution adds second detection mode |

**New R5 patterns incorporated in all five**: C-23 (score-aloud with "stop. Go back."), C-24 (phase exit gate checkboxes for C-20/C-21/C-22), C-25 (C/FP/FN taxonomy + calibration score + <60% diagnosis threshold).

**Predicted ceiling contenders**: V-04 (phase gates make skipping structurally impossible) and V-01 (subsection format makes blank gaps mechanically visible). V-03's imperative framing is the highest-risk/highest-reward bet — it relies on the register phrasing to do work that structural format does passively.
osing |
| **V-05** | Role sequence + Inertia framing | Sales | Four-charge prosecution model — each anomaly type is a formal charge that must produce a conviction or a prejudice-dismissal (naming the missing trace condition); doc-vs-trace framing adds a second detection mode |

---

## V-01 — Axis: Output Format (Per-Type Anomaly Subsections / All-Four Mandate)

**Hypothesis**: Decomposing the anomaly sweep into four dedicated subsections — one per anomaly type
— makes each type structurally independent. A blank subsection is more detectable than a "None" row
in a shared table. Pairing this with an explicit "extend the trace" instruction converts C-09 from a
quality gate the model can avoid (write "None" in four rows) into a structural obligation: find the
type or write the trace steps that expose it. C-23, C-24, C-25 incorporated.

---

```markdown
You are running **trace-state** for a Finance domain entity.

Read these four constraints before anything else. They govern the entire session.

**Constraint 1 — Score-aloud protocol (C-23).**
The moment you identify a finding, score its Strength (1/2/3) before writing the description.
Say it: "this is a 2 — reachable in normal Finance workflows." Then write it.
If you catch yourself filling in Strength cells after completing a subsection — stop. Go back.
A retroactive score revision is not permitted. Open a new row instead.

**Constraint 2 — Numeric/temporal invariant gate (C-20).**
At least one invariant must name a specific number, amount, percentage, or duration.
"Invoice amounts must be positive" does not pass.
"Invoice total may not exceed the approved purchase order amount" passes.
Part 1 does not close until this gate is met.

**Constraint 3 — All four main anomaly types require a finding row (C-09 mandate).**
Parts 5A–5D each cover one anomaly type. Each subsection must contain at least one finding.
If the trace as written does not expose the type, write the minimal additional steps in Part 3
that would expose it, then complete the subsection. "None" is only permitted in Part 5E
(Undeclared ID reference), and only with a one-sentence structural confirmation.

**Constraint 4 — Exit gates are hard checkboxes, not suggestions.**
Each part ends with a gate checklist. Do not start the next part until every box is checked.

---

## Part 1 — Domain Setup

**[Finance Domain Expert]**

Choose one entity: Invoice, Expense Claim, Purchase Order, Journal Entry, Budget Allocation,
Vendor Payment.

- **Entity**:
- **Business purpose** (one sentence):
- **Primary audit risk** — the one failure mode that causes ledger errors or duplicate payments
  in practice:
- **Lifecycle in plain English** (ordered list, no IDs yet):
- **Actors** (AP clerk, approver, controller, system, other):

**Pre-declared invariants** — at least two, including at least one numeric or temporal constraint:

| # | Invariant | Numeric/Temporal? | Falsification test | Consequence if violated |
|---|-----------|------------------|--------------------|------------------------|
| 1 | | Y / N | | |
| 2 | | Y / N | | |

**Part 1 exit gate (C-20 + C-24):**
- [ ] Entity chosen with business purpose and primary audit risk stated
- [ ] At least one invariant row has Y in Numeric/Temporal? and a falsification test referencing
      a specific value, amount, percentage, count, or date constraint
- [ ] No invariant row says only "data is valid", "amounts must be set", or equivalent

---

## Part 2 — State Machine Declaration

**[Lifecycle Analyst]**

Assign IDs to everything. Any S-ID, OP-ID, or INV-ID used downstream without a declaration
here is a finding by definition.

### 2A — States (minimum 5)

| S-ID | Name | Entry Condition | Terminal? |
|------|------|-----------------|-----------|
| S-01 | | | |

*Entry Condition must reference specific field values, actor roles, or amounts — not generic
validity. "Amount field is non-null and > 0" passes. "Data is valid" does not.*

### 2B — Operations (minimum 7)

| OP-ID | Name | Valid-From S-IDs | Produces S-ID | Actor | Guard |
|-------|------|-----------------|---------------|-------|-------|
| OP-01 | | | | | |

*Guard = any condition beyond Valid-From state membership required to execute.*

### 2C — Invariants

Assign INV-IDs to Part 1 invariants first. Add structural invariants as needed.

| INV-ID | Statement | Scope (S-IDs) | Source | Enforcement Mechanism |
|--------|-----------|--------------|--------|-----------------------|
| INV-01 | (from Part 1 row 1) | | Expert | |
| INV-02 | (from Part 1 row 2) | | Expert | |

*Minimum 3 invariants total. At least one INV-ID must trace to a Part 1 row (Source = Expert).*
*If enforcement is silent — documentation claims the invariant holds but does not explain how —
write "Silent" and flag it as a finding candidate.*

### 2D — ID Coverage Pre-Check

List any ID referenced in 2B or 2C but not yet declared:

| Undeclared Reference | Type | Appears In | Action |
|---------------------|------|------------|--------|
| (none) or [list] | | | Declare now / Flag as 5E candidate |

**Part 2 exit gate:**
- [ ] State table: >= 5 rows with non-generic Entry Conditions
- [ ] Operation table: >= 7 rows
- [ ] Invariant table: >= 3 rows, at least one Source = Expert
- [ ] 2D coverage check completed

---

## Part 3 — Step-by-Step Trace

**[Lifecycle Analyst]**

Trace at least 7 numbered operations. Include all three required trace types.

**Step N — [OP-ID]: [Operation Name]**
- **Before**: [S-ID] — [State Name] | [key field values]
- **Preconditions** (state-specific; name the field and value; "preconditions met" does not pass):
- **Execution**:
- **After**: [S-ID] — [State Name] | [changed field values]
- **Postconditions**:
- **Invariants active**: [INV-IDs] — holds / violated
- **Guard evaluated**: [result]

Required trace types (all three must be present):
1. **Happy path**: >= 4 states traversed in sequence
2. **Negative path**: an operation attempted from an invalid state, precondition failure named
   by field and value, rejection behavior documented
3. **Concurrent scenario**: two operations that could interleave on the same entity instance;
   the conflicting state outcome named (not just "conflict exists")

*Note: If Parts 5A–5D require trace extensions to expose missing anomaly types, add those
steps here before completing Part 5.*

**Part 3 exit gate:**
- [ ] >= 7 numbered steps (or more if trace extensions were added in Part 5)
- [ ] Happy path, negative path, and concurrent scenario present
- [ ] No step references an S-ID, OP-ID, or INV-ID not declared in Part 2

---

## Part 4 — Pre-Sweep Hypothesis

**[Anomaly Hunter]**

Read only the declaration tables (Parts 2A, 2B, 2C) and Part 1 invariants.
Do not re-read the Part 3 trace steps yet.

| Anomaly Type | Predicted? | Confidence | Structural evidence from declaration tables only |
|--------------|-----------|------------|--------------------------------------------------|
| Invalid transition | Y/N | H/M/L | |
| Missing precondition check | Y/N | H/M/L | |
| Invariant violation | Y/N | H/M/L | |
| Race condition | Y/N | H/M/L | |
| Undeclared ID reference | Y/N | H/M/L | |

**Part 4 exit gate:**
- [ ] Every row has a Predicted value and a rationale derived from declaration tables

---

## Part 5 — Anomaly Hunt (Per-Type Subsections)

**Score-aloud rule in effect (C-23)**:
Score each finding's Strength (1/2/3) the moment you identify it — before writing description or
evidence. "This is a 3 — will cause duplicate payment without review." Then write it.
If you notice a score needs to change after seeing a later finding: do not revise. Open a new row.

**Strength scale**: 1 = edge case only | 2 = reachable in normal Finance workflows |
3 = will produce incorrect ledger state, duplicate payment, or audit failure

**All-four mandate**: Parts 5A–5D must each contain at least one finding row.
If no finding exists in the current trace for a type, extend Part 3 with the minimal steps
that expose it, then complete the subsection.

---

### 5A — Invalid Transition

*An operation that executed from a state not listed in its Valid-From S-IDs in 2B.*

Now read Part 3. Does any step move from a state not in the Valid-From column for its OP-ID?

| OP-ID | Actual From S-ID | Valid-From Per 2B | Gap Description | Strength |
|-------|-----------------|------------------|----------------|----------|

If no finding in current trace: name the minimal trace extension (one additional step) that
would expose an invalid transition, write it into Part 3, then complete this table.

**5A exit gate:**
- [ ] At least one finding row present (after trace extension if required)
- [ ] Strength scored at point of discovery

---

### 5B — Missing Precondition Check

*An operation that executed without evaluating a Guard that exists in the 2B Guard column.*

Now scan Part 3 for operations with a non-empty Guard in 2B where the trace step does not
explicitly evaluate the guard condition.

| OP-ID | S-ID | Guard in 2B | Trace Evidence (not checked / partially checked) | Strength |
|-------|------|-------------|------------------------------------------------|----------|

If no finding in current trace: name the minimal trace extension that would expose a missing
precondition check, write it into Part 3, then complete this table.

**5B exit gate:**
- [ ] At least one finding row present (after trace extension if required)
- [ ] Strength scored at point of discovery

---

### 5C — Invariant Violation

*After an operation executes, an INV-ID evaluates to false.*

Review each Part 3 step's "Invariants active" row. Identify steps where the state after the
operation violates any INV-ID in Part 2C, even if the trace marks it as "holds".

| INV-ID | OP-ID | S-ID | What the operation produces | Why the invariant is violated | Strength |
|--------|-------|------|-----------------------------|------------------------------|----------|

If no finding in current trace: name the minimal trace extension (a step that violates INV-01
or INV-02 via the specific value from the falsification test), write it into Part 3, then
complete this table.

**5C exit gate:**
- [ ] At least one finding row present (after trace extension if required)
- [ ] Strength scored at point of discovery

---

### 5D — Race Condition

*Two operations that could interleave on the same entity instance, producing a conflicting state.*

Identify the most concurrent-prone pair of operations from Part 2B — two operations with
overlapping Valid-From S-IDs. Describe the conflicting outcome if both execute without
serialization.

| OP-ID-1 | OP-ID-2 | Shared Entry State (S-ID) | Conflicting Outcome | Resolution or Detection Mechanism | Strength |
|---------|---------|--------------------------|--------------------|------------------------------------|----------|

If the trace does not set up a concurrent scenario: write the scenario as a Step in Part 3,
then complete this table.

**5D exit gate:**
- [ ] At least one finding row present (after trace extension if required)
- [ ] Strength scored at point of discovery

---

### 5E — Undeclared ID Reference

*An S-ID, OP-ID, or INV-ID used anywhere in Part 3 or Part 5 without a declaration in Part 2.*

| Undeclared ID | Type | Used In | Production Consequence | Strength |
|---------------|------|---------|----------------------|----------|

If none: confirm in one sentence that every ID in Parts 3 and 5 appears in Part 2.
"None" is permitted here with confirmation.

---

**Overall quality gate (C-22 + C-24):**
- [ ] Score-aloud rule was followed: no Strength cell was filled retroactively
      (If you are reading this after the sweep: did you score-aloud per type, or fill these cells
      in a final pass? If the latter — stop. Go back and re-score each finding in sequence.)
- [ ] Parts 5A, 5B, 5C, 5D each have at least one finding row
- [ ] At least one finding row across all subsections has Strength >= 2
- [ ] Part 5E has either a finding row or a written confirmation

---

## Part 6 — Anomaly Register

One row per finding from Parts 5A–5E. Strength here must match the subsection score — no revision.

| A-ID | Type | OP-ID | S-ID | INV-ID | Description | Severity | Strength | Reachability Path |
|------|------|-------|------|--------|-------------|----------|---------|------------------|
| A-01 | | | | | | | | |

*Severity*: Low / Medium / High / Critical (Finance perspective: ledger corruption = Critical).
*Reachability path*: shortest OP-ID sequence from initial state that triggers this anomaly.
*No blank cells — use "N/A: [reason]" where genuinely inapplicable.*

---

## Part 7 — Calibration Report

### 7A — Reconciliation with Three-Value Taxonomy (C-25)

Compare Part 4 predictions to Part 5 findings.

| Type | Predicted | Found | Code | Explanation |
|------|-----------|-------|------|-------------|
| Invalid transition | | | C/FP/FN | |
| Missing precondition | | | C/FP/FN | |
| Invariant violation | | | C/FP/FN | |
| Race condition | | | C/FP/FN | |
| Undeclared ID reference | | | C/FP/FN | |

**C** = Correct prediction | **FP** = Predicted found; was not found |
**FN** = Did not predict; was found

**Calibration score**: [C rows] / 5 x 100% = _____%

If below 60%: write one sentence identifying which structural property of the declaration tables
(overly optimistic Guard coverage, missing Valid-From constraints, or silent enforcement) produced
the most misleading predictions.

### 7B — Session Verdict

Two to three sentences:
- Which of the four anomaly types represents the highest Finance risk for this specific entity?
- Did the numeric/temporal invariant in Part 1 correspond to the most critical finding in Part 5?
  If not, explain the gap.

**Part 7 exit gate (C-21 + C-25 + C-24):**
- [ ] Every row in 7A has a Code and an Explanation
- [ ] Calibration score computed
- [ ] Diagnosis written if score < 60%
- [ ] Session Verdict addresses the numeric/temporal invariant explicitly
```

---

## V-02 — Axis: Role Sequence (Four Anomaly Auditor Roles / All-Four Mandate)

**Hypothesis**: Assigning one specialist Auditor role per anomaly type makes coverage mandatory
through role structure. Unlike a sweep table where a "None" row satisfies the format, an unfilled
Auditor role slot is a visible structural gap. Each Auditor's opening instruction says "Your job
is to find a [type] anomaly. If the current trace does not contain one, write the minimal step
that exposes it, then find it." C-23 (score-aloud) is framed as each Auditor's professional
discipline. C-24 as per-phase exit gates. C-25 in the final Calibration role.

---

```markdown
You are running **trace-state** for a Customer Service domain entity.

This session uses seven sequential roles. Roles 1–3 build the state machine and trace.
Roles 4–7 are Anomaly Auditors — one per type. Each Auditor must deliver at least one finding.

**Session constraint — Score-aloud discipline (C-23)**:
Every Anomaly Auditor (Roles 4–7) follows the same rule: score Strength (1/2/3) the moment
a finding is identified, before writing evidence. "This is a 2 — a support agent following
process would trigger this." Then write the finding.
If a score needs to change after seeing the next finding: do not revise. Open a new row.
"I'll fill in Strength at the end" is not permitted.

---

## ROLE 1 — CS Domain Expert

Pick a Customer Service entity: Support Ticket, Escalation Case, Customer Complaint,
Refund Request, or SLA Contract.

**Entity**:
**Business purpose** (one sentence):
**What it means when this entity gets stuck** — the failure mode customers call back about:
**Lifecycle in plain English** (ordered states, no IDs):
**Actors** (support agent, tier-2 specialist, manager, customer, system):

**Pre-declared invariants** — at least two, including at least one with a timer, count cap,
or numeric threshold:

| # | Invariant | Numeric/Temporal? | Falsification test | What breaks for the customer |
|---|-----------|------------------|--------------------|------------------------------|
| 1 | | Y / N | | |
| 2 | | Y / N | | |

**Role 1 exit gate (C-20 + C-24):**
- [ ] Entity chosen with failure mode stated
- [ ] At least one invariant has Y in Numeric/Temporal? and a falsification test referencing a
      specific SLA duration, response count, or numeric threshold
- [ ] Generic invariants ("tickets must be valid") absent

---

## ROLE 2 — State Machine Analyst

Using the CS Expert's setup and pre-declared invariants, formalize the state machine.

Every state gets an S-ID, every operation an OP-ID, every invariant an INV-ID.
An ID used without a declaration is a finding that belongs to Role 7.

### State Table (minimum 5 states)

| S-ID | Name | Entry Condition | Terminal? |
|------|------|-----------------|-----------|
| S-01 | | | |

*Entry Condition = what must be true about the ticket to be in this state.
"Ticket is assigned to an active agent" passes. "System is online" does not.*

### Operation Table (minimum 7 operations)

| OP-ID | Name | Valid-From S-IDs | Produces S-ID | Actor | Guard |
|-------|------|-----------------|---------------|-------|-------|
| OP-01 | | | | | |

### Invariant Table

Assign INV-IDs to Role 1 invariants first. Add structural invariants as needed.

| INV-ID | Rule | When it applies (S-IDs) | Source | Enforcement Mechanism |
|--------|------|------------------------|--------|-----------------------|
| INV-01 | (from Role 1 row 1) | | Expert | |
| INV-02 | (from Role 1 row 2) | | Expert | |

*Minimum 3 invariants. Source: Expert = from Role 1; Analyst = identified during formalization.*
*"Silent" enforcement = doc claims the invariant holds but explains no mechanism — flag it.*

### ID Coverage Check

| Undeclared Reference | Type | Appears In | Action |
|---------------------|------|------------|--------|

**Role 2 exit gate:**
- [ ] State table: >= 5 rows, non-generic Entry Conditions
- [ ] Operation table: >= 7 rows
- [ ] Invariant table: >= 3 rows, at least one Source = Expert
- [ ] ID coverage check completed

---

## ROLE 3 — Trace Compiler

Compile a numbered step-by-step trace of the CS entity lifecycle.
Minimum 7 steps. Required trace types: happy path, negative path, concurrent scenario.

**Step N — [OP-ID]: [Operation Name]**
- **Before**: [S-ID] — [State Name] | [key field values including SLA timers where relevant]
- **Preconditions** (name the field and value — "preconditions met" does not count):
- **What happens**:
- **After**: [S-ID] — [State Name] | [changed field values]
- **Postconditions**:
- **Invariants in play**: [INV-IDs] — holds / violated
- **Guard evaluated**: [result]

Required:
- At least one step that gets rejected: name exactly which precondition fails and what the
  system does (error message, state unchanged, notification triggered)
- At least one concurrent scenario setup: two operations that could race on the same ticket;
  name the conflicting state outcome

*If any Auditor role below requires a trace extension, add steps here.*

**Role 3 exit gate:**
- [ ] >= 7 numbered steps (including any extensions added during Auditor phases)
- [ ] Happy path, negative path, and concurrent scenario present
- [ ] No step uses an undeclared S-ID, OP-ID, or INV-ID

---

## ROLE 4 — Invalid Transition Auditor

**Your one job**: find at least one case where the trace executes an operation from a state
not listed in its Valid-From column.

If the current trace (Role 3) does not contain this: write the minimal additional step that
does, add it to Role 3, then complete the table below.

Pre-sweep prediction (from Role 2 tables only, before re-reading Role 3):
- [ ] I predict an invalid transition exists: Y / N
- Structural evidence:

Now read Role 3.

**Score Strength the moment you identify each instance — before writing evidence.**

| A-ID | OP-ID | Actual From S-ID | Valid-From Per OP Table | Gap | Strength | Severity |
|------|-------|-----------------|------------------------|-----|----------|----------|
| A-01 | | | | | | |

*Minimum 1 row required. If not found in current trace: extend Role 3, then complete table.*

---

## ROLE 5 — Missing Precondition Auditor

**Your one job**: find at least one operation that executed without evaluating a Guard
condition that exists in the Guard column of the operation table.

If the current trace does not contain this: write the minimal additional step that exposes
a guard bypass, add it to Role 3, then complete the table below.

Pre-sweep prediction:
- [ ] I predict a missing precondition check exists: Y / N
- Structural evidence:

Now read Role 3.

**Score Strength the moment you identify each instance.**

| A-ID | OP-ID | S-ID | Guard in Operation Table | Trace Evidence | Strength | Severity |
|------|-------|------|--------------------------|----------------|----------|----------|
| A-01 | | | | (not checked / partially checked / wrong field) | | |

*Minimum 1 row required. If not found in current trace: extend Role 3, then complete table.*

---

## ROLE 6 — Invariant Violation Auditor

**Your one job**: find at least one step where an INV-ID evaluates to false after execution,
even if the trace marks it as "holds".

Cross-check every step's "After" state against every INV-ID in scope for that state.
Pay special attention to the numeric/temporal invariants from Role 1 — these are the most
commonly missed.

If the current trace does not expose a violation: write a step using the Role 1 falsification
test (the exact input that violates INV-01 or INV-02), add it to Role 3, then complete the table.

Pre-sweep prediction:
- [ ] I predict an invariant violation exists: Y / N
- Structural evidence:

Now read Role 3.

**Score Strength the moment you identify each violation.**

| A-ID | INV-ID | OP-ID | S-ID | What the operation produces | Why INV fails | Strength | Severity |
|------|--------|-------|------|-----------------------------|--------------|----------|----------|
| A-01 | | | | | | | |

*Minimum 1 row required. The Role 1 falsification test is the starting point if nothing else
exposes a violation.*

---

## ROLE 7 — Race Condition and ID Discipline Auditor

**Two jobs in sequence.**

### Job A — Race Condition

Find at least one pair of operations that could interleave on the same ticket instance,
producing a conflicting state. Both operations must have an overlapping Valid-From S-ID.

If no concurrent scenario in the current trace: write the scenario as a step in Role 3,
then complete the table.

Pre-sweep prediction:
- [ ] I predict a race condition exists: Y / N
- Structural evidence (operations with overlapping Valid-From states):

**Score Strength at point of identification.**

| A-ID | OP-ID-1 | OP-ID-2 | Shared Entry S-ID | Conflicting Outcome | Resolution or Detection | Strength | Severity |
|------|---------|---------|------------------|--------------------|-----------------------------|----------|----------|
| A-01 | | | | | | | |

*Minimum 1 row required.*

### Job B — Undeclared ID Reference

Scan all Role 3 steps and A-ID rows from Roles 4–7 for S-IDs, OP-IDs, or INV-IDs not
declared in Role 2 tables.

| A-ID | Undeclared ID | Type | Used In | Production Consequence | Strength |
|------|---------------|------|---------|----------------------|----------|

*If none: confirm in one sentence that every ID in Roles 3–7 appears in Role 2.*

**Role 7 exit gate (C-22 + C-24):**
- [ ] Race condition finding present (or Role 3 extended to expose one)
- [ ] ID discipline check complete
- [ ] Score-aloud rule honored: no Strength cell was filled retroactively across Roles 4–7
      (If reviewing now: did each Auditor score before writing? If not — stop. Go back.)

---

## ROLE 8 — Calibration Analyst

### Pre-Calibration Prediction Summary

Collect the pre-sweep predictions from Roles 4–7:

| Auditor Role | Anomaly Type | Predicted? | Found? |
|-------------|-------------|-----------|--------|
| Role 4 | Invalid transition | | |
| Role 5 | Missing precondition | | |
| Role 6 | Invariant violation | | |
| Role 7A | Race condition | | |
| Role 7B | Undeclared ID reference | | |

### Reconciliation with Three-Value Taxonomy (C-25)

| Type | Predicted | Found | Code | What each Auditor role missed — or caught — about the declaration tables |
|------|-----------|-------|------|--------------------------------------------------------------------------|
| Invalid transition | | | C/FP/FN | |
| Missing precondition | | | C/FP/FN | |
| Invariant violation | | | C/FP/FN | |
| Race condition | | | C/FP/FN | |
| Undeclared ID reference | | | C/FP/FN | |

**C** = Correct | **FP** = Predicted; not found | **FN** = Not predicted; found

**Calibration score**: [C rows] / 5 x 100% = _____%

If below 60%: one sentence — which structural property of Role 2's tables produced the
most FP or FN Auditor predictions?

### Full Anomaly Register

Consolidate all A-ID rows from Roles 4–7.

| A-ID | Type | OP-ID | S-ID | INV-ID | Description | Severity | Strength |
|------|------|-------|------|--------|-------------|----------|---------|

*Strength must match each Auditor role's score — no revision.*

**Role 8 exit gate (C-21 + C-25 + C-24):**
- [ ] Every reconciliation row has a Code and an Explanation
- [ ] Calibration score computed
- [ ] Diagnosis written if score < 60%
- [ ] All A-IDs from Roles 4–7 appear in register without blank ID cells
```

---

## V-03 — Axis: Phrasing Register (Hunt-Mode Imperative / Commitment Questions)

**Hypothesis**: An imperative commitment opening per anomaly type — "Find the [type]. There is one.
Walk through every step." — creates stronger pressure to produce a finding than a table row with
a Found/None option. The bet: a model that hears "there is one" will search harder and extend
the trace before accepting "None". Paired with the score-aloud discipline from R5 V-03 (upgraded
with C-23's explicit behavioral rule), C-24 phase gates, and C-25's three-value taxonomy.
The conversational register keeps all three new aspirational criteria feeling operational rather
than bureaucratic.

---

```markdown
You're running a state machine audit on a Sales domain entity.

Before you start — three behavioral rules. Read them carefully. They're not suggestions.

---

**Rule 1: Score-aloud (C-23).**
When you find an anomaly, say the Strength number out loud before you write anything else.
"This is a 2. Reachable in a normal quote approval flow."
Then write the description and evidence.
If you reach the end of a section and realize you haven't scored yet — stop. Go back.
Don't revise a score you already wrote. If you learn something new, open a new row.

**Rule 2: At least one invariant must be real.**
A real invariant has a number in it, or a deadline. "Quotes must be valid" is not real.
"Discounts above 25% require VP approval" is real. This gate closes Section 1.

**Rule 3: The hunt sections are commitments, not optional.**
Sections 5A–5D each ask you to find a specific anomaly type. You will find one.
If it isn't in the trace yet, write the steps that expose it, then find it.
These sections do not close until you have found something.

---

### Section 1: Set the scene as a Sales expert

Pick one entity: Deal, Quote, Sales Order, Compensation Plan, or Discount Approval.

As the Sales domain expert:
- **What is this entity and why does it exist?** (one or two sentences)
- **The one failure mode that causes lost commissions or incorrect pricing in practice**
- **Lifecycle in plain English** (ordered stages a salesperson would recognize)

Now write two invariants. At least one must have a number, a threshold, or a deadline.

| # | Invariant | Has a number or deadline? | What a test would do to break it |
|---|-----------|--------------------------|----------------------------------|
| 1 | | Yes / No | |
| 2 | | Yes / No | |

If both rows say "No" in the second column: revise at least one. This gate must close
before you build any tables.

**Section 1 gate check (C-20 + C-24):**
- [ ] Entity chosen with failure mode named
- [ ] At least one invariant has Yes and a specific threshold or deadline in the test column
- [ ] No invariant reads "data must be valid" or similar

---

### Section 2: Build the machine

Every state gets an S-ID. Every operation gets an OP-ID. Every invariant gets an INV-ID.
Using an ID you haven't declared is itself a finding — you'll catch it in Section 5E.

**States** (at least 5, including at least one terminal state):

| S-ID | Name | Entry Condition | Terminal? |
|------|------|-----------------|-----------|
| S-01 | | | |

Entry condition: what must be true about the entity to be in this state — not how it got here.
"Quote total is finalized and customer has received the PDF" passes.
"System is ready" does not.

**Operations** (at least 7, covering the full lifecycle):

| OP-ID | Name | Allowed From | Leads To | Guard | Who triggers it |
|-------|------|-------------|---------|-------|----------------|
| OP-01 | | | | | |

**Invariants** — bring in the two from Section 1 (assign INV-IDs), then add structural ones:

| INV-ID | Rule | When it applies (S-IDs) | What breaks if violated |
|--------|------|------------------------|------------------------|
| INV-01 | (from Section 1 row 1) | | |
| INV-02 | (from Section 1 row 2) | | |

**Section 2 gate check:**
- [ ] At least 5 states, at least 7 operations
- [ ] Entry conditions are state-specific, not generic
- [ ] INV-01 and INV-02 trace to Section 1

---

### Section 3: Walk the lifecycle

Trace at least 7 operations as numbered steps.

**Step N — [OP-ID] [Operation name]**
Before: [S-ID], key field values
Preconditions (name the field and value — don't say "preconditions met"):
What happens:
After: [S-ID], key field values that changed
Postconditions:
Invariants in play: [INV-IDs] — holds / violated

Include:
- At least one step that gets rejected: name exactly which precondition fails
- At least one step that sets up a race: name the two operations that could collide and the
  conflicting state that results

---

### Section 4: Before the hunt — commit to your predictions

Look at the tables only. Do not re-read Section 3 yet.

For each type: do you think it's there? Say why, based on what you see in the tables.

| Type | Your prediction | Confidence | What in the tables points you there |
|------|----------------|------------|--------------------------------------|
| Invalid transition | Y / N | H/M/L | |
| Missing precondition check | Y / N | H/M/L | |
| Invariant violation | Y / N | H/M/L | |
| Race condition | Y / N | H/M/L | |
| Undeclared ID reference | Y / N | H/M/L | |

---

### Section 5A: Find the invalid transition

Walk through every step in Section 3.
For each OP-ID: does the Before state appear in its Allowed-From column?
Find the step where it doesn't.

**There is an invalid transition in this trace. Find it.**
If you've reviewed every step and can't find one: write one additional step where the operation
is attempted from an illegal state. Add it to Section 3. Then find it here.

**Score Strength the moment you find it. Before writing anything else.**

| OP-ID | Before S-ID | Allowed-From (per Section 2) | Why It's Invalid | Strength | Severity |
|-------|-------------|------------------------------|-----------------|----------|----------|
| | | | | | |

**Section 5A gate:**
- [ ] At least one finding row
- [ ] Strength scored at point of identification

---

### Section 5B: Find the missing precondition check

Walk through every step that has a Guard in the Section 2 operation table.
Find the step where the trace doesn't evaluate it — or evaluates it against the wrong field.

**There is a missing precondition check in this trace. Find it.**
If you can't: write a step where the guard is skipped, add it to Section 3, then find it.

**Score Strength the moment you identify it.**

| OP-ID | S-ID | Guard in Table | What the trace doesn't check | Strength | Severity |
|-------|------|----------------|------------------------------|----------|----------|
| | | | | | |

**Section 5B gate:**
- [ ] At least one finding row
- [ ] Strength scored at point of identification

---

### Section 5C: Find the invariant violation

After each step in Section 3, check whether the entity's new state violates any INV-ID
that applies to that state. Pay special attention to INV-01 and INV-02 — the ones with
real numbers. Use the falsification test from Section 1 as your starting point.

**There is an invariant violation in this trace. Find it.**
If you can't: write a step using the exact input from the Section 1 falsification test,
add it to Section 3, then find the violation.

**Score Strength the moment you find it.**

| INV-ID | OP-ID | S-ID | What the step produces | Why the invariant fails | Strength | Severity |
|--------|-------|------|----------------------|------------------------|----------|----------|
| | | | | | | |

**Section 5C gate:**
- [ ] At least one finding row
- [ ] Strength scored at point of identification

---

### Section 5D: Find the race condition

Look at your operation table. Find two operations that share at least one entry in their
Allowed-From column — they could both start from the same state.
Now follow them both forward. What happens to the entity if they execute concurrently?

**There is a race condition in this trace. Find it.**
If the Section 3 concurrent scenario you wrote isn't enough to fully describe the conflict:
add one more step that makes the conflicting outcome explicit.

**Score Strength the moment you name the conflict.**

| OP-ID-1 | OP-ID-2 | Entry State (S-ID) | What each produces | The conflict | Resolution / Detection | Strength |
|---------|---------|-------------------|-------------------|-------------|----------------------|----------|
| | | | | | | |

**Section 5D gate:**
- [ ] At least one finding row with both operations and the conflicting outcome named
- [ ] Strength scored at point of identification

---

### Section 5E: Find undeclared ID references

Scan every step in Section 3 and every finding in Sections 5A–5D.
Find any S-ID, OP-ID, or INV-ID that appears without a declaration in Section 2.

| Undeclared ID | Type | Where it appears | What would break without a declaration |
|---------------|------|-----------------|---------------------------------------|

If none: confirm in one sentence that every ID in Sections 3–5 appears in Section 2.
("None" is permitted here with a written confirmation.)

---

**Full hunt gate (C-22 + C-24):**
- [ ] Score-aloud rule was followed throughout Sections 5A–5D
      Right now — did you score each finding at the moment you found it, or fill cells at the end?
      If you filled cells at the end: stop. Go back. Re-run each section in sequence.
- [ ] Sections 5A, 5B, 5C, 5D each have at least one finding row
- [ ] At least one finding has Strength >= 2

---

### Section 6: Register the findings

One row per finding from Sections 5A–5E. Strength here must match what you wrote in each section.
You are not allowed to change it.

| A-ID | Type | OP-ID | S-ID | INV-ID | What breaks | Severity | Strength |
|------|------|-------|------|--------|------------|----------|---------|
| A-01 | | | | | | Low/Med/High/Critical | |

No blank cells. "N/A: [reason]" where an ID doesn't apply.

---

### Section 7: Be honest about what surprised you

Compare your Section 4 predictions to what you actually found.
Three codes: **C** = called it right | **FP** = predicted it; wasn't there |
**FN** = missed it; was there

| Type | Predicted | Found | Code | What the tables hid — or correctly tipped you off to |
|------|-----------|-------|------|-------------------------------------------------------|
| Invalid transition | | | | |
| Missing precondition | | | | |
| Invariant violation | | | | |
| Race condition | | | | |
| Undeclared ID reference | | | | |

Calibration score: [C rows] / 5 x 100% = _____%
If below 60%: one sentence — what made the tables misleading?

**Section 7 gate (C-21 + C-25 + C-24):**
- [ ] Every row has a Code and an explanation
- [ ] Calibration score computed
- [ ] Below-60% diagnosis written if needed
```

---

## V-04 — Axes: Lifecycle Emphasis + Output Format (Phase-Per-Anomaly-Type / Per-Type Exit Gates)

**Hypothesis**: Splitting Phase 4 into four named sub-phases — 4A (Invalid Transition), 4B
(Missing Precondition), 4C (Invariant Violation), 4D (Race Condition) — creates a structural
requirement that each type receives its own analysis cycle. Each sub-phase has its own entry
requirement and exit gate that cannot be satisfied by writing "None". The phase cannot close
without a finding or a written trace extension. This is a stronger structural mandate than a
sweep table row because it is not possible to omit a phase without a visible structural gap.
C-23, C-24, C-25 incorporated. Finance domain.

---

```markdown
You are running **trace-state** for a Finance domain entity.
This session uses five phases. Phases 1–3 build the state machine and trace.
Phase 4 has four sub-phases — one per anomaly type. Phase 5 is calibration.

**Non-negotiable constraints (read before starting)**:

- **Score-aloud protocol (C-23)**: in Phase 4, score each finding's Strength (1/2/3) the moment
  you identify it. "This is a 3 — will produce an audit failure." Then write the description.
  If you catch yourself scoring cells after a sub-phase is complete — stop. Go back. Do not revise
  existing scores; open a new row for new information.

- **Numeric/temporal invariant gate (C-20)**: Phase 1 does not close until at least one invariant
  names a specific amount, percentage, count, or deadline with a falsification test.

- **All four anomaly type sub-phases must close with a finding (C-09)**: Phase 4A, 4B, 4C, and 4D
  each require at least one finding row. If the trace as written does not expose the type, the
  sub-phase cannot close until Phase 3 has been extended with a step that exposes it.

Roles: Finance Domain Expert (Phase 1) | Lifecycle Analyst (Phases 2–3) | Anomaly Hunter (Phase 4)
       Calibration Analyst (Phase 5)

---

## PHASE 1 — Domain Setup
**Role**: Finance Domain Expert
**Entry**: none
**Exit gate**: entity profile complete AND numeric/temporal invariant gate satisfied

### 1A — Entity Profile

Choose one: Invoice, Expense Claim, Purchase Order, Journal Entry, Budget Allocation, Vendor Payment.

- **Entity**:
- **Business purpose** (one sentence):
- **Lifecycle in plain English** (ordered stages an AP clerk would recognize):
- **Actors** (AP clerk, approver, controller, system, auditor):
- **Primary risk** — the one pattern that causes reconciliation failures or duplicate payments:

### 1B — Pre-Declared Invariants

At least two. At least one must name a specific threshold, ratio, or date constraint.

| # | Invariant | Numeric/Temporal? | Falsification test (exact input that violates it) | Domain consequence |
|---|-----------|------------------|-------------------------------------------------|-------------------|
| 1 | | Y / N | | |
| 2 | | Y / N | | |

**Phase 1 exit gate (C-20 + C-24):**
- [ ] Entity chosen with lifecycle and risk named
- [ ] At least one invariant has Y in Numeric/Temporal? and a falsification test naming a
      specific value, amount, percentage, or date constraint
- [ ] No invariant says only "data must be set" or equivalent

Do not begin Phase 2 until all boxes are checked.

---

## PHASE 2 — State Machine Declaration
**Role**: Lifecycle Analyst
**Entry**: Phase 1 complete
**Exit gate**: all declaration tables populated; at least one INV-ID traces to Phase 1B;
              ID coverage check complete

### 2A — States (minimum 5)

| S-ID | Name | Entry Condition | Terminal? |
|------|------|-----------------|-----------|
| S-01 | | | |

*Entry Condition: specific field values, actor roles, or amounts required to be in this state.
"Amount field is non-null and > 0" passes. "Data is valid" does not.*

### 2B — Operations (minimum 7)

| OP-ID | Name | Valid-From S-IDs | Produces S-ID | Actor | Guard |
|-------|------|-----------------|---------------|-------|-------|
| OP-01 | | | | | |

### 2C — Invariants

Assign INV-IDs to Phase 1B invariants first.

| INV-ID | Invariant | Scope (S-IDs) | Source | Enforcement Mechanism |
|--------|-----------|--------------|--------|-----------------------|
| INV-01 | (from 1B row 1) | | Expert | |
| INV-02 | (from 1B row 2) | | Expert | |

*Minimum 3 invariants. At least one Source = Expert (traces to 1B).
"Silent" enforcement: doc claims the invariant holds but explains no mechanism — flag it.*

### 2D — ID Coverage Check

| Undeclared Reference | Type | Appears In | Action |
|---------------------|------|------------|--------|

**Phase 2 exit gate:**
- [ ] State table: >= 5 rows, non-generic Entry Conditions
- [ ] Operation table: >= 7 rows
- [ ] Invariant table: >= 3 rows, at least one Source = Expert
- [ ] 2D completed

Do not begin Phase 3 until all boxes are checked.

---

## PHASE 3 — Step-by-Step Trace
**Role**: Lifecycle Analyst
**Entry**: Phase 2 complete
**Exit gate**: >= 7 numbered steps; all three required trace types present; no undeclared IDs
              (Note: this phase may be extended during Phase 4 sub-phases)

Trace the Finance entity from initial state through resolution.

**Step N — [OP-ID]: [Operation Name]**
- **Before**: [S-ID] — [State Name] | [relevant field values including amounts]
- **Preconditions** (state-specific; name the field and value):
- **Execution**:
- **After**: [S-ID] — [State Name] | [changed field values]
- **Postconditions**:
- **Invariants active**: [INV-IDs] — holds / violated
- **Guard evaluated**: [result]

Required trace types:
1. Happy path: >= 4 states traversed in sequence
2. Negative path: operation attempted from invalid state; precondition failure named by
   field and value; rejection behavior documented
3. Concurrent scenario: two operations that could interleave on the same entity; conflicting
   outcome described (not just "conflict could occur")

**Phase 3 exit gate:**
- [ ] >= 7 numbered steps (baseline; may grow during Phase 4)
- [ ] Happy path, negative path, and concurrent scenario present
- [ ] No step uses an S-ID, OP-ID, or INV-ID not declared in Phase 2

Do not begin Phase 4 until all boxes are checked.

---

## PHASE 4 — Anomaly Detection
**Role**: Anomaly Hunter
**Entry**: Phase 3 complete
**Score-aloud rule applies in all sub-phases**

---

### PHASE 4A — Invalid Transition Analysis
**Entry requirement**: Phase 3 trace present
**Exit gate**: at least one finding row; Strength scored at point of identification

*An invalid transition: an operation executed from a state not in its Valid-From S-IDs.*

Pre-sub-phase prediction (from Phase 2 tables only):
- Predicted: Y / N | Confidence: H/M/L
- Structural evidence:

Now read Phase 3.

**Score Strength at point of identification — before writing evidence.**

| A-ID | OP-ID | Actual Entry S-ID | Valid-From Per 2B | Gap Description | Strength | Severity |
|------|-------|-----------------|------------------|----------------|----------|----------|
| A-01 | | | | | | |

**Phase 4A exit gate:**
- [ ] At least one finding row present
      If not found in current Phase 3: identify the minimal step (one operation from an invalid
      state), add it to Phase 3, then complete this table before checking this box
- [ ] Strength scored at moment of identification, not retroactively

---

### PHASE 4B — Missing Precondition Analysis
**Entry requirement**: Phase 4A complete
**Exit gate**: at least one finding row; Strength scored at point of identification

*A missing precondition: an operation executed without evaluating a Guard in the 2B Guard column.*

Pre-sub-phase prediction (from Phase 2 tables only):
- Predicted: Y / N | Confidence: H/M/L
- Structural evidence:

Now scan Phase 3 for operations with non-empty Guards in 2B.

**Score Strength at point of identification.**

| A-ID | OP-ID | S-ID | Guard in 2B | What the trace omits or misapplies | Strength | Severity |
|------|-------|------|------------|-----------------------------------|----------|----------|
| A-01 | | | | | | |

**Phase 4B exit gate:**
- [ ] At least one finding row present
      If not found: add a Phase 3 step where the guard condition is present but not evaluated;
      then complete this table
- [ ] Strength scored at moment of identification

---

### PHASE 4C — Invariant Violation Analysis
**Entry requirement**: Phase 4B complete
**Exit gate**: at least one finding row; Strength scored at point of identification

*An invariant violation: an INV-ID that evaluates to false after an operation executes.*

Start with INV-01 and INV-02 — use the falsification tests from Phase 1B as your search guide.

Pre-sub-phase prediction (from Phase 2 tables only):
- Predicted: Y / N | Confidence: H/M/L
- Structural evidence (which INV-ID has the highest risk of violation):

Now review each Phase 3 step against the invariants in scope.

**Score Strength the moment a violation is identified.**

| A-ID | INV-ID | OP-ID | S-ID | What the step produces | Why INV fails | Strength | Severity |
|------|--------|-------|------|-----------------------|--------------|----------|----------|
| A-01 | | | | | | | |

**Phase 4C exit gate:**
- [ ] At least one finding row present
      If not found: write a Phase 3 step using the Phase 1B falsification test (exact input
      that triggers the invariant); then complete this table
- [ ] Strength scored at moment of identification

---

### PHASE 4D — Race Condition Analysis
**Entry requirement**: Phase 4C complete
**Exit gate**: at least one finding row; Strength scored at point of identification

*A race condition: two operations that could interleave on the same entity instance,
producing a conflicting state outcome.*

Start by identifying pairs from Phase 2B with overlapping Valid-From S-IDs.

Pre-sub-phase prediction (from Phase 2 tables only):
- Predicted: Y / N | Confidence: H/M/L
- Structural evidence (candidate operation pairs with overlapping Valid-From states):

Now read the Phase 3 concurrent scenario. If it does not name the conflicting state outcome
explicitly, extend it.

**Score Strength the moment you identify the conflict.**

| A-ID | OP-ID-1 | OP-ID-2 | Shared S-ID | Conflicting Outcome | Resolution Mechanism | Strength | Severity |
|------|---------|---------|------------|--------------------|-----------------------|----------|----------|
| A-01 | | | | | | | |

**Phase 4D exit gate:**
- [ ] At least one finding row with both operations and the conflicting outcome named
      If not found: extend Phase 3 with the concurrent scenario using the candidate pair
      identified above; then complete this table
- [ ] Strength scored at moment of identification

---

### PHASE 4E — Undeclared ID Reference Analysis
**Entry requirement**: Phase 4D complete
**Exit gate**: findings listed or written confirmation of ID discipline

Scan Phase 3 and all A-IDs from Phases 4A–4D.

| A-ID | Undeclared ID | Type | Used In | Production Consequence | Strength |
|------|---------------|------|---------|----------------------|----------|

If none: confirm with one sentence.

**Phase 4 overall exit gate (C-22 + C-23 + C-24):**
- [ ] All four sub-phases (4A–4D) have at least one finding row
- [ ] Score-aloud rule honored across all sub-phases
      Right now: did you score each finding at the moment of identification per sub-phase,
      or in a single pass after completing 4A–4D? If the latter — stop. Go back.
- [ ] At least one finding across 4A–4D has Strength >= 2
- [ ] No Strength cell is blank in any finding row

Do not begin Phase 5 until all boxes are checked.

---

## PHASE 5 — Calibration
**Role**: Calibration Analyst
**Entry**: Phase 4 complete

### Full Anomaly Register

Consolidate all findings from Phases 4A–4E.

| A-ID | Type | OP-ID | S-ID | INV-ID | Description | Severity | Strength | Reachability Path |
|------|------|-------|------|--------|-------------|----------|---------|------------------|

*Strength matches Phase 4 sub-phase scores — no revision.*
*Reachability path: shortest OP-ID sequence from initial state.*

### Reconciliation with Three-Value Taxonomy (C-25)

Collect the pre-sub-phase predictions from Phases 4A–4E.

| Type | Predicted | Found | Code | What the Phase 2 tables hid — or correctly predicted |
|------|-----------|-------|------|-------------------------------------------------------|
| Invalid transition | | | C/FP/FN | |
| Missing precondition | | | C/FP/FN | |
| Invariant violation | | | C/FP/FN | |
| Race condition | | | C/FP/FN | |
| Undeclared ID reference | | | C/FP/FN | |

**C** = Correct | **FP** = Predicted; not found | **FN** = Not predicted; found

**Calibration score**: [C rows] / 5 x 100% = _____%

If below 60%: one sentence naming which structural property of Phase 2 (Valid-From coverage,
Guard completeness, or invariant specificity) generated the most misleading predictions.

**Phase 5 exit gate (C-21 + C-25 + C-24):**
- [ ] Every reconciliation row has a Code and an explanation
- [ ] Calibration score computed
- [ ] Diagnosis written if score < 60%
- [ ] Register has no blank ID cells in any finding row
```

---

## V-05 — Axes: Role Sequence + Inertia Framing (Four-Charge Prosecution Model)

**Hypothesis**: Framing the anomaly hunt as a prosecution where the state machine faces four
formal charges — one per anomaly type — creates a burden-of-proof structure that makes "None"
require active effort. A "Not Guilty" verdict must produce a structural defense (what feature
of the state machine prevents this charge from being sustained). A "Guilty" verdict produces a
conviction with specific evidence. Either way, the Analyst cannot skip the charge. This combines
the role sequence axis (specialized Prosecutor and Defense roles) with the inertia/doc-vs-trace
framing: the "existing documentation" makes implied claims about which charges it defends against,
and the trace tests each claim. C-23, C-24, C-25 incorporated. Sales domain.

---

```markdown
You are running **trace-state** for a Sales domain entity.

Framing: you are a state machine auditor. The entity you are auditing faces four formal charges.
Your job is to investigate each charge, produce evidence, and return a verdict.

For each charge: **Guilty** (anomaly confirmed, evidence produced) or
**Not Guilty** (anomaly not present, structural defense provided).

A Not Guilty verdict requires a one-sentence structural defense naming what feature of the state
machine prevents the charge. "No anomaly found" is not a defense — it is a blank.

**Behavioral constraint — Score-aloud protocol (C-23)**:
The moment you identify evidence for a Guilty verdict, score its Strength (1/2/3) before
writing the evidence summary. "This is a 2 — reachable in a normal Sales approval flow."
If you find yourself scoring after reviewing all four charges: stop. Go back. Scores must
reflect first-contact reasoning, not post-hoc review.

---

## PART 1 — What the Documentation Claims

**[Sales Domain Expert]**

Choose one entity: Deal, Quote, Sales Order, Compensation Plan, or Discount Approval.

Write what the system documentation says — how the entity lifecycle is supposed to work,
as written for a new Sales Engineer who needs to trust the system:

**Documented lifecycle** (ordered states in plain English, no IDs):

**Documented operations** (what the system allows and who triggers each):

**Documented invariants** — at least three rules the system is supposed to enforce.
At least one must constrain a specific numeric threshold or approval deadline:
1.
2.
3.

**Documented defenses** — anomaly types the documentation claims the system prevents:
(e.g., "The system prevents concurrent approvals by...", "Invalid transitions are blocked by...")

**Numeric/temporal invariant gate check (C-20)**:
Review the invariant list. If none reference a specific number, percentage, dollar amount,
or date constraint, add one before continuing:
___ [add invariant or write "gate satisfied by invariant N above"]

**Part 1 exit gate (C-20 + C-24):**
- [ ] Entity chosen with at least three documented invariants
- [ ] At least one invariant references a specific numeric or temporal value
- [ ] Documented defenses section addresses at least one anomaly type

---

## PART 2 — State Machine Formalization

**[Lifecycle Analyst]**

Formalize the documentation claims. Use full ID discipline throughout.

### 2A — States

| S-ID | Name | Entry Condition | Doc Reference | Terminal? |
|------|------|-----------------|---------------|-----------|
| S-01 | | | (quote or paraphrase the Part 1 text implying this state) | |

*Undocumented state: any state with no Doc Reference is undocumented behavior — flag it.*

### 2B — Operations

| OP-ID | Name | Valid-From S-IDs | Produces S-ID | Guard | Doc Reference |
|-------|------|-----------------|---------------|-------|---------------|
| OP-01 | | | | | |

*Undocumented operation: any operation with no Doc Reference is undocumented — note it.*

### 2C — Invariants

| INV-ID | Invariant | Scope (S-IDs) | Doc Reference | Numeric/Temporal? | Enforcement Mechanism (per Doc) |
|--------|-----------|--------------|---------------|------------------|--------------------------------|
| INV-01 | | | | Y/N | (what doc says prevents violation, or "Silent") |

*At least one INV-ID must map to the numeric/temporal invariant from Part 1.*
*"Silent" enforcement = doc claims invariant holds but does not explain the mechanism —
that silence is itself a finding candidate in Charge 2.*

### 2D — Charge Brief Pre-Audit

Before compiling the trace, examine the documentation claims against the formal tables.
Note any gaps already visible:

| Gap Type | Description | Doc Reference | Charge Relevance |
|----------|-------------|--------------|-----------------|
| Undocumented state | | | Charge 1 (invalid transition risk) |
| Undocumented operation | | | Charge 1 |
| Silent enforcement | | | Charge 2 / Charge 3 |
| Missing Guard | | | Charge 2 |
| Concurrent operation pair | (two OP-IDs with overlapping Valid-From) | | Charge 4 |

---

## PART 3 — Pre-Charge Hypothesis

**[Anomaly Hunter]**

Reading only Parts 1 and 2 — not the trace you are about to compile.
For each charge: what does the documentation imply? Will it sustain or fail?

| Charge | Documentation Implies | Your Prediction | Confidence | Defense the doc claims |
|--------|----------------------|----------------|-----------|----------------------|
| 1 — Invalid transition | | Guilty/Not Guilty | H/M/L | |
| 2 — Missing precondition | | Guilty/Not Guilty | H/M/L | |
| 3 — Invariant violation | | Guilty/Not Guilty | H/M/L | |
| 4 — Race condition | | Guilty/Not Guilty | H/M/L | |
| 5 — Undeclared ID reference | | Guilty/Not Guilty | H/M/L | |

---

## PART 4 — The Trace

**[Lifecycle Analyst]**

Compile the actual trace. For each step: show what the documentation claims and what the
trace shows. Assign Strength immediately when you identify a discrepancy.

**Step N — [OP-ID]: [Operation Name]**

| | Documentation Claims | Trace Shows |
|-|---------------------|-------------|
| **Before state** | [valid prior state per doc] | [S-ID and field values] |
| **Preconditions** | [what doc says must hold] | [what trace actually checks — or fails to check] |
| **After state** | [result per doc] | [S-ID and field values] |
| **Invariants** | [INV-IDs doc claims are enforced] | [which hold, which don't] |
| **Gap** | — | [discrepancy between columns, or "none"] |

Minimum 7 steps. Required:
1. Happy path: documentation and trace agree; Gap = "none"
2. Negative path: documentation claims rejection occurs — confirm whether trace does too
3. Concurrent scenario: two operations on the same entity; documentation's implied defense named;
   conflicting outcome described whether defense holds or not

*Note: if any Charge below requires a trace extension, add those steps here.*

---

## PART 5 — The Four Charges

**Score-aloud rule in effect**:
When you identify evidence for a Guilty verdict — score Strength before writing evidence.
"This is a 3 — wrong commission calculation." Then write it.

**Strength scale**: 1 = edge case only | 2 = reachable in normal Sales workflows |
3 = incorrect commissions, lost deal records, or customer-facing pricing error

---

### CHARGE 1 — Invalid Transition

*The charge: the trace executes an operation from a state not listed in its Valid-From column.*

Does the documentation's defense (from Part 3) hold up?
Examine every step in Part 4 against the 2B Valid-From columns.

**Verdict**: Guilty / Not Guilty

If **Guilty** — score Strength at point of identification, then complete the evidence table:

| OP-ID | Actual From S-ID | Valid-From Per 2B | Doc's Claimed Defense | Why Defense Failed | Strength | Severity |
|-------|-----------------|------------------|----------------------|-------------------|----------|----------|
| | | | | | | |

If **Not Guilty** — write the structural defense:
*What specific feature of the 2B Valid-From columns makes this charge impossible to sustain
against this entity?* (One sentence; name a specific state or operation constraint.)

*Charge 1 cannot remain uncharged: if no evidence in current trace and "Not Guilty" defense
is insufficient, extend Part 4 with a step that tests the charge, then re-evaluate.*

---

### CHARGE 2 — Missing Precondition Check

*The charge: the trace executes an operation without evaluating a Guard in the 2B Guard column.*

Does the documentation's claimed enforcement hold in the trace?
Examine every step with a non-empty Guard in 2B.

**Verdict**: Guilty / Not Guilty

If **Guilty** — score Strength at point of identification:

| OP-ID | S-ID | Guard in 2B | What the trace omits | Doc's Claimed Defense | Why Defense Failed | Strength | Severity |
|-------|------|------------|---------------------|----------------------|-------------------|----------|----------|
| | | | | | | | |

If **Not Guilty** — write the structural defense:
*What specific enforcement mechanism in the formalized model makes every Guard impossible
to bypass?* (Name the specific INV-ID or structural constraint.)

---

### CHARGE 3 — Invariant Violation

*The charge: after an operation executes, an INV-ID evaluates to false.*

Start with INV-01 and INV-02 — use the Part 1 falsification tests.
The numeric/temporal invariants are the prosecution's primary evidence.

**Verdict**: Guilty / Not Guilty

If **Guilty** — score Strength at point of identification:

| INV-ID | OP-ID | S-ID | What the step produces | Why INV fails | Doc's Claimed Defense | Why Defense Failed | Strength | Severity |
|--------|-------|------|-----------------------|--------------|----------------------|-------------------|----------|----------|
| | | | | | | | | |

If **Not Guilty** — write the structural defense:
*Which specific enforcement mechanism in the system prevents every INV-ID violation?
Name the specific guard, state constraint, or validation step.* Not "the system validates inputs."

---

### CHARGE 4 — Race Condition

*The charge: two operations interleave on the same entity instance, producing a conflicting state.*

Start from the 2D concurrent operation pair candidates. The prosecution's opening is: two
operations share a Valid-From state, creating the opportunity for interleaving.

**Verdict**: Guilty / Not Guilty

If **Guilty** — score Strength at point of identification:

| OP-ID-1 | OP-ID-2 | Shared S-ID | Conflicting Outcome | Documentation's Defense | Why Defense Failed | Strength | Severity |
|---------|---------|------------|--------------------|--------------------------|--------------------|----------|----------|
| | | | | | | | |

If **Not Guilty** — write the structural defense:
*What serialization or locking mechanism in the documented model prevents concurrent access?
Name the specific constraint.* "Concurrent operations are unlikely" is not a defense.

---

### CHARGE 5 — Undeclared ID Reference

*The charge: an ID used in Parts 3–5 was never declared in Part 2.*

Scan all steps and all charge evidence tables.

**Verdict**: Guilty / Not Guilty

If **Guilty**:

| Undeclared ID | Type | Used In | Production Consequence | Strength |
|---------------|------|---------|----------------------|----------|

If **Not Guilty**: confirm in one sentence that every ID in Parts 3–5 appears in Part 2.

---

**Charges gate (C-22 + C-23 + C-24):**
- [ ] Charges 1, 2, 3, and 4 have either a Guilty verdict with evidence or a written
      structural defense (Not Guilty without a written structural defense is not permitted)
- [ ] Score-aloud rule honored: Strength was assigned at point of identification for each
      Guilty verdict, not filled retroactively after reviewing all five charges
      (If filling scores now: stop. Go back. Re-evaluate each charge in sequence.)
- [ ] At least one Guilty verdict across Charges 1–4 has Strength >= 2

---

## PART 6 — Anomaly Register

| A-ID | Type | OP-ID | S-ID | INV-ID | Charge | Description | Severity | Strength |
|------|------|-------|------|--------|--------|-------------|----------|---------|

*Strength matches Charge evidence scores — no revision.*
*Severity from the Sales team's perspective: wrong commission = Critical.*
*Include "Not Guilty" charges as register rows with Description = defense statement.*

---

## PART 7 — Calibration Report

### 7A — Verdict vs Prediction Reconciliation (C-25)

| Charge | Predicted | Actual Verdict | Code | What the documentation hid — or correctly defended |
|--------|-----------|---------------|------|-----------------------------------------------------|
| 1 — Invalid transition | | Guilty/Not Guilty | C/FP/FN | |
| 2 — Missing precondition | | Guilty/Not Guilty | C/FP/FN | |
| 3 — Invariant violation | | Guilty/Not Guilty | C/FP/FN | |
| 4 — Race condition | | Guilty/Not Guilty | C/FP/FN | |
| 5 — Undeclared ID | | Guilty/Not Guilty | C/FP/FN | |

**C** = Correct prediction | **FP** = Predicted Guilty; Not Guilty | **FN** = Predicted Not Guilty; Guilty

**Calibration score**: [C rows] / 5 x 100% = _____%

If below 60%: one sentence identifying whether the documentation's claimed defenses were
overstated (leading to FP predictions) or understated (leading to FN findings).

### 7B — Documentation Verdict

Two to three sentences for the documentation author:
- Which charge produced the most significant finding and what must be corrected?
- Did the numeric/temporal invariant's enforcement claim hold up in Charge 3?
  If "Silent" appeared in INV-ID enforcement in Part 2C: name the mechanism that must be added.

**Part 7 exit gate (C-21 + C-25 + C-24):**
- [ ] Every row in 7A has a Code and an explanation
- [ ] Calibration score computed
- [ ] Below-60% diagnosis written if needed
- [ ] Documentation verdict addresses the numeric/temporal invariant explicitly
```

---

## Summary Table

| Variation | Primary Axis | Secondary Axis | Domain | Key C-09 Mechanism |
|-----------|-------------|----------------|--------|-------------------|
| V-01 | Output format (per-type subsections) | — | Finance | Blank subsection = structural gap; "None" requires written acquittal + trace extension instruction |
| V-02 | Role sequence (specialist Auditors per type) | — | Customer Service | Unfilled Auditor role = visible structural failure; each role must deliver or extend the trace |
| V-03 | Phrasing register (imperative commitment) | — | Sales | "Find it. There is one." per type; "None" requires writing two trace steps, then finding the type |
| V-04 | Lifecycle emphasis (phase-per-type) | Output format | Finance | Sub-phase exit gate requires a finding; phase cannot close until finding or trace extension complete |
| V-05 | Role sequence (prosecution) | Inertia framing (doc-vs-trace) | Sales | Four formal charges; "Not Guilty" requires a named structural defense, not a blank "None" row |
