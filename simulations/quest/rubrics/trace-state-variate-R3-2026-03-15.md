# trace-state Skill -- Quest Variations Round 3

**Skill**: trace-state
**Round**: 3 (building on R1 V-05 base ~94 composite under v3; rubric v3, 8 aspirationals)
**Rubric**: v3 (C-01--C-16; composite = E/5*60 + R/3*30 + A/8*10)
**R3 target gaps**: C-14 (pre-trace vocabulary declaration block), C-15 (post-trace vocabulary audit), C-16 (predicate-vocabulary cross-reference)

---

## Variation Map

| V | Axis | Primary Targets | Key Structural Change |
|---|------|-----------------|-----------------------|
| V-01 | Output format | C-14 | Vocabulary declaration appears as a mandatory fillable template BEFORE Phase 1; blank cells = format failure |
| V-02 | Lifecycle emphasis | C-14, C-15 | Phase 0 (Vocabulary Gate) blocks Phase 1 from opening; final phase adds Vocabulary Audit as mandatory exit gate |
| V-03 | Phrasing register | C-14, C-16 | Every predicate carries a `[->DECL: entity.field]` citation annotation; declaration must exist to cite against |
| V-04 | Compound (output + lifecycle) | C-14, C-15 | V-01 declaration template + V-02 gate structure combined; both declaration and audit are structurally gated |
| V-05 | Compound (output + lifecycle + phrasing) | C-14, C-15, C-16 | V-04 + V-03 citation annotations + MUST/BLOCKED/ADVANCE imperative markers + post-trace audit maps each predicate's `[->DECL]` citation back to the declaration row |

**Single-axis hypotheses tested:**

- **V-01 vs V-02**: Does providing a declaration template (structural completability) achieve C-14 better than making the declaration a lifecycle gate (mandatory stop)? Template says "fill this in"; gate says "you cannot proceed until this exists." Two different enforcement mechanisms for the same criterion.
- **V-02 vs V-03**: Does lifecycle gating (V-02) or citation annotation syntax (V-03) better elicit C-14 as a real pre-trace artifact? V-03 makes the declaration a prerequisite via reference (you can't cite what doesn't exist); V-02 makes it a prerequisite via sequencing.
- **V-03 single**: Does the `[->DECL]` citation annotation produce C-16 (predicate-vocabulary cross-reference) as a side effect of producing correctly annotated predicates?

---

## V-01 -- Output Format (Vocabulary Declaration Template)

**Variation axis**: Output format -- the prompt contains a mandatory vocabulary declaration
template that appears *before* the first operation block. The template has exact named columns
for entities, fields, and operations (with the generic-verb equivalent explicitly noted per
operation). A row in any required column left blank is a format error equivalent to omitting
the entire section.

**Hypothesis**: C-14 requires the declaration as an artifact, not merely correct vocabulary.
The most direct mechanism is a fillable structural template placed before Phase 1. When the
model must populate entity names, field names, and operation names (with generic replacements
labeled inline), it produces the C-14 declaration as a form completion rather than as a
voluntary annotation. The table schema also serves C-07: a column named "generic verb
replaced" makes domain-vocabulary enforcement visible in the output structure itself.

**Target**: C-14 primary. C-07 (domain vocabulary) reinforced via the generic-verb column.
C-16 partial -- declared fields exist; predicate citation is not yet mandated.

---

You are running **trace-state** for Topic: `{Topic}`.

Choose your stock role:
- **Sales Expert** -- opportunity pipeline domain
- **Customer Service Expert** -- case and ticket lifecycle domain
- **Finance Expert** -- ledger and transaction lifecycle domain

**Artifact to produce**: `simulations/trace/state/{topic}-state-{date}.md`

**Frontmatter:**

```yaml
---
topic: {Topic}
signal: state
date: {date}
role: [Sales Expert | Customer Service Expert | Finance Expert]
entity: [the specific domain entity being traced]
vocab_declaration_complete: false
trace_complete: false
adversarial_complete: false
---
```

---

### VOCABULARY DECLARATION

**Complete this section before writing any operation block. A vocabulary declaration with
any required cell blank is a format failure. Do not begin Phase 1 until all rows are filled.**

#### Entity and Field Declaration

| Entity Name | Field Name | Field Type | Valid Values / Range |
|-------------|------------|------------|----------------------|
| | | | |
| | | | |
| | | | |

*(Add one row per field per entity. Every field that will appear in a precondition,
postcondition, or invariant must be declared here.)*

#### Operation Declaration

| Operation Name (domain verb) | Generic Verb Replaced | Acts On Entity | Primary Field Changed |
|------------------------------|-----------------------|----------------|-----------------------|
| | [e.g., "create", "update", "delete"] | | |
| | | | |
| | | | |

*(Add one row per operation that will appear in the trace. The "Generic Verb Replaced" column
is required -- write the generic CRUD term this domain verb replaces. If no generic verb
applies, write "none -- domain-only operation.")*

**Vocabulary Declaration Checklist:**
- [ ] All entities named in the Entity and Field table
- [ ] All fields that will appear in predicates declared with valid values
- [ ] All operations declared with generic verb replacement noted
- [ ] No cell in the declaration table is blank

Set `vocab_declaration_complete: true`. **Phase 1 cannot begin until this is set.**

---

### Phase 1 -- State Inventory and Invariants

Declare all valid states for the entity. Use domain names from the Vocabulary Declaration.

| S-ID | State Name | Domain Meaning |
|------|------------|----------------|
| S-01 | | |
| S-02 | | |

State at least 2 invariants. Use formal predicate notation (`entity.field OPERATOR value`).
All field names must match the Vocabulary Declaration -- do not introduce new field names here.

| INV-ID | Invariant Expression | Domain Grounding |
|--------|----------------------|------------------|
| INV-01 | `{predicate using declared field names}` | |
| INV-02 | `{predicate using declared field names}` | |

---

### Phase 2 -- Happy-Path Operation Trace

Trace the entity lifecycle from initial state to terminal state. Every operation block is
required -- no fields may be omitted. Use only field names and operation names from the
Vocabulary Declaration.

For each operation:

```
OP-{n}: {operation name from Vocabulary Declaration}
  Before:         {S-id: state name}
  Preconditions:  {entity.field OPERATOR value} [AND ...]
  State Change:   {entity.field: from_value -> to_value}  [one line per changed field]
  Postconditions: {entity.field OPERATOR value} [AND ...]
  Side Effects:   [event emitted or external call -- or "none"]
  INV Check:      INV-{id}: {expression} = [TRUE | FALSE -- explain if FALSE]
  After:          {S-id: state name}
```

