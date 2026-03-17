R5 variations written. Here's what was generated:

---

## trace-state Variations R5 — Summary

Five complete, runnable prompt bodies (V-01 through V-05), each incorporating C-20, C-21, and C-22 from rubric v5.

### Single-axis variations (3):

| Variation | Axis | Domain | Core Bet |
|-----------|------|--------|----------|
| **V-01** | Role sequence | Sales | Numeric/temporal invariant gate lives in the domain expert role (1B), not the analyst's formalization tables. Expert declares the threshold; analyst inherits it with an INV-ID. Harder to produce a generic invariant when forced to write a falsification test first. |
| **V-02** | Output format | Finance | Replaces binary expected/surprising with a 3-value taxonomy (C/FP/FN) and computes a numeric calibration score. A score below 60% is a second quality gate signaling structurally misleading declaration tables. |
| **V-03** | Phrasing register | Customer Service | Workshop voice with a "score-aloud protocol" — the model is told to score Strength before writing anything else about a finding. Makes C-22 a verbal discipline, not a table-filling task. |

### Combined-axis variations (2):

| Variation | Axes | Domain | Core Bet |
|-----------|------|--------|----------|
| **V-04** | Role sequence + Lifecycle emphasis | Finance | Phase exit gates make the numeric invariant gate and Surprise column explicit completion criteria — checkboxes that prevent them from being treated as optional boilerplate. |
| **V-05** | Inertia framing + Output format | Sales | Documentation-vs-trace framing combined with a full Calibration Report section (FP/FN/C + calibration score + Documentation Verdict paragraph). Two simultaneous gap-detection modes — structural and predictive. |
omain Consequence if Violated |
|---|--------------------------|--------------------------|-------------------|---------------------------------|
| 1 | | | e.g., "create a quote where discount > 40% — does the system reject it?" | |
| 2 | | | | |

**Gate**: The Analyst may not start Section 2 until this table has at least two rows
with non-blank Falsification Tests referencing specific thresholds, ratios, or date constraints.
Generic invariants ("amounts must be valid", "dates must be set") do not pass this gate.

---

## ROLE 2 — State Machine Analyst

Using the Sales Expert's scene and pre-declared invariants, formalize the state machine.

### 2A — State Declaration

| S-ID | State Name | Entry Condition | Description | Terminal? |
|------|------------|-----------------|-------------|-----------|
| S-01 | | | | |

*Entry Condition* = what must be true about the entity to be in this state, not just what
caused the transition. Be state-specific; "data is valid" does not pass. Minimum 5 states.

### 2B — Operation Declaration

| OP-ID | Operation | Valid-From S-IDs | Produces S-ID | Actor | Guard |
|-------|-----------|-----------------|---------------|-------|-------|
| OP-01 | | | | | |

*Guard* = any condition beyond Valid-From state membership required to execute. Minimum 7 operations.

### 2C — Invariant Declaration

Assign INV-IDs to the pre-declared invariants from Role 1B first. Add structural invariants as needed.

| INV-ID | Invariant Statement | Scope (S-IDs) | Source | Violation Consequence | Enforcement Mechanism |
|--------|---------------------|--------------|--------|-----------------------|----------------------|
| INV-01 | (from 1B row 1) | | Expert | | |
| INV-02 | (from 1B row 2) | | Expert | | |

*Source*: Expert = from Role 1B; Analyst = identified during formalization.
At least one INV-ID must map directly to each of the two pre-declared invariants from 1B.

### 2D — ID Coverage Check

Before advancing: list any S-ID, OP-ID, or INV-ID referenced in 2B or 2C but not yet declared.

| Undeclared Reference | Type | Appears In | Action |
|---------------------|------|------------|--------|
| (none) or [list] | | | Declare now / Flag as anomaly candidate |

---

## ROLE 3 — Step-by-Step Trace

Trace at least 7 operations as numbered steps. Include:
- At least one complete happy-path sequence
- At least one negative path (rejected transition with precondition failure named)
- At least one concurrent scenario setup (two operations that could race on the same entity)

**Step N — [OP-ID]: [Operation Name]**
- **Before**: [S-ID] — [State Name] | [key field values]
- **Preconditions** (state-specific, name the field and value):
- **Execution**:
- **After**: [S-ID] — [State Name] | [key field values changed]
- **Postconditions**:
- **Invariants checked**: [INV-IDs] — pass / fail
- **Guard evaluated**: [result]

For negative-path steps: name the failing precondition and expected rejection behavior.
For concurrent setup steps: name the two competing operations and the conflicting outcome.

---

## ANOMALY FINDER — Pass 1: State Machine Only

*Read only Sections 2A–2C and Role 1B. Do not re-read Role 3 yet.*

Predict which anomaly types exist before reading the trace evidence:

