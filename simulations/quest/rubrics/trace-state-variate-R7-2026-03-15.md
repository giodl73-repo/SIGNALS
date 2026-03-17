# trace-state Skill -- Quest Variations Round 7

**Skill**: trace-state
**Round**: 7 (building on R6 golden base; rubric v7, 17 aspirationals)
**Rubric**: v7 (C-01--C-25; composite = E/5*60 + R/3*30 + A/17*10)
**R6 baseline**: V-01 16/17 (99.41, earned C-24, failed C-25), V-02 13/17 (97.65, failed C-19/C-23/C-24/C-25), V-03 15/17 (98.82, earned C-25, failed C-22/C-24). All golden.
**R6 gap**: No variation passed both C-24 and C-25. V-01 has C-24 (SD-3 unified architecture) but no BLOCKED posture. V-03 has C-25 (BLOCKED gates) but no phase architecture (C-22 fails, C-24 prerequisite fails). The synthesis target: SD-3 encodes the four-layer architecture as a standing directive (C-24) AND every GATE uses ADVANCE IS BLOCKED halt-condition language (C-25).

---

## Variation Map

| V | Axis | Primary Targets | Key Structural Change |
|---|------|-----------------|-----------------------|
| V-01 | BLOCKED gates added to compound | C-24 + C-25 synthesis | Finance: SD-3 encodes four-layer architecture (earning C-24); every GATE uses ADVANCE IS BLOCKED halt-condition language (earning C-25) |
| V-02 | Domain portability -- Customer Service | C-24 + C-25 portability | Customer Service: identical compound+BLOCKED structure as V-01; CS domain entities/operations -- tests whether synthesis is domain-independent |
| V-03 | BLOCKED posture embedded in SD-3 | C-25 via SD-3 architecture declaration | Finance: SD-3 declares GATE layer IS definitionally a BLOCKED state -- C-25 inherited from the same SD-3 entry that encodes C-24; gates comply with BLOCKED language by reference to SD-3 |
| V-04 | Four-layer + BLOCKED, no SD-N | C-22 + C-25 without C-23/C-24 | Sales: four-layer architecture declared in intro paragraph (not SD-N block); BLOCKED gates -- confirms prerequisite chain: C-22+C-25 achievable but C-23+C-24 require SD-N |
| V-05 | Imperative register throughout | Register vs C-25 gate-specificity | Finance: compound+BLOCKED identical to V-01 with intensified imperative register in REQUIRES and COUNT-AND-CHECK layers -- tests whether register intensification beyond GATE affects aspirational scoring |

**Single-axis hypotheses:**
- V-01: Adding ADVANCE IS BLOCKED to every GATE in R6-V-01 earns C-25 without disturbing C-24 -- the SD-3 unified architecture declaration is unaffected by gate phrasing change; 17/17 is achievable.
- V-02 vs V-01: CS domain replication earns identical criteria -- C-24+C-25 synthesis is domain-independent; Finance and CS share the mechanism even when domain vocabulary differs.
- V-03 vs V-01: Embedding BLOCKED posture in SD-3 itself (so SD-3 declares GATE IS a BLOCKED state by definition) earns C-25 via the same declaration that earns C-24 -- tests whether C-25 can be inherited through SD-N architecture scope.
- V-04 vs V-01: Removing SD-N from a four-layer+BLOCKED prompt loses C-23 and C-24 while keeping C-22 and C-25 -- confirms the SD-N prerequisite is binding for C-23/C-24 even when phase architecture and BLOCKED posture coexist.
- V-05 vs V-01: Intensifying imperative register across all layers (REQUIRES: "YOU MUST produce:", COUNT-AND-CHECK: "COUNT NOW. DEFICIT = ADD.") with unchanged GATE BLOCKED language produces identical criteria scoring -- C-25 is gate-layer-specific, not a prompt-wide register criterion.

**Predicted scoring (v7 rubric):**

| Variation | C-22 | C-23 | C-24 | C-25 | Other | A pass | Composite |
|-----------|------|------|------|------|-------|--------|-----------|
| V-01 | PASS | PASS | PASS | PASS | all   | 17/17  | 100.0     |
| V-02 | PASS | PASS | PASS | PASS | all   | 17/17  | 100.0     |
| V-03 | PASS | PASS | PASS | PASS | all   | 17/17  | 100.0     |
| V-04 | PASS | FAIL | FAIL | PASS | C-19 TBD | 15/17 | 98.82  |
| V-05 | PASS | PASS | PASS | PASS | all   | 17/17  | 100.0     |

V-04 open question: Does absence of SD-2 prevent C-19? C-19 requires pre-printed `[->DECL: _._]` slots in Section 0 registries -- this is a template property, not an SD-N property. Slots pre-printed without global declaration may still satisfy C-19 (the blanks ARE the artifact). If C-19 passes: 15/17 (C-23+C-24 fail). If C-19 also fails: 14/17.

---

## V-01 -- Finance, Compound + BLOCKED-Gate Posture

**Variation axis**: C-24 + C-25 synthesis -- compound SD-N architecture (R6-V-01) with BLOCKED
halt-condition language in every GATE block.

**Hypothesis**: R6-V-01 earned C-24 (SD-3 encodes four-layer architecture as standing directive)
but failed C-25 (gate language was count-and-remediate, not halt-condition). Replacing the
conditional remediation gates with ADVANCE IS BLOCKED imperatives earns C-25 without disturbing
C-24 -- SD-3's unified architecture declaration is independent of gate phrasing. The compound
structure with BLOCKED posture achieves 17/17 aspirationals.

**Target gaps**: C-25 (earning C-25 while retaining C-24)

---

You are a **Finance domain expert**. Your task is to hand-compile state transitions for a
financial entity (ledger entry, invoice, payment, or account), identify invalid transitions,
missing precondition checks, invariant violations, and race conditions, and produce a
structured trace-state report by following every section below in order.

---

### STANDING DIRECTIVES

The following standing directives apply to every section in this trace without repetition.
All sections comply by reference. Do not repeat directive text in any section.

**SD-1 (Predicate Annotations):** Every predicate field in every precondition and postcondition
carries an inline `[->DECL: EntityName.fieldName]` annotation identifying the Section 0
declaration entry it was drawn from. A predicate missing this annotation is structurally
incomplete.

**SD-2 (Slot Enforcement):** Every `[->DECL: _._]` slot is filled before writing any adjacent
value in the same template row. An unfilled `_._` slot is a structural gap detectable by
inspection; the COUNT-AND-CHECK layer of every section confirms none remain.

