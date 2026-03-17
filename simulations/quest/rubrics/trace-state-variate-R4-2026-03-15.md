# trace-state Skill -- Quest Variations Round 4

**Skill**: trace-state
**Round**: 4 (building on R3 golden base; rubric v4, 10 aspirationals)
**Rubric**: v4 (C-01--C-18; composite = E/5*60 + R/3*30 + A/10*10)
**R4 target gaps**: C-17 (per-predicate source citation `[->DECL: EntityName.fieldName]`), C-18 (per-section completion gate markers)

**R3 baseline**: V-01 5/10 aspirational (95 composite), V-02 8/10 (98), V-03 7/10 (97). All golden.
**R3 gap**: No variation passed both C-17 and C-18 simultaneously. V-02 passed C-18; V-03 passed C-17.

---

## Variation Map

| V | Axis | Primary Targets | Key Structural Change |
|---|------|-----------------|-----------------------|
| V-01 | Output format | C-17 | Pre-printed `[->DECL: _._]` slots in every predicate position; model fills entity.field into blank rather than deciding to annotate |
| V-02 | Lifecycle emphasis | C-18 | Two-sided gate contracts: each section opens with a prospective contract AND closes with a gate check; only closing gates were present in R3 V-02 |
| V-03 | Phrasing register | C-17, C-18 | ADVANCE BLOCKED conditions name specific missing elements (annotation absent / row count short) rather than generic checklist items |
| V-04 | Compound (output + lifecycle) | C-17, C-18 | V-01 citation-slot template + V-02 two-sided gate contract; both mechanisms active simultaneously |
| V-05 | Compound (full stack) | C-17, C-18, all 10 aspirationals | V-04 + V-03 BLOCKED/ADVANCE language + alternate path section + all prior excellence (T0/T1 table, baseline deltas, vocabulary audit, severity classification) |

**Single-axis hypotheses tested:**

- **V-01 hypothesis**: A fill-in-the-blank template where `[->DECL: _._]` slots are pre-printed produces C-17 compliance at higher rates than an instruction to "add citation annotations." The slot cannot be silently skipped -- a remaining `_._` is visibly incomplete output, identical to a blank cell in a table.

- **V-02 hypothesis**: Opening a section with "This section will produce: [list of required elements]" produces higher C-18 compliance than a trailing gate alone. The prospective contract primes the model to generate required elements *before* writing the section body; a trailing gate is consulted only after the section is complete, when correction is more costly.

- **V-03 hypothesis**: ADVANCE BLOCKED conditions that name the specific missing element ("BLOCKED until every predicate carries [->DECL: E.f]") are more compliance-inducing than checklist gates ("[ ] annotations present") because they identify the exact absent artifact rather than requiring the model to scan a generic list and decide whether the condition applies.

- **V-04 compound test**: Can citation-slot scaffolding (V-01) and prospective gate contracts (V-02) coexist without interference? V-01's slot template gives the model the annotation structure; V-02's opening contract tells it the annotation is required before it starts writing. The two mechanisms target different moments in generation: V-01 acts at the predicate; V-02 acts at the section boundary.

---

## V-01 -- Output Format: Citation-Slot Template

**Variation axis**: Output format -- every predicate position in the output template contains a
pre-printed `[->DECL: _._]` slot. The model does not decide whether to annotate; it fills the
blank entity name and field name into an annotation that already exists. A remaining `_._` in
the output is a visible format failure, identical to an unfilled table cell.

**Hypothesis**: C-17 requires the annotation as an artifact at the predicate, not merely the
match as a property. The most direct mechanism is a pre-printed slot that the model fills as
part of template completion rather than as a voluntary act. The slot also makes C-16 verifiable
one predicate at a time: the reviewer checks `[->DECL: EntityName.fieldName]` against the Phase
0 row without a document-level scan.

**Closing gates** are present per section (single-sided -- closing only). The gate enumerates
specific required elements for that section. This is the same gate structure as R3 V-01; it
targets C-18 as a secondary mechanism but does not add the opening contract axis.

**Primary target**: C-17. **Secondary**: C-18 (closing gates).

---

You are running **trace-state** for Topic: `{Topic}`.

Choose your stock role:
- **Sales Expert** -- opportunity pipeline domain
- **Customer Service Expert** -- case and ticket lifecycle domain
- **Finance Expert** -- ledger and transaction lifecycle domain

**Artifact**: `simulations/trace/state/{topic}-state-{date}.md`

---

### Phase 0 -- Vocabulary Declaration

Declare every entity name, field name, and operation name before writing any transitions. You
may not introduce any name in a later phase that does not appear in this table.

**Entity and Field Declaration:**

| Entity Name | Field Name | Field Type | Valid Values / Range |
|-------------|------------|------------|----------------------|
| | | | |
| | | | |
| | | | |
| | | | |

*(Add one row per field. Every field that will appear in any predicate, state assignment, or
invariant must be declared here.)*

**Operation Declaration:**

| Operation Name (domain verb) | Generic Verb Replaced | Primary Entity Affected |
|------------------------------|-----------------------|-------------------------|
| | [e.g., "create", "update"] | |
| | | |
| | | |

*(For every operation: name the generic CRUD verb it replaces. "none -- domain-only" is
acceptable only if no generic verb maps.)*

**Phase 0 Gate:**
- [ ] At least 2 entities declared with at least 2 fields each
- [ ] At least 3 operations declared with generic-verb replacements named
- [ ] No blank cells in any declaration row

---

### Phase 1 -- State Transition Chain

Produce at least 4 complete transition triples forming an unbroken chain. Fill every slot
including the `[->DECL: _._]` annotation for each field reference. Replace `_` with the
exact entity name and field name from Phase 0. A remaining `_._` is a format failure.

**Triple template (copy and complete for each operation):**

```
Operation N: [name -- from Phase 0 Operation table]

Before-state:
  EntityName.fieldName [->DECL: _._] = value
  EntityName.fieldName [->DECL: _._] = value

Preconditions:
  EntityName.fieldName [->DECL: _._] OPERATOR value    -- reason
  EntityName.fieldName [->DECL: _._] OPERATOR value    -- reason

Postconditions (mutations):
  EntityName.fieldName [->DECL: _._]: old_value -> new_value
  EntityName.fieldName [->DECL: _._]: old_value -> new_value

Side effects: [events emitted / external calls / none]

After-state:
  EntityName.fieldName [->DECL: _._] = value
  EntityName.fieldName [->DECL: _._] = value
```

After-state of triple N must equal before-state of triple N+1 exactly.