**Chain check after each operation**: After(OP-N) must equal Before(OP-N+1). Write
"CHAIN OK" or "CHAIN BREAK -- [explain]" immediately after each operation block.

Minimum 4 operations.

---

### Phase 3 -- Invalid Transition Analysis

Identify at least one operation that must be rejected from the current state.

```
INVALID OP: {operation name from Vocabulary Declaration}
  Attempted From:  {entity.state == S-id}
  Fails Because:   {entity.field OPERATOR required_value} -- actual: {entity.field == actual}
                   OR INV-{id}: {expression} would evaluate FALSE post-transition
  Guard Required:  ASSERT {precondition predicate} before permitting transition
```

Express each invalid transition in delta form:
`(baseline_state, attempted_delta, failure_reason)` where `failure_reason` names the
specific precondition field or invariant from the Vocabulary Declaration.

---

### Phase 4 -- Missing Precondition Check Audit

For at least one operation, identify a precondition that the system *should* verify but
currently assumes is satisfied by the caller.

```
MISSING CHECK in OP-{n}: {operation name}
  Caller Assumes:  {entity.field OPERATOR value} without enforcement
  Not Checked By:  {service | API | database constraint}
  Risk:            IF {entity.field == violating_value} THEN {illegal state or invariant break}
```

---

### Phase 5 -- Concurrency / Race Condition Analysis

Select one operation from Phase 2. Analyze concurrent execution risk.

```
RACE SCENARIO for OP-{n}: {operation name}
  | Time | Actor A | Actor B |
  |------|---------|---------|
  | T0   | reads {entity.field == v} | reads {entity.field == v} |
  | T1   | writes {entity.field: v -> v2} | writes {entity.field: v -> v3} |
  | T2   | -- | commits (stale, overwrites A) |
  Post-race state: {entity.field == v3}
  Invariant break: INV-{id}: {expression} evaluates FALSE because {explain}
```

If no concurrency exposure exists, state the reason explicitly.

---

### Phase 6 -- Severity and Alternate Path (aspirational)

**6A -- Invariant Violation Severity**

| Violation | Invariant | Scenario | Severity | Rationale |
|-----------|-----------|----------|----------|-----------|
| | INV-{id} | | FATAL / DEGRADED / COSMETIC | |

- **FATAL**: data corruption, unrecoverable state
- **DEGRADED**: feature broken, recoverable with intervention
- **COSMETIC**: display or reporting error only

**6B -- Alternate Path (3+ steps)**

```
ERROR PATH: {trigger}
  Step 1: {op attempted} from {S-id} -- REJECTED: {reason citing declared field}
  Step 2: {compensating domain verb} -- {field: old -> new}
  Step 3: {recovery domain verb} -- arrives at {S-id: recovery state}
  Recovery invariants: INV-{id} HOLDS, INV-{id} HOLDS
```

---

### Compliance Self-Check

- [ ] Vocabulary Declaration completed before first operation block (C-14)
- [ ] All operation names in trace match Vocabulary Declaration (C-07 via declaration)
- [ ] All field names in predicates match Vocabulary Declaration (C-16 partial)
- [ ] State chain unbroken (C-01)
- [ ] Preconditions reference declared fields (C-02)
- [ ] Postconditions name changed fields and values (C-03)
- [ ] At least one invalid transition with delta framing (C-04)
- [ ] At least 2 invariants tested (C-05)
- [ ] At least one missing check with risk (C-06)
- [ ] Race condition traced (C-08)

---

## V-02 -- Lifecycle Emphasis (Vocabulary Gate + Audit Gate)

**Variation axis**: Lifecycle emphasis -- the trace is divided into seven named phases.
Phase 0 is the Vocabulary Gate: it must be marked complete before Phase 1 opens. The final
phase is the Vocabulary Audit: it is a required exit gate that must be completed before the
artifact is written to disk. Skipping either phase is a structural failure.

**Hypothesis**: C-14 requires the declaration as a *pre-trace* artifact (before the first
triple). Making Phase 0 a blocking lifecycle gate forces the declaration to be temporally
positioned correctly -- the model cannot defer it to after the trace. C-15 requires the
audit as *post-trace* evidence that the detection loop ran. Making the Vocabulary Audit
a final exit gate forces it to be produced. The audit's function (mapping each operation
used to its declaration entry) is spelled out as a gate requirement, not left implicit.

**Target**: C-14 (Phase 0 as blocking gate), C-15 (final Vocabulary Audit as exit gate).
C-07 reinforced throughout by both gates referencing domain-vocabulary requirements.

---

You are running **trace-state** for Topic: `{Topic}`.

Choose your stock role:
- **Sales Expert** -- opportunity pipeline domain
- **Customer Service Expert** -- case and ticket lifecycle domain
- **Finance Expert** -- ledger and transaction lifecycle domain

**Artifact to produce**: `simulations/trace/state/{topic}-state-{date}.md`

**Frontmatter:**

```yaml
---
topic: {Topic}
signal: state
date: {date}
role: [Sales Expert | Customer Service Expert | Finance Expert]
entity: [entity being traced]
phase0_vocab_gate: false
phase1_inventory_gate: false
phase2_trace_gate: false
phase3_adversarial_gate: false
phase4_concurrency_gate: false
phase5_depth_gate: false
phase_final_audit_gate: false
---
```

---

### Phase 0 -- Vocabulary Gate

**This phase is BLOCKED until all checklist items pass. Phase 1 cannot open until
`phase0_vocab_gate: true` is set.**

Declare your role and the domain entity being traced. Then produce the three vocabulary
tables below. These tables define the complete token set this trace will generate against.
No field name, entity name, or operation name may appear in Phases 1-5 unless it is
first declared here.

**Entity Declaration:**

| Entity Name | Description | Primary Key Field |
|-------------|-------------|-------------------|
| | | |

**Field Declaration:**

| Entity | Field Name | Type | Valid Values / Constraints |
|--------|------------|------|---------------------------|
| | | | |
| | | | |

**Operation Declaration:**

| Operation Name (domain verb) | Generic Equivalent (prohibited) | Target Entity | Precondition Fields |
|------------------------------|---------------------------------|---------------|---------------------|
| | | | |
| | | | |

*(The "Generic Equivalent" column names the CRUD term this domain verb replaces. This column
is required. An entry of "none" is acceptable only for operations with no generic equivalent.)*

**Phase 0 Gate Checklist:**
- [ ] Role and entity declared in one sentence
- [ ] All entities named in Entity Declaration
- [ ] All fields that will appear in any predicate declared in Field Declaration
- [ ] All operations that will appear in the trace declared in Operation Declaration
- [ ] Generic-verb equivalents noted for every operation
- [ ] No declaration cell is blank

