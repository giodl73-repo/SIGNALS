## trace-state — V-01 through V-05

---

## V-01: Output Format axis
**Hypothesis**: A schema-first format with criterion IDs embedded in column headers, a filled example row using placeholder syntax, and a declared hard no-prose rule will structurally enforce C-14/C-15/C-16 and make rubric compliance unavoidable at write time.

```
You are a state-transition analyst. Your domain expert is a **Finance Controller**
(accounts receivable, approval workflows, ledger state).

Your task: hand-compile state transitions for the feature described below, producing
a complete trace artifact. Every section must use the locked table format. Prose
substitutions are forbidden — if a cell cannot be filled, write "N/A" or "none", not
a sentence.

**HARD RULE — NO PROSE SUBSTITUTIONS**: Every field must be filled using the column
schema. Narrative paragraphs, bullet summaries, or free-form prose may not substitute
for any table cell. Violation of this rule invalidates the artifact.

---

## Feature
{{topic}}

{{spec}}

---

## Section 1 — Transition Trace [C-01 | C-02 | C-06]

Use this exact schema. The example row shows placeholder syntax.

| C-01a: Starting State | C-01b: Operation | C-01c: Ending State | C-02a: Preconditions [C-02] | C-02b: Postconditions [C-02] |
|-----------------------|-----------------|---------------------|---------------------------|------------------------------|
| Invoice.DRAFT | SubmitForApproval(invoiceId) | Invoice.PENDING_APPROVAL | balance > 0; approver exists | approval_queue contains invoiceId |
| … | … | … | … | … |

Fill a minimum of 5 rows covering the main lifecycle path. Omit no column.

---

## Section 2 — Invariant Register [C-03 | C-07]

Declare at least two domain-meaningful invariants. Each must encode a real Finance
business rule (not a generic structural rule like "ID is not null").

| Invariant ID | Rule [C-07] | Checked After Operation(s) [C-03] | Derivation Source Row [C-13] |
|--------------|-------------|----------------------------------|------------------------------|
| INV-01 | … | … | Row N from Section 1 |
| INV-02 | … | … | Row N from Section 1 |

**C-13 requirement**: the Derivation Source Row column must name a specific row from
Section 1. Declaring an invariant with no trace linkage does not satisfy C-13.

---

## Section 3 — Defect Register [C-04]

At least one defect must be named with all four fields.

| Defect ID | Type | Triggering Operation [C-04] | Reason |
|-----------|----|----------------------------|--------|
| D-01 | missing_precondition_check | … | … |

Defect types: invalid_transition / missing_precondition / invariant_violation / race_condition

---

## Section 4 — Negative Path [C-09]

One rejected operation. All four elements required.

| Invalid Starting State | Blocked Operation | Unchanged State (confirmed) | Named Error |
|------------------------|------------------|-----------------------------|-------------|
| … | … | … | … |

---

## Section 5 — Race Condition Analysis [C-08 | C-12]

One concurrent operation pair. Describe **both orderings** explicitly.

| Ordering | Thread A | Thread B | Conflict or Resolution |
|----------|----------|----------|------------------------|
| A before B | … | … | … |
| B before A | … | … | … |

"The reverse is symmetric" does not satisfy C-12. Both orderings must be written out.

---

## Section 6 — Omitted Transitions [C-10]

List every transition in the state space that does not appear in Section 1.
Silent omissions do not qualify. Each must carry a rationale.

| Omitted Transition | Rationale for Omission |
|--------------------|------------------------|
| … | out of scope for this feature / invalid by invariant / deferred to Wave 2 |

---

**Reminder**: No prose substitutions anywhere in this document. Every field must be
filled using the column schema above. [C-16]
```

---

## V-02: Role Sequence axis
**Hypothesis**: Leading with Finance (most invariant-dense domain) before Sales and CS
forces richer precondition declarations early and produces more non-trivial invariants
(C-07) than role-agnostic or Sales-first ordering.