**Phase 1 Gate:**
- [ ] At least 4 complete transition triples
- [ ] Every `[->DECL: _._]` slot filled -- no underscore placeholders remaining
- [ ] After-state of triple N matches before-state of triple N+1 for all N
- [ ] All operation names from Phase 0 vocabulary (no new names introduced)
- [ ] Zero generic verbs ("create", "update", "delete", "set", "get") in operation names

---

### Phase 2 -- System Invariants

State at least 2 invariants in predicate form. Apply each to at least one trace step.
Classify each potential violation.

```
INV-N: EntityName.fieldName [->DECL: _._] OPERATOR value
  Applied at Operation N: HOLDS -- current value is [actual]
                       OR VIOLATION -- current value is [actual]
  Severity if violated: FATAL / DEGRADED / COSMETIC -- reason
```

**Phase 2 Gate:**
- [ ] At least 2 invariants in predicate form, all `[->DECL: _._]` slots filled
- [ ] Each invariant applied to at least one trace step with HOLDS or VIOLATION marked
- [ ] Every potential violation severity-classified

---

### Phase 3 -- Invalid Transitions

Express at least one invalid transition as a baseline delta.

```
INVALID-N:
  Baseline:  EntityName.fieldName [->DECL: _._] = current_value
  Attempted: [operation name from Phase 0]
  Failure:   EntityName.fieldName [->DECL: _._] OPERATOR required_value -- not satisfied
             OR INV-N violated because EntityName.fieldName [->DECL: _._] = actual_value
```

**Phase 3 Gate:**
- [ ] At least 1 INVALID-N in baseline delta form
- [ ] Failure reason names a specific field with predicate, or names an invariant by label
- [ ] All `[->DECL: _._]` slots filled

---

### Phase 4 -- Missing Precondition Checks

Flag at least one precondition the system assumes but does not enforce.

```
GAP-N:
  Operation:  [Phase 0 name]
  Assumed:    EntityName.fieldName [->DECL: _._] OPERATOR value
  Enforced:   none / partial -- reason
  Risk:       what breaks if violated
```

**Phase 4 Gate:**
- [ ] At least 1 GAP-N with assumed precondition in predicate form and `[->DECL: _._]` filled
- [ ] Risk stated

---

### Phase 5 -- Race Condition Analysis

For at least one operation, trace concurrent execution as a T0/T1 interleaving table.
Minimum 4 rows. Mark the VIOLATION row and name the broken invariant.

| Step | T0 (Actor A) | T1 (Actor B) | Shared state | Invariant status |
|------|--------------|--------------|--------------|------------------|
| 1 | | | EntityName.fieldName [->DECL: _._] = v | HOLDS |
| 2 | | | EntityName.fieldName [->DECL: _._] = v' | HOLDS |
| 3 | | | EntityName.fieldName [->DECL: _._] = v'' | *** VIOLATION: [INV-N] *** |
| 4 | | | | |

Replace all `[->DECL: _._]` slots in the shared-state column with Phase 0 names.

**Phase 5 Gate:**
- [ ] T0/T1 table row count >= 4
- [ ] At least one VIOLATION row with invariant named by label (not description)
- [ ] At least one `[->DECL: E.f]` annotation completed in the shared-state column

---

### Phase 6 -- Post-Trace Vocabulary Audit

Enumerate every distinct operation name used in phases 1-5 and map to Phase 0.

| Operation Used in Trace | Phase 0 Entry | Status |
|-------------------------|---------------|--------|
| | | MATCH |
| | (none) | CORRECTION -- replace with: [Phase 0 name] |

**Phase 6 Gate:**
- [ ] Every operation from phases 1-5 appears in the table
- [ ] All CORRECTION rows have a replacement name specified
- [ ] Final scan: zero generic verbs remaining as operation names in phases 1-5

---

**Output rules:**
1. Every `[->DECL: _._]` slot must be filled with the exact entity name and field name from
   Phase 0. No `_._` placeholders may remain in the submitted output.
2. All field names in predicates are drawn from Phase 0 declarations only. A field name
   not in Phase 0 is a format failure.
3. Operation names come from Phase 0 only. If you introduce a new name, add it to Phase 0
   first, then use it.
4. Generic verbs ("create", "update", "delete", "set", "get") are not valid operation names.
   If you write one, stop and replace it before continuing.

---

## V-02 -- Lifecycle Emphasis: Two-Sided Gate Contract

**Variation axis**: Lifecycle emphasis -- every section has both an *opening contract*
declaring what the section will produce (before the section body) AND a *closing gate*
confirming required elements were produced (after the section body). R3 V-02 had closing gates
only; this variation adds the opening contract as the single new axis.

**Hypothesis**: A closing gate is consulted after the section is complete, when the model must
revise content already written. An opening contract is consulted before the section body, when
the model is priming what to generate. The opening contract converts the gate from a
retrospective compliance check into a prospective generation target, reducing the revision
cost of non-compliance.

**C-18 mechanism**: Both the opening contract and the closing gate are present for at least
two sections. The opening contract enumerates required elements by name; the closing gate
confirms each by name. The pair satisfies "enumerates specific required elements for that
section by name, marks each as present or absent, appears between that section and the next"
(C-18 pass condition) more robustly than a closing gate alone.

**C-17 mechanism**: Citation annotations are instructed via global rules and in the Phase 1
contract ("every field reference carries [->DECL: E.f]") but without pre-printed slots.
Compliance depends on instruction adherence rather than template scaffolding.

**Primary target**: C-18. **Secondary**: C-17 (instruction-based).

---

You are running **trace-state** for Topic: `{Topic}`.

Choose your stock role:
- **Sales Expert** -- opportunity pipeline domain
- **Customer Service Expert** -- case and ticket lifecycle domain
- **Finance Expert** -- ledger and transaction lifecycle domain

**Artifact**: `simulations/trace/state/{topic}-state-{date}.md`

This output is a gated pipeline. Each section opens with a contract stating what it will
produce, then produces it, then closes with a gate confirming required elements are present.
The next section begins only when the closing gate is satisfied.

---

### Phase 0 -- Vocabulary Declaration

**Opening contract:**
This section will produce: (a) declarations for all entity names and their relevant field
names, (b) declarations for all operation names with generic-verb equivalents noted.
Minimum: 2 entities, 4 fields, 3 operations.

Produce the declaration tables:

**Entity and Field Declaration:**

| Entity Name | Field Name | Field Type | Valid Values / Range |
|-------------|------------|------------|----------------------|
| | | | |

*(One row per field. Every field that will appear in a predicate must be declared here.)*

**Operation Declaration:**

| Operation Name | Generic Verb Replaced | Primary Entity |
|----------------|-----------------------|----------------|
| | | |

*(One row per operation. Name the generic CRUD verb it replaces.)*

**Phase 0 Closing Gate:**

