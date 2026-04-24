# trace-state Skill -- Quest Variations Round 1

**Skill**: trace-state
**Round**: 1 (first rubric, v1, 10 criteria)
**Rubric**: v1 (5 essential / 3 recommended / 2 aspirational, composite formula: E/5*60 + R/3*30 + A/2*10)
**R1 target**: All 10 criteria, no prior score to beat -- establish baseline golden

## Variation Map

| Variation | Axis | Primary Targets | Hypothesis |
|-----------|------|-----------------|------------|
| V-01 | Role sequence | C-07, C-05, C-04 | Role-first declaration forces domain vocabulary before structure |
| V-02 | Output format | C-01, C-02, C-03 | Per-operation table schema makes omission detectable as blank cell |
| V-03 | Lifecycle emphasis | C-04, C-06, C-08, C-09, C-10 | Explicit phases with gates convert optional criteria into mandatory stops |
| V-04 | Phrasing register (formal/technical) | C-02, C-05, C-08 | Mathematical predicate notation makes each criterion mechanically verifiable |
| V-05 | Role sequence + inertia framing | C-04, C-06, C-07 | Baseline-first framing makes invalid transitions and missing checks concrete deltas |

---

## V-01 -- Role Sequence

**Variation axis**: Role sequence -- the stock domain role is declared and instantiated before any
structural instruction. The analyst adopts the role identity first, then receives the trace
template. Every output element is produced by someone who already thinks in domain terms.

**Hypothesis**: When the model instantiates the domain expert persona before encountering the
technical structure, domain vocabulary (C-07) emerges by default rather than requiring a
post-hoc cleanup pass. Domain-grounded invariants (C-05) and domain-specific invalid transitions
(C-04) follow from the same commitment: the expert knows what the system *should not allow*
because they know how the domain actually works, not just what the spec says.

---

You are a **domain expert** in one of three fields. Choose the role that best fits the topic
you are tracing:

| Role | Domain | State Vocabulary Sample |
|------|--------|------------------------|
| Sales Expert | CRM opportunity pipeline | stage, qualify, commit, close_won, close_lost, forecast_category |
| Customer Service Expert | Case and ticket lifecycle | severity, escalate, assign, resolve, reopen, SLA_breach |
| Finance Expert | Ledger and transaction lifecycle | post, approve, reverse, reconcile, period_close, journal_entry |

**Declare your role now** -- one sentence, stating your role and the domain entity you are
tracing. All subsequent output uses domain verbs, domain state names, and domain invariants.
Generic terms like "update", "set field", or "record.status" are not permitted once your role
is declared.

---

You are running **trace-state** for Topic: `{Topic}`.

**Artifact to produce**: `simulations/trace/state/{topic}-state-{date}.md`

**Frontmatter** -- write at artifact top, update as each gate passes:

```yaml
---
topic: {Topic}
signal: state
date: {date}
role: [Sales Expert | Customer Service Expert | Finance Expert]
entity: [the specific domain entity being traced]
phase1_domain_committed: false
phase2_trace_complete: false
phase3_adversarial_complete: false
gate_final_passed: false
---
```

---

### Phase 1 -- Domain Setup (Role Owner)

State your role and entity. List the complete set of valid states for the entity being traced.
States must use domain names -- not generic status codes.

**State Inventory:**

| State ID | State Name (domain) | Meaning in domain |
|----------|--------------------|--------------------|
| S-01 | | |
| ... | | |

**Invariants** -- state at least two, expressed as boolean-checkable conditions:

| INV-ID | Invariant | Domain Grounding |
|--------|-----------|-----------------|
| INV-01 | | (why this must always hold in the domain) |
| INV-02 | | |

**GATE 1** (Role Owner):
- [ ] Role declared by name, domain entity named
- [ ] All valid states enumerated with domain names
- [ ] At least 2 invariants stated as checkable conditions, not goals
- [ ] No generic vocabulary in state names or invariant text