| Anomaly Type | Predicted (Y/N) | Confidence | Rationale (declaration tables and invariant pre-declaration only) |
|--------------|----------------|------------|------------------------------------------------------------------|
| Invalid transition | | H/M/L | |
| Missing precondition check | | H/M/L | |
| Invariant violation | | H/M/L | |
| Race condition | | H/M/L | |
| Undeclared ID reference | | H/M/L | |

---

## ANOMALY FINDER — Pass 2: Full Trace Sweep

Now read Role 3 in full. Assign Strength **at the moment you identify each finding** —
do not adjust scores after completing the sweep.

**Strength scale**:
- **1** — Present but minor: only reachable via adversarial input or unusual sequence
- **2** — Moderate: reachable in normal Sales workflows; a rep following process could trigger this
- **3** — Critical: likely silent data corruption, incorrect commission, or lost deal record

| Type | Found/None | Count | Strength | Triggering OP-ID | Affected S-ID | INV-ID | Predicted? |
|------|-----------|-------|----------|-----------------|--------------|--------|-----------|
| Invalid transition | | | | | | N/A | |
| Missing precondition | | | | | | N/A | |
| Invariant violation | | | | | | | |
| Race condition | | | | | | N/A | |
| Undeclared ID reference | | | | | | N/A | |

**Quality gate**: PASS requires (a) >= 2 rows "Found" AND (b) >= 1 "Found" row with Strength >= 2.
If the gate fails: add a *Gap note* naming which additional OP-IDs would expose the missing types.

**Reconciliation**:

| Type | Predicted | Found | Match? | Surprise | Surprise Explanation |
|------|-----------|-------|--------|----------|---------------------|
| Invalid transition | | | Y/N | Expected / Surprising | |
| Missing precondition | | | Y/N | Expected / Surprising | |
| Invariant violation | | | Y/N | Expected / Surprising | |
| Race condition | | | Y/N | Expected / Surprising | |
| Undeclared ID reference | | | Y/N | Expected / Surprising | |

*Surprise*: **Expected** = the trace confirmed what the declaration tables implied.
**Surprising** = the trace contradicted the prediction in either direction (found when not predicted,
or not found when predicted). Write one sentence explaining why.

---

## Anomaly Register

One row per "Found" verdict. Assign Strength as you write each row — same score as the sweep table,
no revision.

| A-ID | Type | OP-ID | S-ID | INV-ID | Description | Severity | Strength |
|------|------|-------|------|--------|-------------|----------|---------|
| A-01 | | | | | | | |

Rules:
- No blank cells in a found-verdict row; use "N/A: [reason]" where genuinely inapplicable
- Severity: Low / Medium / High / Critical
- If any OP-ID, S-ID, or INV-ID referenced here was not declared in Section 2, that reference
  is itself an Undeclared ID anomaly — add a row
```

---

## V-02 — Axis: Output Format (Surprise Taxonomy with Three-Value Classification)

**Hypothesis**: Replacing the binary expected/surprising label with a three-value taxonomy (C = Calibrated, FP = False Positive, FN = False Negative) and computing a numeric calibration score creates a stronger quality signal than a match/mismatch column. The model must classify each prediction outcome precisely, and the calibration score creates a second gate: a score below 60% indicates the declaration tables are structurally misleading.

---

```markdown
You are running **trace-state** for a Finance domain entity.
This prompt produces fully tabular output. Every section is a structured table.

Two prompt-engineering constraints apply throughout:
1. **Score at point of discovery** — assign evidence Strength when you first identify each finding,
   not after the full sweep is complete. Do not revise scores retroactively.
2. **Surprise taxonomy** — the reconciliation table uses three codes, not a binary flag:
   C = Calibrated, FP = False Positive, FN = False Negative (defined below).

---

## Surprise Taxonomy (Read Before Anything Else)

| Code | Label | Meaning |
|------|-------|---------|
| **C** | Calibrated | Predicted correctly — trace confirmed the prediction |
| **FP** | False Positive | Predicted the anomaly type; trace did not find it |
| **FN** | False Negative | Did not predict the anomaly type; trace found it |

A calibration score is computed at the end:
- Correct predictions (C) / total rows with a prediction x 100%
- Rows where Predicted = N and Found = None count as C (correctly predicted absence)
- A calibration score below 60% signals that the declaration tables are structurally misleading

---

## Section 1 — Entity Selection

| Field | Value |
|-------|-------|
| Entity | |
| Domain | Finance |
| Business purpose | |
| Lifecycle entry point (initial state) | |
| Terminal state(s) | |
| Primary actors | |

Choose from: Invoice, Expense Claim, Purchase Order, Journal Entry, Budget Allocation, Vendor Payment.

---

## Section 2 — Numeric/Temporal Invariant Pre-Declaration

Declare at least two falsifiable numeric or temporal invariants **before** building the state tables.
Generic invariants ("amounts must be set", "dates must not be null") do not pass this gate.
Each must name a specific threshold, ratio, deadline, or ordering constraint with a falsification test.