Before opening Phase 1, confirm:
- [ ] Entity declarations: at least 2 entities, at least 2 fields each
- [ ] Operation declarations: at least 3 operations with generic equivalents named
- [ ] No blank cells in any declaration row

---

### Phase 1 -- State Transition Chain

**Opening contract:**
This section will produce at least 4 (before, op, after) transition triples forming an
unbroken chain. Required elements per triple: before-state field values with [->DECL: E.f]
annotations, preconditions in predicate form with [->DECL: E.f] annotations, postconditions
expressing state mutations with [->DECL: E.f] annotations, side effects, after-state. The
after-state of triple N will exactly equal the before-state of triple N+1.

Annotation rule: every field name reference in this section -- in before-states,
preconditions, postconditions, and after-states -- must carry a `[->DECL: EntityName.fieldName]`
annotation citing the exact Phase 0 declaration row for that field.

Produce at least 4 transition triples:

```
Operation N: [Phase 0 name]

Before-state:
  EntityName.fieldName [->DECL: E.f] = value
  EntityName.fieldName [->DECL: E.f] = value

Preconditions:
  EntityName.fieldName [->DECL: E.f] OPERATOR value  -- reason
  EntityName.fieldName [->DECL: E.f] OPERATOR value  -- reason

Postconditions:
  EntityName.fieldName [->DECL: E.f]: old -> new
  EntityName.fieldName [->DECL: E.f]: old -> new

Side effects: [events / calls / none]

After-state:
  EntityName.fieldName [->DECL: E.f] = value
  EntityName.fieldName [->DECL: E.f] = value
```

**Phase 1 Closing Gate:**

Before opening Phase 2, confirm:
- [ ] Triple count >= 4
- [ ] Every field reference carries a [->DECL: E.f] annotation (no unannotated field names)
- [ ] After-state of triple N matches before-state of triple N+1 for all N
- [ ] All operation names from Phase 0
- [ ] Zero generic verbs in operation names

---

### Phase 2 -- System Invariants

**Opening contract:**
This section will produce at least 2 invariants in predicate form using Phase 0 vocabulary.
Each invariant will be applied to at least one trace step showing HOLDS or VIOLATION.
Each potential violation will be severity-classified: FATAL / DEGRADED / COSMETIC.
All field references carry [->DECL: E.f] annotations.

```
INV-N: EntityName.fieldName [->DECL: E.f] OPERATOR value
  Tested at Operation N: HOLDS -- current value [actual]
                      OR VIOLATION -- current value [actual]
  Severity if violated: FATAL / DEGRADED / COSMETIC -- reason
```

**Phase 2 Closing Gate:**

Before opening Phase 3, confirm:
- [ ] Invariant count >= 2, each in predicate form
- [ ] Each invariant applied to >= 1 trace step with HOLDS or VIOLATION marked
- [ ] All VIOLATION outcomes severity-classified
- [ ] All [->DECL: E.f] annotations present on field references

---

### Phase 3 -- Invalid Transitions

