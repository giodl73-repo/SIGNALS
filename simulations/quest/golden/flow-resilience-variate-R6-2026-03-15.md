# Flow-Resilience Skill — Round 6 Variations (Rubric v6)

**Skill**: flow-resilience — Simulate degraded conditions: offline, partial failure, eventual consistency.
**Rubric**: v6 (C-01 through C-24, essential/recommended/aspirational tiers)
**Date**: 2026-03-15

---

## Round 6 Context

**New criteria entering R6**: C-22, C-23, and C-24 are freshly extracted from R5 excellence signals.

**R5 diagnosis**:
- V-01 (R5) earned C-12 by writing `OEG-NIL: [scope rationale]` — a nil finding with a type prefix
  and scope rationale. C-22 tightens this: the prefix must carry a run-level unique numeric suffix
  (`OEG-NIL-1`, `DCV-NIL-1`, `MRF-NIL-1`). When a multi-phase analysis produces two nil findings
  of the same type, non-unique forms (`OEG-NIL:`) are ambiguous — the reader cannot tell whether
  they are one finding or two. The indexed identifier resolves this; it also enables a supersession
  reference (`DCV-NIL-1: SUPERSEDED — DCV-CR-01 added`) when a Gate 4 amendment replaces a nil.
  Without a unique ID, the supersession cannot cite which nil was overwritten.
- V-01 (R5) introduced `SCOPE DECLARATION COMPLETE` as an opening confirmation block and a
  `Scope Verification` section at the end. C-23 tightens this: the commitment must be formally
  bracketed by two named boundary blocks — an opening block (closing the declaration phase before
  analysis begins) and a terminal `Scope Verification` block (naming each declared operation with
  its coverage outcome). The terminal block is not satisfied by a generic verification table; it
  must reference the opening declaration's operation list by name and declare coverage outcomes
  per-operation. A declaration with only one block is formally open and unverified.
- V-01 (R5) earned C-14 by writing `If verdict is 'no' or strategy is 'undefined': append DCV-CR-NN`
  — an inline conditional embedded in prose. C-24 tightens this: the conditional must be encoded
  as a named rule (`RULE CR-DCV: if verdict is [inadequate | undefined]: append DCV-CR-NN`) within
  the template, not described in a prose instruction or left to analyst discretion. A prose
  instruction that describes the linkage without a named rule block does not satisfy C-24. At least
  two distinct named conditional rules are required.

**R6 synthesis path**: The three new criteria complete the format-layer formalization:

- C-22: Nil-finding uniqueness — typed identifiers with run-level unique suffixes prevent ambiguity
  when multiple nil findings of the same type exist and enable cross-reference supersession.
- C-23: Scope bracket closure — the scope declaration is not verified unless both the opening and
  terminal blocks are present and paired; a single block is an unclosed bracket.
- C-24: Mandatory conditional rules — cross-section linkages encoded as named rule blocks make
  correct behavior mandatory and auditable by rule ID, not dependent on analyst interpretation
  of prose instructions.

**Axes selected**:

- V-01: Single-axis — Typed Nil-Finding Identifiers (C-22)
- V-02: Single-axis — Scope Declaration Closure Bracket (C-23)
- V-03: Single-axis — Template-Embedded Conditional Linkage Rules (C-24)
- V-04: Combination — Typed Nil Identifiers + Scope Closure Bracket (C-22 + C-23)
- V-05: Combination — All three new axes + full R5 formalization (C-22 + C-23 + C-24 + C-15 through C-21)

---

## V-01 — Typed Nil-Finding Identifiers

**Variation axis**: Typed nil-finding identifiers with run-level unique numeric suffixes
**Hypothesis**: The gap between C-12 and C-22 is the difference between a nil statement that
is readable and one that is queryable and supersedable. V-01 from R5 wrote `OEG-NIL: [scope
rationale]` — correct for C-12. C-22 requires the prefix to carry a unique numeric suffix:
`OEG-NIL-1`. Even when only one nil of a type is written, the `-1` suffix is required to
establish the uniqueness contract and distinguish "first nil of this type" from "nil with no
ID." When a Gate 4 amendment replaces a DCV nil, the supersession record must cite the nil
by ID (`DCV-NIL-1: SUPERSEDED — DCV-CR-01 added`). Without the typed unique ID, this
cross-reference is impossible. The single axis in V-01 is the nil identifier format: every
nil finding in Phase 3 carries a typed prefix and a unique numeric suffix. The base structure
is a four-phase analysis (no scope declaration, no full gate formalization) to isolate the
nil-identifier mechanism without confounding it with other structural requirements.

---

You are a Commerce / distributed systems domain expert. Your task is to simulate how a
commerce system behaves under degraded conditions and produce a signal artifact for
decision-making.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### Phase 1 — Discovery Triage

Enumerate every failure mode that could plausibly apply to the architecture implied by the
topic. For every entry, assign exactly one disposition:

