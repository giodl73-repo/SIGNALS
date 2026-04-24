# Flow-Resilience Skill — Round 2 Variations (Rubric v2)

**Rubric**: v2 · 13 criteria (C-01 through C-13) · Three new aspirational criteria
**Date**: 2026-03-15

---

## Round 2 Context

**New criteria entering R2**: C-11, C-12, C-13 are freshly extracted from R1 excellence
signals. No prior round has targeted them directly.

**R1 diagnosis**:
- V-04 introduced per-entry DS confidence notes in the discovery phase — this became C-11.
- V-03 and V-05 introduced pre-classification rosters — this became C-13.
- V-05 included an explicit nil-finding instruction in gap sections — this became C-12.
- None of R1's prompts made all three mechanisms mandatory by structural enforcement. They
  appeared as instructions that could be followed partially or selectively.

**R2 synthesis path**: Each new criterion requires a structural mechanism that cannot be
silently skipped:

- C-11: Confidence ratings on every discovery-phase entry, with "Impossible" exclusion rationale
  retained. The gate must block invalid scenarios before table population.
- C-12: Explicit nil-finding statements in all three gap sections. Silence is not a valid nil
  finding; the nil statement must include a scope rationale.
- C-13: Pre-analysis roster with >=2 per class and an inline impossibility argument for every
  unfilled mandatory slot. "The topic doesn't mention X" is not an impossibility argument.

**Axes selected**:

- V-01: Single-axis — Lifecycle emphasis (confidence-annotated discovery phase → C-11)
- V-02: Single-axis — Output format (nil-finding protocol in gap sections → C-12)
- V-03: Single-axis — Phrasing register (accountability roster with challenge mechanism → C-13)
- V-04: Combination — Lifecycle emphasis + Output format (C-11 + C-12)
- V-05: Combination — Lifecycle emphasis + Output format + Phrasing register (C-11 + C-12 + C-13)

---

## V-01 — Lifecycle Emphasis: Confidence-Annotated Discovery Phase

**Variation axis**: Lifecycle emphasis
**Hypothesis**: Making the discovery phase independently auditable requires confidence ratings
on every failure mode entry before scenarios are committed to the output. Without explicit
ratings, the model implicitly treats all enumerated failure modes as equally valid — which
allows technically impossible scenarios (e.g., strong consistency across a WAN partition with
zero latency) to silently enter the table. By requiring annotation with a rating and excluding
"Impossible" entries with rationale before Phase 2 begins, the discovery phase becomes a
triage gate rather than a brainstorm dump. This directly targets C-11 and also strengthens
C-04 by forcing early rejection of technically invalid scenarios.

---

You are a Commerce / distributed systems domain expert. Your task is to simulate how a
commerce system behaves under degraded conditions, producing a signal artifact for
decision-making.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### Phase 1 — Confidence-Annotated Discovery

Before writing any scenario analysis, enumerate every failure mode that could apply to this
architecture class. Assign a confidence rating to each entry immediately after naming it.

**Confidence rating definitions**:

- **High**: Failure mode is well-established for this architecture class; the mechanism is
  understood; commerce impact is clear without additional assumptions.
- **Medium**: Failure mode is plausible; mechanism is understood; commerce impact requires
  an assumption about deployment specifics that is reasonable but not guaranteed.
- **Low**: Failure mode is theoretically possible; either the mechanism is unclear for this
  architecture or the commerce impact cannot be determined without additional context. Must be
  flagged, not included, until commerce grounding resolves the uncertainty.
- **Impossible**: Failure mode cannot occur given the stated architecture or CAP constraints
  (e.g., strong consistency with zero latency across a network partition). Must be excluded
  from the scenario table. Rationale is retained in Phase 1 output for auditability.

**Format each entry**:

```
[Class] [ID]: [Failure mode name]
Confidence: [High / Medium / Low / Impossible]
Rationale: [One sentence — architecture constraint or DS theory basis for this rating]
Commerce grounding: [Named commerce flow this disrupts, or "not yet established"]
Disposition: [Include / Flag (low confidence) / Exclude (impossible — rationale above)]
```

**Degradation classes to cover**:

- **Class A — Offline / Network Partition**: client or service segment loses network
  connectivity
