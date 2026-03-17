# Flow-Resilience Skill — Round 7 Variations (Rubric v7)

**Skill**: flow-resilience — Simulate degraded conditions: offline, partial failure, eventual consistency.
**Rubric**: v7 (C-01 through C-27, essential/recommended/aspirational tiers)
**Date**: 2026-03-15

---

## Round 7 Context

**New criteria entering R7**: C-25, C-26, and C-27 are freshly extracted from R6 excellence signals.

**R6 diagnosis**:
- V-01 (R6) introduced typed nil identifiers with unique numeric suffixes (`OEG-NIL-1`). C-25
  tightens this by closing the nil lifecycle: a nil finding has two states — ACTIVE (declared,
  gap type absent) and SUPERSEDED (downstream analysis later identified a gap in the same
  category). When a Gate 4 amendment generates `DCV-CR-01` in a section that held `DCV-NIL-1`,
  the nil must be annotated `DCV-NIL-1: SUPERSEDED by DCV-CR-01`. Without the SUPERSEDED
  annotation, a live nil and a live gap coexist with no audit trail. When no supersessions
  occur, an explicit "no supersessions" confirmation closes the nil lifecycle log.
- V-03 (R6) introduced `GATE 1b` as a BARRED-entry resolution pass, handling the path where
  an entry's confidence basis is never resolved (permanently BARRED → CG entry via RULE
  BARRED-CG). C-26 handles the inverse: when a BARRED entry's basis is subsequently satisfied
  and the entry is promoted to Include, that promotion is recorded under a labeled sub-gate
  `GATE 1b: RESOLVED` naming the entry ID, the satisfied basis, the resolution mechanism, and
  the new disposition. Without this sub-gate, a scenario appearing in the Include column may
  have started BARRED with no trace of the promotion path.
- V-03 (R6) placed named conditional rules in a preamble section before Gate 1. C-27 requires
  those rules to appear in a discrete, named RULE REGISTRY with unique IDs, so all rules are
  enumerable from a single section without traversing gate prose. Gate sections that invoke
  linkage behavior cite rules by registry ID rather than restating the conditional logic.
  A template where rules are correct in form (satisfying C-24) but scattered inline fails
  C-27: inline rules are not independently enumerable and cannot be cited by ID.

**R7 synthesis path**:

- C-25: Nil lifecycle closure — nil findings have two states; supersession annotates the nil
  and cites the replacing finding ID; a Nil Supersession Log records all lifecycle events.
- C-26: Confidence resolution sub-gate — BARRED-to-Include promotions are auditable through
  a labeled sub-gate that names the entry, the satisfied basis, and the re-closed gate status.
- C-27: Rule registry enumeration — the complete rule set is declared in one discrete section;
  gate sections cite rules by registry ID, preventing rule duplication and enabling audit.

**Axes selected**:

- V-01: Single-axis — Nil-Finding Supersession Protocol (C-25)
- V-02: Single-axis — Confidence Triage Resolution Sub-Gate (C-26)
- V-03: Single-axis — Named Rule Block Registry (C-27)
- V-04: Combination — Nil Supersession Protocol + Confidence Resolution Sub-Gate (C-25 + C-26)
- V-05: Combination — All three new axes + full R6 formalization (C-25 + C-26 + C-27 + C-15 through C-24)

---

## V-01 — Nil-Finding Supersession Protocol

**Variation axis**: Typed nil finding lifecycle — ACTIVE / SUPERSEDED states with explicit
annotation and a Nil Supersession Log
**Hypothesis**: A typed nil identifier (C-22) proves queryability; a supersession annotation
(C-25) proves lifecycle integrity. V-01 R6 established `OEG-NIL-1` as a run-unique typed
identifier. C-25 asks: what happens to that identifier when downstream analysis discovers a
gap in the same category? Without a SUPERSEDED annotation, the nil stands alongside the gap
finding — the reader cannot tell whether the nil was examined and overruled, or simply not
updated. V-01 R7 closes the nil lifecycle: every nil is born ACTIVE, and becomes SUPERSEDED
when a downstream finding in the same gap category is produced. The supersession cites the
finding ID that replaced it. A Nil Supersession Log at the end of Phase 4 records all
lifecycle transitions or confirms none occurred. The single axis in V-01 is the nil lifecycle
mechanism; the base structure is the same four-phase analysis from R6 V-01 to isolate it.

---

You are a Commerce / distributed systems domain expert. Your task is to simulate how a
commerce system behaves under degraded conditions and produce a signal artifact.

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
| `Argued-Impossible` | Foreclosed by a specific DS primitive — named CAP theorem guarantee, synchronous consistency property, or named topology constraint. Description absence is not a valid basis. Retained with rationale. |

"Flagged", "Uncertain", and similar free-text qualifiers are not dispositions.

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
has a stated basis, and each degradation class has at least two `Include` entries.

---

### Phase 2 — Scenario Analysis

For every `Include` entry from Phase 1, produce the four mandatory fields. At least six
scenarios total; at least two per degradation class.

**[Entry ID — Scenario Name]** `[Class]`

- **State**: Precise failure description — which services, replicas, or segments are affected.
- **Capability**: For each commerce operation relevant to the scenario, state whether it is
  `available` / `degraded` / `blocked`. Reference at least two of: checkout, inventory
  reservation, payment processing, cart state, order fulfillment, loyalty redemption.
- **Data at risk**: Named data object, failure mode (lost / stale / inconsistent / duplicated),
  scope (per-user / per-session / global).
- **Recovery path**: Ordered steps with actor prefix — `[client]` / `[server]` / `[operator]` /
  `[user]`. Each step names its trigger condition and observable success signal.

---

### Phase 3 — Gap Identification

**Typed Nil-Finding Identifier Protocol**

Every nil finding carries:

1. A gap-type prefix: `OEG-NIL` (offline experience gap), `DCV-NIL` (data consistency
   violation), `MRF-NIL` (missing recovery flow).
2. A run-level unique numeric suffix: `-1`, `-2`, etc. Required even when only one nil of
   that type exists in this run.
3. A scope rationale explaining why this gap type does not apply.

Format: `OEG-NIL-1: No offline experience gaps identified — [scope rationale].`

**Nil Lifecycle**

Each typed nil identifier has two lifecycle states:

| State | Meaning |
|-------|---------|
| `ACTIVE` | Nil declared; gap type confirmed absent for this deployment pattern. Default state at declaration. |
| `SUPERSEDED` | Downstream analysis (Phase 4 or later) identified a gap in the same category, rendering the nil obsolete. |

A nil is ACTIVE until explicitly marked SUPERSEDED. When Phase 4 generates a DCV-CR-NN
finding in a section that held `DCV-NIL-N`, update the nil:

```
DCV-NIL-1: SUPERSEDED by DCV-CR-01
  [Nil declared ACTIVE in Phase 3; superseded when DCV-CR-01 added in Phase 4]
```

The supersession annotation must cite the superseding finding ID. A nil declaration and a gap
finding of the same type coexisting without a SUPERSEDED marker on the nil is an audit-trail
failure.

**Offline Experience Gaps**

`OEG-NN: [scenario name] — [what the user encounters that the design does not handle]`

