# Flow-Resilience Skill — Round 5 Variations (Rubric v5)

**Skill**: flow-resilience — Simulate degraded conditions: offline, partial failure, eventual consistency.
**Rubric**: v5 (C-01 through C-21, essential/recommended/aspirational tiers)
**Date**: 2026-03-15

---

## Round 5 Context

**New criteria entering R5**: C-19, C-20, and C-21 are freshly extracted from R4 excellence
signals.

**R4 diagnosis**:
- V-03 (R4) earned C-18 by requiring named entry/exit conditions on each gate. Its gate
  templates included `Reason if OPEN: [which condition is not met]` — a category description.
  C-19 tightens this: the reason field must name the *specific* blocking item (the unresolved
  entry ID, the unmet class minimum, the pending verdict, the outstanding amendment). A field
  that says "coverage minimum not met" without identifying which class and how many entries are
  present does not satisfy C-19. A bare `GATE N: OPEN` with no reason is an error, not a valid
  in-progress state.
- V-03 (R4) introduced the `GATE 3b: AMENDED` pattern for CR-triggered DCV additions, but the
  amendment only wrote the new DCV entry — it did not cite the downstream CR finding by ID,
  and it did not require an explicit no-amendment confirmation when no inadequate verdicts were
  found. C-20 formalizes this: the amendment record must name the downstream finding that
  triggered the re-open; the sub-gate re-close is mandatory; and when no amendments are needed,
  an explicit confirmation is required so "no amendments" and "amendments not checked" are
  distinguishable.
- V-05 (R4) enumerated all six named commerce operations (checkout, inventory reservation,
  payment processing, cart state, order fulfillment, loyalty redemption) inside the Gate 2
  Capability field template — but this was an implicit list embedded in the analysis phase.
  C-21 requires the commitment to precede the analysis: a named scope list declared before Gate 1
  (or Phase 1) that is explicitly cross-checked against the final scenario table. Operations
  discovered within scenario bodies only — not declared upfront — do not satisfy C-21.

**R5 synthesis path**: The three new criteria continue the formalization layer:

- C-19: Gate state specificity — OPEN gates must declare exactly what is blocking them, not
  a category. The gap between "coverage minimum not met" and "Partial-Failure class has 1 Include
  entry; minimum is 2" is the difference between a state label and an actionable blocking condition.
- C-20: Amendment traceability — every downstream finding that reopens a prior gate must be cited
  by ID in the amendment record. A `GATE 3b: AMENDED` with no citation is unverifiable; the
  reader cannot confirm which CR finding triggered the amendment without re-reading Gate 4.
- C-21: Scope-before-analysis — the commerce operation commitment must precede the analysis, not
  emerge from it. A scope list extracted post-hoc from the scenario table does not satisfy C-21;
  only an upfront declaration does.

**Axes selected**:

- V-01: Single-axis — Pre-Analysis Commerce Operation Scope Declaration (C-21)
- V-02: Single-axis — Gate Blockage Transparency with specific Reason-if-OPEN (C-19)
- V-03: Single-axis — Downstream Gate Amendment with Re-Close Record (C-20)
- V-04: Combination — Commerce Scope Declaration + Gate Blockage Transparency (C-21 + C-19)
- V-05: Combination — All three new axes + full R4 formalization (C-19 + C-20 + C-21 + C-15 through C-18)

---

## V-01 — Pre-Analysis Commerce Operation Scope Declaration

**Variation axis**: Pre-analysis commerce operation scope declaration
**Hypothesis**: The gap between C-05 (scenarios anchored to named operations) and C-21 (scope
declared before analysis) is the difference between discovering what you covered and committing
to what you will cover. V-05 (R4) passed C-05 by naming all six operations inside the Capability
template — but that list was embedded in an analysis phase, not declared before it. When the
scope declaration precedes Phase 1, the reader can verify coverage without reading the scenario
bodies, and gaps are distinguishable from intentional exclusions. The upfront list creates a
checkable commitment: each declared operation either receives scenario coverage or is explicitly
recorded as a gap.

---

You are a Commerce / distributed systems domain expert. Your task is to simulate how a
commerce system behaves under degraded conditions and produce a signal artifact for
decision-making.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### Commerce Operation Scope Declaration

Before any analysis begins, declare which commerce operations this resilience analysis covers.
This list is a commitment, not a summary — it must be written before Phase 1 starts.

Declare at least four operations from the standard commerce set. For each operation, assign
one of two scope designations:

| Designation | Meaning |
|-------------|---------|
| `In-scope` | This operation will be covered by at least one scenario in Phase 2. Any In-scope operation that receives no scenario coverage is a named gap. |
| `Excluded` | This operation is not covered in this analysis. A brief rationale is required. Excluded operations are not coverage gaps — they are intentional omissions. |

Standard commerce operations (name at least four):
- Checkout
- Inventory reservation
- Payment processing
- Cart state
- Order fulfillment
- Loyalty redemption

Format:

```
Operation: [name]
Scope: [In-scope | Excluded]
Rationale if Excluded: [one sentence — why this operation is outside the analysis boundary]
```

After all operations are declared:

```
SCOPE DECLARATION COMPLETE
In-scope operations: [list]
Excluded operations: [list, or "none"]
```

Do not begin Phase 1 until the scope declaration is complete.

---

### Phase 1 — Discovery Triage

Enumerate every failure mode that could plausibly apply to the architecture implied by the
topic. For every entry, assign exactly one disposition:

| Disposition | Meaning |
|-------------|---------|
| `Include` | Mechanism understood; commerce impact clear for at least one In-scope operation. Enters Phase 2. |
| `BARRED` | Plausible but cannot be confirmed without architecture detail not present in the topic signal. Excluded from Phase 2; confidence basis must be named. |
| `Argued-Impossible` | Foreclosed by a specific DS primitive — named CAP guarantee, synchronous consistency property, or named topology constraint. Description absence ("the topic doesn't mention X") is not a valid basis. Retained with rationale. |