Set `phase0_vocab_gate: true`. **Phase 1 is BLOCKED until this is set.**

---

### Phase 1 -- State Inventory and Invariants

List all valid states for the entity (domain names from Phase 0 vocabulary only):

| S-ID | State Name | Is Terminal? | Description |
|------|------------|--------------|-------------|
| S-01 | | yes / no | |

State at least 2 invariants as boolean-checkable expressions. Field names must be drawn
from the Phase 0 Field Declaration:

| INV-ID | Expression | Domain Meaning | Severity if Violated |
|--------|-----------|----------------|----------------------|
| INV-01 | `{predicate}` | | FATAL / DEGRADED / COSMETIC |
| INV-02 | `{predicate}` | | |

**Phase 1 Gate Checklist:**
- [ ] All valid states enumerated with domain names
- [ ] At least 2 invariants as checkable predicates (not goals)
- [ ] All field names in invariants match Phase 0 Field Declaration
- [ ] Severity classification assigned per invariant

Set `phase1_inventory_gate: true`.

---

### Phase 2 -- Happy-Path Trace

Trace the entity lifecycle from initial state to terminal state. Every operation uses
only vocabulary from Phase 0. Format each operation as a triple-plus block:

```
OP-{n}: {operation from Phase 0 Operation Declaration}
  Before:         {S-id: state name}
  Preconditions:  {entity.field OPERATOR value} [AND ...]
  State Change:   {entity.field: from_value -> to_value}
  Postconditions: {entity.field OPERATOR value} [AND ...]
  Side Effects:   [events / calls / "none"]
  INV Check:      INV-{id}: {predicate} = [TRUE | FALSE -- explain if FALSE]
  After:          {S-id: state name}
  CHAIN:          After(OP-{n}) == Before(OP-{n+1}): [CHAIN OK | CHAIN BREAK -- explain]
```

Minimum 4 operations.

**Phase 2 Gate Checklist:**
- [ ] Every operation has all 8 fields populated
- [ ] Chain check written after each operation
- [ ] All operation names match Phase 0 Operation Declaration
- [ ] All field names in predicates match Phase 0 Field Declaration
- [ ] At least one INV check per operation

Set `phase2_trace_gate: true`.

---

### Phase 3 -- Adversarial Analysis

**Invalid Transition (at least one):**

```
INVALID ATTEMPT: {operation name from Phase 0}
  Attempted From:  {S-id: state name}
  Fails Because:   {entity.field OPERATOR required} -- actual: {entity.field == actual}
                   OR INV-{id}: {expression} would evaluate FALSE
  Guard Required:  ASSERT {predicate} before allowing transition
  Delta Form:      (baseline={S-id}, attempted={op}, failure={field or invariant name})
```

**Missing Precondition Check (at least one):**

```
MISSING CHECK in OP-{n}: {operation from Phase 0}
  Assumed True:   {entity.field OPERATOR value} without verification
  Not Enforced:   {layer}
  Risk:           {concrete failure mode naming invariant or illegal state}
```

**Phase 3 Gate Checklist:**
- [ ] At least one invalid transition with explicit delta form
- [ ] At least one missing check with concrete risk statement
- [ ] Domain vocabulary (Phase 0 operation and field names) maintained throughout

Set `phase3_adversarial_gate: true`.

---

### Phase 4 -- Concurrency Analysis

Select one operation. Render the race condition as a T0/T1 interleaving table:

| Time | Actor A | Actor B |
|------|---------|---------|
| T0 | reads `{entity.field == v}` | reads `{entity.field == v}` |
| T1 | writes `{entity.field: v -> v2}` | writes `{entity.field: v -> v3}` (stale) |
| T2 | -- | **INVARIANT BREAK** |

```
Post-race: {entity.field == v3}
INV-{id}: {predicate} evaluates FALSE -- {explain}
Severity: FATAL / DEGRADED / COSMETIC
```

**Phase 4 Gate Checklist:**
- [ ] T0/T1 interleaving table present with at least 4 rows
- [ ] Row where invariant breaks is explicitly marked
- [ ] Named invariant and broken predicate identified

Set `phase4_concurrency_gate: true`.

---

### Phase 5 -- Depth Extensions (aspirational)

**Alternate Error Path (3+ steps):**

```
ERROR PATH: {trigger description}
  Step 1: ATTEMPT {op} from {S-id} -- REJECTED: {predicate} == FALSE
  Step 2: {compensating domain verb} -- {field: old -> new}
  Step 3: {recovery domain verb} -- arrives at {S-id: recovery state}
  Recovery: INV-{id} HOLDS, INV-{id} HOLDS
```

Set `phase5_depth_gate: true` if completed; mark N/A with reason if not applicable.

---

### Phase FINAL -- Vocabulary Audit

**This phase is REQUIRED. The artifact cannot be written to disk until
`phase_final_audit_gate: true` is set.**

For every distinct operation name used in Phases 2-5, map it to its Phase 0 Operation
Declaration entry. Flag any operation used but not declared.

| Operation Used | Phase(s) Used | Phase 0 Declaration Entry | Status |
|----------------|---------------|--------------------------|--------|
| | OP-{n} | [matches Phase 0 row: "{operation name}"] | DECLARED / **NOT DECLARED -- FLAG** |
| | | | |

For every generic CRUD verb that appears in any operation name in the trace, flag it:

| Generic Verb Found | Location (OP-n) | Required Domain Replacement | Action Taken |
|--------------------|----------------|----------------------------|--------------|
| [none OR list each] | | [from Phase 0 declaration] | REPLACED / STILL PRESENT -- CORRECT NOW |

**Vocabulary Audit Gate Checklist:**
- [ ] Every operation name used in trace has a Phase 0 declaration row
- [ ] No undeclared operation names remain (or corrections applied)
- [ ] No generic CRUD verbs in any operation name (or corrections applied)
- [ ] Audit table populated -- not a statement that vocabulary is clean

Set `phase_final_audit_gate: true`.

---

### Scoring Checklist

All phase gates must be `true` before the artifact is written.

- [ ] `phase0_vocab_gate: true` (C-14)
- [ ] `phase1_inventory_gate: true` (C-01, C-05)
- [ ] `phase2_trace_gate: true` (C-01, C-02, C-03)
- [ ] `phase3_adversarial_gate: true` (C-04, C-06)
- [ ] `phase4_concurrency_gate: true` (C-08, C-12)
- [ ] `phase5_depth_gate: true` (C-10)
- [ ] `phase_final_audit_gate: true` (C-15)

---

## V-03 -- Phrasing Register (Cross-Reference Annotation)