**Opening contract:**
This section will produce at least 1 invalid transition expressed as a baseline delta:
(baseline_state, attempted_delta, failure_reason). The failure reason will name a specific
predicate field with condition, or an invariant by label. Generic statements ("operation not
permitted") do not satisfy the failure-reason requirement.

```
INVALID-N:
  Baseline:  EntityName.fieldName [->DECL: E.f] = value
  Attempted: [Phase 0 operation name]
  Failure:   EntityName.fieldName [->DECL: E.f] OPERATOR required -- current value [actual] fails
             OR INV-N violated because EntityName.fieldName [->DECL: E.f] = [actual]
```

**Phase 3 Closing Gate:**

Before opening Phase 4, confirm:
- [ ] At least 1 INVALID-N in baseline delta form
- [ ] Failure reason names specific field/condition or invariant label
- [ ] All [->DECL: E.f] annotations present

---

### Phase 4 -- Missing Precondition Checks

**Opening contract:**
This section will produce at least 1 precondition gap: a condition an operation assumes
but the system does not enforce. The assumed precondition will be in predicate form with
[->DECL: E.f] annotation. The enforcement gap and risk will be stated explicitly.

```
GAP-N:
  Operation:  [Phase 0 name]
  Assumed:    EntityName.fieldName [->DECL: E.f] OPERATOR value
  Enforced:   none / partial -- why it is not enforced
  Risk:       what breaks if violated
```

**Phase 4 Closing Gate:**

Before opening Phase 5, confirm:
- [ ] At least 1 GAP-N
- [ ] Assumed precondition in predicate form with [->DECL: E.f] annotation
- [ ] Risk stated

---

### Phase 5 -- Race Condition Analysis

**Opening contract:**
This section will produce a T0/T1 concurrent interleaving table for at least one operation.
The table will have at least 4 rows. The row where an invariant breaks will be marked
VIOLATION with the broken invariant named by label.

```
Operation analyzed: [Phase 0 name]
Race scenario: [describe two concurrent actors and their conflicting actions]
```

| Step | T0 (Actor A) | T1 (Actor B) | Shared state | Invariant status |
|------|--------------|--------------|--------------|------------------|
| 1 | | | EntityName.fieldName [->DECL: E.f] = v | HOLDS |
| 2 | | | | HOLDS |
| 3 | | | | *** VIOLATION: [INV-N] *** |
| 4 | | | | |

Name the broken invariant in the VIOLATION row. Minimum 4 rows.

**Phase 5 Closing Gate:**

Before opening Phase 6, confirm:
- [ ] T0/T1 table row count >= 4 (count: ___)
- [ ] At least 1 VIOLATION row with invariant named by label
- [ ] Shared state column contains at least 1 [->DECL: E.f] annotation

---

### Phase 6 -- Vocabulary Audit

**Opening contract:**
This section will enumerate every distinct operation name used in phases 1-5 and map each
to its Phase 0 declaration row. Any operation not in Phase 0 will be flagged CORRECTION
with a replacement from Phase 0 named. After flagging, the correction will be applied in
the originating phase.

| Operation Used | Phase 0 Entry | Status |
|----------------|---------------|--------|
| | | MATCH / CORRECTION -- replace with: [Phase 0 name] |

**Phase 6 Closing Gate:**

- [ ] Every operation from phases 1-5 in the audit table
- [ ] All CORRECTION rows have a replacement name specified and applied
- [ ] Final scan: zero generic verbs as operation names across phases 1-5

---

**Global rules:**
1. Every field reference carries [->DECL: EntityName.fieldName]. Entity and field names must
   match Phase 0 declaration rows exactly.
2. Operation names are Phase 0 vocabulary only.
3. Generic verbs ("create", "update", "delete", "set", "get") are prohibited as operation
   names. Stop and replace before continuing.
4. Every closing gate must be completed before the next section begins. An unchecked box
   means the section is incomplete.

---

## V-03 -- Phrasing Register: ADVANCE-BLOCKED Imperatives

**Variation axis**: Phrasing register -- section transitions use `>> ADVANCE BLOCKED <<`
language with conditions that name the specific missing artifact. The blocking condition
identifies the exact element that is absent ("BLOCKED until every predicate carries
[->DECL: E.f]") rather than listing a generic requirement ("[ ] annotations present").
Sections open with a brief summary; no formal opening contract as in V-02.

**Hypothesis**: Named blocking conditions are more compliance-inducing than checklist gates
because they identify the specific absent artifact rather than requiring the model to scan
a general list and judge whether the condition applies. A condition that names
`[->DECL: EntityName.fieldName]` as the absent element is harder to overlook than a
checkbox labeled "annotations present" that the model must map to its own output.

**C-17 mechanism**: BLOCKED condition names the annotation syntax explicitly -- "BLOCKED until
every predicate carries [->DECL: EntityName.fieldName]" -- forcing the model to identify any
unannotated predicate before proceeding.

**C-18 mechanism**: BLOCKED conditions appear at every section boundary (between sections,
not only at the end), naming specific quantitative requirements: "BLOCKED if T0/T1 table has
fewer than 4 rows", "BLOCKED until vocabulary declaration has >= 3 operation rows."

**Primary targets**: C-17 and C-18 simultaneously via phrasing discipline.

---

You are running **trace-state** for Topic: `{Topic}`.

State your role in the first line of output:
- **Sales Expert** -- opportunity pipeline domain
- **Customer Service Expert** -- case and ticket lifecycle domain
- **Finance Expert** -- ledger and transaction lifecycle domain

**Artifact**: `simulations/trace/state/{topic}-state-{date}.md`

This output follows a strictly gated pipeline. At the transition between each section you
will encounter an `>> ADVANCE BLOCKED <<` condition. If the named condition is not met, do
not write the next section heading -- go back and correct the current section first.

---

### Section 1 -- Vocabulary Declaration

Declare all entity names, field names, and operation names you will reference in this trace.
This section establishes the complete token budget for sections 2-7. Any name used after this
section that does not appear here is a correction.

**Entity and Field Declaration:**

| Entity Name | Field Name | Field Type | Valid Values / Range |
|-------------|------------|------------|----------------------|
| | | | |

**Operation Declaration:**

| Operation Name | Generic Verb Replaced | Primary Entity |
|----------------|-----------------------|----------------|
| | | |

---

`>> ADVANCE BLOCKED <<` until:
- Entity declaration has at least 2 entity rows and at least 2 fields per entity
- Operation declaration has at least 3 rows with generic-verb equivalents named
- No blank cells in either table

If any condition fails, add the missing rows before writing "Section 2".

---

### Section 2 -- State Transition Chain

Trace the operation sequence as (before, op, after) triples. Minimum 4 triples. The
after-state of triple N is the before-state of triple N+1.

Every field name reference in this section -- in before-states, preconditions,
postconditions, and after-states -- must carry a `[->DECL: EntityName.fieldName]`
annotation citing its Section 1 declaration row.

```
Operation N: [Section 1 operation name]

Before-state:
  EntityName.fieldName [->DECL: EntityName.fieldName] = value
  EntityName.fieldName [->DECL: EntityName.fieldName] = value

Preconditions:
  EntityName.fieldName [->DECL: EntityName.fieldName] OPERATOR value  -- reason
  EntityName.fieldName [->DECL: EntityName.fieldName] OPERATOR value  -- reason

Postconditions:
  EntityName.fieldName [->DECL: EntityName.fieldName]: old -> new
  EntityName.fieldName [->DECL: EntityName.fieldName]: old -> new

Side effects: [events / calls / none]

After-state:
  EntityName.fieldName [->DECL: EntityName.fieldName] = value
  EntityName.fieldName [->DECL: EntityName.fieldName] = value
```

---

`>> ADVANCE BLOCKED <<` until:
- Triple count >= 4
- Every field name reference in every triple carries `[->DECL: EntityName.fieldName]`
  -- scan each triple: before-state, preconditions, postconditions, after-state;
     any unannotated field name is a blocking condition
- After-state of triple N = before-state of triple N+1 for all N
- All operation names from Section 1; zero generic verbs

If the annotation condition fails, add the missing `[->DECL:]` annotations before
writing "Section 3".

---

### Section 3 -- System Invariants

State at least 2 invariants. For each: predicate form using Section 1 vocabulary, applied
to at least one trace step, potential violations severity-classified.

```
INV-N: EntityName.fieldName [->DECL: EntityName.fieldName] OPERATOR value
  Tested at Operation N: HOLDS -- current value [actual]
                      OR VIOLATION -- current value [actual]
  Severity if violated: FATAL / DEGRADED / COSMETIC -- reason
```

---

`>> ADVANCE BLOCKED <<` until:
- Invariant count >= 2, each in predicate form with `[->DECL:]` annotations
- Each invariant tested at >= 1 trace step
- All VIOLATION outcomes severity-classified
- No unannotated field references in this section

---

### Section 4 -- Invalid Transitions

At least 1 invalid transition in baseline delta form. Failure reason must name a specific
predicate field or invariant label -- not "operation not permitted."

```
INVALID-N:
  Baseline:  EntityName.fieldName [->DECL: EntityName.fieldName] = value
  Attempted: [Section 1 operation name]
  Failure:   EntityName.fieldName [->DECL: EntityName.fieldName] OPERATOR required
             current value [actual] fails this condition
             OR INV-N violated because EntityName.fieldName [->DECL: EntityName.fieldName] = [actual]
```

---

`>> ADVANCE BLOCKED <<` until:
- At least 1 INVALID-N in baseline delta form
- Failure reason names a specific field/condition or invariant label (not generic)
- All `[->DECL:]` annotations present

---

### Section 5 -- Missing Precondition Checks

At least 1 precondition gap with assumed precondition in predicate form and risk stated.

```
GAP-N:
  Operation:  [Section 1 name]
  Assumed:    EntityName.fieldName [->DECL: EntityName.fieldName] OPERATOR value
  Enforced:   none / partial -- describe
  Risk:       what breaks
```

---

`>> ADVANCE BLOCKED <<` until:
- At least 1 GAP-N with assumed precondition in predicate form
- `[->DECL:]` annotation present on assumed precondition field reference
- Risk stated

---

### Section 6 -- Race Condition Analysis

For at least one operation, a T0/T1 concurrent interleaving table with at least 4 rows.
The VIOLATION row must name the broken invariant by label.

| Step | T0 (Actor A) | T1 (Actor B) | Shared state | Invariant status |
|------|--------------|--------------|--------------|------------------|
| 1 | | | EntityName.fieldName [->DECL: E.f] = v | HOLDS |
| 2 | | | | HOLDS |
| 3 | | | | *** VIOLATION: [INV-N] *** |
| 4 | | | | |

---

`>> ADVANCE BLOCKED <<` until:
- T0/T1 row count >= 4 -- count them: if fewer than 4 rows exist, add rows before proceeding
- At least 1 VIOLATION row with INV label named (not described, labeled -- "INV-1", "INV-2")
- Shared state column contains at least 1 `[->DECL: E.f]` annotation with Section 1 names

If the row-count condition fails, add rows to reach 4 before writing "Section 7".

---

### Section 7 -- Vocabulary Audit

Enumerate every distinct operation name used in sections 2-6. Map each to its Section 1
declaration row. Apply CORRECTION where necessary.

| Operation Used | Section 1 Entry | Status |
|----------------|-----------------|--------|
| | | MATCH / CORRECTION -- replace with: [Section 1 name] |

---

`>> ADVANCE BLOCKED <<` until:
- Every operation from sections 2-6 appears in the audit table
- All CORRECTION entries have a replacement named and applied in the source section
- Final scan: zero generic verbs as operation names across sections 2-6

---

**Global rules applied at every step:**
1. `[->DECL: EntityName.fieldName]` annotations are required on every field name reference
   in sections 2-6. The entity and field names must match Section 1 rows exactly.
2. Operation names come from Section 1 only. A new name is a correction -- add to Section 1
   first, then use.
3. Generic verbs prohibited as operation names. Stop and replace before continuing.
4. ADVANCE BLOCKED conditions are hard stops. Do not write the next section heading until
   every named blocking condition is resolved.

---

## V-04 -- Compound: Citation-Slot Template + Two-Sided Gate Contract

**Variation axis**: Compound (output format + lifecycle emphasis) -- combines V-01's
pre-printed `[->DECL: _._]` citation slots with V-02's two-sided gate contracts (opening
contract + closing gate per section).

**Mechanism**: V-01 acts at the predicate level: the slot is pre-printed, so the model fills
an annotation that already exists rather than deciding to add one. V-02 acts at the section
boundary: the opening contract names required elements before the section body is written;
the closing gate confirms each element after. The two mechanisms target different moments in
generation and do not interfere: slot-filling happens during content generation; gate-checking
happens at section transitions.

**Hypothesis**: Citation-slot scaffolding (C-17 mechanism) and two-sided prospective gate
contracts (C-18 mechanism) are independent and additive. Together they should produce both
C-17 PASS and C-18 PASS, where each variation alone achieves only one.

**Expected delta over V-01**: C-18 PASS (V-01 had closing gates only; V-04 adds opening
contracts making the gate two-sided and satisfying C-18's "appears between that section and
the next" requirement more robustly).

**Expected delta over V-02**: C-17 PASS (V-02 had instruction-based annotation; V-04
pre-prints slots making annotation structural rather than instructional).

---

You are running **trace-state** for Topic: `{Topic}`.

Choose your stock role:
- **Sales Expert** -- opportunity pipeline domain
- **Customer Service Expert** -- case and ticket lifecycle domain
- **Finance Expert** -- ledger and transaction lifecycle domain

**Artifact**: `simulations/trace/state/{topic}-state-{date}.md`

This output uses two structural enforcement mechanisms simultaneously:
1. **Citation-slot template**: every predicate position contains a pre-printed
   `[->DECL: _._]` slot; fill the entity and field name from Phase 0; a remaining `_._`
   is a visible format failure.
2. **Two-sided gate contract**: each section opens with a contract naming required output
   elements, and closes with a gate confirming each element was produced.

---

### Phase 0 -- Vocabulary Declaration

**Opening contract:**
This phase will produce: entity declarations (>= 2 entities, >= 2 fields each) and operation
declarations (>= 3 operations, each with a generic-verb equivalent named). No name may appear
in later phases without a declaration row here.

**Entity and Field Declaration:**

| Entity Name | Field Name | Field Type | Valid Values / Range |
|-------------|------------|------------|----------------------|
| [fill] | [fill] | [fill] | [fill] |
| [fill] | [fill] | [fill] | [fill] |

*(Add rows until all entities and fields are covered.)*

**Operation Declaration:**

| Operation Name | Generic Verb Replaced | Primary Entity |
|----------------|-----------------------|----------------|
| [fill] | [not: fill generic verb] | [fill] |
| [fill] | [not: fill generic verb] | [fill] |
| [fill] | [not: fill generic verb] | [fill] |

*(Add rows until all operations are covered.)*

**Phase 0 Closing Gate:**

Before opening Phase 1:
- [ ] Entity rows >= 2 entities, >= 2 fields each; all [fill] placeholders replaced
- [ ] Operation rows >= 3, all with generic equivalents named; all [fill] placeholders replaced
- [ ] No [fill] placeholders remaining in any declaration row

---

### Phase 1 -- State Transition Chain

**Opening contract:**
This phase will produce >= 4 (before, op, after) triples forming an unbroken chain.
Every field reference carries a `[->DECL: _._]` annotation (pre-printed in the template
below). Fill the entity name and field name into each `_._` from Phase 0.

Fill one block per operation:

```
Operation N: [fill: Phase 0 operation name]

Before-state:
  [fill: Entity].[fill: field] [->DECL: _._] = [fill: value]
  [fill: Entity].[fill: field] [->DECL: _._] = [fill: value]

Preconditions:
  [fill: Entity].[fill: field] [->DECL: _._] OPERATOR [fill: value]  -- [fill: reason]
  [fill: Entity].[fill: field] [->DECL: _._] OPERATOR [fill: value]  -- [fill: reason]

Postconditions:
  [fill: Entity].[fill: field] [->DECL: _._]: [fill: old] -> [fill: new]
  [fill: Entity].[fill: field] [->DECL: _._]: [fill: old] -> [fill: new]

Side effects: [fill: events / calls / none]

After-state:
  [fill: Entity].[fill: field] [->DECL: _._] = [fill: value]
  [fill: Entity].[fill: field] [->DECL: _._] = [fill: value]
```

Replace every `_._` with `Phase0Entity.phase0field`. Replace all `[fill: ...]` placeholders.

**Phase 1 Closing Gate:**

Before opening Phase 2:
- [ ] Triple count >= 4; all [fill:] placeholders replaced
- [ ] Every `[->DECL: _._]` completed -- no `_._` remaining anywhere in this phase
- [ ] After-state of triple N = before-state of triple N+1 for all N
- [ ] All operation names from Phase 0; zero generic verbs

---

### Phase 2 -- System Invariants

**Opening contract:**
This phase will produce >= 2 invariants: predicate form using Phase 0 vocabulary, each
applied to >= 1 trace step (HOLDS or VIOLATION), each potential violation severity-classified.
All `[->DECL: _._]` slots pre-printed below; fill entity and field names.

```
INV-N: [fill: Entity].[fill: field] [->DECL: _._] OPERATOR [fill: value]
  Tested at Operation N: HOLDS -- current value [fill: actual]
                      OR VIOLATION -- current value [fill: actual]
  Severity if violated: FATAL / DEGRADED / COSMETIC -- [fill: reason]
```

**Phase 2 Closing Gate:**

Before opening Phase 3:
- [ ] Invariant count >= 2; all [fill:] and `_._` placeholders replaced
- [ ] Each invariant tested at >= 1 trace step
- [ ] All VIOLATION outcomes severity-classified

---

### Phase 3 -- Invalid Transitions

**Opening contract:**
This phase will produce >= 1 invalid transition in baseline delta form. Failure reason names
a specific predicate field or invariant label. Pre-printed `[->DECL: _._]` slots below.

```
INVALID-N:
  Baseline:  [fill: Entity].[fill: field] [->DECL: _._] = [fill: value]
  Attempted: [fill: Phase 0 operation name]
  Failure:   [fill: Entity].[fill: field] [->DECL: _._] OPERATOR [fill: required]
             current value [fill: actual] fails this condition
             OR INV-[fill: N] violated because [fill: Entity].[fill: field] [->DECL: _._] = [fill: actual]
```

**Phase 3 Closing Gate:**

Before opening Phase 4:
- [ ] >= 1 INVALID-N in baseline delta form; all placeholders replaced
- [ ] Failure reason names specific field/condition or invariant label

---

### Phase 4 -- Missing Precondition Checks

**Opening contract:**
This phase will produce >= 1 precondition gap with assumed precondition in predicate form
and risk stated. Pre-printed `[->DECL: _._]` slot below.

```
GAP-N:
  Operation:  [fill: Phase 0 name]
  Assumed:    [fill: Entity].[fill: field] [->DECL: _._] OPERATOR [fill: value]
  Enforced:   none / partial -- [fill: why not enforced]
  Risk:       [fill: what breaks]
```

**Phase 4 Closing Gate:**

Before opening Phase 5:
- [ ] >= 1 GAP-N; all placeholders replaced; risk stated

---

### Phase 5 -- Race Condition Analysis

**Opening contract:**
This phase will produce a T0/T1 interleaving table with >= 4 rows. The VIOLATION row
names the broken invariant by label. Pre-printed `[->DECL: _._]` slots in the shared-state
column below; fill from Phase 0.

| Step | T0 (Actor A) | T1 (Actor B) | Shared state | Invariant status |
|------|--------------|--------------|--------------|------------------|
| 1 | [fill] | -- | [fill: Entity].[fill: field] [->DECL: _._] = [fill: v] | HOLDS |
| 2 | -- | [fill] | [fill: Entity].[fill: field] [->DECL: _._] = [fill: v'] | HOLDS |
| 3 | [fill] | -- | [fill: Entity].[fill: field] [->DECL: _._] = [fill: v''] | *** VIOLATION: INV-[fill: N] *** |
| 4 | -- | [fill] | [fill: state] | [fill: status] |

Replace all `_._` and `[fill:]` placeholders. Add rows to reach >= 4.

**Phase 5 Closing Gate:**

Before opening Phase 6:
- [ ] Row count >= 4 (count: ___); all placeholders replaced
- [ ] >= 1 VIOLATION row with INV label filled in
- [ ] >= 1 `[->DECL: E.f]` annotation in shared-state column with Phase 0 names

---

### Phase 6 -- Vocabulary Audit

**Opening contract:**
This phase will enumerate every distinct operation name used in phases 1-5 and map each to
its Phase 0 declaration row. CORRECTION entries have replacement names applied in the source.

| Operation Used | Phase 0 Entry | Status |
|----------------|---------------|--------|
| [fill] | [fill] | MATCH / CORRECTION -- replace with: [fill: Phase 0 name] |

**Phase 6 Closing Gate:**

- [ ] Every operation from phases 1-5 in the audit table; all [fill:] replaced
- [ ] All CORRECTION rows resolved; replacements applied in source phases
- [ ] Final scan: zero generic verbs as operation names in phases 1-5

---

**Output rules:**
1. `[->DECL: _._]` slots -- replace `_._` with `Phase0Entity.phase0field`. Remaining `_._`
   is a Phase Gate failure.
2. `[fill: ...]` placeholders -- replace with actual content. Remaining `[fill:]` is a Phase
   Gate failure.
3. Operation names from Phase 0 only. Generic verbs prohibited.
4. Closing gates completed before next section. Opening contracts are generation targets;
   closing gates are compliance checks.

---

## V-05 -- Compound: Full Stack (V-01 + V-02 + V-03 + All Prior Excellence)

**Variation axis**: Compound (full stack) -- all three enforcement mechanisms active
simultaneously: V-01 citation-slot templates, V-02 two-sided gate contracts, V-03
ADVANCE BLOCKED imperatives. Also incorporates all prior excellence criteria from R1-R3:
alternate error path (C-10), T0/T1 table with labeled violation (C-12), baseline delta
invalids (C-13), vocabulary declaration (C-14), vocabulary audit with mapping table (C-15),
predicate-vocabulary cross-reference (C-16), severity classification (C-09).

**Hypothesis**: All three enforcement mechanisms are complementary and non-interfering:
citation-slot templates act at the predicate (C-17 mechanism), two-sided gate contracts act
at the section boundary (C-18 mechanism), and BLOCKED imperatives provide a named backup
condition at each transition. Adding an alternate path section covers C-10. Together, these
target all 10 aspirationals simultaneously.

**Expected scoring against v4**: 10/10 aspirational (100 composite) if all mechanisms fire.
Likely failure mode: C-10 (alternate path) competes with C-12 (race table) for the model's
attention in Phase 5/6; if one is shortchanged, either C-10 or C-12 may miss the minimum.

---

You are running **trace-state** for Topic: `{Topic}`.

State your role and scenario in the first line of output:
- **Sales Expert** -- opportunity pipeline domain
- **Customer Service Expert** -- case and ticket lifecycle domain
- **Finance Expert** -- ledger and transaction lifecycle domain

**Artifact**: `simulations/trace/state/{topic}-state-{date}.md`

This output uses three simultaneous enforcement systems:
1. **Citation-slot template**: every predicate position has a pre-printed `[->DECL: _._]`
   slot; fill entity.field from Phase 0; remaining `_._` = format failure.
2. **Two-sided gate contract**: each phase opens with a contract naming required elements;
   closes with a gate confirming each element; the pair spans the phase.
3. **ADVANCE BLOCKED imperatives**: every phase transition names the specific blocking
   condition; a named condition is a hard stop -- do not write the next phase heading until
   it is resolved.

---

### Phase 0 -- Vocabulary Declaration

**Opening contract:** This phase produces entity declarations (>= 2 entities, >= 2 fields
each) and operation declarations (>= 3 operations, each with generic-verb equivalent). This
is the complete token budget for phases 1-7. No name appearing later may be absent here.

**Entity and Field Declaration:**

| Entity Name | Field Name | Field Type | Valid Values / Range |
|-------------|------------|------------|----------------------|
| [fill] | [fill] | [fill] | [fill] |
| [fill] | [fill] | [fill] | [fill] |
| [fill] | [fill] | [fill] | [fill] |
| [fill] | [fill] | [fill] | [fill] |

**Operation Declaration:**

| Operation Name | Generic Verb Replaced | Primary Entity |
|----------------|-----------------------|----------------|
| [fill] | [not: fill] | [fill] |
| [fill] | [not: fill] | [fill] |
| [fill] | [not: fill] | [fill] |

*(Add rows for all operations. Each row maps to a later triple.)*

**Phase 0 Closing Gate:**

- [ ] Entity rows: >= 2 entities, >= 2 fields each; no [fill] remaining
- [ ] Operation rows: >= 3, generic equivalents named; no [fill] remaining

`>> ADVANCE BLOCKED <<` until both boxes are checked. Add missing rows before writing "Phase 1".

---

### Phase 1 -- State Transition Chain

**Opening contract:** This phase produces >= 4 (before, op, after) triples forming an
unbroken chain. Every field reference carries `[->DECL: _._]` (pre-printed; fill from Phase 0).
After-state of triple N equals before-state of triple N+1.

Fill one block per operation. Produce >= 4 blocks.

```
Operation N: [fill: Phase 0 operation name]

Before-state:
  [fill: Entity].[fill: field] [->DECL: _._] = [fill: value]
  [fill: Entity].[fill: field] [->DECL: _._] = [fill: value]

Preconditions:
  [fill: Entity].[fill: field] [->DECL: _._] OPERATOR [fill: value]  -- [fill: reason]
  [fill: Entity].[fill: field] [->DECL: _._] OPERATOR [fill: value]  -- [fill: reason]

Postconditions:
  [fill: Entity].[fill: field] [->DECL: _._]: [fill: old] -> [fill: new]
  [fill: Entity].[fill: field] [->DECL: _._]: [fill: old] -> [fill: new]

Side effects: [fill: events / calls / none]

After-state:
  [fill: Entity].[fill: field] [->DECL: _._] = [fill: value]
  [fill: Entity].[fill: field] [->DECL: _._] = [fill: value]
```

Replace every `_._` with `Phase0Entity.phase0field`. Replace all `[fill:]`.

**Phase 1 Closing Gate:**

- [ ] Triple count >= 4; no [fill:] or `_._` remaining
- [ ] Every field reference annotated -- scan each triple for unannotated field names
- [ ] Chain unbroken: after-state N = before-state N+1
- [ ] All operation names from Phase 0; zero generic verbs

`>> ADVANCE BLOCKED <<` until every box is checked.
If annotation box fails: scan every triple, add `[->DECL: Phase0Entity.phase0field]` to
any unannotated field reference, then recheck.

---

### Phase 2 -- System Invariants

**Opening contract:** This phase produces >= 2 invariants: predicate form, each tested at
>= 1 trace step, each potential violation severity-classified. All `[->DECL: _._]` pre-printed.

```
INV-N: [fill: Entity].[fill: field] [->DECL: _._] OPERATOR [fill: value]
  Tested at Operation N: HOLDS -- current value [fill: actual]
                      OR VIOLATION -- current value [fill: actual]
  Severity if violated: FATAL / DEGRADED / COSMETIC -- [fill: reason]
```

**Phase 2 Closing Gate:**

- [ ] Invariant count >= 2; no [fill:] or `_._` remaining
- [ ] Each invariant tested at >= 1 step; HOLDS or VIOLATION marked
- [ ] All VIOLATION outcomes severity-classified

`>> ADVANCE BLOCKED <<` until every box is checked.

---

### Phase 3 -- Invalid Transitions

**Opening contract:** This phase produces >= 1 INVALID-N in baseline delta form. Failure
reason names a specific predicate field or invariant label.

```
INVALID-N:
  Baseline:  [fill: Entity].[fill: field] [->DECL: _._] = [fill: value]
  Attempted: [fill: Phase 0 operation name]
  Failure:   [fill: Entity].[fill: field] [->DECL: _._] OPERATOR [fill: required]
             current value [fill: actual] fails this condition
             OR INV-[fill: N] violated because [fill: Entity].[fill: field] [->DECL: _._] = [fill: actual]
```

**Phase 3 Closing Gate:**

- [ ] >= 1 INVALID-N in baseline delta form; no [fill:] or `_._` remaining
- [ ] Failure reason names specific field/condition or invariant label

`>> ADVANCE BLOCKED <<` until every box is checked.

---

### Phase 4 -- Missing Precondition Checks

**Opening contract:** This phase produces >= 1 GAP-N with assumed precondition in predicate
form and risk stated.

```
GAP-N:
  Operation:  [fill: Phase 0 name]
  Assumed:    [fill: Entity].[fill: field] [->DECL: _._] OPERATOR [fill: value]
  Enforced:   none / partial -- [fill: why]
  Risk:       [fill: what breaks]
```

**Phase 4 Closing Gate:**

- [ ] >= 1 GAP-N; no [fill:] or `_._` remaining; risk stated

`>> ADVANCE BLOCKED <<` until the box is checked.

---

### Phase 5 -- Alternate / Error Path

**Opening contract:** This phase traces at least one alternate path -- an error response,
retry, or compensating transaction returning the system to a valid state. The alternate path
has >= 3 steps. It is labeled "alternate path" or "error path."

```
Alternate path: [fill: name -- e.g., "cancellation after failed payment"]

Step N: [fill: Phase 0 operation name]
  Before:  [fill: Entity].[fill: field] [->DECL: _._] = [fill: value]
  Trigger: [fill: what caused this branch]
  Post:    [fill: Entity].[fill: field] [->DECL: _._]: [fill: old] -> [fill: new]
  After:   [fill: Entity].[fill: field] [->DECL: _._] = [fill: recovery value]
```

**Phase 5 Closing Gate:**

- [ ] Alternate path clearly labeled; >= 3 steps
- [ ] Recovery state named (the state the system returns to after the error path)
- [ ] All `[->DECL: _._]` slots filled with Phase 0 names

`>> ADVANCE BLOCKED <<` until every box is checked.

---

### Phase 6 -- Race Condition Analysis

**Opening contract:** This phase produces a T0/T1 interleaving table with >= 4 rows. The
VIOLATION row names the broken invariant by label. Pre-printed `[->DECL: _._]` slots in the
shared-state column.

```
Operation analyzed: [fill: Phase 0 name]
Race scenario: [fill: two concurrent actors and their conflicting actions]
```

| Step | T0 (Actor A) | T1 (Actor B) | Shared state | Invariant status |
|------|--------------|--------------|--------------|------------------|
| 1 | [fill] | -- | [fill: Entity].[fill: field] [->DECL: _._] = [fill: v] | HOLDS |
| 2 | -- | [fill] | [fill: Entity].[fill: field] [->DECL: _._] = [fill: v'] | HOLDS |
| 3 | [fill] | -- | [fill: Entity].[fill: field] [->DECL: _._] = [fill: v''] | *** VIOLATION: INV-[fill: N] *** |
| 4 | -- | [fill] | [fill: state] | [fill: status] |

Add rows until >= 4. Replace all `_._` and `[fill:]`.

**Phase 6 Closing Gate:**

- [ ] Row count >= 4 (count: ___); all placeholders replaced
- [ ] >= 1 VIOLATION row with INV label filled (not described)
- [ ] >= 1 `[->DECL: E.f]` annotation completed in shared-state column

`>> ADVANCE BLOCKED <<` if row count < 4: add rows before writing "Phase 7".
`>> ADVANCE BLOCKED <<` if VIOLATION row absent: add the interleaving step where the
invariant breaks before writing "Phase 7".

---

### Phase 7 -- Vocabulary Audit

**Opening contract:** This phase enumerates every distinct operation name used in phases 1-6,
maps each to its Phase 0 declaration row, and applies corrections for any name not in Phase 0.
After corrections, a final scan confirms zero generic verbs remain.

| Operation Used | Phase 0 Entry | Status |
|----------------|---------------|--------|
| [fill] | [fill] | MATCH / CORRECTION -- replace with: [fill: Phase 0 name] |

Apply all CORRECTION replacements in the source phases before closing this gate.

**Phase 7 Closing Gate:**

- [ ] Every operation from phases 1-6 in the table; all [fill:] replaced
- [ ] All CORRECTION entries resolved and applied
- [ ] Final scan: zero generic verbs as operation names in phases 1-6

`>> ADVANCE BLOCKED <<` until every box is checked and all corrections applied.

---

**Global enforcement rules:**

1. **Citation slots**: Replace every `_._` in `[->DECL: _._]` with `Phase0Entity.phase0field`.
   A remaining `_._` is a closing gate failure for that phase.

2. **Fill placeholders**: Replace every `[fill: ...]` with actual content before the closing
   gate. A remaining `[fill:]` is a closing gate failure.

3. **BLOCKED discipline**: ADVANCE BLOCKED conditions are hard stops. Do not write the next
   phase heading until every named condition is resolved. If an annotation condition fails,
   scan the entire current phase and add the missing annotations; then recheck.

4. **Vocabulary discipline**: Operation names from Phase 0 only. A new name in any phase is
   a CORRECTION -- add to Phase 0 first. Generic verbs prohibited as operation names.

5. **Chain discipline**: After-state of triple N is the before-state of triple N+1. Any
   contradiction between adjacent states means at least one triple is incomplete.

---

## Expected Scoring Against v4

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Essential | PASS | PASS | PASS | PASS | PASS |
| C-02 Essential | PASS | PASS | PASS | PASS | PASS |
| C-03 Essential | PASS | PASS | PASS | PASS | PASS |
| C-04 Essential | PASS | PASS | PASS | PASS | PASS |
| C-05 Essential | PASS | PASS | PASS | PASS | PASS |
| C-06 Recommended | PASS | PASS | PASS | PASS | PASS |
| C-07 Recommended | PASS | PASS | PASS | PASS | PASS |
| C-08 Recommended | PASS | PASS | PASS | PASS | PASS |
| C-09 Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-10 Aspirational | FAIL | FAIL | FAIL | FAIL | PASS |
| C-11 Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-12 Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-13 Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-14 Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-15 Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-16 Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-17 Aspirational | PASS | ? | PASS | PASS | PASS |
| C-18 Aspirational | PASS | PASS | PASS | PASS | PASS |
| **Aspirational** | **9/10** | **8/10** | **9/10** | **9/10** | **10/10** |
| **Composite** | **99** | **98** | **99** | **99** | **100** |

**Notes on uncertainty:**

- **V-01 C-17**: Pre-printed slots are the strongest C-17 mechanism. High confidence PASS.
  C-18 PASS from closing gates per section (6 sections, each with a named-element checklist).

- **V-02 C-17**: Instruction-based ("every field reference carries [->DECL: E.f]") without
  slot scaffolding. C-17 compliance depends on the model following the instruction at every
  predicate. Marked `?` -- likely PASS but less certain than V-01. C-18 PASS from two-sided
  gates (opening contract + closing gate per section = strongest C-18 mechanism).

- **V-03 C-17 and C-18**: BLOCKED conditions name the exact missing artifact. Confident PASS
  on both but depends on the BLOCKED language being interpreted as a hard stop rather than
  a suggestion. C-10 FAIL (no alternate path section).

- **V-04**: Both slot template (C-17) and two-sided gate (C-18). Strongest combined
  guarantee. C-10 FAIL (no alternate path section in this variation).

- **V-05 C-10**: Dedicated Phase 5 alternate path section. PASS if model produces >= 3
  steps with recovery state named. The only variation targeting all 10 aspirationals.

**Key test**: V-01 vs V-03 for C-17. V-01 uses structural scaffolding (fill the blank);
V-03 uses named BLOCKED language (name the absent annotation). Which mechanism achieves
higher per-predicate annotation density? If V-03 matches V-01 on C-17, BLOCKED language
alone is sufficient for annotation compliance. If V-01 exceeds V-03, structural scaffolding
is the necessary mechanism.

**Key test**: V-02 vs V-01 for C-18. V-01 has closing gates only; V-02 has two-sided
(opening + closing) gates. If V-02 scores higher on C-18 correctness (e.g., fewer gates
omitting required elements), the prospective opening contract adds genuine compliance beyond
the retrospective closing check alone.
