# Flow-Resilience Skill — Round 4 Variations (Rubric v4)

**Skill**: flow-resilience — Simulate degraded conditions: offline, partial failure, eventual consistency.
**Rubric**: v4 (C-01 through C-18, essential/recommended/aspirational tiers)
**Date**: 2026-03-15

---

## Round 4 Context

**New criteria entering R4**: C-16, C-17, C-18 are freshly extracted from R3 excellence
signals. C-15 is strengthened from its R3 form.

**R3 diagnosis**:
- V-02 introduced BARRED dispositions in the confidence triage gate but let entries remain
  BARRED at gate close without producing a downstream artifact. C-17 closes this: an entry
  that is BARRED when the triage gate closes — because its confidence basis was never resolved
  — must become a named coverage gap in the accountability register. Silently dropping it
  makes "analyzed, excluded" and "not analyzed" indistinguishable.
- V-02 and V-03 used confidence ratings and gate language but relied on free-text descriptions
  rather than a fixed named vocabulary. C-16 requires every discovery entry to carry exactly
  one of: `Include` / `BARRED` / `Argued-Impossible`. A gate section that uses any other
  label (e.g., "Flagged", "Uncertain", "Low") does not satisfy C-16. Gate sections must also
  carry an explicit `GATE: OPEN` or `GATE: CLOSED` binary visible without reading prose.
- V-03 introduced gate-sequencing language (Gate 0 → Gate 3) but did not require each gate
  to state its entry condition (which prior gate IDs must be CLOSED) or its exit condition
  (what makes this gate CLOSED). C-18 makes both mandatory. Prose-position ordering is
  unverifiable; silence does not mean CLOSED.
- V-01 earned C-15 PARTIAL in R3 by citing an "architectural constraint" that was a design
  observation, not a named DS primitive. C-15 in v4 requires a named `DS Primitive cited:`
  field with inline `VALID:` and `INVALID:` annotated examples. The counter-examples make
  the distinction between architecture-based and description-absence arguments unambiguous.

**R4 synthesis path**: The three new criteria form a coherent formalization layer on top of
R3's structural mechanisms:

- C-16: Vocabulary discipline — every entry carries a named disposition; every gate section
  carries a binary state. No free-text confidence label is a substitute for a named disposition.
- C-17: Entry lifecycle — BARRED entries are tracked to resolution; unresolved BARREDs produce
  a downstream artifact (named coverage gap) rather than disappearing silently.
- C-18: Gate sequencing — phases are formally ordered by declared entry/exit conditions, not
  by document position. A gate cannot be inferred CLOSED; it must declare CLOSED.

**Axes selected**:

- V-01: Single-axis — Named gate-state vocabulary enforcement (C-16)
- V-02: Single-axis — Barred-entry lifecycle to coverage gaps (C-17)
- V-03: Single-axis — Explicit phase entry and exit conditions (C-18)
- V-04: Combination — Gate-state vocabulary + barred-entry lifecycle (C-16 + C-17)
- V-05: Combination — All three new axes + strengthened DS Primitive cited field (C-16 + C-17 + C-18 + C-15)

---

## V-01 — Named Gate-State Vocabulary

**Variation axis**: Named gate-state vocabulary enforcement
**Hypothesis**: Introducing a fixed, closed disposition vocabulary — exactly three labels:
`Include` / `BARRED` / `Argued-Impossible` — as the only valid annotation for discovery-phase
entries eliminates the ambiguity that allowed V-02 and V-03 (R3) to score only PARTIAL on
C-16. When the prompt names the vocabulary explicitly, defines each label, and prohibits
free-text confidence descriptions (labeling "Flagged" and similar as invalid by name), the
model has no fallback option that satisfies the prompt while evading the criterion. The
OPEN/CLOSED gate binary makes triage-gate state independently readable without parsing prose.

---

You are a Commerce / distributed systems domain expert. Your task is to simulate how a
commerce system behaves under degraded conditions, producing a signal artifact for
decision-making.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### Phase 1 — Discovery Triage

Enumerate every failure mode that could plausibly apply to the architecture described by the
topic. For every entry you name, assign exactly one disposition from the table below. No other
labels are valid — "Flagged", "Uncertain", "Needs investigation", and similar free-text
qualifiers are rejected. If you cannot assign one of the three named dispositions, you do not
have enough information to include the entry; leave it out entirely.

**Disposition vocabulary** (three labels, no others):