| INV-ID | Invariant Statement | Numeric / Temporal / Both | Falsification Test | Domain Consequence |
|--------|---------------------|--------------------------|-------------------|--------------------|
| INV-01 | | | | |
| INV-02 | | | | |

*Gate*: Do not start Section 3 until both rows have a non-blank Falsification Test referencing
a specific value, not a generic condition.

---

## Section 3 — State Declarations

| S-ID | State Name | Entry Condition | Description | Terminal? |
|------|------------|-----------------|-------------|-----------|
| S-01 | | | | |

*Minimum 5 states. Entry Condition must reference specific field values, amounts, or actor roles
— not generic validity statements.*

---

## Section 4 — Operation Declarations

| OP-ID | Operation | Valid-From S-IDs | Produces S-ID | Guard | Actor |
|-------|-----------|-----------------|---------------|-------|-------|
| OP-01 | | | | | |

*Minimum 7 operations. Guard = condition beyond state membership.*

---

## Section 5 — Full Invariant Declarations

Merge the pre-declared invariants from Section 2. Add structural invariants as needed.

| INV-ID | Invariant | Scope (S-IDs) | Violation Consequence | Enforcement Mechanism |
|--------|-----------|--------------|----------------------|-----------------------|
| INV-01 | (from Sec 2) | | | |
| INV-02 | (from Sec 2) | | | |

*Minimum 3 invariants total. At least one INV-ID must trace directly to each Section 2 row.*

---

## Section 6 — Step-by-Step Trace

| Step | OP-ID | Before S-ID | Preconditions Met? | Guard Result | After S-ID | Postconditions | INV-IDs Checked | Result |
|------|-------|------------|-------------------|-------------|-----------|----------------|-----------------|--------|
| 1 | | | | | | | | Pass/Reject |

*Minimum 7 steps. Include at least one Reject row (negative path) and one concurrent scenario setup.*
*For Reject rows: add a "Rejection reason" note below the row naming the failing precondition.*
*For concurrent setup: add a "Race scenario" note below the step describing the conflicting outcome.*

---

## Section 7 — Pre-Sweep Hypothesis

*Scan Sections 2–5 only. Do not re-read Section 6.*

| Anomaly Type | Predicted (Y/N) | Confidence | Structural evidence from declaration tables |
|--------------|----------------|------------|---------------------------------------------|
| Invalid transition | | H/M/L | |
| Missing precondition check | | H/M/L | |
| Invariant violation | | H/M/L | |
| Race condition | | H/M/L | |
| Undeclared ID reference | | H/M/L | |

---

## Section 8 — Full Trace Sweep

*Now read Section 6 in full. Score Strength at point of discovery — do not retroactively adjust.*

| Type | Found/None | Count | Strength | Triggering OP-ID | Affected S-ID | Affected INV-ID | Predicted? |
|------|-----------|-------|----------|-----------------|--------------|----------------|-----------|
| Invalid transition | | | | | | N/A | |
| Missing precondition | | | | | | N/A | |
| Invariant violation | | | | | | | |
| Race condition | | | | | | N/A | |
| Undeclared ID reference | | | | | | N/A | |

**Quality gate**:
- Gate A: >= 2 rows "Found"
- Gate B: >= 1 "Found" row with Strength >= 2
- Gate C: no blank cells in any "Found" row (use "N/A: [reason]" where not applicable)

If any gate fails: add a *Gap note* row identifying the corrective action and what additional
operations or states would close the gap.

---

## Section 9 — Reconciliation with Surprise Taxonomy

| Type | Predicted | Found | Match? | Surprise Code | Surprise Explanation |
|------|-----------|-------|--------|---------------|---------------------|
| Invalid transition | | | Y/N | C / FP / FN | |
| Missing precondition | | | Y/N | C / FP / FN | |
| Invariant violation | | | Y/N | C / FP / FN | |
| Race condition | | | Y/N | C / FP / FN | |
| Undeclared ID reference | | | Y/N | C / FP / FN | |