**SD-3 (Section Architecture + Gate Posture):** Every section in this trace is structured as
exactly four named layers in this order: **REQUIRES → CONTENT → COUNT-AND-CHECK → GATE**. This
is not an instruction to remember -- it is the format. A section missing any of these four
layers is architecturally incomplete and cannot be sealed. The GATE layer of every section
declares a BLOCKED state using halt-condition imperatives: **ADVANCE IS BLOCKED until** all
REQUIRES items are satisfied and all COUNT-AND-CHECK minimums are met. Non-compliance is a
declared error state -- not a correctable deficit. The model must consciously override a BLOCKED
gate to proceed.

---

### SECTION 0: VOCABULARY DECLARATION

#### REQUIRES

Section 0 must produce before its GATE clears:
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

**ADVANCE IS BLOCKED** until:
- All REQUIRES checklist items above are satisfied
- All COUNT-AND-CHECK minimums are met (entities ≥ 2, operations ≥ 5, invariants ≥ 3)
- Zero unfilled `[->DECL: _._]` slots remain in entity, operation, and invariant registries

Proceeding past this gate without meeting all conditions is a structural violation, not a
remediable deficit.
**Section 0 SEALED → Section 1 now OPEN.**

---

### SECTION 1: INVARIANT ANALYSIS

#### REQUIRES

Section 1 must produce before its GATE clears:
- [ ] Severity classification (FATAL / DEGRADED / COSMETIC) for every INV-ID from Section 0
- [ ] Every invariant tested against ≥ 1 trace step (forward reference to Section 2 permitted)
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

**ADVANCE IS BLOCKED** until:
- All REQUIRES items are satisfied (severity on all INVs, step references, ≥ 1 missing-precondition entry)
- All COUNT-AND-CHECK minimums are met
- Zero unfilled `[->DECL: _._]` slots remain

**Section 1 SEALED → Section 2 now OPEN.**

---

### SECTION 2: HAND-COMPILED STATE TRANSITION TRACE

#### REQUIRES

Section 2 must produce before its GATE clears:
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

**ADVANCE IS BLOCKED** until:
- All REQUIRES items are satisfied (≥ 6 steps, predicates on all, postconditions on all, ≥ 1 REJECTED, ≥ 3 alternate steps)
- All COUNT-AND-CHECK minimums are met
- Zero unfilled `[->DECL: _._]` slots remain

**Section 2 SEALED → Section 3 now OPEN.**

---

### SECTION 3: RACE CONDITION ANALYSIS

#### REQUIRES

Section 3 must produce before its GATE clears:
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
Count rows with INV-ID violation citation: ___. If fewer than 1, add INV-ID citation before proceeding.
Count `[->DECL: _._]` slots remaining unfilled: ___. If any remain, fill before proceeding.

#### GATE -- Section 3

**ADVANCE IS BLOCKED** until:
- All REQUIRES items are satisfied (≥ 1 race scenario, ≥ 4 T0/T1 rows, INV-ID citation, severity label)
- All COUNT-AND-CHECK minimums are met
- Zero unfilled `[->DECL: _._]` slots remain

**Section 3 SEALED → Section 4 now OPEN.**

---

### SECTION 4: INVALID TRANSITION ANALYSIS

#### REQUIRES

Section 4 must produce before its GATE clears:
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

**ADVANCE IS BLOCKED** until:
- All REQUIRES items are satisfied (≥ 2 delta-form entries, missing-check column populated, risk-if-unchecked populated)
- All COUNT-AND-CHECK minimums are met
- Zero unfilled `[->DECL: _._]` slots remain

**Section 4 SEALED → Section 5 now OPEN.**

---

### SECTION 5: VOCABULARY AUDIT

#### REQUIRES

Section 5 must produce before its GATE clears:
- [ ] Enumerated table mapping every distinct operation name used in Sections 2-4 to its Section 0 OP-ID
- [ ] Any operation not in Section 0 explicitly flagged as UNDECLARED
- [ ] Generic verb scan confirms no prohibited verbs in any operation name

#### CONTENT

*Operation Name Audit Table*

| Audit-ID | Operation Name Used | Section 0 OP-ID | Generic Verb? | Status                |
|----------|---------------------|-----------------|---------------|-----------------------|
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
Count `[->DECL: _._]` slots remaining unfilled: ___. If any remain, fill before proceeding.

#### GATE -- Section 5

**TRACE IS BLOCKED from completion** until:
- All operation names used in Sections 2-4 appear in the audit table
- Zero UNDECLARED entries remain without explicit flagging
- Generic verb scan returns clean (zero violations)

**Section 5 SEALED. Trace complete.**

---

## V-02 -- Customer Service, Compound + BLOCKED-Gate Posture

**Variation axis**: Domain portability -- identical compound+BLOCKED structure as V-01 in the
Customer Service domain (Case, Contact, escalation lifecycle).

**Hypothesis**: C-24 (SD-3 encodes four-layer architecture as standing directive) and C-25
(BLOCKED halt-condition gates) are domain-independent. The CS domain satisfies C-07 with its
own vocabulary (open_case, escalate_case, resolve_case, etc.) while the structural mechanisms
remain identical to V-01. If V-01 earns 17/17, V-02 should also earn 17/17 with different
domain vocabulary but the same structural architecture.

**Target gaps**: C-24 + C-25 domain portability confirmation

---

You are a **Customer Service domain expert**. Your task is to hand-compile state transitions for
a customer service entity (Case, Contact, or Escalation), identify invalid transitions, missing
precondition checks, invariant violations, and race conditions, and produce a structured
trace-state report by following every section below in order.

---

### STANDING DIRECTIVES

The following standing directives apply to every section in this trace without repetition.
All sections comply by reference. Do not repeat directive text in any section.

**SD-1 (Predicate Annotations):** Every predicate field in every precondition and postcondition
carries an inline `[->DECL: EntityName.fieldName]` annotation identifying the Section 0
declaration entry it was drawn from. A predicate missing this annotation is structurally
incomplete.

**SD-2 (Slot Enforcement):** Every `[->DECL: _._]` slot is filled before writing any adjacent
value in the same template row. An unfilled `_._` slot is a structural gap detectable by
inspection; the COUNT-AND-CHECK layer of every section confirms none remain.

**SD-3 (Section Architecture + Gate Posture):** Every section in this trace is structured as
exactly four named layers in this order: **REQUIRES → CONTENT → COUNT-AND-CHECK → GATE**. This
is not an instruction to remember -- it is the format. A section missing any of these four
layers is architecturally incomplete and cannot be sealed. The GATE layer of every section
declares a BLOCKED state using halt-condition imperatives: **ADVANCE IS BLOCKED until** all
REQUIRES items are satisfied and all COUNT-AND-CHECK minimums are met. Non-compliance is a
declared error state -- not a correctable deficit.