If none: `OEG-NIL-1: No offline experience gaps identified — [scope rationale].`
Lifecycle: ACTIVE (until superseded by a downstream OEG finding)

**Data Consistency Violations**

`DCV-NN: [data object] — [missing invariant or undetected divergence]`

If none: `DCV-NIL-1: No data consistency violations identified — [scope rationale].`
Lifecycle: ACTIVE (Phase 4 may generate DCV-CR-NN findings that supersede this nil)

**Missing Recovery Flows**

`MRF-NN: [scenario name] — [the recovery actor with no defined action]`

If none: `MRF-NIL-1: No missing recovery flows identified — [scope rationale].`
Lifecycle: ACTIVE (until superseded by a downstream MRF finding)

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
Consistency Violations. If the DCV section held `DCV-NIL-N`, write the supersession
annotation on that nil:

```
DCV-NIL-N: SUPERSEDED by DCV-CR-NN
  [Nil declared ACTIVE in Phase 3; superseded when DCV-CR-NN added in Phase 4]
DCV-CR-NN: [data object] — [missing invariant or undetected divergence]
  Triggered by: Phase 4 CR entry "[scenario name]" — strategy [undefined/inadequate]
```

**Nil Supersession Log**

After all CR entries are assessed, write the Nil Supersession Log. This log closes the nil
lifecycle for this analysis run.

```
NIL SUPERSESSION LOG
─────────────────────────────────────────────────────
OEG-NIL-N: [ACTIVE | SUPERSEDED by OEG-F-NN]
DCV-NIL-N: [ACTIVE | SUPERSEDED by DCV-CR-NN]
MRF-NIL-N: [ACTIVE | SUPERSEDED by MRF-NN]
─────────────────────────────────────────────────────
Total nils declared: [N]
Total supersessions: [N]
[If N=0: "No supersessions — all declared nils remain ACTIVE."]
```

The Nil Supersession Log is mandatory. Its absence means the nil lifecycle was not closed.
When zero supersessions occur, the "no supersessions" confirmation is the closure record.

**Output artifact**: `simulations/flow/resilience/{{topic}}-resilience-{{date}}.md`

---

## V-02 — Confidence Triage Resolution Sub-Gate

**Variation axis**: Labeled sub-gate for BARRED-to-Include promotions during triage resolution
**Hypothesis**: R6 V-03 introduced Gate 1b to handle BARRED entries — testing whether their
confidence basis could be resolved. The gate handled the permanently-BARRED path cleanly
(C-17: recorded as coverage gap). C-26 addresses the path R6 did not formalize: when a
BARRED entry's basis IS resolved and the entry IS promoted to Include, that promotion has no
labeled sub-gate. A scenario that appears in the scenario table as Include may have started
BARRED with no trace of when or why the barrier was lifted. V-02 adds `GATE 1b: RESOLVED`
as a labeled sub-gate for every BARRED-to-Include promotion, naming the entry ID, the
confidence basis that was satisfied, how it was satisfied, and the new disposition. The gate
then re-closes with the resolution on record. The single axis in V-02 is Gate 1b: RESOLVED;
the base structure is the four-gate analysis with BARRED resolution from R6 V-03.

---