"Flagged", "Uncertain", and similar free-text qualifiers are not dispositions. An entry
without a named disposition is excluded.

Entry format:

```
Entry: [name]
Class: [Offline / Partial-Failure / Eventual-Consistency]
Disposition: [Include | BARRED | Argued-Impossible]
Basis: [one sentence]
```

When all entries are assigned:

```
TRIAGE GATE: [OPEN | CLOSED]
Minimum coverage check: Offline=[N Include] / Partial-Failure=[N Include] / Eventual-Consistency=[N Include]
```

The gate is `CLOSED` only when every entry has a named disposition, every `BARRED` entry has
a stated basis, and each degradation class has at least two `Include` entries. A gate with
no explicit `CLOSED` declaration is `OPEN` by definition. Do not proceed to Phase 2 until
the Triage Gate is `CLOSED`.

---

### Phase 2 — Scenario Analysis

For every `Include` entry from Phase 1, produce the four mandatory fields.

**[Entry ID — Scenario Name]**

- **State**: Precise failure description. Name which services, replicas, or network segments
  are affected and how. "System is degraded" is not acceptable.
- **Capability**: For each In-scope operation declared above, state whether it is:
  `available` / `degraded` (slower or unreliable) / `blocked`. Do not omit declared In-scope
  operations from this field.
- **Data at risk**: Named data object, failure mode (lost / stale / inconsistent / duplicated),
  and scope (per-user / per-session / global).
- **Recovery path**: Ordered steps with actor prefix — `[client]` / `[server]` / `[operator]` /
  `[user]`. Each step names its trigger condition and observable success signal.

Minimum: at least six scenarios total, at least two per degradation class.

---

### Phase 3 — Gap Identification

Produce three labeled sections. Each finding references a named scenario or data object from
Phase 2. If a section has no findings, write an explicit nil statement with scope rationale
(not a bare "none found").

**Offline Experience Gaps** — `OEG-NN: [scenario name] — [what the user encounters that the design does not handle]`

If none: `OEG-NIL: No offline experience gaps identified — [scope rationale explaining why this gap type does not apply for this deployment pattern].`

**Data Consistency Violations** — `DCV-NN: [data object] — [missing invariant or undetected divergence]`

If none: `DCV-NIL: No data consistency violations identified — [scope rationale].`

**Missing Recovery Flows** — `MRF-NN: [scenario name] — [the recovery actor with no defined action]`

If none: `MRF-NIL: No missing recovery flows identified — [scope rationale].`

---

### Phase 4 — Conflict Resolution Adequacy

For each Eventual-Consistency scenario from Phase 2:

```
Scenario: [name]
Strategy: [last-write-wins | merge | manual-reconcile | reject-stale | undefined]
Data type: [specific data object in conflict]
Adequate: [yes | no]
Rationale: [one sentence]
```

If verdict is `no` or strategy is `undefined`: append `DCV-CR-NN` to Phase 3 Data Consistency
Violations list.

---

### Scope Verification

Cross-check every `In-scope` operation from the Commerce Operation Scope Declaration against
the Phase 2 scenario table.

```
Operation: [name]
Coverage: [covered — scenario IDs] | [gap — no scenario covers this operation]
```

If any In-scope operation has no scenario coverage, record it:

```
Coverage Gap: SCOV-NN
Operation: [name]
Gap: Declared In-scope but received no scenario coverage in Phase 2.
```

If all In-scope operations have coverage: `SCOV-NIL: All declared In-scope operations
receive scenario coverage in Phase 2.`

**Output artifact**: `simulations/flow/resilience/{{topic}}-resilience-{{date}}.md`

---

## V-02 — Gate Blockage Transparency (Reason-if-OPEN)

**Variation axis**: Gate blockage transparency with specific blocking condition
**Hypothesis**: R4 V-03 introduced `Reason if OPEN: [which condition is not met]` — but this
field accepts a category description ("minimum not met") rather than a specific blocking item.
C-19 requires the reason to name exactly what is blocking the gate: the specific entry ID with
unresolved basis, the degradation class with insufficient Include entries and the current count,
the pending adequacy verdict by scenario name, or the outstanding amendment by finding ID. The
difference matters for resumability: "minimum not met" requires re-reading all prior entries to
find the gap; "Partial-Failure class has 1 Include entry; 2 required; add 1 more to close" is
immediately actionable. A gate displaying only `OPEN` with no reason is treated as an error —
indistinguishable from an abandoned gate.

---

You are a Commerce / distributed systems domain expert. Simulate how the commerce system
described by the topic behaves under degraded conditions.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### Gate 1 — Failure Mode Discovery

**Entry condition**: None. Gate 1 is the analysis entry point.
**Exit condition**: Every failure mode entry carries one of three named dispositions
(`Include` / `BARRED` / `Argued-Impossible`) with a stated basis; no entry uses a free-text
qualifier; each degradation class has at least two `Include` entries. Write `GATE 1: CLOSED`
only when all three conditions are satisfied.

Enumerate failure modes for the architecture implied by the topic. For each:

```
Entry: [name]
Class: [Offline / Partial-Failure / Eventual-Consistency]
Disposition: [Include | BARRED | Argued-Impossible]
Basis: [one sentence — architecture reason or confidence gap]
```

"Flagged" is not a disposition. A gate with no explicit `CLOSED` declaration is `OPEN` by
definition.

After all entries are assigned:

```
GATE 1 STATUS: [OPEN | CLOSED]
Include entries by class: Offline=[N] / Partial-Failure=[N] / Eventual-Consistency=[N]
BARRED entries: [list names, or "none"]
Argued-Impossible entries: [list names, or "none"]
Reason if OPEN: [name the specific blocking item — e.g., "Entry 'Inventory cache split-brain'
  has no confidence basis stated" or "Partial-Failure class has 1 Include entry; 2 required;
  add 1 more before closing" or "Entry 'Loyalty sync delay' disposition is 'Uncertain' which
  is not a named disposition; reclassify to Include / BARRED / Argued-Impossible"]
```