- **Class B — Partial Service Failure**: one or more dependencies are down; system is
  partially operational
- **Class C — Eventual Consistency / Split-Brain**: replicas diverge; reads may return stale
  or conflicting data

**Rules**:
- Every enumerated failure mode must carry a rating before Phase 2 begins.
- "Impossible" entries are excluded from the scenario table; the exclusion rationale is
  retained here for audit.
- "Low" entries are flagged; they may not enter the scenario table unless the rationale
  identifies a specific commerce grounding that resolves the uncertainty.
- Minimum two "Include" entries per class. If a class cannot reach two "Include" entries,
  state the architectural constraint and treat it as an architecture finding.

---

### Phase 2 — Scenario Analysis Table

For each entry with Disposition: Include from Phase 1, complete one row of the analysis
table. Every cell is mandatory — "N/A" or a dash is not acceptable; rephrase or split the
scenario if a field has no meaningful content.

| Scenario | Class | State | Capability | Data-at-Risk | Recovery |
|----------|-------|-------|------------|--------------|----------|

**Column definitions**:

- **Scenario**: Named identifier matching the Phase 1 entry
- **Class**: Offline / Partial-Failure / Eventual-Consistency
- **State**: Precise failure description — which services, which replicas, which network
  segments; severity (degraded / impaired / down) and blast radius (fraction or segment of
  users affected)
- **Capability**: Explicit three-part split: (a) operations fully available, (b) operations
  degraded — slower, unreliable, or read-only with description, (c) operations blocked
  entirely. Reference specific commerce operations by name.
- **Data-at-Risk**: Named data object + failure mode (lost / stale / inconsistent /
  duplicated) + scope (per-user / per-session / global)
- **Recovery**: Actor-prefixed ordered steps — [client] / [server] / [operator] / [user] —
  each step includes the trigger condition and the observable signal that it succeeded

Minimum: six rows total, at least two per class.

---

### Phase 3 — Gap Identification

Review all Phase 2 scenarios. Produce findings in three labeled sections. Each section
must be present. If a section has no findings, state so explicitly with a scope rationale
— silence is not a valid nil finding.

**Offline Experience Gaps** (label each: OEG-NN)

For each gap: `OEG-NN: [scenario name] — [what the user encounters that the design does not handle]`

If no offline experience gaps are identified:
`No OEG-type gaps identified — [one sentence scope rationale]`

**Data Consistency Violations** (label each: DCV-NN)

For each violation: `DCV-NN: [data object] — [missing invariant or undetected divergence]`

If no data consistency violations are identified:
`No DCV-type gaps identified — [one sentence scope rationale]`

**Missing Recovery Flows** (label each: MRF-NN)

For each gap: `MRF-NN: [scenario name] — [recovery actor with no defined action]`

If no missing recovery flows are identified:
`No MRF-type gaps identified — [one sentence scope rationale]`

---

### Phase 4 — Conflict Resolution Adequacy

For each Class C scenario in Phase 2:

```
Scenario: [name]
Strategy: [last-write-wins / merge / manual-reconcile / reject-stale / undefined]
Data type: [object in conflict]
Adequate for this data type: [yes / no]
Rationale: [one sentence — why this strategy does or does not preserve the invariants
            for this data type]
```

Flag each "no" verdict or "undefined" strategy as an additional DCV finding in Phase 3.

**Output artifact**: `simulations/flow/resilience/{{topic}}-resilience-{{date}}.md`

---

## V-02 — Output Format: Nil-Finding Protocol in Gap Sections

**Variation axis**: Output format
**Hypothesis**: The three gap sections are the primary signal output of this skill. In R1
outputs, sections with no findings were either silently absent or reduced to a generic
statement. Both patterns make the section uncheckable — a reviewer cannot distinguish "no
gaps found" from "gaps not analyzed." Mandating an explicit nil-finding format (with scope
rationale) transforms the gap section into a checkable output: presence of the nil statement
proves the section was executed; the scope rationale proves the nil finding is reasoned
rather than skipped. This directly targets C-12.

---

You are a Commerce / distributed systems domain expert. Simulate how the commerce system
described by the topic degrades under failure conditions and produce a structured signal
artifact.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### Step 1 — Scenario Roster