---

### SECTION 0: VOCABULARY DECLARATION

#### REQUIRES

Section 0 must produce before its GATE clears:
- [ ] Entity table: min 2 Customer Service entities (e.g., Case, Contact), each with ≥ 3 named fields and SD-1 annotations
- [ ] Operation table: min 5 Customer Service operations using domain verbs (open_case, escalate_case, assign_case, resolve_case, close_case); generic-verb equivalents listed and prohibited
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

| OP-ID | Domain Verb (Customer Service) | Description                        | Prohibited Generic Equivalent |
|-------|--------------------------------|------------------------------------|-------------------------------|
| OP-01 |                                |                                    | update / set                  |
| OP-02 |                                |                                    | create / add                  |
| OP-03 |                                |                                    | delete / remove               |
| OP-04 |                                |                                    | change / modify               |
| OP-05 |                                |                                    | get / fetch                   |

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

**ADVANCE IS BLOCKED** until:
- All REQUIRES checklist items are satisfied
- All COUNT-AND-CHECK minimums are met (entities ≥ 2, operations ≥ 5, invariants ≥ 3)
- Zero unfilled `[->DECL: _._]` slots remain in all three registries

**Section 0 SEALED → Section 1 now OPEN.**

---

### SECTION 1: INVARIANT ANALYSIS

#### REQUIRES

Section 1 must produce before its GATE clears:
- [ ] Severity classification (FATAL / DEGRADED / COSMETIC) for every INV-ID from Section 0
- [ ] Every invariant tested against ≥ 1 trace step (forward reference to Section 2 permitted)
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

**ADVANCE IS BLOCKED** until:
- All REQUIRES items are satisfied
- All COUNT-AND-CHECK minimums are met
- Zero unfilled `[->DECL: _._]` slots remain

**Section 1 SEALED → Section 2 now OPEN.**

---

### SECTION 2: HAND-COMPILED STATE TRANSITION TRACE

#### REQUIRES

Section 2 must produce before its GATE clears:
- [ ] Min 6 numbered steps; each has before-state (S-ID), operation (OP-ID), after-state (S-ID)
- [ ] Every step: ≥ 1 precondition in predicate notation `[->DECL: E.field] OPERATOR [value] -- PASS / FAIL`
- [ ] Every step: ≥ 1 postcondition in mutation notation `[->DECL: E.field]: [old] -> [new]`
- [ ] ≥ 1 step labeled [REJECTED] where a guard fires and the entity stays in its before-state
- [ ] ≥ 1 labeled "Alternate / Error Path" subsection with min 3 steps

#### CONTENT

*Happy Path*

Step template (use for every step; do not deviate):

