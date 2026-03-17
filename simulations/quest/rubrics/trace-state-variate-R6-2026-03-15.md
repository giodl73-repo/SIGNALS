# trace-state Skill -- Quest Variations Round 6

**Skill**: trace-state
**Round**: 6 (building on R5 golden base; rubric v6, 15 aspirationals)
**Rubric**: v6 (C-01--C-23; composite = E/5*60 + R/3*30 + A/15*10)
**R5 baseline**: V-01 13/15 (98.67), V-02 14/15 (99.33, earned C-22), V-03 14/15 (99.33, earned C-23). All golden.
**R5 gap**: No variation passed both C-22 and C-23 simultaneously. V-02 passed C-22 (REQUIRES/CONTENT/COUNT-AND-CHECK/GATE layers); V-03 passed C-23 (SD-N standing directives at document level).

---

## Variation Map

| V | Axis | Primary Targets | Key Structural Change |
|---|------|-----------------|-----------------------|
| V-01 | Compliance compound | C-22 + C-23 | Finance: SD-N standing directive block at document header + REQUIRES/CONTENT/COUNT-AND-CHECK/GATE four-layer architecture in every section |
| V-02 | Role sequence | C-22 baseline | Sales: four-layer phase architecture without SD-N block -- tests C-22 portability to Sales domain |
| V-03 | Phrasing register | C-23 baseline | Finance: SD-N standing directives + MUST/BLOCKED imperative phrasing, sections use Opening-Contract/Gate style (not four-layer) -- isolates C-23 with register change |
| V-04 | Compound role | C-22 + C-23 | Customer Service: same compound structure as V-01 -- tests domain portability |
| V-05 | Compound + phrasing | C-22 + C-23 | Finance: V-01 compound + MUST/BLOCKED/ADVANCE imperative markers at every layer boundary |

**Single-axis hypotheses:**
- V-01 vs V-04: Does Finance vs CS domain affect whether a prompt satisfying both C-22 and C-23 earns both?
- V-02: Phase architecture alone (no SD-N) earns C-22 but not C-23 -- does Sales domain match R5 V-02 result?
- V-03: SD-N alone (no phase layers) earns C-23 but not C-22 -- does imperative phrasing change this split?

---

## V-01 -- Finance, Compound (SD-N + REQUIRES/CONTENT/COUNT-AND-CHECK/GATE)

**Variation axis**: Compliance compound -- document-level standing directives (C-23) combined with
four-layer phase architecture (C-22) in the Finance domain.

**Hypothesis**: The SD-N block declares global compliance policy once; the REQUIRES/CONTENT/
COUNT-AND-CHECK/GATE architecture makes compliance the structural identity of every section.
These two mechanisms solve the same compliance-reliability problem from orthogonal angles and
can coexist in a single prompt. A prompt with both earns C-22 (architecture) and C-23 (global
policy) simultaneously, yielding 15/15 aspirationals.

**Target gaps**: C-22, C-23

---

You are a **Finance domain expert**. Your task is to hand-compile state transitions for a
financial entity (ledger entry, invoice, payment, or account), identify invalid transitions,
missing precondition checks, invariant violations, and race conditions, and produce a
structured trace-state report by following every section below in order.

---

### STANDING DIRECTIVES

The following standing directives apply to every section in this trace without repetition.
All sections comply by reference to these directives. Do not repeat the directive text in
any section -- compliance is assumed from this point forward.

**SD-1 (Predicate Annotations):** Every predicate field in every precondition and
postcondition carries an inline `[->DECL: EntityName.fieldName]` annotation identifying the
Section 0 declaration entry it was drawn from. A predicate missing this annotation is
structurally incomplete.

**SD-2 (Slot Enforcement):** Every `[->DECL: _._]` slot is filled before writing any
adjacent value in the same template row. An unfilled `_._` slot is a structural gap
detectable by inspection; the COUNT-AND-CHECK layer of every section confirms none remain.

**SD-3 (Section Architecture):** Every section in this trace is structured as exactly four
named layers in this order: **REQUIRES → CONTENT → COUNT-AND-CHECK → GATE**. This is not an
instruction to remember -- it is the format. Completing REQUIRES and writing CONTENT is what
every section is. Reaching COUNT-AND-CHECK and GATE is what every section does. A section
missing any of these four layers is architecturally incomplete and cannot be sealed.

---

### SECTION 0: VOCABULARY DECLARATION

#### REQUIRES

Section 0 must produce before its GATE releases:
- [ ] Entity table: min 2 Finance entities, each with ≥ 3 named fields and SD-1 annotations
- [ ] Operation table: min 5 Finance operations using domain verbs; generic-verb equivalents listed and prohibited
- [ ] Invariant table: min 3 invariants; ≥ 1 numeric with falsifiable threshold; ≥ 1 temporal

#### CONTENT

*Entity and Field Registry*

| ENT-ID | Entity Name            | Field                  | Type   |
|--------|------------------------|------------------------|--------|
| E-01   | [->DECL: _._]          | [->DECL: _._]          |        |
| E-01   | [->DECL: _._]          | [->DECL: _._]          |        |
| E-01   | [->DECL: _._]          | [->DECL: _._]          |        |
| E-02   | [->DECL: _._]          | [->DECL: _._]          |        |
| E-02   | [->DECL: _._]          | [->DECL: _._]          |        |
| E-02   | [->DECL: _._]          | [->DECL: _._]          |        |

*Operation Registry*

| OP-ID | Domain Verb (Finance) | Description                        | Prohibited Generic Equivalent |
|-------|-----------------------|------------------------------------|-------------------------------|
| OP-01 |                       |                                    | update / set                  |
| OP-02 |                       |                                    | create / add                  |
| OP-03 |                       |                                    | delete / remove               |
| OP-04 |                       |                                    | change / modify               |
| OP-05 |                       |                                    | get / fetch                   |

*Invariant Registry*

| INV-ID | Invariant Statement                                        | Scope     | Severity             | Falsifiable Threshold |
|--------|-------------------------------------------------------------|-----------|----------------------|-----------------------|
| INV-01 | [->DECL: _._].[->DECL: _._] [op] [->DECL: _._]            | All states| FATAL/DEGRADED/COSMETIC |                    |
| INV-02 | [->DECL: _._].[->DECL: _._] [op] [->DECL: _._]            | All states| FATAL/DEGRADED/COSMETIC |                    |
| INV-03 | [->DECL: _._].[->DECL: _._] [op] [->DECL: _._]            | Specific  | FATAL/DEGRADED/COSMETIC |                    |

#### COUNT-AND-CHECK

Count entities declared: ___. If fewer than 2, add entities before proceeding.
Count operations declared: ___. If fewer than 5, add operations before proceeding.
Count invariants declared: ___. If fewer than 3, add invariants before proceeding.
Count `[->DECL: _._]` slots remaining unfilled: ___. If any remain, fill before proceeding.

#### GATE -- Section 0

All REQUIRES checklist items satisfied? [ ] Yes  [ ] No -- if No, complete missing items before proceeding.
COUNT-AND-CHECK all minimums met? [ ] Yes  [ ] No -- if No, add missing entries before proceeding.
SD-1 annotations present in all predicate positions? [ ] Yes  [ ] No -- if No, fill before proceeding.
**Section 0 SEALED → Section 1 now OPEN.**

---

### SECTION 1: INVARIANT ANALYSIS

#### REQUIRES

Section 1 must produce before its GATE releases:
- [ ] Severity classification (FATAL / DEGRADED / COSMETIC) for every INV-ID from Section 0
- [ ] Every invariant tested against ≥ 1 trace step (forward reference to Section 2 is permitted)
- [ ] Missing-precondition risk table: ≥ 1 entry naming a check the system does not enforce

#### CONTENT

*Invariant Testing Table*

| INV-ID | Invariant (from Section 0)    | Severity             | Tested at Step | Holds / Violated | If Violated: Reason |
|--------|-------------------------------|----------------------|---------------|-----------------|---------------------|
| INV-01 | [->DECL: _._]                 | FATAL/DEGRADED/COSMETIC | Step ___   | Holds / Violated |                     |
| INV-02 | [->DECL: _._]                 | FATAL/DEGRADED/COSMETIC | Step ___   | Holds / Violated |                     |
| INV-03 | [->DECL: _._]                 | FATAL/DEGRADED/COSMETIC | Step ___   | Holds / Violated |                     |

*Missing Precondition Risk Table*

| OP-ID | Precondition Not Enforced by System | Risk if Unchecked      |
|-------|-------------------------------------|------------------------|
|       | [->DECL: _._].[->DECL: _._] [op] [value] -- assumed, not checked |          |

#### COUNT-AND-CHECK

Count invariants with severity classifications: ___. If fewer than 3, add classifications before proceeding.
Count invariants with step references: ___. If fewer than 2, add forward references before proceeding.
Count missing-precondition entries: ___. If fewer than 1, add an entry before proceeding.
Count `[->DECL: _._]` slots remaining unfilled: ___. If any remain, fill before proceeding.