You are a Commerce / distributed systems domain expert. Simulate how the commerce system
described by the topic behaves under degraded conditions and produce a signal artifact.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

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
Reason if OPEN: [specific blocking condition — entry name, unmet minimum, or outstanding basis]
```

If `GATE 1: CLOSED`, proceed to Gate 1b.

---

### Gate 1b — BARRED Triage Resolution

**Entry condition**: Gate 1 `CLOSED`.
**Exit condition**: Every BARRED entry from Gate 1 has a resolution verdict — either
promoted to Include or confirmed permanently BARRED. Write `GATE 1b: CLOSED`.

For each BARRED entry, attempt to resolve the confidence basis using the topic signal and
architecture inferences:

```
Entry: [name]
Confidence basis: [restate from Gate 1]
Resolution attempt: [what in the topic signal or architecture addresses this basis]
Outcome: [Include — basis resolved | Permanently BARRED — basis not resolved]
```

**When Outcome is `Include — basis resolved`**, record the promotion under a labeled
resolution sub-gate immediately after that entry:

```
GATE 1b: RESOLVED
Entry promoted: [name]
Previous disposition: BARRED
Confidence basis: [the basis that was previously unresolved]
Basis satisfied by: [specific signal, architecture inference, or named assumption]
New disposition: Include
Applies to Gate 2: yes — this entry enters Gate 2 scenario analysis
GATE 1b RESOLUTION STATUS: CLOSED — promotion on record
```

A BARRED entry that silently appears in the Gate 2 scenario table without a
`GATE 1b: RESOLVED` sub-gate record has no auditable promotion path.

**When Outcome is `Permanently BARRED`**, record the coverage gap:

```
Coverage Gap queued: CG-NN
Entry: [name] / Class: [class] / Unresolved basis: [confidence gap]
This entry will appear in Gate 3b Coverage Gap Registry.
```

**When Gate 1b has no BARRED entries to process:**

```
GATE 1b: NO ENTRIES — Gate 1 produced no BARRED entries.
GATE 1b STATUS: CLOSED
```

**Summary block:**

```
GATE 1b STATUS: [OPEN | CLOSED]
BARRED-to-Include upgrades: [list entry names + sub-gate labels, or "none"]
Permanently BARRED: [list names, or "none"]
Coverage gaps queued (CG-NN): [list, or "none"]
Reason if OPEN: [specific unresolved entry name]
```

If `GATE 1b: CLOSED`, proceed to Gate 2. Include entries promoted via `GATE 1b: RESOLVED`
are treated as Include entries in Gate 2.

---

### Gate 2 — Scenario Analysis

**Entry condition**: Gate 1 `CLOSED` AND Gate 1b `CLOSED`.
**Exit condition**: Every `Include` entry (from Gate 1 and promoted via Gate 1b) has a
complete four-field analysis. Minimum: six scenarios total, two per class.
Write `GATE 2: CLOSED`.

**[Entry ID — Name]** `[Class]`

- **State**: Precise failure description — named services, replicas, segments, failure mode
- **Capability**: Available / degraded / blocked for each named commerce operation
  (checkout, inventory reservation, payment processing, cart state, order fulfillment)
- **Data at risk**: Named object, failure mode (lost / stale / inconsistent / duplicated), scope
- **Recovery path**: Actor-prefixed ordered steps — `[client]` / `[server]` / `[operator]` /
  `[user]`; each step includes trigger condition and observable success signal

```
GATE 2 STATUS: [OPEN | CLOSED]
Scenario count: Offline=[N] / Partial-Failure=[N] / Eventual-Consistency=[N]
Entries from Gate 1b RESOLVED promotions included: [list, or "none"]
Reason if OPEN: [specific entry missing or coverage minimum unmet]
```

If `GATE 2: CLOSED`, proceed to Gate 3 and Gate 3b.

---

### Gate 3 — Gap Identification

**Entry condition**: Gate 2 `CLOSED`.
**Exit condition**: All three gap sections present and labeled; nil findings carry scope
rationale; all findings reference named Gate 2 scenarios or data objects. Write `GATE 3: CLOSED`.

**Offline Experience Gaps**

`OEG-NN: [scenario name] — [unhandled user encounter during offline failure]`
Nil: `OEG-NIL: No offline experience gaps identified — [scope rationale].`

**Data Consistency Violations**

`DCV-NN: [data object] — [missing invariant or undetected divergence]`
[Gate 4 may append DCV-CR-NN entries here via the CR-DCV linkage]
Nil: `DCV-NIL: No data consistency violations identified — [scope rationale].`

**Missing Recovery Flows**

`MRF-NN: [scenario name] — [recovery actor with no defined action]`
Nil: `MRF-NIL: No missing recovery flows identified — [scope rationale].`

```
GATE 3 STATUS: [OPEN | CLOSED]
OEG section: [present | nil-stated]
DCV section: [present | nil-stated]
MRF section: [present | nil-stated]
Reason if OPEN: [specific section absent or finding not linked to named Gate 2 artifact]
```

If `GATE 3: CLOSED`, proceed to Gate 3b and Gate 4 in parallel.

---

### Gate 3b — Coverage Gap Registry

**Entry condition**: Gate 1b `CLOSED` AND Gate 3 `CLOSED`.
**Exit condition**: Every CG-NN queued from permanently BARRED entries appears as a named
coverage gap. Write `GATE 3b: CLOSED`.

```
Coverage Gap: CG-NN
Entry: [scenario name from Gate 1]
Class: [degradation class]
Unresolved basis: [confidence gap that was never resolved in Gate 1b]
```

If no permanently BARRED entries were produced:
`CG-NIL: No permanently BARRED entries in Gate 1b — no coverage gaps recorded.`

```
GATE 3b STATUS: [OPEN | CLOSED]
Coverage gaps recorded: [count, or "CG-NIL"]
```

---

### Gate 4 — Conflict Resolution Adequacy

**Entry condition**: Gate 3 `CLOSED`.
**Exit condition**: Every Eventual-Consistency scenario from Gate 2 has a CR entry; all
`inadequate` or `undefined` verdicts have generated `DCV-CR-NN` amendments to Gate 3.
Write `GATE 4: CLOSED`.

```
CR-NN: [scenario name]
Conflict strategy: [last-write-wins | merge | manual-reconcile | reject-stale | undefined]
Data type: [object in conflict]
Adequacy verdict: [adequate | inadequate]
Rationale: [one sentence]
```

If verdict is `inadequate` or strategy is `undefined`:

```
GATE 3: REOPENED — triggering finding: CR-NN / [brief description]
DCV-CR-NN: [data object] — [missing invariant from inadequate/undefined strategy]
Triggered by: CR-NN
GATE 3[a/b/c]: AMENDED
Status: CLOSED
Amendment applied: DCV-CR-NN added to Data Consistency Violations
```

If all CR verdicts are `adequate` and strategies are defined:

```
No CR-DCV linkage triggered. All CR verdicts adequate; all strategies defined.
GATE 3 ORIGINAL CLOSURE CONFIRMED.
```

```
GATE 4 STATUS: [OPEN | CLOSED]
CR entries assessed: [count]
DCV amendments appended: [list DCV-CR-NN entries, or "none"]
Reason if OPEN: [specific EC scenario without CR entry, or pending amendment]
```

**Output artifact**: `simulations/flow/resilience/{{topic}}-resilience-{{date}}.md`

---

## V-03 — Named Rule Block Registry

**Variation axis**: Discrete enumerable RULE REGISTRY section; gate sections cite rules by
registry ID rather than restating conditional logic inline
**Hypothesis**: R6 V-03 placed two named rules (`RULE CR-DCV`, `RULE BARRED-CG`) in a
`Template Linkage Rules` preamble. These rules satisfied C-24 (named conditional rules in
explicit if-then form) but not C-27, because they were defined in a single block at the top
but gated sections restated partial conditions inline when invoking them ("RULE CR-DCV
trigger point — for each CR entry where verdict is `inadequate`..."). C-27 requires a
stricter separation: the registry declares rules once with unique IDs; gate sections invoke
rules by citing their ID without restating the trigger condition. This keeps the registry the
single source of truth for all conditional linkage behavior and makes the rule set enumerable
in isolation. V-03 adds `RULE-ID` as the canonical identifier field, adds a registry status
marker (`REGISTRY CLOSED` before Gate 1), and replaces inline trigger-point prose in gate
sections with rule citations (`per RULE-CR-DCV`). The single axis is the registry structure;
the base is the four-gate analysis from R6 V-03.

---

You are a Commerce / distributed systems domain expert. Simulate how the commerce system
described by the topic behaves under degraded conditions and produce a signal artifact.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### RULE REGISTRY

All conditional linkage rules for this analysis template are declared below. Rules are
identified by their registry ID (`RULE-CR-DCV`, `RULE-BARRED-CG`, etc.). Gate sections
invoke rules by citing their registry ID — they do not restate the trigger condition.

No cross-section linkage may be applied without a registry entry or an inline declaration
(see Inline Declaration Protocol below). The registry is closed before Gate 1 opens.

---

```
RULE-ID:  RULE-CR-DCV
Trigger:  Adequacy verdict is `inadequate` OR Conflict strategy is `undefined`
          (Gate 4 CR entries)
Action:   1. Reopen Gate 3 under a labeled sub-gate (GATE 3a, 3b, 3c, ...).
          2. Append DCV-CR-NN to Gate 3 Data Consistency Violations.
          3. Re-close the sub-gate with amendment record citing this rule ID.
IDs used: DCV-CR-01, DCV-CR-02, ... (one per trigger instance)
Scope:    Gate 4 → Gate 3
```

```
RULE-ID:  RULE-BARRED-CG
Trigger:  Entry remains Permanently BARRED after Gate 1b (confidence basis never resolved)
Action:   1. Append CG-NN to Gate 3b Coverage Gap Registry.
          2. Cite RULE-BARRED-CG in the CG-NN record.
IDs used: CG-01, CG-02, ... (one per permanently barred entry)
Scope:    Gate 1b → Gate 3b
```

**Inline Declaration Protocol**: If a cross-section linkage arises during analysis that is
not covered by a registry entry, declare it inline at first application:

```
RULE-INLINE-[N] (declared inline):
Trigger: [condition]
Action:  [cross-section action]
```

Inline-declared rules apply from their declaration point forward and are enumerable by
post-analysis registry audit.

```
REGISTRY STATUS: CLOSED
Rules declared: RULE-CR-DCV, RULE-BARRED-CG
Inline rules: [none at registry close — may be added inline during analysis]
```

Gate 1 may not open before `REGISTRY STATUS: CLOSED` is written.

---

### Gate 1 — Failure Mode Discovery

**Entry condition**: `REGISTRY STATUS: CLOSED`.
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
Reason if OPEN: [specific blocking condition]
```

If `GATE 1: CLOSED`, proceed to Gate 1b.

---

### Gate 1b — BARRED Register

**Entry condition**: Gate 1 `CLOSED`.
**Exit condition**: Every BARRED entry from Gate 1 has a resolution verdict.
Write `GATE 1b: CLOSED`.