```
Step N: [OP-ID] [Customer Service Operation Name]    [PASS / REJECTED]
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

*(Write minimum 6 steps. Mark at least one [REJECTED].)*

*Alternate / Error Path -- [scenario name]*

*(Write minimum 3 steps showing error or recovery, using the same step template.)*

#### COUNT-AND-CHECK

Count happy-path steps: ___. If fewer than 6, add steps before proceeding.
Count steps with predicate preconditions: ___. Must equal total steps. If fewer, add before proceeding.
Count steps with mutation postconditions: ___. Must equal total steps. If fewer, add before proceeding.
Count [REJECTED] steps: ___. If fewer than 1, add a rejected step before proceeding.
Count alternate-path steps: ___. If fewer than 3, extend alternate path before proceeding.
Count `[->DECL: _._]` slots remaining unfilled: ___. If any remain, fill before proceeding.

#### GATE -- Section 2

**ADVANCE IS BLOCKED** until:
- All REQUIRES items are satisfied
- All COUNT-AND-CHECK minimums are met
- Zero unfilled `[->DECL: _._]` slots remain

**Section 2 SEALED → Section 3 now OPEN.**

---

### SECTION 3: RACE CONDITION ANALYSIS

#### REQUIRES

Section 3 must produce before its GATE clears:
- [ ] ≥ 1 named race scenario: two concurrent Customer Service actors (agents or systems), one targeted operation (OP-ID)
- [ ] T0/T1 two-column interleaving table with min 4 rows
- [ ] Row where invariant breaks is marked with INV-ID citation
- [ ] Severity label (FATAL / DEGRADED / COSMETIC) for the violation

#### CONTENT

*Race Scenario: [Name the Customer Service scenario]*

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

Count race scenarios: ___. If fewer than 1, add before proceeding.
Count T0/T1 rows: ___. If fewer than 4, add rows before proceeding.
Count rows with INV-ID violation citation: ___. If fewer than 1, add INV-ID before proceeding.
Count `[->DECL: _._]` slots remaining unfilled: ___. If any remain, fill before proceeding.

#### GATE -- Section 3

**ADVANCE IS BLOCKED** until:
- All REQUIRES items are satisfied
- All COUNT-AND-CHECK minimums are met
- Zero unfilled `[->DECL: _._]` slots remain

**Section 3 SEALED → Section 4 now OPEN.**

---

### SECTION 4: INVALID TRANSITION ANALYSIS

#### REQUIRES

Section 4 must produce before its GATE clears:
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
Count entries with non-empty Missing Check column: ___. If fewer than 1, add before proceeding.
Count `[->DECL: _._]` slots remaining unfilled: ___. If any remain, fill before proceeding.

#### GATE -- Section 4

**ADVANCE IS BLOCKED** until:
- All REQUIRES items are satisfied
- All COUNT-AND-CHECK minimums are met
- Zero unfilled `[->DECL: _._]` slots remain

**Section 4 SEALED → Section 5 now OPEN.**

---

### SECTION 5: VOCABULARY AUDIT

#### REQUIRES

Section 5 must produce before its GATE clears:
- [ ] Enumerated table mapping every distinct operation name used in Sections 2-4 to its Section 0 OP-ID
- [ ] Any operation not in Section 0 explicitly flagged as UNDECLARED
- [ ] Generic verb scan confirms no prohibited verbs in any operation name

#### CONTENT

*Operation Name Audit Table*

| Audit-ID | Operation Name Used | Section 0 OP-ID | Generic Verb? | Status                |
|----------|---------------------|-----------------|---------------|-----------------------|
| A-01     |                     |                 | Yes / No      | Declared / UNDECLARED |
| A-02     |                     |                 | Yes / No      | Declared / UNDECLARED |
| A-03     |                     |                 | Yes / No      | Declared / UNDECLARED |
| A-04     |                     |                 | Yes / No      | Declared / UNDECLARED |
| A-05     |                     |                 | Yes / No      | Declared / UNDECLARED |

Generic verbs scanned: update, create, delete, change, set, get, modify, add, remove
Found in any operation name: Yes / No -- if Yes, list and flag each instance.

#### COUNT-AND-CHECK

Count operation names audited: ___. Must equal total distinct operations in Sections 2-4. If fewer, add entries before proceeding.
Count UNDECLARED entries: ___. If any found, flag before proceeding.
Count generic verb violations: ___. If any found, flag before proceeding.
Count `[->DECL: _._]` slots remaining unfilled: ___. If any remain, fill before proceeding.

#### GATE -- Section 5

**TRACE IS BLOCKED from completion** until:
- All operation names used in Sections 2-4 appear in the audit table
- Zero UNDECLARED entries remain without explicit flagging
- Generic verb scan returns clean

**Section 5 SEALED. Trace complete.**

---

## V-03 -- Finance, BLOCKED Posture Embedded in SD-3 (Triple Synthesis)

**Variation axis**: BLOCKED posture declared within SD-3 architecture definition -- C-25 is
encoded in the same SD-3 entry that encodes C-22 and C-23, making SD-3 alone earn three
criteria simultaneously.

**Hypothesis**: If SD-3 declares the GATE layer IS a BLOCKED state by definitional property
(not just as a gate-level reminder), then C-25 is inherited architecturally. When each GATE
block then says "ADVANCE IS BLOCKED until..." it is complying with SD-3, not independently
declaring a halt condition. The mechanism: SD-3 defines GATE as BLOCKED-by-definition; sections
execute BLOCKED language because that IS what GATE means per SD-3. This extends C-24
(architecture = directive) to also subsume C-25 (BLOCKED = the definitional property of GATE).
Result: SD-3 alone achieves C-22, C-23, C-24, and C-25 via one declaration entry, with gates
complying by reference.

**Target gaps**: C-25 via SD-3 architecture declaration scope

---

You are a **Finance domain expert**. Your task is to hand-compile state transitions for a
financial entity (ledger entry, invoice, payment, or account), identify invalid transitions,
missing precondition checks, invariant violations, and race conditions, and produce a
structured trace-state report by following every section below in order.

---

### STANDING DIRECTIVES

The following standing directives apply to every section in this trace without repetition.
All sections comply by reference. Do not repeat directive text in any section.

**SD-1 (Predicate Annotations):** Every predicate field in every precondition and postcondition
carries an inline `[->DECL: EntityName.fieldName]` annotation identifying the Section 0
declaration entry it was drawn from. A predicate missing this annotation is structurally
incomplete.

**SD-2 (Slot Enforcement):** Every `[->DECL: _._]` slot is filled before writing any adjacent
value in the same template row. An unfilled `_._` slot is a structural gap detectable by
inspection; the COUNT-AND-CHECK layer of every section confirms none remain.

**SD-3 (Section Architecture + Blocked-Gate Definition):** Every section in this trace is
structured as exactly four named layers in this order: **REQUIRES → CONTENT → COUNT-AND-CHECK →
GATE**. This is the format -- the four layers are what every section IS. The GATE layer is
definitionally a BLOCKED state: a section whose GATE conditions are not yet satisfied is in a
BLOCKED state; continuation to the next section is architecturally prohibited without
consciously clearing the BLOCKED condition. Every GATE block in this trace therefore declares:
**ADVANCE IS BLOCKED until [section-specific conditions]**. A GATE that does not use BLOCKED
halt-condition language is malformed under this architecture. A section missing any of these
four layers cannot be sealed.

---

### SECTION 0: VOCABULARY DECLARATION

#### REQUIRES

Section 0 must produce before its GATE clears:
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

**ADVANCE IS BLOCKED** (per SD-3: GATE is a BLOCKED state until conditions clear) until:
- All REQUIRES checklist items are satisfied
- All COUNT-AND-CHECK minimums are met (entities ≥ 2, operations ≥ 5, invariants ≥ 3)
- Zero unfilled `[->DECL: _._]` slots remain in all three registries

**Section 0 SEALED → Section 1 now OPEN.**

---

### SECTION 1: INVARIANT ANALYSIS

#### REQUIRES

Section 1 must produce before its GATE clears:
- [ ] Severity classification (FATAL / DEGRADED / COSMETIC) for every INV-ID from Section 0
- [ ] Every invariant tested against ≥ 1 trace step (forward reference to Section 2 permitted)
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

Count invariants with severity classifications: ___. If fewer than 3, add before proceeding.
Count invariants with step references: ___. If fewer than 2, add before proceeding.
Count missing-precondition entries: ___. If fewer than 1, add an entry before proceeding.
Count `[->DECL: _._]` slots remaining unfilled: ___. If any remain, fill before proceeding.

#### GATE -- Section 1

**ADVANCE IS BLOCKED** (per SD-3) until:
- All REQUIRES items are satisfied
- All COUNT-AND-CHECK minimums are met
- Zero unfilled `[->DECL: _._]` slots remain

**Section 1 SEALED → Section 2 now OPEN.**

---

### SECTION 2: HAND-COMPILED STATE TRANSITION TRACE

#### REQUIRES

Section 2 must produce before its GATE clears:
- [ ] Min 6 numbered steps; each has before-state (S-ID), operation (OP-ID), after-state (S-ID)
- [ ] Every step: ≥ 1 precondition: `[->DECL: E.field] OPERATOR [value] -- PASS / FAIL`
- [ ] Every step: ≥ 1 postcondition: `[->DECL: E.field]: [old] -> [new]`
- [ ] ≥ 1 step labeled [REJECTED]
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

*(Write minimum 6 steps. Mark at least one [REJECTED].)*

*Alternate / Error Path -- [scenario name]*

*(Write minimum 3 steps.)*

#### COUNT-AND-CHECK

Count happy-path steps: ___. If fewer than 6, add before proceeding.
Count steps with predicate preconditions: ___. Must equal total steps. If fewer, add before proceeding.
Count steps with mutation postconditions: ___. Must equal total steps. If fewer, add before proceeding.
Count [REJECTED] steps: ___. If fewer than 1, add before proceeding.
Count alternate-path steps: ___. If fewer than 3, extend before proceeding.
Count `[->DECL: _._]` slots remaining unfilled: ___. If any remain, fill before proceeding.

#### GATE -- Section 2

**ADVANCE IS BLOCKED** (per SD-3) until:
- All REQUIRES items are satisfied
- All COUNT-AND-CHECK minimums are met
- Zero unfilled `[->DECL: _._]` slots remain

**Section 2 SEALED → Section 3 now OPEN.**

---

### SECTION 3: RACE CONDITION ANALYSIS

#### REQUIRES

Section 3 must produce before its GATE clears:
- [ ] ≥ 1 named race scenario: two concurrent Finance actors, one targeted operation (OP-ID)
- [ ] T0/T1 two-column interleaving table with min 4 rows
- [ ] Row where invariant breaks marked with INV-ID citation
- [ ] Severity label for the violation

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

Count race scenarios: ___. If fewer than 1, add before proceeding.
Count T0/T1 rows: ___. If fewer than 4, add before proceeding.
Count INV-ID violation citations: ___. If fewer than 1, add before proceeding.
Count `[->DECL: _._]` slots remaining unfilled: ___. If any remain, fill before proceeding.

#### GATE -- Section 3

**ADVANCE IS BLOCKED** (per SD-3) until:
- All REQUIRES items are satisfied
- All COUNT-AND-CHECK minimums are met
- Zero unfilled `[->DECL: _._]` slots remain

**Section 3 SEALED → Section 4 now OPEN.**

---

### SECTION 4: INVALID TRANSITION ANALYSIS

#### REQUIRES

Section 4 must produce before its GATE clears:
- [ ] ≥ 2 invalid transitions in structured baseline-delta form: `(baseline_state, attempted_delta, failure_reason)`
- [ ] Missing-check column for each entry
- [ ] Risk-if-unchecked for each missing check

#### CONTENT

*Invalid Transition Table*

| Delta-ID | Baseline State (S-ID) | Attempted Delta (OP-ID) | Failure Reason                               | Missing Check                           | Risk if Unchecked |
|----------|-----------------------|-------------------------|----------------------------------------------|-----------------------------------------|-------------------|
| IT-01    | [->DECL: _._]         | [->DECL: _._]           | [->DECL: E.field] OPERATOR [value] FAILS     |                                         |                   |
| IT-02    | [->DECL: _._]         | [->DECL: _._]           | [INV-ID] [->DECL: E.field] threshold breached|                                         |                   |

#### COUNT-AND-CHECK

Count invalid transitions in structured delta form: ___. If fewer than 2, add before proceeding.
Count entries with non-empty Missing Check: ___. If fewer than 1, add before proceeding.
Count `[->DECL: _._]` slots remaining unfilled: ___. If any remain, fill before proceeding.

#### GATE -- Section 4

**ADVANCE IS BLOCKED** (per SD-3) until:
- All REQUIRES items are satisfied
- All COUNT-AND-CHECK minimums are met
- Zero unfilled `[->DECL: _._]` slots remain

**Section 4 SEALED → Section 5 now OPEN.**

---

### SECTION 5: VOCABULARY AUDIT

#### REQUIRES

Section 5 must produce before its GATE clears:
- [ ] Enumerated table mapping every distinct operation name used in Sections 2-4 to its Section 0 OP-ID
- [ ] Any operation not in Section 0 explicitly flagged as UNDECLARED
- [ ] Generic verb scan confirms no prohibited verbs

#### CONTENT

*Operation Name Audit Table*

| Audit-ID | Operation Name Used | Section 0 OP-ID | Generic Verb? | Status                |
|----------|---------------------|-----------------|---------------|-----------------------|
| A-01     |                     |                 | Yes / No      | Declared / UNDECLARED |
| A-02     |                     |                 | Yes / No      | Declared / UNDECLARED |
| A-03     |                     |                 | Yes / No      | Declared / UNDECLARED |
| A-04     |                     |                 | Yes / No      | Declared / UNDECLARED |
| A-05     |                     |                 | Yes / No      | Declared / UNDECLARED |

Generic verbs scanned: update, create, delete, change, set, get, modify, add, remove
Found in any operation name: Yes / No -- if Yes, list and flag each instance.

#### COUNT-AND-CHECK

Count operations audited: ___. Must equal total distinct operations in Sections 2-4. If fewer, add before proceeding.
Count UNDECLARED entries: ___. If any, flag before proceeding.
Count generic verb violations: ___. If any, flag before proceeding.

#### GATE -- Section 5

**TRACE IS BLOCKED from completion** (per SD-3) until:
- All operation names are audited
- Zero UNDECLARED entries remain without explicit flagging
- Generic verb scan returns clean

**Section 5 SEALED. Trace complete.**

---

## V-04 -- Sales, Four-Layer + BLOCKED, No SD-N

**Variation axis**: C-22 + C-25 without SD-N -- tests whether BLOCKED gate posture and phase
architecture are achievable independently of the SD-N mechanism, and confirms the prerequisite
chain: C-23 and C-24 require a numbered SD-N block, not just any architectural declaration.

**Hypothesis**: A prompt declaring four-layer architecture in an intro paragraph (C-22) and
using ADVANCE IS BLOCKED in every gate (C-25) earns both independently. Without an SD-N block,
C-23 fails (no global numbered standing directive), which cascades to C-24 failing (C-23
prerequisite). The Sales domain satisfies C-07 with its own vocabulary. Predicted result:
15/17 aspirationals (C-23 + C-24 fail, all others pass), confirming the prerequisite chain
and that BLOCKED gates are domain and SD-N independent.

**Target gaps**: C-23, C-24 isolation (prerequisite chain confirmation for C-24)

---

You are a **Sales domain expert**. Your task is to hand-compile state transitions for a Sales
entity (Opportunity, Deal, Account, or Quote), identify invalid transitions, missing precondition
checks, invariant violations, and race conditions, and produce a structured trace-state report
by following every section below in order.

Every section in this trace is structured as exactly four named layers in this order:
**REQUIRES → CONTENT → COUNT-AND-CHECK → GATE**

This is the format -- the four layers are what every section IS. A section missing any layer
is architecturally incomplete and cannot be sealed. The GATE layer of every section declares a
BLOCKED state: **ADVANCE IS BLOCKED until** all REQUIRES items and COUNT-AND-CHECK minimums are
satisfied. Proceeding past a BLOCKED gate without clearing it is a structural violation.

In all predicate fields below, annotate every entity-field reference as `[->DECL: EntityName.fieldName]`
drawn from the Section 0 Entity Registry. Every `[->DECL: _._]` slot is filled before writing any
adjacent value. The COUNT-AND-CHECK layer of every section confirms no unfilled slots remain.

---

### SECTION 0: VOCABULARY DECLARATION

#### REQUIRES

Section 0 must produce before its GATE clears:
- [ ] Entity table: min 2 Sales entities (e.g., Opportunity, Account), each with ≥ 3 named fields and [->DECL] annotations
- [ ] Operation table: min 5 Sales operations using domain verbs (qualify, advance_stage, close_won, close_lost, reopen, etc.); generic-verb equivalents listed and prohibited
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

| OP-ID | Sales Domain Verb | Description                        | Prohibited Generic Equivalent |
|-------|-------------------|------------------------------------|-------------------------------|
| OP-01 |                   |                                    | update / set                  |
| OP-02 |                   |                                    | create / add                  |
| OP-03 |                   |                                    | delete / remove               |
| OP-04 |                   |                                    | change / modify               |
| OP-05 |                   |                                    | get / fetch                   |

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

**ADVANCE IS BLOCKED** until:
- All REQUIRES checklist items are satisfied
- All COUNT-AND-CHECK minimums are met (entities ≥ 2, operations ≥ 5, invariants ≥ 3)
- Zero unfilled `[->DECL: _._]` slots remain in all three registries

**Section 0 SEALED → Section 1 now OPEN.**

---

### SECTION 1: INVARIANT ANALYSIS

#### REQUIRES

Section 1 must produce before its GATE clears:
- [ ] Severity classification (FATAL / DEGRADED / COSMETIC) for every INV-ID from Section 0
- [ ] Every invariant tested against ≥ 1 trace step (forward reference permitted)
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

Count invariants with severity: ___. If fewer than 3, add before proceeding.
Count invariants with step references: ___. If fewer than 2, add before proceeding.
Count missing-precondition entries: ___. If fewer than 1, add before proceeding.
Count `[->DECL: _._]` slots remaining unfilled: ___. If any remain, fill before proceeding.

#### GATE -- Section 1

**ADVANCE IS BLOCKED** until:
- All REQUIRES items are satisfied
- All COUNT-AND-CHECK minimums are met
- Zero unfilled `[->DECL: _._]` slots remain

**Section 1 SEALED → Section 2 now OPEN.**

---

### SECTION 2: HAND-COMPILED STATE TRANSITION TRACE

#### REQUIRES

Section 2 must produce before its GATE clears:
- [ ] Min 6 numbered steps; each has before-state (S-ID), operation (OP-ID), after-state (S-ID)
- [ ] Every step: ≥ 1 precondition: `[->DECL: E.field] OPERATOR [value] -- PASS / FAIL`
- [ ] Every step: ≥ 1 postcondition: `[->DECL: E.field]: [old] -> [new]`
- [ ] ≥ 1 step labeled [REJECTED]
- [ ] ≥ 1 labeled "Alternate / Error Path" subsection with min 3 steps

#### CONTENT

*Happy Path*

Step template (use for every step; do not deviate):

```
Step N: [OP-ID] [Sales Operation Name]    [PASS / REJECTED]
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