#### GATE -- Section 1

All REQUIRES items satisfied? [ ] Yes  [ ] No
COUNT-AND-CHECK all minimums met? [ ] Yes  [ ] No
**Section 1 SEALED → Section 2 now OPEN.**

---

### SECTION 2: HAND-COMPILED STATE TRANSITION TRACE

#### REQUIRES

Section 2 must produce before its GATE releases:
- [ ] Min 6 numbered steps; each has before-state (S-ID), operation (OP-ID), after-state (S-ID)
- [ ] Every step: ≥ 1 precondition in predicate notation `[->DECL: E.field] OPERATOR [value] -- PASS / FAIL`
- [ ] Every step: ≥ 1 postcondition in mutation notation `[->DECL: E.field]: [old] -> [new]`
- [ ] ≥ 1 step labeled [REJECTED] where a guard fires and the entity stays in its before-state
- [ ] ≥ 1 labeled "Alternate / Error Path" subsection with min 3 steps

#### CONTENT

*Happy Path*

Step template (use for every step; do not deviate):

```
Step N: [OP-ID] [Finance Operation Name]    [PASS / REJECTED]
  Before:  [S-ID] [State Name] -- { [->DECL: E.field]: value, [->DECL: E.field]: value }
  Preconditions:
    [->DECL: EntityName.fieldName] OPERATOR [value]  -- PASS / FAIL
    [->DECL: EntityName.fieldName] OPERATOR [value]  -- PASS / FAIL
  Guard:   passes -- continue  /  fires -- reason: [specific predicate text]
  After:   [S-ID] [State Name] -- { [->DECL: E.field]: value, [->DECL: E.field]: value }
    [REJECTED: entity remains in before-state; confirm field-for-field match]
  Postconditions:
    [->DECL: EntityName.fieldName]: [old_value] -> [new_value]
    [->DECL: EntityName.fieldName]: unchanged
```

*(Write minimum 6 steps here using this template. Mark at least one [REJECTED].)*

*Alternate / Error Path -- [scenario name]*

*(Write minimum 3 steps showing error or recovery, using the same step template.)*

#### COUNT-AND-CHECK

Count happy-path steps: ___. If fewer than 6, add steps before proceeding.
Count steps with predicate preconditions: ___. Must equal total steps. If fewer, add missing predicates before proceeding.
Count steps with mutation postconditions: ___. Must equal total steps. If fewer, add missing postconditions before proceeding.
Count [REJECTED] steps: ___. If fewer than 1, add a rejected step before proceeding.
Count alternate-path steps: ___. If fewer than 3, extend alternate path before proceeding.
Count `[->DECL: _._]` slots remaining unfilled: ___. If any remain, fill before proceeding.

#### GATE -- Section 2

All REQUIRES items satisfied? [ ] Yes  [ ] No
COUNT-AND-CHECK all minimums met? [ ] Yes  [ ] No
**Section 2 SEALED → Section 3 now OPEN.**

---

### SECTION 3: RACE CONDITION ANALYSIS

#### REQUIRES

Section 3 must produce before its GATE releases:
- [ ] ≥ 1 named race scenario: two concurrent Finance actors, one targeted operation (OP-ID)
- [ ] T0/T1 two-column interleaving table with min 4 rows
- [ ] Row where invariant breaks is marked with INV-ID citation
- [ ] Severity label (FATAL / DEGRADED / COSMETIC) for the violation

#### CONTENT

*Race Scenario: [Name the Finance scenario]*

Two actors attempting [OP-ID: operation] concurrently on the same [entity]:

| Time | Actor T0                                              | Actor T1                                              |
|------|-------------------------------------------------------|-------------------------------------------------------|
| t=0  | [->DECL: _._]: reads [->DECL: _._] = [value]         | [->DECL: _._]: reads [->DECL: _._] = [value]         |
| t=1  | [->DECL: _._] OPERATOR [value] -- PASS (stale)        | waits                                                 |
| t=2  | [->DECL: _._]: [old] -> [new] (write commits)         | [->DECL: _._] OPERATOR [value] -- PASS (stale)        |
| t=3  | completes                                             | [->DECL: _._]: [old] -> [new] -- **[INV-ID] VIOLATED**|

Invariant broken: [INV-ID] -- [statement from Section 0]
Severity: FATAL / DEGRADED / COSMETIC

#### COUNT-AND-CHECK

Count race scenarios: ___. If fewer than 1, add a scenario before proceeding.
Count T0/T1 rows: ___. If fewer than 4, add rows before proceeding.
Count rows with INV-ID violation citation: ___. If fewer than 1, add INV-ID before proceeding.
Count `[->DECL: _._]` slots remaining unfilled: ___. If any remain, fill before proceeding.

#### GATE -- Section 3

All REQUIRES items satisfied? [ ] Yes  [ ] No
COUNT-AND-CHECK all minimums met? [ ] Yes  [ ] No
**Section 3 SEALED → Section 4 now OPEN.**

---

### SECTION 4: INVALID TRANSITION ANALYSIS

#### REQUIRES

Section 4 must produce before its GATE releases:
- [ ] ≥ 2 invalid transitions in structured baseline-delta form: `(baseline_state, attempted_delta, failure_reason)`
- [ ] Missing-check column: names the system gap for each invalid transition
- [ ] Risk-if-unchecked for each missing check

#### CONTENT

*Invalid Transition Table*

| Delta-ID | Baseline State (S-ID) | Attempted Delta (OP-ID) | Failure Reason                               | Missing Check                           | Risk if Unchecked |
|----------|-----------------------|-------------------------|----------------------------------------------|-----------------------------------------|-------------------|
| IT-01    | [->DECL: _._]         | [->DECL: _._]           | [->DECL: E.field] OPERATOR [value] FAILS     |                                         |                   |
| IT-02    | [->DECL: _._]         | [->DECL: _._]           | [INV-ID] [->DECL: E.field] threshold breached|                                         |                   |

#### COUNT-AND-CHECK

Count invalid transitions in structured delta form: ___. If fewer than 2, add entries before proceeding.
Count entries with non-empty Missing Check column: ___. If fewer than 1, add a missing-check entry before proceeding.
Count `[->DECL: _._]` slots remaining unfilled: ___. If any remain, fill before proceeding.

#### GATE -- Section 4

All REQUIRES items satisfied? [ ] Yes  [ ] No
COUNT-AND-CHECK all minimums met? [ ] Yes  [ ] No
**Section 4 SEALED → Section 5 now OPEN.**

---

### SECTION 5: VOCABULARY AUDIT

#### REQUIRES

Section 5 must produce before its GATE releases:
- [ ] Enumerated table mapping every distinct operation name used in Sections 2-4 to its Section 0 OP-ID
- [ ] Any operation not in Section 0 explicitly flagged as UNDECLARED
- [ ] Generic verb scan confirms no prohibited verbs in any operation name

#### CONTENT

*Operation Name Audit Table*

| Audit-ID | Operation Name Used | Section 0 OP-ID | Generic Verb? | Status       |
|----------|---------------------|-----------------|---------------|--------------|
| A-01     |                     |                 | Yes / No      | Declared / UNDECLARED |
| A-02     |                     |                 | Yes / No      | Declared / UNDECLARED |
| A-03     |                     |                 | Yes / No      | Declared / UNDECLARED |
| A-04     |                     |                 | Yes / No      | Declared / UNDECLARED |
| A-05     |                     |                 | Yes / No      | Declared / UNDECLARED |

Generic verbs scanned: update, create, delete, change, set, get, modify, add, remove
Found in any operation name: Yes / No -- if Yes, list and flag each instance.

#### COUNT-AND-CHECK

Count operation names audited: ___. Must equal total distinct operations in Sections 2-4. If fewer, add missing entries before proceeding.
Count UNDECLARED entries: ___. If any found, flag for remediation before proceeding.
Count generic verb violations: ___. If any found, flag for remediation before proceeding.

#### GATE -- Section 5

All REQUIRES items satisfied? [ ] Yes  [ ] No
COUNT-AND-CHECK all minimums met? [ ] Yes  [ ] No
Generic verb drift check clean? [ ] Yes  [ ] No
**Section 5 COMPLETE. Trace is complete.**

---

## V-02 -- Sales, Phase Architecture Only (No SD-N)

**Variation axis**: Role sequence -- Sales domain with REQUIRES/CONTENT/COUNT-AND-CHECK/GATE
four-layer architecture, no global standing directive block.

**Hypothesis**: The phase-layer architecture (C-22) is portable to the Sales domain. Without
an SD-N block at document level, C-23 cannot be earned. Result should match R5 V-02:
14/15 aspirationals (C-22 pass, C-23 fail), confirming that role-domain change does not
alter the C-22/C-23 split when only one mechanism is present.

**Target gaps**: C-22 (role portability baseline)