```
Entry: [name]
Confidence basis: [restate from Gate 1]
Resolution attempt: [what in the topic signal could resolve this, and whether it does]
Outcome: [Include (reclassified) | Permanently BARRED]
```

For each `Outcome: Permanently BARRED` — per **RULE-BARRED-CG**:

```
RULE-BARRED-CG invoked: CG-NN queued for Gate 3b
Entry: [name] / Class: [class] / Unresolved basis: [confidence gap]
```

```
GATE 1b STATUS: [OPEN | CLOSED]
Reclassified to Include: [list, or "none"]
Permanently BARRED: [list, or "none"]
RULE-BARRED-CG triggers queued: [list CG-NN IDs, or "none"]
Reason if OPEN: [specific unresolved entry]
```

If `GATE 1b: CLOSED`, proceed to Gate 2.

---

### Gate 2 — Scenario Analysis

**Entry condition**: Gate 1 `CLOSED` AND Gate 1b `CLOSED`.
**Exit condition**: Every `Include` entry has a complete four-field analysis. Minimum:
six scenarios total, two per class. Write `GATE 2: CLOSED`.

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
Reason if OPEN: [specific entry missing or coverage minimum unmet]
```

If `GATE 2: CLOSED`, proceed to Gate 3.

---

### Gate 3 — Gap Identification

**Entry condition**: Gate 2 `CLOSED`.
**Exit condition**: All three gap sections present and labeled; nil findings carry scope
rationale; all findings reference named Gate 2 scenarios or data objects. Write `GATE 3: CLOSED`.

Note: **RULE-CR-DCV** (Gate 4) may reopen Gate 3 to append DCV-CR-NN entries. These
amendments create labeled sub-gates; Gate 3's original CLOSED status is preserved.
When invoking RULE-CR-DCV from Gate 4, cite the rule ID — do not restate the condition.

**Offline Experience Gaps**

`OEG-NN: [scenario name] — [unhandled user encounter during offline failure]`
Nil: `OEG-NIL: No offline experience gaps identified — [scope rationale].`

**Data Consistency Violations**

`DCV-NN: [data object] — [missing invariant or undetected divergence]`
[RULE-CR-DCV may append DCV-CR-NN entries here via Gate 4 amendments]
Nil: `DCV-NIL: No data consistency violations identified — [scope rationale].`

**Missing Recovery Flows**

`MRF-NN: [scenario name] — [recovery actor with no defined action]`
Nil: `MRF-NIL: No missing recovery flows identified — [scope rationale].`

```
GATE 3 STATUS: [OPEN | CLOSED]
OEG section: [present | nil-stated]
DCV section: [present | nil-stated]
MRF section: [present | nil-stated]
Reason if OPEN: [specific section absent or unlinked finding]
```

If `GATE 3: CLOSED`, proceed to Gate 3b and Gate 4 in parallel.

---

### Gate 3b — Coverage Gap Registry

**Entry condition**: Gate 1b `CLOSED` AND Gate 3 `CLOSED`.
**Exit condition**: Every CG-NN queued by RULE-BARRED-CG in Gate 1b appears as a named
coverage gap entry; or `CG-NIL` is declared. Write `GATE 3b: CLOSED`.

For each CG-NN queued:

```
Coverage Gap: CG-NN
Rule invoked: RULE-BARRED-CG
Entry: [scenario name from Gate 1]
Class: [degradation class]
Unresolved basis: [confidence gap from Gate 1b — never resolved]
```

If no RULE-BARRED-CG triggers occurred:
`CG-NIL: RULE-BARRED-CG not triggered — no permanently BARRED entries in Gate 1b.`

```
GATE 3b STATUS: [OPEN | CLOSED]
Coverage gaps recorded: [count, or "CG-NIL"]
```

---

### Gate 4 — Conflict Resolution Adequacy

**Entry condition**: Gate 3 `CLOSED`.
**Exit condition**: Every Eventual-Consistency scenario from Gate 2 has a CR entry; all
RULE-CR-DCV triggers have been applied and sub-gate amendments closed; or No-Amendment
Confirmation is written. Write `GATE 4: CLOSED`.

```
CR-NN: [scenario name]
Conflict strategy: [last-write-wins | merge | manual-reconcile | reject-stale | undefined]
Data type: [object in conflict]
Adequacy verdict: [adequate | inadequate]
Rationale: [one sentence]
```

For each CR entry where verdict is `inadequate` or strategy is `undefined`,
invoke **RULE-CR-DCV**:

```
RULE-CR-DCV invoked by CR-NN:
GATE 3: REOPENED — triggering: CR-NN / [description]
DCV-CR-NN: [data object] — [missing invariant]
Rule: RULE-CR-DCV
GATE 3[a/b/c]: AMENDED — per RULE-CR-DCV / CR-NN
Status: CLOSED
```

When all CR verdicts are `adequate` and all strategies are defined:

```
RULE-CR-DCV: no triggers. All verdicts adequate; all strategies defined.
GATE 3 ORIGINAL CLOSURE CONFIRMED — no RULE-CR-DCV amendments required.
```

```
GATE 4 STATUS: [OPEN | CLOSED]
CR entries assessed: [count]
RULE-CR-DCV triggers: [list sub-gate labels and CR-NN IDs, or "none — see No-Amendment Confirmation"]
Reason if OPEN: [specific EC scenario without CR entry]
```

**Post-Analysis Registry Audit**

After Gate 4 closes, enumerate all rules actually invoked during this analysis run:

```
REGISTRY AUDIT
─────────────────────────────────────────────────────
RULE-CR-DCV: [invoked — list instances | not triggered]
RULE-BARRED-CG: [invoked — list instances | not triggered]
Inline rules declared: [list, or "none"]
─────────────────────────────────────────────────────
```

The registry audit confirms that no undeclared linkage was applied. Its absence is an
audit-trail gap.

**Output artifact**: `simulations/flow/resilience/{{topic}}-resilience-{{date}}.md`

---

## V-04 — Combination: Nil Supersession Protocol + Confidence Triage Resolution Sub-Gate

**Variation axes**: Nil-Finding Supersession Protocol (C-25) + Confidence Triage Resolution
Sub-Gate (C-26)
**Hypothesis**: C-25 and C-26 address complementary lifecycle gaps. C-25 closes the nil
lifecycle: when a nil is superseded by a downstream gap finding, the nil is annotated and the
supersession is logged. C-26 closes the BARRED promotion lifecycle: when a BARRED entry's
confidence basis is later satisfied, the promotion is recorded under a labeled sub-gate. Both
criteria answer the same structural question — "what happened to this artifact between when
it was declared and now?" — at different artifact types. Together they create a fully auditable
analysis where no artifact's lifecycle is open-ended: every nil reaches either ACTIVE (confirmed)
or SUPERSEDED (cited), and every BARRED entry reaches either Permanently BARRED (recorded as
CG) or Include via GATE 1b: RESOLVED. The combination tests whether both lifecycle protocols
can coexist in a single template without structural conflict.

---

You are a Commerce / distributed systems domain expert. Produce a resilience signal artifact
for the commerce system described by the topic.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### Gate 1 — Failure Mode Discovery

**Entry condition**: None (Gate 1 is the analysis entry point).
**Exit condition**: Every failure mode entry carries one of three named dispositions
(`Include` / `BARRED` / `Argued-Impossible`) with a stated basis; each degradation class
has at least two `Include` entries. Write `GATE 1: CLOSED`.

```
Entry: [name]
Class: [Offline / Partial-Failure / Eventual-Consistency]
Disposition: [Include | BARRED | Argued-Impossible]
Basis: [one sentence — architecture reason or confidence gap]
```

"Flagged" is not a disposition.

```
GATE 1 STATUS: [OPEN | CLOSED]
Include entries by class: Offline=[N] / Partial-Failure=[N] / Eventual-Consistency=[N]
BARRED entries: [list names, or "none"]
Reason if OPEN: [specific blocking condition]
```

If `GATE 1: CLOSED`, proceed to Gate 1b.

---

### Gate 1b — BARRED Triage Resolution

**Entry condition**: Gate 1 `CLOSED`.
**Exit condition**: Every BARRED entry has a resolution verdict. Write `GATE 1b: CLOSED`.

For each BARRED entry:

```
Entry: [name]
Confidence basis: [restate from Gate 1]
Resolution attempt: [what in the topic signal addresses this basis]
Outcome: [Include — basis resolved | Permanently BARRED — basis not resolved]
```

**When Outcome is `Include — basis resolved`**, record the promotion under a labeled
resolution sub-gate:

```
GATE 1b: RESOLVED
Entry promoted: [name]
Previous disposition: BARRED
Confidence basis: [previously unresolved basis]
Basis satisfied by: [specific signal, inference, or named assumption]
New disposition: Include
Applies to Gate 2: yes
GATE 1b RESOLUTION STATUS: CLOSED — promotion on record
```

Without this sub-gate, the reader cannot determine whether the entry was always Include or
promoted from BARRED.

**When Outcome is `Permanently BARRED`**:

```
Coverage Gap queued: CG-NN
Entry: [name] / Class: [class] / Unresolved basis: [gap]
Appears in Gate 3b Coverage Gap Registry.
```

**When Gate 1b has no BARRED entries**:
`GATE 1b: NO ENTRIES — Gate 1 produced no BARRED entries. GATE 1b STATUS: CLOSED`

```
GATE 1b STATUS: [OPEN | CLOSED]
BARRED-to-Include upgrades: [list entry names + GATE 1b: RESOLVED sub-gate labels, or "none"]
Permanently BARRED: [list names, or "none"]
Coverage gaps queued: [list CG-NN, or "none"]
```

If `GATE 1b: CLOSED`, proceed to Gate 2.

---

### Gate 2 — Scenario Analysis

**Entry condition**: Gate 1 `CLOSED` AND Gate 1b `CLOSED`.
**Exit condition**: Every `Include` entry (from Gate 1 and any Gate 1b: RESOLVED promotions)
has a complete four-field analysis. Minimum: six scenarios total, two per class.
Write `GATE 2: CLOSED`.

**[Entry ID — Name]** `[Class]`

- **State**: Precise failure description — named services, replicas, segments, failure mode
- **Capability**: Available / degraded / blocked for each named commerce operation
  (checkout, inventory reservation, payment processing, cart state, order fulfillment)
- **Data at risk**: Named object, failure mode (lost / stale / inconsistent / duplicated), scope
- **Recovery path**: Actor-prefixed steps — `[client]` / `[server]` / `[operator]` / `[user]`;
  each step includes trigger condition and observable success signal

```
GATE 2 STATUS: [OPEN | CLOSED]
Scenario count: Offline=[N] / Partial-Failure=[N] / Eventual-Consistency=[N]
Entries from Gate 1b RESOLVED: [list, or "none"]
```

If `GATE 2: CLOSED`, proceed to Gate 3.

---

### Gate 3 — Gap Identification

**Entry condition**: Gate 2 `CLOSED`.
**Exit condition**: All three gap sections present and labeled; nil findings carry typed unique
identifiers (`OEG-NIL-N`, `DCV-NIL-N`, `MRF-NIL-N`) and scope rationale; all findings
reference named Gate 2 scenarios or data objects. Write `GATE 3: CLOSED`.

**Typed Nil Identifiers with Lifecycle States**

Every nil finding carries a gap-type prefix, a run-unique numeric suffix, a scope rationale,
and an initial lifecycle state:

Format: `OEG-NIL-1: [ACTIVE] No offline experience gaps identified — [scope rationale].`

The lifecycle state field `[ACTIVE]` is written at declaration time. A nil becomes
`[SUPERSEDED by FINDING-ID]` when Gate 4 or a downstream gate produces a finding in the
same gap category.

**Offline Experience Gaps**

`OEG-NN: [scenario name] — [unhandled user encounter during offline failure]`
Nil: `OEG-NIL-1: [ACTIVE] No offline experience gaps identified — [scope rationale].`

**Data Consistency Violations**

`DCV-NN: [data object] — [missing invariant or undetected divergence]`
[Gate 4 may supersede DCV-NIL-N here via the CR-DCV linkage]
Nil: `DCV-NIL-1: [ACTIVE] No data consistency violations identified — [scope rationale].`

**Missing Recovery Flows**

`MRF-NN: [scenario name] — [recovery actor with no defined action]`
Nil: `MRF-NIL-1: [ACTIVE] No missing recovery flows identified — [scope rationale].`

```
GATE 3 STATUS: [OPEN | CLOSED]
OEG section: [present | nil-stated — identifier]
DCV section: [present | nil-stated — identifier]
MRF section: [present | nil-stated — identifier]
```

If `GATE 3: CLOSED`, proceed to Gate 3b and Gate 4 in parallel.

---

### Gate 3b — Coverage Gap Registry

**Entry condition**: Gate 1b `CLOSED` AND Gate 3 `CLOSED`.
**Exit condition**: Every CG-NN queued from permanently BARRED entries appears; or CG-NIL
is declared. Write `GATE 3b: CLOSED`.

```
Coverage Gap: CG-NN
Entry: [scenario name] / Class: [class] / Unresolved basis: [gap]
```

If no permanently BARRED entries: `CG-NIL: No permanently BARRED entries — no coverage gaps.`

```
GATE 3b STATUS: [OPEN | CLOSED]
Coverage gaps recorded: [count, or "CG-NIL"]
```

---

### Gate 4 — Conflict Resolution Adequacy

**Entry condition**: Gate 3 `CLOSED`.
**Exit condition**: Every Eventual-Consistency scenario has a CR entry; all inadequate/undefined
verdicts have generated DCV-CR-NN amendments with nil supersession annotations as required;
Nil Supersession Log is written. Write `GATE 4: CLOSED`.

```
CR-NN: [scenario name]
Conflict strategy: [last-write-wins | merge | manual-reconcile | reject-stale | undefined]
Data type: [object in conflict]
Adequacy verdict: [adequate | inadequate]
Rationale: [one sentence]
```

If verdict is `inadequate` or strategy is `undefined`:

```
GATE 3: REOPENED — triggering: CR-NN / [description]
DCV-CR-NN: [data object] — [missing invariant]
GATE 3[a/b/c]: AMENDED
Status: CLOSED
Amendment: DCV-CR-NN added to Data Consistency Violations
```

If the DCV section held `DCV-NIL-N`:

```
NIL LIFECYCLE UPDATE:
DCV-NIL-N: [SUPERSEDED by DCV-CR-NN]
  Nil declared ACTIVE in Gate 3; superseded when DCV-CR-NN added in Gate 4 amendment.
  Superseding finding: DCV-CR-NN