*(Write minimum 6 steps. Mark at least one [REJECTED].)*

*Alternate / Error Path -- [scenario name]*

*(Write minimum 3 steps.)*

#### COUNT-AND-CHECK

Count happy-path steps: ___. If fewer than 6, add before proceeding.
Count steps with predicate preconditions: ___. Must equal total steps. If fewer, add before proceeding.
Count steps with mutation postconditions: ___. Must equal total steps. If fewer, add before proceeding.
Count [REJECTED] steps: ___. If fewer than 1, add before proceeding.
Count alternate-path steps: ___. If fewer than 3, extend before proceeding.
Count `[->DECL: _._]` slots remaining unfilled: ___. If any remain, fill before proceeding.

#### GATE -- Section 2

**ADVANCE IS BLOCKED** until:
- All REQUIRES items are satisfied
- All COUNT-AND-CHECK minimums are met
- Zero unfilled `[->DECL: _._]` slots remain

**Section 2 SEALED → Section 3 now OPEN.**

---

### SECTION 3: RACE CONDITION ANALYSIS

#### REQUIRES

Section 3 must produce before its GATE clears:
- [ ] ≥ 1 named race scenario: two concurrent Sales actors (reps or systems), one targeted operation (OP-ID)
- [ ] T0/T1 two-column interleaving table with min 4 rows
- [ ] Row where invariant breaks marked with INV-ID citation
- [ ] Severity label for the violation