---

You are a **Sales domain expert**. Your task is to hand-compile state transitions for a
Sales entity (Opportunity, Deal, Account, or Quote), identify invalid transitions, missing
precondition checks, invariant violations, and race conditions, and produce a structured
trace-state report by following every section below in order.

Every section in this trace is structured as exactly four named layers:
**REQUIRES → CONTENT → COUNT-AND-CHECK → GATE**

Following this structure is compliance. Each layer is a mandatory step in the format, not an
optional instruction. A section missing any of these four layers is architecturally incomplete.

---

### SECTION 0: VOCABULARY DECLARATION

#### REQUIRES

Section 0 must produce before its GATE releases:
- [ ] Entity table: min 2 Sales entities (e.g., Opportunity, Account), each with ≥ 3 named fields
- [ ] Operation table: min 5 Sales operations using domain verbs (qualify, advance, close_won, etc.)
- [ ] Generic-verb prohibition list: ≥ 3 domain-verb/generic-verb pairs
- [ ] Invariant table: min 3 invariants; ≥ 1 numeric; ≥ 1 temporal

#### CONTENT

*Entity and Field Registry*

| ENT-ID | Entity Name    | Field                | Type | Notes |
|--------|----------------|----------------------|------|-------|
| E-01   |                |                      |      |       |
| E-01   |                |                      |      |       |
| E-01   |                |                      |      |       |
| E-02   |                |                      |      |       |
| E-02   |                |                      |      |       |
| E-02   |                |                      |      |       |

*Operation Registry*

| OP-ID | Sales Domain Verb        | Description                     | Prohibited Generic Equivalent |
|-------|--------------------------|---------------------------------|-------------------------------|
| OP-01 |                          |                                 | update / set                  |
| OP-02 |                          |                                 | create / add                  |
| OP-03 |                          |                                 | change / modify               |
| OP-04 |                          |                                 | delete / remove               |
| OP-05 |                          |                                 | get / fetch                   |

*Invariant Registry*

| INV-ID | Invariant Statement                          | Scope     | Severity             | Falsifiable Threshold |
|--------|----------------------------------------------|-----------|----------------------|-----------------------|
| INV-01 |                                              | All states| FATAL/DEGRADED/COSMETIC |                    |
| INV-02 |                                              | All states| FATAL/DEGRADED/COSMETIC |                    |
| INV-03 |                                              | Specific  | FATAL/DEGRADED/COSMETIC |                    |

In all predicate fields below, annotate every entity-field reference as `[->DECL: EntityName.fieldName]`
drawn from the Entity Registry above.

#### COUNT-AND-CHECK

Count entities declared: ___. If fewer than 2, add entities before proceeding.
Count operations declared: ___. If fewer than 5, add operations before proceeding.
Count invariants declared: ___. If fewer than 3, add invariants before proceeding.

#### GATE -- Section 0

All REQUIRES checklist items satisfied? [ ] Yes  [ ] No
COUNT-AND-CHECK all minimums met? [ ] Yes  [ ] No
**Section 0 SEALED → Section 1 now OPEN.**

---

### SECTION 1: INVARIANT ANALYSIS

#### REQUIRES

Section 1 must produce before its GATE releases:
- [ ] Severity classification for every INV-ID
- [ ] Each invariant tested against ≥ 1 trace step
- [ ] ≥ 1 missing-precondition entry with risk statement

#### CONTENT

*Invariant Testing Table*

| INV-ID | Invariant                    | Severity             | Tested at Step | Holds / Violated | Reason if Violated |
|--------|------------------------------|----------------------|---------------|-----------------|---------------------|
| INV-01 |                              | FATAL/DEGRADED/COSMETIC | Step ___   |                 |                     |
| INV-02 |                              | FATAL/DEGRADED/COSMETIC | Step ___   |                 |                     |
| INV-03 |                              | FATAL/DEGRADED/COSMETIC | Step ___   |                 |                     |

*Missing Precondition Risk Table*

| OP-ID | Precondition Not Enforced by System       | Risk if Unchecked |
|-------|-------------------------------------------|-------------------|
|       |                                           |                   |

#### COUNT-AND-CHECK

Count invariants with severity: ___. If fewer than 3, add before proceeding.
Count invariants with step references: ___. If fewer than 2, add forward references before proceeding.
Count missing-precondition entries: ___. If fewer than 1, add an entry before proceeding.

#### GATE -- Section 1

All REQUIRES items satisfied? [ ] Yes  [ ] No
COUNT-AND-CHECK all minimums met? [ ] Yes  [ ] No
**Section 1 SEALED → Section 2 now OPEN.**

---

### SECTION 2: HAND-COMPILED STATE TRANSITION TRACE

#### REQUIRES

Section 2 must produce before its GATE releases:
- [ ] Min 6 numbered steps with before-state (S-ID), operation (OP-ID), after-state (S-ID)
- [ ] ≥ 1 precondition per step: `[->DECL: E.field] OPERATOR [value] -- PASS / FAIL`
- [ ] ≥ 1 postcondition per step: `[->DECL: E.field]: [old] -> [new]`
- [ ] ≥ 1 [REJECTED] step
- [ ] ≥ 1 labeled "Alternate / Error Path" subsection with min 3 steps

#### CONTENT

*Happy Path*

Step template:
```
Step N: [OP-ID] [Sales Operation Name]    [PASS / REJECTED]
  Before:  [S-ID] [State Name] -- { [->DECL: E.field]: value, [->DECL: E.field]: value }
  Preconditions:
    [->DECL: EntityName.fieldName] OPERATOR [value]  -- PASS / FAIL
  Guard:   passes / fires -- reason: [text]
  After:   [S-ID] [State Name] -- { [->DECL: E.field]: value, [->DECL: E.field]: value }
  Postconditions:
    [->DECL: EntityName.fieldName]: [old] -> [new]
```

*(Write min 6 steps. Mark ≥ 1 as [REJECTED].)*

*Alternate / Error Path -- [scenario name]*

*(Write min 3 steps.)*

#### COUNT-AND-CHECK

Count steps: ___. If fewer than 6, add steps before proceeding.
Count [REJECTED] steps: ___. If fewer than 1, add a rejected step before proceeding.
Count alternate-path steps: ___. If fewer than 3, extend before proceeding.

#### GATE -- Section 2

All REQUIRES items satisfied? [ ] Yes  [ ] No
COUNT-AND-CHECK all minimums met? [ ] Yes  [ ] No
**Section 2 SEALED → Section 3 now OPEN.**

---

### SECTION 3: RACE CONDITION ANALYSIS

#### REQUIRES

Section 3 must produce before its GATE releases:
- [ ] ≥ 1 named race scenario with two Sales-domain actors
- [ ] T0/T1 table with min 4 rows
- [ ] Violation row marked with INV-ID
- [ ] Severity label

#### CONTENT

*Race Scenario: [Name]*

| Time | Actor T0                                        | Actor T1                                        |
|------|-------------------------------------------------|-------------------------------------------------|
| t=0  | reads [->DECL: E.field] = [value]               | reads [->DECL: E.field] = [value]               |
| t=1  | [->DECL: E.field] OPERATOR [value] -- PASS      | waits                                           |
| t=2  | [->DECL: E.field]: [old] -> [new]               | [->DECL: E.field] OPERATOR [value] -- PASS (stale) |
| t=3  | completes                                       | [->DECL: E.field]: [old] -> [new] -- **[INV-ID] VIOLATED** |

Severity: FATAL / DEGRADED / COSMETIC

#### COUNT-AND-CHECK

Count race scenarios: ___. If fewer than 1, add before proceeding.
Count T0/T1 rows: ___. If fewer than 4, add rows before proceeding.
Count violation rows with INV-ID: ___. If fewer than 1, add citation before proceeding.

#### GATE -- Section 3

All REQUIRES items satisfied? [ ] Yes  [ ] No
COUNT-AND-CHECK all minimums met? [ ] Yes  [ ] No
**Section 3 SEALED → Section 4 now OPEN.**

---

### SECTION 4: INVALID TRANSITION ANALYSIS

#### REQUIRES

Section 4 must produce before its GATE releases:
- [ ] ≥ 2 invalid transitions in baseline-delta form
- [ ] Missing-check column with ≥ 1 non-empty entry
- [ ] Risk-if-unchecked for each missing check

#### CONTENT

*Invalid Transition Table*

| Delta-ID | Baseline State (S-ID) | Attempted Delta (OP-ID) | Failure Reason                          | Missing Check | Risk if Unchecked |
|----------|-----------------------|-------------------------|-----------------------------------------|---------------|-------------------|
| IT-01    |                       |                         | [->DECL: E.field] OPERATOR [value] FAILS|               |                   |
| IT-02    |                       |                         | [INV-ID] threshold breached             |               |                   |

#### COUNT-AND-CHECK

Count invalid transitions: ___. If fewer than 2, add before proceeding.
Count missing-check entries: ___. If fewer than 1, add before proceeding.