```

**Nil Supersession Log**

After all CR entries are assessed, write the Nil Supersession Log:

```
NIL SUPERSESSION LOG
─────────────────────────────────────────────────────
OEG nils: OEG-NIL-N [ACTIVE | SUPERSEDED by OEG-F-NN]
DCV nils: DCV-NIL-N [ACTIVE | SUPERSEDED by DCV-CR-NN]
MRF nils: MRF-NIL-N [ACTIVE | SUPERSEDED by MRF-NN]
─────────────────────────────────────────────────────
Total nils declared: [N]
Total supersessions this run: [N]
[If N=0: "No supersessions — all declared nils remain ACTIVE."]
```

If no CR verdicts are inadequate and no strategies are undefined:
`No CR-DCV linkage triggered. GATE 3 ORIGINAL CLOSURE CONFIRMED.`

```
GATE 4 STATUS: [OPEN | CLOSED]
CR entries assessed: [count]
DCV amendments: [list DCV-CR-NN, or "none"]
Nil supersessions: [list nil IDs + superseding finding IDs, or "none"]
```

**Gate 1b Promotion Audit** (final check after Gate 4):

Cross-reference Gate 2 scenario entries against Gate 1b records to confirm every
BARRED-to-Include entry has a `GATE 1b: RESOLVED` sub-gate on record:

```
GATE 1b PROMOTION AUDIT
─────────────────────────────────────────────────────
[Entry name]: promoted via GATE 1b: RESOLVED — [sub-gate label]
[Or: "No promotions — all Include entries entered directly from Gate 1."]
─────────────────────────────────────────────────────
All promotions auditable: [yes | no — list missing sub-gate records]
```

**Output artifact**: `simulations/flow/resilience/{{topic}}-resilience-{{date}}.md`

---

## V-05 — Full R7 Integration: Nil Supersession + Confidence Resolution Sub-Gate + Rule Registry

**Variation axes**: All three R7 criteria (C-25, C-26, C-27) combined with full R6
formalization (C-22 through C-24, C-21 scope declaration, C-15 through C-20 gate formalism)
**Hypothesis**: C-25, C-26, and C-27 are all lifecycle closure mechanisms. C-25 closes the
nil lifecycle (ACTIVE → SUPERSEDED). C-26 closes the BARRED promotion lifecycle
(BARRED → Include via labeled sub-gate). C-27 closes the rule declaration lifecycle
(rules declared once in a registry, invoked by ID, audited post-analysis). Together with the
full R6 formalization — scope brackets, typed nil identifiers, phase entry/exit conditions,
gate-state vocabulary, coverage accountability roster, DS-primitive grounded impossibility
arguments — V-05 assembles the most complete template in the series. Every artifact type has
a lifecycle with an explicit start, a lifecycle state, and a terminal closure. The test is
whether the formalization is coherent end-to-end: that rules, nils, gate states, scope
brackets, and BARRED promotions all close cleanly without structural conflicts.

---

You are a Commerce / distributed systems domain expert. Produce a resilience signal artifact
for the commerce system described by the topic. Apply the full analysis protocol below.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### RULE REGISTRY

All cross-section conditional linkage rules are declared here before Gate 1 opens.
Each rule has a unique registry ID. Gate sections cite rules by ID — they do not restate
the trigger condition inline. All rules are mandatory; when a trigger condition is met,
the action applies automatically.

```
RULE-ID:  RULE-CR-DCV
Trigger:  Adequacy verdict is `inadequate` OR Conflict strategy is `undefined`
          (Gate 4 CR entries)