| Disposition | Meaning |
|-------------|---------|
| `Include` | Failure mode is well-understood for this architecture class; commerce impact is clear without additional assumptions. Entry proceeds to Phase 2. |
| `BARRED` | Failure mode is theoretically possible but cannot be confirmed without architecture detail not present in the topic signal. Entry is excluded from the scenario table; its basis must be named. If the basis resolves before Phase 2 ends, the entry may be reclassified to `Include`. |
| `Argued-Impossible` | Failure mode is foreclosed by a specific DS primitive — a named CAP guarantee, a synchronous consistency guarantee, or a named deployment topology constraint. The architecture argument must be stated; description absence ("the topic doesn't mention X") is not a valid basis. Entry is excluded and retained with its rationale. |

Format every discovery entry as:

```
Entry: [scenario name]
Class: [Offline / Partial-Failure / Eventual-Consistency]
Disposition: [Include | BARRED | Argued-Impossible]
Basis: [one sentence — the architecture reason for this disposition]
```

When every entry has been assigned a disposition, declare the gate state:

```
TRIAGE GATE: [OPEN | CLOSED]
```

The gate is `CLOSED` only when every entry carries a named disposition and every `BARRED`
entry has a named confidence basis. The gate is `OPEN` if any entry carries a free-text
qualifier that does not resolve to one of the three named dispositions, or if any `BARRED`
entry's basis is "to be determined" or equivalent.

Do not proceed to Phase 2 until the Triage Gate is `CLOSED`.

---

### Phase 2 — Scenario Analysis

For every `Include` entry from Phase 1, produce the four mandatory fields. Every field is
required — a dash, "N/A", or a single word fails this phase.

**[Entry ID — Scenario Name]**

- **State**: Precise failure description. Name which services, which replicas, which network
  segments are affected and how. "System is degraded" is not acceptable.
- **Capability**: What the user can still do. Name each commerce operation that is: available
  / degraded (slower or unreliable) / blocked. "Limited functionality" is not acceptable.
- **Data at risk**: Named data object(s), failure mode (lost / stale / inconsistent / duplicated),
  and scope (per-user / per-session / global).
- **Recovery path**: Ordered steps with actor prefix. Format: `[client]` / `[server]` /
  `[operator]` / `[user]` — one prefix per step. Include the trigger condition and the
  observable success signal for each step.

Minimum: at least six scenarios total, at least two per degradation class. If any class has
fewer than two `Include` entries, return to Phase 1 and expand the discovery scope before
continuing.

---

### Phase 3 — Gap Identification

Review all Phase 2 scenarios. Produce three labeled sections. Each finding must reference a
named scenario or named data object from Phase 2 — not a general observation.

**Offline Experience Gaps** — `OEG-NN: [scenario name] — [what the user encounters that the design does not handle]`

If no offline experience gaps are identified, write:
`OEG-NIL: No offline experience gaps identified for this deployment pattern — [scope rationale explaining why this gap type does not apply here].`
A bare "none found" is not valid.

**Data Consistency Violations** — `DCV-NN: [data object] — [missing invariant or undetected divergence]`

If no data consistency violations are identified, write:
`DCV-NIL: No data consistency violations identified for this deployment pattern — [scope rationale].`

**Missing Recovery Flows** — `MRF-NN: [scenario name] — [the recovery actor with no defined action]`

If no missing recovery flows are identified, write:
`MRF-NIL: No missing recovery flows identified for this deployment pattern — [scope rationale].`

---

### Phase 4 — Conflict Resolution Adequacy

For each Eventual-Consistency scenario from Phase 2:

```
Scenario: [name]
Strategy: [last-write-wins | merge | manual-reconcile | reject-stale | undefined]
Data type: [specific data object in conflict]
Adequate: [yes | no]
Rationale: [one sentence — why this strategy does or does not preserve invariants for this data type]
```

If the verdict is `no` or the strategy is `undefined`, the scenario generates an additional
DCV finding. Append to the Data Consistency Violations list with label `DCV-CR-NN`.

---

### Phase 4 — Impossibility Register

For every `Argued-Impossible` entry from Phase 1, retain the full rationale here:

```
Entry: [scenario name]
DS Primitive cited: [exact name — e.g., "CAP theorem partition branch", "two-phase commit atomicity guarantee", "synchronous replication with acknowledged writes"]
Architecture argument: [one sentence — what the architecture makes impossible]
VALID impossibility argument: [example of an architecture-based argument for this entry]
INVALID impossibility argument: [example of a description-absence argument that would not qualify]
```