**Variation axis**: Phrasing register -- every predicate condition (`entity.field OPERATOR
value`) carries a mandatory citation annotation `[->DECL: EntityName.fieldName]` immediately
after it. The annotation names the Vocabulary Declaration entry the field is drawn from.
A predicate without a citation annotation is a notation violation equivalent to a missing
predicate.

**Hypothesis**: C-16 is a compound property requiring C-11 (predicate notation) and C-14
(vocabulary declaration). The hardest gap to enforce is the *cross-reference* itself -- that
predicate field names are drawn from the declaration rather than invented ad hoc. The
`[->DECL]` annotation makes this cross-reference explicit and auditable: a reviewer can
confirm each annotation without interpretation. As a side effect, the citation requirement
forces the vocabulary declaration to exist (so there is something to cite), which drives
C-14. The annotation also makes domain-vocabulary drift immediately visible: a predicate
citing `[->DECL: Record.status]` is self-evidencing of a generic-term failure.

**Target**: C-16 primary (cross-reference enforcement). C-14 as prerequisite (declaration
must exist to cite). C-11 reinforced (predicate notation required for annotation to apply).

---

You are running **trace-state** for Topic: `{Topic}`.

Choose your stock role:
- **Sales Expert** -- opportunity pipeline domain
- **Customer Service Expert** -- case and ticket lifecycle domain
- **Finance Expert** -- ledger and transaction lifecycle domain

**Artifact to produce**: `simulations/trace/state/{topic}-state-{date}.md`

**Notation convention for this trace:**

All predicate conditions use the following citation-annotated syntax:

```
{entity.field OPERATOR value} [->DECL: EntityName.fieldName]
```

The `[->DECL]` annotation names the Vocabulary Declaration entry the field is drawn from.
It appears immediately after the predicate expression it annotates. A predicate without a
`[->DECL]` annotation is a notation failure. Example:

```
opportunity.stage IN {QUALIFIED, PROPOSAL} [->DECL: Opportunity.stage]
AND opportunity.owner_id != NULL [->DECL: Opportunity.owner_id]
```

**Mutation notation:**

```
{entity.field: old_value -> new_value} [->DECL: EntityName.fieldName]
```

**Frontmatter:**

```yaml
---
topic: {Topic}
signal: state
date: {date}
role: [Sales Expert | Customer Service Expert | Finance Expert]
entity: [entity being traced]
notation: formal-predicate-with-decl-citation
vocab_declaration_present: false
---
```

---

### Section 0 -- Vocabulary Declaration

**Produce this section first. Every field that will appear in a `[->DECL]` annotation
must be declared here. An annotation citing an undeclared field is a cross-reference
failure.**

**Entity and Field Declaration:**

| Entity Name | Field Name | Type | Valid Values |
|-------------|------------|------|--------------|
| | | | |
| | | | |

**Operation Declaration:**

| Operation Name | Generic Equivalent | Entity | Declared Fields Used |
|----------------|--------------------|--------|---------------------|
| | [prohibited generic term] | | |
| | | | |

Set `vocab_declaration_present: true`. Annotations may not appear before this section.

---

### Section 1 -- State Inventory and Invariants

**States:**

```
ENTITY: {entity name from Declaration}
VALID_STATES = {S-01: name, S-02: name, ...}
TERMINAL_STATES = {S-0n: name}
```

**Invariants** (formal notation with `[->DECL]` annotations on every field reference):

```
INV-01: {entity.field OPERATOR value} [->DECL: EntityName.fieldName]
        [AND {entity.field OPERATOR value} [->DECL: EntityName.fieldName] ...]
        Domain meaning: {one sentence}
        Severity if violated: FATAL / DEGRADED / COSMETIC

INV-02: {predicate with [->DECL] annotations}
        Domain meaning: {one sentence}
        Severity if violated: FATAL / DEGRADED / COSMETIC
```

---

### Section 2 -- Operation Trace

For each operation, every predicate and mutation field carries a `[->DECL]` annotation.
A field without an annotation is a notation failure.

```
OP-{n}: {operation name from Section 0 Declaration}
  PRE:   {entity.field OPERATOR value} [->DECL: EntityName.fieldName]
         [AND {entity.field OPERATOR value} [->DECL: EntityName.fieldName] ...]
  DELTA: {entity.field: old -> new} [->DECL: EntityName.fieldName]
         {entity.field: old -> new} [->DECL: EntityName.fieldName]  // one line per field
  POST:  {entity.field OPERATOR value} [->DECL: EntityName.fieldName]
         [AND ...]
  FX:    {EventEmitted(payload) | ExternalCall(endpoint) | NONE}
  INV:   INV-{id}: {predicate} [->DECL annotations on all fields] = {TRUE | FALSE}
  CHAIN: After(OP-{n}).state == Before(OP-{n+1}).state: [CHAIN OK | CHAIN BREAK]
```

**If you use a field name not in the Vocabulary Declaration, STOP. Add it to the Declaration
first, then complete the annotation. Do not proceed with an undeclared field name.**

Minimum 4 operations.

---

### Section 3 -- Invalid Transition

```
INVALID OP: {operation name from Declaration}
  ATTEMPTED FROM: {entity.state == S-id}
  PRE FAILS:  {entity.field OPERATOR required} [->DECL: EntityName.fieldName]
              -- actual: {entity.field == actual_value}
              OR INV-{id}: {predicate with ->DECL annotations} would evaluate FALSE
  GUARD:      ASSERT {predicate with ->DECL annotation} BEFORE transition
  DELTA FORM: (baseline={S-id}, attempted={op}, failure={DeclarationFieldName or INV-id})
```

---

### Section 4 -- Missing Check

```
MISSING CHECK in OP-{n}: {operation from Declaration}
  CALLER ASSUMES: {entity.field OPERATOR value} [->DECL: EntityName.fieldName] == TRUE
  NOT ENFORCED:   {layer}
  RISK: IF {entity.field OPERATOR violating_value} [->DECL: EntityName.fieldName]
        THEN {illegal state -- name the invariant or field that breaks}
```

---

### Section 5 -- Concurrency Interleaving

```
RACE IN OP-{n}: {operation from Declaration}

| Time | Actor A | Actor B |
|------|---------|---------|
| T0 | reads {entity.field == v} [->DECL: EN.fn] | reads {entity.field == v} [->DECL: EN.fn] |
| T1 | writes {entity.field: v -> v2} [->DECL: EN.fn] | writes {entity.field: v -> v3} [->DECL: EN.fn] |
| T2 | -- | commits (stale) -- **BREAK** |

POST-RACE: {entity.field == v3} [->DECL: EntityName.fieldName]
INV CHECK: INV-{id}: {predicate with ->DECL annotations} = FALSE -- {explain}
SEVERITY: FATAL / DEGRADED / COSMETIC
```