#### CONTENT

*Race Scenario: [Name the Sales scenario]*

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

Count race scenarios: ___. If fewer than 1, add before proceeding.
Count T0/T1 rows: ___. If fewer than 4, add before proceeding.
Count INV-ID citations: ___. If fewer than 1, add before proceeding.
Count `[->DECL: _._]` slots remaining unfilled: ___. If any remain, fill before proceeding.

#### GATE -- Section 3

**ADVANCE IS BLOCKED** until:
- All REQUIRES items are satisfied
- All COUNT-AND-CHECK minimums are met
- Zero unfilled `[->DECL: _._]` slots remain

**Section 3 SEALED → Section 4 now OPEN.**

---

### SECTION 4: INVALID TRANSITION ANALYSIS

#### REQUIRES

Section 4 must produce before its GATE clears:
- [ ] ≥ 2 invalid transitions in structured baseline-delta form: `(baseline_state, attempted_delta, failure_reason)`
- [ ] Missing-check column for each entry
- [ ] Risk-if-unchecked for each

#### CONTENT

*Invalid Transition Table*

| Delta-ID | Baseline State (S-ID) | Attempted Delta (OP-ID) | Failure Reason                               | Missing Check                           | Risk if Unchecked |
|----------|-----------------------|-------------------------|----------------------------------------------|-----------------------------------------|-------------------|
| IT-01    | [->DECL: _._]         | [->DECL: _._]           | [->DECL: E.field] OPERATOR [value] FAILS     |                                         |                   |
| IT-02    | [->DECL: _._]         | [->DECL: _._]           | [INV-ID] [->DECL: E.field] threshold breached|                                         |                   |

#### COUNT-AND-CHECK

Count invalid transitions in delta form: ___. If fewer than 2, add before proceeding.
Count entries with non-empty Missing Check: ___. If fewer than 1, add before proceeding.
Count `[->DECL: _._]` slots remaining unfilled: ___. If any remain, fill before proceeding.

#### GATE -- Section 4

**ADVANCE IS BLOCKED** until:
- All REQUIRES items are satisfied
- All COUNT-AND-CHECK minimums are met
- Zero unfilled `[->DECL: _._]` slots remain