| Disposition | Meaning |
|-------------|---------|
| `Include` | Mechanism understood; commerce impact clear for at least one named commerce operation. Enters Phase 2. |
| `BARRED` | Plausible but cannot be confirmed without architecture detail absent from the topic signal. Excluded from Phase 2; confidence basis must be named. |
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
Include entries by class: Offline=[N] / Partial-Failure=[N] / Eventual-Consistency=[N]
```

The gate is `CLOSED` only when every entry has a named disposition, every `BARRED` entry
has a stated basis, and each degradation class has at least two `Include` entries. Do not
proceed to Phase 2 until the Triage Gate is `CLOSED`.

---

### Phase 2 — Scenario Analysis

For every `Include` entry from Phase 1, produce the four mandatory fields. At least six
scenarios total; at least two per degradation class.

**[Entry ID — Scenario Name]** `[Class]`

- **State**: Precise failure description. Name which services, replicas, or network segments
  are affected and how.
- **Capability**: For each commerce operation relevant to the scenario, state whether it is
  `available` / `degraded` / `blocked`. Reference at least two of: checkout, inventory
  reservation, payment processing, cart state, order fulfillment, loyalty redemption.
- **Data at risk**: Named data object, failure mode (lost / stale / inconsistent / duplicated),
  and scope (per-user / per-session / global).
- **Recovery path**: Ordered steps with actor prefix — `[client]` / `[server]` / `[operator]` /
  `[user]`. Each step names its trigger condition and observable success signal.

---

### Phase 3 — Gap Identification

Produce three labeled sections. Each finding references a named scenario or data object
from Phase 2.

**Typed Nil-Finding Identifier Protocol**

When a gap section has no findings, write a typed nil finding. Every nil finding carries:

1. A gap-type prefix: `OEG-NIL` (offline experience gap), `DCV-NIL` (data consistency
   violation), `MRF-NIL` (missing recovery flow)
2. A run-level unique numeric suffix: `-1`, `-2`, etc. The suffix is required even when
   only one nil of that type is written in this analysis run. Assign suffixes sequentially
   within each prefix type.
3. A scope rationale explaining why this gap type does not apply.

Format: `OEG-NIL-1: No offline experience gaps identified — [scope rationale].`

A nil statement without a typed prefix identifier does not satisfy the nil-finding norm.
A nil statement that reuses an identifier already assigned earlier in this run is an error;
use the next available suffix (`OEG-NIL-2`) for any subsequent nil of the same type.

**Nil supersession**: If a Phase 4 amendment adds a DCV-CR entry to a section that held
`DCV-NIL-N`, mark the nil as superseded:
`DCV-NIL-N: SUPERSEDED — DCV-CR-NN added in Phase 4 amendment`

**Offline Experience Gaps**

`OEG-NN: [scenario name] — [what the user encounters that the design does not handle]`

If none: `OEG-NIL-1: No offline experience gaps identified — [scope rationale explaining
why this gap type does not apply for this deployment pattern].`

**Data Consistency Violations**

`DCV-NN: [data object] — [missing invariant or undetected divergence]`

If none: `DCV-NIL-1: No data consistency violations identified — [scope rationale].`

**Missing Recovery Flows**

`MRF-NN: [scenario name] — [the recovery actor with no defined action]`

If none: `MRF-NIL-1: No missing recovery flows identified — [scope rationale].`

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

If verdict is `no` or strategy is `undefined`: append `DCV-CR-NN` to Phase 3 Data
Consistency Violations. If the DCV section held `DCV-NIL-1`, write:
`DCV-NIL-1: SUPERSEDED — DCV-CR-NN added in Phase 4 amendment`

**Output artifact**: `simulations/flow/resilience/{{topic}}-resilience-{{date}}.md`

---

## V-02 — Scope Declaration Closure Bracket

**Variation axis**: Two-block scope declaration bracket with named opening and terminal blocks
**Hypothesis**: R5 V-01 introduced `SCOPE DECLARATION COMPLETE` as an opening confirmation
and `Scope Verification` as a terminal cross-check. These were structurally present but not
formally paired: the terminal section was a verification activity, not an explicitly named
closing bracket that references the opening by name. C-23 requires both blocks to be named
boundary events visible as a pair — the opening block closes the declaration phase; the
terminal block closes the verification phase and must name each declared operation with its
coverage outcome (covered / gap / out-of-scope). A declaration with only one block is an
unclosed bracket: the reader cannot confirm whether coverage was cross-checked without
reading all scenario bodies. The terminal block must reference the opening declaration's
operation list by name rather than reconstructing the list from analysis output, so the
bracket is independently auditable. The single axis in V-02 is the scope bracket: every
scope declaration ends with an opening block and, after analysis, a terminal closing block.
The base structure is a standard gate-based analysis to isolate the bracket mechanism.

---

You are a Commerce / distributed systems domain expert. Simulate how the commerce system
described by the topic behaves under degraded conditions.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### Commerce Operation Scope Declaration

Before any gate opens, declare which commerce operations this resilience analysis covers.
This is a commitment, not a discovery — it must precede Gate 1.

Choose at least four operations from the standard set:
checkout / inventory reservation / payment processing / cart state / order fulfillment / loyalty redemption

For each operation:

```
Operation: [name]
Scope: [In-scope | Excluded]
Rationale if Excluded: [one sentence]
```

After all operations are declared, write the **opening bracket block**:

```
╔══ SCOPE BRACKET: OPENING ══════════════════════════════════════╗
SCOPE DECLARATION COMPLETE
In-scope operations: [list — minimum four]
Excluded operations: [list, or "none"]
Terminal bracket block: Scope Verification (appears after Gate 4)
╚════════════════════════════════════════════════════════════════╝
```

Gate 1 may not open before this block is written.

---

### Gate 1 — Failure Mode Discovery

**Entry condition**: Scope Declaration opening bracket written.
**Exit condition**: Every failure mode entry carries one of three named dispositions
(`Include` / `BARRED` / `Argued-Impossible`) with a stated basis; each degradation class
has at least two `Include` entries. Write `GATE 1: CLOSED` only when all conditions are met.

```
Entry: [name]
Class: [Offline / Partial-Failure / Eventual-Consistency]
Disposition: [Include | BARRED | Argued-Impossible]
Basis: [one sentence]
```

"Flagged" is not a disposition. A gate with no explicit `CLOSED` declaration is `OPEN`.

```
GATE 1 STATUS: [OPEN | CLOSED]
Include entries by class: Offline=[N] / Partial-Failure=[N] / Eventual-Consistency=[N]
```

If `GATE 1: OPEN`, resolve before continuing. If `GATE 1: CLOSED`, proceed to Gate 2.

---

### Gate 2 — Scenario Analysis

**Entry condition**: Gate 1 `CLOSED`.
**Exit condition**: Every `Include` entry has a complete four-field analysis. Minimum: six
scenarios total, two per class. Write `GATE 2: CLOSED` when all conditions are met.

For each `Include` entry:

**[Entry ID — Name]** `[Class]`

- **State**: Precise failure description — named services, replicas, segments, failure mode
- **Capability**: For each In-scope operation from the Scope Declaration, state whether it
  is `available` / `degraded` / `blocked`. Do not omit declared In-scope operations.
- **Data at risk**: Named object, failure mode (lost / stale / inconsistent / duplicated), scope
- **Recovery path**: Actor-prefixed ordered steps — `[client]` / `[server]` / `[operator]` /
  `[user]`; each step includes trigger condition and observable success signal

```
GATE 2 STATUS: [OPEN | CLOSED]
Scenario count: Offline=[N] / Partial-Failure=[N] / Eventual-Consistency=[N]
```

If `GATE 2: CLOSED`, proceed to Gate 3.

---

### Gate 3 — Gap Identification

**Entry condition**: Gate 2 `CLOSED`.
**Exit condition**: All three gap sections present and labeled; nil findings carry scope
rationale; all findings reference named Gate 2 scenarios or data objects. Write `GATE 3: CLOSED`.

**Offline Experience Gaps**

`OEG-NN: [scenario name] — [unhandled user encounter]`
Nil: `OEG-NIL: No offline experience gaps identified — [scope rationale].`

**Data Consistency Violations**

`DCV-NN: [data object] — [missing invariant or undetected divergence]`
Nil: `DCV-NIL: No data consistency violations identified — [scope rationale].`

**Missing Recovery Flows**

`MRF-NN: [scenario name] — [actor with no defined action]`
Nil: `MRF-NIL: No missing recovery flows identified — [scope rationale].`

```
GATE 3 STATUS: [OPEN | CLOSED]
OEG section: [present | nil-stated]
DCV section: [present | nil-stated]
MRF section: [present | nil-stated]
```

If `GATE 3: CLOSED`, proceed to Gate 4.

---

### Gate 4 — Conflict Resolution Adequacy

**Entry condition**: Gate 3 `CLOSED`.
**Exit condition**: Every Eventual-Consistency scenario from Gate 2 has a CR entry. Every
`inadequate` or `undefined` verdict has generated a `DCV-CR-NN` entry appended to Gate 3.
Write `GATE 4: CLOSED` when complete.

```
Scenario: [name]
Strategy: [last-write-wins | merge | manual-reconcile | reject-stale | undefined]
Data type: [object in conflict]
Adequacy verdict: [adequate | inadequate]
Rationale: [one sentence]
```

If verdict is `inadequate` or strategy is `undefined`: append `DCV-CR-NN` to Gate 3 DCV list.

```
GATE 4 STATUS: [OPEN | CLOSED]
DCV amendments from CR: [list DCV-CR-NN entries added, or "none"]
```

---

### Scope Verification *(Terminal Bracket Block)*

**Entry condition**: Gate 2 `CLOSED` (scenario table complete).

Cross-check every operation from the opening Scope Declaration bracket against the Gate 2
scenario table. This block closes the scope commitment opened by `SCOPE BRACKET: OPENING`.

For each declared operation:

```
Operation: [name] (declared [In-scope | Excluded])
Coverage outcome: [covered — scenario IDs] | [gap — declared In-scope; no Gate 2 scenario covers this operation] | [out-of-scope — declared Excluded; not expected to appear]
```

If any In-scope operation has no coverage:
`SCOV-NN: [operation name] — declared In-scope in opening bracket but not covered in Gate 2.`

If all In-scope operations have coverage:
`SCOV-NIL: All declared In-scope operations receive scenario coverage in Gate 2.`

Write the **terminal bracket block** after all coverage outcomes are recorded:

```
╔══ SCOPE BRACKET: CLOSING ══════════════════════════════════════╗
Opening block: SCOPE BRACKET: OPENING (before Gate 1)
Terminal block: Scope Verification (this block)
In-scope operations declared: [list from opening block]
Coverage outcomes: covered=[N] / gap=[N] / out-of-scope=[N]
SCOPE BRACKET CLOSED
╚════════════════════════════════════════════════════════════════╝
```

This terminal block, together with the opening `SCOPE BRACKET: OPENING` block, forms the
complete scope closure bracket. A scope declaration without this terminal block is unverified.

**Output artifact**: `simulations/flow/resilience/{{topic}}-resilience-{{date}}.md`

---

## V-03 — Template-Embedded Conditional Linkage Rules

**Variation axis**: Named conditional linkage rules encoded in the template as named rule blocks
**Hypothesis**: R5 V-04 and V-05 expressed cross-section linkages as protocol instructions
("Apply this protocol for every CR entry where adequacy verdict is `inadequate` or strategy is
`undefined`"). These instructions describe the conditional logic but do not name it — the analyst
reads and interprets the instruction, then applies it. C-24 requires the conditional logic to be
encoded as a named rule in explicit `if [condition]: [action]` form so that correct behavior is
mandatory rather than instructional. Named rules have three properties prose instructions lack:
(1) the trigger condition is precise and testable; (2) the cross-section action is explicit;
(3) the rule can be cited by ID in amendment records, so two separate findings that both trigger
the same linkage are both traceable to the same rule. Without rule names, "amendment applied
because CR-02 was inadequate" and "amendment applied because protocol said so" are equivalent
in the output — there is no rule ID to reference. With at least two named rules, the template
demonstrates that conditional-rule encoding is a systemic pattern, not a one-time exception. The
single axis in V-03 is the linkage rules section: a named `Template Linkage Rules` block precedes
Gate 1 and defines at least two named conditional rules in explicit if-then form. The base
structure is a standard four-gate analysis.

---

You are a Commerce / distributed systems domain expert. Simulate how the commerce system
described by the topic behaves under degraded conditions and produce a signal artifact.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### Template Linkage Rules

The following named conditional rules govern cross-section behavior in this analysis.
Each rule is mandatory — not advisory. When a trigger condition is satisfied, the rule
action applies automatically. Rules are cited by ID in all amendment and sub-gate records
they produce.

```
RULE CR-DCV
Trigger:   if Adequacy verdict is `inadequate` OR Conflict strategy is `undefined`
Action:    append DCV-CR-NN to Gate 3 Data Consistency Violations section
           reopen Gate 3 under labeled sub-gate; cite RULE CR-DCV in the re-open record
