## trace-state — Round 10 Variations (V-01 through V-05)

---

### V-01 — **Variation axis: Role sequence (Finance → Sales → CS)**
**Hypothesis:** Leading with Finance — where invariants carry regulatory weight — calibrates the model toward domain-meaningful business rules before entering operationally looser domains; the Finance invariant bar propagates forward.

---

You are a state-domain expert in Finance, Sales, and Customer Service. Hand-compile state transition traces for a software feature under evaluation. Execute three domain passes in this order: **Finance first, Sales second, Customer Service third.**

---

## Output Format

Each domain pass produces four sections. The Invariant Register is produced once, after all three passes.

---

### Section 1 — State Transition Table (minimum 5 rows per pass)

| Step | Starting State | Operation | Preconditions [write `none` if genuinely absent] | Postconditions [write `none` if genuinely absent] | Ending State | Invariants Checked |
|------|---------------|-----------|--------------------------------------------------|---------------------------------------------------|--------------|-------------------|

**Invariant rules:**
- Declare at least 2 domain-meaningful invariants per pass. Check them after every operation.
- Invariants must encode real business rules. Disqualified patterns: `"ID is not null"`, `"record exists"`, `"amount field is populated"`. A qualifying example: `"Invoice total must equal the sum of approved line items after any line-item modification"`.
- Entries matching any disqualified pattern invalidate the invariant section.

---

### Section 2 — Defect Log (at least 1 per pass)

- **Defect type:**
- **Triggering operation:**
- **Reason:**

---

### Section 3 — Race Condition Analysis

Identify one concurrent operation pair per pass.

**Operations: [Op A name] and [Op B name]**

Name both operations explicitly. Naming only the conflict outcome or only one operation does not satisfy this section.

- **Ordering 1 — [Op A] executes before [Op B]:** Describe the full interleaving — what state each operation reads, what conflict arises or how it resolves.
- **Ordering 2 — [Op B] executes before [Op A]:** Describe this ordering fully and independently. Do not write "same as above," "symmetric," or any cross-reference to Ordering 1. Each ordering must stand on its own.

---

### Section 4 — Negative Path Trace (one per pass)

| Invalid Starting State | Blocked Operation | Unchanged State | Named Error |
|------------------------|------------------|-----------------|------------|

After completing this row: **confirm no mutation occurred** — actively verify the system state after the rejected operation is identical to the starting state. Recording the pre-operation state as a passive column value does not satisfy this requirement; the verification must be explicitly noted.

---

### Section 5 — Invariant Register (produced once, after all three passes)

| Invariant | Domain | Derived From (Pass + Step) |
|-----------|--------|---------------------------|

Cross-domain invariants that hold across two or more passes must list all source derivations.

---

## Pass 1 — Finance

Operate as a Finance domain expert. Trace state transitions in financial workflows: invoice lifecycle, payment processing, budget approval routing, reconciliation cycles, approver assignment. Apply Sections 1–4 above.

## Pass 2 — Sales

Operate as a Sales domain expert. Trace state transitions in sales workflows: lead qualification, opportunity stages, quote issuance, order fulfillment, contract execution. Apply Sections 1–4 above.

## Pass 3 — Customer Service

Operate as a Customer Service domain expert. Trace state transitions in CS workflows: ticket creation, escalation, SLA expiration, resolution, closure, reopening. Apply Sections 1–4 above.

After Pass 3, produce Section 5 (Invariant Register).

---

**No prose substitutions.** Every output element must appear in the schema slots defined above. Prose narrative in place of structured fields invalidates the artifact.

Minimum 5 rows per pass. Minimum 15 state transition rows total across all three passes.

---
---

### V-02 — **Variation axis: Output format (criterion IDs embedded as field-label annotations)**
**Hypothesis:** Embedding rubric criterion IDs directly in column headers and field labels makes compliance structurally unavoidable — filling any cell mechanically satisfies the associated criterion without requiring cross-referencing.

---

You are a state-domain expert in Sales, Customer Service, and Finance. Hand-compile state transition traces for a software feature. Run all three domain passes.

The output schema below annotates each field with the criterion it satisfies. Filling a cell satisfies the criterion; no cross-referencing required.

---

## State Transition Table [C-01: starting state → operation → ending state] [C-06: uniform format throughout]

Minimum 5 rows per pass. Minimum 15 rows total across all passes.

| Step | Starting State [C-01a] | Operation [C-01b] | Preconditions [C-02a] [write `none` if genuinely absent] | Postconditions [C-02b] [write `none` if genuinely absent] | Ending State [C-01c] | Invariants Checked [C-03: minimum 2 per pass — never skip] |
|------|----------------------|-------------------|---------------------------------------------------------|---------------------------------------------------------|----------------------|-------------------------------------------------------------|

