# trace-state Variations R4

---

## V-01 — Axis: Role Sequence (Finance Expert Leads)

**Hypothesis**: Seeding with a Finance domain expert in position 1 anchors the entity lifecycle in accounting vocabulary before the state machine analyst ever sees it, producing tighter INV-IDs (amount constraints, ledger balance rules) than when the analyst invents the domain from scratch.

---

```markdown
You are running **trace-state** for a Finance domain entity.
Roles execute in sequence: Finance Expert → State Machine Analyst → ANOMALY FINDER (two passes).

---

## ROLE 1 — Finance Domain Expert

Name a Finance entity with a realistic multi-stage lifecycle.
Good candidates: Invoice, Expense Claim, Purchase Order, Journal Entry, Budget Allocation.

Provide:
- **Entity**: [name]
- **Business purpose**: one sentence
- **Lifecycle sketch**: ordered list of states the entity moves through, in plain English
- **Who acts on it**: which roles (AP clerk, approver, controller, system) trigger state changes
- **What can go wrong**: one or two failure modes you've seen in real Finance workflows

Do not declare IDs yet — just set the scene for the Analyst.

---

## ROLE 2 — State Machine Analyst

Using the Finance Expert's scene, formalize the state machine.

### 2A — State Declaration

| S-ID | State Name | Entry Condition | Description |
|------|------------|-----------------|-------------|
| S-01 | | | |

*Entry Condition* = what must be true about the entity to be in this state at all,
not just what caused the transition into it. Be state-specific; "data is valid" does not pass.

### 2B — Operation Declaration

| OP-ID | Operation | Valid-From S-IDs | Produces S-ID | Actor | Guard |
|-------|-----------|-----------------|---------------|-------|-------|
| OP-01 | | | | | |

*Guard* = any additional condition beyond the Valid-From state that must hold.

### 2C — Invariant Declaration

| INV-ID | Invariant Statement | Scope (states) | Violation Consequence |
|--------|---------------------|----------------|----------------------|
| INV-01 | | | |

At least two invariants. At least one must constrain a numeric or temporal value
(e.g., "approved amount ≤ budget line remaining", "payment date ≥ invoice date").

---

## ROLE 3 — Step-by-Step Trace

Trace at least 7 operations as numbered steps.
Include at least one happy path sequence and one negative path (rejected transition).

**Step N — [OP-ID]: [Operation Name]**
- **Before**: [S-ID] — [State Name] | [key field values]
- **Preconditions** (state-specific):
- **Execution**:
- **After**: [S-ID] — [State Name] | [key field values changed]
- **Postconditions**:
- **Invariants checked**: [INV-IDs] — pass / fail

For the negative-path step: name the precondition that fails and the expected rejection behavior.

---

## ANOMALY FINDER — Pass 1: State Machine Only

*Read only the declaration tables (Sections 2A–2C). Do not re-read the trace steps yet.*

Predict which anomaly types exist before reading the evidence:

| Anomaly Type | Predicted (Y/N) | Rationale (from declaration tables only) |
|--------------|----------------|------------------------------------------|
| Invalid transition | | |
| Missing precondition check | | |
| Invariant violation | | |
| Race condition | | |
| Undeclared ID reference | | |

---

## ANOMALY FINDER — Pass 2: Full Trace

Now read the complete trace. Build the sweep table:

| Type | Found/None | Count | Strength | Triggering OP-ID | Affected S-ID | INV-ID | Predicted? |
|------|-----------|-------|----------|-----------------|--------------|--------|-----------|
| Invalid transition | | | | | | N/A | |
| Missing precondition | | | | | | N/A | |
| Invariant violation | | | | | | | |
| Race condition | | | | | | N/A | |
| Undeclared ID reference | | | | | | N/A | |

**Strength scale**:
- **1** — Present but minor: edge case, unlikely in normal operation
- **2** — Moderate: reachable in standard workflows, could reach production
- **3** — Critical: likely data loss, silent corruption, or incorrect ledger state

**Quality gate**: PASS requires (a) ≥ 2 rows "Found" AND (b) ≥ 1 "Found" row with Strength ≥ 2.
If the gate fails, add a *Gap note* naming which additional OP-IDs would expose the missing types.

**Reconciliation**:

| Type | Predicted | Found | Match? | Surprise |
|------|-----------|-------|--------|----------|
| Invalid transition | | | | |
| Missing precondition | | | | |
| Invariant violation | | | | |
| Race condition | | | | |
| Undeclared ID reference | | | | |

---

## Anomaly Register

One row per "Found" verdict:

| A-ID | Type | OP-ID | S-ID | INV-ID | Description | Severity | Strength |
|------|------|-------|------|--------|-------------|----------|---------|
| A-01 | | | | | | | |

Rules:
- No blank cells in a found-verdict row; use "N/A: [reason]" where genuinely inapplicable
- Severity: Low / Medium / High / Critical
- Strength matches the sweep table entry
- If an OP-ID, S-ID, or INV-ID is referenced here but was not declared in Section 2, that reference is itself an Undeclared ID anomaly — add a row
```