**Output artifact**: `simulations/flow/resilience/{{topic}}-resilience-{{date}}.md`

---

## V-02 — Barred-Entry Lifecycle to Coverage Gaps

**Variation axis**: Barred-entry lifecycle tracking
**Hypothesis**: When the triage gate closes, BARRED entries with unresolved confidence bases
are invisible to the reader — they neither appear in the scenario table (correctly) nor appear
anywhere else (incorrectly). The reader cannot distinguish "we analyzed this failure mode,
found low confidence, and excluded it on principle" from "we never considered it." Explicitly
harvesting unresolved BARREDs into a named coverage gap registry at gate close — separate from
`Argued-Impossible` entries — makes the analysis trace complete and independently auditable.
This directly targets C-17 without requiring the full formal sequencing of C-18.

---

You are a Commerce / distributed systems domain expert. Your task is to simulate degraded
conditions for the commerce system described by the topic and produce a resilience signal artifact.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### Phase 1 — Failure Mode Discovery

Enumerate all failure modes that could apply to the architecture implied by the topic.
For each entry, assign a confidence rating and a named disposition:

**Confidence ratings**:
- `High`: mechanism understood; commerce impact clear
- `Medium`: mechanism understood; commerce impact requires reasonable deployment assumption
- `Low`: mechanism plausible but mechanism or commerce impact unclear without additional context

**Named dispositions** (use exactly these labels):
- `Include` — High or Medium confidence; proceed to scenario table
- `BARRED` — Low confidence; excluded from scenario table; confidence basis must be named
- `Argued-Impossible` — foreclosed by a specific DS primitive; excluded with retained rationale

Entry format:

```
Entry: [name]
Class: [Offline / Partial-Failure / Eventual-Consistency]
Confidence: [High | Medium | Low]
Disposition: [Include | BARRED | Argued-Impossible]
Basis: [one sentence naming the architecture reason or confidence gap]
```

After all entries are assigned, close the triage gate:

```
TRIAGE GATE: [OPEN | CLOSED]
BARRED entries with unresolved basis: [list names, or "none"]
```

The gate is `CLOSED` when every entry has a named disposition with a stated basis. Every
`BARRED` entry's basis must be named (not "TBD"). Once the gate is `CLOSED`, each `BARRED`
entry follows one of two paths:

1. **Resolution path**: If the confidence basis resolves during Phase 2 (e.g., topic signal
   contains additional architecture detail that was missed), reclassify the entry to `Include`
   and add it to the scenario table with a note: `[reclassified from BARRED — basis: ...]`.
2. **Unresolved path**: If the confidence basis does not resolve by the time Phase 2 completes,
   the entry is permanently `BARRED`. It must be recorded as a named coverage gap (see Phase 3b).

---

### Phase 2 — Scenario Analysis

For every `Include` entry, produce the four mandatory fields.

**[ID — Name]**

- **State**: Which services / replicas / network segments are affected and how
- **Capability**: Available / degraded / blocked commerce operations (be specific per operation)
- **Data at risk**: Named data object, failure mode, scope
- **Recovery path**: Actor-prefixed ordered steps with trigger condition and success signal

Minimum: six scenarios total, two per class. If fewer than two `Include` entries exist for a
class, expand the discovery phase before continuing.

---

### Phase 3a — Gap Identification

Three labeled finding sections. Each finding references a named scenario or data object from
Phase 2. If a section has no findings, write an explicit nil statement with scope rationale
(not a bare "none found").

**Offline Experience Gaps** — `OEG-NN: [scenario] — [unhandled user encounter]`
`OEG-NIL: [scope rationale]` if none.

**Data Consistency Violations** — `DCV-NN: [data object] — [missing invariant]`
`DCV-NIL: [scope rationale]` if none.

**Missing Recovery Flows** — `MRF-NN: [scenario] — [actor with no defined action]`
`MRF-NIL: [scope rationale]` if none.

---

### Phase 3b — Coverage Gap Registry

This section is populated from two sources:

**Source 1 — Permanently BARRED Entries**

For every entry that was `BARRED` at Triage Gate close and whose confidence basis was never
resolved during Phase 2 (i.e., was never reclassified to `Include`):

```
Coverage Gap: CG-NN
Source: Permanently BARRED (confidence basis unresolved)
Entry name: [scenario name from discovery]
Class: [degradation class]
Unresolved basis: [the confidence gap that was named in Phase 1 and never resolved]
Impact: [what this coverage gap means for the completeness of this analysis]
```