#### GATE -- Section 4

All REQUIRES items satisfied? [ ] Yes  [ ] No
COUNT-AND-CHECK all minimums met? [ ] Yes  [ ] No
**Section 4 SEALED → Section 5 now OPEN.**

---

### SECTION 5: VOCABULARY AUDIT

#### REQUIRES

Section 5 must produce before its GATE releases:
- [ ] Enumerated audit table mapping every operation name used to its OP-ID
- [ ] UNDECLARED flag for any unlisted operation
- [ ] Generic verb scan complete

#### CONTENT

*Operation Name Audit Table*

| Audit-ID | Operation Name Used | OP-ID | Generic Verb? | Status       |
|----------|---------------------|-------|---------------|--------------|
| A-01     |                     |       | Yes / No      | Declared / UNDECLARED |
| A-02     |                     |       | Yes / No      | Declared / UNDECLARED |
| A-03     |                     |       | Yes / No      | Declared / UNDECLARED |
| A-04     |                     |       | Yes / No      | Declared / UNDECLARED |
| A-05     |                     |       | Yes / No      | Declared / UNDECLARED |

Generic verbs scanned: update, create, delete, change, set, get, modify
Generic verb violations found: Yes / No

#### COUNT-AND-CHECK

Count operations audited: ___. Must match total distinct operations in Sections 2-4. If fewer, add before proceeding.
Count UNDECLARED entries: ___. If any, flag for remediation.
Count generic verb violations: ___. If any, flag for remediation.

#### GATE -- Section 5

All REQUIRES items satisfied? [ ] Yes  [ ] No
COUNT-AND-CHECK all minimums met? [ ] Yes  [ ] No
**Section 5 COMPLETE. Trace is complete.**

---

## V-03 -- Finance, Standing Directives + MUST/BLOCKED (No Phase Architecture)

**Variation axis**: Phrasing register -- Finance domain with SD-N standing directives and
strong imperative MUST/BLOCKED language throughout, but sections use the traditional
Opening-Contract/Closing-Gate structure rather than the four-layer phase architecture.

**Hypothesis**: SD-N standing directives at document level earn C-23 regardless of phrasing
register. The absence of REQUIRES/CONTENT/COUNT-AND-CHECK/GATE as named structural layers
means C-22 is not earned. Imperative phrasing does not substitute for architectural
identity. Result should match R5 V-03: 14/15 aspirationals (C-23 pass, C-22 fail), and
isolates phrasing register as a non-variable for C-22.

**Target gaps**: C-23 (phrasing-register baseline)

---

You are a **Finance domain expert**. Your task is to hand-compile state transitions for a
financial entity, identify invalid transitions, missing precondition checks, invariant
violations, and race conditions, and produce a structured trace-state report by following
every section below in order.

---

### STANDING DIRECTIVES

The following standing directives apply to every section in this trace. All sections comply
by reference. These directives are not repeated in any section.

**SD-1 (Predicate Annotations):** MUST annotate every predicate field with `[->DECL: EntityName.fieldName]`
identifying its Section 0 declaration source. A predicate without this annotation is
structurally blocked from satisfying its section gate.

**SD-2 (Slot Enforcement):** MUST fill every `[->DECL: _._]` slot before writing any adjacent
value. Unfilled `_._` slots BLOCK the section gate. Closing gates confirm zero unfilled slots remain.

**SD-3 (Gate Enforcement):** MUST close every section with a count-and-remediate gate. Gates
MUST count required elements by type and issue an explicit "if fewer than N, add N before
proceeding" directive. A passive checklist that does not count and does not direct addition
does NOT satisfy this directive.

---

### SECTION 0: VOCABULARY DECLARATION

**Opening contract -- Section 0 MUST produce:**
- [ ] Entity table: min 2 Finance entities, ≥ 3 fields each, SD-1 annotations in all field positions
- [ ] Operation table: min 5 Finance domain verbs with generic-verb prohibitions
- [ ] Invariant table: min 3 invariants; ≥ 1 numeric; ≥ 1 temporal

*Entity and Field Registry (SD-1 annotation REQUIRED in every Entity Name and Field cell)*

| ENT-ID | Entity Name            | Field                  | Type |
|--------|------------------------|------------------------|------|
| E-01   | [->DECL: _._]          | [->DECL: _._]          |      |
| E-01   | [->DECL: _._]          | [->DECL: _._]          |      |
| E-01   | [->DECL: _._]          | [->DECL: _._]          |      |
| E-02   | [->DECL: _._]          | [->DECL: _._]          |      |
| E-02   | [->DECL: _._]          | [->DECL: _._]          |      |
| E-02   | [->DECL: _._]          | [->DECL: _._]          |      |

*Operation Registry*

| OP-ID | Domain Verb           | Description               | Prohibited Generic Equivalent |
|-------|-----------------------|---------------------------|-------------------------------|
| OP-01 |                       |                           | update / set                  |
| OP-02 |                       |                           | create / add                  |
| OP-03 |                       |                           | delete / remove               |
| OP-04 |                       |                           | change / modify               |
| OP-05 |                       |                           | get / fetch                   |

*Invariant Registry*

| INV-ID | Invariant Statement                             | Scope     | Severity             | Falsifiable Threshold |
|--------|-------------------------------------------------|-----------|----------------------|-----------------------|
| INV-01 | [->DECL: _._].[->DECL: _._] [op] [->DECL: _._] | All states| FATAL/DEGRADED/COSMETIC |                    |
| INV-02 | [->DECL: _._].[->DECL: _._] [op] [->DECL: _._] | All states| FATAL/DEGRADED/COSMETIC |                    |
| INV-03 | [->DECL: _._].[->DECL: _._] [op] [->DECL: _._] | Specific  | FATAL/DEGRADED/COSMETIC |                    |

**Closing gate -- Section 0 (SD-3):**
Count entities declared: ___. If fewer than 2, ADD entities before proceeding. ADVANCE BLOCKED until count ≥ 2.
Count operations declared: ___. If fewer than 5, ADD operations before proceeding. ADVANCE BLOCKED until count ≥ 5.
Count invariants declared: ___. If fewer than 3, ADD invariants before proceeding. ADVANCE BLOCKED until count ≥ 3.
Count `[->DECL: _._]` slots unfilled: ___. If any remain, FILL them before proceeding. ADVANCE BLOCKED until count = 0.

---

### SECTION 1: INVARIANT ANALYSIS

**Opening contract -- Section 1 MUST produce:**
- [ ] Severity classification for every INV-ID from Section 0
- [ ] Each invariant tested against ≥ 1 trace step (forward reference permitted)
- [ ] ≥ 1 missing-precondition entry with risk statement

*Invariant Testing Table (SD-1 annotation REQUIRED in all predicate cells)*

| INV-ID | Invariant (SD-1 annotated)    | Severity             | Tested at Step | Holds / Violated | Reason if Violated |
|--------|-------------------------------|----------------------|---------------|-----------------|---------------------|
| INV-01 | [->DECL: _._]                 | FATAL/DEGRADED/COSMETIC | Step ___   |                 |                     |
| INV-02 | [->DECL: _._]                 | FATAL/DEGRADED/COSMETIC | Step ___   |                 |                     |
| INV-03 | [->DECL: _._]                 | FATAL/DEGRADED/COSMETIC | Step ___   |                 |                     |

*Missing Precondition Risk Table*

| OP-ID | Precondition Not Enforced                         | Risk if Unchecked |
|-------|---------------------------------------------------|-------------------|
|       | [->DECL: _._].[->DECL: _._] [op] [val] -- assumed, not checked | |

**Closing gate -- Section 1 (SD-3):**
Count invariants with severity: ___. If fewer than 3, ADD classifications before proceeding. ADVANCE BLOCKED.
Count invariants with step references: ___. If fewer than 2, ADD references before proceeding. ADVANCE BLOCKED.
Count missing-precondition entries: ___. If fewer than 1, ADD an entry before proceeding. ADVANCE BLOCKED.
Count `[->DECL: _._]` slots unfilled: ___. If any remain, FILL before proceeding. ADVANCE BLOCKED.

---

### SECTION 2: HAND-COMPILED STATE TRANSITION TRACE

**Opening contract -- Section 2 MUST produce:**
- [ ] Min 6 steps with before-state (S-ID), OP-ID, after-state (S-ID)
- [ ] ≥ 1 predicate precondition per step (SD-1 annotated): `[->DECL: E.field] OPERATOR [value] -- PASS / FAIL`
- [ ] ≥ 1 mutation postcondition per step (SD-1 annotated): `[->DECL: E.field]: [old] -> [new]`
- [ ] ≥ 1 [REJECTED] step confirming entity stays in before-state
- [ ] ≥ 1 labeled "Alternate / Error Path" subsection with min 3 steps

Step template (SD-1 annotations MUST appear in all predicate field positions; slots MUST be filled
per SD-2 before writing adjacent values):