A bare `GATE 1: OPEN` with no `Reason if OPEN` is an error, not a valid in-progress state.
If `GATE 1: OPEN`, resolve the stated blocking condition before continuing.
If `GATE 1: CLOSED`, proceed to Gate 2.

---

### Gate 2 — Scenario Analysis

**Entry condition**: Gate 1 `CLOSED`.
**Exit condition**: Every `Include` entry from Gate 1 has a complete four-field analysis
(State / Capability / Data at risk / Recovery path). Minimum: six scenarios total, two per
class. All recovery paths include at least one actor-prefixed step. Write `GATE 2: CLOSED`
when all conditions are met.

For each `Include` entry from Gate 1:

**[Entry ID — Name]**

- **State**: Precise failure description — named services, replicas, network segments, failure mode
- **Capability**: Available / degraded / blocked operations — named per commerce flow
  (checkout, inventory reservation, payment processing, cart state, order fulfillment)
- **Data at risk**: Named object, failure mode (lost / stale / inconsistent / duplicated), scope
- **Recovery path**: Actor-prefixed steps — `[client]` / `[server]` / `[operator]` / `[user]`;
  each step includes trigger condition and observable success signal

After all scenarios:

```
GATE 2 STATUS: [OPEN | CLOSED]
Scenario count by class: Offline=[N] / Partial-Failure=[N] / Eventual-Consistency=[N]
Reason if OPEN: [name the specific blocking item — e.g., "Entry S-04 (Payment service timeout)
  is missing the Data at risk field" or "Eventual-Consistency class has 1 scenario; 2 required;
  add 1 more before closing" or "Recovery path for S-02 has no actor-prefixed steps"]
```

A bare `GATE 2: OPEN` with no `Reason if OPEN` is an error. If `GATE 2: OPEN`, resolve the
stated blocking condition before continuing. If `GATE 2: CLOSED`, proceed to Gate 3.

---

### Gate 3 — Gap Identification

**Entry condition**: Gate 2 `CLOSED`.
**Exit condition**: All three gap sections are present and labeled; sections with no findings
carry a nil statement with scope rationale; all findings reference named scenarios or data
objects from Gate 2. Write `GATE 3: CLOSED` when all conditions are met.

**Offline Experience Gaps**

`OEG-NN: [scenario name] — [unhandled user encounter during offline failure]`

If none: `OEG-NIL: No offline experience gaps identified — [scope rationale explaining why this gap type does not apply for this deployment pattern].`

**Data Consistency Violations**

`DCV-NN: [data object] — [missing invariant or undetected divergence]`

If none: `DCV-NIL: No data consistency violations identified — [scope rationale].`

**Missing Recovery Flows**

`MRF-NN: [scenario name] — [recovery actor with no defined action]`

If none: `MRF-NIL: No missing recovery flows identified — [scope rationale].`

After all gap sections:

```
GATE 3 STATUS: [OPEN | CLOSED]
OEG section: [present | nil-stated]
DCV section: [present | nil-stated]
MRF section: [present | nil-stated]
Reason if OPEN: [name the specific blocking item — e.g., "DCV section is absent (not nil-stated,
  absent)" or "OEG-01 references 'scenario 3' which has no ID in Gate 2; clarify reference before
  closing" or "MRF section is present but MRF-02 has no named recovery actor"]
```

A bare `GATE 3: OPEN` with no `Reason if OPEN` is an error. If `GATE 3: OPEN`, resolve the
stated blocking condition before continuing. If `GATE 3: CLOSED`, proceed to Gate 4.

---

### Gate 4 — Conflict Resolution Adequacy

**Entry condition**: Gate 3 `CLOSED`.
**Exit condition**: Every Eventual-Consistency scenario from Gate 2 has a conflict-resolution
entry with a named strategy and adequacy verdict. Every `inadequate` or `undefined` verdict
has generated a DCV-CR entry in Gate 3 (amendments accepted). Write `GATE 4: CLOSED` when
all conditions are met.

For each Eventual-Consistency scenario:

```
Scenario: [name]
Conflict strategy: [last-write-wins | merge | manual-reconcile | reject-stale | undefined]
Data type: [object in conflict]
Adequacy verdict: [adequate | inadequate]
Rationale: [one sentence]
```

If verdict is `inadequate` or strategy is `undefined`: add `DCV-CR-NN` to Gate 3 DCV list.
Write `GATE 3 AMENDMENT: DCV-CR-NN added` and `GATE 3 REMAINS CLOSED` (amendment does not
reopen).

After all CR entries:

```
GATE 4 STATUS: [OPEN | CLOSED]
DCV amendments from CR: [list DCV-CR-NN entries added, or "none"]
Reason if OPEN: [name the specific blocking item — e.g., "Scenario EC-02 (Cart sync divergence)
  has no conflict strategy assigned; assign last-write-wins / merge / manual-reconcile /
  reject-stale / undefined before closing" or "EC-03 adequacy verdict is 'maybe' which is
  not a named verdict; reclassify to adequate / inadequate"]
```

A bare `GATE 4: OPEN` with no `Reason if OPEN` is an error.

**Output artifact**: `simulations/flow/resilience/{{topic}}-resilience-{{date}}.md`

---

## V-03 — Downstream Gate Amendment with Re-Close Record

**Variation axis**: Downstream gate amendment with labeled re-open and re-close record
**Hypothesis**: When conflict-resolution analysis finds an inadequate or undefined strategy,
the resulting DCV entry must amend an already-CLOSED gate. R4 V-03 introduced `GATE 3b: AMENDED`
for this case — but the amendment record did not cite the downstream CR finding by ID, and
the protocol did not require an explicit no-amendment confirmation when all verdicts were
adequate. Without the citation, the reader cannot verify which CR finding triggered the
amendment without re-reading Gate 4. Without the no-amendment confirmation, "no amendments
needed" is indistinguishable from "amendment check skipped." C-20 requires: the re-open
record names the triggering finding by ID; the amendment sub-gate is labeled; the re-close
is explicit; and when no amendments are needed, a confirmation is present.