Set `phase1_domain_committed: true`. Phase 2 cannot begin until gate passes.

---

### Phase 2 -- Happy-Path Trace (Role Owner)

Trace the primary lifecycle of the entity from initial state to terminal state.
Every operation is recorded as a triple PLUS preconditions and postconditions.

For each operation, produce this block:

```
Operation N: {domain verb} ({operation name in domain language})
  Before:         {State ID and state name}
  Preconditions:  {field} == {value} [AND {field} == {value} ...]
  State Change:   {field}: {from_value} -> {to_value}  [list all changed fields]
  Postconditions: {field} == {value} [AND ...]
  Side Effects:   [events emitted, external calls -- or "none"]
  Invariant Check: INV-{id}: [{value} passes | {value} FAILS]
  After:          {State ID and state name}
```

Minimum 4 operations. Chain must be unbroken: the `After` state of operation N is the
`Before` state of operation N+1.

**GATE 2** (Role Owner):
- [ ] Every operation has a complete block (no omitted fields)
- [ ] Before/After chain is unbroken across all operations
- [ ] All preconditions reference domain state fields (not operation names restated)
- [ ] At least one invariant is tested per step

Set `phase2_trace_complete: true`. Phase 3 cannot begin until gate passes.

---

### Phase 3 -- Adversarial Analysis (Role Owner)

Identify at least one invalid transition: an operation that would be attempted but must be
rejected, stating the exact precondition that fails or invariant that would be violated.

**Invalid Transition:**

```
Attempted Operation: {domain verb}
  Attempted From:    {State ID}
  Reason Invalid:    precondition [{field} == {value}] not met -- actual value is [{actual}]
                     OR invariant INV-{id} would be violated because [{explain}]
  Guard Required:    [{what check would prevent this}]
```

Identify at least one missing precondition check: a precondition the system *should* verify
but currently assumes is satisfied by the caller.

**Missing Check:**

```
Operation:        {operation name}
Missing Check:    {what should be verified}
Current Behavior: caller assumes [{condition}] without enforcement
Risk:             [{what breaks if the assumption is violated}]
```

**GATE 3** (Role Owner):
- [ ] At least one invalid transition with explicit failing precondition or violated invariant
- [ ] At least one missing check with named risk
- [ ] Domain vocabulary maintained throughout

Set `phase3_adversarial_complete: true`.

---

### Phase 4 -- Concurrency Note (Role Owner, if applicable)

Select one operation from Phase 2. Analyze what happens if two actors attempt it simultaneously.

```
Operation at Risk:    {operation name}
Race Scenario:        Actor A reads [{field}={value}], Actor B reads [{field}={value}]
                      Actor A writes [{field}={new_value}], Actor B writes [{field}=other_value}]
Invariant at Risk:    INV-{id} -- [{how it breaks}]
Corrupted State:      [{describe the resulting illegal state}]
```

If no concurrency exposure exists for this topic, state why and label the section "N/A --
[reason]".

---

### GATE FINAL

- [ ] Role declared and maintained throughout (C-07)
- [ ] State transition chain unbroken, all triples complete (C-01)
- [ ] Preconditions present per operation, reference state fields (C-02)
- [ ] Postconditions present per operation, fields and values (C-03)
- [ ] At least one invalid transition identified (C-04)
- [ ] At least 2 invariants, at least one tested in trace (C-05)
- [ ] At least one missing check with risk (C-06)
- [ ] Race condition analysis present (C-08)

Set `gate_final_passed: true`.

---

## V-02 -- Output Format

**Variation axis**: Output format -- every operation is rendered using a strict 5-section
per-operation table. Omission is structurally detectable: a blank cell in any required column
fails the operation block. The chain integrity check is a mechanical diff of the After column
against the next row's Before column.

**Hypothesis**: When preconditions, postconditions, and the triple all live in the same
mandatory table schema, the model cannot satisfy the format without satisfying C-01, C-02,
and C-03 simultaneously. A blank cell in "Preconditions" is a format error, not a judgment
call. Chain integrity (C-01) is a row-to-row match check, not a narrative audit.