---

## V-02 — Axis: Output Format (Evidence-Strength as First-Class Column)

**Hypothesis**: Defining the 1/2/3 evidence-strength scale at the top of the prompt — before any declarations — primes the model to annotate strength on every finding as it goes, rather than retrofitting scores at the sweep stage. This produces more accurate Strength values because the model is reasoning about reachability at the moment of discovery, not after the fact.

---

```markdown
You are running **trace-state** for a Customer Service domain entity.
This prompt produces a fully tabular output. Every section is a structured table.
Evidence strength (1/2/3) is tracked from the first anomaly you identify — not retroactively.

---

## Evidence Strength Scale (Read Before Anything Else)

You will assign a Strength score to every anomaly you find, at the moment you find it:

| Score | Meaning | Test |
|-------|---------|------|
| **1** | Present but minor | Requires unusual sequence or adversarial actor to trigger |
| **2** | Moderate | Reachable in standard CS workflows; a support agent could hit this |
| **3** | Critical | Likely to corrupt state silently, expose customer data, or loop indefinitely |

Do not average or adjust scores after the sweep. Score at point of discovery.

---

## Section 1 — Entity and Domain

Select a Customer Service entity: Support Ticket, Escalation, SLA Contract, Refund Request, or Agent Case.

| Field | Value |
|-------|-------|
| Entity | |
| Domain | Customer Service |
| Business purpose | |
| Primary actor | |
| Secondary actors | |

---

## Section 2 — State Declarations

| S-ID | State Name | Entry Condition | Terminal? |
|------|------------|-----------------|-----------|
| S-01 | | | |

*Minimum 5 states. Terminal = no valid outbound operations.*

---

## Section 3 — Operation Declarations

| OP-ID | Operation | Valid-From S-IDs | Produces S-ID | Guard | Actor |
|-------|-----------|-----------------|---------------|-------|-------|
| OP-01 | | | | | |

*Minimum 6 operations. Guard = any condition beyond state membership required to execute.*

---

## Section 4 — Invariant Declarations

| INV-ID | Invariant | Scope | Violation Consequence |
|--------|-----------|-------|----------------------|
| INV-01 | | | |

*Minimum 3 invariants. At least one must involve a time constraint (e.g., SLA deadline).*

---

## Section 5 — Step-by-Step Trace

Trace at least 7 operations. One step must be a negative path (rejected transition).

| Step | OP-ID | Before S-ID | Preconditions Met? | After S-ID | Postconditions | INV-IDs Checked | Result |
|------|-------|-------------|-------------------|------------|----------------|-----------------|--------|
| 1 | | | | | | | Pass/Reject |

*For Reject rows: name the failing precondition and expected system response.*

---

## Section 6 — Pre-Sweep Hypothesis (State Machine Only)

*Scan Sections 2–4 only. Do not re-read Section 5.*

| Anomaly Type | Predicted | Confidence (H/M/L) | Evidence from Declaration Tables |
|--------------|-----------|-------------------|----------------------------------|
| Invalid transition | | | |
| Missing precondition check | | | |
| Invariant violation | | | |
| Race condition | | | |
| Undeclared ID reference | | | |

---

## Section 7 — Anomaly Sweep (Full Trace Pass)

*Now read Section 5 in full. Complete the sweep table, assigning Strength at point of discovery.*

| Type | Found/None | Count | Strength | Triggering OP-ID | Affected S-ID | Affected INV-ID | Predicted? | Prediction Match? |
|------|-----------|-------|----------|-----------------|--------------|----------------|-----------|-----------------|
| Invalid transition | | | | | | N/A | | |
| Missing precondition | | | | | | N/A | | |
| Invariant violation | | | | | | | | |
| Race condition | | | | | | N/A | | |
| Undeclared ID reference | | | | | | N/A | | |

**Quality gate**:
- Gate A (quantity): ≥ 2 rows "Found"
- Gate B (quality): ≥ 1 "Found" row with Strength ≥ 2
- Gate C (ID discipline): every cell in a "Found" row has either a declared ID or "N/A: [reason]" — no blank cells

If any gate fails: add a *Gap note* row at the bottom naming the corrective action.

---

## Section 8 — Anomaly Register

| A-ID | Type | OP-ID | S-ID | INV-ID | Description | Severity | Strength | Reachability Path |
|------|------|-------|------|--------|-------------|----------|---------|------------------|
| A-01 | | | | | | | | |

*Reachability path* = shortest sequence of operations from the initial state that triggers this anomaly.
*Severity*: Low / Medium / High / Critical.

---

## Section 9 — Reconciliation Summary

| Type | Predicted | Found | Match? | What the trace revealed that the declaration tables hid |
|------|-----------|-------|--------|--------------------------------------------------------|
| Invalid transition | | | | |
| Missing precondition | | | | |
| Invariant violation | | | | |
| Race condition | | | | |
| Undeclared ID reference | | | | |
```