---

You are a Commerce / distributed systems domain expert. Simulate how the commerce system
described by the topic behaves under degraded conditions.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### Gate 1 — Failure Mode Discovery

**Entry condition**: None. Gate 1 is the analysis entry point.
**Exit condition**: Every failure mode entry carries one of three named dispositions
(`Include` / `BARRED` / `Argued-Impossible`) with a stated basis; each degradation class
has at least two `Include` entries. Write `GATE 1: CLOSED` only when satisfied.

Enumerate failure modes for the architecture implied by the topic. For each:

```
Entry: [name]
Class: [Offline / Partial-Failure / Eventual-Consistency]
Disposition: [Include | BARRED | Argued-Impossible]
Basis: [one sentence — architecture reason or confidence gap]
```

"Flagged" is not a disposition. A gate with no explicit `CLOSED` declaration is `OPEN`.

```
GATE 1 STATUS: [OPEN | CLOSED]
Include entries by class: Offline=[N] / Partial-Failure=[N] / Eventual-Consistency=[N]
Reason if OPEN: [which condition is not met]
```

If `GATE 1: OPEN`, resolve before continuing. If `GATE 1: CLOSED`, proceed to Gate 2.

---

### Gate 2 — Scenario Analysis

**Entry condition**: Gate 1 `CLOSED`.
**Exit condition**: Every `Include` entry has a complete four-field analysis. Minimum: six
scenarios total, two per class. All recovery paths include at least one actor-prefixed step.
Write `GATE 2: CLOSED` when all conditions are met.

For each `Include` entry:

**[Entry ID — Name]**

- **State**: Precise failure description — named services, replicas, segments, failure mode
- **Capability**: Available / degraded / blocked — named per commerce operation
- **Data at risk**: Named object, failure mode (lost / stale / inconsistent / duplicated), scope
- **Recovery path**: Actor-prefixed ordered steps — `[client]` / `[server]` / `[operator]` /
  `[user]`; each step includes trigger condition and observable success signal

```
GATE 2 STATUS: [OPEN | CLOSED]
Scenario count: Offline=[N] / Partial-Failure=[N] / Eventual-Consistency=[N]
Reason if OPEN: [which condition is not met]
```

If `GATE 2: OPEN`, resolve before continuing. If `GATE 2: CLOSED`, proceed to Gate 3.

---

### Gate 3 — Gap Identification

**Entry condition**: Gate 2 `CLOSED`.
**Exit condition**: All three gap sections present and labeled; sections with no findings carry
a nil statement with scope rationale; all findings reference named scenarios or data objects
from Gate 2. Write `GATE 3: CLOSED` when all conditions are met.

**Offline Experience Gaps**

`OEG-NN: [scenario name] — [unhandled user encounter]`
Nil: `OEG-NIL: No offline experience gaps identified — [scope rationale].`

**Data Consistency Violations**

`DCV-NN: [data object] — [missing invariant or undetected divergence]`
Nil: `DCV-NIL: No data consistency violations identified — [scope rationale].`

**Missing Recovery Flows**

`MRF-NN: [scenario name] — [recovery actor with no defined action]`
Nil: `MRF-NIL: No missing recovery flows identified — [scope rationale].`

```
GATE 3 STATUS: [OPEN | CLOSED]
OEG section: [present | nil-stated]
DCV section: [present | nil-stated]
MRF section: [present | nil-stated]
Reason if OPEN: [which condition is not met]
```

If `GATE 3: OPEN`, resolve before continuing. If `GATE 3: CLOSED`, proceed to Gate 4.

Note: Gate 3 may be reopened by Gate 4 if conflict-resolution analysis produces DCV
amendments. Reopening does not invalidate the original GATE 3: CLOSED — it creates a
labeled amendment sub-gate. See the Gate 4 amendment protocol below.

---

### Gate 4 — Conflict Resolution Adequacy

**Entry condition**: Gate 3 `CLOSED`.
**Exit condition**: Every Eventual-Consistency scenario from Gate 2 has a conflict-resolution
entry with a named strategy, adequacy verdict, and rationale. Every `inadequate` or `undefined`
verdict has triggered the Gate 3 Amendment Protocol (below). When all verdicts are `adequate`,
the No-Amendment Confirmation is written. Write `GATE 4: CLOSED` when all conditions are met.

For each Eventual-Consistency scenario:

```
CR-NN: [scenario name]
Strategy: [last-write-wins | merge | manual-reconcile | reject-stale | undefined]
Data type: [object in conflict]
Adequacy verdict: [adequate | inadequate]
Rationale: [one sentence — why this strategy does or does not preserve invariants for this data type]
```

---

#### Gate 3 Amendment Protocol

Apply this protocol for every CR entry where verdict is `inadequate` or strategy is `undefined`.

**Step 1 — Declare re-open**:
```
GATE 3: REOPENED
Triggering finding: CR-NN — [brief description of the inadequate/undefined verdict]
Amendment to apply: DCV-CR-NN — [data object] — [inadequate/undefined strategy + consequence]
```

**Step 2 — Apply amendment** (write the new DCV entry):
```
DCV-CR-NN: [data object] — [missing invariant created by inadequate/undefined conflict strategy]
Triggered by: CR-NN
```

**Step 3 — Re-close under labeled sub-gate**:
```
GATE 3a: AMENDED — triggered by CR-NN
Status: CLOSED
Amendment applied: DCV-CR-NN added to Data Consistency Violations section
```

If there are multiple CR-triggered amendments, use sequential sub-gates:
`GATE 3a`, `GATE 3b`, `GATE 3c`, etc. Each sub-gate names its triggering CR finding.

