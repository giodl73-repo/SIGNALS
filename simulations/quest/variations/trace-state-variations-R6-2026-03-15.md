## trace-state — Round 6 Variations (v21 rubric)

---

### V-01 — Axis: Role Sequence (Finance → Sales → CS)
**Hypothesis**: Finance domain primes stronger invariants because amount-positivity, payment idempotency, and invoice lifecycle are inherently state-dependent. Leading with Finance before Sales/CS raises C-07 and C-20 (positive qualifying examples emerge naturally from Finance rules).

---

You are a **Finance state domain expert**. Hand-compile the state machine for a Finance entity (invoice, payment, ledger entry, or credit memo). Then validate the same transition model from a **Sales** perspective and a **Customer Service** perspective.

**Phase 1 — Finance Trace**

For the Finance entity you select, compile a state transition table with a minimum of 5 rows. Each row is one operation:

| Starting State | Operation | Preconditions | State Change | Ending State | Postconditions | Invariants Checked |
|---|---|---|---|---|---|---|

Rules:
- **Preconditions** and **Postconditions**: write `none` if genuinely absent. Do not leave blank.
- **Invariants Checked**: name the invariants evaluated after this operation. Minimum 2 domain invariants must appear across the trace. Non-trivial means the invariant encodes a real Finance business rule — e.g., *"Invoice amount must remain positive after creation"* qualifies. *"ID is not null"* does not qualify.
- Invariant triviality test: ask whether the rule would survive an audit meeting. Structural presence checks fail this test.

**Phase 2 — Defect Identification**

Identify at least one defect in your trace. Label it:

```
Defect: [name]
Type: [missing precondition check | invalid state transition | invariant violation | race condition]
Triggering operation: [operation name]
Reason: [why it is a defect]
```

**Phase 3 — Negative Path Trace**

Trace one rejected operation:

| Invalid Starting State | Blocked Operation | Unchanged Ending State | Named Error |
|---|---|---|---|

**Phase 4 — Race Condition**

Identify one pair of concurrent operations on the same entity. Describe **both** orderings independently:

*Ordering A→B*: [full description — do not write "same as below"]
*Ordering B→A*: [full description — do not write "same as above"]

Name the conflict or resolution mechanism for each ordering.

**Phase 5 — Sales and CS Cross-Validation**

Map the same entity lifecycle from a Sales domain perspective, then a CS domain perspective. Note any operations that have different preconditions or invariants across roles.

**Phase 6 — Reachability**

List every state transition you omitted, with a rationale for each omission. Silent omissions disqualify this criterion.

---

### V-02 — Axis: Output Format (Schema-first, criterion IDs embedded in column headers, example row, numeric floor)
**Hypothesis**: Embedding criterion IDs in column headers makes satisfaction structurally unavoidable at write time (C-14). Providing a filled example row (C-15) eliminates schema ambiguity. An explicit floor (C-17) makes completeness measurable. Nil-value annotations at the column level satisfy C-22.

---

You are a state domain expert in **Sales, Customer Service, or Finance**. Hand-compile a state machine for one entity from your chosen domain.

**Output Schema (minimum 6 rows — no exceptions)**

Fill this table. Every cell is required. Criterion IDs are embedded as field labels — satisfying the column structure satisfies the criterion.

| C-01a: Starting State | C-01b: Operation | C-02a: Preconditions [write `none` if genuinely absent] | C-01c: Ending State | C-02b: Postconditions [write `none` if genuinely absent] | C-03: Invariants Checked (min 2 domain invariants total) |
|---|---|---|---|---|---|
| *Draft* | *Submit for approval* | *Submitter has edit rights; amount > 0* | *Pending Review* | *Approval request logged; submitter notified* | *Invoice amount remains positive; status progression is monotonic* |
| … | … | … | … | … | … |

**Invariant Declaration Block (C-03, C-07, C-18, C-20)**

Declare all invariants referenced in the Invariants Checked column:

```
Invariant [N]: [statement]
Source row(s): [row numbers where this invariant was checked — C-13 linkage]
```

Invariant quality bar:
- **Disqualified pattern** (do not use): *"Entity ID is not null"* — generic structural presence checks fail the domain-relevance test.
- **Qualifying pattern** (use as a model): *"Invoice amount must remain positive after creation"* — encodes a Finance business rule auditable in domain terms.

Prose substitutions for table cells are not permitted. Any cell replaced with a narrative paragraph invalidates this artifact.

**Defect Block (C-04)**

```
Defect: [name]
Type: [missing precondition check | invalid state transition | invariant violation | race condition]
Triggering operation: [row reference or operation name]
Reason: [one sentence]
```

**Negative Path Block (C-09)**

| Invalid Starting State | Blocked Operation | Unchanged Ending State | Named Error |
|---|---|---|---|
| … | … | … | … |

**Race Condition Block (C-08, C-12, C-21)**

One concurrent operation pair. Describe each ordering in full — **do not write "same as above" or reference the other ordering**; each must be independently and completely described.

*Ordering A→B*:
— Preconditions at start of A: …
— State after A completes: …
— State after B completes: …
— Conflict or resolution: …

*Ordering B→A*:
— Preconditions at start of B: …
— State after B completes: …
— State after A completes: …
— Conflict or resolution: …

**Reachability Block (C-10)**

| Omitted Transition | Rationale |
|---|---|

Every omitted state→operation pair must appear here. No silent omissions.

---

### V-03 — Axis: Lifecycle Emphasis (Invariant derivation pipeline as primary structure)
**Hypothesis**: Inverting the default order — extracting invariants from domain knowledge before tracing operations — produces C-13 (derivation pipeline) by construction and raises C-07 (non-trivial invariants) because invariants are declared before they can be weakened by the trace.

---

You are a **Customer Service, Sales, or Finance** state domain expert. This exercise is structured as an **invariant derivation pipeline**: declare what must always be true first, then trace operations against that declared truth.

**Step 1 — Domain Invariant Declaration**

Before tracing any operations, declare the invariants that must hold throughout this entity's lifecycle. Minimum 2 invariants.

```
Invariant I-01: [statement]
Domain basis: [why this is a real business rule — one sentence]

Invariant I-02: [statement]
Domain basis: [why this is a real business rule]
```

Quality bar:
- **Disqualifying pattern**: *"Record ID is not null"* — generic structural presence checks fail this bar.
- **Qualifying pattern**: *"Invoice amount must remain positive after creation"* — names a business constraint that would appear in a Finance policy document.

**Step 2 — State Transition Trace (minimum 5 operations)**

For each operation, identify which declared invariants are checked:

| Starting State | Operation | Preconditions | Ending State | Postconditions | Invariants Checked [cite I-NN] |
|---|---|---|---|---|---|

Rules:
- **Preconditions** and **Postconditions**: write `none` if genuinely absent — do not leave blank.
- **Invariants Checked**: cite at least one of your declared invariants (I-01, I-02, …) per row where relevant. This cross-reference is the derivation link.
- Any row that cannot cite an invariant must explain why in the Reachability block.

**Step 3 — Defect Discovery**

Review the trace for: missing precondition checks, invalid state transitions, invariant violations, race conditions. Label at least one:

```
Defect: [name]
Type: [category]
Triggering operation: [operation or row ref]
Invariant violated: [I-NN or "none"]
Reason: [one sentence]
```

**Step 4 — Race Condition (at least one concurrent pair)**

Concurrent operations A and B on the same entity. Describe both orderings:

*Ordering A→B*: [full independent description — do not refer to Ordering B→A]
*Ordering B→A*: [full independent description — do not refer to Ordering A→B]
Name the conflict or resolution for each.

**Step 5 — Negative Path**

One rejected operation, all four elements: invalid starting state, blocked operation, unchanged ending state, named error.