---

### Section 6 -- Alternate Path (aspirational)

```
ERROR PATH: {trigger}
  Step 1: ATTEMPT {op} from {S-id}
          RESULT: REJECTED -- {predicate with ->DECL annotation} == FALSE
  Step 2: {compensating domain verb}
          DELTA: {field: old -> new} [->DECL: EntityName.fieldName]
  Step 3: {recovery domain verb}
          POST: {entity.state == S-recovery}
          INV CHECK: INV-{id} HOLDS [->DECL annotations on all fields checked]
  RECOVERY STATE: valid, all invariants hold
```

---

### Notation Compliance Check

- [ ] Every predicate in PRE/POST/INV has `[->DECL: EntityName.fieldName]` annotation
- [ ] Every field in DELTA has `[->DECL: EntityName.fieldName]` annotation
- [ ] Every `[->DECL]` citation names a field present in Section 0 Declaration
- [ ] No undeclared field names appear in any annotation
- [ ] All operation names match Section 0 Operation Declaration
- [ ] CHAIN check written at every operation
- [ ] T0/T1 interleaving table present in Section 5

---

## V-04 -- Compound (Output Format + Lifecycle Emphasis)

**Variation axis**: Output format + lifecycle emphasis -- V-01's vocabulary declaration
template is combined with V-02's phase gate structure. The declaration appears as a
mandatory fillable template in Phase 0 (a blocking gate). The vocabulary audit appears
as a mandatory final phase gate. Both C-14 and C-15 have two enforcement mechanisms each:
structural (the fillable template / audit table), and sequential (the lifecycle cannot
advance without them).

**Hypothesis**: V-01 and V-02 address C-14 via different mechanisms. V-01 uses structural
completability (blank cells = format failure); V-02 uses sequential blocking (phase cannot
open until gate passes). Combining them removes the trade-off: the declaration is both
structurally templated AND a lifecycle gate. If one mechanism fails (model skips the gate
check), the other catches it (blank template cells are visibly wrong). C-15 gains the same
compound enforcement: the audit is a required final gate AND a structured table that cannot
be satisfied by a statement of cleanliness alone.

**Target**: C-14 (declaration template + Phase 0 gate), C-15 (audit table + final phase gate).
C-07 reinforced. C-16 partial (declared fields exist; citation not mandated).

---

You are running **trace-state** for Topic: `{Topic}`.

Choose your stock role:
- **Sales Expert** -- opportunity pipeline domain
- **Customer Service Expert** -- case and ticket lifecycle domain
- **Finance Expert** -- ledger and transaction lifecycle domain

**Artifact to produce**: `simulations/trace/state/{topic}-state-{date}.md`

**Frontmatter:**

```yaml
---
topic: {Topic}
signal: state
date: {date}
role: [Sales Expert | Customer Service Expert | Finance Expert]
entity: [entity being traced]
phase0_gate: false
phase1_gate: false
phase2_gate: false
phase3_gate: false
phase4_gate: false
phase5_gate: false
vocab_audit_gate: false
---
```

---

### Phase 0 -- Vocabulary Declaration Gate

**BLOCKED. Phase 1 is BLOCKED until `phase0_gate: true`.**

Declare your role and entity. Then complete all three declaration tables. A declaration
table with any blank required cell fails this gate. Phase 1 cannot open until all tables
are filled and the gate checklist passes.

**Entity Declaration Table:**

| Entity Name | Description | Trace Role |
|-------------|-------------|------------|
| | | [subject entity / supporting entity] |

**Field Declaration Table:**

| Entity | Field Name | Type | Valid Values / Constraints |
|--------|------------|------|---------------------------|
| | | | |
| | | | |

*(Every field that will appear in a precondition, postcondition, state mutation, or invariant
must have a row here. Blank "Valid Values" cells fail the gate.)*

**Operation Declaration Table:**

| Operation Name (domain verb) | Generic Verb Replaced | Entity | Key Precondition Field(s) |
|------------------------------|-----------------------|--------|--------------------------|
| | | | |
| | | | |

*(The "Generic Verb Replaced" column is required. At least one entry must note the generic
CRUD equivalent this domain verb replaces. Entries of "none" are acceptable only for
operations with no generic equivalent.)*

**Phase 0 Gate Checklist:**
- [ ] Role declared in opening sentence
- [ ] Entity Declaration Table fully populated (no blank cells in required columns)
- [ ] Field Declaration Table: all fields that will appear in predicates declared
- [ ] Operation Declaration Table: all trace operations declared with generic equivalent
- [ ] At least one Operation Declaration entry notes a generic verb replacement

Set `phase0_gate: true`. **Phase 1 is BLOCKED until this is set.**

---

### Phase 1 -- State Inventory and Invariants

All entity names, field names, and operation names used from here forward must match
the Phase 0 Declaration. Introducing a name not in the Declaration is a vocabulary failure.

**State Inventory:**

| S-ID | State Name (from domain) | Is Terminal? | Domain Meaning |
|------|--------------------------|--------------|----------------|
| S-01 | | yes / no | |

**Invariants (at least 2):**

| INV-ID | Expression (field names from Phase 0) | Domain Grounding | Severity |
|--------|-----------------------------------------|------------------|----------|
| INV-01 | `{entity.field OPERATOR value}` | | FATAL / DEGRADED / COSMETIC |
| INV-02 | `{entity.field OPERATOR value}` | | |

**Phase 1 Gate Checklist:**
- [ ] All states enumerated with domain names
- [ ] At least 2 invariants as checkable predicates
- [ ] All field names in invariants match Phase 0 Field Declaration
- [ ] Severity assigned per invariant

Set `phase1_gate: true`.

---

### Phase 2 -- Happy-Path Trace

Trace the entity lifecycle from initial to terminal state. Use only vocabulary from
Phase 0. Chain must be unbroken.

```
OP-{n}: {operation from Phase 0 Declaration}
  Before:         {S-id: state name}
  Preconditions:  {entity.field OPERATOR value} [AND ...]
  State Change:   {entity.field: from -> to}
  Postconditions: {entity.field OPERATOR value} [AND ...]
  Side Effects:   [events / calls / "none"]
  INV Check:      INV-{id}: {expression} = [TRUE | FALSE]
  After:          {S-id: state name}
  CHAIN:          [CHAIN OK | CHAIN BREAK -- explain]
```

Minimum 4 operations.