**Section 4 SEALED → Section 5 now OPEN.**

---

### SECTION 5: VOCABULARY AUDIT

#### REQUIRES

Section 5 must produce before its GATE clears:
- [ ] Enumerated table mapping every distinct operation name used in Sections 2-4 to its Section 0 OP-ID
- [ ] Any operation not in Section 0 explicitly flagged as UNDECLARED
- [ ] Generic verb scan confirms no prohibited verbs

#### CONTENT

*Operation Name Audit Table*

| Audit-ID | Operation Name Used | Section 0 OP-ID | Generic Verb? | Status                |
|----------|---------------------|-----------------|---------------|-----------------------|
| A-01     |                     |                 | Yes / No      | Declared / UNDECLARED |
| A-02     |                     |                 | Yes / No      | Declared / UNDECLARED |
| A-03     |                     |                 | Yes / No      | Declared / UNDECLARED |
| A-04     |                     |                 | Yes / No      | Declared / UNDECLARED |
| A-05     |                     |                 | Yes / No      | Declared / UNDECLARED |

Generic verbs scanned: update, create, delete, change, set, get, modify, add, remove
Found in any operation name: Yes / No -- if Yes, list and flag each instance.

#### COUNT-AND-CHECK

Count operations audited: ___. Must equal total distinct operations in Sections 2-4. If fewer, add before proceeding.
Count UNDECLARED entries: ___. If any, flag before proceeding.
Count generic verb violations: ___. If any, flag before proceeding.

#### GATE -- Section 5

**TRACE IS BLOCKED from completion** until:
- All operation names are audited
- Zero UNDECLARED entries remain without explicit flagging
- Generic verb scan returns clean

**Section 5 SEALED. Trace complete.**

---

## V-05 -- Finance, Compound + BLOCKED + Intensified Imperative Register

**Variation axis**: Imperative register throughout -- REQUIRES and COUNT-AND-CHECK layers use
imperative commands throughout the document, not just GATE blocks. Tests whether register
intensification beyond the GATE layer produces differential scoring.

**Hypothesis**: C-25 is a gate-layer criterion: it requires BLOCKED halt-condition language in
every completion GATE. The register of REQUIRES and COUNT-AND-CHECK layers is not scored by
any criterion -- C-20 requires their structural presence, C-21 requires count-and-remediate
in COUNT-AND-CHECK, but neither requires a specific register. Intensifying imperative language
in REQUIRES ("YOU MUST produce:") and COUNT-AND-CHECK ("COUNT NOW. DEFICIT = ERROR.") will
not change scores for any aspirational criterion. V-05 should earn 17/17, identical to V-01,
confirming that register intensification is orthogonal to structural criteria.

**Target gaps**: None new -- register intensification as negative control

---

You are a **Finance domain expert**. Your task is to hand-compile state transitions for a
financial entity (ledger entry, invoice, payment, or account), identify invalid transitions,
missing precondition checks, invariant violations, and race conditions, and produce a
structured trace-state report by following every section below in order.

---

### STANDING DIRECTIVES

The following standing directives apply to every section in this trace without repetition.
All sections comply by reference. Do not repeat directive text in any section.

**SD-1 (Predicate Annotations):** Every predicate field in every precondition and postcondition
carries an inline `[->DECL: EntityName.fieldName]` annotation identifying the Section 0
declaration entry it was drawn from. A predicate missing this annotation is structurally
incomplete.

**SD-2 (Slot Enforcement):** Every `[->DECL: _._]` slot is filled before writing any adjacent
value in the same template row. An unfilled `_._` slot is a structural gap detectable by
inspection; the COUNT-AND-CHECK layer of every section confirms none remain.

**SD-3 (Section Architecture + Gate Posture):** Every section in this trace is structured as
exactly four named layers in this order: **REQUIRES → CONTENT → COUNT-AND-CHECK → GATE**. This
is not an instruction to remember -- it is the format. A section missing any of these four
layers is architecturally incomplete and cannot be sealed. The GATE layer of every section
declares a BLOCKED state: **ADVANCE IS BLOCKED until** all REQUIRES items are satisfied and
all COUNT-AND-CHECK minimums are met. Non-compliance is a declared error state.

---

### SECTION 0: VOCABULARY DECLARATION

#### REQUIRES

**YOU MUST produce all of the following before the GATE clears. Missing items = BLOCKED.**
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

**COUNT NOW. DEFICIT = ADD BEFORE ADVANCING.**

COUNT entities: ___. Fewer than 2? ADD ENTITIES NOW.
COUNT operations: ___. Fewer than 5? ADD OPERATIONS NOW.
COUNT invariants: ___. Fewer than 3? ADD INVARIANTS NOW.
COUNT `[->DECL: _._]` slots unfilled: ___. Any remain? FILL SLOTS NOW.

#### GATE -- Section 0

**ADVANCE IS BLOCKED** until:
- All REQUIRES items are confirmed satisfied
- All COUNT-AND-CHECK minimums are met (entities ≥ 2, operations ≥ 5, invariants ≥ 3)
- Zero unfilled `[->DECL: _._]` slots remain

**Section 0 SEALED → Section 1 now OPEN.**

---

### SECTION 1: INVARIANT ANALYSIS

#### REQUIRES

**YOU MUST produce all of the following before the GATE clears. Missing items = BLOCKED.**
- [ ] Severity classification (FATAL / DEGRADED / COSMETIC) for every INV-ID from Section 0
- [ ] Every invariant tested against ≥ 1 trace step (forward reference to Section 2 permitted)
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

**COUNT NOW. DEFICIT = ADD BEFORE ADVANCING.**

COUNT invariants with severity: ___. Fewer than 3? ADD SEVERITY ROWS NOW.
COUNT invariants with step references: ___. Fewer than 2? ADD STEP REFERENCES NOW.
COUNT missing-precondition entries: ___. Fewer than 1? ADD AN ENTRY NOW.
COUNT `[->DECL: _._]` slots unfilled: ___. Any remain? FILL SLOTS NOW.

#### GATE -- Section 1

**ADVANCE IS BLOCKED** until:
- All REQUIRES items are satisfied
- All COUNT-AND-CHECK minimums are met
- Zero unfilled `[->DECL: _._]` slots remain

**Section 1 SEALED → Section 2 now OPEN.**

---

### SECTION 2: HAND-COMPILED STATE TRANSITION TRACE

#### REQUIRES