**Step 6 — Reachability**

Every transition pair not traced must be listed with a rationale. Silent omissions are not permitted.

---

### V-04 — Combined: V-02 schema spine + consequence language + C-21 anti-lazy-copy inside race instructions
**Hypothesis**: Adding explicit invalidation language (C-19) to the V-02 schema and embedding the anti-lazy-copy constraint specifically inside the race section instructions (C-21) closes the two remaining enforcement gaps from Round 5 without disrupting the schema structure that already satisfies C-14/C-15/C-17/C-22.

---

You are a state domain expert in **Sales, Customer Service, or Finance**. Hand-compile a complete state machine for one entity.

**Hard Constraints — Violation of any of these invalidates this artifact**:
1. The state transition table must contain at least 5 complete rows (no partial rows).
2. Preconditions and Postconditions cells may not be left blank — write `none` if genuinely absent.
3. No table cell may be replaced with prose narrative.
4. The Race Condition section must describe each ordering independently — "same as above" or cross-references between orderings disqualify that section.

**State Transition Table (minimum 5 rows)**

| Starting State | Operation | Preconditions [write `none` if absent] | Ending State | Postconditions [write `none` if absent] | Invariants Checked |
|---|---|---|---|---|---|
| *Active* | *Place order* | *Customer has payment method on file; inventory ≥ 1* | *Order Pending* | *Order ID assigned; inventory decremented* | *Inventory count ≥ 0; order total > 0* |
| … | … | … | … | … | … |

**Invariant Registry**

List every distinct invariant referenced in the table. Minimum 2.

- **Disqualifying pattern** (do not use): *"ID is not null"* — fails the domain-relevance test.
- **Qualifying pattern** (use as positive model): *"Invoice amount must remain positive after creation"* — auditable in domain terms.

```
Invariant [N]: [statement]
Referenced in rows: [row numbers]
```

**Defect Block**

```
Defect: [name]
Type: [missing precondition check | invalid state transition | invariant violation | race condition]
Triggering operation: [operation or row]
Reason: [one sentence]
```

**Negative Path Block**

| Invalid Starting State | Blocked Operation | Unchanged Ending State | Named Error |
|---|---|---|---|

**Race Condition Block**

Select one concurrent operation pair. The following constraint applies to this section: **describe each ordering completely and independently — do not write "same as above," do not reference the other ordering, and do not use shorthand like "reverse of the above."** Each ordering must be fully self-contained.

*Ordering A→B*:
— Starting state and preconditions: …
— State after A completes: …
— State after B completes: …
— Conflict or resolution: …

*Ordering B→A*:
— Starting state and preconditions: …
— State after B completes: …
— State after A completes: …
— Conflict or resolution: …

Failure to describe both orderings fully invalidates the race condition section.

**Reachability Block**

| Omitted Transition | Rationale |
|---|---|

No silent omissions. A blank reachability block disqualifies C-10.

---

### V-05 — Combined: V-03 lifecycle + V-02 schema + Finance-first role + C-20/C-21/C-22 field-level anchors
**Hypothesis**: Fusing the invariant-derivation-first lifecycle (V-03) with the schema column-level criterion ID anchors (V-02), Finance-first role framing (V-01), a positive qualifying invariant example (C-20), field-level nil-value annotations (C-22), and anti-lazy-copy inside the race section (C-21) should be the highest-composite rubric scoring configuration — targeting all 22 criteria simultaneously.

---

You are a **Finance state domain expert** (cross-validated by Sales and Customer Service). This trace is structured as an **invariant-first derivation pipeline**: declare invariants before operations, then trace operations against declared invariants.

**Step 1 — Invariant Declaration (C-03, C-07, C-18, C-20)**

Declare all invariants before tracing any operations. Minimum 2.

```
Invariant I-01: [statement]
Domain basis: [one sentence — why this is a Finance business rule]

Invariant I-02: [statement]
Domain basis: [one sentence]
```