---

## V-03 — Axis: Phrasing Register (Conversational / Practitioner Workshop)

**Hypothesis**: An imperative, second-person, workshop-style prompt reduces structural scaffolding overhead and gets faster to anomaly discovery. The model spends less effort reproducing template boilerplate and more effort reasoning about the domain. Tradeoff: less mechanical completeness on ID cross-referencing.

---

```markdown
You're about to hand-compile a state machine trace for a Sales domain entity.
Think of this as a workshop, not a report. Work through it step by step.
You're playing three roles: the Sales expert who knows the domain, the analyst who builds
the machine, and the anomaly hunter who tears it apart.

---

### Step 1: Pick your entity and tell me why it matters

Choose a Sales entity with a real lifecycle: Deal, Opportunity, Quote, Sales Order,
Commission Calculation, or Territory Assignment.

Write two to three sentences as the Sales expert:
- What is this entity?
- What does it mean when it reaches each major state?
- What's the one failure mode that costs the sales team the most?

---

### Step 2: Build the state machine — declare everything with IDs

Here's your discipline: every state gets an S-ID, every operation gets an OP-ID,
every invariant gets an INV-ID. You'll need these IDs later. If you reference something
without declaring it, that's a finding.

**States** — at least 5, including at least one terminal state:

| S-ID | Name | Entry Condition | Terminal? |
|------|------|-----------------|-----------|
| S-01 | | | |

*Entry condition = what must be true about the entity to be in this state, not just how it got here.*

**Operations** — at least 6, covering the full lifecycle:

| OP-ID | Name | Allowed From | Leads To | Guard | Who does it |
|-------|------|-------------|---------|-------|-------------|
| OP-01 | | | | | |

**Invariants** — at least 3, at least one involving a dollar amount or date constraint:

| INV-ID | Rule | When it applies | What breaks if violated |
|--------|------|-----------------|------------------------|
| INV-01 | | | |

---

### Step 3: Walk through the lifecycle

Trace at least 7 operations. Show the entity state before and after each one.
Include at least one moment where someone tries to do something they shouldn't —
and show how the system pushes back.

For each step, write it out like this:

**Step N — [OP-ID] [Operation name]**
Before: [S-ID] with [key field values]
Preconditions: (be specific — "deal is valid" doesn't count)
What happens:
After: [S-ID] with [key field values changed]
Postconditions:
Invariants in play: [INV-IDs]

---

### Step 4: Before you look at the trace — what do you predict?

Look only at your state machine tables. Not the trace.
Based on the structure alone, what anomalies do you expect to find when you read it?

| Type | Predict it's there? | Why (from the tables) |
|------|--------------------|-----------------------|
| Invalid transition | | |
| Missing precondition | | |
| Invariant violation | | |
| Race condition | | |
| Undeclared ID reference | | |

---

### Step 5: Now read the trace and hunt

Go back through every step. For each anomaly type, ask yourself:
- **Invalid transition**: did anything move between states without a valid operation?
- **Missing precondition**: did any operation execute when a guard condition wasn't checked?
- **Invariant violation**: did any state change break one of your INV-IDs?
- **Race condition**: if two operations ran concurrently on this entity, what would break?
- **Undeclared ID reference**: did you use an S-ID, OP-ID, or INV-ID that isn't in your tables?

Fill in the sweep table. Rate each finding on strength (1 = edge case, 2 = reachable in practice, 3 = likely data corruption):

| Type | Found? | Count | Strength | Where (OP-ID + S-ID) | Predicted? |
|------|--------|-------|----------|---------------------|-----------|
| Invalid transition | | | | | |
| Missing precondition | | | | | |
| Invariant violation | | | | | |
| Race condition | | | | | |
| Undeclared ID reference | | | | | |

**Check your work**: you need at least 2 "Found" rows, and at least 1 of them at Strength ≥ 2.
If you don't have that, you haven't looked hard enough — add operations or states that expose the gap.

---

### Step 6: Log the anomalies

One row per finding. No blank cells — if an ID doesn't apply, say "N/A: [why]".

| A-ID | Type | OP-ID | S-ID | INV-ID | What breaks | How bad | Strength |
|------|------|-------|------|--------|------------|---------|---------|
| A-01 | | | | | | | |

---

### Step 7: What surprised you?

Compare your Step 4 predictions to what you actually found.
For each type: did it match? What did the trace reveal that the state machine tables hid from you?

One sentence per type. Be honest about misses.
```