```
You are a state-transition analyst working with three domain experts in sequence.
Run each expert pass completely before moving to the next.

**Expert sequence**:
1. Finance Controller — approval workflows, ledger state, payment lifecycles
2. Sales Operations Manager — opportunity pipeline, quote-to-order, forecast state
3. Customer Service Lead — case lifecycle, escalation chains, SLA state

Each expert contributes their section independently. Do not merge or average; surface
disagreements as findings.

---

## Feature
{{topic}}

{{spec}}

---

## Pass 1: Finance Controller

### 1A — Transition Trace
For each operation in scope: starting state → operation → ending state.
Format: numbered steps, one per operation.

Step 1: State=[…] | Op=[…] | EndState=[…]
  Preconditions: …
  Postconditions: …

(minimum 5 steps)

### 1B — Invariants
At least two invariants that reflect Finance business rules.
Invariant must name which step(s) it is checked after.

INV-F-01: [rule] — checked after steps: …
INV-F-02: [rule] — checked after steps: …

### 1C — Defects Found
At least one defect from Finance perspective.
Format: [type] at [step] — [reason]

---

## Pass 2: Sales Operations Manager

### 2A — Transition Trace
Same format as Pass 1. Cover the Sales-specific state lifecycle.

### 2B — Invariants
At least two invariants reflecting Sales pipeline rules.

### 2C — Defects Found + Cross-Domain Conflicts
Name any state assumption in Pass 1 that conflicts with Sales state model.

---

## Pass 3: Customer Service Lead

### 3A — Transition Trace
Same format. Cover CS case/ticket lifecycle.

### 3B — Invariants
At least two invariants reflecting SLA or escalation rules.

### 3C — Defects Found + Cross-Domain Conflicts
Name any conflict with Pass 1 or Pass 2 findings.

---

## Synthesis

### Race Condition Analysis
Using findings from all three passes, identify one concurrent operation pair where
state contention is possible. Describe both orderings:

- A before B: [what happens]
- B before A: [what happens]

### Consolidated Defect Register
One row per defect across all passes.

| ID | Type | Triggering Operation | Domain | Reason |
|----|------|---------------------|--------|--------|
| D-01 | … | … | Finance / Sales / CS | … |

### Omitted Transitions
Every transition visible in the domain model but absent from the traces above.
Each omission must carry a rationale.

| Transition | Domain | Rationale |
|-----------|--------|-----------|
| … | … | … |
```

---

## V-03: Lifecycle Emphasis axis
**Hypothesis**: Allocating explicit, bounded phase sections (preconditions-first, then
state body, then invariant check, then defect review, then race) with minimum-item
requirements per phase produces balanced coverage across all essential criteria without
any phase being skipped.

```
You are a state-transition analyst. Domain: Sales, Customer Service, or Finance —
choose the domain that best matches the feature.

Work through exactly five phases in order. Do not skip a phase or merge phases.

---

## Feature
{{topic}}

{{spec}}

---

## Phase 1 — Precondition Inventory (complete before writing any transitions)

List every precondition that must hold before any operation in scope can execute.
At least 4 preconditions. For each:

- PC-01: [condition] — applies to operation(s): …
- PC-02: [condition] — applies to operation(s): …
- PC-03: [condition] — applies to operation(s): …
- PC-04: [condition] — applies to operation(s): …

If a precondition cannot be named, write "none" explicitly — do not leave blank.

---

## Phase 2 — Transition Body

For each operation, produce one block. Reference the preconditions from Phase 1 by ID.

**Operation: [name]**
- Starting State: …
- Preconditions: [PC-XX, PC-XX or "none"]
- State Changes: …
- Ending State: …
- Postconditions: …

Minimum 5 operations. Every block must be complete; partial blocks are not acceptable.

---

## Phase 3 — Invariant Check

Declare at least two domain invariants. Each must:
1. Encode a real business rule (not a structural identity like "ID is non-null")
2. Name every operation from Phase 2 after which it is checked
3. Trace back to a Phase 2 block as its derivation source

INV-01: [rule]
  Checked after: [Op names]
  Derived from: [Op name] — [brief linkage note]

INV-02: [rule]
  Checked after: [Op names]
  Derived from: [Op name] — [brief linkage note]

---

## Phase 4 — Defect Analysis

Review Phase 2 and Phase 3 for:
- Operations that begin without checking required preconditions
- Transitions that violate declared invariants
- Missing or incorrect postcondition declarations

Report at minimum one defect:

D-01: Type=[invalid_transition|missing_precondition|invariant_violation|race_condition]
  Triggering operation: …
  Reason: …

Then: one negative path example showing a rejected operation.
  Attempted state: … | Blocked op: … | State after rejection: … | Error: …

---

## Phase 5 — Concurrency Review

Identify one pair of operations that could execute concurrently and produce a conflict.

Describe both orderings:

Ordering A→B:
  Thread A executes [Op]: state becomes …
  Thread B then executes [Op]: result is …
  Conflict: …

Ordering B→A:
  Thread B executes [Op]: state becomes …
  Thread A then executes [Op]: result is …
  Conflict: …

Then list every transition in the domain model that does NOT appear in Phase 2,
with rationale for each omission.
```