**Phase 2 Gate Checklist:**
- [ ] Every operation block has all 8 fields populated (no blank cells)
- [ ] CHAIN check written after each operation
- [ ] All operation names match Phase 0 Operation Declaration
- [ ] All field names in Pre/Post/Change match Phase 0 Field Declaration
- [ ] At least one INV check per operation

Set `phase2_gate: true`.

---

### Phase 3 -- Adversarial Analysis

**Invalid Transition (at least one):**

```
INVALID ATTEMPT: {operation from Phase 0}
  Attempted From:  {S-id}
  Fails Because:   {entity.field OPERATOR required} -- actual: {actual value}
                   OR INV-{id}: {expression} would evaluate FALSE
  Guard Required:  ASSERT {precondition} before transition
  Delta Form:      (baseline={S-id}, attempted={op name}, failure={field or INV-id})
```

**Missing Check (at least one):**

```
MISSING CHECK in OP-{n}: {operation from Phase 0}
  Caller Assumes:  {entity.field OPERATOR value} without verification
  Not Enforced By: {layer}
  Risk:            {concrete failure -- names invariant or illegal state}
```

**Phase 3 Gate Checklist:**
- [ ] At least one invalid transition with delta form (C-04, C-13)
- [ ] At least one missing check with named risk (C-06)
- [ ] All vocabulary matches Phase 0 Declaration

Set `phase3_gate: true`.

---

### Phase 4 -- Concurrency Analysis

Select one operation. Render as T0/T1 interleaving table (at least 4 rows):

| Time | Actor A | Actor B |
|------|---------|---------|
| T0 | reads `{field == v}` | reads `{field == v}` |
| T1 | writes `{field: v -> v2}` | writes `{field: v -> v3}` (stale) |
| T2 | -- | commits, overwrites A |
| **BREAK** | **INV-{id} violated** | **{expression} == FALSE** |

```
Post-race: {entity.field == corrupted}
Invariant: INV-{id}: {expression} evaluates FALSE -- {explain}
Severity:  FATAL / DEGRADED / COSMETIC
```

**Phase 4 Gate Checklist:**
- [ ] T0/T1 table with at least 4 rows
- [ ] Row where invariant breaks explicitly marked
- [ ] Named invariant and broken expression

Set `phase4_gate: true`.

---

### Phase 5 -- Severity Classification and Alternate Path (aspirational)

**5A -- Severity Table:**

| Violation | Invariant | Scenario | Severity | Recovery Path |
|-----------|-----------|----------|----------|---------------|
| | INV-{id} | | FATAL / DEGRADED / COSMETIC | |

**5B -- Alternate Error Path (3+ steps):**

```
ERROR PATH: {trigger}
  Step 1: ATTEMPT {op} from {S-id} -- REJECTED: {precondition fails}
  Step 2: {compensating domain verb} -- {field: old -> new}
  Step 3: {recovery domain verb} -- arrives at {S-id: recovery state}
  Recovery: INV-{id} HOLDS, INV-{id} HOLDS
```

Set `phase5_gate: true` if completed; mark "N/A -- {reason}" if not applicable.

---

### Phase FINAL -- Vocabulary Audit Gate

**REQUIRED. Artifact cannot be written until `vocab_audit_gate: true`.**

**Part A -- Operation Audit:**

For every distinct operation name used in Phases 2-5, identify its Phase 0 row.
Flag any operation used but not declared.

| Operation Used | Phase(s) | Phase 0 Declaration Row | Status |
|----------------|----------|------------------------|--------|
| | | matches: "{declared name}" | DECLARED / NOT DECLARED -- CORRECT NOW |

**Part B -- Generic Verb Scan:**

Search the entire trace body for generic CRUD verbs (update, set, create, delete, modify,
add, remove, get, fetch). List every instance found:

| Generic Verb | Location (OP-n, Phase) | Required Replacement | Correction Applied |
|--------------|----------------------|---------------------|-------------------|
| [none -- scan clean] OR [list each] | | | |

**Part C -- Deviation Summary:**

```
Total operations declared in Phase 0: {n}
Total distinct operations used in trace: {n}
Operations used but not declared: {list or "none"}
Operations declared but not used: {list or "none"}
Generic verbs found and not corrected: {list or "none"}
```

**Vocabulary Audit Gate Checklist:**
- [ ] Part A: every operation mapped to Phase 0 row
- [ ] Part B: generic verb scan completed (statement of cleanliness does not satisfy this)
- [ ] Part C: deviation summary written
- [ ] Any deviations corrected before this gate is set

Set `vocab_audit_gate: true`.

---

### Final Scoring Checklist

- [ ] Phase 0 declaration block complete and gate set (C-14)
- [ ] Vocabulary Audit gate complete (C-15)
- [ ] All field names in predicates match Phase 0 Field Declaration (C-16 partial)
- [ ] State chain unbroken, all triples complete (C-01)
- [ ] Preconditions reference declared fields (C-02)
- [ ] Postconditions name changed fields (C-03)
- [ ] At least one invalid transition with delta form (C-04, C-13)
- [ ] At least 2 invariants tested (C-05)
- [ ] Missing check with risk (C-06)
- [ ] Domain vocabulary consistent with Phase 0 (C-07)
- [ ] Race condition with T0/T1 table (C-08, C-12)

---

## V-05 -- Compound (Output Format + Lifecycle + Phrasing Register + Imperative Markers)

**Variation axis**: All three single-axis mechanisms combined plus imperative phrasing
register. V-01's vocabulary declaration template + V-02's blocking phase gates + V-03's
`[->DECL]` citation annotation syntax + MUST/BLOCKED/ADVANCE markers throughout. The
post-trace Vocabulary Audit maps each predicate's `[->DECL]` citations back to the
Phase 0 declaration rows, providing compound evidence for C-15 and C-16 simultaneously.

**Hypothesis**: C-14, C-15, and C-16 have a prerequisite chain: C-14 must exist before
C-16 can apply; C-15 requires C-14 to exist to audit against. V-05 enforces this chain
structurally. The `[->DECL]` citation in every predicate (V-03) makes Phase 0 mandatory
by reference. The Phase 0 gate (V-02) makes it mandatory by sequencing. The structured
audit table (V-02 final phase) maps each citation back to its declaration entry, satisfying
C-15 with compound evidence. MUST/BLOCKED/ADVANCE markers convert every gate condition
from a recommendation into an imperative, reducing the chance of silent gate skipping.

**Target**: C-14, C-15, C-16. All essential and recommended criteria from prior rounds
maintained via the proven triple-plus operation block format.

---

You are running **trace-state** for Topic: `{Topic}`.

Choose your stock role:
- **Sales Expert** -- opportunity pipeline domain
- **Customer Service Expert** -- case and ticket lifecycle domain
- **Finance Expert** -- ledger and transaction lifecycle domain

