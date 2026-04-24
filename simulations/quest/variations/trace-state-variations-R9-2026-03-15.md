## trace-state — Round 9 Variates (rubric v23)

---

## V-01 — Role Sequence: Finance → CS → Sales

**Axis**: Role sequence (Finance anchors first)
**Hypothesis**: Finance-first establishes the strictest numeric invariant bar; CS and Sales passes inherit that rigor rather than establishing their own looser baseline. Predicted effect: stronger C-03 and C-27 compliance across all passes; Finance invariants bleed forward and raise the floor for domain plausibility.
**New criteria targeted**: C-26, C-27 — plus C-09, C-17, C-18, C-19, C-22

---

You are a state-transition auditor. Hand-compile state transitions for the feature under review. Run three domain passes in this fixed order: **Finance**, then **Customer Service**, then **Sales**.

### Output Format

For each pass, produce a State Transition Table using this exact column set:

| Row | Starting State | Operation | Preconditions [write `none` if genuinely absent] | Ending State | Postconditions [write `none` if genuinely absent] | Invariants Checked |

**Completeness floors — hard constraints:**

- Minimum 5 rows per pass
- Minimum 15 rows total across all three passes
- Any table falling below either floor is incomplete and invalidates the artifact

Leave no cell blank. If a value is genuinely absent for a given operation, write `none` — a blank cell is not the same as an acknowledged absence.

### Invariants

Before running Pass 1 (Finance), declare at least two domain-meaningful invariants. These must encode real business rules, not structural data checks.

**Disqualified patterns — the following do NOT qualify as invariants:**

- `"ID is not null"`
- `"record exists"`
- `"amount field is populated"`

These are checks that are true by definition of the data existing. If either declared invariant matches any pattern on this list, it is invalid and the invariant section fails.

Check all declared invariants after every operation row. A row that omits invariant verification is structurally incomplete.

### Defect Section

After all three passes, label at least one defect:

- **Type**: missing precondition / invariant violation / invalid state transition / other
- **Triggering Operation**: row reference (e.g., Finance Pass, Row 3)
- **Reason**: why this constitutes a defect in this domain

### Negative Path

Trace at least one rejected operation. All four elements are required:

1. Invalid starting state
2. Blocked operation
3. Post-rejection state — must be unchanged; confirm no mutation occurred
4. Named error or rejection reason

### Race Condition Analysis

Identify one pair of concurrent operations. Name both operations and describe the conflict or resolution that arises from their interleaving.

### Domain Requirement

All states and operations must be recognizable in Finance, Customer Service, or Sales domains. Use real business vocabulary: invoice, ticket, order, payment, approval, escalation, dispute, quote, fulfillment. Generic system states (e.g., "pending", "active") without explicit business context do not satisfy the domain plausibility requirement.

---

## V-02 — Output Format: Numbered Step Blocks with Schema-Level Criterion Embedding

**Axis**: Output format (numbered step blocks replace tables; criterion IDs are embedded as field labels)
**Hypothesis**: Embedding criterion IDs directly into field label syntax makes satisfaction structurally unavoidable at write time — a filled step is a compliant step by construction. Predicted effect: C-14 and C-11 both satisfied mechanically; prose substitution drops to near zero.
**New criteria targeted**: C-26, C-27 — plus C-14, C-15, C-16, C-17, C-24

---

You are a state-transition auditor. Hand-compile state transitions for the feature under review. Run three domain passes: **Sales**, then **Customer Service**, then **Finance**.

**No prose substitutions.** All output must conform to the numbered-step format below. Prose narrative in place of a structured step is a format violation and invalidates the artifact.

### Step Format

Write every operation as a numbered step block using this exact structure:

```
Step N — [C-01: Starting State] ___ → [C-01: Ending State] ___ via [C-01: Operation] ___
  [C-02] Preconditions: ___
  [C-02] Postconditions: ___
  [C-03] Invariants Checked: ___
```

