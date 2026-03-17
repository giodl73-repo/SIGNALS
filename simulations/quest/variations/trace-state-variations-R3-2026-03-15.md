## trace-state — V-01 through V-05 (Round 3)

---

## V-01 — Output Format Axis

**Hypothesis**: Embedding criterion IDs directly in column headers makes compliance structurally unavoidable (C-14), and a pre-filled example row with placeholder anchors (C-15) eliminates schema ambiguity before generation begins.

---

You are a state-transition analyst compiling domain state changes by hand.

**Domain**: Choose one — Sales pipeline, Customer Service ticket lifecycle, or Finance payment authorization.

**Hard rule**: No prose substitutions. Every element of this trace must appear in a table cell. If you find yourself writing a paragraph where a row belongs, that is a format violation.

---

### Invariant Declaration

Before filling any trace row, declare your invariants here:

| ID | Invariant | Business Rule |
|----|-----------|---------------|
| I-1 | … | … |
| I-2 | … | … |

Minimum two. Must encode real domain rules — not generic structural facts like "object must have an ID."

---

### Main Trace [C-01 · C-02 · C-03]

Column headers carry criterion IDs. Filling any cell in a column satisfies that criterion at the element level.

| Step [C-01a] | From [C-01b] | Operation [C-01c] | To [C-01d] | Pre [C-02a] | Post [C-02b] | Invariants Checked [C-03: ≥2 per row] |
|---|---|---|---|---|---|---|
| 1 | Draft | SubmitQuote | UnderReview | RepAssigned=true; Amount>0 | InReviewQueue=true | I-1: Amount≥0 ✓; I-2: ValidStage ✓ |
| 2 | … | … | … | … | … | … |
| 3 | … | … | … | … | … | … |

> Example row above is filled. Replace `…` with your domain values. Do not collapse or omit columns.

---

### Defect Log [C-04]

| ID | Type | Triggering Operation | State at Trigger | Reason |
|----|------|---------------------|-----------------|--------|
| D-01 | … | … | … | … |

Minimum one row. Permitted types: `InvalidTransition` · `MissingPreconditionCheck` · `InvariantViolation` · `RaceCondition`

---

### Race Condition Analysis [C-08 · C-12]

Both orderings are required. Writing "symmetric" without describing both does not qualify.

| Pair | Op-A | Op-B | Result A→B | Result B→A | Asymmetric? |
|------|------|------|-----------|-----------|-------------|
| RC-01 | … | … | … | … | Yes/No |

If results differ: name the conflict. If results match: confirm idempotency explicitly.

---

### Negative Path [C-09]

| Step | Invalid State | Blocked Operation | Unchanged State | Named Error |
|------|-------------|-----------------|----------------|-------------|
| N-01 | … | … | … | … |

---

### Omitted Transitions [C-10]

| Transition Skipped | Rationale |
|-------------------|-----------|
| … | … |

Silent omissions do not qualify. Every skipped transition needs a named rationale.

---

### Invariant Derivation Pass [C-13]

After completing the trace, cross-reference each invariant against the rows that generated it:

> I-1 [AmountNeverNegative] ← derived from rows 1, 4, 8 — each transition constrained the Amount field at write time

One derivation note per declared invariant.

---

### Domain Expert Review

Three experts review the completed trace in sequence:

1. **Sales Expert** — validates pipeline stage names, quota invariants, deal lifecycle rules
2. **Customer Service Expert** — validates ticket status flows, SLA states, escalation transitions
3. **Finance Expert** — validates payment states, balance invariants, authorization flows

Each expert: (a) confirms domain plausibility, (b) flags or approves one non-trivial invariant, (c) signs off or escalates.

---

BEGIN. Declare invariants, fill all tables, complete expert review.

---

---

## V-02 — Lifecycle Emphasis Axis

**Hypothesis**: Giving equal explicit instruction depth to each lifecycle phase — preconditions, transition, postconditions, defect — produces richer hand-compiled traces than open-ended output instructions.

---

You are a state-machine analyst. Hand-compile a state machine trace for one domain: Sales pipeline, Customer Service ticket lifecycle, or Finance payment processing.

For each operation in your chosen domain, work through four lifecycle phases in sequence. Do not skip phases or merge them into a single description.

---

### Phase 1 — Precondition Inventory

Before executing any operation, name every condition that must hold. Organize as three sub-categories:

- **Entity state**: What state is the object currently in?
- **Guard conditions**: What values or flags must be true?
- **External dependencies**: What external state is assumed?

Write each as a named condition, not a prose sentence. If preconditions are genuinely none, write `none` — do not leave the phase blank.

---

### Phase 2 — State Transition

Record the transition as a labeled tuple:

```
(FromState, Operation) → ToState
```

- `FromState`: named state label from your domain vocabulary
- `Operation`: verb-noun form preferred (e.g., `ApproveQuote`, `EscalateTicket`)
- `ToState`: named state label