Applies:   Gate 4 conflict-resolution entries
IDs used:  DCV-CR-01, DCV-CR-02, ... (one per trigger instance)
```

```
RULE BARRED-CG
Trigger:   if entry remains Permanently BARRED after Gate 1b resolution attempt
Action:    append CG-NN to Coverage Gap Registry (Gate 3b)
           cite RULE BARRED-CG in the CG record
Applies:   Gate 1b resolution outcomes
IDs used:  CG-01, CG-02, ... (one per permanently barred entry)
```

If any other cross-section linkage is identified during analysis, declare it inline at first
application: `RULE [name] (inline): if [condition]: [action]`

Do not apply an undeclared linkage.

---

### Gate 1 — Failure Mode Discovery

**Entry condition**: None (Gate 1 is the analysis entry point).
**Exit condition**: Every failure mode entry carries one of three named dispositions
(`Include` / `BARRED` / `Argued-Impossible`) with a stated basis; each degradation class
has at least two `Include` entries. Write `GATE 1: CLOSED` only when all conditions are met.

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
BARRED entries: [list names, or "none"]
Argued-Impossible entries: [list names, or "none"]
```

If `GATE 1: CLOSED`, proceed to Gate 1b.

---

### Gate 1b — BARRED Register

**Entry condition**: Gate 1 `CLOSED`.
**Exit condition**: Every BARRED entry from Gate 1 has a resolution verdict. Write `GATE 1b: CLOSED`.

```
Entry: [name]
Confidence basis: [restate from Gate 1]
Resolution attempt: [what in the topic signal could resolve this, and whether it does]
Outcome: [Include (reclassified) | Permanently BARRED]
```