Action:   1. Reopen Gate 3 under a labeled amendment sub-gate (GATE 3a, 3b, 3c, ...).
          2. Append DCV-CR-NN to Gate 3 Data Consistency Violations.
          3. If DCV section held DCV-NIL-N: write NIL LIFECYCLE UPDATE in the Nil
             Supersession Log — DCV-NIL-N: SUPERSEDED by DCV-CR-NN.
          4. Re-close the sub-gate citing this rule ID and the triggering CR-NN.
IDs used: DCV-CR-01, DCV-CR-02, ...
Scope:    Gate 4 → Gate 3 (+ Nil Supersession Log)
```

```
RULE-ID:  RULE-BARRED-CG
Trigger:  Entry remains Permanently BARRED after Gate 1b (basis never resolved)
Action:   1. Append CG-NN to Gate 3b Coverage Gap Registry.
          2. Cite RULE-BARRED-CG in the CG-NN record.
IDs used: CG-01, CG-02, ...
Scope:    Gate 1b → Gate 3b
```

```
RULE-ID:  RULE-NIL-SUPERSEDE
Trigger:  Any gate or phase produces a gap finding in the same category as a
          currently ACTIVE typed nil identifier (OEG-NIL-N, DCV-NIL-N, MRF-NIL-N)
Action:   1. Annotate the nil: [type]-NIL-N: SUPERSEDED by [finding-ID]
          2. Record the supersession in the Nil Supersession Log.
IDs used: References existing nil IDs and new finding IDs
Scope:    Any gate → Nil Supersession Log
```

**Inline Declaration Protocol**: For any linkage not covered above, declare inline at first
application: `RULE-INLINE-N (declared inline): Trigger: [condition] / Action: [action]`

```
REGISTRY STATUS: CLOSED
Rules declared: RULE-CR-DCV, RULE-BARRED-CG, RULE-NIL-SUPERSEDE
Inline rules: none at registry close
```

Gate 1 may not open before `REGISTRY STATUS: CLOSED`.

---

### Commerce Operation Scope Declaration

Declare the commerce operations this analysis covers before Gate 1 opens. This is a
commitment — it must precede the first analysis gate. Assign each operation a short
identifier (OP-01, OP-02, ...).

Choose at least four operations from the standard set:
checkout / inventory reservation / payment processing / cart state / order fulfillment / loyalty redemption

```
Operation: [name] — ID: OP-NN
Scope: [In-scope | Excluded]
DS Primitive or reason if Excluded: [one sentence]
```

After all operations are declared, write the opening bracket block:

```
╔══ SCOPE BRACKET: OPENING ══════════════════════════════════════╗
SCOPE DECLARATION COMPLETE
In-scope: [OP-01: name, OP-02: name, ...]   (minimum four)
Excluded: [OP-NN: name, ...] or "none"
Terminal bracket block: Scope Verification (appears after Gate 4)
╚════════════════════════════════════════════════════════════════╝
```

Gate 1 may not open before this block is written.

---

### Coverage Accountability Roster

Before Gate 1 opens, commit to minimum coverage across degradation classes. This roster
is checkable: the reader can verify coverage against the final scenario table independently.

```
Class: Offline
Committed minimum: 2 scenarios
Slot 1: [brief description of planned scenario] — [commerce operation anchor]
Slot 2: [brief description of planned scenario] — [commerce operation anchor]
Additional slots: [planned, or "none beyond minimum"]