**No-Amendment Confirmation** (write this when all CR verdicts are `adequate` and no strategy
is `undefined`):
```
GATE 4 AMENDMENT REVIEW: No inadequate or undefined CR verdicts.
GATE 3 ORIGINAL CLOSURE CONFIRMED — no amendments required.
```

This confirmation is mandatory. Its absence means the amendment check was skipped.

---

After all CR entries and amendment protocol steps:

```
GATE 4 STATUS: [OPEN | CLOSED]
CR entries assessed: [count]
Gate 3 amendments: [list sub-gate labels and their triggering CR-NN IDs, or "none — see No-Amendment Confirmation"]
Reason if OPEN: [which condition is not met]
```

**Output artifact**: `simulations/flow/resilience/{{topic}}-resilience-{{date}}.md`

---

## V-04 — Combination: Commerce Scope Declaration + Gate Blockage Transparency

**Variation axes**: Pre-analysis commerce operation scope declaration (C-21) + Gate blockage
transparency with specific Reason-if-OPEN (C-19)
**Hypothesis**: C-21 and C-19 operate at different points in the analysis lifecycle but share
a common mechanism: they both require a specific commitment that is checkable without re-reading
prose. The scope declaration (C-21) commits to which operations will be covered; the Reason-if-OPEN
field (C-19) commits to which specific item is blocking a gate. Together they create two
independent audit points: one at the analysis entry (what will be covered) and one at every
gate transition (what specifically is preventing closure). The combination prevents two
otherwise independent failure modes: a scope list that emerges from the analysis instead of
precedes it, and gate OPEN states that don't communicate the specific blocker.

---

You are a Commerce / distributed systems domain expert. Simulate degraded conditions for the
commerce system described by the topic and produce a resilience signal artifact.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### Commerce Operation Scope Declaration

Declare the in-scope commerce operations before any analysis begins. This is a commitment,
not a discovery — it must precede Gate 1.

Choose at least four operations from the standard set:
checkout / inventory reservation / payment processing / cart state / order fulfillment / loyalty redemption

For each operation:

```
Operation: [name]
Scope: [In-scope | Excluded]
Rationale if Excluded: [one sentence]
```

After all operations are declared:

```
SCOPE DECLARATION COMPLETE
In-scope operations: [list — at least four]
Excluded operations: [list, or "none"]
```

Each `In-scope` operation must appear in the Capability field of at least one Phase 2 scenario.
Any `In-scope` operation that receives no scenario coverage is a named gap in the Scope
Verification section at the end. Do not begin Gate 1 until this declaration is complete.

---

### Gate 1 — Failure Mode Discovery

**Entry condition**: Commerce Operation Scope Declaration complete.
**Exit condition**: Every failure mode entry carries one of three named dispositions
(`Include` / `BARRED` / `Argued-Impossible`) with a stated basis; each degradation class has
at least two `Include` entries. Write `GATE 1: CLOSED` only when all conditions are satisfied.

For each failure mode:

```
Entry: [name]
Class: [Offline / Partial-Failure / Eventual-Consistency]
Disposition: [Include | BARRED | Argued-Impossible]
Basis: [one sentence]
```

"Flagged" is not a disposition.

```
GATE 1 STATUS: [OPEN | CLOSED]
Include entries by class: Offline=[N] / Partial-Failure=[N] / Eventual-Consistency=[N]
BARRED entries: [list names, or "none"]
Argued-Impossible entries: [list names, or "none"]
Reason if OPEN: [name the specific blocking item — entry ID with unresolved basis, class name
  with current Include count and required count, or entry with invalid disposition label]
```

A bare `GATE 1: OPEN` with no `Reason if OPEN` is an error. Resolve the stated blocking
condition before continuing. If `GATE 1: CLOSED`, proceed to Gate 2.

---

### Gate 2 — Scenario Analysis

**Entry condition**: Gate 1 `CLOSED`.
**Exit condition**: Every `Include` entry from Gate 1 has a complete four-field analysis.
Minimum: six scenarios total, two per class. Write `GATE 2: CLOSED` when all conditions are met.

For each `Include` entry:

**[Entry ID — Name]**

- **State**: Precise failure description — named services, replicas, segments, failure mode
- **Capability**: For each In-scope operation from the Scope Declaration, state whether it is
  `available` / `degraded` / `blocked`. Do not omit declared In-scope operations.
- **Data at risk**: Named object, failure mode (lost / stale / inconsistent / duplicated), scope
- **Recovery path**: Actor-prefixed ordered steps — `[client]` / `[server]` / `[operator]` /
  `[user]`; each step includes trigger condition and observable success signal

```
GATE 2 STATUS: [OPEN | CLOSED]
Scenario count by class: Offline=[N] / Partial-Failure=[N] / Eventual-Consistency=[N]
Reason if OPEN: [name the specific blocking item — scenario ID missing a required field,
  class name with current count and required count, or scenario with malformed recovery path]
```

A bare `GATE 2: OPEN` with no `Reason if OPEN` is an error. If `GATE 2: CLOSED`, proceed.

---

### Gate 3 — Gap Identification

**Entry condition**: Gate 2 `CLOSED`.
**Exit condition**: All three gap sections present and labeled; nil findings carry scope
rationale; all findings reference named Gate 2 scenarios or data objects. Write `GATE 3: CLOSED`
when all conditions are met.

**Offline Experience Gaps**

`OEG-NN: [scenario name] — [unhandled user encounter]`
Nil: `OEG-NIL: No offline experience gaps identified — [scope rationale].`

**Data Consistency Violations**

`DCV-NN: [data object] — [missing invariant]`
Nil: `DCV-NIL: No data consistency violations identified — [scope rationale].`

**Missing Recovery Flows**

`MRF-NN: [scenario name] — [actor with no defined action]`
Nil: `MRF-NIL: No missing recovery flows identified — [scope rationale].`