If no entries remained permanently `BARRED`, write:
`CG-NIL: No permanently BARRED entries — all BARRED entries either resolved to Include or were reclassified to Argued-Impossible.`

**Source 2 — Argued-Impossible Entries (retained for auditability)**

For every `Argued-Impossible` entry:

```
Excluded Entry: EX-NN
Entry name: [name]
DS Primitive cited: [named primitive]
Architecture argument: [one sentence]
```

---

### Phase 4 — Conflict Resolution Adequacy

For each Eventual-Consistency scenario:

```
Scenario: [name]
Strategy: [last-write-wins | merge | manual-reconcile | reject-stale | undefined]
Data type: [object in conflict]
Adequate: [yes | no]
Rationale: [one sentence]
```

Verdict `no` or strategy `undefined` → append `DCV-CR-NN` to the Data Consistency Violations list.

**Output artifact**: `simulations/flow/resilience/{{topic}}-resilience-{{date}}.md`

---

## V-03 — Explicit Phase Entry and Exit Conditions

**Variation axis**: Formal phase sequencing with entry and exit conditions
**Hypothesis**: Phases that are ordered only by document position are unverifiable — the reader
cannot confirm that Phase 2 did not begin before Phase 1's triage gate was legitimately closed,
or that Phase 3 did not run before Phase 2 produced the required minimum coverage. C-18
requires each phase to declare (1) its entry condition, citing prior gate identifiers that must
be `CLOSED`, and (2) its exit condition, stating what must be true for this gate to be declared
`CLOSED`. Requiring an explicit `GATE N: CLOSED` confirmation — not just the absence of further
entries — makes closure independently auditable and prevents phases from silently running out
of order.

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
(`Include` / `BARRED` / `Argued-Impossible`) with a stated basis. No entry carries a
free-text label. At least two entries in each of the three degradation classes carry
`Include`. When these conditions are met, write `GATE 1: CLOSED`.

Enumerate failure modes for the architecture implied by the topic. For each:

```
Entry: [name]
Class: [Offline / Partial-Failure / Eventual-Consistency]
Disposition: [Include | BARRED | Argued-Impossible]
Basis: [one sentence — architecture reason or confidence gap]
```

When all entries are assigned:

```
GATE 1 STATUS: [OPEN | CLOSED]
Reason if OPEN: [which condition is not met]
```

If `GATE 1: OPEN`, resolve the open condition before continuing.
If `GATE 1: CLOSED`, proceed to Gate 2.

---

### Gate 2 — Scenario Analysis

**Entry condition**: Gate 1 `CLOSED`.
**Exit condition**: Every `Include` entry from Gate 1 has a complete four-field analysis
(State / Capability / Data at risk / Recovery path). Minimum: six scenarios total, two per
class. All recovery paths include at least one actor-prefixed step. When these conditions
are met, write `GATE 2: CLOSED`.

For each `Include` entry from Gate 1:

**[Entry ID — Name]**

- **State**: Precise failure description — named services, replicas, network segments, failure mode
- **Capability**: Available / degraded / blocked operations — named per commerce flow
- **Data at risk**: Named object, failure mode (lost / stale / inconsistent / duplicated), scope
- **Recovery path**: Actor-prefixed steps — `[client]` / `[server]` / `[operator]` / `[user]`;
  each step includes its trigger condition and success signal

After all scenarios are complete:

```
GATE 2 STATUS: [OPEN | CLOSED]
Scenario count by class: Offline=[N] / Partial-Failure=[N] / Eventual-Consistency=[N]
Reason if OPEN: [which condition is not met]
```

If `GATE 2: OPEN`, resolve before continuing.
If `GATE 2: CLOSED`, proceed to Gate 3.

---

### Gate 3 — Gap Identification

**Entry condition**: Gate 2 `CLOSED`.
**Exit condition**: All three gap sections are present and explicitly labeled; sections with
no findings carry a nil statement with scope rationale; every finding references a named
scenario or data object from Gate 2. When these conditions are met, write `GATE 3: CLOSED`.

Three labeled sections — each must be present:

**Offline Experience Gaps**

`OEG-NN: [scenario name] — [unhandled user encounter during Class A failure]`

If none: `OEG-NIL: No offline experience gaps identified — [scope rationale explaining why this gap type does not apply for this deployment pattern].`