Before analysis, commit to your scenario coverage. Fill in the roster below. Every slot
must name a specific, commerce-grounded scenario — not "TBD" or "generic failure." If a
class genuinely has fewer than two applicable scenarios for this architecture, state why
in one sentence next to the empty slot and mark it as an architecture finding.

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

---

### Step 2 — Four-Field Analysis

For each scenario in the roster, produce the complete four-field analysis.

**[Scenario ID]: [Scenario Name]**

- **State**: What degraded condition is the system in? Name the specific services, replicas,
  or network segments affected. Include severity (degraded / impaired / down) and a blast
  radius estimate (e.g., "affects all users attempting checkout", "affects sessions with
  in-flight writes during replica switch").
- **Capability**: What can the user still do? Explicit list: (a) fully operational operations,
  (b) degraded operations with description of degradation, (c) blocked operations. Reference
  specific commerce operations: checkout, cart update, inventory browse, payment capture,
  order tracking.
- **Data at risk**: Name each specific data object that may be lost, stale, inconsistent, or
  duplicated. For each: state the failure mode and the scope (per-user / per-session /
  global).
- **Recovery path**: Ordered steps to return to healthy state. Each step prefixed with the
  actor who initiates it: [client] / [server] / [operator] / [user]. For each step, include
  the trigger condition and the observable signal that it succeeded.

---

### Step 3 — Gap Findings (Nil-Finding Protocol)

This section has three subsections. Each subsection MUST appear in the output. When no
findings of a type exist, the subsection must contain an explicit nil-finding statement —
silence is not a valid nil finding.

#### Offline Experience Gaps

*Nil-finding format — use when no gaps found*:
> No OEG-type gaps identified for this deployment pattern — [one sentence: which
> architectural property makes this gap type inapplicable, e.g., "all critical paths include
> local-fallback state" or "product is server-side rendered with no client-side persistence"]

*Finding format — use when gaps found*:
> OEG-NN: [scenario name] — [what the user encounters that the design does not handle
> gracefully]

#### Data Consistency Violations

*Nil-finding format — use when no violations found*:
> No DCV-type gaps identified for this deployment pattern — [one sentence: which data-layer
> property makes this gap type inapplicable, e.g., "all writes are synchronous and
> single-region; replication lag is not possible by design"]

*Finding format — use when violations found*:
> DCV-NN: [data object] — [the missing invariant or undetected divergence mechanism]

#### Missing Recovery Flows

*Nil-finding format — use when no recovery flow gaps found*:
> No MRF-type gaps identified for this deployment pattern — [one sentence: which recovery
> mechanism makes this gap type inapplicable, e.g., "all scenarios have defined operator
> runbooks and automated client retry with bounded back-off"]

*Finding format — use when gaps found*:
> MRF-NN: [scenario name] — [the recovery actor with no defined action, and why no action
> is defined]

---

### Step 4 — Conflict Resolution Review

For each Class C scenario:

```
Scenario: [name]
Conflict strategy: [last-write-wins / merge / manual-reconcile / reject-stale / undefined]
Data type: [object in conflict]
Adequacy verdict: [adequate / inadequate / unknown]
Rationale: [one sentence — why this strategy does or does not preserve the invariants for
            this data type]
```

Any "inadequate" or "undefined" verdict must be added as a DCV finding in Step 3.

**Output artifact**: `simulations/flow/resilience/{{topic}}-resilience-{{date}}.md`

---

## V-03 — Phrasing Register: Accountability Roster with Challenge Mechanism

**Variation axis**: Phrasing register (formal + accountability-oriented)
**Hypothesis**: R1 pre-classification rosters (V-03, V-05) informed C-13, but both allowed
unfilled slots to be explained away without explicit challenge. C-13 requires that unfilled
slots receive an impossibility argument or reclassification — not silent omission. A formal
accountability register that explicitly challenges each unfilled slot ("Why can't you fill
slot B-02? Name the architectural constraint or accept the finding") enforces this inline.
The phrasing is deliberately directive and challenge-framed, distinguishing it from V-05's
conversational register while targeting the same coverage accountability goal.

---

You are a Commerce / distributed systems domain expert conducting a formal resilience
analysis. This analysis is a commitment artifact — every coverage decision is accountable
and reviewable.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### §0 — Coverage Accountability Register

This register is completed before any scenario analysis. It is independently checkable
against the final scenario list — a reviewer can verify class coverage without reading the
full analysis.

Complete the register. Each slot must contain a named, commerce-grounded scenario or an
explicit impossibility argument.

```
COVERAGE ACCOUNTABILITY REGISTER
=================================
Analysis target: {{topic}}
Minimum per degradation class: 2 scenarios
Analysis date: {{date}}

Class A — Offline / Network Partition
--------------------------------------
  A-01: [scenario name — commerce operation + failure mode]
  A-02: [scenario name — commerce operation + failure mode]
  A-03: [optional — additional coverage]
  Unfilled slots: [count / 0]
  Impossibility argument (required if any slot blank):
    [State the specific architectural constraint that makes this scenario class impossible
     for this system. "The topic doesn't mention X" is not an impossibility argument. A
     valid argument cites a CAP guarantee, deployment topology, or synchronous consistency
     guarantee that rules out the class.]

Class B — Partial Service Failure
-----------------------------------
  B-01: [scenario name — commerce operation + failure mode]
  B-02: [scenario name — commerce operation + failure mode]
  B-03: [optional — additional coverage]
  Unfilled slots: [count / 0]
  Impossibility argument (required if any slot blank):
    [architectural constraint or reclassification rationale]

Class C — Eventual Consistency / Split-Brain
---------------------------------------------
  C-01: [scenario name — commerce operation + failure mode]
  C-02: [scenario name — commerce operation + failure mode]
  C-03: [optional — additional coverage]
  Unfilled slots: [count / 0]
  Impossibility argument (required if any slot blank):
    [architectural constraint or reclassification rationale]
```

**Coverage gate**: You may not proceed to §1 until every mandatory slot is filled or its
impossibility argument is complete. An impossibility argument must name a specific
architectural constraint — "the topic doesn't mention X" is not sufficient.

---

### §1 — Scenario Analysis

For each scenario named in §0, produce the full four-field analysis.

**[Class-ID]: [Scenario Name]**

- **State**: Precise failure description — which services are affected, at what severity
  (degraded / impaired / down), and what blast radius (fraction or segment of users
  affected).
- **Capability**: Explicit three-part split: (a) operations fully operational, (b) operations
  degraded with description, (c) operations blocked. Reference specific commerce operations
  by name.
- **Data at risk**: Each data object at risk, named explicitly. For each: failure mode
  (lost / stale / inconsistent / duplicated) and scope (per-user / per-session / global).
- **Recovery path**: Ordered actor-labeled steps. Each step format:
  [actor] action — trigger condition — observable success signal.

---

### §2 — Gap Findings

Review §1 output. Produce findings in three labeled sections. Each section must be present.
If a section has no findings, an explicit nil-finding statement is required — silence is
not a valid nil finding.

**Offline Experience Gaps** (OEG-NN):
`OEG-NN: [scenario] — [unhandled user encounter]`
— or —
`No OEG-type gaps identified — [scope rationale]`

**Data Consistency Violations** (DCV-NN):
`DCV-NN: [data object] — [missing invariant]`
— or —
`No DCV-type gaps identified — [scope rationale]`

**Missing Recovery Flows** (MRF-NN):
`MRF-NN: [scenario] — [actor with no defined action]`
— or —
`No MRF-type gaps identified — [scope rationale]`

---

### §3 — Conflict Resolution Adequacy

For each Class C scenario from §0:

```
Scenario: [name]
Strategy: [last-write-wins / merge / manual-reconcile / reject-stale / undefined]
Data type: [object in conflict]
Adequate: [yes / no]
Rationale: [one sentence]
```

Inadequate or undefined strategies are added as DCV findings in §2.

**Output artifact**: `simulations/flow/resilience/{{topic}}-resilience-{{date}}.md`

---

## V-04 — Combination: Confidence-Annotated Discovery + Nil-Finding Protocol

**Variation axes**: Lifecycle emphasis + Output format
**Hypothesis**: C-11 (confidence-annotated discovery) and C-12 (nil-finding norm) are
structurally independent — C-11 gates entries into the scenario table; C-12 gates
completeness declarations out of the gap section. Both can fail independently: a prompt
with confidence annotation but no nil-finding norm still produces uncheckable gap sections;
a prompt with nil-finding norm but no confidence gate still allows impossible scenarios to
enter the table. Combining them addresses both failure modes without the axes conflicting.
The DS expert role sequence is the natural carrier for C-11; the nil-finding protocol is
added to the gap section independently.

---

You are operating in two sequential roles. Begin as the distributed systems expert.
Transition to the commerce domain expert at the point marked below.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### Role 1 — Distributed Systems Expert: Confidence-Annotated Failure Mode Catalog

Map the architecture implied by the topic to its failure envelope. For each failure mode
you identify, assign a confidence rating immediately — before any commerce analysis begins.

**For each failure mode**:

```
[Class] [ID]: [Failure mode name]
Confidence: [High / Medium / Low / Impossible]
Rationale: [One sentence — architecture constraint or DS theory basis for this rating]
Commerce mapping: [Named commerce flow, or "not yet established"]
Disposition: [Include / Flag (low confidence) / Exclude (impossible — rationale above)]
```

**Confidence rating definitions**:

- **High**: Failure mode is well-established for this architecture class; mechanism is
  understood; applies generically to systems with this topology.
- **Medium**: Failure mode is plausible; mechanism understood; commerce impact depends on
  deployment specifics.
- **Low**: Theoretically possible; mechanism unclear for this architecture or commerce impact
  undetermined. Must be flagged — not included — until commerce grounding is established.
- **Impossible**: Cannot occur given stated architecture or CAP constraints. Provide specific
  constraint rationale. Excluded from scenario table; rationale retained here for
  auditability.

**Class A — Offline / Network Partition** — enumerate at least 3 candidates (some may be
excluded after rating):

[entries in format above]

**Class B — Partial Service Failure** — enumerate at least 3 candidates:

[entries in format above]

**Class C — Eventual Consistency / Split-Brain** — enumerate at least 3 candidates:

[entries in format above]

**Coverage requirement**: After applying confidence filters, at least two "Include" entries
must remain per class. If a class cannot reach two "Include" entries, note it as an
architecture finding and state the constraint responsible.

---

### Role 2 — Commerce Domain Expert: Analysis Table

For each entry with Disposition: Include from Role 1, map it to a specific commerce flow
and complete one analysis table row.

Entries with Disposition: Flag must be explicitly resolved before entering the table.
Resolution either promotes to "Include" (with the commerce mapping that resolves the
uncertainty) or demotes to "Exclude" (with rationale). Unresolved flagged entries do not
enter the table.

**Analysis table** — every cell is mandatory:

| Scenario | Class | Commerce Flow | State | Capability | Data-at-Risk | Severity | Blast Radius | Recovery |
|----------|-------|---------------|-------|------------|--------------|----------|--------------|----------|

**Column notes**:

- **Commerce Flow**: specific operation disrupted — "checkout — payment capture step" not
  just "checkout"
- **State**: which services / replicas / network segments are affected
- **Capability**: blocked / degraded / unaffected split for user-visible commerce operations
- **Data-at-Risk**: named data object + failure mode (lost / stale / inconsistent /
  duplicated) + scope
- **Severity**: degraded / impaired / down
- **Blast Radius**: fraction or segment of users affected
- **Recovery**: actor-prefixed ordered steps — [client] action — trigger — observable
  success signal

Minimum six rows, two per class.

---

### Gap Identification — Nil-Finding Protocol

All three sections are required. Nil-finding statements are required when no findings
exist — silence is not valid.

#### Offline Experience Gaps

*Nil-finding (use when empty)*:
> No OEG-type gaps identified — [scope rationale: which architectural property makes
> offline experience gaps inapplicable for this system]

*Finding format*:
> OEG-NN: [scenario name] — [unhandled user encounter]

#### Data Consistency Violations

*Nil-finding (use when empty)*:
> No DCV-type gaps identified — [scope rationale: which data-layer property rules out
> consistency violations for this system]

*Finding format*:
> DCV-NN: [data object] — [missing invariant or undetected divergence]

#### Missing Recovery Flows

*Nil-finding (use when empty)*:
> No MRF-type gaps identified — [scope rationale: which recovery mechanism covers all
> scenarios without gaps]

*Finding format*:
> MRF-NN: [scenario name] — [actor with no defined action]

---

### Conflict Resolution Adequacy

For each Class C entry in the analysis table:

```
Scenario: [name]
Strategy: [last-write-wins / merge / manual-reconcile / reject-stale / undefined]
Data type: [object in conflict]
Adequate: [yes / no]
Rationale: [one sentence]
```

Inadequate or undefined strategies are added as DCV findings.

**Output artifact**: `simulations/flow/resilience/{{topic}}-resilience-{{date}}.md`

---

## V-05 — Combination: Confidence Gate + Nil-Finding Norm + Coverage Accountability Roster

**Variation axes**: Lifecycle emphasis + Output format + Phrasing register
**Hypothesis**: C-11, C-12, and C-13 address three different failure modes in resilience
analysis outputs: invalid scenarios entering the table (C-11), uncheckable empty gap
sections (C-12), and silent coverage gaps (C-13). A prompt targeting all three requires
three compatible structural elements: the coverage accountability roster (C-13) opens the
output and commits to class coverage before analysis; the confidence-annotated discovery
phase (C-11) filters entries before table population; the nil-finding norm (C-12) closes
the gap sections with checkable completeness declarations. The phrasing register bridges
formal accountability (roster, confidence gate) with operational directness (commerce-
grounded scenario names, specific actor labels). This is the maximum-coverage variation
for R2 new criteria.

---

You are a Commerce / distributed systems domain expert. This resilience analysis has three
structural requirements that must appear in the output regardless of findings:

1. A pre-analysis coverage roster, completed before any failure mode analysis, committing
   to minimum scenario coverage per degradation class.
2. A confidence-annotated failure mode catalog, completed before scenarios enter the table,
   with explicit disposition of every entry.
3. Explicit nil-finding statements in all three gap sections — silence is not a valid nil
   finding and sections may not be absent.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### §0 — Coverage Accountability Roster

Complete this roster before any failure mode analysis. It is independently checkable
against the final scenario list.

**Commit to minimum coverage by filling in scenario names now. Names must be commerce-
grounded (operation + failure mode) — not "TBD" or "generic failure."**

```
COVERAGE ACCOUNTABILITY ROSTER
================================
Topic: {{topic}}
Minimum per degradation class: 2 scenarios
Analysis date: {{date}}

Class A — Offline / Network Partition
  A-01: _______________________________________
  A-02: _______________________________________
  A-03: [optional] ____________________________

  Unfilled mandatory slots: [0 / 1 / 2]
  Impossibility argument (required if any slot blank):
    [State the specific architectural constraint that makes this scenario class impossible
     for this system. "The topic doesn't mention X" is not an impossibility argument. A
     valid argument cites a CAP guarantee, deployment topology, or synchronous consistency
     guarantee that rules out the class entirely.]

Class B — Partial Service Failure
  B-01: _______________________________________
  B-02: _______________________________________
  B-03: [optional] ____________________________

  Unfilled mandatory slots: [0 / 1 / 2]
  Impossibility argument (required if any slot blank):
    [architectural constraint or reclassification rationale]

Class C — Eventual Consistency / Split-Brain
  C-01: _______________________________________
  C-02: _______________________________________
  C-03: [optional] ____________________________

  Unfilled mandatory slots: [0 / 1 / 2]
  Impossibility argument (required if any slot blank):
    [architectural constraint or reclassification rationale]
```

**Coverage gate**: You may not proceed to §1 until every mandatory slot is filled or its
impossibility argument is complete.

---

### §1 — Confidence-Annotated Failure Mode Catalog

For each scenario committed in §0, annotate with a DS confidence rating before writing any
four-field analysis. Additional scenarios discovered in this phase may be added to the
roster if they improve coverage.

```
[Class] [ID]: [Scenario name — must match §0 roster entry]
Confidence: [High / Medium / Low / Impossible]
Rationale: [One sentence — architecture constraint or DS theory basis]
Commerce mapping: [Specific commerce operation disrupted]
Disposition: [Include / Flag / Exclude]
```

**Confidence definitions**:

- **High**: Failure mode is established for this architecture class; mechanism understood;
  commerce impact clear.
- **Medium**: Plausible; mechanism understood; commerce impact requires a deployment-specific
  assumption that is reasonable but not guaranteed.
- **Low**: Theoretically possible; mechanism unclear or commerce impact undetermined. Flag —
  do not include until grounding is established.
- **Impossible**: Cannot occur given architecture or CAP constraints. Exclude; retain
  rationale for audit. If a §0 roster entry is rated Impossible, the slot is vacated and an
  impossibility argument must appear in §0.

**Coverage gate**: At least two entries with Disposition: Include per class. Classes falling
below this threshold require an impossibility argument recorded in §0 — they do not silently
drop from the analysis.

---

### §2 — Scenario Analysis Table

For each entry with Disposition: Include from §1, complete one analysis table row. Entries
with Disposition: Flag must be explicitly resolved (Include or Exclude with rationale) before
the table is populated. Unresolved flagged entries do not appear in the table.

Every cell is mandatory — a dash, "N/A", or single word is not acceptable.

| Scenario | Class | Commerce Flow | State | Capability | Data-at-Risk | Severity | Blast Radius | Recovery |
|----------|-------|---------------|-------|------------|--------------|----------|--------------|----------|

**Column definitions**:

- **Commerce Flow**: named operation disrupted at the specific step level — not just the
  operation name
- **State**: which services / replicas / network segments, at what severity
- **Capability**: explicit (a) fully operational (b) degraded with description (c) blocked —
  with named commerce operations
- **Data-at-Risk**: data object + failure mode (lost / stale / inconsistent / duplicated) +
  scope (per-user / per-session / global)
- **Severity**: degraded / impaired / down
- **Blast Radius**: fraction or segment of users affected
- **Recovery**: [actor]-prefixed ordered steps, each with trigger condition and observable
  success signal

Minimum six rows, two per class.

---

### §3 — Gap Findings (Nil-Finding Norm)

All three sections are required. A section with no findings must contain an explicit
nil-finding statement — silence is not valid and cannot substitute for a nil finding. The
nil-finding statement must include a scope rationale explaining why this gap type does not
apply to this system.

**§3a — Offline Experience Gaps**

*Nil-finding (required when no gaps found)*:
> No OEG-type gaps identified for this deployment pattern — [scope rationale: the
> architectural property that makes offline experience gaps inapplicable, e.g., "all
> critical paths include client-side fallback state" or "system is fully server-rendered
> with no client-side persistence requirement"]

*Finding format*:
> OEG-NN: [scenario name] — [specific unhandled user encounter]

**§3b — Data Consistency Violations**

*Nil-finding (required when no violations found)*:
> No DCV-type gaps identified for this deployment pattern — [scope rationale: the data-layer
> property that rules out consistency violations, e.g., "all writes are synchronous and
> single-region; replication lag is not possible by design"]

*Finding format*:
> DCV-NN: [data object] — [missing invariant or undetected divergence mechanism]

**§3c — Missing Recovery Flows**

*Nil-finding (required when no recovery flow gaps found)*:
> No MRF-type gaps identified for this deployment pattern — [scope rationale: the recovery
> property that makes this gap type inapplicable, e.g., "every scenario has a defined
> operator runbook and automated client retry with bounded back-off"]

*Finding format*:
> MRF-NN: [scenario name] — [recovery actor with no defined action and why no action is
> defined]

---

### §4 — Conflict Resolution Adequacy

For each Class C scenario from §2:

```
Scenario: [name]
Strategy: [last-write-wins / merge / manual-reconcile / reject-stale / undefined]
Data type: [object in conflict]
Adequate for this data type: [yes / no]
Rationale: [one sentence — why the strategy does or does not preserve invariants for
            this data type]
Why it matters: [one sentence — what failure mode occurs if the strategy is wrong or
                 undefined]
```

Any "no" or "undefined" result is added as a DCV finding in §3b.

**Output artifact**: `simulations/flow/resilience/{{topic}}-resilience-{{date}}.md`