---

You are running **trace-state** for Topic: `{Topic}`.

Choose your stock role:
- **Sales Expert** (opportunity pipeline domain)
- **Customer Service Expert** (case/ticket lifecycle domain)
- **Finance Expert** (ledger/transaction domain)

**Artifact to produce**: `simulations/trace/state/{topic}-state-{date}.md`

**Frontmatter:**

```yaml
---
topic: {Topic}
signal: state
date: {date}
role: [declared role]
entity: [entity being traced]
operation_count: 0
invalid_transition_count: 0
invariant_count: 0
---
```

---

### Step 1 -- State and Invariant Inventory

List all valid states for the entity:

| S-ID | State Name | Description |
|------|------------|-------------|
| S-01 | | |

List all invariants (minimum 2):

| INV-ID | Invariant Expression | Domain Meaning |
|--------|---------------------|----------------|
| INV-01 | `{boolean expression}` | |
| INV-02 | `{boolean expression}` | |

---

### Step 2 -- Operation Trace (one table block per operation)

For every operation, fill in this exact table. No blank cells. Blank = fail.

**OP-{N}: {Operation Name}**

| Field | Value |
|-------|-------|
| Before | S-{id}: {state name} |
| Preconditions | `{field} == {value}` [AND ...] |
| Operation | {domain verb}: {what changes} |
| State Mutation | `{field}: {from} -> {to}` [one row per changed field] |
| Postconditions | `{field} == {value}` [AND ...] |
| Side Effects | [events / calls / "none"] |
| INV Check | INV-{id}: `{expression}` evaluates to [{TRUE / FALSE}] |
| After | S-{id}: {state name} |

**Chain Check after each operation**: After(OP-N) == Before(OP-N+1). State mismatch = chain break.

Minimum 4 operations. Update `operation_count` in frontmatter after each operation.

---

### Step 3 -- Invalid Transition Table

Identify at least one operation that must be rejected.

| # | Attempted OP | From State | Failing Precondition | Violated Invariant | Guard Required |
|---|-------------|------------|---------------------|--------------------|----------------|
| 1 | | S-{id} | `{field} == {actual}` fails check `{field} == {required}` | [INV-id or "none"] | |

Update `invalid_transition_count` in frontmatter.

---

### Step 4 -- Missing Check Table

| # | Operation | Missing Check | Current Assumption | Risk if Violated |
|---|-----------|---------------|-------------------|-----------------|
| 1 | | `{what should be verified}` | caller assumes `{condition}` | |

---

### Step 5 -- Invariant Test Summary

For each invariant, show at which operation(s) it was tested and whether it passed.

| INV-ID | Expression | Tested at OP | Result |
|--------|-----------|--------------|--------|
| INV-01 | | OP-{n} | PASS / FAIL |
| INV-02 | | OP-{n} | PASS / FAIL |

---

### Step 6 -- Race Condition Note

Select one operation. Describe concurrent execution risk:

| Field | Value |
|-------|-------|
| Operation | OP-{n}: {name} |
| Race Scenario | Two actors both read `{field}={value}`, one commits first |
| Invariant at Risk | INV-{id}: `{expression}` |
| Corrupted State | `{field}={wrong_value}` -- invariant now evaluates FALSE |

---

### Format Compliance Check (self-audit before writing artifact)

- [ ] Every OP block has 8 populated rows -- no blank cells (C-01, C-02, C-03)
- [ ] Chain check passes for all adjacent operations (C-01)
- [ ] Invalid transition table has at least 1 row (C-04)
- [ ] Invariant table has at least 2 rows, each tested in Step 5 (C-05)
- [ ] Missing check table has at least 1 row (C-06)
- [ ] Race condition table completed (C-08)
- [ ] All field values use domain vocabulary, not generic CRUD terms (C-07)

---

## V-03 -- Lifecycle Emphasis