**Data Consistency Violations**

`DCV-NN: [data object] — [missing invariant or undetected divergence]`

If none: `DCV-NIL: No data consistency violations identified — [scope rationale].`

**Missing Recovery Flows**

`MRF-NN: [scenario name] — [recovery actor with no defined action]`

If none: `MRF-NIL: No missing recovery flows identified — [scope rationale].`

After all gap sections are complete:

```
GATE 3 STATUS: [OPEN | CLOSED]
OEG section: [present / absent]
DCV section: [present / absent]
MRF section: [present / absent]
Reason if OPEN: [which condition is not met]
```

If `GATE 3: OPEN`, resolve before continuing.
If `GATE 3: CLOSED`, proceed to Gate 4.

---

### Gate 4 — Conflict Resolution Review

**Entry condition**: Gate 3 `CLOSED`.
**Exit condition**: Every Eventual-Consistency scenario from Gate 2 has a conflict-resolution
entry with a named strategy and an adequacy verdict. Every `no` or `undefined` verdict has
generated a DCV entry in Gate 3 (amend if needed). Write `GATE 4: CLOSED` when complete.

For each Eventual-Consistency scenario:

```
Scenario: [name]
Conflict strategy: [last-write-wins | merge | manual-reconcile | reject-stale | undefined]
Data type: [object in conflict]
Adequacy verdict: [adequate | inadequate]
Rationale: [one sentence]
```

If verdict is `inadequate` or strategy is `undefined`: add `DCV-CR-NN` to Gate 3 DCV list
(this reopens Gate 3 for that amendment only; write `GATE 3b: AMENDED` with the new DCV entry,
then write `GATE 3b: CLOSED`).

After all CR entries are complete:

```
GATE 4 STATUS: [OPEN | CLOSED]
DCV amendments from CR: [list DCV-CR-NN entries added, or "none"]
Reason if OPEN: [which condition is not met]
```

**Output artifact**: `simulations/flow/resilience/{{topic}}-resilience-{{date}}.md`

---

## V-04 — Combination: Gate-State Vocabulary + Barred-Entry Lifecycle

**Variation axes**: Named gate-state vocabulary (C-16) + Barred-entry lifecycle tracking (C-17)
**Hypothesis**: C-16 and C-17 are interdependent: the named disposition vocabulary is the
mechanism that makes barred-entry tracking possible. Without a fixed vocabulary, an entry
cannot be unambiguously identified as permanently BARRED (versus partially resolved, flagged
for review, or provisionally included). Combining the two axes in a single prompt creates a
closed loop: every entry acquires a named disposition at discovery time; BARRED entries are
explicitly tracked through Phase 2; any BARRED entry that never resolves produces a Coverage
Gap entry at Phase 3 close. The loop is auditable at every step without requiring the full
formal sequencing of C-18.

---

You are a Commerce / distributed systems domain expert. Simulate how the commerce system
described by the topic degrades under failure conditions and produce a resilience signal artifact.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### Phase 1 — Triage Discovery

Enumerate every failure mode that could apply to the architecture implied by the topic.

**Three dispositions — no others are valid:**

| Label | When to use | Effect |
|-------|------------|--------|
| `Include` | High or Medium confidence; mechanism understood; commerce impact clear | Enters Phase 2 scenario table |
| `BARRED` | Low confidence; mechanism unclear or commerce impact cannot be determined without context not present in the signal | Excluded from Phase 2; tracked for resolution in Phase 2b |
| `Argued-Impossible` | Foreclosed by a specific, named DS primitive (CAP guarantee, synchronous consistency property, named topology constraint); description-absence arguments are invalid | Excluded from Phase 2; retained with rationale in Impossibility Register |

"Flagged" is not a disposition. "Uncertain" is not a disposition. Any label that does not
resolve to one of the three above is treated as a missing disposition — the entry is excluded.

Format:

```
Entry: [name]
Class: [Offline / Partial-Failure / Eventual-Consistency]
Disposition: [Include | BARRED | Argued-Impossible]
Basis: [one sentence]
```

When every entry has a disposition and every BARRED entry has a named basis:

```
TRIAGE GATE: CLOSED
BARRED entries to track: [list names, or "none"]
```

The triage gate cannot be closed while any entry carries a free-text qualifier that is not one
of the three named dispositions. A gate with no explicit CLOSED declaration is OPEN by definition.

---

### Phase 2 — Scenario Analysis