**Invariant constraint [C-03, C-07]:** Each invariant must encode a business rule. Disqualified patterns [C-18, C-27]: `"ID is not null"`, `"record exists"`, `"amount field is populated"`. A qualifying example [C-20]: `"Approved invoice amount must match the submitted amount after any approval decision"`. Entries matching any disqualified pattern invalidate the invariant section [C-23: section-level invalidation].

---

## Defect Log [C-04: labeled defect — type + triggering operation + reason]

At least 1 per pass:

- **Defect type [C-04a]:**
- **Triggering operation [C-04b]:**
- **Reason [C-04c]:**

---

## Race Condition Analysis [C-08: concurrent interleaving] [C-12: both orderings] [C-28: both operations named]

For each pass, identify one concurrent operation pair.

**Operations [C-28]: [Op A name] and [Op B name]**

- **Ordering 1 — [Op A] before [Op B] [C-12a]:** Describe the full interleaving — what state each operation reads, the conflict or resolution outcome.
- **Ordering 2 — [Op B] before [Op A] [C-12b]:** Describe this ordering fully and independently [C-21: anti-lazy-copy constraint — do not write "same as above" or reference Ordering 1; each ordering must stand alone].

---

## Negative Path Trace [C-09: all four elements] [C-29: active mutation verification]

| Invalid Starting State [C-09a] | Blocked Operation [C-09b] | Unchanged State [C-09c] | Named Error [C-09d] |
|-------------------------------|--------------------------|------------------------|-------------------|

After completing this row: **confirm no mutation occurred [C-29]** — actively verify the post-rejection state equals the starting state. Passive column recording does not satisfy C-29; the verification must be an explicit act noted in the trace.

---

## Invariant Register [C-25: cross-pass aggregation with derivation linkage] [C-26: aggregate floor ≥ 15 rows total]

Produce after all three passes.

| Invariant | Domain | Derived From (Pass + Step Ref) |
|-----------|--------|-------------------------------|

Cross-domain invariants must list all source derivations. The aggregate trace floor (15 rows total) must be met before this section is complete.

---

## Domain Passes

Run in this order: **Sales → Customer Service → Finance.** Apply the full schema above to each pass.

- **Sales:** Leads, opportunities, quotes, orders, contracts.
- **Customer Service:** Tickets, escalations, SLA tracking, resolutions, closures.
- **Finance:** Invoices, payments, approvals, reconciliations, budget allocations.

---

**No prose substitutions [C-16].** Narrative in place of structured fields invalidates the artifact [C-19]. Minimum 5 rows per pass. Minimum 15 rows total [C-17, C-26].

---
---

### V-03 — **Variation axis: Phrasing register (conversational imperative, second-person throughout)**
**Hypothesis:** Direct "you will" framing eliminates hedge language and reduces passive-structure drift; compliance rates for section-level requirements improve when instructions read as commands rather than specifications.

---

You are a domain expert in Sales, Customer Service, and Finance. Your task is to hand-compile state transition traces.

Here is exactly what you will produce.

---

**Run three domain passes — Sales first, then Customer Service, then Finance.**

For each pass, you will build four things: a state transition table, a defect entry, a race condition analysis, and a negative path trace. After all three passes, you will produce one consolidated invariant register.

---

### What to put in the state transition table

Give me at least 5 rows per pass — that's 15 rows minimum across all three passes.

| Step | Starting State | Operation | Preconditions | Postconditions | Ending State | Invariants Checked |
|------|---------------|-----------|---------------|----------------|--------------|-------------------|

For Preconditions and Postconditions: if there are none, write `none` — do not leave the cell blank or skip it.

For Invariants: you must declare at least 2 per pass and check them after every single operation. Make them real business rules — things that encode actual domain logic, like "A closed ticket cannot transition to In Progress without first going through Reopened" or "A payment cannot be applied to a cancelled invoice." Do not use generic structural rules like `"ID is not null"`, `"record exists"`, or `"amount field is populated"` — those invalidate your invariant section.

---

### What to put in the defect log

Find at least one defect per pass and label it:
- Defect type:
- Triggering operation:
- Reason:

---

### What to put in the race condition section

Pick two operations that could run concurrently in the domain. Name both of them:

**Operations: [Op A name] and [Op B name]**

Then describe two orderings:
1. What happens when Op A runs first, then Op B — full interleaving, what each operation sees, conflict or resolution named
2. What happens when Op B runs first, then Op A — write this out fully and independently, from scratch; do not write "same as above," "see above," or any reference back to Ordering 1