Class: Partial-Failure
Committed minimum: 2 scenarios
Slot 1: [brief description] — [commerce operation anchor]
Slot 2: [brief description] — [commerce operation anchor]

Class: Eventual-Consistency
Committed minimum: 2 scenarios
Slot 1: [brief description] — [commerce operation anchor]
Slot 2: [brief description] — [commerce operation anchor]
```

If any slot cannot be filled, provide an impossibility argument. The argument must cite a
specific DS primitive — not a topic-scope absence:

```
Impossibility argument for [class] slot [N]:
DS Primitive cited: [named CAP theorem guarantee | topology constraint | sync property]
Architecture basis: [one sentence — why this class cannot occur given the architecture]
VALID example: "split-brain is impossible in a single-node deployment — synchronous
  guarantee forecloses network partition as a failure class."
INVALID example: "the topic doesn't mention a distributed cache, so split-brain can't apply."
```

"The topic doesn't mention X" is not an impossibility argument. The argument must address
the architecture, not the description.

---

### Gate 1 — Failure Mode Discovery

**Entry condition**: `REGISTRY STATUS: CLOSED` AND Scope Declaration opening bracket written
AND Coverage Accountability Roster committed.
**Exit condition**: Every failure mode entry carries one of three named dispositions
(`Include` / `BARRED` / `Argued-Impossible`) with a stated basis; each degradation class
has at least two `Include` entries. Write `GATE 1: CLOSED` only when all conditions are met.

```
Entry: [name]
Class: [Offline / Partial-Failure / Eventual-Consistency]
Disposition: [Include | BARRED | Argued-Impossible]
Basis: [one sentence — architecture reason or confidence gap]
Confidence (if Argued-Impossible): [impossible — DS primitive: name the specific primitive]
```

"Flagged" is not a disposition. A gate with no explicit `CLOSED` declaration is `OPEN`.

For `Argued-Impossible` entries — cite the DS primitive:

```
DS Primitive cited: [named primitive]
Architecture basis: [one sentence]
Topic scope is not a valid basis — see INVALID example in Coverage Accountability Roster.
```

```
GATE 1 STATUS: [OPEN | CLOSED]
Include entries by class: Offline=[N] / Partial-Failure=[N] / Eventual-Consistency=[N]
BARRED entries: [list names, or "none"]
Argued-Impossible entries: [list names + DS primitive cited, or "none"]
Reason if OPEN: [specific blocking condition — named entry, class minimum, or unresolved basis]
```

If `GATE 1: CLOSED`, proceed to Gate 1b.

---

### Gate 1b — BARRED Triage Resolution

**Entry condition**: Gate 1 `CLOSED`.
**Exit condition**: Every BARRED entry has a resolution verdict. Write `GATE 1b: CLOSED`.

For each BARRED entry, attempt to resolve the confidence basis:

```
Entry: [name]
Confidence basis: [restate from Gate 1]
Resolution attempt: [what in the topic signal or architecture addresses this basis]
Outcome: [Include — basis resolved | Permanently BARRED — basis not resolved]
```

**When Outcome is `Include — basis resolved`** — record under a labeled resolution sub-gate:

```
GATE 1b: RESOLVED
Entry promoted: [name]
Previous disposition: BARRED
Confidence basis: [previously unresolved basis]
Basis satisfied by: [specific signal, architecture inference, or named assumption]
New disposition: Include
Applies to Gate 2: yes
GATE 1b RESOLUTION STATUS: CLOSED — promotion on record
```

**When Outcome is `Permanently BARRED`** — per **RULE-BARRED-CG**:

```
RULE-BARRED-CG invoked: CG-NN queued for Gate 3b
Entry: [name] / Class: [class] / Unresolved basis: [gap]
```

**When no BARRED entries exist**:
`GATE 1b: NO ENTRIES — Gate 1 produced no BARRED entries.`

```
GATE 1b STATUS: [OPEN | CLOSED]
BARRED-to-Include upgrades: [list entry names + GATE 1b: RESOLVED labels, or "none"]
Permanently BARRED: [list names, or "none"]
RULE-BARRED-CG triggers queued: [list CG-NN, or "none"]
Reason if OPEN: [specific unresolved entry name]
```

If `GATE 1b: CLOSED`, proceed to Gate 2.

---

### Gate 2 — Scenario Analysis

**Entry condition**: Gate 1 `CLOSED` AND Gate 1b `CLOSED`.
**Exit condition**: Every `Include` entry (from Gate 1 and any Gate 1b: RESOLVED promotions)
has a complete four-field analysis; committed Coverage Accountability Roster slots are filled
or impossibility arguments are present; minimum six scenarios total, two per class.
Write `GATE 2: CLOSED`.

**[Entry ID — Name]** `[Class]`

- **State**: Precise failure description — named services, replicas, segments, failure mode;
  severity (degraded / impaired / down) and blast radius (fraction/segment of users affected)
- **Capability**: For each In-scope operation (by OP-NN ID) from the Scope Declaration,
  state whether it is `available` / `degraded` / `blocked`. Do not omit declared operations.
- **Data at risk**: Named object, failure mode (lost / stale / inconsistent / duplicated), scope
- **Recovery path**: Ordered actor-prefixed steps — `[client]` / `[server]` / `[operator]` /
  `[user]`; each step includes trigger condition and observable success signal

```
GATE 2 STATUS: [OPEN | CLOSED]
Scenario count: Offline=[N] / Partial-Failure=[N] / Eventual-Consistency=[N]
Roster slots filled: Offline=[N/2] / Partial-Failure=[N/2] / Eventual-Consistency=[N/2]
Entries from Gate 1b RESOLVED: [list, or "none"]
Reason if OPEN: [specific entry or slot missing]
```

If `GATE 2: CLOSED`, proceed to Gate 3.

---

### Gate 3 — Gap Identification

**Entry condition**: Gate 2 `CLOSED`.
**Exit condition**: All three gap sections present and labeled; nil findings carry typed
unique identifiers, scope rationale, and initial lifecycle state `[ACTIVE]`; all findings
reference named Gate 2 scenarios or data objects. Write `GATE 3: CLOSED`.

Note: **RULE-CR-DCV** (Gate 4) and **RULE-NIL-SUPERSEDE** may reopen Gate 3 to append
DCV-CR-NN entries and update nil lifecycle states. These amendments create labeled sub-gates;
Gate 3's original CLOSED status is preserved. Gate sections cite rules by registry ID.

**Typed Nil Identifiers — Lifecycle Protocol**

Every nil finding carries:
1. Gap-type prefix: `OEG-NIL`, `DCV-NIL`, or `MRF-NIL`
2. Run-unique numeric suffix: `-1`, `-2`, ...
3. Lifecycle state at declaration: `[ACTIVE]`
4. Scope rationale

Format: `OEG-NIL-1: [ACTIVE] No offline experience gaps identified — [scope rationale].`

State transitions are recorded per **RULE-NIL-SUPERSEDE**:
`DCV-NIL-1: [SUPERSEDED by DCV-CR-01]` — when Gate 4 generates DCV-CR-01 in this category.

**Offline Experience Gaps**

`OEG-NN: [scenario name] — [unhandled user encounter during offline failure]`
Nil: `OEG-NIL-1: [ACTIVE] No offline experience gaps identified — [scope rationale].`

**Data Consistency Violations**

`DCV-NN: [data object] — [missing invariant or undetected divergence]`
[RULE-CR-DCV may append DCV-CR-NN here from Gate 4]
Nil: `DCV-NIL-1: [ACTIVE] No data consistency violations identified — [scope rationale].`

**Missing Recovery Flows**

`MRF-NN: [scenario name] — [recovery actor with no defined action]`
Nil: `MRF-NIL-1: [ACTIVE] No missing recovery flows identified — [scope rationale].`

```
GATE 3 STATUS: [OPEN | CLOSED]
OEG section: [present | nil-stated — OEG-NIL-1 ACTIVE]
DCV section: [present | nil-stated — DCV-NIL-1 ACTIVE]
MRF section: [present | nil-stated — MRF-NIL-1 ACTIVE]
Reason if OPEN: [specific section absent or finding not linked to named Gate 2 artifact]
```

If `GATE 3: CLOSED`, proceed to Gate 3b and Gate 4 in parallel.

---

### Gate 3b — Coverage Gap Registry

**Entry condition**: Gate 1b `CLOSED` AND Gate 3 `CLOSED`.
**Exit condition**: Every CG-NN queued by RULE-BARRED-CG in Gate 1b appears as a named
entry; or CG-NIL declared. Write `GATE 3b: CLOSED`.

```
Coverage Gap: CG-NN
Rule invoked: RULE-BARRED-CG
Entry: [scenario name from Gate 1]
Class: [degradation class]
Unresolved basis: [confidence gap — never resolved in Gate 1b]
```

If no RULE-BARRED-CG triggers occurred:
`CG-NIL: RULE-BARRED-CG not triggered — no permanently BARRED entries in Gate 1b.`

```
GATE 3b STATUS: [OPEN | CLOSED]
Coverage gaps recorded: [count, or "CG-NIL"]
```

---

### Gate 4 — Conflict Resolution Adequacy

**Entry condition**: Gate 3 `CLOSED`.
**Exit condition**: Every Eventual-Consistency scenario from Gate 2 has a CR entry; all
RULE-CR-DCV triggers applied and sub-gate amendments closed; Nil Supersession Log written.
Write `GATE 4: CLOSED`.

```
CR-NN: [scenario name]
Conflict strategy: [last-write-wins | merge | manual-reconcile | reject-stale | undefined]
Data type: [object in conflict]
Adequacy verdict: [adequate | inadequate]
Rationale: [one sentence — include adequacy judgment for the data type]
```

For each CR entry where verdict is `inadequate` or strategy is `undefined` — per
**RULE-CR-DCV**:

```
RULE-CR-DCV invoked by CR-NN:
GATE 3: REOPENED — triggering: CR-NN / [description]
DCV-CR-NN: [data object] — [missing invariant from inadequate/undefined strategy]
Rule: RULE-CR-DCV
GATE 3[a/b/c]: AMENDED — per RULE-CR-DCV / CR-NN
Status: CLOSED
```

If DCV section held `DCV-NIL-N` — per **RULE-NIL-SUPERSEDE**:

```
RULE-NIL-SUPERSEDE invoked:
NIL LIFECYCLE UPDATE: DCV-NIL-1: [SUPERSEDED by DCV-CR-NN]
Nil declared ACTIVE in Gate 3; superseded per RULE-NIL-SUPERSEDE
Superseding finding: DCV-CR-NN (added by RULE-CR-DCV)
```

**No-Amendment Confirmation** (when all CR verdicts are `adequate` and strategies are defined):

```
RULE-CR-DCV: no triggers. All verdicts adequate; all strategies defined.
RULE-NIL-SUPERSEDE: no triggers. No nils superseded by Gate 4 findings.
GATE 3 ORIGINAL CLOSURE CONFIRMED — no RULE-CR-DCV amendments required.
```

**Nil Supersession Log**

```
NIL SUPERSESSION LOG
─────────────────────────────────────────────────────
OEG nils: OEG-NIL-N [ACTIVE | SUPERSEDED by OEG-F-NN]
DCV nils: DCV-NIL-N [ACTIVE | SUPERSEDED by DCV-CR-NN]
MRF nils: MRF-NIL-N [ACTIVE | SUPERSEDED by MRF-NN]
─────────────────────────────────────────────────────
Total nils declared: [N]
Total supersessions this run: [N]
[If 0: "No supersessions — all declared nils remain ACTIVE."]
Rule: RULE-NIL-SUPERSEDE
```

```
GATE 4 STATUS: [OPEN | CLOSED]
CR entries assessed: [count]
RULE-CR-DCV triggers: [list sub-gate labels + CR-NN IDs, or "none"]
RULE-NIL-SUPERSEDE triggers: [list nil IDs + superseding finding IDs, or "none"]
Reason if OPEN: [specific EC scenario without CR entry]
```

---

### Scope Verification *(Terminal Bracket Block)*

**Entry condition**: Gate 2 `CLOSED` (scenario table complete).

Cross-check every operation from the opening Scope Declaration against the Gate 2 scenario
table. This block closes the scope commitment opened by `SCOPE BRACKET: OPENING`.

For each declared operation:

```
Operation: [name — OP-NN] (declared [In-scope | Excluded])
Coverage outcome: [covered — scenario IDs] | [gap — declared In-scope; no Gate 2 scenario]
                  | [out-of-scope — declared Excluded; not expected]