**Variation axis**: Lifecycle emphasis -- the prompt is structured as six named phases with
explicit pass/fail gates. Each gate is a named criterion in the rubric. The model cannot
produce a valid artifact without passing each gate; skipping a phase is a gate failure.
The phases progress from least adversarial to most adversarial, with each phase building
on the previous one's committed output.

**Hypothesis**: When the rubric criteria are embedded as gate conditions rather than listed
as output expectations, the model cannot satisfy the format without satisfying the criteria.
C-04 (invalid transition) is not a hoped-for output -- it is GATE 3 and the artifact cannot
advance past it without a compliant entry. C-08, C-09, and C-10 become required GATE 5/6
outputs rather than optional depth items.

---

You are running **trace-state** for Topic: `{Topic}`.

Choose your stock role: **Sales Expert**, **Customer Service Expert**, or **Finance Expert**.

**Artifact to produce**: `simulations/trace/state/{topic}-state-{date}.md`

**Frontmatter:**

```yaml
---
topic: {Topic}
signal: state
date: {date}
role: [declared]
entity: [entity]
gate1_passed: false
gate2_passed: false
gate3_passed: false
gate4_passed: false
gate5_passed: false
gate6_passed: false
---
```

---

### Phase 1 -- Foundation (Scope + Invariants)

Establish the entity's state space and the invariants that govern it.

1. Declare your role and the entity being traced.
2. List all valid states (domain names, not codes).
3. State at least 2 invariants as boolean expressions -- not goals, not descriptions.
4. For each invariant, write the precise condition in code-like notation:
   `sum(debit_lines.amount) == sum(credit_lines.amount)` not "debits must balance credits".

**GATE 1 checklist:**
- [ ] Role declared
- [ ] State inventory complete (domain names)
- [ ] At least 2 invariants as boolean expressions (not aspirational statements)
- [ ] Invariants grounded in domain meaning (not implementation details)

Set `gate1_passed: true` or STOP and fix before continuing.

---

### Phase 2 -- Primary Trace (Happy Path)

Trace the entity through its main lifecycle from initial to terminal state.
Use this format for every operation:

```
OP-{n}: {domain verb}
  Before:        {S-id: state name}
  Pre:           {field == value [AND ...]}
  Changes:       {field: old_val -> new_val} [one line per changed field]
  Post:          {field == value [AND ...]}
  Events:        {emitted events or "none"}
  INV-{id}:      [{expression evaluates to TRUE / flags FALSE}]
  After:         {S-id: state name}
```

Chain rule: After(OP-n).state == Before(OP-n+1).state. Write "CHAIN OK" or "CHAIN BREAK --
[explain]" after each operation.

Minimum 4 operations.

**GATE 2 checklist:**
- [ ] Every operation has all 7 fields populated (C-01, C-02, C-03)
- [ ] Chain is unbroken (After == next Before, confirmed at each step)
- [ ] At least one invariant tested per operation
- [ ] Domain vocabulary used throughout -- no "update" or "set field"

Set `gate2_passed: true` or STOP and fix.

---

### Phase 3 -- Adversarial: Invalid Transitions

For at least one operation, describe an attempt that must be *rejected*.
State the exact failing precondition or invariant violation that makes it invalid.

```
INVALID ATTEMPT:
  Operation:   {domain verb}
  From State:  {S-id}
  Fails Because: precondition [{field == required}] not met -- actual [{field == actual}]
                 OR invariant [{INV-id: expression}] would evaluate FALSE after transition
  Guard Needed: [{the check that would prevent this}]
```

**GATE 3 checklist:**
- [ ] At least one invalid transition documented (C-04)
- [ ] Failing condition explicitly named (precondition or invariant, with values)
- [ ] Guard identified (what code would prevent the bad transition)

Set `gate3_passed: true` or STOP and fix.

---

### Phase 4 -- Missing Check Audit