If the operation is invalid for the current `FromState`, record it as a **Rejected Transition** and route to Phase 4 directly.

---

### Phase 3 — Postcondition + Invariant Check

Immediately after the transition, verify two things:

**Postconditions**: What must now be true? Name each postcondition explicitly.

**Invariants**: Which declared invariants were potentially affected by this operation? State whether each holds. Invariants must be declared before your first trace row. Declare at least two. They must encode real business rules — not generic structural facts.

Examples of non-trivial invariants:
- "An approved quote cannot revert to Draft without an explicit Undo Approval operation"
- "A payment cannot be Authorized if account balance is below transaction amount"
- "A ticket in Resolved state cannot accept new comments without reopening"

---

### Phase 4 — Defect + Anomaly Catalog

For each anomaly encountered during the trace:

| Defect | Type | Triggering Operation | State at Anomaly | Reason |
|--------|------|---------------------|-----------------|--------|
| D-01 | … | … | … | … |

Types: `InvalidTransition` · `MissingPreconditionCheck` · `InvariantViolation` · `RaceCondition`

At minimum: manufacture one defect by attempting an invalid operation and tracing the failure completely through all four phases — including the precondition that was missing, the invariant that broke, or the state that should have rejected the operation.

---

### Trace Format

Use a numbered step table for Phases 1–3, one row per operation:

| Step | From | Op | To | Phase 1: Pre | Phase 3: Post | Phase 3: Invariants |
|------|------|----|----|-------------|--------------|---------------------|
| 1 | … | … | … | … | … | … |

Phase 4 uses a separate defect table. No phase column may be empty — write `none` if genuinely empty.

---

### Race Condition Section

Identify at least one operation pair that could execute concurrently in your domain. Trace both orderings:

- **Ordering 1**: Op-A executes, then Op-B
- **Ordering 2**: Op-B executes, then Op-A

Name the conflict or confirm idempotency for each ordering separately.

---

### Domain Expert Review

After completing the trace, three domain experts validate in sequence:

**Sales Expert**: Are stage names real pipeline stages? Do quota and forecast invariants match actual practice? Does the defect catalog include a Sales-specific anomaly?

**Customer Service Expert**: Are ticket statuses plausible? Is the SLA escalation path captured? Does Phase 1 correctly identify SLA state as an external dependency?

**Finance Expert**: Are payment and authorization states correct? Do balance invariants hold after every Phase 3 check?

Each expert approves or flags one item for revision. If flagged: revise that row and re-check Phase 3.

---

BEGIN. Declare invariants, then work Phase 1 → Phase 2 → Phase 3 → Phase 4 → Expert Review → Race Conditions, in that order.

---

---

## V-03 — Role Sequence Axis

**Hypothesis**: Leading with the Finance Expert sets balance-sheet-level invariant rigor that propagates discipline into softer state domains, producing non-trivial invariants across all three domains rather than domain-local ones only.

---

You are a state-transition analyst. Hand-compile a state machine trace for one domain: Sales pipeline, Customer Service ticket lifecycle, or Finance payment authorization.

**Mandatory role sequence**: Finance Expert → Customer Service Expert → Sales Expert

The Finance Expert runs first and establishes the invariant standards that subsequent experts must meet or exceed.

---

### Step 1 — Finance Expert Opens

The Finance Expert selects the domain and establishes the framework:

1. Name the domain and its primary entity (e.g., "payment authorization request", "deal record", "support ticket")
2. Declare 3–5 invariants using Finance-style notation:

   | ID | Invariant | Hard or Soft? |
   |----|-----------|--------------|
   | I-1 | … | Hard |
   | I-2 | … | Soft |

   *Hard* = system-enforced (violation must be blocked). *Soft* = convention (violation is a defect but not always prevented).

3. Produce the first 3 trace rows:

   | Step | From | Op | To | Pre | Post | INVs Checked |
   |------|------|----|----|-----|------|-------------|
   | 1 | … | … | … | … | … | I-1 ✓, I-2 ✓ |

---

### Step 2 — Customer Service Expert Extends

The CS Expert adds 3+ trace rows for CS-relevant operations, inheriting the Finance invariant set:

1. Add rows to the main trace table (same format)
2. Add 1–2 CS-specific invariants (e.g., SLA breach trigger, escalation gate) — extend the invariant table
3. Identify one state transition where Finance's invariants create tension in a CS context — note it as a cross-domain flag:

   > *Cross-domain tension*: [transition name] — Finance I-N says X, but CS practice often does Y. Flagged.

---

### Step 3 — Sales Expert Completes

The Sales Expert adds 3+ pipeline-stage operations and closes the trace:

1. Add rows to the main trace table
2. Map deal states into the inherited invariant framework
3. Manufacture and trace one race condition — two Sales reps acting on the same deal simultaneously:

   | Pair | Op-A | Op-B | Result A→B | Result B→A | Asymmetric? |
   |------|------|------|-----------|-----------|-------------|
   | RC-01 | … | … | … | … | … |

   Both orderings required.

---

### Step 4 — Defect Catalog (all three experts contribute)

Each expert nominates one defect from their trace section:

| Defect | Expert | Type | Triggering Op | Reason |
|--------|--------|------|--------------|--------|
| D-01 | Finance | … | … | … |
| D-02 | CS | … | … | … |
| D-03 | Sales | … | … | … |

Types: `InvalidTransition` · `MissingPreconditionCheck` · `InvariantViolation` · `RaceCondition`

---

### Step 5 — Negative Path

Finance Expert traces one rejected operation end-to-end:

| Step | State at Attempt | Blocked Op | State After Block | Error Name |
|------|-----------------|------------|-----------------|-----------|
| N-01 | … | … | … | … |

All four columns required.

---

### Format Rules

- Table format throughout. No prose substitutions for structural elements.
- Invariants must use `I-N` labels and appear in the "INVs Checked" column of every row.
- Race condition section must show both orderings explicitly.
- Omitted transitions: list any skipped transitions with rationale in a final table.

---

BEGIN. Finance Expert, open the trace.

---

---

## V-04 — Combination: Output Format + Hard Constraint + Symmetric Interleaving

**Axes combined**: Schema-level enforcement (C-14) · Hard no-prose declaration (C-16) · Explicit symmetric interleaving requirement (C-12)

**Hypothesis**: Combining structural schema enforcement with a named prose ban and an explicit symmetric-interleaving requirement closes the three most common aspirational-criteria gaps simultaneously without overloading prompt length.

---

You are a state-transition analyst. Produce a structured trace document for one domain: Sales pipeline, Customer Service ticket lifecycle, or Finance payment state machine.

---

**HARD RULE — NO PROSE SUBSTITUTIONS**

Every structural element of this trace must appear in a table cell. If you find yourself writing a paragraph where a table row belongs, stop and restructure. Narrative is permitted only in:
- The "Reason" column of the defect table
- The "Rationale" column of omitted transitions
- The invariant derivation notes

All other content must be structural. This rule is non-negotiable and applies even if a cell value would be brief.

---

### Invariant Declaration

Declare before filling any trace row:

| ID | Invariant | Business Rule Source |
|----|-----------|---------------------|
| I-1 | … | … |
| I-2 | … | … |

Minimum two. Must encode domain business rules. Generic structural facts (e.g., "record must have an ID") do not qualify.

---

### Main Trace

Column headers carry criterion IDs. Filling any cell in a column mechanically satisfies that criterion at the element level — no separate verification needed.

| Step [C-01a] | From [C-01b] | Operation [C-01c] | To [C-01d] | Pre [C-02a] | Post [C-02b] | Invariants [C-03: ≥2 per row] |
|---|---|---|---|---|---|---|
| 1 | New | SubmitQuote | UnderReview | RepAssigned=true; Amount>0 | InReviewQueue=true | I-1: Amount≥0 ✓; I-2: ValidStage ✓ |
| 2 | … | … | … | … | … | … |
| 3 | … | … | … | … | … | … |

> Row 1 is filled. Replace `…` with domain values. Do not collapse or omit any column.

---

### Defect Log

| ID | Type | Triggering Operation | State at Trigger | Reason |
|----|------|---------------------|-----------------|--------|
| D-01 | … | … | … | … |

Minimum one row. Types: `InvalidTransition` · `MissingPreconditionCheck` · `InvariantViolation` · `RaceCondition`

---

### Race Conditions — Symmetric Interleaving Required

**Writing one ordering and noting "the reverse is symmetric" does not satisfy this section.** Both orderings must be described with their results.

| Pair | Op-A | Op-B | Result when A executes first | Result when B executes first | Asymmetric? |
|------|------|------|---------------------------|---------------------------|-------------|
| RC-01 | … | … | … | … | Yes/No |

If results differ between orderings: name the conflict precisely. If results match: confirm idempotency for each ordering explicitly.

---

### Negative Path

| Step | State at Attempt | Blocked Operation | State After Block | Error Name |
|------|-----------------|-----------------|-----------------|-----------|
| N-01 | … | … | … | … |

---

### Omitted Transitions

| Transition Skipped | Rationale |
|-------------------|-----------|
| … | … |

Silent omissions do not qualify. Every skipped transition must have a named rationale.

---

### Invariant Derivation

After completing the trace, cite the rows that generated each declared invariant:

> I-1 [InvariantName] ← rows N, N, N — [one sentence explaining what the rows show]

One derivation note per declared invariant. Linkage must be explicit — "implied by the trace" does not qualify.

---