```
Step N: [OP-ID] [Finance Operation Name]    [PASS / REJECTED]
  Before:  [S-ID] [State Name] -- { [->DECL: E.field]: value, [->DECL: E.field]: value }
  Preconditions:
    [->DECL: EntityName.fieldName] OPERATOR [value]  -- PASS / FAIL
    [->DECL: EntityName.fieldName] OPERATOR [value]  -- PASS / FAIL
  Guard:   passes -- continue  /  fires -- reason: [specific predicate that failed]
  After:   [S-ID] [State Name] -- { [->DECL: E.field]: value, [->DECL: E.field]: value }
  Postconditions:
    [->DECL: EntityName.fieldName]: [old_value] -> [new_value]
    [->DECL: EntityName.fieldName]: unchanged
```

*(Write min 6 steps. Mark ≥ 1 [REJECTED].)*

*Alternate / Error Path -- [scenario name]*

*(Write min 3 steps using same template.)*

**Closing gate -- Section 2 (SD-3):**
Count steps: ___. If fewer than 6, ADD steps. ADVANCE BLOCKED.
Count [REJECTED] steps: ___. If fewer than 1, ADD a rejected step. ADVANCE BLOCKED.
Count alternate-path steps: ___. If fewer than 3, EXTEND path. ADVANCE BLOCKED.
Count `[->DECL: _._]` slots unfilled: ___. If any remain, FILL now. ADVANCE BLOCKED.

---

### SECTION 3: RACE CONDITION ANALYSIS

**Opening contract -- Section 3 MUST produce:**
- [ ] ≥ 1 named race scenario with two Finance actors
- [ ] T0/T1 table with min 4 rows (pre-printed below)
- [ ] Violation row marked with INV-ID citation
- [ ] Severity label

*Race Scenario: [Name the Finance scenario]*

| Time | Actor T0                                              | Actor T1                                              |
|------|-------------------------------------------------------|-------------------------------------------------------|
| t=0  | [->DECL: _._]: reads [->DECL: _._] = [value]         | [->DECL: _._]: reads [->DECL: _._] = [value]         |
| t=1  | [->DECL: _._] OPERATOR [value] -- PASS (stale)        | waits                                                 |
| t=2  | [->DECL: _._]: [old] -> [new] (write commits)         | [->DECL: _._] OPERATOR [value] -- PASS (stale)        |
| t=3  | completes                                             | [->DECL: _._]: [old] -> [new] -- **[INV-ID] VIOLATED**|

Severity: FATAL / DEGRADED / COSMETIC

**Closing gate -- Section 3 (SD-3):**
Count race scenarios: ___. If fewer than 1, ADD a scenario. ADVANCE BLOCKED.
Count T0/T1 rows: ___. If fewer than 4, ADD rows. ADVANCE BLOCKED.
Count violation rows with INV-ID: ___. If fewer than 1, ADD citation. ADVANCE BLOCKED.
Count `[->DECL: _._]` slots unfilled: ___. If any remain, FILL now. ADVANCE BLOCKED.

---

### SECTION 4: INVALID TRANSITION ANALYSIS

**Opening contract -- Section 4 MUST produce:**
- [ ] ≥ 2 invalid transitions in baseline-delta form: `(baseline_state, attempted_delta, failure_reason)`
- [ ] Missing-check column with ≥ 1 non-empty entry and risk-if-unchecked

*Invalid Transition Table*

| Delta-ID | Baseline State (S-ID) | Attempted Delta (OP-ID) | Failure Reason                                    | Missing Check | Risk if Unchecked |
|----------|-----------------------|-------------------------|---------------------------------------------------|---------------|-------------------|
| IT-01    | [->DECL: _._]         | [->DECL: _._]           | [->DECL: E.field] OPERATOR [value] FAILS          |               |                   |
| IT-02    | [->DECL: _._]         | [->DECL: _._]           | [INV-ID] [->DECL: E.field] threshold breached     |               |                   |

**Closing gate -- Section 4 (SD-3):**
Count invalid transitions: ___. If fewer than 2, ADD entries. ADVANCE BLOCKED.
Count missing-check entries: ___. If fewer than 1, ADD an entry. ADVANCE BLOCKED.
Count `[->DECL: _._]` slots unfilled: ___. If any remain, FILL now. ADVANCE BLOCKED.

---

### SECTION 5: VOCABULARY AUDIT

**Opening contract -- Section 5 MUST produce:**
- [ ] Enumerated audit table: every distinct operation name in Sections 2-4 mapped to its OP-ID
- [ ] UNDECLARED flag for any operation not in Section 0
- [ ] Generic verb scan complete

*Operation Name Audit Table*

| Audit-ID | Operation Name Used | OP-ID | Generic Verb? | Status       |
|----------|---------------------|-------|---------------|--------------|
| A-01     |                     |       | Yes / No      | Declared / UNDECLARED |
| A-02     |                     |       | Yes / No      | Declared / UNDECLARED |
| A-03     |                     |       | Yes / No      | Declared / UNDECLARED |
| A-04     |                     |       | Yes / No      | Declared / UNDECLARED |
| A-05     |                     |       | Yes / No      | Declared / UNDECLARED |

Generic verbs scanned: update, create, delete, change, set, get, modify
Found in any operation name: Yes / No

**Closing gate -- Section 5 (SD-3):**
Count operations audited: ___. MUST equal total distinct operations in Sections 2-4. If fewer, ADD entries. ADVANCE BLOCKED.
Count UNDECLARED entries: ___. If any, REMEDIATE before proceeding. ADVANCE BLOCKED.
Count generic verb violations: ___. If any, REMEDIATE before proceeding. ADVANCE BLOCKED.
**Section 5 COMPLETE. Trace is complete.**

---

## V-04 -- Customer Service, Compound (SD-N + REQUIRES/CONTENT/COUNT-AND-CHECK/GATE)

**Variation axis**: Compound role -- Customer Service domain with both C-22 (four-layer
phase architecture) and C-23 (SD-N standing directives). Same compound structure as V-01
applied to the CS domain (cases, tickets, escalations).

**Hypothesis**: The V-01 compound approach (both C-22 and C-23) is domain-portable. CS
domain verbs (escalate_case, resolve, reopen, assign) and CS entities (Case, Agent,
Escalation) do not structurally preclude earning both C-22 and C-23 simultaneously.
Expected result: 15/15, same as V-01.

**Target gaps**: C-22 + C-23 (domain portability test)

---

You are a **Customer Service domain expert**. Your task is to hand-compile state transitions
for a CS entity (Case, Ticket, Escalation, or Support Request), identify invalid transitions,
missing precondition checks, invariant violations, and race conditions, and produce a
structured trace-state report by following every section below in order.

---

### STANDING DIRECTIVES

The following standing directives apply to every section in this trace without repetition.
All sections comply by reference to these directives.

**SD-1 (Predicate Annotations):** Every predicate field in every precondition and
postcondition carries an inline `[->DECL: EntityName.fieldName]` annotation identifying the
Section 0 declaration entry it was drawn from. A predicate missing this annotation is
structurally incomplete.

**SD-2 (Slot Enforcement):** Every `[->DECL: _._]` slot is filled before writing any
adjacent value. An unfilled `_._` slot is a structural gap. The COUNT-AND-CHECK layer of
every section confirms none remain.

**SD-3 (Section Architecture):** Every section is structured as exactly four named layers:
**REQUIRES → CONTENT → COUNT-AND-CHECK → GATE**. This is the format. Completing REQUIRES
and writing CONTENT is what every section is. Reaching COUNT-AND-CHECK and GATE is what
every section does. A section missing any layer is architecturally incomplete.

---

### SECTION 0: VOCABULARY DECLARATION

#### REQUIRES

Section 0 must produce before its GATE releases:
- [ ] Entity table: min 2 CS entities (e.g., Case, Agent), each with ≥ 3 named fields and SD-1 annotations
- [ ] Operation table: min 5 CS domain verbs (open_case, escalate_case, assign_agent, resolve, reopen); generic-verb prohibitions listed
- [ ] Invariant table: min 3 invariants; ≥ 1 numeric (e.g., SLA deadline); ≥ 1 structural

#### CONTENT

*Entity and Field Registry*

| ENT-ID | Entity Name            | Field                  | Type |
|--------|------------------------|------------------------|------|
| E-01   | [->DECL: _._]          | [->DECL: _._]          |      |
| E-01   | [->DECL: _._]          | [->DECL: _._]          |      |
| E-01   | [->DECL: _._]          | [->DECL: _._]          |      |
| E-02   | [->DECL: _._]          | [->DECL: _._]          |      |
| E-02   | [->DECL: _._]          | [->DECL: _._]          |      |
| E-02   | [->DECL: _._]          | [->DECL: _._]          |      |

*Operation Registry*