Review Phase 2 operations. For at least one operation, identify a precondition the system
*should* verify but currently assumes is satisfied by the caller.

```
MISSING CHECK:
  Operation:        {op name}
  Assumed True:     {caller assumes this condition holds}
  Not Enforced By:  {layer that could enforce but does not -- API, service, DB constraint}
  Risk:             {what happens if a caller violates the assumption}
```

**GATE 4 checklist:**
- [ ] At least one missing check identified (C-06)
- [ ] The assumption is named (not just "needs validation")
- [ ] The risk is concrete (what breaks, what state becomes corrupted)

Set `gate4_passed: true` or STOP and fix.

---

### Phase 5 -- Concurrency Analysis

Select one operation from Phase 2. Trace what happens if two actors execute it simultaneously
without coordination. You are looking for race conditions that break invariants.

```
RACE ANALYSIS:
  Operation:        {OP-n: domain verb}
  Actor A sees:     {field == value} at T0
  Actor B sees:     {field == value} at T0
  Actor A commits:  {field: old -> new} at T1
  Actor B commits:  {field: old -> new} at T1 (stale read)
  Resulting State:  {field == corrupted_value}
  Invariant Break:  INV-{id}: {expression} now evaluates FALSE
```

**GATE 5 checklist:**
- [ ] At least one race scenario traced (C-08)
- [ ] Corrupted state is named explicitly
- [ ] Invariant that breaks is identified

Set `gate5_passed: true` or STOP and fix.

---

### Phase 6 -- Depth Extensions (aspirational -- attempt both)

**6A -- Severity Classification** (C-09)

For every invariant violation identified in Phases 3-5, assign severity:

| Violation | Invariant | Scenario | Severity | Rationale |
|-----------|-----------|----------|----------|-----------|
| | INV-{id} | | FATAL / DEGRADED / COSMETIC | |

- **FATAL**: data corruption, unrecoverable state, audit hole
- **DEGRADED**: feature broken, recoverable with intervention
- **COSMETIC**: display or reporting error only

**6B -- Alternate Path Trace** (C-10)

Trace at least one error path -- a sequence of 3+ steps showing how the system responds
to a rejected operation or failure and returns to a valid state.

```
ERROR PATH:
  Step 1: {operation attempted} from {S-id} -- REJECTED because {reason}
  Step 2: {compensating action} -- {field: old -> new}
  Step 3: {recovery operation} -- arrives at {S-id: recovery state}
  Recovery State Invariants: INV-{id} HOLDS, INV-{id} HOLDS
```

**GATE 6 checklist:**
- [ ] At least one severity classification per violation (C-09)
- [ ] At least one FATAL or DEGRADED classification present, or explain why none exist
- [ ] Alternate path traced with 3+ steps and named recovery state (C-10)

Set `gate6_passed: true`.

---

### Final Gate

All 6 gates must be marked `true` before writing the artifact.
Run the rubric score sheet as the final section of the artifact.

---

## V-04 -- Phrasing Register (Formal/Technical)

**Variation axis**: Phrasing register -- all preconditions, postconditions, and invariants
are expressed in formal predicate notation. State transitions are expressed as assignments.
Concurrency is analyzed as an interleaving scenario with explicit T0/T1/T2 timestamps.
Domain verbs are used but the *structure* of every expression is machine-checkable.

**Hypothesis**: Formal notation removes ambiguity from C-02, C-05, and C-08. A precondition
written as `opportunity.stage IN {QUALIFIED, PROPOSAL}` is unambiguously boolean-checkable
(C-02 passes). An invariant written as `pipeline.forecast_total == SUM(opportunity.amount WHERE
stage NOT IN {CLOSED_LOST})` is unambiguously testable (C-05 passes). A race condition expressed
as an interleaving table is unambiguously specific (C-08 passes).

---

You are running **trace-state** for Topic: `{Topic}`.

Choose your stock role: **Sales Expert**, **Customer Service Expert**, or **Finance Expert**.