The field labels carry criterion IDs. Filling any field satisfies the corresponding criterion for that step. Do not remove or rephrase the labels.

> **EXAMPLE STEP — do not reproduce this block verbatim in your output; it is a reference anchor only:**
>
> Step 1 — [C-01: Starting State] Quote Created → [C-01: Ending State] Quote Submitted via [C-01: Operation] Submit Quote
>   [C-02] Preconditions: Customer record is active; Quote total > 0; … (add all that apply)
>   [C-02] Postconditions: Quote status = Submitted; Timestamp recorded; … (add all that apply)
>   [C-03] Invariants Checked: Quote total must remain positive throughout lifecycle; … (check all declared invariants)

**Completeness floors:**

- Minimum 4 steps per pass
- Minimum 15 steps total across all three passes

### Invariants

Before Pass 1 (Sales), declare at least two domain-meaningful invariants. These must be real business rules.

**Disqualified patterns — the following do NOT qualify:**

- `"ID is not null"`
- `"record exists"`
- `"amount field is populated"`

Check all declared invariants in the `[C-03] Invariants Checked` field of every step.

### Defect Section

After all passes, label at least one defect:

```
[C-04] Defect
  Type: ___
  Step Reference: ___
  Reason: ___
```

### Race Condition

```
[C-08] Race Condition
  Operations: ___
  Conflict or Resolution: ___
```

### Domain Requirement

All states and operations must be recognizable in Sales, Customer Service, or Finance. Step content not anchored in one of these domains fails the domain plausibility check.

---

## V-03 — Lifecycle Emphasis: Explicit Phase Gates with Reachability and Cross-Pass Invariant Register

**Axis**: Lifecycle emphasis (full lifecycle coverage required; phase gates and reachability register made explicit; section-level invalidation clauses per section)
**Hypothesis**: Making phase boundaries explicit and requiring a reachability register for every omitted transition forces completeness by accountability rather than by instruction. Predicted effect: C-10 satisfaction climbs; C-25 cross-pass derivation strengthens; section-level invalidation (C-23) is more natural when each section has defined scope.
**New criteria targeted**: C-26, C-27 — plus C-10, C-12, C-21, C-23, C-25

---

You are a state-transition auditor running a full lifecycle analysis. Cover the feature from earliest lifecycle stage to terminal state. Run three domain passes: **Sales**, **Customer Service**, **Finance**.

### State Transition Table (per pass)

| Row | Starting State | Operation | Preconditions | Ending State | Postconditions | Invariants Checked |

**Completeness floors:**

- Minimum 5 rows per pass
- Minimum 15 rows total across all three passes

### Reachability Register (per pass)

After completing each transition table, list every transition you did NOT trace. For each omission:

- **Omitted transition**: name the starting state, operation, and ending state
- **Rationale**: why this transition was excluded from the trace

Silent omissions invalidate this section. A pass with no Reachability Register entry is valid only if all reachable transitions were traced and that fact is explicitly stated.

### Invariant Register

This named structure aggregates invariants across all three domain passes. Populate it after each pass:

| ID | Invariant | Declared In | Derived From |
|----|-----------|-------------|--------------|

Cross-reference every declared invariant to at least one transition row (e.g., "CS Pass, Row 3"). Invariants with no row derivation reference are incomplete entries.

Declare at least two invariants per pass before running that pass. The following do NOT qualify:

- `"ID is not null"`
- `"record exists"`
- `"amount field is populated"`
- `"field is not empty"`

### Defect Section

After all passes, label at least one defect: type, row reference, reason.

### Race Condition Analysis

Identify one pair of concurrent operations. Describe **both orderings independently**:

**Ordering A→B**: [describe fully — starting states, operation sequence, resulting state, conflict or resolution]

**Ordering B→A**: [describe fully — starting states, operation sequence, resulting state, conflict or resolution — do not write "same as above" or reference Ordering A]

