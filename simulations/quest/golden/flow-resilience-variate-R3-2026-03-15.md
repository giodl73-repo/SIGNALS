# Flow-Resilience Skill — Round 3 Variations (Rubric v3)

**Skill**: flow-resilience — Simulate degraded conditions: offline, partial failure, eventual consistency.
**Rubric**: v3 (C-01 through C-15, essential/recommended/aspirational tiers)
**Date**: 2026-03-15

---

## Round 3 Context

**New criteria entering R3**: C-14 and C-15 are freshly extracted from R2 excellence signals.
C-11 and C-12 are strengthened from their R2 forms.

**R2 diagnosis**:
- V-01 (R2) introduced confidence annotation but allowed "Low" entries to be flagged and
  retained in the discovery catalog. C-11 v3 strengthens this to a hard bar: low-confidence
  entries are barred from the table until their basis is resolved — flagging alone is no
  longer sufficient.
- V-02 and V-03 (R2) introduced nil-finding statements, but some outputs included bare "none
  found" without scope rationale. C-12 v3 requires the nil statement to explain *why* the
  gap type doesn't apply — not just assert absence.
- V-04 (R2) noted that inadequate conflict-resolution strategies should be added as DCV
  findings — but left the link optional ("flag each 'no' verdict"). C-14 makes it structural:
  the two sections must bidirectionally reference each other; an "inadequate/undefined"
  verdict in CR is always a DCV entry, not a standalone note.
- V-03 (R2) challenged empty roster slots but accepted "the topic doesn't mention X" as an
  impossibility argument. C-15 explicitly rejects description-absence arguments and requires
  a specific DS primitive: a named CAP guarantee, deployment topology constraint, or
  synchronous consistency guarantee.

**R3 synthesis path**: Each new or strengthened criterion requires a structural mechanism
that cannot be silently skipped:

- C-14: A retroactive DCV amendment gate after conflict-resolution analysis. The gate forces
  the model to return to the DCV section and either add the linked entries or explicitly
  confirm no amendment is needed. The link must be named in both directions.
- C-15: The impossibility argument template must include a required "DS Primitive cited:"
  field that accepts only architectural arguments. The template itself rejects description-
  absence arguments by label.
- C-11 (strengthened): "Low confidence" is now a hard bar — the gate is locked until a
  cited basis (architecture constraint or DS theory reference) is provided. "Flagged" is not
  an allowed disposition; only "Include / Exclude / BARRED (pending resolution)" exist.
- C-12 (strengthened): The nil-finding template now requires a scope rationale field. Bare
  "none found" cannot be inserted into the template without completing the rationale field.

**Axes selected**:

- V-01: Single-axis — Lifecycle emphasis (retroactive DCV amendment gate after CR analysis → C-14)
- V-02: Single-axis — Output format (DS-primitive-anchored impossibility template → C-15)
- V-03: Single-axis — Phrasing register (hard gate language on low-confidence entries → C-11 strengthened)
- V-04: Combination — Lifecycle emphasis + Output format (C-14 + C-15)
- V-05: Combination — Lifecycle emphasis + Output format + Phrasing register + Inertia framing
  (C-14 + C-15 + C-11 hard bar + "what the current design doesn't do")

---

## V-01 — Lifecycle Emphasis: Retroactive DCV Amendment Gate

**Variation axis**: Lifecycle emphasis
**Hypothesis**: C-14 requires bidirectional linkage between the conflict-resolution
adequacy section and the DCV gap section. The failure mode is that outputs treat the
CR section as terminal — inadequate strategies are noted there and never cross-referenced
back to the gap tally. The fix is a lifecycle phase that explicitly reopens the DCV
section after CR analysis. An "Amendment Gate" at the end of the CR phase forces the
model to either write the linked DCV entries or confirm with a scope rationale that no
amendment is required. Without this explicit gate, the natural flow treats gap sections
as closed once written.

---

You are a Commerce / distributed systems domain expert. Your task is to simulate how the
commerce system described by the topic degrades under failure conditions and produce a
structured signal artifact.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### Phase 0 — Coverage Roster

Before any analysis, commit to your scenario coverage. Fill in the roster. Every slot must
name a specific, commerce-grounded scenario — not "TBD" or "generic failure." If a class
genuinely has fewer than two applicable scenarios for this architecture, state why in one
sentence and mark the slot as an architecture finding.

```
SCENARIO ROSTER
===============
Class A — Offline / Network Partition (minimum 2):
  A-01: _______________________________________________
  A-02: _______________________________________________
  A-03: (optional) ____________________________________

Class B — Partial Service Failure (minimum 2):
  B-01: _______________________________________________
  B-02: _______________________________________________
  B-03: (optional) ____________________________________

Class C — Eventual Consistency / Split-Brain (minimum 2):
  C-01: _______________________________________________
  C-02: _______________________________________________
  C-03: (optional) ____________________________________
```

You may not proceed to Phase 1 until every mandatory slot is filled or its omission is
explained. Omission explanations must cite an architectural constraint — not topic scope.

---

### Phase 1 — Confidence-Annotated Discovery

For each scenario in the roster, assign a confidence rating before any four-field analysis.

**Confidence rating definitions**:

- **High**: Failure mode is well-established for this architecture class; mechanism understood;
  commerce impact clear.
- **Medium**: Plausible; mechanism understood; commerce impact requires a deployment-specific
  assumption that is reasonable but not guaranteed.