**Artifact to produce**: `simulations/trace/state/{topic}-state-{date}.md`

**Notation conventions for this trace:**

| Notation | Meaning |
|----------|---------|
| `entity.field == value` | field equality check |
| `entity.field IN {v1, v2}` | membership check |
| `entity.field: old -> new` | state mutation |
| `NOT(expr)` | negation |
| `FORALL x IN collection: expr` | universal quantifier |
| `SUM(field WHERE condition)` | aggregate |
| `T0, T1, T2` | timestamps in concurrency scenarios |

All preconditions, postconditions, and invariants MUST use this notation.
Prose descriptions may follow but are not substitutes.

**Frontmatter:**

```yaml
---
topic: {Topic}
signal: state
date: {date}
role: [declared]
entity: [entity]
notation: formal-predicate
---
```

---

### Section 1 -- State Space Declaration

```
ENTITY: {entity name}
VALID_STATES = {S-01: name, S-02: name, ...}
TERMINAL_STATES = {S-0n: name, ...}  // states from which no further ops are permitted
```

**Invariants** (formal notation required):

```
INV-01: {predicate expression}
        Domain meaning: {one sentence}

INV-02: {predicate expression}
        Domain meaning: {one sentence}
```

---

### Section 2 -- Operation Trace

For each operation, use this exact structure:

```
OP-{n}: {domain verb}
  PRE:   {predicate} [AND {predicate} ...]
  DELTA: {entity.field: old_value -> new_value}
         {entity.field: old_value -> new_value}  // one line per changed field
  POST:  {predicate} [AND {predicate} ...]
  FX:    {EventEmitted(payload) | ExternalCall(endpoint) | NONE}
  INV:   INV-{id}: {expression} = {TRUE | FALSE -- [explain if FALSE]}
  CHAIN: {entity.state} == {next_op_pre_state} [CHAIN OK | CHAIN BREAK]
```

Prose annotation after each block is permitted but cannot replace any field.

Minimum 4 operations.

---

### Section 3 -- Invalid Transition (formal)

```
INVALID OP-{n}: {domain verb}
  ATTEMPTED FROM: {entity.state == S-id}
  PRE FAILS:  {precondition predicate} -- evaluates FALSE because {entity.field == actual_value}
              OR INV VIOLATED: {invariant predicate} would evaluate FALSE post-transition
  GUARD:      ASSERT {precondition predicate} BEFORE allowing transition
```

---

### Section 4 -- Missing Check (formal)

```
MISSING CHECK in OP-{n}: {operation name}
  CALLER ASSUMES: {predicate} == TRUE
  NOT ENFORCED:   no assertion in {layer -- service | API | DB}
  RISK:           IF {predicate} == FALSE THEN {entity reaches illegal state S-id}
                  INV-{id} would evaluate: FALSE
```

---

### Section 5 -- Concurrency Interleaving

```
RACE IN OP-{n}: {domain verb}
  T0: Actor-A reads {entity.field == v1}
  T0: Actor-B reads {entity.field == v1}
  T1: Actor-A writes {entity.field: v1 -> v2}  -- commits
  T1: Actor-B writes {entity.field: v1 -> v3}  -- commits (stale, overwrites A)
  POST-RACE: {entity.field == v3}  // Actor-A's write lost
  INV CHECK: INV-{id}: {expression} evaluates FALSE because {explain}
  SEVERITY: [FATAL | DEGRADED | COSMETIC] -- {rationale}
```

---

### Section 6 -- Invariant Violation Severity Table

| INV-ID | Predicate | Violating Scenario | Severity | Recovery Path |
|--------|-----------|--------------------|----------|---------------|
| INV-01 | `{expr}` | | FATAL / DEGRADED / COSMETIC | |
| INV-02 | `{expr}` | | | |

---

### Section 7 -- Alternate Path (error recovery)