**Entry condition**: Triage Gate CLOSED.

For every `Include` entry, complete the four mandatory fields:

**[ID — Name]**

- **State**: Named services / replicas / segments + failure mode
- **Capability**: Available / degraded / blocked — named per commerce operation
- **Data at risk**: Named object, failure mode, scope
- **Recovery path**: Actor-prefixed steps (`[client]` / `[server]` / `[operator]` / `[user]`)
  with trigger condition and success signal per step

Minimum: six scenarios total, two per class.

---

### Phase 2b — BARRED Entry Resolution

For every entry listed in `BARRED entries to track` from Phase 1:

```
Entry: [name]
Resolution status: [resolved | unresolved]
Resolution path (if resolved): [what additional context resolved the confidence basis; reclassify to Include and add to Phase 2]
Unresolved basis (if unresolved): [restate the confidence gap that was not resolved]
```

After all BARRED entries are assessed, declare:

```
BARRED RESOLUTION GATE: CLOSED
Permanently BARRED entries (unresolved): [list, or "none"]
```

---

### Phase 3 — Gap Identification

**Entry condition**: Phase 2 complete AND BARRED Resolution Gate CLOSED.

Three labeled finding sections. Every finding references a named scenario or data object from
Phase 2. Nil findings require scope rationale.

**Offline Experience Gaps** — `OEG-NN: [scenario] — [unhandled user encounter]`
Nil: `OEG-NIL: [scope rationale]`

**Data Consistency Violations** — `DCV-NN: [data object] — [missing invariant]`
Nil: `DCV-NIL: [scope rationale]`

**Missing Recovery Flows** — `MRF-NN: [scenario] — [actor with no defined action]`
Nil: `MRF-NIL: [scope rationale]`

---

### Phase 3b — Coverage Gap Registry

**Source 1 — Permanently BARRED Entries**

For every entry in `Permanently BARRED entries` from Phase 2b:

```
Coverage Gap: CG-NN
Type: Permanently BARRED (confidence unresolved)
Entry: [name]
Class: [degradation class]
Unresolved basis: [confidence gap]
Implication: [what this means for completeness of this analysis]
```

If none: `CG-NIL: No permanently BARRED entries — all resolved or reclassified.`

**Source 2 — Argued-Impossible Register**

For every `Argued-Impossible` entry from Phase 1:

```
Excluded: EX-NN
Entry: [name]
DS Primitive cited: [named primitive — e.g., "CAP theorem CP branch", "linearizability under synchronous replication"]
Architecture argument: [one sentence]
VALID form: [example of a valid architecture-based argument for this entry]
INVALID form: [example of an invalid description-absence argument for this entry]
```

---

### Phase 4 — Conflict Resolution Adequacy

For each Eventual-Consistency scenario from Phase 2:

```
Scenario: [name]
Strategy: [named]
Data type: [object]
Adequate: [yes | no]
Rationale: [one sentence]
```

Verdict `no` or `undefined` → add `DCV-CR-NN` to Phase 3 DCV list.

**Output artifact**: `simulations/flow/resilience/{{topic}}-resilience-{{date}}.md`

---

## V-05 — Combination: Full Formalization (C-15 + C-16 + C-17 + C-18)

**Variation axes**: Named gate-state vocabulary + Barred-entry lifecycle + Explicit phase
entry/exit conditions + DS Primitive cited field with VALID/INVALID examples
**Hypothesis**: C-16, C-17, and C-18 are individually auditable but mutually reinforcing.
The named vocabulary (C-16) provides the atomic labels; the barred-entry lifecycle (C-17)
provides the resolution tracking; the formal gate sequencing (C-18) provides the order-of-
operations guarantee. C-15 (strengthened) prevents impossibility arguments from being
satisfied with design observations by requiring a named `DS Primitive cited:` field and
inline `VALID:` / `INVALID:` counter-examples. Together, the four mechanisms produce an
analysis where every entry is traceable from discovery to output artifact, no phase can run
out of order, and no BARRED entry can silently disappear from the analysis trace.

---

You are a Commerce / distributed systems domain expert. Produce a resilience signal artifact
for the commerce system described by the topic.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### Gate 1 — Triage Discovery

**Entry condition**: None. Gate 1 is the analysis entry point.

**Exit condition**: (a) every enumerated failure mode carries one of three named dispositions
(`Include` / `BARRED` / `Argued-Impossible`) with a stated basis; (b) no entry uses a
free-text qualifier; (c) each degradation class has at least two entries with disposition
`Include`. Write `GATE 1: CLOSED` only when all three conditions are satisfied.