| OP-ID | CS Domain Verb           | Description                        | Prohibited Generic Equivalent |
|-------|--------------------------|------------------------------------|-------------------------------|
| OP-01 |                          |                                    | update / set                  |
| OP-02 |                          |                                    | create / add                  |
| OP-03 |                          |                                    | change / modify               |
| OP-04 |                          |                                    | delete / remove               |
| OP-05 |                          |                                    | get / fetch                   |

*Invariant Registry*

| INV-ID | Invariant Statement                                        | Scope     | Severity             | Falsifiable Threshold |
|--------|-------------------------------------------------------------|-----------|----------------------|-----------------------|
| INV-01 | [->DECL: _._].[->DECL: _._] [op] [->DECL: _._]            | All states| FATAL/DEGRADED/COSMETIC |                    |
| INV-02 | [->DECL: _._].[->DECL: _._] [op] [->DECL: _._]            | All states| FATAL/DEGRADED/COSMETIC |                    |
| INV-03 | [->DECL: _._].[->DECL: _._] [op] [->DECL: _._]            | Specific  | FATAL/DEGRADED/COSMETIC |                    |

#### COUNT-AND-CHECK

Count entities declared: ___. If fewer than 2, add entities before proceeding.
Count operations declared: ___. If fewer than 5, add operations before proceeding.
Count invariants declared: ___. If fewer than 3, add invariants before proceeding.
Count `[->DECL: _._]` slots remaining unfilled: ___. If any remain, fill before proceeding.

#### GATE -- Section 0

All REQUIRES checklist items satisfied? [ ] Yes  [ ] No -- if No, complete missing items before proceeding.
COUNT-AND-CHECK all minimums met? [ ] Yes  [ ] No -- if No, add missing entries before proceeding.
SD-1 annotations present in all predicate positions? [ ] Yes  [ ] No -- if No, fill before proceeding.
**Section 0 SEALED → Section 1 now OPEN.**

---

### SECTION 1: INVARIANT ANALYSIS

#### REQUIRES

Section 1 must produce before its GATE releases:
- [ ] Severity classification for every INV-ID from Section 0
- [ ] Each invariant tested against ≥ 1 trace step
- [ ] ≥ 1 missing-precondition entry with risk statement

#### CONTENT

*Invariant Testing Table*

| INV-ID | Invariant (from Section 0)    | Severity             | Tested at Step | Holds / Violated | Reason if Violated |
|--------|-------------------------------|----------------------|---------------|-----------------|---------------------|
| INV-01 | [->DECL: _._]                 | FATAL/DEGRADED/COSMETIC | Step ___   |                 |                     |
| INV-02 | [->DECL: _._]                 | FATAL/DEGRADED/COSMETIC | Step ___   |                 |                     |
| INV-03 | [->DECL: _._]                 | FATAL/DEGRADED/COSMETIC | Step ___   |                 |                     |

*Missing Precondition Risk Table*

| OP-ID | Precondition Not Enforced by System              | Risk if Unchecked |
|-------|--------------------------------------------------|-------------------|
|       | [->DECL: _._].[->DECL: _._] [op] [val] -- assumed not checked | |

#### COUNT-AND-CHECK

Count invariants with severity: ___. If fewer than 3, add before proceeding.
Count invariants with step references: ___. If fewer than 2, add before proceeding.
Count missing-precondition entries: ___. If fewer than 1, add before proceeding.
Count `[->DECL: _._]` slots remaining unfilled: ___. If any remain, fill before proceeding.

#### GATE -- Section 1

All REQUIRES items satisfied? [ ] Yes  [ ] No
COUNT-AND-CHECK all minimums met? [ ] Yes  [ ] No
**Section 1 SEALED → Section 2 now OPEN.**

---

### SECTION 2: HAND-COMPILED STATE TRANSITION TRACE

#### REQUIRES

Section 2 must produce before its GATE releases:
- [ ] Min 6 steps with before-state (S-ID), OP-ID, after-state (S-ID)
- [ ] ≥ 1 predicate precondition per step (SD-1 annotated)
- [ ] ≥ 1 mutation postcondition per step (SD-1 annotated)
- [ ] ≥ 1 [REJECTED] step
- [ ] ≥ 1 labeled "Alternate / Error Path" subsection with min 3 steps

#### CONTENT

*Happy Path*

```
Step N: [OP-ID] [CS Operation Name]    [PASS / REJECTED]
  Before:  [S-ID] [State Name] -- { [->DECL: E.field]: value, [->DECL: E.field]: value }
  Preconditions:
    [->DECL: EntityName.fieldName] OPERATOR [value]  -- PASS / FAIL
    [->DECL: EntityName.fieldName] OPERATOR [value]  -- PASS / FAIL
  Guard:   passes / fires -- reason: [text]
  After:   [S-ID] [State Name] -- { [->DECL: E.field]: value, [->DECL: E.field]: value }
  Postconditions:
    [->DECL: EntityName.fieldName]: [old] -> [new]
```

*(Write min 6 steps. Mark ≥ 1 [REJECTED].)*

*Alternate / Error Path -- [scenario name]*

*(Write min 3 steps.)*

#### COUNT-AND-CHECK

Count steps: ___. If fewer than 6, add steps before proceeding.
Count [REJECTED] steps: ___. If fewer than 1, add before proceeding.
Count alternate-path steps: ___. If fewer than 3, extend before proceeding.
Count `[->DECL: _._]` slots remaining unfilled: ___. If any remain, fill before proceeding.

#### GATE -- Section 2

All REQUIRES items satisfied? [ ] Yes  [ ] No
COUNT-AND-CHECK all minimums met? [ ] Yes  [ ] No
**Section 2 SEALED → Section 3 now OPEN.**

---

### SECTION 3: RACE CONDITION ANALYSIS

#### REQUIRES

Section 3 must produce before its GATE releases:
- [ ] ≥ 1 named CS race scenario (e.g., two agents claiming the same case)
- [ ] T0/T1 table with min 4 rows
- [ ] Violation row marked with INV-ID
- [ ] Severity label

#### CONTENT

*Race Scenario: [Name the CS scenario]*

| Time | Actor T0                                              | Actor T1                                              |
|------|-------------------------------------------------------|-------------------------------------------------------|
| t=0  | [->DECL: _._]: reads [->DECL: _._] = [value]         | [->DECL: _._]: reads [->DECL: _._] = [value]         |
| t=1  | [->DECL: _._] OPERATOR [value] -- PASS (stale)        | waits                                                 |
| t=2  | [->DECL: _._]: [old] -> [new] (write commits)         | [->DECL: _._] OPERATOR [value] -- PASS (stale)        |
| t=3  | completes                                             | [->DECL: _._]: [old] -> [new] -- **[INV-ID] VIOLATED**|

Severity: FATAL / DEGRADED / COSMETIC

#### COUNT-AND-CHECK

Count race scenarios: ___. If fewer than 1, add before proceeding.
Count T0/T1 rows: ___. If fewer than 4, add rows before proceeding.
Count violation rows with INV-ID: ___. If fewer than 1, add citation before proceeding.
Count `[->DECL: _._]` slots remaining unfilled: ___. If any remain, fill before proceeding.

#### GATE -- Section 3

All REQUIRES items satisfied? [ ] Yes  [ ] No
COUNT-AND-CHECK all minimums met? [ ] Yes  [ ] No
**Section 3 SEALED → Section 4 now OPEN.**

---

### SECTION 4: INVALID TRANSITION ANALYSIS

#### REQUIRES

Section 4 must produce before its GATE releases:
- [ ] ≥ 2 invalid transitions in baseline-delta form
- [ ] Missing-check column with ≥ 1 non-empty entry
- [ ] Risk-if-unchecked for each missing check

#### CONTENT

*Invalid Transition Table*

| Delta-ID | Baseline State (S-ID) | Attempted Delta (OP-ID) | Failure Reason                               | Missing Check | Risk if Unchecked |
|----------|-----------------------|-------------------------|----------------------------------------------|---------------|-------------------|
| IT-01    | [->DECL: _._]         | [->DECL: _._]           | [->DECL: E.field] OPERATOR [value] FAILS     |               |                   |
| IT-02    | [->DECL: _._]         | [->DECL: _._]           | [INV-ID] threshold breached                  |               |                   |

#### COUNT-AND-CHECK

Count invalid transitions: ___. If fewer than 2, add before proceeding.
Count missing-check entries: ___. If fewer than 1, add before proceeding.
Count `[->DECL: _._]` slots remaining unfilled: ___. If any remain, fill before proceeding.

#### GATE -- Section 4

All REQUIRES items satisfied? [ ] Yes  [ ] No
COUNT-AND-CHECK all minimums met? [ ] Yes  [ ] No
**Section 4 SEALED → Section 5 now OPEN.**

---

### SECTION 5: VOCABULARY AUDIT

#### REQUIRES

Section 5 must produce before its GATE releases:
- [ ] Enumerated audit table mapping every operation name to its OP-ID
- [ ] UNDECLARED flag for any unlisted operation
- [ ] Generic verb scan complete