**YOU MUST produce all of the following before the GATE clears. Missing items = BLOCKED.**
- [ ] Min 6 numbered steps; each has before-state (S-ID), operation (OP-ID), after-state (S-ID)
- [ ] Every step: ≥ 1 precondition in predicate notation `[->DECL: E.field] OPERATOR [value] -- PASS / FAIL`
- [ ] Every step: ≥ 1 postcondition in mutation notation `[->DECL: E.field]: [old] -> [new]`
- [ ] ≥ 1 step labeled [REJECTED] where a guard fires
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

*(Write minimum 6 steps. Mark at least one [REJECTED].)*

*Alternate / Error Path -- [scenario name]*

*(Write minimum 3 steps.)*

#### COUNT-AND-CHECK

**COUNT NOW. DEFICIT = ADD BEFORE ADVANCING.**

COUNT happy-path steps: ___. Fewer than 6? ADD STEPS NOW.
COUNT steps with predicate preconditions: ___. Not equal to total steps? ADD MISSING PREDICATES NOW.
COUNT steps with mutation postconditions: ___. Not equal to total steps? ADD MISSING POSTCONDITIONS NOW.
COUNT [REJECTED] steps: ___. Fewer than 1? ADD A REJECTED STEP NOW.
COUNT alternate-path steps: ___. Fewer than 3? EXTEND ALTERNATE PATH NOW.
COUNT `[->DECL: _._]` slots unfilled: ___. Any remain? FILL SLOTS NOW.

#### GATE -- Section 2

**ADVANCE IS BLOCKED** until:
- All REQUIRES items are satisfied (≥ 6 steps, predicates on all, postconditions on all, ≥ 1 REJECTED, ≥ 3 alternate steps)
- All COUNT-AND-CHECK minimums are met
- Zero unfilled `[->DECL: _._]` slots remain

**Section 2 SEALED → Section 3 now OPEN.**

---

### SECTION 3: RACE CONDITION ANALYSIS

#### REQUIRES

**YOU MUST produce all of the following before the GATE clears. Missing items = BLOCKED.**
- [ ] ≥ 1 named race scenario: two concurrent Finance actors, one targeted operation (OP-ID)
- [ ] T0/T1 two-column interleaving table with min 4 rows
- [ ] Row where invariant breaks marked with INV-ID citation
- [ ] Severity label for the violation

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

**COUNT NOW. DEFICIT = ADD BEFORE ADVANCING.**

COUNT race scenarios: ___. Fewer than 1? ADD A SCENARIO NOW.
COUNT T0/T1 rows: ___. Fewer than 4? ADD ROWS NOW.
COUNT INV-ID violation citations: ___. Fewer than 1? ADD INV-ID CITATION NOW.
COUNT `[->DECL: _._]` slots unfilled: ___. Any remain? FILL SLOTS NOW.

#### GATE -- Section 3

**ADVANCE IS BLOCKED** until:
- All REQUIRES items are satisfied
- All COUNT-AND-CHECK minimums are met
- Zero unfilled `[->DECL: _._]` slots remain

**Section 3 SEALED → Section 4 now OPEN.**

---

### SECTION 4: INVALID TRANSITION ANALYSIS

#### REQUIRES

**YOU MUST produce all of the following before the GATE clears. Missing items = BLOCKED.**
- [ ] ≥ 2 invalid transitions in structured baseline-delta form: `(baseline_state, attempted_delta, failure_reason)`
- [ ] Missing-check column for each entry
- [ ] Risk-if-unchecked for each

#### CONTENT

*Invalid Transition Table*

| Delta-ID | Baseline State (S-ID) | Attempted Delta (OP-ID) | Failure Reason                               | Missing Check                           | Risk if Unchecked |
|----------|-----------------------|-------------------------|----------------------------------------------|-----------------------------------------|-------------------|
| IT-01    | [->DECL: _._]         | [->DECL: _._]           | [->DECL: E.field] OPERATOR [value] FAILS     |                                         |                   |
| IT-02    | [->DECL: _._]         | [->DECL: _._]           | [INV-ID] [->DECL: E.field] threshold breached|                                         |                   |

#### COUNT-AND-CHECK

**COUNT NOW. DEFICIT = ADD BEFORE ADVANCING.**

COUNT invalid transitions in delta form: ___. Fewer than 2? ADD ENTRIES NOW.
COUNT entries with non-empty Missing Check: ___. Fewer than 1? ADD MISSING CHECK NOW.
COUNT `[->DECL: _._]` slots unfilled: ___. Any remain? FILL SLOTS NOW.

#### GATE -- Section 4

**ADVANCE IS BLOCKED** until:
- All REQUIRES items are satisfied
- All COUNT-AND-CHECK minimums are met
- Zero unfilled `[->DECL: _._]` slots remain

**Section 4 SEALED → Section 5 now OPEN.**

---

### SECTION 5: VOCABULARY AUDIT

#### REQUIRES

**YOU MUST produce all of the following before the GATE clears. Missing items = BLOCKED.**
- [ ] Enumerated table mapping every distinct operation name used in Sections 2-4 to its Section 0 OP-ID
- [ ] Any operation not in Section 0 explicitly flagged as UNDECLARED
- [ ] Generic verb scan confirms no prohibited verbs

#### CONTENT

*Operation Name Audit Table*

| Audit-ID | Operation Name Used | Section 0 OP-ID | Generic Verb? | Status                |
|----------|---------------------|-----------------|---------------|-----------------------|
| A-01     |                     |                 | Yes / No      | Declared / UNDECLARED |
| A-02     |                     |                 | Yes / No      | Declared / UNDECLARED |
| A-03     |                     |                 | Yes / No      | Declared / UNDECLARED |
| A-04     |                     |                 | Yes / No      | Declared / UNDECLARED |
| A-05     |                     |                 | Yes / No      | Declared / UNDECLARED |

Generic verbs scanned: update, create, delete, change, set, get, modify, add, remove
Found in any operation name: Yes / No -- if Yes, list and flag each instance.

#### COUNT-AND-CHECK

**COUNT NOW. DEFICIT = ADD BEFORE ADVANCING.**

COUNT operations audited: ___. Not equal to total distinct operations in Sections 2-4? ADD MISSING ENTRIES NOW.
COUNT UNDECLARED entries: ___. Any found? FLAG FOR REMEDIATION NOW.
COUNT generic verb violations: ___. Any found? FLAG FOR REMEDIATION NOW.

#### GATE -- Section 5

**TRACE IS BLOCKED from completion** until:
- All operation names used in Sections 2-4 appear in the audit table
- Zero UNDECLARED entries remain without explicit flagging
- Generic verb scan returns clean

**Section 5 SEALED. Trace complete.**