---

## V-04: Combined — Phrasing Register + Role Sequence (conversational + CS-first)
**Hypothesis**: A conversational register with a named persona narrator leading from
Customer Service surface the most realistic SLA and escalation invariants, producing
more domain-plausible outputs (C-05) and more non-trivial invariants (C-07) than
technical/formal phrasing.

```
Walk me through the state lifecycle for this feature as if you're a **Customer Service
Lead** who's been burned by bad state transitions in production. You know what goes
wrong when cases get stuck, when SLA timers keep running after resolution, when an
escalation undoes a closure. You've seen it.

After the CS walkthrough, hand off to a **Sales Operations Manager** who traces the
same feature from the pipeline side, then a **Finance Controller** who closes the loop
on payment and approval state.

Be specific. Use real domain terms. If a precondition isn't checked in the code, say so.

---

## Feature
{{topic}}

{{spec}}

---

## CS Lead Walkthrough

Start at the beginning: what state is a record in when this feature first touches it?
Walk every operation from there to closure. For each step, tell me:

- What state you're starting from
- What operation fires
- What state you land in
- What has to be true before the operation can run (preconditions — say "none" if clean)
- What's guaranteed true after it runs (postconditions)

Then tell me: what are the two most important rules that must hold throughout this
entire flow? These should be CS business rules — things like "a case can't be closed
while an SLA breach is open" or "escalation level can only increase, not skip."

Name at least one place where you've seen or can imagine the system breaking these
rules. What operation triggers it? Why does it break?

---

## Sales Ops Walkthrough

Same exercise from the Sales side. What does the pipeline state look like?
Where does this feature touch opportunities, quotes, or orders?

Walk the transitions, name the preconditions and postconditions, declare two
Sales-specific invariants.

Then: does anything the CS lead said conflict with what Sales expects? If so, name it.

---

## Finance Controller Walkthrough

Close the loop. What's the Finance state model — invoices, approvals, ledger entries?

Same format: transitions, preconditions, postconditions, two invariants.

Any conflicts with CS or Sales state assumptions?

---

## Race Condition Check

Across the three walkthroughs, name one operation pair that could collide if two users
hit it at the same time. Walk me through what happens if A goes first, then B — and
what happens if B goes first, then A. Both orderings, explicitly.

---

## Summary

Pull together:
1. Full defect list (type, operation, reason) — at least one entry
2. One rejected operation (invalid state, blocked op, state unchanged, named error)
3. All transitions you deliberately left out and why (no silent omissions)
```

---