**Artifact to produce**: `simulations/trace/state/{topic}-state-{date}.md`

**Notation rule for this trace:**

Every predicate condition and every mutation field carries a mandatory citation annotation:

```
{entity.field OPERATOR value} [->DECL: EntityName.fieldName]
```

This annotation names the Phase 0 declaration entry the field is drawn from. **A predicate
without a `[->DECL]` annotation is BLOCKED -- do not advance past it.**

If you need a field name not yet in the Phase 0 declaration, STOP. Add it to Phase 0 first.
Then complete the annotation. **Undeclared field names in annotations are BLOCKED.**

**Frontmatter:**

```yaml
---
topic: {Topic}
signal: state
date: {date}
role: [Sales Expert | Customer Service Expert | Finance Expert]
entity: [entity being traced]
notation: formal-predicate-with-decl-citation
phase0_gate: false
phase1_gate: false
phase2_gate: false
phase3_gate: false
phase4_gate: false
phase5_gate: false
vocab_audit_gate: false
---
```

---

### Phase 0 -- Vocabulary Declaration Gate

**BLOCKED. Phase 1 is BLOCKED until `phase0_gate: true`. You MUST complete all three
declaration tables before writing a single operation block.**

Declare your role and entity in one sentence. Then produce the three declaration tables.
Every cell in a required column MUST be filled. A blank cell BLOCKS this gate.

**Entity Declaration:**

| Entity Name | Description | Trace Role |
|-------------|-------------|------------|
| | | subject / supporting |

**Field Declaration:**

| Entity | Field Name | Type | Valid Values | Will Appear In |
|--------|------------|------|--------------|----------------|
| | | | | PRE / POST / DELTA / INV |
| | | | | |

*(The "Will Appear In" column is required. Every field that will carry a `[->DECL]`
annotation MUST be declared here. A `[->DECL]` citation for an undeclared field BLOCKS
the operation containing it.)*

**Operation Declaration:**

| Operation Name (domain verb) | Generic Verb Replaced | Entity | Precondition Fields |
|------------------------------|-----------------------|--------|---------------------|
| | MUST name the CRUD term replaced | | |
| | | | |

*(The "Generic Verb Replaced" column MUST name the prohibited CRUD term. If no generic
term applies, write "none -- domain-only." This column MUST NOT be blank.)*

**Phase 0 Gate Checklist:**
- [ ] Role and entity declared
- [ ] Entity Declaration complete (no blank required cells)
- [ ] Field Declaration complete -- all predicate-appearing fields declared
- [ ] Operation Declaration complete -- generic equivalents named
- [ ] At least one entry notes a generic verb replacement (not all "none")

**ADVANCE to Phase 1 only after setting `phase0_gate: true`. Phase 1 is BLOCKED until
this gate is set.**

---

### Phase 1 -- State Inventory and Invariants

All names used from here forward MUST match Phase 0 Declaration entries. Introducing
a field or operation name not in Phase 0 is BLOCKED -- add it to Phase 0 first.

**States:**

```
ENTITY: {entity from Phase 0}
VALID_STATES = {S-01: domain-name, S-02: domain-name, ...}
TERMINAL_STATES = {S-0n: domain-name}
```

**Invariants (at least 2 -- formal notation with `[->DECL]` on every field):**

```
INV-01: {entity.field OPERATOR value} [->DECL: EntityName.fieldName]
        [AND {entity.field OPERATOR value} [->DECL: EntityName.fieldName] ...]
        Domain meaning: {one sentence}
        Severity: FATAL / DEGRADED / COSMETIC

INV-02: {predicate with [->DECL] annotations on all field references}
        Domain meaning: {one sentence}
        Severity: FATAL / DEGRADED / COSMETIC
```

**Phase 1 Gate Checklist:**
- [ ] All valid states enumerated with domain names
- [ ] At least 2 invariants with `[->DECL]` annotations on all field references
- [ ] All `[->DECL]` citations name Phase 0 Field Declaration entries
- [ ] Severity assigned per invariant

Set `phase1_gate: true`. **Phase 2 is BLOCKED until this is set.**

---

### Phase 2 -- Happy-Path Trace

Every operation MUST use vocabulary from Phase 0. Every predicate field MUST carry a
`[->DECL]` annotation. Chain MUST be unbroken.

```
OP-{n}: {operation from Phase 0 Declaration}
  Before:         {S-id: state name}
  PRE:   {entity.field OPERATOR value} [->DECL: EntityName.fieldName]
         [AND {entity.field OPERATOR value} [->DECL: EntityName.fieldName] ...]
  DELTA: {entity.field: from_value -> to_value} [->DECL: EntityName.fieldName]
         {entity.field: from_value -> to_value} [->DECL: EntityName.fieldName]
  POST:  {entity.field OPERATOR value} [->DECL: EntityName.fieldName]
         [AND ...]
  FX:    {EventEmitted(payload) | ExternalCall(endpoint) | NONE}
  INV:   INV-{id}: {predicate} [->DECL annotations on all fields] = [TRUE | FALSE]
  After:          {S-id: state name}
  CHAIN: After(OP-{n}) == Before(OP-{n+1}): [CHAIN OK | CHAIN BREAK -- BLOCKED: explain]
```

**If a field name needed in a predicate is not in the Phase 0 Declaration, STOP. Add it
to Phase 0 now. Then write the annotation. Do NOT proceed with an undeclared field.**

Minimum 4 operations.

**Phase 2 Gate Checklist:**
- [ ] Every operation has all fields populated (no blank cells) -- MUST pass
- [ ] Every PRE/POST/DELTA/INV field has `[->DECL]` annotation
- [ ] Every `[->DECL]` citation names a Phase 0 Field Declaration entry
- [ ] CHAIN check written at every operation
- [ ] All operation names match Phase 0 Operation Declaration

Set `phase2_gate: true`. **Phase 3 is BLOCKED until this is set.**

---

### Phase 3 -- Adversarial Analysis

**Invalid Transition (MUST produce at least one):**

```
INVALID OP: {operation from Phase 0}
  ATTEMPTED FROM:  {entity.state == S-id}
  PRE FAILS:  {entity.field OPERATOR required} [->DECL: EntityName.fieldName]
              -- actual: {entity.field == actual}
              OR INV-{id}: {predicate with ->DECL} would evaluate FALSE post-transition
  GUARD:      ASSERT {predicate with ->DECL annotation} BEFORE allowing transition
  DELTA FORM: (baseline={S-id}, attempted={op}, failure={Phase0.FieldName or INV-id})
```

**Missing Check (MUST produce at least one):**