**RULE BARRED-CG trigger point** — for each `Outcome: Permanently BARRED`:

```
RULE BARRED-CG triggered: CG-NN queued for Gate 3b
Entry: [name] / Class: [class] / Unresolved basis: [confidence gap]
```

```
GATE 1b STATUS: [OPEN | CLOSED]
Reclassified to Include: [list, or "none"]
Permanently BARRED: [list, or "none"]
RULE BARRED-CG triggers queued: [list CG-NN IDs, or "none"]
```

If `GATE 1b: CLOSED`, proceed to Gate 2.

---

### Gate 2 — Scenario Analysis

**Entry condition**: Gate 1 `CLOSED` AND Gate 1b `CLOSED`.
**Exit condition**: Every `Include` entry (from Gate 1 and reclassified from Gate 1b) has a
complete four-field analysis. Minimum: six scenarios total, two per class. Write `GATE 2: CLOSED`.

**[Entry ID — Name]** `[Class]`

- **State**: Precise failure description — named services, replicas, segments, failure mode
- **Capability**: Available / degraded / blocked — named per commerce operation (checkout,
  inventory reservation, payment processing, cart state, order fulfillment)
- **Data at risk**: Named object, failure mode (lost / stale / inconsistent / duplicated), scope
- **Recovery path**: Actor-prefixed ordered steps — `[client]` / `[server]` / `[operator]` /
  `[user]`; each step includes trigger condition and observable success signal

```
GATE 2 STATUS: [OPEN | CLOSED]
Scenario count: Offline=[N] / Partial-Failure=[N] / Eventual-Consistency=[N]
```

If `GATE 2: CLOSED`, proceed to Gate 3.

---

### Gate 3 — Gap Identification

**Entry condition**: Gate 2 `CLOSED`.
**Exit condition**: All three gap sections present and labeled; nil findings carry scope
rationale; all findings reference named Gate 2 scenarios or data objects. Write `GATE 3: CLOSED`.

Note: RULE CR-DCV (Gate 4) may append `DCV-CR-NN` entries to the DCV section after Gate 3
initially closes. These amendments create labeled sub-gates and do not invalidate `GATE 3: CLOSED`.

**Offline Experience Gaps**

`OEG-NN: [scenario name] — [unhandled user encounter during offline failure]`
Nil: `OEG-NIL: No offline experience gaps identified — [scope rationale].`

**Data Consistency Violations**

`DCV-NN: [data object] — [missing invariant or undetected divergence]`
[RULE CR-DCV may append DCV-CR-NN entries here from Gate 4; do not pre-populate]
Nil: `DCV-NIL: No data consistency violations identified — [scope rationale].`

**Missing Recovery Flows**

`MRF-NN: [scenario name] — [recovery actor with no defined action]`
Nil: `MRF-NIL: No missing recovery flows identified — [scope rationale].`

```
GATE 3 STATUS: [OPEN | CLOSED]
OEG section: [present | nil-stated]
DCV section: [present | nil-stated]
MRF section: [present | nil-stated]
```

If `GATE 3: CLOSED`, proceed to Gate 3b and Gate 4 in parallel.

---

### Gate 3b — Coverage Gap Registry

**Entry condition**: Gate 1b `CLOSED` AND Gate 3 `CLOSED`.
**Exit condition**: Every CG-NN queued by RULE BARRED-CG in Gate 1b appears as a named
coverage gap, or `CG-NIL` is declared. Write `GATE 3b: CLOSED`.

For each CG-NN queued by RULE BARRED-CG:

```
Coverage Gap: CG-NN
Triggered by: RULE BARRED-CG
Entry: [scenario name from Gate 1]
Class: [degradation class]
Unresolved basis: [confidence gap from Gate 1b that was never resolved]
```

If no RULE BARRED-CG triggers occurred:
`CG-NIL: RULE BARRED-CG not triggered — no Permanently BARRED entries in Gate 1b.`

```
GATE 3b STATUS: [OPEN | CLOSED]
Coverage gaps recorded: [count, or "CG-NIL"]
```

Gates 3b and Gate 4 may run in parallel.

---

### Gate 4 — Conflict Resolution Adequacy

**Entry condition**: Gate 3 `CLOSED`.
**Exit condition**: Every Eventual-Consistency scenario from Gate 2 has a CR entry. RULE CR-DCV
has been applied to every `inadequate` or `undefined` verdict — sub-gate amendments applied
and closed, or No-Amendment Confirmation written. Write `GATE 4: CLOSED`.

```
CR-NN: [scenario name]
Conflict strategy: [last-write-wins | merge | manual-reconcile | reject-stale | undefined]
Data type: [object in conflict]
Adequacy verdict: [adequate | inadequate]
Rationale: [one sentence]
```

**RULE CR-DCV trigger point** — for each CR entry where verdict is `inadequate` or strategy
is `undefined`:

```
RULE CR-DCV triggered by CR-NN:
GATE 3: REOPENED — triggering finding: CR-NN / [brief description]
DCV-CR-NN: [data object] — [missing invariant from inadequate/undefined strategy]
Triggered by: CR-NN via RULE CR-DCV
GATE 3[a/b/c]: AMENDED — RULE CR-DCV / CR-NN
Status: CLOSED
Amendment applied: DCV-CR-NN added to Data Consistency Violations
```

Use sequential letter suffixes for multiple amendments: Gate 3a, Gate 3b, Gate 3c, …
Each sub-gate cites its triggering CR-NN finding and RULE CR-DCV.

**No-Amendment Confirmation** (write when all CR verdicts are `adequate` and all strategies
are defined):

```
RULE CR-DCV: no triggers. All CR verdicts are adequate; all strategies are defined.
GATE 3 ORIGINAL CLOSURE CONFIRMED — no RULE CR-DCV amendments required.
```

This confirmation is mandatory. Its absence means the amendment check was skipped.

```
GATE 4 STATUS: [OPEN | CLOSED]
CR entries assessed: [count]
RULE CR-DCV triggers: [list sub-gate labels and CR-NN IDs, or "none — see No-Amendment Confirmation"]
```

**Output artifact**: `simulations/flow/resilience/{{topic}}-resilience-{{date}}.md`

---

## V-04 — Combination: Typed Nil Identifiers + Scope Closure Bracket