#### CONTENT

*Operation Name Audit Table*

| Audit-ID | Operation Name Used | OP-ID | Generic Verb? | Status       |
|----------|---------------------|-------|---------------|--------------|
| A-01     |                     |       | Yes / No      | Declared / UNDECLARED |
| A-02     |                     |       | Yes / No      | Declared / UNDECLARED |
| A-03     |                     |       | Yes / No      | Declared / UNDECLARED |
| A-04     |                     |       | Yes / No      | Declared / UNDECLARED |
| A-05     |                     |       | Yes / No      | Declared / UNDECLARED |

Generic verbs scanned: update, create, delete, change, set, get, modify
Found in any operation name: Yes / No

#### COUNT-AND-CHECK

Count operations audited: ___. Must equal total distinct operations in Sections 2-4. If fewer, add before proceeding.
Count UNDECLARED entries: ___. If any, flag for remediation.
Count generic verb violations: ___. If any, flag for remediation.

#### GATE -- Section 5

All REQUIRES items satisfied? [ ] Yes  [ ] No
COUNT-AND-CHECK all minimums met? [ ] Yes  [ ] No
**Section 5 COMPLETE. Trace is complete.**

---

## V-05 -- Finance, Compound + Imperative Phrasing (SD-N + Phase Architecture + MUST/BLOCKED/ADVANCE)

**Variation axis**: Compliance compound + phrasing register -- Finance domain with both
C-22 (REQUIRES/CONTENT/COUNT-AND-CHECK/GATE four-layer architecture) and C-23 (SD-N
standing directives), plus MUST/BLOCKED/ADVANCE imperative markers at every layer boundary
throughout the trace.

**Hypothesis**: V-01's compound structure earns both C-22 and C-23 at 15/15. Adding
MUST/BLOCKED/ADVANCE imperative language throughout tests whether the phrasing register
reinforces or interferes with the architectural compliance mechanisms. If imperative
phrasing is orthogonal to the compliance mechanisms, result is still 15/15. If phrasing
overrides structure (causing the model to read MUST as gate-substitute rather than GATE as
architectural layer), C-22 could degrade. Expected result: 15/15 -- imperative phrasing
and architectural identity are additive, not substitutive.

**Target gaps**: C-22 + C-23 (phrasing-register stress test of compound)

---

You are a **Finance domain expert**. Your task is to hand-compile state transitions for a
financial entity, identify invalid transitions, missing precondition checks, invariant
violations, and race conditions, and produce a structured trace-state report by following
every section below in order.

---

### STANDING DIRECTIVES

The following standing directives MUST be applied to every section in this trace without
repetition. All sections comply by reference. Non-compliance with any standing directive
BLOCKS section gate release.

**SD-1 (Predicate Annotations):** Every predicate field MUST carry an inline
`[->DECL: EntityName.fieldName]` annotation identifying its Section 0 declaration source.
A predicate without this annotation BLOCKS the section gate. No exceptions.

**SD-2 (Slot Enforcement):** Every `[->DECL: _._]` slot MUST be filled before any adjacent
value is written. An unfilled `_._` slot BLOCKS the section gate. COUNT-AND-CHECK MUST
confirm zero unfilled slots remain before GATE is released.

**SD-3 (Section Architecture):** Every section MUST be structured as exactly four named
layers: **REQUIRES → CONTENT → COUNT-AND-CHECK → GATE**. This is the format, not an
instruction. REQUIRES is the opening contract. CONTENT is the section body. COUNT-AND-CHECK
is the remediation loop. GATE is the exit certification. A section missing any layer is
architecturally BLOCKED and MUST NOT advance.

---

### SECTION 0: VOCABULARY DECLARATION

#### REQUIRES

The following MUST appear before CONTENT begins -- ADVANCE BLOCKED until all items present:
- [ ] Entity table: min 2 Finance entities, ≥ 3 named fields each, SD-1 slots in all field positions
- [ ] Operation table: min 5 Finance domain verbs with generic-verb prohibitions declared
- [ ] Invariant table: min 3 invariants; ≥ 1 numeric with falsifiable threshold; ≥ 1 temporal

#### CONTENT

*Entity and Field Registry (SD-2: fill [->DECL: _._] slots BEFORE writing adjacent values)*

| ENT-ID | Entity Name            | Field                  | Type |
|--------|------------------------|------------------------|------|
| E-01   | [->DECL: _._]          | [->DECL: _._]          |      |
| E-01   | [->DECL: _._]          | [->DECL: _._]          |      |
| E-01   | [->DECL: _._]          | [->DECL: _._]          |      |
| E-02   | [->DECL: _._]          | [->DECL: _._]          |      |
| E-02   | [->DECL: _._]          | [->DECL: _._]          |      |
| E-02   | [->DECL: _._]          | [->DECL: _._]          |      |

*Operation Registry*

| OP-ID | Finance Domain Verb   | Description                        | Prohibited Generic Equivalent |
|-------|-----------------------|------------------------------------|-------------------------------|
| OP-01 |                       |                                    | update / set                  |
| OP-02 |                       |                                    | create / add                  |
| OP-03 |                       |                                    | delete / remove               |
| OP-04 |                       |                                    | change / modify               |
| OP-05 |                       |                                    | get / fetch                   |

*Invariant Registry*

| INV-ID | Invariant Statement                                        | Scope     | Severity             | Falsifiable Threshold |
|--------|-------------------------------------------------------------|-----------|----------------------|-----------------------|
| INV-01 | [->DECL: _._].[->DECL: _._] [op] [->DECL: _._]            | All states| FATAL/DEGRADED/COSMETIC |                    |
| INV-02 | [->DECL: _._].[->DECL: _._] [op] [->DECL: _._]            | All states| FATAL/DEGRADED/COSMETIC |                    |
| INV-03 | [->DECL: _._].[->DECL: _._] [op] [->DECL: _._]            | Specific  | FATAL/DEGRADED/COSMETIC |                    |

#### COUNT-AND-CHECK

MUST count and remediate before GATE -- ADVANCE BLOCKED if any count falls short:
Count entities declared: ___. If fewer than 2, ADD entities NOW before proceeding.
Count operations declared: ___. If fewer than 5, ADD operations NOW before proceeding.
Count invariants declared: ___. If fewer than 3, ADD invariants NOW before proceeding.
Count `[->DECL: _._]` slots remaining unfilled: ___. If any remain, FILL NOW before proceeding.

#### GATE -- Section 0

REQUIRES items all present? [ ] Yes  [ ] No -- if No, BLOCKED, complete before advancing.
COUNT-AND-CHECK all minimums met? [ ] Yes  [ ] No -- if No, BLOCKED, add before advancing.
SD-1 annotations present in all predicate positions? [ ] Yes  [ ] No -- if No, BLOCKED, fill before advancing.
**Section 0 SEALED → ADVANCE to Section 1.**

---

### SECTION 1: INVARIANT ANALYSIS

#### REQUIRES

The following MUST appear before CONTENT begins -- ADVANCE BLOCKED until all items present:
- [ ] Severity classification (FATAL / DEGRADED / COSMETIC) for every INV-ID from Section 0
- [ ] Each invariant tested against ≥ 1 trace step (forward reference to Section 2 permitted)
- [ ] ≥ 1 missing-precondition entry naming an unenforced system check and its risk

#### CONTENT

*Invariant Testing Table*

| INV-ID | Invariant (SD-1 annotated)    | Severity             | Tested at Step | Holds / Violated | Reason if Violated |
|--------|-------------------------------|----------------------|---------------|-----------------|---------------------|
| INV-01 | [->DECL: _._]                 | FATAL/DEGRADED/COSMETIC | Step ___   |                 |                     |
| INV-02 | [->DECL: _._]                 | FATAL/DEGRADED/COSMETIC | Step ___   |                 |                     |
| INV-03 | [->DECL: _._]                 | FATAL/DEGRADED/COSMETIC | Step ___   |                 |                     |

*Missing Precondition Risk Table*

| OP-ID | Precondition Not Enforced by System                    | Risk if Unchecked |
|-------|--------------------------------------------------------|-------------------|
|       | [->DECL: _._].[->DECL: _._] [op] [val] -- assumed, not checked | |

#### COUNT-AND-CHECK

MUST count and remediate before GATE -- ADVANCE BLOCKED if any count falls short:
Count invariants with severity: ___. If fewer than 3, ADD classifications NOW.
Count invariants with step references: ___. If fewer than 2, ADD references NOW.
Count missing-precondition entries: ___. If fewer than 1, ADD an entry NOW.
Count `[->DECL: _._]` slots unfilled: ___. If any remain, FILL NOW.

#### GATE -- Section 1

REQUIRES items all present? [ ] Yes  [ ] No -- BLOCKED if No.
COUNT-AND-CHECK all minimums met? [ ] Yes  [ ] No -- BLOCKED if No.
**Section 1 SEALED → ADVANCE to Section 2.**