```
ERROR PATH: {description of failure trigger}
  Step 1: ATTEMPT {OP-n} from {entity.state == S-id}
          RESULT: REJECTED -- PRE({predicate}) == FALSE
  Step 2: {compensating domain verb}
          DELTA: {entity.field: old -> new}
  Step 3: {recovery domain verb}
          POST: {entity.state == S-recovery}
          INV CHECK: INV-{id} == TRUE, INV-{id} == TRUE
  RECOVERY STATE: {entity.state == S-recovery} -- valid, all invariants hold
```

---

### Formal Compliance Check

- [ ] All PRE/POST/INV fields use formal predicate notation (no prose-only)
- [ ] DELTA uses assignment notation `field: old -> new`
- [ ] CHAIN check written at every operation
- [ ] INV checks show evaluated truth value, not just "holds"
- [ ] Race scenario uses T0/T1 timestamp notation
- [ ] Severity assigned to every violation

---

## V-05 -- Role Sequence + Inertia Framing

**Variation axis**: Role sequence combined with inertia framing -- the trace opens with a
baseline description of what the *current system* already does for this entity lifecycle.
Invalid transitions (C-04) and missing checks (C-06) are identified as deltas from that
baseline: places where the proposed behavior *differs from* or *tightens* what exists today.

**Hypothesis**: When the analyst first commits to "what the current system does," invalid
transitions become concrete: the current system *allows* operation X but the new behavior
*rejects* it (or vice versa). Missing checks become concrete: the current system *assumes*
condition Y without verifying it because that was acceptable before, but is now a gap. Role
identity reinforces this framing -- a domain expert knows both current behavior and required
behavior, and can articulate the delta precisely. C-04 and C-06 pass because the analyst
has a named baseline to reason against, not just an abstract spec.

---

You are running **trace-state** for Topic: `{Topic}`.

Choose your stock role: **Sales Expert**, **Customer Service Expert**, or **Finance Expert**.

**Artifact to produce**: `simulations/trace/state/{topic}-state-{date}.md`

**Frontmatter:**

```yaml
---
topic: {Topic}
signal: state
date: {date}
role: [declared]
entity: [entity]
baseline_committed: false
trace_complete: false
delta_analysis_complete: false
---
```

---

### Phase 0 -- Baseline Commitment (Role Owner)

Before tracing the proposed behavior, declare what the current system does for this entity.
This is the *inertia baseline* -- the behavior that exists today and that any new design
must consciously depart from.

**Current System Baseline:**

| Aspect | What Current System Does |
|--------|--------------------------|
| States supported | [list current valid states] |
| Transitions allowed | [which ops are currently permitted] |
| Precondition checks enforced | [what the current system actually checks before allowing ops] |
| Invariants the current system maintains | [properties that currently hold] |
| Known gaps in current system | [checks assumed but not enforced today] |

**GATE 0** (Role Owner):
- [ ] Role declared
- [ ] Baseline describes current behavior, not aspirational behavior
- [ ] At least one current gap identified (precondition assumed but not enforced)
- [ ] Baseline committed from domain knowledge, not from the spec

Set `baseline_committed: true`. This baseline is now locked -- it cannot be revised to match
the proposed behavior discovered later.

---

### Phase 1 -- Proposed State Trace

Trace the proposed entity lifecycle. Format every operation as a triple-plus block:

```
OP-{n}: {domain verb}
  Before:        {S-id: state name}
  Preconditions: {field == value} [AND ...]  -- include checks that did NOT exist in baseline
  Changes:       {field: old -> new}
  Postconditions:{field == value} [AND ...]
  Side Effects:  {events or "none"}
  INV Check:     INV-{id}: {expression} = [TRUE | FALSE]
  After:         {S-id: state name}
  Baseline Delta: [SAME AS CURRENT | NEW CHECK: {what was added} | REMOVED CHECK: {what was dropped}]
```

The `Baseline Delta` field is required. If the proposed operation is identical to the current
system, write "SAME AS CURRENT." If it tightens or changes preconditions, name the delta.

Minimum 4 operations.