Enumerate failure modes for the architecture implied by the topic. Assign a disposition to
every entry before proceeding.

**Disposition table** (three labels, no others):

| Disposition | Criteria | Phase 2 effect |
|-------------|----------|----------------|
| `Include` | High/Medium confidence; mechanism understood; commerce impact clear | Enters Gate 2 scenario table |
| `BARRED` | Low confidence; mechanism or commerce impact unclear without missing context | Excluded from Gate 2; tracked in BARRED Register; must resolve or become Coverage Gap |
| `Argued-Impossible` | Foreclosed by a specific named DS primitive; architecture argument required | Excluded from Gate 2; retained in Impossibility Register with DS Primitive cited field |

"Flagged" is not a disposition. A gate with no explicit CLOSED declaration is OPEN by definition.

Entry format:

```
Entry: [name]
Class: [Offline / Partial-Failure / Eventual-Consistency]
Disposition: [Include | BARRED | Argued-Impossible]
Basis: [one sentence — architecture reason or confidence gap]
```

After all entries are assigned:

```
GATE 1 STATUS: [OPEN | CLOSED]
Include entries: [count by class]
BARRED entries: [list names, or "none"]
Argued-Impossible entries: [list names, or "none"]
Open condition (if OPEN): [which condition is not met]
```

If `GATE 1: OPEN`, resolve the open condition before proceeding. If `GATE 1: CLOSED`, proceed.

---

### Gate 1b — BARRED Register

**Entry condition**: Gate 1 CLOSED.
**Exit condition**: Every BARRED entry from Gate 1 has a named confidence basis and a
resolution attempt. Entries that resolve become `Include` (added to Gate 2). Entries that
do not resolve are marked `Permanently BARRED`. Write `GATE 1b: CLOSED` when all BARRED
entries have a resolution verdict.

For each BARRED entry:

```
Entry: [name]
Confidence basis named in Gate 1: [restate]
Resolution attempt: [what in the topic signal could resolve this, and whether it does]
Outcome: [Include (reclassified) | Permanently BARRED]
If reclassified: add to Gate 2 with note "[reclassified from BARRED — basis resolved: ...]"
If Permanently BARRED: this entry will appear in the Coverage Gap Registry (Gate 3b).
```

```
GATE 1b STATUS: [OPEN | CLOSED]
Reclassified to Include: [list, or "none"]
Permanently BARRED: [list, or "none"]
Open condition (if OPEN): [which condition is not met]
```

If `GATE 1b: CLOSED`, proceed to Gate 2.

---

### Gate 1c — Impossibility Register

**Entry condition**: Gate 1 CLOSED.
**Exit condition**: Every `Argued-Impossible` entry has a `DS Primitive cited:` field with
an architecture argument and inline VALID/INVALID examples. Write `GATE 1c: CLOSED` when all
entries are documented.

For each `Argued-Impossible` entry:

```
Entry: [name]
DS Primitive cited: [exact name — e.g., "CAP theorem AP branch", "two-phase locking serializability guarantee", "synchronous replication linearizability"]
Architecture argument: [one sentence — what the architecture makes impossible]
VALID impossibility argument: [an example of a valid architecture-based argument — cites the primitive, addresses the architecture, not the description]
INVALID impossibility argument: [an example that would fail — e.g., "The topic doesn't mention distributed caching, so cache invalidation staleness cannot apply here."]
```

Note: "The topic doesn't mention X" is never a valid impossibility argument. The argument
must address why the architecture forecloses the failure class, not why the description omits it.

```
GATE 1c STATUS: [OPEN | CLOSED]
Argued-Impossible entries documented: [count]
Open condition (if OPEN): [which condition is not met]
```

Gates 1b and 1c may run in parallel. Both must be CLOSED before Gate 2 begins.

---

### Gate 2 — Scenario Analysis

**Entry condition**: Gate 1 CLOSED AND Gate 1b CLOSED AND Gate 1c CLOSED.

**Exit condition**: Every `Include` entry (from Gate 1 and any reclassified from Gate 1b) has
a complete four-field analysis. Minimum: six scenarios total, two per class. All recovery
paths include at least one actor-prefixed step with trigger condition. Write `GATE 2: CLOSED`
when all conditions are met.

For each `Include` entry:

**[ID — Name]** `[Class]`