```
GATE 3 STATUS: [OPEN | CLOSED]
OEG section: [present | nil-stated]
DCV section: [present | nil-stated]
MRF section: [present | nil-stated]
Reason if OPEN: [name the specific blocking item — absent section name, finding with
  missing scenario reference, or nil statement without scope rationale]
```

A bare `GATE 3: OPEN` with no `Reason if OPEN` is an error. If `GATE 3: CLOSED`, proceed.

---

### Gate 4 — Conflict Resolution Adequacy

**Entry condition**: Gate 3 `CLOSED`.
**Exit condition**: Every Eventual-Consistency scenario from Gate 2 has a conflict-resolution
entry with a named strategy and adequacy verdict. Every `inadequate` or `undefined` verdict has
generated a DCV-CR-NN entry appended to Gate 3. Write `GATE 4: CLOSED` when complete.

For each Eventual-Consistency scenario:

```
Scenario: [name]
Strategy: [last-write-wins | merge | manual-reconcile | reject-stale | undefined]
Data type: [object in conflict]
Adequacy verdict: [adequate | inadequate]
Rationale: [one sentence]
```

If verdict is `inadequate` or strategy is `undefined`: write `DCV-CR-NN` and append to Gate 3
DCV list. Write `GATE 3 AMENDMENT: DCV-CR-NN added` and `GATE 3 REMAINS CLOSED`.

```
GATE 4 STATUS: [OPEN | CLOSED]
DCV amendments from CR: [list DCV-CR-NN entries, or "none"]
Reason if OPEN: [name the specific blocking item — scenario ID missing a CR entry, CR entry
  with invalid adequacy label, or pending amendment not yet applied]
```

A bare `GATE 4: OPEN` with no `Reason if OPEN` is an error.

---

### Scope Verification

Cross-check each `In-scope` operation from the Scope Declaration against the Gate 2 scenario table.

```
Operation: [name]
Coverage: [covered — scenario IDs that reference this operation] | [gap — no scenario references this operation]
```

If any In-scope operation has no coverage: `SCOV-NN: [operation] — declared In-scope but
received no scenario coverage; this is a coverage gap, not a scope exclusion.`

If all In-scope operations have coverage: `SCOV-NIL: All declared In-scope operations
receive scenario coverage in Gate 2.`

**Output artifact**: `simulations/flow/resilience/{{topic}}-resilience-{{date}}.md`

---

## V-05 — Combination: Full R5 Formalization (C-15 through C-21)

**Variation axes**: All three new R5 axes (C-19 + C-20 + C-21) layered onto the full R4
formalization (C-15 + C-16 + C-17 + C-18)
**Hypothesis**: The seven criteria from R3/R4 establish a traceable analysis structure: named
dispositions (C-16), barred-entry lifecycle (C-17), formal gate sequencing (C-18), DS-primitive
impossibility arguments (C-15), conflict-resolution-to-DCV linkage (C-14), nil-finding norm
(C-12), and coverage accountability (C-13). The three new R5 criteria extend this traceability
to three previously open edges: the scope commitment that precedes the analysis (C-21), the
specific blocking condition that explains every OPEN gate (C-19), and the sub-gate amendment
record that ties every downstream finding to the gate it reopened (C-20). Together the seven
prior and three new mechanisms close all major audit gaps: every entry is traceable from scope
declaration through discovery to output artifact; every gate state is either CLOSED with a
record or OPEN with a specific reason; and every downstream finding that amends a prior gate
is cited by ID in the amendment sub-gate.

---

You are a Commerce / distributed systems domain expert. Produce a resilience signal artifact
for the commerce system described by the topic.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### Commerce Operation Scope Declaration

Before any gate opens, declare the commerce operations this analysis covers. This is a
pre-analysis commitment — not a summary derived from the scenario table.

Declare at least four operations from the standard set:
checkout / inventory reservation / payment processing / cart state / order fulfillment / loyalty redemption

```
Operation: [name]
Scope: [In-scope | Excluded]
Rationale if Excluded: [one sentence]
```

After all operations are declared:

```
SCOPE DECLARATION COMPLETE
In-scope operations: [list — minimum four]
Excluded operations: [list, or "none"]
```

Each `In-scope` operation will be assessed for coverage in the Scope Verification section
(after Gate 4). Any `In-scope` operation that receives no scenario coverage is a named
coverage gap. Do not open Gate 1 until the Scope Declaration is complete.

---

### Gate 1 — Triage Discovery

**Entry condition**: Scope Declaration complete.

**Exit condition**: (a) every enumerated failure mode carries one of three named dispositions
(`Include` / `BARRED` / `Argued-Impossible`) with a stated basis; (b) no entry uses a
free-text qualifier; (c) each degradation class has at least two entries with disposition
`Include`. Write `GATE 1: CLOSED` only when all three conditions are satisfied.

Enumerate failure modes for the architecture implied by the topic.

**Disposition table** (three labels, no others):

| Disposition | Criteria | Effect |
|-------------|----------|--------|
| `Include` | High or Medium confidence; mechanism understood; commerce impact clear | Enters Gate 2 scenario table |
| `BARRED` | Low confidence; mechanism or commerce impact unclear without context not in the signal | Excluded from Gate 2; tracked in Gate 1b; must resolve to Include or become Coverage Gap |
| `Argued-Impossible` | Foreclosed by a specific named DS primitive; architecture argument required — description absence is invalid | Excluded; retained in Gate 1c with DS Primitive cited field |

"Flagged" is not a disposition. A gate with no explicit `CLOSED` declaration is `OPEN`.

Entry format:

```
Entry: [name]
Class: [Offline / Partial-Failure / Eventual-Consistency]
Disposition: [Include | BARRED | Argued-Impossible]
Basis: [one sentence — architecture reason or confidence gap]
```

After all entries:

```
GATE 1 STATUS: [OPEN | CLOSED]
Include entries by class: Offline=[N] / Partial-Failure=[N] / Eventual-Consistency=[N]
BARRED entries: [list names, or "none"]
Argued-Impossible entries: [list names, or "none"]
Reason if OPEN: [name the specific blocking item — e.g., "Entry 'Payment idempotency failure'
  has no basis stated" or "Partial-Failure class has 1 Include entry; 2 required; add 1 more"
  or "Entry 'Inventory staleness' disposition reads 'Uncertain' — not a named disposition;
  reclassify before closing"]
```

A bare `GATE 1: OPEN` with no `Reason if OPEN` is an error, not a valid in-progress state.
If `GATE 1: OPEN`, resolve the stated blocking condition before continuing.
If `GATE 1: CLOSED`, open Gates 1b and 1c in parallel.

---

### Gate 1b — BARRED Register

**Entry condition**: Gate 1 `CLOSED`.
**Exit condition**: Every BARRED entry from Gate 1 has a named confidence basis and a
resolution attempt. Entries that resolve become `Include` (added to Gate 2). Entries that
do not resolve are marked `Permanently BARRED`. Write `GATE 1b: CLOSED` when all BARRED
entries have a resolution verdict.

For each BARRED entry:

```
Entry: [name]
Confidence basis from Gate 1: [restate]
Resolution attempt: [what in the topic signal could resolve this, and whether it does]
Outcome: [Include (reclassified) | Permanently BARRED]
If reclassified: add to Gate 2 with note "[reclassified from BARRED — basis resolved: ...]"
If Permanently BARRED: this entry will appear in Coverage Gap Registry (Gate 3b).
```

```
GATE 1b STATUS: [OPEN | CLOSED]
Reclassified to Include: [list, or "none"]
Permanently BARRED: [list, or "none"]
Reason if OPEN: [name the specific blocking item — entry ID with no resolution verdict,
  or reclassified entry not yet added to Gate 2]
```

A bare `GATE 1b: OPEN` with no `Reason if OPEN` is an error. If `GATE 1b: CLOSED`, hold
for Gate 1c before opening Gate 2.

---

### Gate 1c — Impossibility Register

**Entry condition**: Gate 1 `CLOSED`.
**Exit condition**: Every `Argued-Impossible` entry has a `DS Primitive cited:` field with
an architecture argument and inline VALID/INVALID examples. Write `GATE 1c: CLOSED` when all
entries are documented.

For each `Argued-Impossible` entry:

```
Entry: [name]
DS Primitive cited: [exact name — e.g., "CAP theorem AP branch", "two-phase locking
  serializability guarantee", "synchronous replication linearizability guarantee under
  acknowledged writes"]
Architecture argument: [one sentence — what the architecture makes impossible]
VALID impossibility argument: [example of a valid architecture-based argument — cites the
  primitive, addresses the architecture, not the description]
INVALID impossibility argument: [example that would fail — e.g., "The topic doesn't mention
  distributed caching, so cache invalidation staleness cannot apply here."]
```

Note: "The topic doesn't mention X" is never a valid impossibility argument. The argument must
address why the architecture forecloses the failure class, not why the description omits it.

```
GATE 1c STATUS: [OPEN | CLOSED]
Argued-Impossible entries documented: [count]
Reason if OPEN: [name the specific blocking item — entry ID missing DS Primitive cited field,
  or entry with VALID/INVALID examples absent]
```

A bare `GATE 1c: OPEN` with no `Reason if OPEN` is an error.
Gates 1b and 1c may run in parallel. Both must be `CLOSED` before Gate 2 opens.

---

### Gate 2 — Scenario Analysis

**Entry condition**: Gate 1 `CLOSED` AND Gate 1b `CLOSED` AND Gate 1c `CLOSED`.

**Exit condition**: Every `Include` entry (from Gate 1 and any reclassified from Gate 1b) has
a complete four-field analysis. Minimum: six scenarios total, two per class. All recovery paths
include at least one actor-prefixed step with trigger condition. Write `GATE 2: CLOSED` when
all conditions are met.

For each `Include` entry:

**[Entry ID — Name]** `[Class]`

- **State**: Named services / replicas / segments + precise failure mode
- **Capability**: For each `In-scope` operation from the Scope Declaration, state whether it is
  `available` / `degraded` / `blocked`. Do not omit declared In-scope operations.
- **Data at risk**: Named data object, failure mode (lost / stale / inconsistent / duplicated), scope
- **Recovery path**: Actor-prefixed ordered steps — `[client]` / `[server]` / `[operator]` /
  `[user]`; each step includes trigger condition and observable success signal

```
GATE 2 STATUS: [OPEN | CLOSED]
Scenario count: Offline=[N] / Partial-Failure=[N] / Eventual-Consistency=[N]
Reason if OPEN: [name the specific blocking item — scenario ID missing a required field,
  class name with current count and required count, or scenario with no actor-prefixed
  recovery step]
```

A bare `GATE 2: OPEN` with no `Reason if OPEN` is an error.
If `GATE 2: CLOSED`, proceed to Gate 3.

---

### Gate 3 — Gap Identification

**Entry condition**: Gate 2 `CLOSED`.

**Exit condition**: All three gap sections present and labeled; sections with no findings carry
a nil statement with scope rationale; all findings reference named scenarios or data objects
from Gate 2. Write `GATE 3: CLOSED` when all conditions are met.

Note: Gate 3 may be amended by Gate 4 (conflict-resolution DCV entries). Amendments create
labeled sub-gates (Gate 3a, Gate 3b, …) and do not invalidate the original `GATE 3: CLOSED`.
See the Gate 4 Amendment Protocol.

**Offline Experience Gaps**

`OEG-NN: [scenario] — [unhandled user encounter]`
Nil: `OEG-NIL: No offline experience gaps identified — [scope rationale: why this gap type does not apply for this deployment pattern].`