**Variation axes**: Typed nil-finding identifiers (C-22) + Scope declaration closure bracket (C-23)
**Hypothesis**: C-22 and C-23 both operate on the format layer but at different artifact
granularities. C-22 enforces that individual nil findings are uniquely typed and addressable;
C-23 enforces that the scope commitment is bounded by two named block events that are
independently auditable. The combination matters because of a specific interaction: when a
Gate 4 amendment supersedes a DCV nil (`DCV-NIL-1: SUPERSEDED — DCV-CR-01 added`), the
supersession reference depends on C-22's unique ID. And when the terminal Scope Verification
block lists coverage outcomes per declared operation, those outcomes may reference the DCV
nil's supersession to note that consistency violations emerged post-analysis. Without typed
unique IDs (C-22), the terminal block cannot trace which nil was superseded. Without the
terminal block (C-23), the coverage cross-check is unverified even if the scenario table
exists. Together C-22 and C-23 create a fully typed, fully bounded output: every nil finding
is a first-class artifact with its own ID; the scope commitment has an explicit open and close.

---

You are a Commerce / distributed systems domain expert. Produce a resilience signal artifact
for the commerce system described by the topic.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### Commerce Operation Scope Declaration

Declare the commerce operations this analysis covers before any gate opens. Assign each
operation a short identifier (OP-01, OP-02, …) for use in coverage cross-references.

Choose at least four operations from the standard set:
checkout / inventory reservation / payment processing / cart state / order fulfillment / loyalty redemption

```
Operation: [name] — ID: OP-NN
Scope: [In-scope | Excluded]
Rationale if Excluded: [one sentence]
```

Write the **opening bracket block** after the last operation declaration:

```
╔══ SCOPE BRACKET: OPENING ══════════════════════════════════════╗
SCOPE DECLARATION COMPLETE
In-scope: [OP-01: name, OP-02: name, ...]   (minimum four)
Excluded: [OP-NN: name, ...]   or "none"
Terminal bracket block: Scope Verification (appears after Gate 4)
╚════════════════════════════════════════════════════════════════╝
```

Gate 1 may not open before the opening bracket block is written.

---

### Gate 1 — Failure Mode Discovery

**Entry condition**: Scope Declaration opening bracket written.
**Exit condition**: Every failure mode entry carries one of three named dispositions
(`Include` / `BARRED` / `Argued-Impossible`) with a stated basis; each degradation class
has at least two `Include` entries. Write `GATE 1: CLOSED` only when all conditions are met.

```
Entry: [name]
Class: [Offline / Partial-Failure / Eventual-Consistency]
Disposition: [Include | BARRED | Argued-Impossible]
Basis: [one sentence]
```

"Flagged" is not a disposition. A gate with no explicit `CLOSED` declaration is `OPEN`.

```
GATE 1 STATUS: [OPEN | CLOSED]
Include entries by class: Offline=[N] / Partial-Failure=[N] / Eventual-Consistency=[N]
BARRED entries: [list names, or "none"]
Argued-Impossible entries: [list names, or "none"]
```

If `GATE 1: CLOSED`, proceed to Gate 2.

---

### Gate 2 — Scenario Analysis

**Entry condition**: Gate 1 `CLOSED`.
**Exit condition**: Every `Include` entry has a complete four-field analysis. Minimum: six
scenarios total, two per class. Write `GATE 2: CLOSED` when all conditions are met.

**[Entry ID — Name]** `[Class]`

- **State**: Precise failure description — named services, replicas, segments, failure mode
- **Capability**: For each In-scope operation (by OP-NN ID) from the Scope Declaration, state
  whether it is `available` / `degraded` / `blocked`. Do not omit declared operations.
- **Data at risk**: Named object, failure mode (lost / stale / inconsistent / duplicated), scope
- **Recovery path**: Actor-prefixed ordered steps — `[client]` / `[server]` / `[operator]` /
  `[user]`; each step includes trigger condition and observable success signal

```
GATE 2 STATUS: [OPEN | CLOSED]
Scenario count: Offline=[N] / Partial-Failure=[N] / Eventual-Consistency=[N]
```

If `GATE 2: CLOSED`, proceed to Gate 3.

---

### Gate 3 — Gap Identification

**Entry condition**: Gate 2 `CLOSED`.
**Exit condition**: All three gap sections present and labeled; nil findings carry typed unique
identifiers and scope rationale; all findings reference named Gate 2 scenarios or data objects.
Write `GATE 3: CLOSED`.

**Typed Nil-Finding Identifiers** — Every nil finding carries:
- A gap-type prefix: `OEG-NIL`, `DCV-NIL`, or `MRF-NIL`
- A run-level unique numeric suffix: `-1`, `-2`, …; required even for the first nil of each type
- A scope rationale

Format: `OEG-NIL-1: No offline experience gaps identified — [scope rationale].`

If a Gate 4 amendment supersedes a nil, mark it:
`DCV-NIL-1: SUPERSEDED — DCV-CR-NN added in Gate 4 amendment`

**Offline Experience Gaps**

`OEG-NN: [scenario name] — [unhandled user encounter during offline failure]`
Nil: `OEG-NIL-1: No offline experience gaps identified — [scope rationale].`

**Data Consistency Violations**

`DCV-NN: [data object] — [missing invariant or undetected divergence]`
[DCV-CR-NN entries may be appended here by Gate 4 adequacy analysis]
Nil: `DCV-NIL-1: No data consistency violations identified — [scope rationale].`

**Missing Recovery Flows**

`MRF-NN: [scenario name] — [actor with no defined action]`
Nil: `MRF-NIL-1: No missing recovery flows identified — [scope rationale].`

```
GATE 3 STATUS: [OPEN | CLOSED]
OEG section: [present | nil-stated (OEG-NIL-N)]
DCV section: [present | nil-stated (DCV-NIL-N)]
MRF section: [present | nil-stated (MRF-NIL-N)]
```

If `GATE 3: CLOSED`, proceed to Gate 4.

---

### Gate 4 — Conflict Resolution Adequacy

**Entry condition**: Gate 3 `CLOSED`.
**Exit condition**: Every Eventual-Consistency scenario from Gate 2 has a CR entry. Every
`inadequate` or `undefined` verdict has generated a `DCV-CR-NN` entry appended to Gate 3,
with nil supersession notation where applicable. Write `GATE 4: CLOSED` when complete.

```
Scenario: [name]
Strategy: [last-write-wins | merge | manual-reconcile | reject-stale | undefined]
Data type: [object in conflict]
Adequacy verdict: [adequate | inadequate]
Rationale: [one sentence]
```

If verdict is `inadequate` or strategy is `undefined`: append `DCV-CR-NN` to Gate 3 DCV
section. If the DCV section held `DCV-NIL-N`, write:
`DCV-NIL-N: SUPERSEDED — DCV-CR-NN added in Gate 4 amendment`