Each ordering must be independently and completely described. Cross-referencing between orderings (e.g., "same as above", "symmetric to A→B", "see previous") is prohibited. If the Race Condition section contains a cross-reference instead of an independent description, this section is invalid.

### Domain Requirement

All states and operations must be recognizable in Sales, Customer Service, or Finance domains.

---

## V-04 — Combination: CS → Finance → Sales + Conversational Register with Inline Criterion Anchoring

**Axes**: Role sequence (CS first) + Phrasing register (conversational, guided)
**Hypothesis**: Leading with Customer Service (empathy-driven, ticket-oriented) in a guided, conversational register produces more naturally derived invariants from real support domain logic; Finance then stress-tests those invariants under numeric constraints; Sales finalizes with commercial realism. Criterion IDs embedded as field labels (C-11) ensure compliance is auditable at the element level regardless of register.
**New criteria targeted**: C-26, C-27 — plus C-11, C-20, C-22, C-23, C-24

---

Walk through state transitions for this feature as a domain expert would — methodically, one operation at a time. Run three passes: **Customer Service** first, then **Finance**, then **Sales**.

For each operation, fill out the block below. Field labels include rubric criterion IDs so compliance is auditable at the element level without cross-referencing.

### Transition Block Format

```
[C-01] Starting State: ___
[C-01] Operation: ___
[C-01] Ending State: ___
[C-02] Preconditions: ___ (write `none` if genuinely absent — do not leave blank)
[C-02] Postconditions: ___ (write `none` if genuinely absent — do not leave blank)
[C-03] Invariants Checked: ___
```

> **EXAMPLE BLOCK — do not reproduce this block verbatim in your output; treat it as a reference template only:**
>
> [C-01] Starting State: Ticket Open
> [C-01] Operation: Assign to Agent
> [C-01] Ending State: Ticket Assigned
> [C-02] Preconditions: Agent is available; Ticket has not been previously assigned; … (add domain-specific conditions)
> [C-02] Postconditions: Agent notified; Ticket status updated to Assigned; … (add all that apply)
> [C-03] Invariants Checked: A ticket must have exactly one owner at all times; … (check all declared invariants)

**Completeness floors:**

- Minimum 4 blocks per pass
- Minimum 15 blocks total across all three passes

### Invariants

Before each pass, declare at least two invariants. These should be real business rules — things that must always hold in this domain, regardless of what operation fires.

**What counts as a valid invariant:**

- "Invoice amount must remain positive after creation" — a Finance business rule about transaction integrity
- "A support ticket must have exactly one owner at all times" — a CS business rule about accountability
- "A closed order cannot be reopened without manager approval" — a Sales business rule about workflow authority

**What does NOT count:**

- `"ID is not null"`
- `"record exists"`
- `"amount field is populated"`

If any declared invariant matches a pattern from the "does not count" list, the Invariant section is incomplete and invalid. This is a section-level failure scored independently of the overall artifact.

### Defect Section

```
[C-04] Defect
  Type: ___
  Block Reference: ___
  Reason: ___
```

At least one qualifying defect block is required. If this section contains no qualifying defect block, the Defect Section is invalid — this is a section-level failure independent of the artifact completeness check.

### Race Condition

```
[C-08] Race Condition
  Operations: ___
  Conflict or Resolution: ___
```

### Domain Check

```
[C-05] Domain: Customer Service / Finance / Sales (all states and operations must be recognizable in one of these)
```

---

## V-05 — Combination: Table Format + Inertia Framing (Status Quo Delta Column)

**Axes**: Output format (table with Status Quo Delta column) + Inertia framing (every transition anchored against current process)
**Hypothesis**: Adding a "Status Quo Delta" column forces the model to compare each new state transition against the existing workflow, surfacing preconditions that arise from organizational inertia (approval flows, legacy data formats, permission structures) that a pure forward-trace misses. Predicted effect: stronger domain realism in preconditions; invariants more naturally derived from visible deltas rather than declared from scratch.
**New criteria targeted**: C-26, C-27 — plus C-13, C-15, C-19, C-20, C-25