- **Low**: Theoretically possible; mechanism unclear or commerce impact undetermined. Entry is
  **barred from the scenario table**. To lift the bar: provide an architecture constraint or
  DS theory reference that establishes the failure mode for this topology. Flagging alone
  does not satisfy this gate.
- **Impossible**: Cannot occur given stated architecture or CAP constraints. Excluded from
  scenario table; rationale retained here for audit.

**Format each entry**:

```
[Class] [ID]: [Scenario name]
Confidence: [High / Medium / Impossible]
Cited basis: [Architecture constraint or DS theory reference — not a topic-scope statement]
Commerce mapping: [Named commerce operation this scenario disrupts]
Disposition: [Include / Exclude-Impossible / BARRED-Low-[unresolved]]
```

Note: "Low" confidence entries are not included with a flag — they are marked BARRED and
excluded until the cited basis is provided. A BARRED entry that remains unresolved does not
enter Phase 2 and is recorded as a coverage gap.

Minimum two "Include" entries per class after confidence filtering.

---

### Phase 2 — Scenario Analysis

For each "Include" entry from Phase 1, produce the complete four-field analysis.

**[Class-ID]: [Scenario Name]**

- **State**: What degraded condition is the system in? Name the specific services, replicas,
  or network segments affected. Include severity (degraded / impaired / down) and blast
  radius (fraction or segment of users affected).
- **Capability**: Explicit three-part list:
  - (a) Fully operational commerce operations
  - (b) Degraded operations — describe the degradation (slower, unreliable, read-only,
    limited functionality)
  - (c) Blocked operations — list by name
- **Data at risk**: Name each specific data object at risk. For each: failure mode
  (lost / stale / inconsistent / duplicated) and scope (per-user / per-session / global).
- **Recovery path**: Ordered steps, each prefixed with the actor who initiates it:
  [client] / [server] / [operator] / [user]. Include the trigger condition and the
  observable signal that the step succeeded.

---

### Phase 3 — Gap Identification

Produce findings in three labeled sections. Each section must be present. If a section
has no findings, write the explicit nil-finding statement — silence is not valid.

**Offline Experience Gaps** (label each: OEG-NN)

*Finding format*: `OEG-NN: [scenario name] — [what the user encounters that the design does not handle]`