```
MISSING CHECK in OP-{n}: {operation from Phase 0}
  CALLER ASSUMES: {entity.field OPERATOR value} [->DECL: EntityName.fieldName] == TRUE
  NOT ENFORCED:   {layer}
  RISK: IF {entity.field == violating_value} [->DECL: EntityName.fieldName]
        THEN {illegal state or named invariant break}
```

**Phase 3 Gate Checklist:**
- [ ] At least one invalid transition with delta form and `[->DECL]` citations (C-04, C-13)
- [ ] At least one missing check with named risk and `[->DECL]` citations (C-06)
- [ ] All `[->DECL]` citations name Phase 0 entries

Set `phase3_gate: true`. **Phase 4 is BLOCKED until this is set.**

---

### Phase 4 -- Concurrency Analysis

**MUST produce T0/T1 interleaving table (at least 4 rows).**

```
RACE IN OP-{n}: {operation from Phase 0}
```

| Time | Actor A | Actor B |
|------|---------|---------|
| T0 | reads `{entity.field == v}` `[->DECL: EN.fn]` | reads `{entity.field == v}` `[->DECL: EN.fn]` |
| T1 | writes `{entity.field: v -> v2}` `[->DECL: EN.fn]` | writes `{entity.field: v -> v3}` `[->DECL: EN.fn]` (stale) |
| T2 | -- | commits, overwrites A |
| **BREAK** | **INV-{id} VIOLATED** | `{predicate [->DECL]}` **== FALSE** |

```
POST-RACE: {entity.field == v3} [->DECL: EntityName.fieldName]
INV CHECK: INV-{id}: {predicate with ->DECL} evaluates FALSE -- {explain}
SEVERITY:  FATAL / DEGRADED / COSMETIC
```

**Phase 4 Gate Checklist:**
- [ ] T0/T1 table with at least 4 rows
- [ ] `[->DECL]` annotations present on all field references in the table
- [ ] Row where invariant breaks explicitly marked
- [ ] Named invariant and broken predicate with annotation

Set `phase4_gate: true`. **Phase 5 is BLOCKED until this is set.**

---

### Phase 5 -- Depth Extensions (aspirational -- ADVANCE to Vocab Audit after this)

**5A -- Severity Classification Table:**

| Violation | Invariant | Scenario | Severity | Recovery Path |
|-----------|-----------|----------|----------|---------------|
| | INV-{id} | | FATAL / DEGRADED / COSMETIC | |

At least one FATAL or DEGRADED MUST be present, or state explicitly why none exist
for this scenario.

**5B -- Alternate Error Path (3+ steps):**

```
ERROR PATH: {trigger}
  Step 1: ATTEMPT {op} from {S-id}
          RESULT: REJECTED -- {predicate with ->DECL} == FALSE
  Step 2: {compensating domain verb}
          DELTA: {field: old -> new} [->DECL: EntityName.fieldName]
  Step 3: {recovery domain verb}
          POST: {entity.state == S-recovery}
          INV CHECK: INV-{id} [->DECL annotations] HOLDS
  RECOVERY: all invariants hold, entity in valid state
```

Set `phase5_gate: true` if completed; mark "N/A -- {reason}" if not applicable.

---

### Phase FINAL -- Vocabulary Audit Gate

**REQUIRED. Artifact MUST NOT be written until `vocab_audit_gate: true`.**

**Part A -- Operation-to-Declaration Audit:**

For every distinct operation name used in Phases 2-5, map it to its Phase 0 row.
A statement that "all vocabulary was clean" does NOT satisfy this part -- the table MUST
be populated.

| Operation Used | Phase(s) | Phase 0 Row | Status |
|----------------|----------|-------------|--------|
| | | declares: "{name}" generic: "{term}" | DECLARED / NOT DECLARED -- CORRECT NOW |

**Part B -- Citation Cross-Reference Audit:**

For every `[->DECL: EntityName.fieldName]` annotation in the entire trace, verify the
cited field appears in the Phase 0 Field Declaration.

| Annotation | Phase / OP | Phase 0 Field Row | Cross-Reference Status |
|------------|------------|-------------------|------------------------|
| `[->DECL: EN.fn]` | Phase {n}, OP-{m} | declared: entity={EN}, field={fn} | VERIFIED / NOT FOUND -- CORRECT NOW |

*(Sampling is acceptable for traces with 20+ annotations: verify all PRE fields in
Phase 2, all fields in all invalid transitions, and all INV fields in Phase 1. List
sample scope explicitly.)*

**Part C -- Generic Verb Scan:**

Search the entire trace body for: update, set, create, delete, modify, add, remove,
get, fetch, process, handle. List every instance:

| Generic Verb | Location | Phase 0 Replacement | Action |
|--------------|----------|--------------------|----|
| [none -- scan clean] OR [list each] | | | REPLACED / BLOCKED IF REMAINING |

**Part D -- Deviation Summary:**

```
Operations declared in Phase 0: {n}
Operations used in trace: {n}
Undeclared operations used: {list or "none"}
[->DECL] citations verified: {n} of {n total}
Citations with undeclared fields: {list or "none"}
Generic verbs found: {n} -- all corrected: yes / no
```

**Vocabulary Audit Gate Checklist:**
- [ ] Part A: every operation mapped to Phase 0 row (MUST NOT be satisfied by statement alone)
- [ ] Part B: `[->DECL]` citation cross-reference table populated
- [ ] Part C: generic verb scan completed with explicit result
- [ ] Part D: deviation summary written
- [ ] All deviations corrected before this gate is set

**ADVANCE: set `vocab_audit_gate: true`. Artifact may now be written to disk.**

---

### Final Scoring Checklist

- [ ] Phase 0 vocabulary declaration block complete (C-14)
- [ ] Vocabulary Audit gate complete with cross-reference table (C-15)
- [ ] All `[->DECL]` citations map to Phase 0 entries -- no predicate uses undeclared field (C-16)
- [ ] State chain unbroken, all triples complete (C-01)
- [ ] Preconditions reference declared fields with `[->DECL]` (C-02, C-11)
- [ ] Postconditions name changed fields with `[->DECL]` (C-03, C-11)
- [ ] At least one invalid transition with delta form (C-04, C-13)
- [ ] At least 2 invariants with `[->DECL]` annotations (C-05)
- [ ] Missing check with risk (C-06)
- [ ] Domain vocabulary matches Phase 0 (C-07)
- [ ] Race condition with T0/T1 table and `[->DECL]` annotations (C-08, C-12)
- [ ] Severity table with FATAL or DEGRADED entry (C-09)
- [ ] Alternate error path 3+ steps (C-10)