## V-05: Combined — Inertia Framing + Output Format (failure-mode-first + locked schema)
**Hypothesis**: Opening with the explicit failure mode ("you will produce prose summaries
that look like analysis but satisfy no criterion") before presenting the locked schema
produces the highest C-16 pass rate and reduces criterion-evading narrative fallback.

```
## Warning: The Default Failure Mode

Without explicit constraints, state-transition analysis artifacts drift toward prose:
paragraphs that describe what transitions "generally" look like, bullet summaries of
"key invariants," narrative defect write-ups. These outputs feel complete but satisfy
no specific criterion. They cannot be scored. They are not artifacts.

This prompt locks you to a schema. Every field has a column. Every column has a
criterion ID. If you fill the column, you satisfy the criterion. If you write prose
instead of filling the column, you have failed the criterion, regardless of how
accurate the prose is.

**Declared hard rule: no prose substitutions.** If a cell cannot be filled, write
"none" or "N/A". Do not write a sentence where a value belongs.

---

## Feature
{{topic}}

{{spec}}

## Domain
Choose the role that best fits: Sales Operations / Customer Service / Finance.
State your choice in one line before the tables.

**Domain expert chosen**: …

---

## Table 1 — Transition Trace

Schema (do not alter column names or order):

| C-01a Starting State | C-01b Operation | C-01c Ending State | C-02a Preconditions | C-02b Postconditions |
|---------------------|-----------------|--------------------|--------------------|--------------------|
| [domain state name] | [operation name with args] | [domain state name] | [condition or "none"] | [condition or "none"] |
| … | … | … | … | … |

Requirements:
- Minimum 5 rows
- State names must be domain terms (C-05), not generic labels like "state_a"
- Every column filled; blank cells invalid [C-16]

---

## Table 2 — Invariant Register

| INV ID | Business Rule [C-07] | Checked After Operations [C-03] | Trace Row Reference [C-13] |
|--------|---------------------|-------------------------------|--------------------------|
| INV-01 | [domain business rule — not a structural identity] | [list op names] | [Table 1 row number] |
| INV-02 | … | … | … |

Requirements:
- Minimum 2 rows
- Trace Row Reference must point to a specific Table 1 row (e.g., "Row 3")
- Generic structural rules ("ID is not null") do not satisfy C-07

---

## Table 3 — Defect Register

| D ID | Type | Triggering Operation [C-04] | Reason |
|------|------|-----------------------------|--------|
| D-01 | [invalid_transition / missing_precondition / invariant_violation / race_condition] | [operation name] | [why this is a defect] |

Minimum 1 row. All four columns required.

---

## Table 4 — Negative Path

One rejected operation. All four cells required.

| Invalid Starting State [C-09] | Blocked Operation | State After Rejection (unchanged) | Named Error |
|------------------------------|------------------|----------------------------------|-------------|
| … | … | … | … |

---

## Table 5 — Race Condition

Both orderings required [C-12]. "See above" or "symmetric to A→B" does not satisfy.

| Ordering | Thread A Operation | Thread B Operation | Conflict or Resolution |
|----------|-------------------|--------------------|------------------------|
| A before B | … | … | … |
| B before A | … | … | … |

---

## Table 6 — Omitted Transitions [C-10]

Every transition in the domain state space not present in Table 1.
Silent omissions (transitions present in the domain but absent from the document
without explanation) invalidate C-10.

| Omitted Transition | Rationale |
|-------------------|-----------|
| … | [out of scope / invalid by invariant / deferred / unreachable] |

---

**Final reminder**: Tables only. No prose between tables except the domain expert
declaration line. [C-16 enforced throughout]
```

---

### Axis Summary

| Variation | Primary Axis | Secondary Axis | Key Hypothesis |
|-----------|-------------|---------------|----------------|
| V-01 | Output format | — | Schema-embedded criterion IDs make C-14/C-15/C-16 structurally unavoidable |
| V-02 | Role sequence | — | Finance-first ordering produces richer invariants (C-07) and more defects (C-04) |
| V-03 | Lifecycle emphasis | — | Bounded phases with minimum-item gates prevent criterion-skipping |
| V-04 | Phrasing register | Role sequence (CS-first) | Conversational + CS-first produces highest C-05/C-07 domain accuracy |
| V-05 | Inertia framing | Output format (locked schema) | Naming the failure mode first produces highest C-16 pass rate |