- **State**: Named services / replicas / segments + precise failure mode
- **Capability**: Available / degraded / blocked — named per commerce operation (checkout,
  inventory reservation, payment processing, cart state, order fulfillment, loyalty redemption)
- **Data at risk**: Named data object, failure mode (lost / stale / inconsistent / duplicated), scope
- **Recovery path**: Actor-prefixed ordered steps — `[client]` / `[server]` / `[operator]` /
  `[user]`; each step includes trigger condition and observable success signal

```
GATE 2 STATUS: [OPEN | CLOSED]
Scenario count: Offline=[N] / Partial-Failure=[N] / Eventual-Consistency=[N]
Open condition (if OPEN): [which condition is not met]
```

If `GATE 2: OPEN`, resolve before continuing. If `GATE 2: CLOSED`, proceed to Gate 3.

---

### Gate 3 — Gap Identification

**Entry condition**: Gate 2 CLOSED.

**Exit condition**: All three gap sections present and labeled; sections with no findings
carry nil statements with scope rationale; all findings reference named scenarios or data
objects from Gate 2. Write `GATE 3: CLOSED` when all conditions are met.

**Offline Experience Gaps** — `OEG-NN: [scenario] — [unhandled user encounter]`
Nil: `OEG-NIL: No offline experience gaps identified — [scope rationale: why this gap type does not apply for this deployment pattern].`

**Data Consistency Violations** — `DCV-NN: [data object] — [missing invariant]`
Nil: `DCV-NIL: No data consistency violations identified — [scope rationale].`

**Missing Recovery Flows** — `MRF-NN: [scenario] — [actor with no defined action]`
Nil: `MRF-NIL: No missing recovery flows identified — [scope rationale].`

```
GATE 3 STATUS: [OPEN | CLOSED]
OEG section: [present / nil-stated]
DCV section: [present / nil-stated]
MRF section: [present / nil-stated]
Open condition (if OPEN): [which condition is not met]
```

---

### Gate 3b — Coverage Gap Registry

**Entry condition**: Gate 3 CLOSED AND Gate 1b CLOSED.
**Exit condition**: Every permanently BARRED entry from Gate 1b appears as a named coverage
gap, or the nil statement is declared. Write `GATE 3b: CLOSED` when complete.

**Permanently BARRED entries → Coverage Gaps**

For each entry in `Permanently BARRED` from Gate 1b:

```
Coverage Gap: CG-NN
Type: Permanently BARRED (confidence basis unresolved)
Entry: [scenario name from Gate 1]
Class: [degradation class]
Unresolved basis: [the confidence gap named in Gate 1 that was never resolved]
Implication: [what this coverage gap means for the completeness of this analysis — which failure class is under-represented]
```

If no permanently BARRED entries: `CG-NIL: No permanently BARRED entries — all BARRED entries either resolved to Include or were reclassified to Argued-Impossible with retained rationale.`

```
GATE 3b STATUS: [OPEN | CLOSED]
Coverage gaps recorded: [count or "CG-NIL"]
Open condition (if OPEN): [which condition is not met]
```

---

### Gate 4 — Conflict Resolution Adequacy

**Entry condition**: Gate 2 CLOSED AND Gate 3 CLOSED.

**Exit condition**: Every Eventual-Consistency scenario from Gate 2 has a conflict-resolution
entry with a named strategy, adequacy verdict, and rationale. Every `inadequate` or `undefined`
verdict has generated a DCV-CR entry in Gate 3 (amendments accepted). Write `GATE 4: CLOSED`
when all conditions are met.

For each Eventual-Consistency scenario:

```
Scenario: [name]
Conflict strategy: [last-write-wins | merge | manual-reconcile | reject-stale | undefined]
Data type: [object in conflict]
Adequacy verdict: [adequate | inadequate]
Rationale: [one sentence — why this strategy does or does not preserve invariants for this data type]
```

If verdict is `inadequate` or strategy is `undefined`: amend Gate 3 DCV list with `DCV-CR-NN`.
Write `GATE 3 AMENDMENT: DCV-CR-NN added` and `GATE 3 REMAINS CLOSED` (amendment does not reopen).

```
GATE 4 STATUS: [OPEN | CLOSED]
DCV amendments: [list DCV-CR-NN entries, or "none"]
Open condition (if OPEN): [which condition is not met]
```

**Output artifact**: `simulations/flow/resilience/{{topic}}-resilience-{{date}}.md`