### Domain Expert Review

Sequence: Sales Expert → Finance Expert → Customer Service Expert

Each expert: (a) confirms domain plausibility of state names and operations, (b) flags or approves one non-trivial invariant, (c) signs off or escalates one item.

---

BEGIN. Declare invariants, fill all tables, complete expert review.

---

---

## V-05 — Combination: Role Sequence (CS-first) + Conversational Register + Invariant Derivation Pipeline

**Axes combined**: Role sequence (CS Expert leads) · Phrasing register (conversational) · Invariant derivation emphasis (C-13)

**Hypothesis**: A conversational register with named expert voices lowers generation friction for role-play sections while CS-first sequencing surfaces ticket-lifecycle edge cases that Sales-first prompts systematically under-trace. Explicit derivation framing in casual language maintains C-13 without sounding like a rubric recitation.

---

Let's hand-compile a state machine trace together. You're playing three domain experts who each care about getting state transitions right for their domain — and they each catch different problems.

Pick one domain to trace: **Sales pipeline**, **Customer Service ticket lifecycle**, or **Finance payment authorization**.

---

### Who's in the room

**The CS Expert goes first.** They live in ticket queues and SLA clocks. They know which transitions get support teams paged at 2am, and they'll declare the invariants that matter before anyone else touches the trace.

**The Sales Expert goes second.** They know deal stages, quota rules, and the race conditions that happen when two reps work the same account. Their job is to extend the trace *and* manufacture a concurrent-operation scenario.

**The Finance Expert goes last and is the strictest.** They won't sign off until the balance rules hold on every single row. They'll find the one invalid transition that slipped through and trace the rejection completely.

---

### What each expert does

**CS Expert — opens the trace**

1. State vocabulary: name every state your domain entity can be in. These are your nodes.
2. Invariant declaration — at least two, in plain language but specific:
   - Good: "A ticket in Resolved state cannot accept new comments without first being Reopened"
   - Too generic: "Every ticket must have an assigned ID"
3. Trace the first 4–5 operations, using this table:

| Step | From | Op | To | Pre | Post | Invariants |
|------|------|----|----|-----|------|-----------|
| ex | Open | Assign | InProgress | AgentAvailable=true | AssignedAgent≠null | I-1 ✓, I-2 ✓ |
| 1 | … | … | … | … | … | … |

The example row above is filled — it shows exactly what belongs in each cell. Replace the `…` rows with your domain trace.

**Sales Expert — extends and stress-tests**

1. Add 3+ rows to the same trace table for Sales-relevant operations
2. Then: pick two concurrent operations that Sales reps might perform simultaneously on the same deal. Walk through both orderings:
   - What happens when Rep-A moves first, then Rep-B?
   - What happens when Rep-B moves first, then Rep-A?
   
   Name the conflict if outcomes differ. Confirm idempotency if they match. Don't just describe one direction.

**Finance Expert — closes and defects**

1. Find one place in the trace where a precondition was skipped, an invalid transition slipped through, or an invariant broke. Document it:

   | Defect | Type | Triggering Op | State at Trigger | Reason |
   |--------|------|--------------|-----------------|--------|
   | D-01 | … | … | … | … |

2. Trace one rejected operation end-to-end — the negative path:

   | Step | State at Attempt | Blocked Op | State After Block | Error Name |
   |------|-----------------|------------|-----------------|-----------|
   | N-01 | … | … | … | … |

---

### After the trace — derivation pass

Once all three experts have contributed, do a quick derivation review. For each invariant you declared, look back at the trace rows and explain where that invariant came from:

> "I-1 came from rows 2 and 6 — both times we saw that if you skip the balance check before authorization, the invariant breaks. That's what generated the rule."

One note per invariant. The goal is to show the invariants weren't invented in advance — they were observed from the transitions and then formalized.

---

### Format note

Use the table for all structural content. No prose substitutions for trace rows, defects, or race conditions. Brief narrative is fine in the derivation pass and defect reasons — everywhere else, keep it in cells.

---

Ready? CS Expert, you're up. Name your domain, declare your states and invariants, and start the trace.

---

---

### Variation Summary

| Var | Primary Axis | New Criteria Targeted | Combination? |
|-----|-------------|----------------------|-------------|
| V-01 | Output format (schema + C-IDs + example row) | C-14, C-15, C-11, C-13 | No |
| V-02 | Lifecycle emphasis (explicit phase depth) | C-02, C-07, C-08, C-12 | No |
| V-03 | Role sequence (Finance-first rigor propagation) | C-07, C-03, C-12, C-09 | No |
| V-04 | Output format + Hard constraint + Symmetric interleaving | C-14, C-15, C-16, C-12, C-13 | Yes |
| V-05 | Role sequence (CS-first) + Conversational register + Derivation pipeline | C-13, C-15, C-16, C-12 | Yes |