```
GATE 4 STATUS: [OPEN | CLOSED]
DCV amendments from CR: [list DCV-CR-NN entries added, or "none"]
```

---

### Scope Verification *(Terminal Bracket Block)*

**Entry condition**: Gate 2 `CLOSED`.

Cross-check every operation from the opening Scope Declaration (OP-01, OP-02, …) against
the Gate 2 scenario table. This block closes the scope bracket opened by `SCOPE BRACKET: OPENING`.

```
Operation: OP-NN — [name]
Declared scope: [In-scope | Excluded]
Coverage outcome: [covered — scenario IDs referencing this operation in Capability field]
               | [gap — declared In-scope; no Gate 2 scenario references this operation]
               | [out-of-scope — declared Excluded; not expected to appear]
```

If any In-scope operation has no coverage:
`SCOV-NN: OP-NN ([name]) — declared In-scope in opening bracket; no Gate 2 coverage.`

If all In-scope operations have coverage:
`SCOV-NIL: All declared In-scope operations receive scenario coverage in Gate 2.`

Write the **terminal bracket block**:

```
╔══ SCOPE BRACKET: CLOSING ══════════════════════════════════════╗
Opening block: SCOPE BRACKET: OPENING (before Gate 1)
Terminal block: Scope Verification (this block)
In-scope operations: [OP-01, OP-02, ...] — covered=[N] / gap=[N]
Excluded operations: [OP-NN, ...] — out-of-scope=[N]
SCOPE BRACKET CLOSED — pre-analysis commitment verified
╚════════════════════════════════════════════════════════════════╝
```

A scope declaration without this terminal block is unverified regardless of scenario coverage.

**Output artifact**: `simulations/flow/resilience/{{topic}}-resilience-{{date}}.md`

---

## V-05 — Combination: Full R6 Formalization

**Variation axes**: All three new R6 axes (C-22 + C-23 + C-24) layered onto the full R5
formalization (C-15 + C-16 + C-17 + C-18 + C-19 + C-20 + C-21 and supporting prior criteria)
**Hypothesis**: R5 V-05 established a traceable analysis structure across seven criteria: named
dispositions (C-16), barred-entry lifecycle (C-17), formal gate sequencing with entry/exit
conditions (C-18), DS-primitive impossibility arguments (C-15), scope commitment preceding
analysis (C-21), gate blockage transparency (C-19), and downstream sub-gate amendment records
(C-20). The three R6 criteria add the final format-layer requirements. C-22 (typed unique nil
IDs) makes nil findings first-class artifacts — addressable by type, unique by run, supersedable
by ID. C-23 (scope closure bracket) makes the scope commitment verifiably closed — the terminal
block names each declared operation with its coverage outcome, closing the loop that the opening
block opened before Gate 1. C-24 (named conditional rules) makes cross-section linkages
mandatory rather than instructional — RULE CR-DCV and RULE BARRED-CG fire automatically and
are cited by ID in every amendment record they produce. Together these ten formalization criteria
close all remaining audit gaps: every entry is traceable from scope declaration through
discovery to output; every gate is either CLOSED with a record or OPEN with a specific blocker;
every downstream finding that amends a prior gate is cited by rule and finding ID; every nil
finding is typed and unique; the scope commitment is bracketed open and closed.

---

You are a Commerce / distributed systems domain expert. Produce a resilience signal artifact
for the commerce system described by the topic.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### Template Linkage Rules

Named conditional rules governing cross-section behavior. Rules are mandatory — not advisory.
Each fires automatically when its trigger condition is satisfied and is cited by ID in every
amendment record it produces. Declare additional inline rules at first application if needed.

```
RULE CR-DCV
Trigger:   if Adequacy verdict is `inadequate` OR Conflict strategy is `undefined`
Action:    append DCV-CR-NN to Gate 3 Data Consistency Violations section;
           reopen Gate 3 under labeled sub-gate; cite RULE CR-DCV in the re-open record
           supersede DCV-NIL-N if present: "DCV-NIL-N: SUPERSEDED — DCV-CR-NN via RULE CR-DCV"
Applies:   Gate 4 conflict-resolution entries
IDs used:  DCV-CR-01, DCV-CR-02, ...
```

```
RULE BARRED-CG
Trigger:   if entry remains Permanently BARRED after Gate 1b resolution attempt
Action:    append CG-NN to Coverage Gap Registry (Gate 3b); cite RULE BARRED-CG in CG record
Applies:   Gate 1b resolution outcomes
IDs used:  CG-01, CG-02, ...
```

---

### Commerce Operation Scope Declaration

Before any gate opens, declare the commerce operations this analysis covers. Assign each
operation a short identifier (OP-NN) for coverage cross-reference in the terminal bracket.

Choose at least four operations from the standard set:
checkout / inventory reservation / payment processing / cart state / order fulfillment / loyalty redemption

```
Operation: [name] — ID: OP-NN
Scope: [In-scope | Excluded]
Rationale if Excluded: [one sentence]
```

Write the **opening bracket block** after the last operation:

```
╔══ SCOPE BRACKET: OPENING ══════════════════════════════════════╗
SCOPE DECLARATION COMPLETE
In-scope: [OP-01: name, OP-02: name, ...]   (minimum four)
Excluded: [OP-NN: name, ...]   or "none"
Terminal bracket block: Scope Verification (appears after Gate 4)
╚════════════════════════════════════════════════════════════════╝
```

Gate 1 may not open before the opening bracket block is written.

---

### Gate 1 — Triage Discovery

**Entry condition**: Scope Declaration opening bracket written.

**Exit condition**: (a) every failure mode entry carries one of three named dispositions
(`Include` / `BARRED` / `Argued-Impossible`) with a stated basis; (b) no entry uses a
free-text qualifier; (c) each degradation class has at least two `Include` entries.
Write `GATE 1: CLOSED` only when all three conditions are satisfied.

**Disposition table** (three labels, no others):

| Disposition | Criteria | Effect |
|-------------|----------|--------|
| `Include` | High or medium confidence; mechanism and commerce impact understood | Enters Gate 2 |
| `BARRED` | Low confidence; mechanism or impact unclear without absent context | Gate 1b; RULE BARRED-CG applies at resolution |
| `Argued-Impossible` | Foreclosed by a specific named DS primitive; description absence is invalid | Gate 1c; DS Primitive cited field required |

Entry format:

```
Entry: [name]
Class: [Offline / Partial-Failure / Eventual-Consistency]
Disposition: [Include | BARRED | Argued-Impossible]
Basis: [one sentence — architecture reason or confidence gap]
```