Both orderings must be complete and self-contained.

---

### What to put in the negative path trace

Show one rejected operation per pass:

| Invalid Starting State | Blocked Operation | Unchanged State | Named Error |
|------------------------|------------------|-----------------|------------|

After you fill this in, do one more thing: **confirm no mutation occurred.** Don't just record the pre-operation state in the column — actively verify the state after rejection is the same as before, and note that verification explicitly. Passive column recording is not sufficient.

---

### What to put in the invariant register

After all three passes, collect every invariant you declared and put them in one table:

| Invariant | Domain | Derived From (Pass + Row) |
|-----------|--------|--------------------------|

If an invariant applies across more than one domain, list every source row.

---

**Domain coverage:**
- Sales: leads, opportunities, quotes, orders, contracts
- Customer Service: tickets, escalations, SLA tracking, resolutions, closures
- Finance: invoices, payments, approvals, reconciliations, budget allocations

Every element belongs in a schema slot. Do not use prose in place of table fields — that invalidates the artifact.

Minimum 5 rows per pass. Minimum 15 rows total.

---
---

### V-04 — **Variation axes (combined): Role sequence (CS → Sales → Finance) + Lifecycle emphasis (explicit numbered phase markers with handoff gates)**
**Hypothesis:** CS-first warm-up establishes narrative variety before Finance's rigor closes the trace; explicit phase gates prevent schema drift across passes and make multi-pass completeness auditable at the phase boundary rather than only at the end.

---

You are a state-domain expert conducting a structured state transition audit across three business domains. Execute three domain passes in strict order: **Customer Service first, Sales second, Finance third.** Each phase must be complete before the next begins.

---

## Phase 0 — Audit Setup

Before beginning any pass, declare:
1. The software feature under evaluation
2. The primary state object for each domain (e.g., "Ticket" for CS, "Opportunity" for Sales, "Invoice" for Finance)

This anchors domain plausibility for all three passes.

---

## Phase 1 — Customer Service Pass

### 1.1 State Transition Table (minimum 5 rows)

| Step | Starting State | Operation | Preconditions [write `none` if genuinely absent] | Postconditions [write `none` if genuinely absent] | Ending State | Invariants Checked |
|------|---------------|-----------|--------------------------------------------------|---------------------------------------------------|--------------|-------------------|

**Invariant rules:** At least 2 per pass. Must encode real CS business rules. Disqualified patterns: `"ID is not null"`, `"record exists"`, `"field is populated"`, `"timestamp is set"`. A qualifying example: `"A ticket in RESOLVED state cannot transition to IN_PROGRESS without first transitioning through REOPENED"`. Entries matching any disqualified pattern invalidate the invariant section for this pass.

### 1.2 Defect Log

- **Defect type:**
- **Triggering operation:**
- **Reason:**

### 1.3 Race Condition Analysis

**Operations: [Op A name] and [Op B name]**

Name both operations explicitly before describing either ordering.

- **Ordering 1 — [Op A] before [Op B]:** Full interleaving — what state each operation reads, conflict or resolution named.
- **Ordering 2 — [Op B] before [Op A]:** Full independent description. Do not reference Ordering 1 or write "same as above." Describe each ordering as if the other does not exist.

### 1.4 Negative Path Trace

| Invalid Starting State | Blocked Operation | Unchanged State | Named Error |
|------------------------|------------------|-----------------|------------|

After filling this row: **confirm no mutation occurred** — explicitly verify the post-rejection state is identical to the starting state; passive column recording does not satisfy this requirement.

**Phase 1 gate:** Sections 1.1–1.4 must be complete before beginning Phase 2.

---

## Phase 2 — Sales Pass

Apply the same four-section schema (2.1 State Transition Table, 2.2 Defect Log, 2.3 Race Condition Analysis, 2.4 Negative Path Trace) to Sales domain states: leads, opportunities, quotes, orders, contracts.

Minimum 5 rows in 2.1. Apply invariant rules identically. Apply race condition and negative path requirements identically.

**Phase 2 gate:** Sections 2.1–2.4 must be complete before beginning Phase 3.

---

## Phase 3 — Finance Pass

Apply the same four-section schema (3.1 State Transition Table, 3.2 Defect Log, 3.3 Race Condition Analysis, 3.4 Negative Path Trace) to Finance domain states: invoices, payments, budget approvals, reconciliations, approval routing.

Minimum 5 rows in 3.1. Apply invariant rules identically. Apply race condition and negative path requirements identically.

---

## Phase 4 — Cross-Pass Synthesis

### 4.1 Invariant Register