**Data Consistency Violations**

`DCV-NN: [data object] — [missing invariant]`
Nil: `DCV-NIL: No data consistency violations identified — [scope rationale].`

**Missing Recovery Flows**

`MRF-NN: [scenario] — [actor with no defined action]`
Nil: `MRF-NIL: No missing recovery flows identified — [scope rationale].`

```
GATE 3 STATUS: [OPEN | CLOSED]
OEG section: [present | nil-stated]
DCV section: [present | nil-stated]
MRF section: [present | nil-stated]
Reason if OPEN: [name the specific blocking item — absent section name, finding with
  no scenario reference, or nil statement missing scope rationale]
```

A bare `GATE 3: OPEN` with no `Reason if OPEN` is an error.
If `GATE 3: CLOSED`, proceed to Gate 3b and Gate 4.

---

### Gate 3b — Coverage Gap Registry

**Entry condition**: Gate 3 `CLOSED` AND Gate 1b `CLOSED`.
**Exit condition**: Every permanently BARRED entry from Gate 1b appears as a named coverage
gap, or the nil statement is declared. Write `GATE 3b: CLOSED` when complete.

**Permanently BARRED Entries → Coverage Gaps**

For each entry in `Permanently BARRED` from Gate 1b:

```
Coverage Gap: CG-NN
Type: Permanently BARRED (confidence basis unresolved)
Entry: [scenario name from Gate 1]
Class: [degradation class]
Unresolved basis: [the confidence gap named in Gate 1 that was never resolved]
Implication: [what this coverage gap means for the completeness of this analysis]
```

If no permanently BARRED entries:
`CG-NIL: No permanently BARRED entries — all BARRED entries either resolved to Include or were reclassified to Argued-Impossible with retained rationale.`

```
GATE 3b STATUS: [OPEN | CLOSED]
Coverage gaps recorded: [count or "CG-NIL"]
Reason if OPEN: [name the specific blocking item]
```

Gates 3b and Gate 4 may run in parallel.

---

### Gate 4 — Conflict Resolution Adequacy

**Entry condition**: Gate 2 `CLOSED` AND Gate 3 `CLOSED`.

**Exit condition**: Every Eventual-Consistency scenario from Gate 2 has a conflict-resolution
entry with a named strategy, adequacy verdict, and rationale. The Gate 4 Amendment Review is
complete — either sub-gate amendments have been applied and closed, or the No-Amendment
Confirmation is written. Write `GATE 4: CLOSED` when all conditions are met.

For each Eventual-Consistency scenario:

```
CR-NN: [scenario name]
Conflict strategy: [last-write-wins | merge | manual-reconcile | reject-stale | undefined]
Data type: [object in conflict]
Adequacy verdict: [adequate | inadequate]
Rationale: [one sentence — why this strategy does or does not preserve invariants for this data type]
```

---

#### Gate 4 Amendment Protocol

Apply this protocol for every CR entry where adequacy verdict is `inadequate` or strategy is
`undefined`. Each such finding triggers a Gate 3 re-open.

**Step 1 — Declare re-open**:

```
GATE 3: REOPENED
Triggering finding: CR-NN — [brief description of the inadequate/undefined verdict that requires a DCV amendment]
Amendment to apply: DCV-CR-NN — [data object] — [consequence of the inadequate/undefined strategy]
```

**Step 2 — Apply amendment**:

```
DCV-CR-NN: [data object] — [missing invariant created by the inadequate/undefined strategy]
Triggered by: CR-NN
```

**Step 3 — Re-close under labeled sub-gate**:

```
GATE 3[letter]: AMENDED — triggered by CR-NN
Status: CLOSED
Amendment applied: DCV-CR-NN added to Data Consistency Violations section
```

Use sequential letter suffixes for multiple amendments: `GATE 3a`, `GATE 3b`, `GATE 3c`, …
Each sub-gate names its triggering CR-NN finding. A sub-gate without a triggering finding
citation is not a valid amendment record.

**No-Amendment Confirmation** — write this when all CR verdicts are `adequate` and no
strategy is `undefined`:

```
GATE 4 AMENDMENT REVIEW: No inadequate or undefined CR verdicts.
GATE 3 ORIGINAL CLOSURE CONFIRMED — no amendments required.
```

This confirmation is mandatory. Its absence means the amendment check was skipped, not that
no amendments were needed.

---

After all CR entries and amendment protocol steps:

```
GATE 4 STATUS: [OPEN | CLOSED]
CR entries assessed: [count]
Gate 3 sub-gate amendments: [list sub-gate labels with triggering CR-NN IDs, or "none — see No-Amendment Confirmation"]
Reason if OPEN: [name the specific blocking item — scenario ID missing a CR entry, CR entry
  with an invalid adequacy label, sub-gate amendment declared but not closed, or
  No-Amendment Confirmation absent when all verdicts are adequate]
```

A bare `GATE 4: OPEN` with no `Reason if OPEN` is an error.

---

### Scope Verification

**Entry condition**: Gate 2 `CLOSED`.

Cross-check every `In-scope` operation from the Scope Declaration against the Gate 2 scenario table.

```
Operation: [name]
Coverage: [covered — list scenario IDs that reference this operation in their Capability field]
       | [gap — no Gate 2 scenario references this operation]
```

If any In-scope operation has no coverage:

```
SCOV-NN: [operation name]
Status: Coverage gap — declared In-scope before Gate 1 but no scenario in Gate 2 covers this operation.
Note: This is a gap, not an exclusion. Exclusions appear in the Scope Declaration as "Excluded"
  with rationale. An uncovered In-scope operation means the scenario table does not honor the
  pre-analysis commitment.
```

If all In-scope operations have coverage:
`SCOV-NIL: All declared In-scope operations receive scenario coverage in Gate 2 — pre-analysis commitment honored.`

**Output artifact**: `simulations/flow/resilience/{{topic}}-resilience-{{date}}.md`