```

If any In-scope operation has no coverage:
`SCOV-NN: [operation name] — declared In-scope but not covered in Gate 2.`

If all In-scope operations have coverage:
`SCOV-NIL: All declared In-scope operations receive scenario coverage in Gate 2.`

Write the terminal bracket block:

```
╔══ SCOPE BRACKET: CLOSING ══════════════════════════════════════╗
Opening block: SCOPE BRACKET: OPENING (before Gate 1)
Terminal block: Scope Verification (this block)
In-scope operations declared: [list from opening block — OP-NN: name, ...]
Coverage outcomes: covered=[N] / gap=[N] / out-of-scope=[N]
SCOPE BRACKET CLOSED
╚════════════════════════════════════════════════════════════════╝
```

---

### Post-Analysis Registry Audit

After all gates and the Scope Verification block are complete, enumerate all rules invoked:

```
REGISTRY AUDIT
─────────────────────────────────────────────────────
RULE-CR-DCV: [invoked — list instances | not triggered]
RULE-BARRED-CG: [invoked — list instances | not triggered]
RULE-NIL-SUPERSEDE: [invoked — list instances | not triggered]
Inline rules declared: [list, or "none"]
─────────────────────────────────────────────────────
All linkages traceable to registry: [yes | no — list any undeclared linkage applied]
```

---

**Output artifact**: `simulations/flow/resilience/{{topic}}-resilience-{{date}}.md`