---

## V-04 — Axes: Role Sequence + Lifecycle Emphasis (Explicit Phase Boundaries)

**Hypothesis**: Combining an explicit role sequence (CS Expert → Lifecycle Analyst → Anomaly Hunter) with equally-weighted phase sections — each with a stated entry criterion and exit deliverable — prevents the model from rushing through declarations to get to the "interesting" anomaly section. Phase exit criteria act as mechanical quality gates before the next phase begins.

---

```markdown
You are running **trace-state** for a Customer Service domain entity.
This session has four phases. Each phase has an entry criterion and an exit deliverable.
You must complete each phase before advancing. Do not read ahead.

Roles:
- **CS Domain Expert** — sets the scene, names failure modes, establishes vocabulary
- **Lifecycle Analyst** — formalizes states, operations, invariants with full ID discipline
- **Anomaly Hunter** — runs two-pass sweep with hypothesis-first protocol

---

## ═══ PHASE 1: DOMAIN SETUP ═══
*Entry*: none
*Exit deliverable*: signed-off entity profile (CS Expert confirms it's realistic)

**[CS Domain Expert]**

Choose a Customer Service entity: Support Ticket, Customer Complaint, Refund Request,
Escalation Case, or SLA Breach Incident.

Provide:

**Entity profile**:
- Entity name:
- Business purpose (one sentence):
- States it passes through (plain English, no IDs yet):
- Actors who touch it (roles, not names):
- The failure mode that generates the most re-open tickets:
- An invariant that finance or legal cares about:

**CS Expert sign-off**: Confirm this profile matches a workflow you'd see in a real
CS operation. Note any edge case the Analyst should model.

*Phase 1 complete when*: entity profile includes at least 5 lifecycle states, at least 3 actors,
and at least 1 explicitly named invariant.

---

## ═══ PHASE 2: STATE MACHINE DECLARATION ═══
*Entry*: Completed Phase 1 entity profile
*Exit deliverable*: Three declaration tables with full ID coverage

**[Lifecycle Analyst]**

### 2A — States

| S-ID | State Name | Entry Condition | Description | Terminal? |
|------|------------|-----------------|-------------|-----------|
| S-01 | | | | |

*Minimum 5 states. Entry Condition must be state-specific, not generic.*

### 2B — Operations

| OP-ID | Operation | Valid-From S-IDs | Produces S-ID | Guard | Actor |
|-------|-----------|-----------------|---------------|-------|-------|
| OP-01 | | | | | |

*Minimum 7 operations. Guard = condition beyond state membership.*

### 2C — Invariants

| INV-ID | Invariant | Scope (S-IDs) | Violation Consequence | Detectable by |
|--------|-----------|--------------|----------------------|---------------|
| INV-01 | | | | |

*Minimum 3 invariants. At least one must constrain an SLA timer or escalation deadline.*

### 2D — ID Coverage Check

Before advancing: verify that every S-ID, OP-ID, and INV-ID used in 2B and 2C
was declared in 2A, 2B, or 2C. List any forward or dangling references here
(they become Undeclared ID anomaly candidates in Phase 4).

| Undeclared reference found | Type | Declared in | Action |
|---------------------------|------|------------|--------|
| (none) or [list] | | | |

*Phase 2 complete when*: all three tables are populated, ID coverage check is done.

---

## ═══ PHASE 3: STEP-BY-STEP TRACE ═══
*Entry*: Completed Phase 2 tables
*Exit deliverable*: Numbered trace with at least 7 steps including one negative path

**[Lifecycle Analyst]**

Trace the entity lifecycle from initial state through resolution. For each step:

**Step N — [OP-ID]: [Operation Name]**
- **Before**: [S-ID] [State Name] | [relevant field values]
- **Preconditions**:
- **Operation execution**:
- **After**: [S-ID] [State Name] | [changed field values]
- **Postconditions**:
- **Invariants active**: [INV-IDs] — ✓ holds / ✗ violated
- **Guard evaluated**: [guard condition result]

Include:
- At least one complete happy-path sequence (ticket opened → resolved → closed)
- At least one negative path: operation attempted from invalid state, with rejection behavior
- At least one concurrent scenario setup (two operations that could race)

*Phase 3 complete when*: ≥ 7 steps, all three trace types covered, no step uses an
undeclared S-ID, OP-ID, or INV-ID.

---

## ═══ PHASE 4: ANOMALY DETECTION ═══
*Entry*: Completed Phases 1–3
*Exit deliverable*: Pre-sweep hypothesis, two-pass sweep table, quality-gated register

**[Anomaly Hunter]**

### 4A — Pass 1: State Machine Hypothesis

*Scan Phases 2A–2C only. Do not re-read Phase 3.*

| Anomaly Type | Predicted | Confidence | Structural evidence (declaration tables only) |
|--------------|-----------|------------|----------------------------------------------|
| Invalid transition | | H/M/L | |
| Missing precondition check | | H/M/L | |
| Invariant violation | | H/M/L | |
| Race condition | | H/M/L | |
| Undeclared ID reference | | H/M/L | |

### 4B — Pass 2: Full Trace Sweep

*Now read Phase 3 in full. Score Strength at moment of discovery, not afterward.*

**Strength**: 1 = edge case only | 2 = reachable in normal CS workflows | 3 = likely to corrupt state or breach SLA silently

| Type | Found/None | Count | Strength | OP-ID | S-ID | INV-ID | Predicted? |
|------|-----------|-------|----------|-------|------|--------|-----------|
| Invalid transition | | | | | | N/A | |
| Missing precondition | | | | | | N/A | |
| Invariant violation | | | | | | | |
| Race condition | | | | | | N/A | |
| Undeclared ID reference | | | | | | N/A | |

**Quality gate** — three conditions must all hold:
1. **Quantity**: ≥ 2 "Found" rows
2. **Quality**: ≥ 1 "Found" row with Strength ≥ 2
3. **ID discipline**: zero blank cells in any "Found" row (use "N/A: [reason]" where not applicable)

If any condition fails: write a *Remediation note* identifying the specific gap and what
Phase 3 additions would close it.

### 4C — Reconciliation

| Type | Pass 1 Predicted | Pass 2 Found | Match | What the trace revealed that the tables concealed |
|------|-----------------|-------------|-------|--------------------------------------------------|
| Invalid transition | | | Y/N | |
| Missing precondition | | | Y/N | |
| Invariant violation | | | Y/N | |
| Race condition | | | Y/N | |
| Undeclared ID reference | | | Y/N | |

### 4D — Anomaly Register

| A-ID | Type | OP-ID | S-ID | INV-ID | Description | Severity | Strength | Reachability |
|------|------|-------|------|--------|-------------|----------|---------|--------------|
| A-01 | | | | | | | | |

*Severity*: Low / Medium / High / Critical
*Reachability*: shortest OP-ID sequence from S-01 that triggers this anomaly

*Phase 4 complete when*: quality gate passes, register has no blank cells in found-verdict rows.*
```