**Calibration score**: [# of C rows] / [rows with a prediction made] x 100% = _____%

If calibration score is below 60%: write one sentence identifying which structural property of
the declaration tables produced the most misleading predictions.

---

## Section 10 — Anomaly Register

| A-ID | Type | OP-ID | S-ID | INV-ID | Description | Severity | Strength | Reachability Path |
|------|------|-------|------|--------|-------------|----------|---------|------------------|
| A-01 | | | | | | | | |

*Reachability path*: shortest OP-ID sequence from the initial state that triggers this anomaly.
*Strength must match Section 8 — no revision permitted.*
*Severity*: Low / Medium / High / Critical.
```

---

## V-03 — Axis: Phrasing Register (Conversational / Score-Aloud Protocol)

**Hypothesis**: A workshop-style prompt that frames strength scoring as a spoken discipline ("score it before you write it down") creates a verbal checkpoint that prevents retroactive score assignment, compared to a table-centric prompt where all Strength cells can be filled in a final editing pass. The conversational register also makes the Surprise column feel like a natural retrospective ("be honest about what you didn't see coming") rather than bureaucratic bookkeeping.

---

```markdown
You're hand-compiling a state machine trace for a Customer Service domain entity.
This is a workshop, not a report. Three rules matter more than any template format:

**Rule 1 — Score as you go.**
The moment you identify a finding, score its Strength (1/2/3) before writing anything else.
If you catch yourself filling in Strength cells at the end of the sweep, stop. Go back.
Score at the point of discovery — not retroactively.

**Rule 2 — At least one invariant must name a real limit.**
An SLA timer, response-time threshold, or re-open count cap. "Tickets must be valid" doesn't count.
"Priority-1 tickets must reach an agent within 15 minutes of submission" counts.

**Rule 3 — Be honest in the Surprise column.**
When you predicted an anomaly and didn't find it, or missed one you should have caught —
say so. The Surprise column is a calibration tool, not a scorecard.

Work through these steps in order. Don't skip ahead.

---

### Step 1: Set the scene as a CS expert

Pick a Customer Service entity: Support Ticket, Escalation Case, Customer Complaint,
Refund Request, or SLA Contract.

As the CS expert, write:
- **What is this entity and why does it exist?** (one or two sentences)
- **What does reaching each major state mean to the customer?** (one sentence per state, plain English)
- **The one failure mode that most often generates re-open tickets or SLA breaches**

Then — before anything else — write down at least two invariants you expect this entity to enforce.
At least one must involve a time limit, a numeric count, or a threshold:

| # | Invariant | Numeric or temporal? | What breaks if violated |
|---|-----------|---------------------|------------------------|
| 1 | | Yes / No | |
| 2 | | Yes / No | |

If both rows say "No" in the numeric/temporal column: revise at least one before moving on.
This gate must close before you build any tables.

---

### Step 2: Build the machine — declare everything with IDs

Your discipline here: every state gets an S-ID, every operation an OP-ID, every invariant an INV-ID.
You'll need these IDs in every subsequent step. Using one without declaring it is a finding.

**States** — at least 5, including at least one terminal state:

| S-ID | Name | Entry Condition | Terminal? |
|------|------|-----------------|-----------|
| S-01 | | | |

Entry condition = what must be true about the entity to be in this state, not just how it got here.
"Ticket is assigned to an agent" is good. "System is online" is not.

**Operations** — at least 7, covering the full lifecycle:

| OP-ID | Name | Allowed From | Leads To | Guard | Actor |
|-------|------|-------------|---------|-------|-------|
| OP-01 | | | | | |

**Invariants** — fold in the two from Step 1 (assign INV-IDs), then add structural ones:

| INV-ID | Rule | When it applies (S-IDs) | What breaks if violated |
|--------|------|------------------------|------------------------|
| INV-01 | (from Step 1 row 1) | | |
| INV-02 | (from Step 1 row 2) | | |

---

### Step 3: Walk through the lifecycle

Trace at least 7 operations. At every step, write it like this:

**Step N — [OP-ID] [Operation name]**
Before: [S-ID], key field values
Preconditions (name the field and value — "preconditions met" doesn't count):
What happens:
After: [S-ID], key field values that changed
Postconditions:
Invariants in play: [INV-IDs] — each holds or fails

Include:
- At least one step that gets rejected: name exactly which precondition fails and what the system does
- At least one step that sets up a race: name the two operations that could collide and what state conflict results

---

### Step 4: Before the hunt — write your predictions

Look at your tables only. Not the trace.

| Type | Predict it's there? | Why? (from the tables alone) |
|------|--------------------|-----------------------------|
| Invalid transition | | |
| Missing precondition check | | |
| Invariant violation | | |
| Race condition | | |
| Undeclared ID reference | | |

---

### Step 5: Hunt — score each finding the moment you find it

Go through the trace type by type. For each one, ask the question, find the evidence,
then **score Strength before writing anything else**. Say it to yourself: "this is a 2 — reachable
in normal workflows." Then write it down.

- **Invalid transition**: did any step move between states without a valid OP-ID in the Allowed-From column?
- **Missing precondition check**: did any operation execute without evaluating a guard that exists in your tables?
- **Invariant violation**: after any step, does any INV-ID evaluate to false?
- **Race condition**: which pair of operations, if concurrent, would produce conflicting entity state?
- **Undeclared ID reference**: did any step or anomaly use an S-ID, OP-ID, or INV-ID not in the declaration tables?

Strength scale: 1 = edge case only | 2 = reachable in normal CS workflows | 3 = will cause silent SLA breach, wrong refund, or data corruption

Fill in one row at a time, scoring Strength as you go:

| Type | Found? | Count | Strength | Where (OP-ID + S-ID) | Predicted? |
|------|--------|-------|----------|---------------------|-----------|
| Invalid transition | | | | | |
| Missing precondition | | | | | |
| Invariant violation | | | | | |
| Race condition | | | | | |
| Undeclared ID reference | | | | | |

**Gate check**: you need at least 2 "Found" rows, and at least one at Strength 2 or higher.
If you don't have that, extend the trace — add operations that expose the missing types.

---

### Step 6: Register the anomalies

One row per finding. No blank cells — use "N/A: [reason]" when an ID doesn't apply.
Strength here must match Step 5. You are not allowed to revise it.

| A-ID | Type | OP-ID | S-ID | INV-ID | What breaks | Severity | Strength |
|------|------|-------|------|--------|------------|----------|---------|
| A-01 | | | | | | Low/Med/High/Critical | |

---

### Step 7: What surprised you?

Compare your Step 4 predictions to what you actually found.
Use three codes: C = called it right | FP = predicted it; wasn't there | FN = missed it; was there

| Type | Predicted | Found | Code | What the trace revealed that the tables hid — or vice versa |
|------|-----------|-------|------|--------------------------------------------------------------|
| Invalid transition | | | | |
| Missing precondition | | | | |
| Invariant violation | | | | |
| Race condition | | | | |
| Undeclared ID reference | | | | |

Calibration score: [C rows] / [rows where you made a prediction] x 100% = _____%
If below 60%: one sentence — what made the declaration tables misleading?
```

---

## V-04 — Axes: Role Sequence + Lifecycle Emphasis (Phase Gates with Hard Invariant Exit Criterion)

**Hypothesis**: Combining the role sequence (Finance Expert → Lifecycle Analyst → Anomaly Hunter) with explicit phase entry/exit criteria — where Phase 1 cannot close until the numeric/temporal invariant gate is satisfied — prevents the gate from being treated as optional boilerplate in the formalization stage. Phase gates also enforce that the Surprise column and score-at-point-of-discovery rule are exit conditions for Phase 4, not suggestions.

---

```markdown
You are running **trace-state** for a Finance domain entity.
This session has four phases. Each phase has an entry requirement and an exit gate.
Complete each phase before advancing. The exit gate is not satisfied by prose alone — check it.

Two non-negotiable constraints apply in every phase:
- **Numeric/temporal invariant gate**: Phase 1 cannot close until at least one invariant with a
  specific numeric threshold or deadline is declared with a falsification test.
- **Score at point of discovery**: Strength (1/2/3) must be written when each finding is first
  recorded in Phase 4. No retroactive revision is permitted.

Roles: Finance Domain Expert (Phase 1) | Lifecycle Analyst (Phases 2–3) | Anomaly Hunter (Phase 4)

---

## PHASE 1 — Domain Setup
**Role**: Finance Domain Expert
**Entry**: none
**Exit gate**: entity profile complete AND >= 1 numeric/temporal invariant declared with a
              falsification test naming a specific threshold or date constraint

### 1A — Entity Profile

Choose a Finance entity: Invoice, Expense Claim, Purchase Order, Journal Entry, Budget Allocation,
Vendor Payment.

- **Entity name**:
- **Business purpose** (one sentence):
- **Lifecycle in plain English** (ordered list of states — no IDs yet):
- **Who acts on it** (roles: AP clerk, approver, controller, system):
- **Primary failure mode**: the one thing that causes journal corrections or audit findings in practice

### 1B — Numeric/Temporal Invariant Pre-Declaration

| # | Invariant | Numeric / Temporal / Both | Falsification Test | Domain Consequence |
|---|-----------|--------------------------|-------------------|--------------------|
| 1 | | | e.g., "submit PO with amount > approved budget line — does system reject?" | |
| 2 | | | | |

**Phase 1 gate check**:
[ ] Entity profile includes >= 5 lifecycle states
[ ] At least one invariant in 1B has a non-blank Falsification Test referencing a specific
    threshold, percentage, count, or date constraint
[ ] Generic invariants ("amounts must be valid") are absent from 1B

Do not start Phase 2 until all three boxes can be checked.

---

## PHASE 2 — State Machine Declaration
**Role**: Lifecycle Analyst
**Entry**: Completed Phase 1 entity profile and 1B invariant table
**Exit gate**: three declaration tables populated; ID coverage check complete; at least one
              INV-ID traces directly to a Phase 1B row

### 2A — States

| S-ID | State Name | Entry Condition | Description | Terminal? |
|------|------------|-----------------|-------------|-----------|
| S-01 | | | | |

Minimum 5 states. Entry Condition = what must be true about the entity to be in this state.
"Data is valid" does not pass. "Amount field is non-null and > 0" passes.

### 2B — Operations

| OP-ID | Operation | Valid-From S-IDs | Produces S-ID | Actor | Guard |
|-------|-----------|-----------------|---------------|-------|-------|
| OP-01 | | | | | |

Minimum 7 operations. Guard = condition beyond state membership required to execute.

### 2C — Invariants

Assign INV-IDs to Phase 1B invariants first. Add structural invariants as needed.

| INV-ID | Invariant | Scope (S-IDs) | Source | Violation Consequence | Enforcement Mechanism |
|--------|-----------|--------------|--------|-----------------------|----------------------|
| INV-01 | (from 1B row 1) | | Expert | | |
| INV-02 | (from 1B row 2) | | Expert | | |

Minimum 3 invariants. At least one must trace to Phase 1B (Source = Expert).

### 2D — ID Coverage Check

List any S-ID, OP-ID, or INV-ID referenced in 2B/2C but not declared above:

| Reference | Type | Appears In | Action |
|-----------|------|------------|--------|
| (none) or [list] | | | Declare now / Flag as undeclared ID anomaly candidate |

**Phase 2 gate check**:
[ ] All three declaration tables have >= minimum rows
[ ] 2D table completed (even if result is "none")
[ ] At least one INV-ID in 2C has Source = Expert (traces to Phase 1B)

---

## PHASE 3 — Step-by-Step Trace
**Role**: Lifecycle Analyst
**Entry**: Completed Phase 2 tables
**Exit gate**: >= 7 numbered steps; negative path present; concurrent scenario setup present;
              no step references an undeclared S-ID, OP-ID, or INV-ID

Trace the entity lifecycle from initial state through resolution.

**Step N — [OP-ID]: [Operation Name]**
- **Before**: [S-ID] — [State Name] | [relevant field values]
- **Preconditions** (name the field and value):
- **Execution**:
- **After**: [S-ID] — [State Name] | [changed field values]
- **Postconditions**:
- **Invariants active**: [INV-IDs] — holds / violated
- **Guard evaluated**: [result]

Required trace types:
1. Happy path: >= 4 states traversed in sequence
2. Negative path: operation attempted from invalid state, precondition failure named,
   rejection behavior documented
3. Concurrent scenario: two operations that could interleave on the same entity,
   with the conflicting outcome described

**Phase 3 gate check**:
[ ] >= 7 numbered steps
[ ] Happy path, negative path, and concurrent scenario all present
[ ] No step uses an S-ID, OP-ID, or INV-ID not declared in Phase 2

---

## PHASE 4 — Anomaly Detection
**Role**: Anomaly Hunter
**Entry**: Completed Phases 1–3
**Exit gate**: quality gate passes; register has no blank cells in found rows;
              reconciliation Surprise column complete; Strength values match sweep table

### 4A — Pass 1: Hypothesis from Declaration Tables Only

*Scan Phase 1B and Phases 2A–2C. Do not re-read Phase 3.*

| Anomaly Type | Predicted | Confidence | Structural evidence |
|--------------|-----------|------------|---------------------|
| Invalid transition | Y/N | H/M/L | |
| Missing precondition check | Y/N | H/M/L | |
| Invariant violation | Y/N | H/M/L | |
| Race condition | Y/N | H/M/L | |
| Undeclared ID reference | Y/N | H/M/L | |

### 4B — Pass 2: Full Trace Sweep

*Now read Phase 3 in full. Score Strength at the moment you identify each finding — not afterward.*

**Strength**: 1 = edge case only | 2 = reachable in normal Finance workflows |
3 = will produce incorrect ledger state, duplicate payment, or audit failure

| Type | Found/None | Count | Strength | OP-ID | S-ID | INV-ID | Predicted? |
|------|-----------|-------|----------|-------|------|--------|-----------|
| Invalid transition | | | | | | N/A | |
| Missing precondition | | | | | | N/A | |
| Invariant violation | | | | | | | |
| Race condition | | | | | | N/A | |
| Undeclared ID reference | | | | | | N/A | |

**Quality gate** — three conditions, all must hold:
1. **Quantity**: >= 2 rows "Found"
2. **Quality**: >= 1 "Found" row with Strength >= 2
3. **ID discipline**: no blank cells in any "Found" row (use "N/A: [reason]" where not applicable)

If any condition fails: write a *Remediation note* naming the specific gap and what Phase 3
additions would close it. Do not advance to 4C until the gate passes or the remediation is written.

### 4C — Reconciliation

| Type | Pass 1 Predicted | Pass 2 Found | Match? | Surprise | Surprise Explanation |
|------|-----------------|-------------|--------|----------|---------------------|
| Invalid transition | | | Y/N | Expected / Surprising | |
| Missing precondition | | | Y/N | Expected / Surprising | |
| Invariant violation | | | Y/N | Expected / Surprising | |
| Race condition | | | Y/N | Expected / Surprising | |
| Undeclared ID reference | | | Y/N | Expected / Surprising | |

*Surprise = Expected*: the trace confirmed what the declaration tables implied.
*Surprise = Surprising*: the trace contradicted the prediction in either direction.

### 4D — Anomaly Register

| A-ID | Type | OP-ID | S-ID | INV-ID | Description | Severity | Strength | Reachability |
|------|------|-------|------|--------|-------------|----------|---------|--------------|
| A-01 | | | | | | | | |

*Strength must match Phase 4B — no revision.*
*Reachability*: shortest OP-ID sequence from initial state that triggers this anomaly.
*Severity*: Low / Medium / High / Critical.

**Phase 4 gate check**:
[ ] Quality gate passes (or Remediation note written)
[ ] No blank cells in any found-verdict row in the register
[ ] Surprise column complete in 4C
[ ] Strength values in register match Phase 4B sweep table
```

---

## V-05 — Axes: Inertia Framing + Output Format (Documentation-vs-Trace with Calibration Report)

**Hypothesis**: Combining the documentation-vs-trace framing with a structured Calibration Report — using the C/FP/FN taxonomy and a numeric calibration score — activates two independent gap-detection modes simultaneously. The structural mode asks "where does the trace diverge from what the documentation claims?" The predictive mode asks "how accurately did the documentation-derived predictions forecast what the trace would reveal?" Low calibration scores expose documentation that is not just wrong but actively misleading.

---

```markdown
You are running **trace-state** for a Sales domain entity.
Framing: you are auditing a state machine that exists in a production system. The system has
documentation. The documentation makes claims. Your job is to compile the trace and build a
Calibration Report showing where the documentation's predictions held and where they failed.

Three structural constraints:
1. **Numeric/temporal invariant gate**: before compiling the trace, the documentation must declare
   at least one invariant referencing a specific numeric threshold or deadline. Documentation that
   only says "amounts must be valid" is incomplete — flag it and add one before continuing.
2. **Score at point of discovery**: assign Strength to each anomaly the moment you identify it.
   The Calibration Report depends on scores that reflect first-contact reasoning, not post-hoc review.
3. **Surprise taxonomy**: the reconciliation table uses C/FP/FN codes. A calibration score below
   60% signals that the documentation is structurally misleading, not just incomplete.

---

## Part 1 — What the Documentation Claims

**[Sales Domain Expert]**

Pick a Sales entity: Deal, Quote, Sales Order, Compensation Plan, or Discount Approval.

Write the documentation voice — how the system is supposed to work, as if written for a new
Sales engineer:

**Documented states** (plain English, ordered list — no IDs yet):

**Documented operations** (what the system allows and who can trigger each):

**Documented invariants** — at least three rules the system is supposed to enforce.
At least one must constrain a numeric threshold or temporal deadline:
1.
2.
3.

**Documented edge cases** (exceptions the documentation acknowledges):

**Numeric/temporal invariant gate check**:
Review the invariant list. If none reference a specific numeric cap, percentage, dollar amount,
or date constraint, add one here before continuing:
___ [add invariant or write "gate satisfied by invariant N above"]

---

## Part 2 — State Machine Formalization

**[Lifecycle Analyst]**

Formalize the documentation claims with full ID discipline.

### 2A — States

| S-ID | State Name | Entry Condition | Doc Reference | Terminal? |
|------|------------|-----------------|---------------|-----------|
| S-01 | | | (quote/paraphrase the Part 1 text implying this state) | |

*Undocumented state*: any state you declare with no Doc Reference is undocumented behavior — flag it.

### 2B — Operations

| OP-ID | Operation | Valid-From S-IDs | Produces S-ID | Guard | Doc Reference |
|-------|-----------|-----------------|---------------|-------|---------------|
| OP-01 | | | | | |

*Any operation with no Doc Reference is undocumented behavior — note it.*

### 2C — Invariants

| INV-ID | Invariant | Scope (S-IDs) | Doc Reference | Numeric/Temporal? | Enforcement Mechanism (per Doc) |
|--------|-----------|--------------|---------------|------------------|--------------------------------|
| INV-01 | | | | Y/N | (what doc says prevents violation, or "Silent" if doc is silent on enforcement) |

*At least one INV-ID must map to the numeric/temporal invariant from Part 1.*
*"Silent" enforcement = doc claims the invariant holds but does not explain how — that silence is a finding.*

### 2D — Documentation Coverage Pre-Audit

Before compiling the trace, note any gaps already visible:

| Gap Type | Description | Part 1 Reference |
|----------|-------------|-----------------|
| Undocumented state | | |
| Undocumented operation | | |
| Silent enforcement | | |

*(Leave rows blank if not applicable — do not delete them.)*

---

## Part 3 — Pre-Sweep Hypothesis

*Reading only Parts 1 and 2 — not the trace you are about to compile.*

For each anomaly type: what does the documentation imply should or should not be present?

| Anomaly Type | Documentation Implies | Your Prediction | Confidence |
|--------------|----------------------|----------------|-----------|
| Invalid transition | | Y/N | H/M/L |
| Missing precondition check | | Y/N | H/M/L |
| Invariant violation | | Y/N | H/M/L |
| Race condition | | Y/N | H/M/L |
| Undeclared ID reference | | Y/N | H/M/L |

---

## Part 4 — The Trace

**[Lifecycle Analyst]**

Compile the actual trace. For each step show both voices. Assign Strength immediately when you
identify any discrepancy — do not wait until Part 5.

**Step N — [OP-ID]: [Operation Name]**

| | Documentation Claims | Trace Shows |
|-|---------------------|-------------|
| **Before state** | [valid prior state per doc] | [S-ID and field values] |
| **Preconditions** | [what doc says must hold] | [what trace actually checks — or fails to check] |
| **After state** | [result per doc] | [S-ID and field values] |
| **Invariants** | [INV-IDs doc says are enforced] | [which actually hold, which do not] |
| **Gap** | — | [discrepancy between columns, or "none"] |

Minimum 7 steps. Required:
- One happy path step: documentation and trace agree, Gap = "none"
- One negative path step: documentation claims rejection occurs — confirm whether trace does too
- One invariant-gap step: documentation claims enforcement; trace reveals the enforcement is silent
  or absent (or vice versa)

---

## Part 5 — Anomaly Sweep

*Read Part 4 in full. Score Strength at point of discovery — not afterward.*

**Strength**:
- **1** — Gap exists but academic: adversarial input or highly unlikely concurrency required
- **2** — Gap reachable: a Sales rep following normal process would trigger this
- **3** — Gap critical: incorrect commissions, lost deal records, or audit failures

| Type | Found/None | Count | Strength | OP-ID | S-ID | INV-ID | Gap Step Ref | Predicted? |
|------|-----------|-------|----------|-------|------|--------|-------------|-----------|
| Invalid transition | | | | | | N/A | Step N | |
| Missing precondition | | | | | | N/A | Step N | |
| Invariant violation | | | | | | | Step N | |
| Race condition | | | | | | N/A | Step N | |
| Undeclared ID reference | | | | | | N/A | — | |

**Quality gate**: PASS requires >= 2 "Found" rows AND >= 1 with Strength >= 2.
If gate fails: name which documentation claim was too optimistic and what additional operation
would surface the missing anomaly type.

---

## Part 6 — Anomaly Register

| A-ID | Type | OP-ID | S-ID | INV-ID | Documentation Claim | What Trace Found | Delta | Severity | Strength |
|------|------|-------|------|--------|---------------------|-----------------|-------|----------|---------|
| A-01 | | | | | | | (gap between claim and finding, one sentence) | | |

*Strength must match Part 5 — no revision permitted.*
*Severity from the Sales team's perspective (wrong commission = Critical; cosmetic label mismatch = Low).*

---

## Part 7 — Calibration Report

### 7A — Reconciliation with Surprise Taxonomy

| Type | Part 3 Prediction | Part 5 Finding | Match? | Surprise Code | What the documentation hid — or correctly predicted |
|------|------------------|----------------|--------|---------------|-----------------------------------------------------|
| Invalid transition | | | Y/N | C / FP / FN | |
| Missing precondition | | | Y/N | C / FP / FN | |
| Invariant violation | | | Y/N | C / FP / FN | |
| Race condition | | | Y/N | C / FP / FN | |
| Undeclared ID reference | | | Y/N | C / FP / FN | |

**C** = Calibrated (predicted correctly) | **FP** = False Positive (predicted; not found) |
**FN** = False Negative (not predicted; found)

**Calibration score**: [# of C rows] / 5 x 100% = _____%

If calibration score is below 60%: write one sentence identifying which documentation property
(overly optimistic invariant claims, missing operation coverage, or silent enforcement) produced
the most FP or FN predictions.

### 7B — Documentation Verdict

Write two to three sentences telling the documentation author what must be updated.
Specifically address the numeric/temporal invariant gate: did the documentation's claimed
enforcement mechanism hold up in the trace? If "Silent" appeared in any INV-ID enforcement cell,
name the concrete enforcement mechanism that must be added.

**Closing note (Documentation Voice)**:
```

---

## Summary Table

| Variation | Primary Axis | Secondary Axis | Domain | Key Structural Bet |
|-----------|-------------|----------------|--------|-------------------|
| V-01 | Role sequence (numeric invariant gate in Expert role) | — | Sales | Gate in Expert role produces stronger INV-IDs than analyst self-generation during formalization |
| V-02 | Output format (three-value surprise taxonomy + calibration score) | — | Finance | FP/FN/C taxonomy + numeric calibration score produces richer signal than binary expected/surprising |
| V-03 | Phrasing register (conversational / score-aloud protocol) | — | Customer Service | Verbal checkpoint at point of discovery prevents retroactive score revision more reliably than tabular format |
| V-04 | Role sequence | Lifecycle emphasis (phase gates with hard invariant exit criterion) | Finance | Phase exit gates prevent numeric invariant gate and Surprise column from being treated as optional boilerplate |
| V-05 | Inertia framing (doc-vs-trace) | Output format (Calibration Report with FP/FN/C taxonomy) | Sales | Two simultaneous gap-detection modes (structural + predictive) expose documentation that is actively misleading, not just incomplete |