"Flagged" is not a disposition. A gate with no `CLOSED` declaration is `OPEN`.

```
GATE 1 STATUS: [OPEN | CLOSED]
Include entries by class: Offline=[N] / Partial-Failure=[N] / Eventual-Consistency=[N]
BARRED entries: [list names, or "none"]
Argued-Impossible entries: [list names, or "none"]
Reason if OPEN: [name the specific blocking item — e.g., "Entry 'X' has no basis stated"
  or "Partial-Failure class has 1 Include entry; 2 required; add 1 more before closing"
  or "Entry 'Y' disposition reads 'Uncertain' — not a named disposition; reclassify"]
```

A bare `GATE 1: OPEN` with no `Reason if OPEN` is an error, not a valid in-progress state.
If `GATE 1: CLOSED`, open Gates 1b and 1c in parallel.

---

### Gate 1b — BARRED Register

**Entry condition**: Gate 1 `CLOSED`.
**Exit condition**: Every BARRED entry from Gate 1 has a resolution verdict (`Include` or
`Permanently BARRED`). Write `GATE 1b: CLOSED` when all entries are resolved.

```
Entry: [name]
Confidence basis: [restate from Gate 1]
Resolution attempt: [what in the topic signal could resolve this, and whether it does]
Outcome: [Include (reclassified) | Permanently BARRED]
If reclassified: add to Gate 2 with note "[reclassified from BARRED — basis resolved: ...]"
```

**RULE BARRED-CG trigger point** — for each `Outcome: Permanently BARRED`:

```
RULE BARRED-CG triggered: CG-NN queued for Gate 3b
Entry: [name] / Class: [class] / Unresolved basis: [confidence gap]
```

```
GATE 1b STATUS: [OPEN | CLOSED]
Reclassified to Include: [list, or "none"]
Permanently BARRED: [list, or "none"]
RULE BARRED-CG triggers queued: [list CG-NN IDs, or "none"]
Reason if OPEN: [name the specific blocking item — entry with no resolution verdict,
  or reclassified entry not yet added to Gate 2]
```

A bare `GATE 1b: OPEN` with no `Reason if OPEN` is an error.
Hold for Gate 1c. Both must be `CLOSED` before Gate 2 opens.

---

### Gate 1c — Impossibility Register

**Entry condition**: Gate 1 `CLOSED`.
**Exit condition**: Every `Argued-Impossible` entry has a `DS Primitive cited:` field with
an architecture argument and inline VALID/INVALID examples. Write `GATE 1c: CLOSED`.

```
Entry: [name]
DS Primitive cited: [exact name — e.g., "CAP theorem AP branch", "synchronous replication
  linearizability guarantee under acknowledged writes", "two-phase locking serializability"]
Architecture argument: [one sentence — what the architecture makes impossible]
VALID impossibility argument: [example that cites the primitive and addresses the architecture]
INVALID impossibility argument: [example invoking description absence — e.g., "The topic
  doesn't mention distributed caching, so cache invalidation staleness cannot apply here."]
```

"The topic doesn't mention X" is never a valid impossibility argument.

```
GATE 1c STATUS: [OPEN | CLOSED]
Argued-Impossible entries documented: [count, or "none — GATE 1c trivially CLOSED"]
Reason if OPEN: [name the specific blocking item]
```

Gates 1b and 1c may run in parallel. Both must be `CLOSED` before Gate 2 opens.

---

### Gate 2 — Scenario Analysis

**Entry condition**: Gate 1 `CLOSED` AND Gate 1b `CLOSED` AND Gate 1c `CLOSED`.

**Exit condition**: Every `Include` entry (from Gate 1 and any reclassified from Gate 1b)
has a complete four-field analysis. Minimum: six scenarios total, two per class. All recovery
paths include at least one actor-prefixed step with trigger condition. Write `GATE 2: CLOSED`.

**[Entry ID — Name]** `[Class]`

- **State**: Named services / replicas / segments + precise failure mode
- **Capability**: For each `In-scope` operation (by OP-NN ID) from the Scope Declaration,
  state whether it is `available` / `degraded` / `blocked`. Do not omit declared operations.
- **Data at risk**: Named data object, failure mode (lost / stale / inconsistent / duplicated), scope
- **Recovery path**: Actor-prefixed ordered steps — `[client]` / `[server]` / `[operator]` /
  `[user]`; each step includes trigger condition and observable success signal

```
GATE 2 STATUS: [OPEN | CLOSED]
Scenario count: Offline=[N] / Partial-Failure=[N] / Eventual-Consistency=[N]
Reason if OPEN: [name the specific blocking item — scenario ID missing a required field,
  class with current count and required count, or scenario with no actor-prefixed recovery step]
```

A bare `GATE 2: OPEN` with no `Reason if OPEN` is an error.
If `GATE 2: CLOSED`, proceed to Gate 3.

---

### Gate 3 — Gap Identification

**Entry condition**: Gate 2 `CLOSED`.

**Exit condition**: All three gap sections present and labeled; nil findings carry typed
unique identifiers and scope rationale; all findings reference named Gate 2 scenarios or
data objects. Write `GATE 3: CLOSED`.

Note: RULE CR-DCV (Gate 4) may append `DCV-CR-NN` entries to the DCV section after Gate 3
initially closes. Amendments create labeled sub-gates (Gate 3a, Gate 3b, …) and do not
invalidate the original `GATE 3: CLOSED`.

**Typed Nil-Finding Identifiers** — Required for all nil findings in this analysis:
- `OEG-NIL-N` — offline experience gap nil (OEG-NIL-1, OEG-NIL-2, …)
- `DCV-NIL-N` — data consistency violation nil (DCV-NIL-1, DCV-NIL-2, …)
- `MRF-NIL-N` — missing recovery flow nil (MRF-NIL-1, MRF-NIL-2, …)

The numeric suffix is required even for the first nil of each type. Assign suffixes
sequentially within each prefix type across the entire analysis run.
If a nil is superseded by RULE CR-DCV: `DCV-NIL-N: SUPERSEDED — DCV-CR-NN via RULE CR-DCV`

**Offline Experience Gaps**

`OEG-NN: [scenario] — [unhandled user encounter]`
Nil: `OEG-NIL-1: No offline experience gaps identified — [scope rationale: why this gap
type does not apply for this deployment pattern].`

**Data Consistency Violations**

`DCV-NN: [data object] — [missing invariant]`
[RULE CR-DCV may append DCV-CR-NN entries here from Gate 4]
Nil: `DCV-NIL-1: No data consistency violations identified — [scope rationale].`