---

You are auditing state transitions for a feature that changes an existing workflow. For each operation, note how the new behavior differs from the current (status quo) process. This anchors your preconditions and invariants in real organizational reality, not just technical correctness.

Run three domain passes: **Sales**, **Customer Service**, **Finance**.

### Transition Table (per pass)

| Row | Starting State | Operation | Preconditions | Ending State | Postconditions | Invariants Checked | Status Quo Delta |

The **Status Quo Delta** column describes how this transition differs from the current process. Write `no change` if the behavior is identical to the existing workflow.

**Completeness floors:**

- Minimum 5 rows per pass
- Minimum 15 rows total across all three passes

> **EXAMPLE ROW — do not reproduce this row verbatim in your output; reference only:**
>
> | 1 | Invoice Draft | Submit for Approval | Amount > 0; Approver assigned; … | Invoice Pending | Approval request sent; Audit entry created; … | Invoice amount unchangeable during approval; … | Previously: email to manager; now: system-routed with SLA |

Leave no cell blank. Write `none` for genuinely absent values in the Preconditions and Postconditions columns.

### Invariant Derivation

As you fill the transition table, flag any row that surfaces an invariant — a business rule that must hold across all future operations. After each pass, record flagged rows in the register below.

**Invariant Register** (aggregate across all passes):

| ID | Invariant | Derived From | Pass |
|----|-----------|--------------|------|

Cross-reference every declared invariant to at least one specific row (e.g., "Sales Pass, Row 3"). Declaring invariants without a row derivation reference fails the derivation requirement.

**Qualifying invariant example**: "Invoice amount must remain positive after creation" — this encodes a real Finance business rule traceable to approval workflow constraints.

**Disqualified patterns — the following do NOT qualify:**

- `"ID is not null"`
- `"record exists"`
- `"amount field is populated"`

If any declared invariant matches a pattern on this list, it is invalid.

### Defect Section

Label at least one defect with: type, row reference, reason. A submission without a qualifying defect is invalid and cannot be accepted.

### Race Condition Analysis

Name one concurrent operation pair. Describe the conflict or resolution arising from their interleaving.

### Domain Requirement

All states and operations must be recognizable in Sales, Customer Service, or Finance.

---

## Coverage Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01–C-05 (essential) | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-06 (consistent format) | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-07 (non-trivial invariants) | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-08 (race condition) | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-09 (negative path) | ✓ | — | — | — | — |
| C-10 (reachability) | — | — | ✓ | — | — |
| C-11 (inline criterion anchoring) | — | ✓ | — | ✓ | — |
| C-12 (symmetric interleaving) | — | — | ✓ | — | — |
| C-13 (invariant derivation pipeline) | — | — | ✓ | — | ✓ |
| C-14 (schema-level enforcement) | — | ✓ | — | — | — |
| C-15 (example row with anchors) | — | ✓ | — | ✓ | ✓ |
| C-16 (no-prose constraint) | — | ✓ | — | — | — |
| C-17 (per-pass floor) | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-18 (named disqualifying example) | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-19 (invalidation consequence) | ✓ | ✓ | — | — | ✓ |
| C-20 (qualifying example) | — | — | — | ✓ | ✓ |
| C-21 (anti-lazy-copy in race) | — | — | ✓ | — | — |
| C-22 (nil-value at field level) | ✓ | — | — | ✓ | ✓ |
| C-23 (section-level invalidation) | — | — | ✓ | ✓ | — |
| C-24 (anti-literal-copy on example) | — | ✓ | — | ✓ | ✓ |
| C-25 (cross-pass invariant register) | — | — | ✓ | — | ✓ |
| **C-26 (aggregate trace floor)** | ✓ | ✓ | ✓ | ✓ | ✓ |
| **C-27 (enumerated exclusion list)** | ✓ | ✓ | ✓ | ✓ | ✓ |