---

### SECTION 2: HAND-COMPILED STATE TRANSITION TRACE

#### REQUIRES

The following MUST appear before CONTENT begins -- ADVANCE BLOCKED until all items present:
- [ ] Min 6 numbered steps with before-state (S-ID), OP-ID, after-state (S-ID) on every step
- [ ] ≥ 1 predicate precondition per step (SD-1 annotated): `[->DECL: E.field] OPERATOR [value] -- PASS / FAIL`
- [ ] ≥ 1 mutation postcondition per step (SD-1 annotated): `[->DECL: E.field]: [old] -> [new]`
- [ ] ≥ 1 step labeled [REJECTED] where guard fires; entity MUST remain in before-state
- [ ] ≥ 1 labeled "Alternate / Error Path" subsection with min 3 steps

#### CONTENT

*Happy Path (SD-2: fill slots BEFORE adjacent values; SD-1 MUST annotate every predicate field)*

```
Step N: [OP-ID] [Finance Operation Name]    [PASS / REJECTED]
  Before:  [S-ID] [State Name] -- { [->DECL: E.field]: value, [->DECL: E.field]: value }
  Preconditions:
    [->DECL: EntityName.fieldName] OPERATOR [value]  -- PASS / FAIL
    [->DECL: EntityName.fieldName] OPERATOR [value]  -- PASS / FAIL
  Guard:   passes -- ADVANCE  /  fires -- BLOCKED, reason: [specific predicate]
  After:   [S-ID] [State Name] -- { [->DECL: E.field]: value, [->DECL: E.field]: value }
    [REJECTED: entity MUST remain in before-state; confirm field-for-field match -- any deviation is BLOCKED]
  Postconditions:
    [->DECL: EntityName.fieldName]: [old_value] -> [new_value]
    [->DECL: EntityName.fieldName]: unchanged
```

*(Write min 6 steps. Mark ≥ 1 [REJECTED].)*

*Alternate / Error Path -- [scenario name]*

*(Write min 3 steps using same template.)*

#### COUNT-AND-CHECK

MUST count and remediate before GATE -- ADVANCE BLOCKED if any count falls short:
Count steps: ___. If fewer than 6, ADD steps NOW.
Count steps with predicate preconditions: ___. MUST equal total steps. If fewer, ADD predicates NOW.
Count steps with mutation postconditions: ___. MUST equal total steps. If fewer, ADD postconditions NOW.
Count [REJECTED] steps: ___. If fewer than 1, ADD a rejected step NOW.
Count alternate-path steps: ___. If fewer than 3, EXTEND path NOW.
Count `[->DECL: _._]` slots unfilled: ___. If any remain, FILL NOW.

#### GATE -- Section 2

REQUIRES items all present? [ ] Yes  [ ] No -- BLOCKED if No.
COUNT-AND-CHECK all minimums met? [ ] Yes  [ ] No -- BLOCKED if No.
**Section 2 SEALED → ADVANCE to Section 3.**

---

### SECTION 3: RACE CONDITION ANALYSIS

#### REQUIRES

The following MUST appear before CONTENT begins -- ADVANCE BLOCKED until all items present:
- [ ] ≥ 1 named Finance race scenario: two actors, one targeted OP-ID
- [ ] T0/T1 two-column interleaving table with min 4 rows (pre-printed below)
- [ ] Row where invariant breaks MUST be marked with INV-ID citation
- [ ] Severity label MUST be present

#### CONTENT

*Race Scenario: [Name the Finance concurrency scenario]*

| Time | Actor T0                                              | Actor T1                                              |
|------|-------------------------------------------------------|-------------------------------------------------------|
| t=0  | [->DECL: _._]: reads [->DECL: _._] = [value]         | [->DECL: _._]: reads [->DECL: _._] = [value]         |
| t=1  | [->DECL: _._] OPERATOR [value] -- PASS (stale read)   | waits                                                 |
| t=2  | [->DECL: _._]: [old] -> [new] (write commits)         | [->DECL: _._] OPERATOR [value] -- PASS (stale read)   |
| t=3  | completes                                             | [->DECL: _._]: [old] -> [new] -- **[INV-ID] VIOLATED**|

Invariant broken: [INV-ID] -- [statement from Section 0]
Severity: FATAL / DEGRADED / COSMETIC

#### COUNT-AND-CHECK

MUST count and remediate before GATE -- ADVANCE BLOCKED if any count falls short:
Count race scenarios: ___. If fewer than 1, ADD a scenario NOW.
Count T0/T1 rows: ___. If fewer than 4, ADD rows NOW.
Count violation rows with INV-ID: ___. If fewer than 1, ADD citation NOW.
Count `[->DECL: _._]` slots unfilled: ___. If any remain, FILL NOW.

#### GATE -- Section 3

REQUIRES items all present? [ ] Yes  [ ] No -- BLOCKED if No.
COUNT-AND-CHECK all minimums met? [ ] Yes  [ ] No -- BLOCKED if No.
**Section 3 SEALED → ADVANCE to Section 4.**

---

### SECTION 4: INVALID TRANSITION ANALYSIS

#### REQUIRES

The following MUST appear before CONTENT begins -- ADVANCE BLOCKED until all items present:
- [ ] ≥ 2 invalid transitions in structured baseline-delta form: `(baseline_state, attempted_delta, failure_reason)`
- [ ] Missing-check column with ≥ 1 non-empty entry naming an unenforced system check
- [ ] Risk-if-unchecked MUST be stated for each missing check

#### CONTENT

*Invalid Transition Table (SD-1 MUST annotate every predicate field in Failure Reason column)*

| Delta-ID | Baseline State (S-ID) | Attempted Delta (OP-ID) | Failure Reason                                    | Missing Check | Risk if Unchecked |
|----------|-----------------------|-------------------------|---------------------------------------------------|---------------|-------------------|
| IT-01    | [->DECL: _._]         | [->DECL: _._]           | [->DECL: E.field] OPERATOR [value] FAILS          |               |                   |
| IT-02    | [->DECL: _._]         | [->DECL: _._]           | [INV-ID] [->DECL: E.field] threshold breached     |               |                   |

#### COUNT-AND-CHECK

MUST count and remediate before GATE -- ADVANCE BLOCKED if any count falls short:
Count invalid transitions in delta form: ___. If fewer than 2, ADD entries NOW.
Count missing-check entries: ___. If fewer than 1, ADD an entry NOW.
Count `[->DECL: _._]` slots unfilled: ___. If any remain, FILL NOW.

#### GATE -- Section 4

REQUIRES items all present? [ ] Yes  [ ] No -- BLOCKED if No.
COUNT-AND-CHECK all minimums met? [ ] Yes  [ ] No -- BLOCKED if No.
**Section 4 SEALED → ADVANCE to Section 5.**

---

### SECTION 5: VOCABULARY AUDIT

#### REQUIRES

The following MUST appear before CONTENT begins -- ADVANCE BLOCKED until all items present:
- [ ] Enumerated audit table: every distinct operation name in Sections 2-4 mapped to its OP-ID
- [ ] UNDECLARED flag for any operation not in Section 0 -- MUST NOT silently pass
- [ ] Generic verb scan: MUST name each prohibited verb and confirm presence or absence

#### CONTENT

*Operation Name Audit Table*

| Audit-ID | Operation Name Used | OP-ID | Generic Verb? | Status       |
|----------|---------------------|-------|---------------|--------------|
| A-01     |                     |       | Yes / No      | Declared / UNDECLARED |
| A-02     |                     |       | Yes / No      | Declared / UNDECLARED |
| A-03     |                     |       | Yes / No      | Declared / UNDECLARED |
| A-04     |                     |       | Yes / No      | Declared / UNDECLARED |
| A-05     |                     |       | Yes / No      | Declared / UNDECLARED |

Generic verbs MUST be scanned: update, create, delete, change, set, get, modify, add, remove
Found in any operation name: Yes / No -- if Yes, each instance MUST be flagged and BLOCKED from advancing.

#### COUNT-AND-CHECK

MUST count and remediate before GATE -- ADVANCE BLOCKED if any count falls short:
Count operations audited: ___. MUST equal total distinct operations in Sections 2-4. If fewer, ADD entries NOW.
Count UNDECLARED entries: ___. If any found, REMEDIATE before advancing. ADVANCE BLOCKED.
Count generic verb violations: ___. If any found, REMEDIATE before advancing. ADVANCE BLOCKED.

#### GATE -- Section 5

REQUIRES items all present? [ ] Yes  [ ] No -- BLOCKED if No.
COUNT-AND-CHECK all minimums met? [ ] Yes  [ ] No -- BLOCKED if No.
Generic verb scan clean? [ ] Yes  [ ] No -- BLOCKED if No.
**Section 5 COMPLETE. Trace is complete. ADVANCE confirmed.**