**Missing Recovery Flows**

`MRF-NN: [scenario] — [actor with no defined action]`
Nil: `MRF-NIL-1: No missing recovery flows identified — [scope rationale].`

```
GATE 3 STATUS: [OPEN | CLOSED]
OEG section: [present | nil-stated (OEG-NIL-N)]
DCV section: [present | nil-stated (DCV-NIL-N)]
MRF section: [present | nil-stated (MRF-NIL-N)]
Reason if OPEN: [name the specific blocking item — absent section name, finding with
  no scenario reference, or nil statement missing typed identifier or scope rationale]
```

A bare `GATE 3: OPEN` with no `Reason if OPEN` is an error.
If `GATE 3: CLOSED`, proceed to Gate 3b and Gate 4 in parallel.

---

### Gate 3b — Coverage Gap Registry

**Entry condition**: Gate 1b `CLOSED` AND Gate 3 `CLOSED`.
**Exit condition**: Every CG-NN queued by RULE BARRED-CG in Gate 1b appears as a named
coverage gap, or `CG-NIL` is declared. Write `GATE 3b: CLOSED`.

For each CG-NN queued by RULE BARRED-CG:

```
Coverage Gap: CG-NN
Triggered by: RULE BARRED-CG
Entry: [scenario name from Gate 1]
Class: [degradation class]
Unresolved basis: [confidence gap from Gate 1 that was never resolved in Gate 1b]
Implication: [what this gap means for analysis completeness]
```

If no RULE BARRED-CG triggers occurred:
`CG-NIL: RULE BARRED-CG not triggered — no Permanently BARRED entries in Gate 1b.`

```
GATE 3b STATUS: [OPEN | CLOSED]
Coverage gaps recorded: [count, or "CG-NIL"]
Reason if OPEN: [name the specific blocking item]
```

Gates 3b and Gate 4 may run in parallel.

---

### Gate 4 — Conflict Resolution Adequacy

**Entry condition**: Gate 2 `CLOSED` AND Gate 3 `CLOSED`.

**Exit condition**: Every Eventual-Consistency scenario from Gate 2 has a CR entry with a
named strategy, adequacy verdict, and rationale. RULE CR-DCV has been applied to every
`inadequate` or `undefined` verdict — sub-gate amendments applied and closed, or
No-Amendment Confirmation written. Write `GATE 4: CLOSED`.

```
CR-NN: [scenario name]
Conflict strategy: [last-write-wins | merge | manual-reconcile | reject-stale | undefined]
Data type: [object in conflict]
Adequacy verdict: [adequate | inadequate]
Rationale: [one sentence — why this strategy does or does not preserve invariants]
```

**RULE CR-DCV trigger point** — for each CR entry where verdict is `inadequate` or strategy
is `undefined`:

```
RULE CR-DCV triggered by CR-NN:
GATE 3: REOPENED
Triggering finding: CR-NN — [brief description of the inadequate/undefined verdict]
Amendment to apply: DCV-CR-NN — [data object] — [consequence of inadequate/undefined strategy]
DCV-CR-NN: [data object] — [missing invariant created by the inadequate/undefined strategy]
Triggered by: CR-NN via RULE CR-DCV
[If DCV-NIL-1 was present: DCV-NIL-1: SUPERSEDED — DCV-CR-NN via RULE CR-DCV]
GATE 3[a/b/c]: AMENDED — RULE CR-DCV / CR-NN
Status: CLOSED
Amendment applied: DCV-CR-NN added to Data Consistency Violations
```

Use sequential letter suffixes for multiple amendments: Gate 3a, Gate 3b, Gate 3c, …
Each sub-gate cites its triggering CR-NN and RULE CR-DCV. A sub-gate without a rule and
finding citation is not a valid amendment record.

**No-Amendment Confirmation** (write when all CR verdicts are `adequate` and all strategies
are defined):

```
GATE 4 AMENDMENT REVIEW: RULE CR-DCV not triggered.
All CR verdicts are adequate; all strategies are defined.
GATE 3 ORIGINAL CLOSURE CONFIRMED — no RULE CR-DCV amendments required.
```

This confirmation is mandatory. Its absence means the amendment check was skipped.

```
GATE 4 STATUS: [OPEN | CLOSED]
CR entries assessed: [count]
RULE CR-DCV triggers: [list sub-gate labels and CR-NN IDs, or "none — see No-Amendment Confirmation"]
Reason if OPEN: [name the specific blocking item — scenario ID missing a CR entry, CR entry
  with invalid adequacy label, sub-gate amendment not closed, or No-Amendment Confirmation absent]
```

A bare `GATE 4: OPEN` with no `Reason if OPEN` is an error.

---

### Scope Verification *(Terminal Bracket Block)*

**Entry condition**: Gate 2 `CLOSED`.

Cross-check every operation from the Scope Declaration (OP-01, OP-02, …) against the
Gate 2 scenario table. This block closes the scope bracket opened by `SCOPE BRACKET: OPENING`.

```
Operation: OP-NN — [name]
Declared scope: [In-scope | Excluded]
Coverage outcome: [covered — scenario IDs referencing this operation in Capability field]
               | [gap — declared In-scope; no Gate 2 scenario references this operation]
               | [out-of-scope — declared Excluded; not expected to appear]
```

If any In-scope operation has no coverage:

```
SCOV-NN: OP-NN ([name])
Status: Coverage gap — declared In-scope in Scope Bracket Opening; no Gate 2 scenario covers it.
Note: This is a gap, not an exclusion. Exclusions appear in the Scope Declaration as "Excluded"
  with rationale. An uncovered In-scope operation means the scenario table does not honor
  the pre-analysis commitment.
```

If all In-scope operations have coverage:
`SCOV-NIL: All declared In-scope operations receive coverage in Gate 2 — pre-analysis commitment honored.`

Write the **terminal bracket block**:

```
╔══ SCOPE BRACKET: CLOSING ══════════════════════════════════════╗
Opening block: SCOPE BRACKET: OPENING (before Gate 1)
Terminal block: Scope Verification (this block)
In-scope operations: [OP-01, OP-02, ...] — covered=[N] / gap=[N]
Excluded operations: [OP-NN, ...] — out-of-scope=[N]   or "none"
SCOPE BRACKET CLOSED — pre-analysis commitment verified
╚════════════════════════════════════════════════════════════════╝
```

A scope declaration without this terminal block is unverified regardless of scenario coverage.

**Output artifact**: `simulations/flow/resilience/{{topic}}-resilience-{{date}}.md`