| Invariant | Domain | Derived From (Pass + Step) |
|-----------|--------|---------------------------|

Cross-domain invariants holding across two or more passes must list all source derivations.

### 4.2 Completeness check

Confirm: at least 5 rows per pass, at least 15 rows total. If any pass falls below its floor, that pass is incomplete and must be extended before synthesis is complete.

---

**No prose substitutions.** Prose narrative in place of structured fields invalidates the artifact. Minimum 5 rows per pass. Minimum 15 rows total.

---
---

### V-05 — **Variation axes (combined): Output format (filled example row + anti-literal-copy guard) + Inertia framing (names what informal tracing looks like and why this replaces it)**
**Hypothesis:** An anchor example row eliminates column-level schema ambiguity before generation begins; naming the informal alternative (whiteboard notes, undeclared preconditions, single-ordering race analysis) creates contrast pressure that motivates compliance over regression.

---

You are a state-domain expert in Sales, Customer Service, and Finance.

Informal state traces — ad-hoc prose, whiteboard snapshots, preconditions left implicit, single-ordering race analysis — miss invariant violations and concurrent conflicts that structured hand-compilation catches. This prompt replaces informal tracing with a rigorous schema. Every state, operation, and invariant belongs in a slot.

---

## Schema 1 — State Transition Table

Minimum 5 rows per domain pass (minimum 15 rows total across all passes).

| Step | Starting State | Operation | Preconditions [write `none` if genuinely absent] | Postconditions [write `none` if genuinely absent] | Ending State | Invariants Checked |
|------|---------------|-----------|--------------------------------------------------|---------------------------------------------------|--------------|-------------------|
| *Example* | *Invoice: SUBMITTED* | *ApproverRejects* | *Invoice in SUBMITTED state; Approver role assigned* | *Approval request closed; Submitter notified* | *Invoice: REJECTED* | *Invoice total unchanged after rejection; Submitter ID preserved* |

**Do not include the example row in your output.** It is a reference anchor for column structure only — reproduce the schema, not this row.

**Invariant rules:** At least 2 per pass. Must encode real business rules. Disqualified patterns: `"ID is not null"`, `"record exists"`, `"amount field is populated"`. A qualifying example: `"Invoice total must equal the sum of approved line items after any line-item modification"`. Entries matching any disqualified pattern invalidate the invariant section. Naming a domain category without a concrete rule does not qualify.

---

## Schema 2 — Defect Log

At least 1 per pass. Ad-hoc notes in prose do not substitute for these three labeled fields.

- **Defect type:**
- **Triggering operation:**
- **Reason:**

---

## Schema 3 — Race Condition Analysis

Identify one concurrent operation pair per pass.

**Operations: [Op A name] and [Op B name]**

Name both operations explicitly. Naming only the conflict outcome, or naming only one operation, does not satisfy this section.

- **Ordering 1 — [Op A] before [Op B]:** Full interleaving — what state each operation reads, the conflict or resolution outcome.
- **Ordering 2 — [Op B] before [Op A]:** Full independent description. Do not write "same as above," "symmetric," "see Ordering 1," or any cross-reference. Each ordering must be self-contained and independently readable.

Single-ordering race analysis is the informal equivalent this section replaces — both orderings are required.

---

## Schema 4 — Negative Path Trace

| Invalid Starting State | Blocked Operation | Unchanged State | Named Error |
|------------------------|------------------|-----------------|------------|
| *Example* | *Invoice: CLOSED* | *AddLineItem* | *Invoice: CLOSED* | *ClosedInvoiceModificationException* |

**Do not include the example row in your output.**

After filling this row: **confirm no mutation occurred** — actively verify the post-rejection state is identical to the pre-operation starting state. Recording the starting state as a passive column value is the informal approach this step replaces; the verification must be an explicit act noted in the trace.

---

## Schema 5 — Invariant Register (produced once, after all passes)

| Invariant | Domain | Derived From (Pass + Step) |
|-----------|--------|---------------------------|

Cross-domain invariants must list all source derivations. This structure replaces per-pass isolated invariant lists with a cross-pass synthesis that makes multi-domain derivation traceable.

---

## Domain Passes — Run in this order: Sales → CS → Finance

**Sales:** Leads, opportunities, quotes, orders, contracts.
**Customer Service:** Tickets, escalations, SLA tracking, resolutions, closures.
**Finance:** Invoices, payments, approvals, reconciliations, budget allocations.

Apply Schemas 1–4 to each pass. Produce Schema 5 once, after all passes.

---

**No prose substitutions.** Narrative in place of structured fields invalidates the artifact. Minimum 5 rows per pass. Minimum 15 rows total.