*Nil-finding format — required when no gaps found*:
> No OEG-type gaps identified for this deployment pattern — [scope rationale: the
> architectural property that makes offline experience gaps inapplicable, e.g., "all
> critical paths include local-fallback state" or "product is fully server-rendered with
> no client-side state"]

**Data Consistency Violations** (label each: DCV-NN)

*Finding format*: `DCV-NN: [data object] — [missing invariant or undetected divergence]`

*Nil-finding format — required when no violations found*:
> No DCV-type gaps identified for this deployment pattern — [scope rationale: the
> data-layer property that rules out consistency violations, e.g., "all writes are
> synchronous and single-region; replication lag is not possible by design"]

**NOTE**: This section will be amended in Phase 4. Do not mark it closed before Phase 4
is complete.

**Missing Recovery Flows** (label each: MRF-NN)

*Finding format*: `MRF-NN: [scenario name] — [the recovery actor with no defined action]`

*Nil-finding format — required when no recovery flow gaps found*:
> No MRF-type gaps identified for this deployment pattern — [scope rationale: which
> recovery mechanism covers all scenarios, e.g., "every scenario has a defined operator
> runbook and automated client retry with bounded back-off"]

---

### Phase 4 — Conflict Resolution Adequacy

For each Class C scenario from Phase 2:

```
Scenario: [name]
Strategy: [last-write-wins / merge / manual-reconcile / reject-stale / undefined]
Data type: [object in conflict]
Adequate for this data type: [yes / no]
Rationale: [one sentence — why this strategy does or does not preserve invariants
            for this data type]
```

---

### Phase 4 Amendment Gate — DCV Section Update

After completing every Phase 4 entry above, execute this gate before closing the artifact:

**Step 1**: Count the number of Phase 4 entries where Adequate = "no" or Strategy =
"undefined". Call this N.

**If N > 0**:

Return to the Phase 3 DCV section and add one DCV entry per inadequate or undefined
strategy. Each entry must:

- Be labeled DCV-NN (continuing the DCV sequence from Phase 3)
- Name the Phase 4 scenario that produced it
- State the specific invariant that the inadequate strategy fails to preserve

Use this format:

```
DCV-NN: [data object] — inadequate conflict-resolution strategy detected in Phase 4
  Source: Phase 4 scenario "[scenario name]"
  Strategy found: [strategy]
  Invariant violated: [the data-type invariant this strategy fails to preserve]
```

**If N = 0**:

Write the following confirmation below Phase 4:

```
DCV Amendment Gate: No amendments required — all Phase 4 strategies rated adequate.
No DCV entries added by this gate.
```

Both outcomes close the gate. The artifact is not complete until the amendment gate has
been executed and its output is present.

**Output artifact**: `simulations/flow/resilience/{{topic}}-resilience-{{date}}.md`

---

## V-02 — Output Format: DS-Primitive-Anchored Impossibility Template

**Variation axis**: Output format
**Hypothesis**: C-15 requires that impossibility arguments cite a specific distributed
systems primitive — a named CAP guarantee, deployment topology constraint, or synchronous
consistency guarantee. The persistent failure mode is that models default to description-
absence arguments: "the topic doesn't mention caching" or "the system description is too
simple for this class." These arguments address the topic description, not the architecture.
An output format that contains a required "DS Primitive cited:" field — where the field
label itself specifies what is and is not acceptable — makes description-absence arguments
structurally visible as incomplete. A reviewer can scan the field and reject any entry that
cites topic scope rather than architecture constraint without reading the full rationale.

---

You are a Commerce / distributed systems domain expert. Simulate how the commerce system
described by the topic degrades under failure conditions and produce a structured signal
artifact.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### Step 1 — Coverage Accountability Register

This register is completed before any scenario analysis. It is independently checkable
against the final scenario list.

**Register format — filled slot**:

```
[Class] [Slot-ID]: [Scenario name — commerce operation + failure mode]
Status: Filled
```

**Register format — unfilled slot** (use only when a class genuinely cannot reach two
scenarios for architectural reasons):

```
[Class] [Slot-ID]: [UNFILLED]
Status: Unfilled
Impossibility argument:
  DS Primitive cited: [Name a specific CAP theorem guarantee, deployment topology
    constraint, or synchronous consistency guarantee that rules out this scenario class
    for this system. Example: "CAP theorem — CP systems trade partition tolerance; in
    a single-datacenter synchronous-replication deployment, Class C scenarios cannot
    occur because the architecture guarantees linearizability by construction."
    INVALID: "the topic does not mention replication" or "the system description is
    too simple for this class" — description absence is not an architectural argument.]
  Architectural basis: [one sentence explaining how the DS primitive forecloses this
    scenario class in this specific deployment topology]
```

If you cannot complete the "DS Primitive cited" field with a real architectural argument,
the slot must be filled — the scenario class is not impossible, it is underdetermined.

```
COVERAGE ACCOUNTABILITY REGISTER
=================================
Analysis target: {{topic}}
Minimum per degradation class: 2 scenarios

Class A — Offline / Network Partition
  A-01: [filled or unfilled per format above]
  A-02: [filled or unfilled per format above]
  A-03: [optional]

Class B — Partial Service Failure
  B-01: [filled or unfilled per format above]
  B-02: [filled or unfilled per format above]
  B-03: [optional]

Class C — Eventual Consistency / Split-Brain
  C-01: [filled or unfilled per format above]
  C-02: [filled or unfilled per format above]
  C-03: [optional]
```

**Coverage gate**: You may not proceed to Step 2 until every mandatory slot is filled or
contains a complete impossibility argument with a DS Primitive cited. An unfilled slot
with a description-absence argument ("topic doesn't mention X") is not a complete
impossibility argument — it is an incomplete slot that blocks the gate.

---

### Step 2 — Confidence-Annotated Failure Mode Discovery

For each filled scenario from the register, annotate with a confidence rating before the
four-field analysis.

```
[Class] [ID]: [Scenario name]
Confidence: [High / Medium / Low / Impossible]
Cited basis: [Specific architecture constraint or DS theory reference — one sentence.
  "High confidence" requires naming the failure mechanism and why it applies to this
  topology. "Impossible" must cite the same DS Primitive format used in Step 1.]
Commerce mapping: [Named commerce flow this scenario disrupts]
Disposition: [Include / BARRED (low — [unresolved basis]) / Exclude (impossible)]
```

Low-confidence entries are barred from the analysis table. A barred entry requires a
cited basis to be promoted to "Include" — the entry either resolves to Include or remains
barred and is recorded as a coverage gap.

---

### Step 3 — Four-Field Analysis Table

For each "Include" entry from Step 2, complete one row. Every cell is mandatory — no
dashes, no "N/A," no single-word answers.

| Scenario | Class | State | Capability | Data-at-Risk | Recovery |
|----------|-------|-------|------------|--------------|----------|

**Column definitions**:

- **Scenario**: Named identifier matching the Step 1 register
- **Class**: Offline / Partial-Failure / Eventual-Consistency
- **State**: Precise failure description — named services / replicas / network segments;
  severity label (degraded / impaired / down); blast radius (fraction or segment of users
  affected)
- **Capability**: Three-part split — (a) fully operational operations by name, (b) degraded
  operations with description of degradation, (c) blocked operations by name. All three
  parts present.
- **Data-at-Risk**: Named data object + failure mode (lost / stale / inconsistent /
  duplicated) + scope (per-user / per-session / global)
- **Recovery**: Actor-prefixed ordered steps — [client] / [server] / [operator] / [user]
  — each step includes trigger condition and observable success signal

Minimum six rows, two per class.

---

### Step 4 — Gap Findings

All three sections required. Nil-finding statements required when no findings exist.

**Offline Experience Gaps** (OEG-NN)

*Finding*: `OEG-NN: [scenario name] — [specific unhandled user encounter]`

*Nil-finding* (required when empty):
> No OEG-type gaps identified for this deployment pattern — [scope rationale: which
> architectural property makes offline experience gaps inapplicable for this system]

**Data Consistency Violations** (DCV-NN)

*Finding*: `DCV-NN: [data object] — [missing invariant or undetected divergence mechanism]`

*Nil-finding* (required when empty):
> No DCV-type gaps identified for this deployment pattern — [scope rationale: which
> data-layer property rules out consistency violations for this system]

**Missing Recovery Flows** (MRF-NN)

*Finding*: `MRF-NN: [scenario name] — [recovery actor with no defined action and why]`

*Nil-finding* (required when empty):
> No MRF-type gaps identified for this deployment pattern — [scope rationale: which
> recovery property makes this gap type inapplicable for this system]

---

### Step 5 — Conflict Resolution Adequacy

For each Class C scenario in the analysis table:

```
Scenario: [name]
Strategy: [last-write-wins / merge / manual-reconcile / reject-stale / undefined]
Data type: [object in conflict]
Adequate for this data type: [yes / no]
Rationale: [one sentence — why this strategy does or does not preserve the invariants
            for this data type]
```

Any "no" or "undefined" result must be added as a DCV finding in Step 4. The DCV entry
must cite this Step 5 entry as its source:

```
DCV-NN: [data object] — inadequate or undefined conflict-resolution strategy
  Source: Step 5 — scenario "[name]"
  Strategy: [strategy]
  Invariant failure: [the invariant this strategy fails to preserve]
```

**Output artifact**: `simulations/flow/resilience/{{topic}}-resilience-{{date}}.md`

---

## V-03 — Phrasing Register: Hard Gate Language on Low-Confidence Entries

**Variation axis**: Phrasing register (formal / gate-enforcing)
**Hypothesis**: R2's confidence annotation (V-01, V-04) used conditional language for
low-confidence entries: "must be flagged, not included, until commerce grounding resolves
the uncertainty." C-11 v3 removes the conditionality — low-confidence entries are barred,
not flagged, and the bar requires a cited basis to lift, not a commerce-grounding note.
Formal gate language — using GATE CLOSED / GATE OPEN framing with explicit lift conditions
— makes the barrier structurally distinct from a soft annotation. A reviewer can scan for
GATE CLOSED entries and verify that each one is either resolved (with cited basis) or still
barred (and excluded from the table). The phrasing register also enforces that scope-
absence ("topic doesn't mention X") is an invalid impossibility argument by labeling it
explicitly as such in the template.

---

You are a Commerce / distributed systems domain expert conducting a formal resilience
analysis. This analysis is a gate-controlled commitment artifact — each phase has explicit
entry and exit conditions that must be satisfied before the next phase begins.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### Gate 0 — Pre-Analysis Coverage Commitment

**Entry condition**: None (this is the first gate).
**Exit condition**: Every mandatory scenario slot is filled, or an impossibility argument
with a cited DS primitive is recorded for every unfilled slot.

Complete the coverage commitment table. A slot is one of:

- **Filled**: Commerce-grounded scenario name (operation + failure mode)
- **Argued Impossible**: Requires a "DS Primitive cited" entry (see format below)
- **OPEN**: Not yet analyzed — blocks exit from Gate 0; you may not proceed

```
COVERAGE COMMITMENT TABLE
==========================
Class A — Offline / Network Partition
  A-01: [Filled: scenario name] or [Argued Impossible] or [OPEN — blocks gate]
  A-02: [Filled: scenario name] or [Argued Impossible] or [OPEN — blocks gate]
  A-03: [optional]

Class B — Partial Service Failure
  B-01: [Filled: scenario name] or [Argued Impossible] or [OPEN — blocks gate]
  B-02: [Filled: scenario name] or [Argued Impossible] or [OPEN — blocks gate]
  B-03: [optional]

Class C — Eventual Consistency / Split-Brain
  C-01: [Filled: scenario name] or [Argued Impossible] or [OPEN — blocks gate]
  C-02: [Filled: scenario name] or [Argued Impossible] or [OPEN — blocks gate]
  C-03: [optional]
```

**Argued Impossible format** (required for each impossibility claim):

```
Slot [Class-ID]: Argued Impossible
DS Primitive cited: [Name the specific CAP theorem guarantee, deployment topology
  constraint, or synchronous consistency guarantee that architecturally forecloses this
  class. VALID EXAMPLES: "CAP — CP guarantee in single-datacenter synchronous replication
  forecloses partition-tolerance scenarios by construction." INVALID: "The topic doesn't
  mention X." "The system is described as simple." Description absence is not an
  architectural argument.]
Architectural closure: [One sentence — how the named primitive makes this class impossible
  for this specific deployment topology, not for this topic description]
```

Gate 0 is CLOSED until all OPEN slots are resolved. Impossibility arguments that cite
description absence rather than a DS primitive are treated as OPEN slots — the argument
is incomplete.

**Gate 0 status**: [OPEN / CLOSED — confirmed when all slots are filled or argued impossible
with a DS primitive]

---

### Gate 1 — Confidence Triage

**Entry condition**: Gate 0 status = CLOSED.
**Exit condition**: Every scenario in the coverage table has a confidence rating with a
cited basis. No "Low" entries remain unresolved. No entry is in "Flagged" status — flagging
is not a valid disposition.

For each filled scenario from Gate 0, produce:

```
[Class] [ID]: [Scenario name]
Confidence: [High / Medium / Impossible]
Cited basis: [One sentence — the architecture constraint or DS theory reference that
  supports this rating. For High: name the failure mechanism and why it applies to this
  topology. For Medium: name the deployment-specific assumption required. For Impossible:
  cite the DS primitive using Gate 0 Argued Impossible format.]

GATE STATUS: [OPEN — LOW CONFIDENCE / CLOSED — INCLUDE / CLOSED — EXCLUDE IMPOSSIBLE]
```

**GATE OPEN — LOW CONFIDENCE** means:
- Entry is barred from Gate 2 scenario table
- To lift the bar: provide an architecture constraint or DS theory reference that establishes
  this failure mode for this topology as "Medium" or "High"
- If the bar cannot be lifted: the entry is demoted to Exclude and recorded as a coverage gap

Valid dispositions after Gate 1:
- **CLOSED — INCLUDE**: enters Gate 2 scenario table
- **CLOSED — EXCLUDE IMPOSSIBLE**: excluded; rationale retained from Gate 0
- **GATE OPEN — LOW CONFIDENCE**: barred; resolution required before table entry

No other dispositions exist. "Flagged" is not a disposition.

Gate 1 is CLOSED when every entry has a CLOSED disposition, or every OPEN entry has a
recorded resolution attempt (Include with lifted basis, or Exclude with coverage gap note).

---

### Gate 2 — Scenario Analysis

**Entry condition**: Gate 1 status = CLOSED.
**Exit condition**: Every "CLOSED — INCLUDE" entry from Gate 1 has a complete four-field
analysis row in the table below. No missing cells.

| Scenario | Class | State | Capability | Data-at-Risk | Recovery |
|----------|-------|-------|------------|--------------|----------|

**Column enforcement**:

- **State**: services / replicas / network segments named; severity (degraded / impaired /
  down); blast radius (fraction or segment of users affected). Missing any element: gate
  remains open for this row.
- **Capability**: three-part split — (a) fully operational operations by name, (b) degraded
  operations with degradation description, (c) blocked operations by name. Missing any part:
  gate remains open for this row.
- **Data-at-Risk**: data object named; failure mode (lost / stale / inconsistent / duplicated)
  named; scope (per-user / per-session / global) named. Missing any element: gate remains
  open for this row.
- **Recovery**: actor-prefixed steps ([client] / [server] / [operator] / [user]); trigger
  condition per step; observable success signal per step. Missing any element: gate remains
  open for this row.

Minimum six rows. Gate 2 is CLOSED when all rows are complete.

---

### Gate 3 — Gap Identification

**Entry condition**: Gate 2 status = CLOSED.
**Exit condition**: All three gap sections are present. Sections with no findings carry
an explicit nil-finding with scope rationale. Bare "none found" without scope rationale
leaves the gate OPEN for that section.

**Offline Experience Gaps** (OEG-NN)

Gate 3a status: [OPEN / CLOSED]

*Finding*: `OEG-NN: [scenario name] — [specific unhandled user encounter]`

*Nil-finding* (closes gate 3a when no findings exist — scope rationale is mandatory):
> No OEG-type gaps identified for this deployment pattern — [scope rationale: which
> architectural property makes offline experience gaps inapplicable; bare "none found"
> does not close this gate]

**Data Consistency Violations** (DCV-NN)

Gate 3b status: [OPEN / CLOSED]
**NOTE**: This gate reopens after Gate 4. Do not mark CLOSED until Gate 4 amendment is
complete.

*Finding*: `DCV-NN: [data object] — [missing invariant or undetected divergence]`

*Nil-finding*:
> No DCV-type gaps identified for this deployment pattern — [scope rationale]

**Missing Recovery Flows** (MRF-NN)

Gate 3c status: [OPEN / CLOSED]

*Finding*: `MRF-NN: [scenario name] — [actor with no defined action and why]`

*Nil-finding*:
> No MRF-type gaps identified for this deployment pattern — [scope rationale]

---

### Gate 4 — Conflict Resolution Adequacy

**Entry condition**: Gate 3 status = CLOSED on gates 3a and 3c (3b remains open).
**Exit condition**: Every Class C scenario has a CR entry. DCV amendment is complete.
Gate 3b is CLOSED.

For each Class C scenario:

```
Scenario: [name]
Strategy: [last-write-wins / merge / manual-reconcile / reject-stale / undefined]
Data type: [object in conflict]
Adequate for this data type: [yes / no]
Rationale: [one sentence]
```

**DCV Amendment** — required after all CR entries are written:

For every entry where Adequate = "no" or Strategy = "undefined":

```
DCV-NN: [data object] — conflict-resolution strategy [inadequate / undefined]
  Gate 4 source: scenario "[name]", strategy "[strategy]"
  Invariant violated: [the data-type invariant this strategy fails to preserve]
```

After amendments, update Gate 3b status to CLOSED. If no amendments were required:

```
Gate 4 DCV Amendment: CLOSED — no inadequate or undefined strategies found.
Gate 3b updated to: CLOSED
```

Gate 4 is CLOSED when: all CR entries written + DCV amendment executed + Gate 3b CLOSED.

**Output artifact**: `simulations/flow/resilience/{{topic}}-resilience-{{date}}.md`

---

## V-04 — Combination: Lifecycle Emphasis + Output Format (C-14 + C-15)

**Variation axes**: Lifecycle emphasis + Output format
**Hypothesis**: C-14 (bidirectional CR-DCV linkage) and C-15 (DS-primitive impossibility
arguments) are structurally independent and compatible: C-15 applies in the coverage roster
(Gate 0) and confidence triage (Phase 1); C-14 applies in the CR adequacy phase (Phase 4)
and its retroactive amendment of the DCV section (Phase 4 Amendment Gate). The lifecycle
axis governs when the amendment happens; the output format axis governs what the
impossibility template requires. Neither axis interferes with the other. Combined, they
address both R3 new criteria in a single variation. The nil-finding and confidence-bar
mechanisms from R2 are included at their v3-strengthened levels: low-confidence entries
barred (not flagged); nil-findings require scope rationale (not bare "none found").

---

You are operating in two sequential roles. Begin as the distributed systems expert.
Transition to the commerce domain expert at the point marked below.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### §0 — Coverage Accountability Register

Complete this register before any failure mode analysis. It is independently checkable
against the final scenario list.

**Filled slot format**:

```
[Class] [ID]: [Scenario name — commerce operation + failure mode]
Status: Filled
```

**Unfilled slot format** (use only when architectural argument forecloses the class):

```
[Class] [ID]: UNFILLED
DS Primitive cited: [The specific CAP theorem guarantee, deployment topology constraint,
  or synchronous consistency guarantee that makes this failure class architecturally
  impossible for this system. VALID: "CAP — CP guarantee with synchronous single-region
  replication forecloses network-partition scenarios by construction." INVALID: "The
  topic doesn't mention distributed caching." Description absence is not an architectural
  argument — only architectural constraints are valid.]
Architectural closure: [One sentence — how the DS primitive forecloses this class for
  this specific topology, not for this topic description]
```

```
COVERAGE ACCOUNTABILITY REGISTER
=================================
Topic: {{topic}}
Minimum per degradation class: 2 scenarios

Class A — Offline / Network Partition
  A-01: [filled or unfilled per format above]
  A-02: [filled or unfilled per format above]
  A-03: [optional]

Class B — Partial Service Failure
  B-01: [filled or unfilled per format above]
  B-02: [filled or unfilled per format above]
  B-03: [optional]

Class C — Eventual Consistency / Split-Brain
  C-01: [filled or unfilled per format above]
  C-02: [filled or unfilled per format above]
  C-03: [optional]
```

Coverage gate: you may not proceed to §1 until every mandatory slot is filled or contains
a complete impossibility argument with a DS Primitive cited. An impossibility argument
citing description absence is incomplete — it does not close the gate.

---

### Role 1 — Distributed Systems Expert: Confidence-Annotated Failure Mode Catalog

**§1 — Confidence Triage**

For each filled scenario from §0, annotate with a DS confidence rating before any four-
field analysis.

```
[Class] [ID]: [Scenario name — must match §0 entry]
Confidence: [High / Medium / Low / Impossible]
Cited basis: [One sentence — architecture constraint or DS theory reference. High requires
  naming the failure mechanism. Medium requires naming the deployment-specific assumption.
  Low requires noting what is undetermined. Impossible must use the DS Primitive format
  from §0.]
Commerce mapping: [Named commerce flow this scenario disrupts]
Disposition: [Include / BARRED (low — resolution required) / Exclude (impossible)]
```

**Confidence definitions**:

- **High**: Failure mode well-established for this architecture class; mechanism understood;
  commerce impact clear without additional assumptions.
- **Medium**: Plausible; mechanism understood; commerce impact requires a deployment-specific
  assumption that is reasonable but not guaranteed.
- **Low**: Theoretically possible; mechanism unclear or commerce impact undetermined.
  **Disposition: BARRED** — not flagged. Entry may not enter §2 table until an architecture
  constraint or DS theory reference is provided as cited basis. Flagging alone does not
  satisfy this gate.
- **Impossible**: Cannot occur given stated architecture or CAP constraints. Disposition:
  Exclude. Rationale retained here for audit. DS Primitive must be cited per §0 format.

Coverage requirement: two "Include" entries per class after triage. Classes falling below
this threshold are recorded as coverage gaps in §0 with the architectural constraint
responsible.

---

### Role 2 — Commerce Domain Expert: Analysis and Gap Identification

**§2 — Scenario Analysis Table**

For each "Include" entry from §1, complete one row. Flagged entries must be explicitly
resolved (promoted to Include with cited basis, or demoted to Exclude with coverage gap
note) before the table is populated. BARRED entries that remain unresolved do not enter
the table.

Every cell is mandatory — no dashes, no "N/A," no single-word entries.

| Scenario | Class | Commerce Flow | State | Capability | Data-at-Risk | Severity | Blast Radius | Recovery |
|----------|-------|---------------|-------|------------|--------------|----------|--------------|----------|

**Column definitions**:

- **Commerce Flow**: named operation at the specific step level — "checkout — payment
  capture step" not just "checkout"
- **State**: named services / replicas / network segments affected
- **Capability**: (a) fully operational commerce operations by name / (b) degraded operations
  with description / (c) blocked operations by name — all three parts required
- **Data-at-Risk**: named data object + failure mode (lost / stale / inconsistent /
  duplicated) + scope (per-user / per-session / global)
- **Severity**: degraded / impaired / down
- **Blast Radius**: fraction or segment of users affected; a qualifier is required
- **Recovery**: [actor]-prefixed ordered steps, each with trigger condition and observable
  success signal

Minimum six rows, two per class.

---

**§3 — Gap Identification (Nil-Finding Norm)**

All three sections required. Nil-finding statements required when no findings exist; the
nil-finding must include a scope rationale — bare "none found" does not satisfy this norm.

**NOTE on DCV section**: This section will be amended in §4. Do not mark it closed until
§4 Amendment Gate is executed.

**Offline Experience Gaps** (OEG-NN)

*Finding*: `OEG-NN: [scenario name] — [specific unhandled user encounter]`

*Nil-finding* (required when empty):
> No OEG-type gaps identified for this deployment pattern — [scope rationale: the
> architectural property that makes offline experience gaps inapplicable for this system]

**Data Consistency Violations** (DCV-NN) — OPEN pending §4 Amendment Gate

*Finding*: `DCV-NN: [data object] — [missing invariant or undetected divergence]`

*Nil-finding* (required when empty):
> No DCV-type gaps identified for this deployment pattern — [scope rationale]

**Missing Recovery Flows** (MRF-NN)

*Finding*: `MRF-NN: [scenario name] — [actor with no defined action and why]`

*Nil-finding* (required when empty):
> No MRF-type gaps identified for this deployment pattern — [scope rationale]

---

**§4 — Conflict Resolution Adequacy + DCV Amendment Gate**

For each Class C scenario in §2:

```
Scenario: [name]
Strategy: [last-write-wins / merge / manual-reconcile / reject-stale / undefined]
Data type: [object in conflict]
Adequate for this data type: [yes / no]
Rationale: [one sentence — why this strategy does or does not preserve invariants
            for this data type]
Why it matters: [one sentence — what failure mode occurs if the strategy is wrong or
                 undefined]
```

**§4 Amendment Gate** — execute after all CR entries are written:

Count entries where Adequate = "no" OR Strategy = "undefined". Call this N.

**If N > 0**: Return to §3 DCV section and add one DCV entry per inadequate or undefined
strategy. Each entry:

```
DCV-NN: [data object] — conflict-resolution strategy inadequate/undefined
  §4 source: scenario "[name]", strategy "[strategy]"
  Invariant violated: [the data-type invariant this strategy fails to preserve]
```

**If N = 0**: Write below §4:

```
§4 Amendment Gate: CLOSED — no inadequate or undefined strategies found.
DCV section: no amendments required.
```

The DCV section is not finalized until the Amendment Gate is executed.

**Output artifact**: `simulations/flow/resilience/{{topic}}-resilience-{{date}}.md`

---

## V-05 — Combination: Lifecycle Emphasis + Output Format + Phrasing Register + Inertia Framing

**Variation axes**: Lifecycle emphasis + Output format + Phrasing register + Inertia framing
**Hypothesis**: R3's full set of changes — C-14 (CR→DCV feedback), C-15 (DS-primitive
impossibility), C-11 hard bar, C-12 scope rationale — plus one new axis not yet explored:
inertia framing. "Inertia framing" makes the status-quo design's absence explicit in each
scenario: before asking what the system can do in a degraded state, ask what the current
design DOES NOT do. This surfaces the implicit gap between the scenario and the existing
design, which is the gap the resilience analysis is meant to find. For C-08 and C-14, the
inertia frame makes the inadequacy of current conflict-resolution strategies visible as a
contrast: "The current design uses last-write-wins. For inventory counts, LWW is inadequate
because oversell is not detectable at write time." Inertia framing also strengthens C-05
commerce grounding by anchoring scenarios in what a real commerce system currently does —
or fails to do — rather than describing a hypothetical failure in the abstract.

---

You are a senior Commerce / distributed systems engineer who has spent years operating
high-traffic retail platforms. You know what these systems do when they fail — and more
importantly, you know what the CURRENT DESIGN fails to do when things go wrong.

Your job in this analysis is to expose what the system doesn't handle. Not what it does —
what it leaves unhandled.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### Step 0 — Coverage Commitment (Before Any Analysis)

Before you think about individual scenarios, claim your territory. Fill in the roster.
Every slot must name a specific commerce failure — the operation, the failure mode, the
user impact at one line of description.

If you can't fill a slot, don't leave it blank — argue why, but the argument has to be
architectural, not descriptive. "The topic doesn't mention caching" is not a reason a
slot can't be filled. "This system uses synchronous single-region writes with no
replication, which means by CAP's consistency guarantee there is no partition-tolerant
read path and Class C scenarios are architecturally foreclosed" — that's an argument.

```
SCENARIO ROSTER
===============
Class A — Offline / Network Partition (need at least 2):
  A-01: _______________________________________________
  A-02: _______________________________________________
  A-03: (optional) ____________________________________

  Any slots you cannot fill? [yes / no]
  If yes — DS Primitive that forecloses this class:
    [Name the specific CAP guarantee, topology constraint, or synchronous consistency
     guarantee. If you cannot name one, fill the slot — the class is not impossible,
     it is unexplored.]

Class B — Partial Service Failure (need at least 2):
  B-01: _______________________________________________
  B-02: _______________________________________________
  B-03: (optional) ____________________________________

  Any slots you cannot fill? [yes / no]
  If yes — DS Primitive that forecloses this class: [architectural argument]

Class C — Eventual Consistency / Split-Brain (need at least 2):
  C-01: _______________________________________________
  C-02: _______________________________________________
  C-03: (optional) ____________________________________

  Any slots you cannot fill? [yes / no]
  If yes — DS Primitive that forecloses this class: [architectural argument]
```

---

### Step 1 — Confidence Check

Before writing any scenario, rate each one. Be honest — if you don't actually know whether
this failure mode applies to this architecture, say so. But "low confidence" means it stays
out of the table until you can give a real architectural basis for including it.

```
[ID]: [Scenario name]
Confidence: [High / Medium — these enter the table / Low — barred until basis established]
Cited basis: [One sentence — name the failure mechanism and why it applies here.
  High confidence without a named mechanism is not high confidence.]
Commerce operation disrupted: [specific operation name]
```

**Low confidence = barred from the table**. Not flagged, not conditionally included, not
noted as uncertain. Barred. To lift the bar: provide an architecture constraint or DS
theory reference that establishes this failure mode for this topology. If you can't lift
the bar, record it as a coverage gap and move on.

---

### Step 2 — Scenario Analysis (With Inertia Frame)

For each scenario that passed the confidence check, work through the four fields. But
for each scenario, start with the inertia frame: what does the CURRENT DESIGN do — or
fail to do — in this condition? That gap is what the analysis is looking for.

**[Scenario ID]: [Scenario Name]**

**What the current design does in this condition** (inertia frame):
> [One sentence describing what the current design does — or specifically does not do —
> when this failure occurs. Example: "The current design has no client-side cart
> persistence, so a network partition during checkout causes silent session loss with
> no user notification." This is the status quo you are analyzing against.]

**State**: What degraded condition is the system actually in? Name the services,
replicas, or network segments affected. Include severity (degraded / impaired / down)
and blast radius (what fraction or segment of users is affected — a range or qualifier
is required; "some users" is not sufficient).

**What can the user still do?**: Be specific. Name each commerce operation that remains
fully available, each that is degraded (and describe the degradation), and each that is
blocked entirely. "Limited functionality" is not an answer.

**What data is at risk?**: Name each specific data object. For each: what is the failure
mode (lost / stale / inconsistent / duplicated) and what is the scope (per-user /
per-session / global)?

**Recovery path — who does what, in order**: Write each step on its own line. Name who
initiates it: [client], [server], [operator], or [user]. Name the trigger that fires the
step. Name the observable signal that the step succeeded.

---

### Step 3 — Name the Gaps

Review your table. For each of the three finding types, list what you found. The inertia
frame from Step 2 makes this easier — the gap is often right there in the "what the
current design doesn't do" line.

If you found nothing in a category, say so explicitly with a scope rationale — *why*
does this gap type not apply here? "No offline experience gaps" without an explanation
of why leaves the reader unable to check your work.

**Offline experience gaps** (OEG-NN)

What happens to the user during Class A scenarios that the current design leaves
unhandled? Think: blank screens, spinner that never resolves, silent data loss,
no way to recover cart state.

*Finding*: `OEG-NN: [scenario name] — [specific unhandled user encounter]`

*Nil-finding* (required when no gaps — scope rationale is mandatory):
> No OEG-type gaps — [one sentence: the architectural property that makes offline
> experience gaps inapplicable for this system, e.g., "all critical paths include
> client-side fallback state; no silent data loss is possible by design"]

**Data consistency violations** (DCV-NN)

Where does the system not have the machinery to detect or resolve inconsistency?
Think: inventory oversell, duplicate orders, stale loyalty balances, conflicting cart
states after reconnect.

**NOTE**: This section stays open until Step 4 is complete. Conflict-resolution
inadequacies found in Step 4 will be added here.

*Finding*: `DCV-NN: [data object] — [missing invariant or undetected divergence]`

*Nil-finding* (required when no violations — scope rationale is mandatory):
> No DCV-type gaps — [one sentence: the data-layer property that rules out consistency
> violations for this system]

**Missing recovery flows** (MRF-NN)

Where does the system just not have a path back? No retry, no reconcile UI, no operator
action defined. Name the scenario and the actor who needs to act but has no defined action.

*Finding*: `MRF-NN: [scenario name] — [actor with no defined action, and why no
action is defined]`

*Nil-finding* (required when no gaps — scope rationale is mandatory):
> No MRF-type gaps — [one sentence: the recovery property that makes this gap type
> inapplicable for this system]

---

### Step 4 — Split-Brain Scenarios: What the Current Design Does vs. What It Should Do

For each eventual-consistency scenario from your roster, answer one question first:

> What does the current design do when two replicas disagree — and is that the right
> choice for this data type?

This is the inertia frame for split-brain analysis. The current strategy might be
last-write-wins by default (because that's what most caches do). But for inventory
counts, LWW means the most recent write wins regardless of whether it captured all
concurrent decrements — which is how you oversell.

```
Scenario: [name]
What the current design does in a conflict: [current strategy — or "undefined: no
  conflict-resolution policy is explicitly specified for this data type"]
Data in conflict: [specific data object]
Is the current strategy adequate for this data type?: [yes / no]
Why it matters: [one sentence — what goes wrong if the strategy is wrong or undefined]
```

**After completing all entries above — DCV Amendment**:

For every entry where "Is the current strategy adequate" = "no" OR current strategy =
"undefined": add a DCV entry to Step 3. The entry must cite this Step 4 entry as its
source and the inertia frame as the basis.

```
DCV-NN: [data object] — current conflict-resolution strategy is [inadequate / undefined]
  Step 4 source: scenario "[name]"
  Current strategy: [strategy]
  What the design doesn't do: [the invariant the current strategy fails to enforce for
    this data type]
```

If no amendments are required:

```
Step 4 DCV Amendment: complete — no inadequate or undefined strategies found.
DCV section closed.
```

**Output artifact**: `simulations/flow/resilience/{{topic}}-resilience-{{date}}.md`