Invariant quality bar — both a disqualifying and a qualifying example are given:
- **Disqualifying** (do not use this pattern): *"Record ID is not null"* — generic structural presence check, fails Finance domain relevance.
- **Qualifying** (use this as a positive model): *"Invoice amount must remain positive after creation"* — names a Finance business rule auditable in domain terms.

Declaring invariants that match only the disqualifying pattern invalidates the invariant section.

**Step 2 — State Transition Table (minimum 6 rows)**

Every column header below carries its criterion ID. Filling the column satisfies the criterion.

| C-01a: Starting State | C-01b: Operation | C-02a: Preconditions [write `none` if genuinely absent] | C-01c: Ending State | C-02b: Postconditions [write `none` if genuinely absent] | C-03/C-13: Invariants Checked [cite I-NN] |
|---|---|---|---|---|---|
| *Draft* | *Approve invoice* | *Approver role assigned; I-01 holds at entry* | *Approved* | *Approval timestamp set; audit log entry created* | *I-01: amount > 0 confirmed; I-02: status is monotonic* |
| … | … | … | … | … | … |

Rules:
- **Preconditions / Postconditions**: write `none` if genuinely absent. A blank cell is not equivalent to `none`.
- **Invariants Checked**: cite the declared invariant by ID (I-01, I-02, …). This cross-reference is the derivation link required to satisfy C-13. A row that asserts an invariant not in Step 1 does not count.
- Prose substitutions for any cell are prohibited. Violation invalidates this artifact.

**Step 3 — Sales and CS Cross-Validation**

Briefly note any operations where Sales or CS would declare different preconditions or invariants. One to three examples is sufficient.

**Step 4 — Defect Block (C-04)**

```
Defect: [name]
Type: [missing precondition check | invalid state transition | invariant violation | race condition]
Triggering operation: [row reference or operation name]
Invariant at risk: [I-NN or "none"]
Reason: [one sentence]
```

**Step 5 — Negative Path Block (C-09)**

| Invalid Starting State | Blocked Operation | Unchanged Ending State | Named Error |
|---|---|---|---|
| … | … | … | … |

**Step 6 — Race Condition Block (C-08, C-12, C-21)**

Select one concurrent Finance operation pair. Declare each ordering below.

**Race section rule — applies only to this section**: describe each ordering completely and independently. Do not write "same as above," do not reference Ordering B→A from Ordering A→B or vice versa, and do not use phrases like "the reverse applies." Each ordering must be a fully self-contained description. Failure to describe both orderings independently disqualifies this section.

*Ordering A→B*:
- Preconditions at start of A: …
- State after A completes: …
- State after B completes: …
- Conflict or resolution mechanism: …
- Invariant status: …

*Ordering B→A*:
- Preconditions at start of B: …
- State after B completes: …
- State after A completes: …
- Conflict or resolution mechanism: …
- Invariant status: …

**Step 7 — Reachability Block (C-10)**

| Omitted State Transition | Rationale for Omission |
|---|---|

List every (starting state, operation) pair not traced. A blank reachability block is a silent omission and disqualifies C-10.

---

## Variation Map

| Variation | Primary Axis | Secondary Axes | New Criteria Targeted |
|-----------|-------------|----------------|----------------------|
| V-01 | Role sequence: Finance → Sales → CS | — | C-07, C-20 (Finance domain primes stronger invariants) |
| V-02 | Output format: schema with embedded criterion IDs, example row, numeric floor | — | C-14, C-15, C-17, C-22 |
| V-03 | Lifecycle emphasis: invariant derivation as primary structure | — | C-13, C-07 |
| V-04 | Combined: V-02 schema + consequence language + C-21 inside race section | V-02 + invalidation language | C-19, C-21 |
| V-05 | Combined: V-03 lifecycle + V-02 schema + Finance-first + C-20/C-21/C-22 field anchors | V-01 + V-02 + V-03 | C-20, C-21, C-22 (all Round 6 targets) |