**GATE 1** (Role Owner):
- [ ] All 8 fields populated per operation (including Baseline Delta)
- [ ] Chain unbroken (After == next Before)
- [ ] At least one operation has a non-trivial Baseline Delta
- [ ] Domain vocabulary used throughout

Set `trace_complete: true`.

---

### Phase 2 -- Invariants

State at least 2 invariants. For each, note whether the current system already maintains it
or whether it is new to the proposed behavior.

| INV-ID | Expression | Current System | Proposed Behavior |
|--------|-----------|----------------|------------------|
| INV-01 | `{predicate}` | MAINTAINED / NOT MAINTAINED | REQUIRED |
| INV-02 | `{predicate}` | MAINTAINED / NOT MAINTAINED | REQUIRED |

Test each invariant against at least one operation in Phase 1. Write `INV-{id}: HOLDS at OP-{n}` or
`INV-{id}: FAILS at OP-{n} -- [explain]`.

---

### Phase 3 -- Delta Analysis (Invalid Transitions + Missing Checks)

This phase identifies where the proposed behavior *differs from* the baseline in ways that
require explicit guarding.

**Invalid Transitions -- delta from baseline:**

| # | Operation | From State | Current System | Proposed Behavior | Why Now Invalid |
|---|-----------|------------|---------------|------------------|-----------------|
| 1 | {domain verb} | S-{id} | allows without check | rejects because {precondition fails} | {domain reason} |

**Missing Checks -- carried forward from baseline:**

| # | Operation | Gap | Baseline Assumed | Proposed Fix Needed | Risk if Unfixed |
|---|-----------|-----|-----------------|---------------------|-----------------|
| 1 | | | `{condition}` assumed true | ASSERT `{condition}` before allowing | |

**GATE 3** (Role Owner):
- [ ] At least one invalid transition with explicit precondition failure (C-04)
- [ ] At least one missing check with baseline origin and risk (C-06)
- [ ] Delta column populated for all transitions in phase 1

Set `delta_analysis_complete: true`.

---

### Phase 4 -- Concurrency + Severity (aspirational)

**Race Condition** -- select one operation, trace simultaneous execution:

```
RACE: OP-{n}: {domain verb}
  Two actors both read {field == value}
  Actor A commits {field: v -> v2}
  Actor B commits {field: v -> v3} (stale, overwrites A)
  Invariant Break: INV-{id} now FALSE -- {explain}
  Baseline Comparison: current system [had same risk | added new risk | mitigated this]
```

**Severity Classification** -- for every invariant violation found:

| Violation | Invariant | Severity | Rationale |
|-----------|-----------|----------|-----------|
| | INV-{id} | FATAL / DEGRADED / COSMETIC | |

---

### Phase 5 -- Alternate Path (aspirational)

Trace a 3+ step error path showing recovery to a valid state. Frame it as a delta from
what the current system would do in the same failure scenario.

```
ERROR PATH: {trigger}
  Current System Response: [what current system does]
  Proposed Response:
    Step 1: {attempted op} REJECTED -- {reason}
    Step 2: {compensating op} -- {field: old -> new}
    Step 3: {recovery op} -- arrives at {S-id: recovery state}
  Invariants at Recovery: INV-{id} HOLDS, INV-{id} HOLDS
  Delta from Current: [SAME | IMPROVED RECOVERY | NEW FAILURE MODE]
```

---

### Final Self-Check

- [ ] Baseline committed before trace started (C-07 framing)
- [ ] Baseline Delta populated per operation (supports C-04, C-06)
- [ ] State chain unbroken (C-01)
- [ ] Preconditions reference state fields (C-02)
- [ ] Postconditions name changed fields and values (C-03)
- [ ] At least one invalid transition with delta framing (C-04)
- [ ] At least 2 invariants tested in trace (C-05)
- [ ] At least one missing check with baseline origin (C-06)
- [ ] Domain vocabulary throughout (C-07)
- [ ] Race condition traced (C-08)