---

## V-05 — Axes: Output Format + Inertia Framing (Contrast with Status-Quo Implementation)

**Hypothesis**: Framing the trace explicitly against "what the current implementation claims to do" vs. "what the trace reveals" sharpens anomaly detection by forcing the model to maintain two parallel representations. The status-quo framing activates a different reasoning mode — looking for gaps between stated behavior and actual behavior — than the standard "find anomalies in a clean state machine" prompt.

---

```markdown
You are running **trace-state** for a Sales domain entity.
This prompt has a specific framing: you are auditing a state machine that already exists
in a production system. The system has documentation. The documentation makes claims.
Your job is to compile the trace and find where the claims break down.

You play two alternating voices throughout:
- **The Documentation** — what the system is supposed to do (set up by the Sales Expert)
- **The Trace** — what actually happens when you run the operations (compiled by the Analyst)

Gaps between Documentation and Trace are the signal.

---

## Part 1 — What the Documentation Claims

**[Sales Domain Expert]**

Pick a Sales entity: Deal, Quote, Sales Order, Compensation Plan, or Discount Approval.

Write the documentation voice: a short description of how the entity is supposed to work,
as if you were the original developer explaining it to a new hire.
Include:
- The states the entity moves through
- The key operations that advance it
- The invariants the system is supposed to enforce
- Any known edge cases the documentation acknowledges

This is the "official story." It will be challenged by the trace.

---

## Part 2 — State Machine Formalization

**[Lifecycle Analyst]**

Formalize the Documentation claims with full ID discipline.

### States

| S-ID | State Name | Entry Condition | Doc Reference |
|------|------------|-----------------|---------------|
| S-01 | | | (quote the relevant claim from Part 1) |

*Doc Reference*: quote or paraphrase the Part 1 text that implies this state exists.
Any state you declare that has no Doc Reference is an undocumented state — flag it.

### Operations

| OP-ID | Operation | Valid-From S-IDs | Produces S-ID | Guard | Doc Reference |
|-------|-----------|-----------------|---------------|-------|---------------|
| OP-01 | | | | | |

*Any operation with no Doc Reference is undocumented behavior.*

### Invariants

| INV-ID | Invariant | Scope | Doc Reference | Enforcement mechanism claimed |
|--------|-----------|-------|---------------|-------------------------------|
| INV-01 | | | | |

*Enforcement mechanism*: what the documentation says prevents a violation (e.g., "system rejects if...").
Leave blank if the documentation is silent on enforcement — that silence is a finding.

---

## Part 3 — Pre-Sweep Hypothesis (Documentation Voice)

*Reading only Parts 1 and 2, not the trace you are about to compile:*

Where do you expect the Documentation to be wrong?

| Anomaly Type | The Documentation Claims | What the Trace Might Actually Show | Confidence |
|--------------|--------------------------|-----------------------------------|-----------|
| Invalid transition | | | H/M/L |
| Missing precondition check | | | H/M/L |
| Invariant violation | | | H/M/L |
| Race condition | | | H/M/L |
| Undeclared ID reference | | | H/M/L |

---

## Part 4 — The Trace

**[Lifecycle Analyst]**

Compile the actual trace. For each step, show both voices:

**Step N — [OP-ID]: [Operation Name]**

| | Documentation Claims | Trace Shows |
|-|---------------------|-------------|
| **Before state** | [what the doc says should be the valid prior state] | [S-ID and field values] |
| **Preconditions** | [what the doc says must hold] | [what the trace checks — or fails to check] |
| **After state** | [what the doc says the result should be] | [S-ID and field values] |
| **Invariants** | [INV-IDs the doc says are enforced] | [which actually hold, which do not] |
| **Gap** | — | [any discrepancy between columns, or "none"] |

Include at least 7 steps. Include:
- One happy path with no gap
- One negative path where the documentation claims rejection occurs
- One step where the Documentation claims an invariant is enforced but the trace reveals it is not (or vice versa)

---

## Part 5 — Anomaly Sweep

Read the full Part 4 trace. Build the sweep table.

**Strength scale**:
- **1** — Gap exists but is academic: only reachable via adversarial input or unlikely concurrency
- **2** — Gap is reachable: a Sales rep following normal workflow could trigger this
- **3** — Gap is critical: will produce wrong commission calculations, lost deals, or audit failures

| Type | Found/None | Count | Strength | OP-ID | S-ID | INV-ID | Gap column ref | Predicted? |
|------|-----------|-------|----------|-------|------|--------|---------------|-----------|
| Invalid transition | | | | | | N/A | Step N | |
| Missing precondition | | | | | | N/A | Step N | |
| Invariant violation | | | | | | | Step N | |
| Race condition | | | | | | N/A | Step N | |
| Undeclared ID reference | | | | | | N/A | — | |

**Quality gate**: PASS requires ≥ 2 "Found" rows AND ≥ 1 with Strength ≥ 2.
If gate fails: name which Documentation claim was too optimistic and what additional
operation would surface the missing anomaly type.

---

## Part 6 — Anomaly Register

| A-ID | Type | OP-ID | S-ID | INV-ID | Documentation Claim | What Trace Found | Delta | Severity | Strength |
|------|------|-------|------|--------|---------------------|-----------------|-------|----------|---------|
| A-01 | | | | | | | | | |

*Delta*: one sentence describing the gap between the claim and the finding.
*Severity*: Low / Medium / High / Critical — rated from the Sales team's perspective
(wrong commission = Critical; cosmetic label mismatch = Low).

---

## Part 7 — Reconciliation

| Type | Part 3 Prediction | Part 5 Finding | Match? | What the Documentation hid |
|------|------------------|----------------|--------|---------------------------|
| Invalid transition | | | Y/N | |
| Missing precondition | | | Y/N | |
| Invariant violation | | | Y/N | |
| Race condition | | | Y/N | |
| Undeclared ID reference | | | Y/N | |

**Closing note** (Documentation Voice):
Summarize in two to three sentences what the Documentation would need to be updated to say,
given the trace findings.
```

---

## Summary Table

| Variation | Primary Axis | Secondary Axis | Domain | Key Structural Bet |
|-----------|-------------|----------------|--------|-------------------|
| V-01 | Role sequence (Finance-first) | — | Finance | Finance Expert anchors INV-IDs in accounting constraints before Analyst touches it |
| V-02 | Output format (table-centric) | — | CS | Strength scoring defined first primes earlier, more accurate annotation |
| V-03 | Phrasing register (conversational) | — | Sales | Workshop tone reduces boilerplate pressure, more reasoning per word |
| V-04 | Role sequence | Lifecycle emphasis (explicit phases) | CS | Phase entry/exit criteria prevent rushing to anomaly section |
| V-05 | Output format (two-voice) | Inertia framing (doc vs. trace) | Sales | Documentation/Trace contrast activates gap-detection reasoning mode |
