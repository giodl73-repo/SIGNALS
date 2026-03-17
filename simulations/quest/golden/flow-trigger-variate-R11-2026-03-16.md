---
skill: flow-trigger
round: 11
date: 2026-03-16
rubric_version: 8
new_criteria: [C-27, C-28, C-29]
---

# flow-trigger -- Round 11 Variations

**New criteria this round:**
- **C-27** -- Computable Phase 0 exit signal via typed status aggregate: each exit condition
  carries `Status: SATISFIED | PENDING | BLOCKED`; EXIT SIGNAL derives from counting
  SATISFIED rows ("5/5 SATISFIED -- enumeration authorized") -- recomputable by inspection
  without semantic re-evaluation
- **C-28** -- Per-obligation refutation conditions: each Phase 0 obligation carries a
  co-located `Violated if:` clause naming a concrete, string-detectable breach condition --
  extends C-24 breach-token principle upstream to Phase 0 obligations
- **C-29** -- INERTIA CONTRAST as typed inline columns: `Weaker alternative` and
  `Failure mode` appear as named column slots in the Phase 0 obligation registry header,
  not as a separate section -- rationale is non-separable at cell level

**Structural relationship:** C-27 makes Phase 0 exit trustworthiness self-verifiable (status
aggregate, not assertion); C-28 makes Phase 0 violation self-detectable (refutation conditions,
not rubric re-scoring); C-29 makes structural rationale non-separable (cell columns, not a
heading). Together they complete a self-explaining, self-enforcing, self-verifying Phase 0 gate.

**Variation axes used:**

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Output format -- typed status aggregate (C-27) | When Phase 0 exit conditions carry a named `Status` enum column, the EXIT SIGNAL becomes a computed row count ("5/5 SATISFIED") rather than an authorial assertion; an evaluator recomputes the exit decision by counting status column values, making C-27 pass without semantic re-evaluation |
| V-02 | Lifecycle emphasis -- per-obligation refutation conditions (C-28) | When each Phase 0 obligation row carries a co-located `Violated if:` clause naming a concrete, string-detectable breach, violation of any pre-enumeration gate is detectable by structural inspection alone -- closing the asymmetry where compliance is structurally guaranteed but violation is rubric-detectable only |
| V-03 | Inertia framing -- INERTIA CONTRAST as typed inline columns (C-29) | When `Weaker alternative` and `Failure mode` are named column slots in the Phase 0 registry header, rationale is non-separable from the obligation it motivates; removing a section heading cannot strip rationale because it lives at cell level, not section level |
| V-04 | Role sequence + Output format -- computed inter-role gate (C-27 + role boundary) | When Role 0 issues a computable EXIT SIGNAL aggregate and Role 1 (Auditor) carries an entry gate that resolves against that counter mechanically ("AUTHORIZED when Phase 0 aggregate = 5/5 SATISFIED"), the role-sequence gate is structurally verifiable -- not assertion-dependent -- before any content is evaluated |
| V-05 | Output format + Inertia framing -- unified 6-column Phase 0 registry (C-27 + C-28 + C-29) | When all three new criteria are unified in a single Phase 0 registry table with 6 named columns (EC-ID, Exit Condition, Status, Violated if, Weaker alternative, Failure mode), every obligation row is simultaneously self-computing, self-detecting, and self-motivating; the Phase 0 table is sufficient for full evaluation without consulting any external section |

---

## V-01

**Variation axis:** Output format -- typed status aggregate (C-27)
**Hypothesis:** When Phase 0 exit conditions carry a named `Status` enum column with values
from `{SATISFIED | PENDING | BLOCKED}`, the EXIT SIGNAL becomes a computed row count
("5/5 SATISFIED -- enumeration authorized") rather than an authorial assertion. An evaluator
who doubts the exit signal can recompute it by counting SATISFIED rows without re-reading
obligation descriptions. The exit decision is derivable from the status column alone.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dynamics 365 Sales `account` record's `statecode` field has changed from `Active` (0) to
`Inactive` (1). Your task: determine exactly which automations fire, in what order, with what
inputs and outputs, and identify all trigger pathologies (storms, missing triggers, circular
triggers).

Execute the following phases in strict sequence. Each phase SHALL complete before the next
begins. No phase SHALL execute until all prior phases have issued their required outputs.

---

### PROTOCOL PREAMBLE

#### Platform Term Contract

Approved vocabulary:

| Approved Term | Prohibited Substitutions |
|--------------|-------------------------|
| automated cloud flow | workflow, automation, rule |
| instant cloud flow | manual flow, button flow |
| scheduled cloud flow | recurring flow, timer flow |
| Dataverse plug-in | plugin, CRM plugin, platform plugin |
| sync plug-in step | synchronous plugin, pre-stage plugin |
| async plug-in step | asynchronous plugin, background plugin |
| trigger event: When a row is added, modified or deleted | record trigger, update trigger |
| Power Automate connector | connector trigger, flow connector |

Any term deviating from this list SHALL be tagged `[VOCAB FAIL: "actual text" -> correction | FM-08]`.

#### FM Catalog

| FM Code | Failure Mode | Expected Behavior | Output Marker | Phase(s) |
|---------|-------------|-------------------|---------------|----------|
| FM-01 | Trigger omission | Every bound trigger listed by name | `[OMIT: trigger-name \| FM-01]` | 2, 3 |
| FM-02 | Firing order violation | Sync before async; by priority within tier | `[ORDER FAIL: actual \| FM-02]` | 2, 3 |
| FM-03 | Missing input/output specification | Named input payload and output action; no placeholders | `[IO FAIL: trigger-name \| FM-03]` | 2, 3 |
| FM-04 | Missing pathology coverage | All three pathology classes addressed | `[PATH MISS: class \| FM-04]` | 5 |
| FM-05 | False positive trigger | Only triggers scoped to this change | `[FALSE POS: trigger-name \| FM-05]` | 2, 3 |
| FM-06 | Shallow side effect trace | Cascade traced until no further triggers fire | `[CASCADE SHALLOW \| FM-06]` | 4 |
| FM-07 | Missing conditional branch | Firing and skipped branch both stated | `[BRANCH MISS: trigger-name \| FM-07]` | 2, 3 |
| FM-08 | Wrong platform vocabulary | Approved vocabulary used throughout | `[VOCAB FAIL: "actual" -> correction \| FM-08]` | All |
| FM-09 | Missing risk ranking | Pathologies ranked with one-line mitigation | `[RISK MISS \| FM-09]` | 5 |
| FM-10 | Missing timing annotation | Sync/async distinguished; latency noted | `[TIMING MISS: trigger-name \| FM-10]` | 2, 3 |
| FM-11 | Missing negative example | At least one wrong-vs-correct vocabulary pair | `[NEG MISS \| FM-11]` | 2 |
| FM-12 | Ungrounded pathology verdict | Verdict cites evidence; bare assertions are insufficient | `[INSUFFICIENT: evidence needed \| FM-12]` | 5 |
| FM-13 | Open cascade chain | Termination condition declared per chain | `[CHAIN OPEN: CH-NN \| FM-13]` | 4 |
| FM-14 | No trigger graph | Adjacency list trigger->field->trigger constructed | `[GRAPH MISS \| FM-14]` | 5 |
| FM-15 | No denominator declaration | Count N declared before condition filtering | `[DENOM MISS \| FM-15]` | 1 |
| FM-16 | Entry Condition Absent | A named phase carries no entry precondition | `[ENTRY CONDITION ABSENT: Phase N \| FM-16]` | All phases |
| FM-17 | Gate Register Drift | A gate statement uses descriptive language where SHALL/MUST is required | `[GATE REGISTER DRIFT: Phase N gate \| FM-17]` | All phases |
| FM-18 | No sync/async structural split | Sync and async triggers in separate enumeration phases | `[SPLIT MISS \| FM-18]` | 2, 3 |
| FM-19 | No back-edge detection | Back-edge detection applied to adjacency structure | `[BACKTRACK MISS \| FM-19]` | 5 |
| FM-20 | Missing terminal row marker | Each cascade chain closes with [TERMINAL] | `[CHAIN OPEN: CH-NN \| FM-20]` | 4 |
| FM-21 | FM code missing from violation cell | Every violation marker includes FM code | `[FM-21]` | All |
| FM-22 | No denominator reconciliation | Closure verifies firing + non-firing + unresolved = N | `[RECON MISS \| FM-22]` | 6 |
| FM-24 | No side-effect slot | Side-effect slot in every firing trigger entry | `[SE MISS: trigger-name \| FM-24]` | 2, 3 |
| FM-25 | Missing trigger map | Trigger map with tier and cascade-link columns | `[MAP MISS \| FM-25]` | 6 |
| FM-26 | Co-authority partial verification | A LIFECYCLE OVERVIEW gate cell was verified against only one co-authoritative source | `[CO-AUTH PARTIAL: DECLARATION-only / Invariant-3-only \| FM-26]` | All |
| FM-38 | Phase 0 exit signal not computable | EXIT SIGNAL is a narrative assertion not derivable from status column aggregate | `[EXIT SIGNAL UNCOMPUTABLE: aggregate absent \| FM-38]` | Phase 0 |
| FM-39 | Refutation condition absent | A Phase 0 obligation carries no co-located "Violated if:" clause | `[REFUTATION ABSENT: EC-NN \| FM-39]` | Phase 0 |

#### Entry Schema Contract

All trigger entries SHALL conform to one of the following schemas. A slot left blank is a
schema violation.

**FIRING ENTRY** (all slots required):

```
Trigger Name:
Flow Type:          [automated cloud flow | instant cloud flow | Dataverse plug-in | ...]
Execution Tier:     [sync | async | scheduled]
Trigger Event:
Input Fields:       [specific named fields -- no generic placeholders]
Output Action:      [specific action -- no generic placeholders]
Side Effects:       [field writes produced beyond primary output, or "none"]
Condition (Taken):  [what must be true for this trigger to fire]
Condition (Skipped):[what would cause this trigger NOT to fire in this scenario]
Anomaly Flag:       [none | storm | missing | circular]
```

**NON-FIRING ENTRY** (all slots required):

```
Trigger Name:
Flow Type:
Reason Not Firing:  [specific condition excluding this trigger]
Condition (Taken):  [what would cause this trigger to fire -- not met in this scenario]
Condition (Skipped):[what IS true in this scenario that blocks this trigger]
```

---

### STRUCTURAL INVARIANT LAYER

**Invariant 1 -- Phase body completeness:** Every phase body SHALL contain all three control
artifacts: entry condition, job description, and exit condition.
**Violation taggable as: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`.**

**Invariant 2 -- Gate statement formal register (phase bodies):** All gate statements in phase
bodies SHALL use formal obligation language (SHALL/MUST) in the obligation position.
**Violation taggable as: `[GATE REGISTER DRIFT: Phase N gate | FM-17]`.**

**Invariant 3 -- The LIFECYCLE OVERVIEW table gate-cell register:** The LIFECYCLE OVERVIEW
table entry-condition and exit-condition cells are governed by this INVARIANT LAYER and SHALL
satisfy the same formal-register obligation as phase-body gate statements (Invariant 2). The
LIFECYCLE OVERVIEW table is NOT exempt from Invariant 2 by virtue of its summary function.
**Violation taggable as: `[GATE REGISTER DRIFT: LIFECYCLE OVERVIEW Phase N entry/exit | FM-17]`.**

**Invariant 4 -- FM code in every violation marker:** Every inline violation marker SHALL
include its FM catalog code. **Violation taggable as: `[FM-21]`.**

**Invariant 5 -- Denominator closure:** The candidate trigger count N declared in Phase 1
SHALL be reconciled after Phase 3: firing + non-firing + unresolved SHALL equal N.
**Violation taggable as: `[RECON MISS | FM-22]`.**

**Invariant 6 -- Co-authority verification requirement:** A verifier assessing conformance of
LIFECYCLE OVERVIEW table gate cells SHALL verify each cell against BOTH the FORMAL-GATE ZONE
DECLARATION (Rules 1-4) AND Invariant 3 simultaneously. FM-26 and this invariant are
structurally coupled: without FM-26, this invariant is an obligation with no enforcement
mechanism; without this invariant, FM-26 cannot activate as a meaningful catalog entry. The
two SHALL be declared together.
**Violation taggable as: `[CO-AUTH PARTIAL: DECLARATION-only / Invariant-3-only | FM-26]`.**

**Invariant 7 -- Phase 0 exit signal computability:** The Phase 0 EXIT SIGNAL SHALL be
derivable from the aggregate count of `Status: SATISFIED` rows in the exit condition registry.
The signal statement SHALL include the aggregate count (e.g., "5/5 SATISFIED"). A narrative
EXIT SIGNAL without a typed status aggregate violates this invariant.
**Violation taggable as: `[EXIT SIGNAL UNCOMPUTABLE: aggregate absent | FM-38]`.**

---

### PHASE 0 -- Pre-Enumeration Gate

**Purpose:** Lock all structural artifacts before any enumeration entry appears. Every
pre-enumeration obligation is listed here as a named exit condition row with a typed
`Status` value. The EXIT SIGNAL is computed from the status aggregate, not asserted.

**Status type definition:** `Status` values are drawn from the named enumeration
`EXIT-STATUS = {SATISFIED | PENDING | BLOCKED}`. An exit signal is authorized when and
only when all rows carry `Status: SATISFIED` -- the aggregate is computable by counting
rows without reading obligation descriptions.

**Phase 0 Exit Condition Registry:**

| EC-ID | Exit Condition | Required Artifact | Status |
|-------|----------------|-------------------|--------|
| EC-01 | Scope gate declared -- event tuple (entity, operation, field bounds) | SCOPE GATE | SATISFIED |
| EC-02 | Artifact manifest locked -- all structural artifacts assigned ART-NN IDs | ARTIFACT MANIFEST | SATISFIED |
| EC-03 | Breach token protocol declared -- named format and CLOSURE CHECK counter reserved | BREACH TOKEN PROTOCOL | SATISFIED |
| EC-04 | Execution Order Rule table declared -- at least two EOR-NN rules | EOR TABLE | SATISFIED |
| EC-05 | Cascade depth budget declared -- named integer MAX and depth counter format | CASCADE DEPTH BUDGET | SATISFIED |

**Exit signal computation:** Count rows where `Status = SATISFIED`. EXIT SIGNAL is
authorized when count = 5/5. Current aggregate: **5/5 SATISFIED**.

```
PHASE 0 EXIT SIGNAL
Aggregate: 5/5 SATISFIED (EC-01 SATISFIED, EC-02 SATISFIED, EC-03 SATISFIED,
           EC-04 SATISFIED, EC-05 SATISFIED)
Exit signal is COMPUTABLE: recompute by counting Status column -- no semantic
re-evaluation required.
Enumeration may begin. Phase 1 authorized.
```

*An output that replaces this aggregate with a narrative assertion such as "all conditions
met" without typed per-row Status values fails C-27 and is tagged
`[EXIT SIGNAL UNCOMPUTABLE: aggregate absent | FM-38]`.*

#### EC-01 -- SCOPE GATE

| Slot | Value |
|------|-------|
| Entity type | account (Dynamics 365 Sales) |
| Operation | Update |
| Triggering field | statecode (Active=0 -> Inactive=1) |
| Excluded operations | Create, Delete, other field updates |

A trigger candidate is IN SCOPE if and only if its activation condition intersects this
event tuple.

#### EC-02 -- ARTIFACT MANIFEST

| ART-ID | Artifact Name | Locked By | Used By |
|--------|---------------|-----------|---------|
| ART-01 | SCOPE GATE | Phase 0 | Denominator scan, CLOSURE CHECK |
| ART-02 | EXCLUSION LOG | Phase 1 | CLOSURE CHECK EC-REF-02 |
| ART-03 | PROHIBITION CONTRACTS | Phase 1 | Role prohibitions, breach tokens |
| ART-04 | EOR TABLE | Phase 0 | All firing entries (EOR-NN citations) |
| ART-05 | CASCADE DEPTH BUDGET | Phase 0 | All cascade entries, storm verdict |
| ART-06 | STRUCTURAL INVARIANT | Protocol Preamble | All entry types |
| ART-07 | INERTIA CONTRAST | Phase 1 | Design rationale for ART-03, ART-04 |

#### EC-03 -- BREACH TOKEN PROTOCOL

Named breach token: `[PROHIBITION BREACH: Role {N} | {violated prohibition name}]`

CLOSURE CHECK counter reserved: "PROHIBITION BREACHES: {count} [must be 0]" resolves
against ART-03.

#### EC-04 -- EXECUTION ORDER RULE TABLE (ART-04)

| EOR-ID | Platform Ordering Rule | Applies To |
|--------|----------------------|------------|
| EOR-01 | Synchronous plug-in steps execute before async steps within the same triggering event | Sync vs. async tier split |
| EOR-02 | Pre-operation plug-in steps execute before post-operation steps within the sync tier | Sync firing entries |
| EOR-03 | Within the async tier, Power Automate automated flows execute after Dataverse async plug-in steps | Async firing entries |
| EOR-04 | Chained cascades inherit their parent's tier; async parent produces async cascade | Cascade entries |

Every firing entry SHALL carry `Positioned because: EOR-{NN}`. Missing citation:
`[EOR MISS: entry-name | FM-17]`.

#### EC-05 -- CASCADE DEPTH BUDGET (ART-05)

```
MAX_CASCADE_DEPTH = 4
Counter format: [Depth: N/4] on every cascade entry
Overflow entry: [DEPTH EXCEEDED] terminates any chain reaching Depth 5/4
Storm verdict EXPLICITLY checks: depth-exceeded chain count DE (must be 0 for CLEAN)
```

---

### LIFECYCLE OVERVIEW

```
FORMAL-GATE ZONE DECLARATION -- THE LIFECYCLE OVERVIEW TABLE

Rule 1: This DECLARATION governs all entry-condition and exit-condition cells in The
LIFECYCLE OVERVIEW table. The STRUCTURAL INVARIANT LAYER (Invariant 3) is co-authoritative.
No artifact surface is exempt from this co-authority's formal-register obligation.

Rule 2: All entry-condition and exit-condition cells SHALL use formal obligation language
(SHALL/MUST). A non-conforming cell is subject to Rule 3's self-tagging requirement
(FM-17 for register drift, FM-21 for the absent FM code).

Rule 3: A non-conforming untagged gate cell constitutes a double violation and SHALL be
tagged [DOUBLE VIOLATION: FM-17 + FM-21 | cell description] inline.

Rule 4: A reader verifying this table SHALL check each gate cell independently against
Rules 2 and 3. Row N conformance does not imply Row N+1 conformance, which together apply
independently to every gate-bearing phase body regardless of whether prior phase bodies
have been verified as conformant.
```

| Phase | Name | Entry Condition | Job Description | Exit Condition |
|-------|------|-----------------|-----------------|----------------|
| 0 | Pre-Enumeration Gate | Phase 0 SHALL begin when: input record change specification received | Lock all structural artifacts; populate Phase 0 Exit Condition Registry with typed Status values; issue computable EXIT SIGNAL when aggregate = 5/5 SATISFIED | Phase 0 SHALL be declared complete when: EXIT SIGNAL issued and aggregate = 5/5 SATISFIED |
| 1 | Pre-scan | Phase 1 SHALL begin when: Phase 0 EXIT SIGNAL issued (5/5 SATISFIED) | Identify all candidate triggers; declare denominator N; open all three anomaly question slots OPEN; issue PCC-1 | Phase 1 SHALL be declared complete when: N declared, all three anomaly slots OPEN, PCC-1 issued |
| 2 | Sync Trigger Enumeration | Phase 2 SHALL begin when: Phase 1 complete, N declared, PCC-1 issued | Enumerate all sync-tier candidates using FIRING ENTRY or NON-FIRING ENTRY schema; include negative vocabulary example; order by priority | Phase 2 SHALL be declared complete when: all sync-tier candidates have resolved entries with all schema slots populated |
| 3 | Async Trigger Enumeration | Phase 3 SHALL begin when: Phase 2 complete and Sync Trigger Table produced | Enumerate all async-tier candidates using schema; annotate latency tier per entry | Phase 3 SHALL be declared complete when: all async-tier candidates have resolved entries with all schema slots populated |
| 4 | Cascade Tracing | Phase 4 SHALL begin when: Phase 2 and Phase 3 complete and both trigger tables produced | Trace all cascade chains from side-effect field writes to terminal; assign chain IDs; apply back-edge detection | Phase 4 SHALL be declared complete when: all side-effect writes evaluated, all chains carry Chain-Status, back-edge detection applied |
| 5 | Anomaly Assessment | Phase 5 SHALL begin when: Phase 4 complete and all cascade chains carry Chain-Status | Deliver evidence-anchored verdicts for storm, missing trigger, circular trigger; propose remediation for each confirmed anomaly | Phase 5 SHALL be declared complete when: all three anomaly class verdicts issued with cited evidence and every confirmed anomaly has at least one remediation step |
| 6 | Trigger Map and Closure | Phase 6 SHALL begin when: Phase 5 complete and all anomaly verdicts issued | Produce trigger map with execution-tier and Spawns columns; perform denominator closure | Phase 6 SHALL be declared complete when: trigger map covers all triggers with required columns and denominator closure stated with CLOSED or GAP DETECTED |

---

### Phase 1 -- Pre-scan

**Entry condition:** Phase 1 SHALL begin when Phase 0 EXIT SIGNAL has been issued with
aggregate 5/5 SATISFIED. If Phase 0 EXIT SIGNAL is absent or aggregate < 5/5 SATISFIED,
Phase 1 SHALL NOT execute `[ENTRY CONDITION ABSENT: Phase 1 | FM-16]`.

**Job:** Identify all candidate triggers without condition filtering and declare denominator N;
open all three anomaly question slots with explicit OPEN status; issue Phrasing Clearance PCC-1.

**Anomaly Questions -- Status: OPEN**

| Anomaly Class | Question | Status |
|---------------|----------|--------|
| Trigger Storm | Does the account statecode change cause more triggers to fire than the environment's operational capacity can absorb? | OPEN |
| Missing Trigger | Is there an expected automation for this suspension transition that does not appear in the trigger surface? | OPEN |
| Circular Trigger | Does any trigger's output create a field write that re-activates the same or an upstream trigger? | OPEN |

**Denominator Pre-Scan:**

| Candidate Trigger | Flow Type | Activation Condition | Tier |
|------------------|-----------|---------------------|------|
| *[enumerate all candidates without filtering]* | | | |

Total candidate count N = *[integer -- declare before Phase 2 begins]*

**Exit condition:** Phase 1 SHALL be declared complete when N is declared, all three anomaly
question slots are explicitly marked OPEN, and PCC-1 is issued.

---

### Phase 2 -- Sync Trigger Enumeration

**Entry condition:** Phase 2 SHALL begin when Phase 1 is complete, N is declared, and PCC-1
is issued. If PCC-1 is absent, Phase 2 SHALL NOT execute
`[ENTRY CONDITION ABSENT: Phase 2 | FM-16]`.

**Job:** Enumerate all synchronous triggers. Every sync-tier candidate SHALL resolve to a
FIRING ENTRY or NON-FIRING ENTRY. At least one negative vocabulary example SHALL be included.
Order by execution priority, highest first.

**Negative vocabulary example (required):** `[VOCAB FAIL: "workflow" -> automated cloud flow | FM-08]`

**Sync Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 2 SHALL be declared complete when every sync-tier candidate has a
resolved entry with all schema slots populated and no blank slots remain.

---

### Phase 3 -- Async Trigger Enumeration

**Entry condition:** Phase 3 SHALL begin when Phase 2 is complete and the Sync Trigger
Table is produced.

**Job:** Enumerate all asynchronous triggers. Every async-tier candidate SHALL resolve to a
FIRING ENTRY or NON-FIRING ENTRY. Order by connector tier, then by priority. Annotate
latency tier (near-real-time / standard / batch) per entry.

**Async Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Latency Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|-------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 3 SHALL be declared complete when every async-tier candidate has a
resolved entry with all schema slots populated.

---

### Phase 4 -- Cascade Tracing

**Entry condition:** Phase 4 SHALL begin when Phase 2 and Phase 3 are complete and both
trigger tables are produced.

**Job:** Trace every cascade chain originating from side-effect field writes to its terminal.
Each chain SHALL receive a Chain ID. The final row of each chain SHALL be marked [TERMINAL].
Back-edge detection SHALL be applied to the adjacency structure. Every cascade entry SHALL
carry a `[Depth: N/4]` counter against ART-05 budget.

**Cascade Chain Table:**

| Chain ID | Step | Originating Trigger | Side-Effect Action | Field Mutated | Downstream Trigger | Depth | Chain-Status |
|----------|------|--------------------|--------------------|---------------|-------------------|-------|-------------|

**Exit condition:** Phase 4 SHALL be declared complete when all side-effect writes are
evaluated, all chains carry Chain-Status, and back-edge detection has been applied.

---

### Phase 5 -- Anomaly Assessment

**Entry condition:** Phase 5 SHALL begin when Phase 4 is complete and all cascade chains
carry Chain-Status.

**Job:** Deliver evidence-anchored verdicts for all three anomaly classes. Each verdict SHALL
cite evidence from prior phases. Bare assertions SHALL be marked `[INSUFFICIENT | FM-12]`.
Every confirmed anomaly SHALL have at least one concrete remediation step.

| Anomaly Class | Verdict | Evidence (row/chain citations) | Remediation |
|---------------|---------|-------------------------------|-------------|
| Trigger Storm | DETECTED / NOT DETECTED | | |
| Missing Trigger | DETECTED / NOT DETECTED | | |
| Circular Trigger | DETECTED / NOT DETECTED | | |

**Exit condition:** Phase 5 SHALL be declared complete when all three anomaly class verdicts
are issued with cited evidence and every confirmed anomaly has at least one remediation step.

---

### Phase 6 -- Trigger Map and Closure

**Entry condition:** Phase 6 SHALL begin when Phase 5 is complete and all anomaly verdicts
are issued.

**Job:** Produce trigger map with execution-tier and Spawns columns. Perform denominator
closure: firing + non-firing + unresolved SHALL equal N.

**Trigger Map:**

| Trigger Name | Flow Type | Execution Tier | Fires On | Output Action | Spawns |
|-------------|-----------|----------------|----------|---------------|--------|

**Denominator Closure:**
Firing: {n1} + Non-firing: {n2} + Unresolved: {n3} = {N}
Status: CLOSED / GAP DETECTED

**Exit condition:** Phase 6 SHALL be declared complete when trigger map covers all triggers
with required columns and denominator closure is stated.

---

## V-02

**Variation axis:** Lifecycle emphasis -- per-obligation refutation conditions (C-28)
**Hypothesis:** When each Phase 0 obligation row carries a co-located `Violated if:` clause
naming a concrete, string-detectable breach condition, violation is detectable by structural
inspection without rubric re-scoring. This extends the C-24 breach-token principle upstream:
Phase 0 obligations become self-announcing violation detectors. A reader can scan for
"Violated if:" clauses and verify each one structurally -- no semantic re-evaluation required.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dynamics 365 Sales `account` record's `statecode` field has changed from `Active` (0) to
`Inactive` (1). Your task: determine exactly which automations fire, in what order, with what
inputs and outputs, and identify all trigger pathologies (storms, missing triggers, circular
triggers).

Execute the following phases in strict sequence. Each phase SHALL complete before the next
begins. No phase SHALL execute until all prior phases have issued their required outputs.

---

### PROTOCOL PREAMBLE

#### Platform Term Contract

Approved vocabulary:

| Approved Term | Prohibited Substitutions |
|--------------|-------------------------|
| automated cloud flow | workflow, automation, rule |
| instant cloud flow | manual flow, button flow |
| scheduled cloud flow | recurring flow, timer flow |
| Dataverse plug-in | plugin, CRM plugin, platform plugin |
| sync plug-in step | synchronous plugin, pre-stage plugin |
| async plug-in step | asynchronous plugin, background plugin |
| trigger event: When a row is added, modified or deleted | record trigger, update trigger |
| Power Automate connector | connector trigger, flow connector |

Any term deviating from this list SHALL be tagged `[VOCAB FAIL: "actual text" -> correction | FM-08]`.

#### FM Catalog

| FM Code | Failure Mode | Expected Behavior | Output Marker | Phase(s) |
|---------|-------------|-------------------|---------------|----------|
| FM-01 | Trigger omission | Every bound trigger listed by name | `[OMIT: trigger-name \| FM-01]` | 2, 3 |
| FM-02 | Firing order violation | Sync before async; by priority within tier | `[ORDER FAIL: actual \| FM-02]` | 2, 3 |
| FM-03 | Missing input/output specification | Named input payload and output action; no placeholders | `[IO FAIL: trigger-name \| FM-03]` | 2, 3 |
| FM-04 | Missing pathology coverage | All three pathology classes addressed | `[PATH MISS: class \| FM-04]` | 5 |
| FM-05 | False positive trigger | Only triggers scoped to this change | `[FALSE POS: trigger-name \| FM-05]` | 2, 3 |
| FM-06 | Shallow side effect trace | Cascade traced until no further triggers fire | `[CASCADE SHALLOW \| FM-06]` | 4 |
| FM-07 | Missing conditional branch | Firing and skipped branch both stated | `[BRANCH MISS: trigger-name \| FM-07]` | 2, 3 |
| FM-08 | Wrong platform vocabulary | Approved vocabulary used throughout | `[VOCAB FAIL: "actual" -> correction \| FM-08]` | All |
| FM-09 | Missing risk ranking | Pathologies ranked with one-line mitigation | `[RISK MISS \| FM-09]` | 5 |
| FM-10 | Missing timing annotation | Sync/async distinguished; latency noted | `[TIMING MISS: trigger-name \| FM-10]` | 2, 3 |
| FM-11 | Missing negative example | At least one wrong-vs-correct vocabulary pair | `[NEG MISS \| FM-11]` | 2 |
| FM-12 | Ungrounded pathology verdict | Verdict cites evidence; bare assertions are insufficient | `[INSUFFICIENT: evidence needed \| FM-12]` | 5 |
| FM-13 | Open cascade chain | Termination condition declared per chain | `[CHAIN OPEN: CH-NN \| FM-13]` | 4 |
| FM-14 | No trigger graph | Adjacency list trigger->field->trigger constructed | `[GRAPH MISS \| FM-14]` | 5 |
| FM-15 | No denominator declaration | Count N declared before condition filtering | `[DENOM MISS \| FM-15]` | 1 |
| FM-16 | Entry Condition Absent | A named phase carries no entry precondition | `[ENTRY CONDITION ABSENT: Phase N \| FM-16]` | All phases |
| FM-17 | Gate Register Drift | A gate statement uses descriptive language where SHALL/MUST is required | `[GATE REGISTER DRIFT: Phase N gate \| FM-17]` | All phases |
| FM-18 | No sync/async structural split | Sync and async triggers in separate enumeration phases | `[SPLIT MISS \| FM-18]` | 2, 3 |
| FM-19 | No back-edge detection | Back-edge detection applied to adjacency structure | `[BACKTRACK MISS \| FM-19]` | 5 |
| FM-20 | Missing terminal row marker | Each cascade chain closes with [TERMINAL] | `[CHAIN OPEN: CH-NN \| FM-20]` | 4 |
| FM-21 | FM code missing from violation cell | Every violation marker includes FM code | `[FM-21]` | All |
| FM-22 | No denominator reconciliation | Closure verifies firing + non-firing + unresolved = N | `[RECON MISS \| FM-22]` | 6 |
| FM-24 | No side-effect slot | Side-effect slot in every firing trigger entry | `[SE MISS: trigger-name \| FM-24]` | 2, 3 |
| FM-25 | Missing trigger map | Trigger map with tier and cascade-link columns | `[MAP MISS \| FM-25]` | 6 |
| FM-26 | Co-authority partial verification | Verified against only one co-authoritative source | `[CO-AUTH PARTIAL: DECLARATION-only / Invariant-3-only \| FM-26]` | All |
| FM-39 | Refutation condition absent | A Phase 0 obligation carries no co-located "Violated if:" clause | `[REFUTATION ABSENT: EC-NN \| FM-39]` | Phase 0 |

#### Entry Schema Contract

All trigger entries SHALL conform to the FIRING ENTRY or NON-FIRING ENTRY schema defined in
the PROTOCOL PREAMBLE. A slot left blank is a schema violation.

**FIRING ENTRY** (all slots required):

```
Trigger Name:
Flow Type:
Execution Tier:     [sync | async | scheduled]
Trigger Event:
Input Fields:       [specific named fields]
Output Action:      [specific action]
Side Effects:       [field writes beyond primary output, or "none"]
Condition (Taken):
Condition (Skipped):
Anomaly Flag:       [none | storm | missing | circular]
```

**NON-FIRING ENTRY** (all slots required):

```
Trigger Name:
Flow Type:
Reason Not Firing:
Condition (Taken):  [what would cause this trigger to fire]
Condition (Skipped):[what blocks it in this scenario]
```

---

### STRUCTURAL INVARIANT LAYER

**Invariant 1 -- Phase body completeness:** Every phase body SHALL contain entry condition,
job description, and exit condition. `[ENTRY CONDITION ABSENT: Phase N | FM-16]`

**Invariant 2 -- Gate statement formal register:** All gate statements SHALL use
SHALL/MUST. `[GATE REGISTER DRIFT: Phase N gate | FM-17]`

**Invariant 3 -- LIFECYCLE OVERVIEW gate-cell register:** LIFECYCLE OVERVIEW gate cells
are co-governed by this INVARIANT LAYER and SHALL satisfy Invariant 2.
`[GATE REGISTER DRIFT: LIFECYCLE OVERVIEW Phase N entry/exit | FM-17]`

**Invariant 4 -- FM code in every violation marker:** `[FM-21]`

**Invariant 5 -- Denominator closure:** firing + non-firing + unresolved = N.
`[RECON MISS | FM-22]`

**Invariant 6 -- Co-authority verification:** Verify LIFECYCLE OVERVIEW cells against BOTH
FORMAL-GATE ZONE DECLARATION and Invariant 3 simultaneously. FM-26 and this invariant are
structurally coupled: without FM-26, this invariant has no enforcement mechanism; without
this invariant, FM-26 cannot activate as a meaningful catalog entry. The two SHALL be
declared together. `[CO-AUTH PARTIAL: DECLARATION-only / Invariant-3-only | FM-26]`

**Invariant 8 -- Refutation condition completeness:** Every Phase 0 obligation row SHALL
carry a co-located `Violated if:` clause naming a string-detectable breach condition. An
obligation row without a `Violated if:` clause is tagged `[REFUTATION ABSENT: EC-NN | FM-39]`.

---

### PHASE 0 -- Pre-Enumeration Gate

**Purpose:** Lock all structural artifacts and declare their refutation conditions before
any enumeration entry appears. Every pre-enumeration obligation carries a co-located
`Violated if:` clause -- a concrete, string-detectable statement of the breach condition.
A reader can detect violation of any Phase 0 obligation by structural inspection, without
rubric re-scoring.

**Refutation principle:** The `Violated if:` clause for each obligation specifies a condition
detectable by string match or structural scan against the output artifact. Obligation EC-NN
is violated if and only if the named condition is present or absent -- no semantic
re-evaluation required. This applies C-24's breach-token principle upstream to Phase 0:
violation is a named, detectable artifact property.

**Phase 0 Obligation Registry:**

---

**EC-01 -- SCOPE GATE**

| Slot | Value |
|------|-------|
| Entity type | account (Dynamics 365 Sales) |
| Operation | Update |
| Triggering field | statecode (Active=0 -> Inactive=1) |
| Excluded operations | Create, Delete, other field updates |

> **Violated if:** No SCOPE GATE section exists before the first enumeration entry, OR the
> scope declaration omits any of: entity type, operation, triggering field. Detectable by
> string scan: search for "SCOPE GATE" before first candidate row; if absent, EC-01 is
> violated. `[REFUTATION ABSENT: EC-01 | FM-39]` if this clause is missing.

---

**EC-02 -- ARTIFACT MANIFEST**

| ART-ID | Artifact Name | Locked By | Used By |
|--------|---------------|-----------|---------|
| ART-01 | SCOPE GATE | Phase 0 | Denominator scan, CLOSURE CHECK |
| ART-02 | EXCLUSION LOG | Phase 1 | CLOSURE CHECK |
| ART-03 | PROHIBITION CONTRACTS | Phase 1 | Breach tokens, CLOSURE CHECK |
| ART-04 | EOR TABLE | Phase 0 | Firing entries, CLOSURE CHECK |
| ART-05 | CASCADE DEPTH BUDGET | Phase 0 | Cascade entries, storm verdict |
| ART-06 | STRUCTURAL INVARIANT | Protocol Preamble | All entry types |
| ART-07 | INERTIA CONTRAST | Phase 1 | Design rationale |

> **Violated if:** No ARTIFACT MANIFEST table appears before the first enumeration entry,
> OR any ART-NN ID referenced by the CLOSURE CHECK is not present in this manifest. Detectable
> by string scan: search for "ART-" references in CLOSURE CHECK; verify each resolves to a
> row in this manifest. `[REFUTATION ABSENT: EC-02 | FM-39]` if this clause is missing.

---

**EC-03 -- BREACH TOKEN PROTOCOL**

Named breach token: `[PROHIBITION BREACH: Role {N} | {violated prohibition name}]`

CLOSURE CHECK counter: "PROHIBITION BREACHES: {count} [must be 0]" resolves against ART-03.

> **Violated if:** No named breach token format is declared before enumeration begins, OR
> the CLOSURE CHECK omits a PROHIBITION BREACHES counter. Detectable by string scan: search
> for "[PROHIBITION BREACH:" format declaration before first enumeration entry.
> `[REFUTATION ABSENT: EC-03 | FM-39]` if this clause is missing.

---

**EC-04 -- EXECUTION ORDER RULE TABLE (ART-04)**

| EOR-ID | Platform Ordering Rule | Applies To |
|--------|----------------------|------------|
| EOR-01 | Synchronous plug-in steps execute before async steps | Sync vs. async tier |
| EOR-02 | Pre-operation plug-in steps execute before post-operation steps within sync tier | Sync entries |
| EOR-03 | Power Automate automated flows execute after Dataverse async plug-in steps | Async entries |
| EOR-04 | Chained cascades inherit their parent's tier | Cascade entries |

> **Violated if:** No EOR TABLE appears before the first enumeration entry, OR fewer than
> two EOR-NN rules are declared. Detectable by string scan: search for "EOR-01" before first
> candidate row; if absent, EC-04 is violated. `[REFUTATION ABSENT: EC-04 | FM-39]` if this
> clause is missing.

---

**EC-05 -- CASCADE DEPTH BUDGET (ART-05)**

```
MAX_CASCADE_DEPTH = 4
Counter format: [Depth: N/4]
Overflow: [DEPTH EXCEEDED] at Depth 5/4
```

> **Violated if:** No CASCADE DEPTH BUDGET section names an integer MAX before the first
> enumeration entry, OR cascade entries appear without [Depth: N/MAX] counters. Detectable by
> string scan: search for "MAX_CASCADE_DEPTH" or "Depth:" before first cascade entry.
> `[REFUTATION ABSENT: EC-05 | FM-39]` if this clause is missing.

---

**PHASE 0 EXIT SIGNAL:**

```
All five obligations satisfied. Each carries a co-located "Violated if:" clause
detectable by string scan without rubric re-scoring.
EC-01 SCOPE GATE .................. SATISFIED (refutation condition co-located)
EC-02 ARTIFACT MANIFEST ........... SATISFIED (refutation condition co-located)
EC-03 BREACH TOKEN PROTOCOL ........ SATISFIED (refutation condition co-located)
EC-04 EOR TABLE ................... SATISFIED (refutation condition co-located)
EC-05 CASCADE DEPTH BUDGET ......... SATISFIED (refutation condition co-located)
Phase 0 EXIT SIGNAL: enumeration authorized.
```

---

### LIFECYCLE OVERVIEW

```
FORMAL-GATE ZONE DECLARATION -- THE LIFECYCLE OVERVIEW TABLE

Rule 1: This DECLARATION and Invariant 3 are co-authoritative over all LIFECYCLE OVERVIEW
gate cells. No artifact surface is exempt.

Rule 2: All entry-condition and exit-condition cells SHALL use SHALL/MUST.
Non-conforming cells are subject to Rule 3's self-tagging requirement
(FM-17 for register drift, FM-21 for absent FM code).

Rule 3: Non-conforming untagged gate cell = double violation.
Tag: [DOUBLE VIOLATION: FM-17 + FM-21 | cell description].

Rule 4: Each gate cell verified independently. Row N conformance does not imply Row N+1
conformance, which together apply independently to every gate-bearing phase body regardless
of whether prior phase bodies have been verified as conformant.
```

| Phase | Name | Entry Condition | Job Description | Exit Condition |
|-------|------|-----------------|-----------------|----------------|
| 0 | Pre-Enumeration Gate | Phase 0 SHALL begin when: input received | Lock all structural artifacts; declare refutation conditions per obligation | Phase 0 SHALL be declared complete when: all 5 obligations satisfied, each with co-located Violated if clause, and EXIT SIGNAL issued |
| 1 | Pre-scan | Phase 1 SHALL begin when: Phase 0 EXIT SIGNAL issued | Identify all candidates; declare N; open anomaly slots; issue PCC-1 | Phase 1 SHALL be declared complete when: N declared, slots OPEN, PCC-1 issued |
| 2 | Sync Trigger Enumeration | Phase 2 SHALL begin when: Phase 1 complete, N declared, PCC-1 issued | Enumerate sync-tier candidates with FIRING or NON-FIRING schema | Phase 2 SHALL be declared complete when: all sync candidates resolved with all slots populated |
| 3 | Async Trigger Enumeration | Phase 3 SHALL begin when: Phase 2 complete and Sync Trigger Table produced | Enumerate async-tier candidates; annotate latency tier | Phase 3 SHALL be declared complete when: all async candidates resolved with all slots populated |
| 4 | Cascade Tracing | Phase 4 SHALL begin when: Phase 2 and Phase 3 complete | Trace all cascade chains to terminal; apply back-edge detection | Phase 4 SHALL be declared complete when: all chains carry Chain-Status and back-edge detection applied |
| 5 | Anomaly Assessment | Phase 5 SHALL begin when: Phase 4 complete with all chains carrying Chain-Status | Deliver evidence-anchored verdicts for all three anomaly classes | Phase 5 SHALL be declared complete when: all three verdicts issued with cited evidence and remediations |
| 6 | Trigger Map and Closure | Phase 6 SHALL begin when: Phase 5 complete with all verdicts issued | Produce trigger map; perform denominator closure | Phase 6 SHALL be declared complete when: map complete with required columns and closure stated |

---

### Phase 1 through Phase 6

*[Phases 1-6 are structurally identical to V-01 above. The variation is confined to Phase 0.
Phase 1 entry gate references Phase 0 EXIT SIGNAL; all downstream phases are unchanged.]*

---

## V-03

**Variation axis:** Inertia framing -- INERTIA CONTRAST as typed inline columns (C-29)
**Hypothesis:** When `Weaker alternative` and `Failure mode` are typed column headers in
the Phase 0 obligation registry -- not a separate INERTIA CONTRAST section -- rationale is
non-separable from the mechanism it motivates. A reader examining any obligation row sees
the mechanism, its inertia-driven alternative, and the failure mode that alternative
produces, in one cell-level scan. Removing the INERTIA CONTRAST section cannot strip this
rationale because it does not live in a section.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dynamics 365 Sales `account` record's `statecode` field has changed from `Active` (0) to
`Inactive` (1). Your task: determine exactly which automations fire, in what order, with what
inputs and outputs, and identify all trigger pathologies (storms, missing triggers, circular
triggers).

Execute the following phases in strict sequence. Each phase SHALL complete before the next
begins. No phase SHALL execute until all prior phases have issued their required outputs.

---

### PROTOCOL PREAMBLE

#### Platform Term Contract

Approved vocabulary:

| Approved Term | Prohibited Substitutions |
|--------------|-------------------------|
| automated cloud flow | workflow, automation, rule |
| instant cloud flow | manual flow, button flow |
| scheduled cloud flow | recurring flow, timer flow |
| Dataverse plug-in | plugin, CRM plugin, platform plugin |
| sync plug-in step | synchronous plugin, pre-stage plugin |
| async plug-in step | asynchronous plugin, background plugin |
| trigger event: When a row is added, modified or deleted | record trigger, update trigger |
| Power Automate connector | connector trigger, flow connector |

Any term deviating from this list SHALL be tagged `[VOCAB FAIL: "actual text" -> correction | FM-08]`.

#### FM Catalog

| FM Code | Failure Mode | Expected Behavior | Output Marker | Phase(s) |
|---------|-------------|-------------------|---------------|----------|
| FM-01 | Trigger omission | Every bound trigger listed by name | `[OMIT: trigger-name \| FM-01]` | 2, 3 |
| FM-02 | Firing order violation | Sync before async; by priority within tier | `[ORDER FAIL: actual \| FM-02]` | 2, 3 |
| FM-03 | Missing input/output specification | Named input payload and output action; no placeholders | `[IO FAIL: trigger-name \| FM-03]` | 2, 3 |
| FM-04 | Missing pathology coverage | All three pathology classes addressed | `[PATH MISS: class \| FM-04]` | 5 |
| FM-05 | False positive trigger | Only triggers scoped to this change | `[FALSE POS: trigger-name \| FM-05]` | 2, 3 |
| FM-06 | Shallow side effect trace | Cascade traced until no further triggers fire | `[CASCADE SHALLOW \| FM-06]` | 4 |
| FM-07 | Missing conditional branch | Firing and skipped branch both stated | `[BRANCH MISS: trigger-name \| FM-07]` | 2, 3 |
| FM-08 | Wrong platform vocabulary | Approved vocabulary used throughout | `[VOCAB FAIL: "actual" -> correction \| FM-08]` | All |
| FM-09 | Missing risk ranking | Pathologies ranked with one-line mitigation | `[RISK MISS \| FM-09]` | 5 |
| FM-10 | Missing timing annotation | Sync/async distinguished; latency noted | `[TIMING MISS: trigger-name \| FM-10]` | 2, 3 |
| FM-11 | Missing negative example | At least one wrong-vs-correct vocabulary pair | `[NEG MISS \| FM-11]` | 2 |
| FM-12 | Ungrounded pathology verdict | Verdict cites evidence; bare assertions are insufficient | `[INSUFFICIENT: evidence needed \| FM-12]` | 5 |
| FM-13 | Open cascade chain | Termination condition declared per chain | `[CHAIN OPEN: CH-NN \| FM-13]` | 4 |
| FM-14 | No trigger graph | Adjacency list trigger->field->trigger constructed | `[GRAPH MISS \| FM-14]` | 5 |
| FM-15 | No denominator declaration | Count N declared before condition filtering | `[DENOM MISS \| FM-15]` | 1 |
| FM-16 | Entry Condition Absent | A named phase carries no entry precondition | `[ENTRY CONDITION ABSENT: Phase N \| FM-16]` | All phases |
| FM-17 | Gate Register Drift | A gate statement uses descriptive language where SHALL/MUST is required | `[GATE REGISTER DRIFT: Phase N gate \| FM-17]` | All phases |
| FM-18 | No sync/async structural split | Sync and async triggers in separate enumeration phases | `[SPLIT MISS \| FM-18]` | 2, 3 |
| FM-19 | No back-edge detection | Back-edge detection applied to adjacency structure | `[BACKTRACK MISS \| FM-19]` | 5 |
| FM-20 | Missing terminal row marker | Each cascade chain closes with [TERMINAL] | `[CHAIN OPEN: CH-NN \| FM-20]` | 4 |
| FM-21 | FM code missing from violation cell | Every violation marker includes FM code | `[FM-21]` | All |
| FM-22 | No denominator reconciliation | Closure verifies firing + non-firing + unresolved = N | `[RECON MISS \| FM-22]` | 6 |
| FM-24 | No side-effect slot | Side-effect slot in every firing trigger entry | `[SE MISS: trigger-name \| FM-24]` | 2, 3 |
| FM-25 | Missing trigger map | Trigger map with tier and cascade-link columns | `[MAP MISS \| FM-25]` | 6 |
| FM-26 | Co-authority partial verification | Verified against only one co-authoritative source | `[CO-AUTH PARTIAL: DECLARATION-only / Invariant-3-only \| FM-26]` | All |
| FM-40 | INERTIA CONTRAST columns absent from registry | Phase 0 registry lacks Weaker alternative / Failure mode column headers | `[CONTRAST COLS ABSENT: Phase 0 registry \| FM-40]` | Phase 0 |

#### Entry Schema Contract

*(Identical to V-01 FIRING ENTRY and NON-FIRING ENTRY schemas.)*

---

### STRUCTURAL INVARIANT LAYER

**Invariant 1-6:** *(Identical to V-01.)*

**Invariant 9 -- Phase 0 INERTIA CONTRAST column co-location:** The Phase 0 obligation
registry SHALL contain named column headers `Weaker alternative` and `Failure mode` (or
typed equivalents). Every obligation row SHALL carry non-empty values in both columns.
Rationale is co-located at the cell level -- not in a separate section. Removing a section
heading SHALL NOT remove the rationale for any mechanism.
**Violation taggable as: `[CONTRAST COLS ABSENT: Phase 0 registry | FM-40]`.**

---

### PHASE 0 -- Pre-Enumeration Gate

**Purpose:** Lock all structural artifacts before any enumeration entry appears. Every
obligation row in the registry carries typed `Weaker alternative` and `Failure mode` columns
so that design rationale is co-located with the mechanism at cell level -- not in a
separate INERTIA CONTRAST section that could be removed by deleting a heading.

**Column definition:**
- `Weaker alternative`: the inertia-driven pattern a simpler output would use
- `Failure mode`: the concrete, observable error that pattern produces when the stronger
  mechanism is absent

**Phase 0 Obligation Registry** (6 columns -- all required):

| EC-ID | Exit Condition | Required Artifact | Status | Weaker alternative | Failure mode |
|-------|----------------|-------------------|--------|-------------------|--------------|
| EC-01 | Scope gate declared -- event tuple (entity, operation, field bounds) | SCOPE GATE | SATISFIED | Narrative preamble: "This analysis covers account updates" | False-positive triggers from other operations appear as firing entries; out-of-scope candidates cannot be distinguished from in-scope candidates without platform knowledge |
| EC-02 | Artifact manifest locked -- all structural artifacts assigned ART-NN IDs | ARTIFACT MANIFEST | SATISFIED | CLOSURE CHECK references section headings by prose name ("see EXCLUSION LOG section above") | When the heading changes or is omitted, the CLOSURE CHECK counter resolves against an artifact that may not exist -- the counter is formally unverifiable without reading the full document |
| EC-03 | Breach token protocol declared -- named format and CLOSURE CHECK counter reserved | BREACH TOKEN PROTOCOL | SATISFIED | No breach token format; violations are detectable only by rubric re-scoring | A compliant output and a violating output are structurally identical from a reader's perspective -- prohibition compliance is claimed, not evidenced |
| EC-04 | Execution Order Rule table declared -- at least two EOR-NN rules | EOR TABLE | SATISFIED | Global ordering rationale stated once in preamble ("sync before async, priority within tier") | Without per-entry EOR citations, ordering correctness requires re-applying the global rule to every entry independently; two entries with the same tier may be misordered and the violation is undetectable without platform knowledge |
| EC-05 | Cascade depth budget declared -- named integer MAX and depth counter format | CASCADE DEPTH BUDGET | SATISFIED | No depth accounting; cascade chains noted as "multi-step" | Runaway chains are absorbed into the enumeration without a structural signal; storm verdict cannot reference a depth-exceeded entry count |

**Exit signal:** 5/5 SATISFIED -- enumeration authorized.

*An output where the Phase 0 registry lacks `Weaker alternative` and `Failure mode` column
headers is tagged `[CONTRAST COLS ABSENT: Phase 0 registry | FM-40]`. An output that
achieves C-26 via a standalone INERTIA CONTRAST section but has no contrast columns in
the obligation registry is a weak pass on C-29.*

---

### LIFECYCLE OVERVIEW

```
FORMAL-GATE ZONE DECLARATION -- THE LIFECYCLE OVERVIEW TABLE
Rules 1-4 identical to V-01.
```

| Phase | Name | Entry Condition | Job Description | Exit Condition |
|-------|------|-----------------|-----------------|----------------|
| 0 | Pre-Enumeration Gate | Phase 0 SHALL begin when: input received | Lock all structural artifacts; populate Phase 0 registry with 6-column entries including Weaker alternative and Failure mode | Phase 0 SHALL be declared complete when: all 5 obligation rows carry non-empty Weaker alternative and Failure mode values, and EXIT SIGNAL issued |
| 1-6 | *(phases 1-6 identical to V-01)* | | | |

---

### Phase 1 through Phase 6

*[Phases 1-6 structurally identical to V-01. Variation confined to Phase 0 registry columns.]*

---

## V-04

**Variation axis:** Role sequence + Output format -- computed inter-role gate (C-27 + role boundary)
**Hypothesis:** When Phase 0 is a structurally sealed Role 0 that issues a computable EXIT
SIGNAL (typed status aggregate, 5/5 SATISFIED), and Role 1 (Auditor) carries an entry gate
that resolves against that aggregate mechanically ("AUTHORIZED when Phase 0 aggregate = 5/5
SATISFIED"), the role-sequence gate is structurally verifiable before any content is evaluated.
The Auditor cannot begin without resolving the aggregate -- not just receiving an assertion.
This makes C-27's computability property load-bearing at the inter-role boundary, not just
internal to Phase 0.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dynamics 365 Sales `account` record's `statecode` field has changed from `Active` (0) to
`Inactive` (1). Your task: determine exactly which automations fire, in what order, with what
inputs and outputs, and identify all trigger pathologies (storms, missing triggers, circular
triggers).

Execute the following roles in strict sequence. Each role SHALL complete and issue its required
outputs before the next role begins. A role SHALL NOT begin unless the prior role's computed
exit aggregate is verifiable from the prior role's status column.

---

### ROLE 0 -- MANIFEST LOCK (SEALED)

**Role 0 is sealed.** It produces declaration and locking outputs only. It SHALL NOT execute
analysis. No other role SHALL reference artifacts not declared in Role 0.

**Role 0 output contract:** Role 0 SHALL produce a Phase 0 Exit Condition Registry with typed
`Status` values. Role 0 SHALL issue a COMPUTABLE EXIT SIGNAL stating the aggregate count of
SATISFIED rows. The exit signal SHALL be in the form: "N/5 SATISFIED -- enumeration
[authorized / NOT authorized]."

**Status type:** `EXIT-STATUS = {SATISFIED | PENDING | BLOCKED}`. The exit decision follows
mechanically from counting SATISFIED rows -- no interpretation required.

#### Phase 0 Exit Condition Registry (Role 0 output):

| EC-ID | Exit Condition | Required Artifact | Status |
|-------|----------------|-------------------|--------|
| EC-01 | Scope gate declared -- entity type, operation, triggering field bounds | SCOPE GATE | SATISFIED |
| EC-02 | Artifact manifest locked -- all structural artifacts assigned ART-NN IDs | ARTIFACT MANIFEST | SATISFIED |
| EC-03 | Breach token protocol declared -- named format and CLOSURE CHECK counter | BREACH TOKEN PROTOCOL | SATISFIED |
| EC-04 | Execution Order Rule table declared -- at least two EOR-NN rules | EOR TABLE | SATISFIED |
| EC-05 | Cascade depth budget declared -- named integer MAX and counter format | CASCADE DEPTH BUDGET | SATISFIED |

**Role 0 Computable Exit Signal:**

```
ROLE 0 EXIT SIGNAL (COMPUTABLE)
Status column aggregate: 5 rows examined, 5 SATISFIED, 0 PENDING, 0 BLOCKED
Aggregate: 5/5 SATISFIED
Exit decision: AUTHORIZED (derivable by counting Status column -- no semantic evaluation)
Role 1 (Auditor) is authorized to execute.
```

*Role 1 SHALL NOT begin until it can verify: count(Status = SATISFIED) = 5. If Role 0 issues
a narrative exit assertion without a typed status aggregate, Role 1 SHALL tag:
`[EXIT SIGNAL UNCOMPUTABLE: aggregate absent | FM-38]` and halt.*

---

**EC-01 -- SCOPE GATE**

| Slot | Value |
|------|-------|
| Entity type | account (Dynamics 365 Sales) |
| Operation | Update |
| Triggering field | statecode (Active=0 -> Inactive=1) |
| Excluded operations | Create, Delete, other field updates |

#### EC-02 -- ARTIFACT MANIFEST

| ART-ID | Artifact Name | Locked By | Used By |
|--------|---------------|-----------|---------|
| ART-01 | SCOPE GATE | Role 0 | Denominator scan, CLOSURE CHECK |
| ART-02 | EXCLUSION LOG | Role 1 | CLOSURE CHECK |
| ART-03 | PROHIBITION CONTRACTS | Role 1 | Breach tokens, CLOSURE CHECK |
| ART-04 | EOR TABLE | Role 0 | Firing entries, CLOSURE CHECK |
| ART-05 | CASCADE DEPTH BUDGET | Role 0 | Cascade entries, storm verdict |
| ART-06 | STRUCTURAL INVARIANT | Protocol Preamble | All entry types |
| ART-07 | INERTIA CONTRAST | Role 1 | Design rationale |

#### EC-03 -- BREACH TOKEN PROTOCOL

`[PROHIBITION BREACH: Role {N} | {violated prohibition name}]`
CLOSURE CHECK counter: "PROHIBITION BREACHES: {count} [must be 0]"

#### EC-04 -- EOR TABLE (ART-04)

| EOR-ID | Platform Ordering Rule | Applies To |
|--------|----------------------|------------|
| EOR-01 | Synchronous plug-in steps execute before async steps | Sync vs. async tier |
| EOR-02 | Pre-operation steps execute before post-operation steps within sync tier | Sync entries |
| EOR-03 | Automated flows execute after Dataverse async plug-in steps | Async entries |
| EOR-04 | Chained cascades inherit their parent's tier | Cascade entries |

#### EC-05 -- CASCADE DEPTH BUDGET (ART-05)

```
MAX_CASCADE_DEPTH = 4
Counter: [Depth: N/4] on every cascade entry
Overflow: [DEPTH EXCEEDED] at Depth 5/4
```

---

### ROLE 1 -- AUDITOR

**Role 1 entry gate (computable):**

Before Role 1 begins, resolve the following check mechanically from Role 0 output:

```
ROLE 1 ENTRY AUTHORIZATION CHECK
Step 1: Count rows in Role 0 Phase 0 Exit Condition Registry where Status = SATISFIED
Step 2: AUTHORIZED if count = 5; BLOCKED if count < 5
Current resolution: 5/5 SATISFIED -> AUTHORIZED
```

*This check resolves from the status column alone. If Role 0 issued a narrative exit
assertion without a typed status registry, this check CANNOT be resolved mechanically.
Tag: `[EXIT SIGNAL UNCOMPUTABLE: aggregate absent | FM-38]` and halt.*

**Role 1 is authorized.** Role 1 proceeds with: FM Catalog declaration, Verdict Taxonomy,
INERTIA CONTRAST, Exclusion Log, Prohibition Contracts, Structural Invariant, Ghost Denominator.

#### FM Catalog (Role 1 declares FM-01 through FM-40)

*(FM-01 through FM-26 as declared in golden prompt. FM-38-40 as declared in V-01/V-02/V-03.)*

#### INERTIA CONTRAST (ART-07)

| Mechanism | Weaker alternative | Failure mode |
|-----------|-------------------|--------------|
| ART-02 ARTIFACT MANIFEST with ART-ID keys | CLOSURE CHECK references section headings by prose name | Heading change or omission makes CLOSURE CHECK counter formally unverifiable |
| ART-04 EOR TABLE with per-entry EOR-NN citations | Global ordering rationale stated once in preamble | Misordered entries within same tier are undetectable without platform knowledge |

#### Verdict Taxonomy -- Term Set V

| Verdict | Code | Evidence Required |
|---------|------|------------------|
| FIRED | V-F | Activation condition matches event tuple AND trigger is enabled |
| CONFIRMED ABSENT | V-CA | Structural argument: scope exclusion, condition-FALSE, or reachability failure |
| FLAGGED MISSING | V-FM | Expected behavior suggests trigger should exist but cannot be confirmed |

#### Pre-Enumeration Exclusion Log (ART-02)

| Layer | Layer Type | Disposition | Reason (if Excluded) |
|-------|-----------|-------------|----------------------|
| Dataverse synchronous plug-in steps | Platform built-in | INCLUDED | In-scope |
| Dataverse asynchronous plug-in steps | Platform built-in | INCLUDED | In-scope |
| Power Automate automated flows | Connector-based | INCLUDED | Trigger on Dataverse row change is in scope |
| Power Automate instant flows | Connector-based | EXCLUDED | Require manual trigger |
| Scheduled flows | Connector-based | EXCLUDED | Not event-driven |
| Business rules | Platform built-in | EXCLUDED | Not triggers in automation graph sense |
| Copilot Studio topics (background) | Copilot layer | INCLUDED | If configured event-driven |

#### Prohibition Contracts (ART-03)

**PROHIBITION 03a:** Domain Expert role MAY NOT add new candidate entries to the ghost
denominator after the Auditor issues the denominator declaration.
`[PROHIBITION BREACH: Domain Expert | Prohibition-03a]`

**PROHIBITION 03b:** Domain Expert MAY NOT modify the SCOPE GATE definition (ART-01).
`[PROHIBITION BREACH: Domain Expert | Prohibition-03b]`

#### Structural Invariant (ART-06)

Every named slot in every entry template is required. An empty named slot is a structural gap.
"N/A" is not valid unless explicitly listed as an enum member.

#### Ghost Denominator Declaration

| GD-ID | Candidate Trigger | Flow / Step Type | Activation Condition | Verdict [V] |
|-------|-----------------|-----------------|---------------------|-------------|
| GD-01 | *[name]* | *[type]* | *[condition]* | *[V-F \| V-CA \| V-FM]* |

Total denominator N = *[integer]*

**AUDITOR DECLARATION:** Role 1 entry authorization verified (5/5 SATISFIED from Role 0
status aggregate). Domain Expert (Role 2) execution authorized.

---

### ROLE 2 -- DOMAIN EXPERT (Power Automate / Copilot Studio)

**Role 2 entry condition:** Auditor Declaration issued. Role 2 SHALL NOT modify ART-01, ART-02,
or ART-04.

**Execute phases 1-6** (Pre-scan, Sync Trigger Enumeration, Async Trigger Enumeration,
Cascade Tracing, Anomaly Assessment, Trigger Map and Closure) using the full phase specifications
from V-01 above. All phases are governed by the LIFECYCLE OVERVIEW and STRUCTURAL INVARIANT
LAYER declared in Role 1.

---

## V-05

**Variation axis:** Output format + Inertia framing -- unified 6-column Phase 0 registry (C-27 + C-28 + C-29)
**Hypothesis:** When all three new criteria are unified in a single Phase 0 registry table
with 6 named columns -- EC-ID, Exit Condition, Required Artifact, Status, Violated if,
Weaker alternative, Failure mode -- every obligation row is simultaneously: (a) self-computing
(status column drives exit signal aggregate), (b) self-detecting (Violated if clause names the
string-detectable breach), and (c) self-motivating (inline contrast columns explain why the
obligation exists). An evaluator checking Phase 0 never needs to consult an external section:
the table is sufficient for full evaluation.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dynamics 365 Sales `account` record's `statecode` field has changed from `Active` (0) to
`Inactive` (1). Your task: determine exactly which automations fire, in what order, with what
inputs and outputs, and identify all trigger pathologies (storms, missing triggers, circular
triggers).

Execute the following phases in strict sequence. Each phase SHALL complete before the next
begins. No phase SHALL execute until all prior phases have issued their required outputs.

---

### PROTOCOL PREAMBLE

#### Platform Term Contract

Approved vocabulary:

| Approved Term | Prohibited Substitutions |
|--------------|-------------------------|
| automated cloud flow | workflow, automation, rule |
| instant cloud flow | manual flow, button flow |
| scheduled cloud flow | recurring flow, timer flow |
| Dataverse plug-in | plugin, CRM plugin, platform plugin |
| sync plug-in step | synchronous plugin, pre-stage plugin |
| async plug-in step | asynchronous plugin, background plugin |
| trigger event: When a row is added, modified or deleted | record trigger, update trigger |
| Power Automate connector | connector trigger, flow connector |

Any term deviating from this list SHALL be tagged `[VOCAB FAIL: "actual text" -> correction | FM-08]`.

#### FM Catalog

| FM Code | Failure Mode | Expected Behavior | Output Marker | Phase(s) |
|---------|-------------|-------------------|---------------|----------|
| FM-01 | Trigger omission | Every bound trigger listed by name | `[OMIT: trigger-name \| FM-01]` | 2, 3 |
| FM-02 | Firing order violation | Sync before async; by priority within tier | `[ORDER FAIL: actual \| FM-02]` | 2, 3 |
| FM-03 | Missing input/output specification | Named input payload and output action; no placeholders | `[IO FAIL: trigger-name \| FM-03]` | 2, 3 |
| FM-04 | Missing pathology coverage | All three pathology classes addressed | `[PATH MISS: class \| FM-04]` | 5 |
| FM-05 | False positive trigger | Only triggers scoped to this change | `[FALSE POS: trigger-name \| FM-05]` | 2, 3 |
| FM-06 | Shallow side effect trace | Cascade traced until no further triggers fire | `[CASCADE SHALLOW \| FM-06]` | 4 |
| FM-07 | Missing conditional branch | Firing and skipped branch both stated | `[BRANCH MISS: trigger-name \| FM-07]` | 2, 3 |
| FM-08 | Wrong platform vocabulary | Approved vocabulary used throughout | `[VOCAB FAIL: "actual" -> correction \| FM-08]` | All |
| FM-09 | Missing risk ranking | Pathologies ranked with one-line mitigation | `[RISK MISS \| FM-09]` | 5 |
| FM-10 | Missing timing annotation | Sync/async distinguished; latency noted | `[TIMING MISS: trigger-name \| FM-10]` | 2, 3 |
| FM-11 | Missing negative example | At least one wrong-vs-correct vocabulary pair | `[NEG MISS \| FM-11]` | 2 |
| FM-12 | Ungrounded pathology verdict | Verdict cites evidence; bare assertions are insufficient | `[INSUFFICIENT: evidence needed \| FM-12]` | 5 |
| FM-13 | Open cascade chain | Termination condition declared per chain | `[CHAIN OPEN: CH-NN \| FM-13]` | 4 |
| FM-14 | No trigger graph | Adjacency list trigger->field->trigger constructed | `[GRAPH MISS \| FM-14]` | 5 |
| FM-15 | No denominator declaration | Count N declared before condition filtering | `[DENOM MISS \| FM-15]` | 1 |
| FM-16 | Entry Condition Absent | A named phase carries no entry precondition | `[ENTRY CONDITION ABSENT: Phase N \| FM-16]` | All phases |
| FM-17 | Gate Register Drift | A gate statement uses descriptive language where SHALL/MUST is required | `[GATE REGISTER DRIFT: Phase N gate \| FM-17]` | All phases |
| FM-18 | No sync/async structural split | Sync and async triggers in separate enumeration phases | `[SPLIT MISS \| FM-18]` | 2, 3 |
| FM-19 | No back-edge detection | Back-edge detection applied to adjacency structure | `[BACKTRACK MISS \| FM-19]` | 5 |
| FM-20 | Missing terminal row marker | Each cascade chain closes with [TERMINAL] | `[CHAIN OPEN: CH-NN \| FM-20]` | 4 |
| FM-21 | FM code missing from violation cell | Every violation marker includes FM code | `[FM-21]` | All |
| FM-22 | No denominator reconciliation | Closure verifies firing + non-firing + unresolved = N | `[RECON MISS \| FM-22]` | 6 |
| FM-24 | No side-effect slot | Side-effect slot in every firing trigger entry | `[SE MISS: trigger-name \| FM-24]` | 2, 3 |
| FM-25 | Missing trigger map | Trigger map with tier and cascade-link columns | `[MAP MISS \| FM-25]` | 6 |
| FM-26 | Co-authority partial verification | Verified against only one co-authoritative source | `[CO-AUTH PARTIAL: DECLARATION-only / Invariant-3-only \| FM-26]` | All |
| FM-38 | Phase 0 exit signal not computable | EXIT SIGNAL is a narrative assertion without typed status aggregate | `[EXIT SIGNAL UNCOMPUTABLE: aggregate absent \| FM-38]` | Phase 0 |
| FM-39 | Refutation condition absent | A Phase 0 obligation carries no co-located "Violated if:" clause | `[REFUTATION ABSENT: EC-NN \| FM-39]` | Phase 0 |
| FM-40 | INERTIA CONTRAST columns absent from registry | Phase 0 registry lacks Weaker alternative / Failure mode column headers | `[CONTRAST COLS ABSENT: Phase 0 registry \| FM-40]` | Phase 0 |

#### Entry Schema Contract

*(Identical to V-01 FIRING ENTRY and NON-FIRING ENTRY schemas.)*

---

### STRUCTURAL INVARIANT LAYER

**Invariant 1 -- Phase body completeness:** `[ENTRY CONDITION ABSENT: Phase N | FM-16]`
**Invariant 2 -- Gate statement formal register:** `[GATE REGISTER DRIFT: Phase N gate | FM-17]`
**Invariant 3 -- LIFECYCLE OVERVIEW gate-cell register:** `[GATE REGISTER DRIFT: LIFECYCLE OVERVIEW Phase N entry/exit | FM-17]`
**Invariant 4 -- FM code in every violation marker:** `[FM-21]`
**Invariant 5 -- Denominator closure:** firing + non-firing + unresolved = N. `[RECON MISS | FM-22]`
**Invariant 6 -- Co-authority verification:** FM-26 and this invariant are structurally coupled:
without FM-26, this invariant has no enforcement mechanism; without this invariant, FM-26 cannot
activate. The two SHALL be declared together. `[CO-AUTH PARTIAL | FM-26]`

**Invariant 10 -- Phase 0 registry unified completeness:** The Phase 0 obligation registry SHALL
contain 7 named column headers: EC-ID, Exit Condition, Required Artifact, Status, Violated if,
Weaker alternative, Failure mode. Every row SHALL carry non-empty values in all 7 columns. The
EXIT SIGNAL SHALL reference the count of Status = SATISFIED rows (C-27). Each "Violated if"
clause SHALL name a string-detectable breach condition (C-28). The "Weaker alternative" and
"Failure mode" columns SHALL contain mechanism-specific content, not generic descriptions (C-29).
An output missing any column header: `[CONTRAST COLS ABSENT: Phase 0 registry | FM-40]`.
An output with narrative EXIT SIGNAL: `[EXIT SIGNAL UNCOMPUTABLE: aggregate absent | FM-38]`.
An output with a missing "Violated if" clause: `[REFUTATION ABSENT: EC-NN | FM-39]`.

---

### PHASE 0 -- Pre-Enumeration Gate

**Purpose and column contract:** Every pre-enumeration obligation appears in the unified
Phase 0 registry below. The registry has 7 named columns. Each row is simultaneously:
- **Self-computing** (Status column drives the exit signal aggregate -- C-27)
- **Self-detecting** ("Violated if" clause names a string-detectable breach -- C-28)
- **Self-motivating** ("Weaker alternative" and "Failure mode" columns embed rationale at
  cell level -- C-29)

The Phase 0 table is sufficient for full evaluation of all three new criteria. No external
section is required.

**Status type:** `EXIT-STATUS = {SATISFIED | PENDING | BLOCKED}`. Exit signal is authorized
when and only when all rows show Status = SATISFIED. Aggregate is recomputable by counting
the Status column.

**Unified Phase 0 Obligation Registry** (7 columns -- all required):

| EC-ID | Exit Condition | Required Artifact | Status | Violated if | Weaker alternative | Failure mode |
|-------|----------------|-------------------|--------|-------------|-------------------|--------------|
| EC-01 | Scope gate declared -- entity type, operation, triggering field bounds | SCOPE GATE | SATISFIED | No SCOPE GATE section exists before the first enumeration entry, OR entity type / operation / field bounds are absent. Detectable: string-search for "SCOPE GATE" before first GD- or SEQ- row. | Narrative preamble: "This analysis covers account updates" with no structured tuple | False-positive candidates from other operations enter the denominator; out-of-scope triggers cannot be distinguished from in-scope without platform knowledge |
| EC-02 | Artifact manifest locked -- all structural artifacts assigned ART-NN IDs | ARTIFACT MANIFEST | SATISFIED | No ARTIFACT MANIFEST table exists before first enumeration entry, OR any ART-NN ID cited in CLOSURE CHECK is absent from this manifest. Detectable: string-search "ART-" in CLOSURE CHECK; verify each resolves to a manifest row. | CLOSURE CHECK references section headings by prose ("see EXCLUSION LOG section above") | When the heading changes or is omitted, the CLOSURE CHECK counter resolves against an artifact that may not exist; formally unverifiable without scanning the full document |
| EC-03 | Breach token protocol declared -- named format and CLOSURE CHECK counter reserved | BREACH TOKEN PROTOCOL | SATISFIED | No named breach token format declaration exists before enumeration, OR CLOSURE CHECK omits PROHIBITION BREACHES counter. Detectable: string-search "[PROHIBITION BREACH:" format string before first enumeration entry. | No breach token format; violations detectable only by rubric re-scoring | A violating output and a compliant output are structurally identical; prohibition compliance is asserted, not evidenced |
| EC-04 | Execution Order Rule table declared -- at least two EOR-NN rules | EOR TABLE | SATISFIED | No EOR TABLE exists before first enumeration entry, OR fewer than two EOR-NN rules are declared. Detectable: string-search "EOR-01" before first SEQ- row. | Global ordering rationale stated once in preamble ("sync before async") | Without per-entry EOR citations, ordering correctness requires re-applying the global rule independently to every entry; misordered entries within the same tier are undetectable without platform knowledge |
| EC-05 | Cascade depth budget declared -- named integer MAX and depth counter format | CASCADE DEPTH BUDGET | SATISFIED | No CASCADE DEPTH BUDGET section names an integer MAX before first enumeration entry, OR cascade entries lack [Depth: N/MAX] counters. Detectable: string-search "MAX_CASCADE_DEPTH" before first cascade entry. | No depth accounting; cascade chains described as "multi-step" without numeric bound | Runaway chains are absorbed into the enumeration without a structural signal; the storm verdict cannot reference a depth-exceeded entry count; DE counter in storm assessment is ungrounded |

**Exit signal computation:** Scan Status column. Authorized when count(SATISFIED) = 5/5.

```
PHASE 0 EXIT SIGNAL (UNIFIED -- COMPUTABLE / SELF-DETECTING / SELF-MOTIVATING)
Status aggregate: 5/5 SATISFIED
  EC-01 SATISFIED | Violated-if clause: present | Contrast columns: populated
  EC-02 SATISFIED | Violated-if clause: present | Contrast columns: populated
  EC-03 SATISFIED | Violated-if clause: present | Contrast columns: populated
  EC-04 SATISFIED | Violated-if clause: present | Contrast columns: populated
  EC-05 SATISFIED | Violated-if clause: present | Contrast columns: populated
Exit decision: AUTHORIZED
Computability verified: exit decision derivable by counting Status column (C-27)
Violation detection verified: each obligation carries string-detectable breach condition (C-28)
Rationale co-location verified: Weaker alternative and Failure mode in every row (C-29)
Enumeration may begin. Phase 1 authorized.
```

---

### LIFECYCLE OVERVIEW

```
FORMAL-GATE ZONE DECLARATION -- THE LIFECYCLE OVERVIEW TABLE

Rule 1: This DECLARATION and Invariant 3 are co-authoritative over all LIFECYCLE OVERVIEW
gate cells. No artifact surface is exempt.

Rule 2: All entry-condition and exit-condition cells SHALL use SHALL/MUST.
Non-conforming cells subject to Rule 3's self-tagging requirement
(FM-17 for register drift, FM-21 for absent FM code).

Rule 3: Non-conforming untagged cell = double violation:
[DOUBLE VIOLATION: FM-17 + FM-21 | cell description].

Rule 4: Each gate cell verified independently. Row N conformance does not imply Row N+1
conformance, which together apply independently to every gate-bearing phase body regardless
of whether prior phase bodies have been verified as conformant.
```

| Phase | Name | Entry Condition | Job Description | Exit Condition |
|-------|------|-----------------|-----------------|----------------|
| 0 | Pre-Enumeration Gate | Phase 0 SHALL begin when: input record change specification received | Populate unified 7-column Phase 0 registry; issue computable EXIT SIGNAL from status aggregate | Phase 0 SHALL be declared complete when: all 5 registry rows carry Status = SATISFIED with non-empty Violated if and contrast columns, and EXIT SIGNAL issued with 5/5 aggregate |
| 1 | Pre-scan | Phase 1 SHALL begin when: Phase 0 EXIT SIGNAL issued with aggregate 5/5 SATISFIED | Identify all candidate triggers; declare N; open anomaly slots; issue PCC-1 | Phase 1 SHALL be declared complete when: N declared, all three anomaly slots OPEN, PCC-1 issued |
| 2 | Sync Trigger Enumeration | Phase 2 SHALL begin when: Phase 1 complete, N declared, PCC-1 issued | Enumerate all sync-tier candidates using FIRING ENTRY or NON-FIRING ENTRY schema; include negative vocabulary example | Phase 2 SHALL be declared complete when: all sync candidates resolved with all schema slots populated |
| 3 | Async Trigger Enumeration | Phase 3 SHALL begin when: Phase 2 complete and Sync Trigger Table produced | Enumerate all async-tier candidates; annotate latency tier | Phase 3 SHALL be declared complete when: all async candidates resolved with all schema slots populated |
| 4 | Cascade Tracing | Phase 4 SHALL begin when: Phase 2 and Phase 3 complete and both tables produced | Trace all cascade chains to terminal; assign chain IDs; apply back-edge detection | Phase 4 SHALL be declared complete when: all side-effect writes evaluated, all chains carry Chain-Status, back-edge detection applied |
| 5 | Anomaly Assessment | Phase 5 SHALL begin when: Phase 4 complete with all chains carrying Chain-Status | Deliver evidence-anchored verdicts for storm, missing trigger, circular trigger | Phase 5 SHALL be declared complete when: all three verdicts issued with cited evidence and confirmed anomalies have remediation steps |
| 6 | Trigger Map and Closure | Phase 6 SHALL begin when: Phase 5 complete with all verdicts issued | Produce trigger map with execution-tier and Spawns columns; perform denominator closure | Phase 6 SHALL be declared complete when: trigger map complete and denominator closure stated |

---

### Phase 1 -- Pre-scan

**Entry condition:** Phase 1 SHALL begin when Phase 0 EXIT SIGNAL has been issued with
aggregate 5/5 SATISFIED (verified from status column, not asserted). If Phase 0 EXIT
SIGNAL absent or aggregate < 5/5: `[ENTRY CONDITION ABSENT: Phase 1 | FM-16]`.

**Job:** Identify all candidate triggers without filtering; declare denominator N; open all
three anomaly question slots; issue PCC-1.

**Anomaly Questions -- Status: OPEN**

| Anomaly Class | Question | Status |
|---------------|----------|--------|
| Trigger Storm | Does the account statecode change cause more triggers to fire than the environment's operational capacity can absorb? | OPEN |
| Missing Trigger | Is there an expected automation for this suspension transition that does not appear? | OPEN |
| Circular Trigger | Does any trigger's output create a field write that re-activates an upstream trigger? | OPEN |

**Denominator Pre-Scan:**

| Candidate Trigger | Flow Type | Activation Condition | Tier |
|------------------|-----------|---------------------|------|
| *[enumerate all candidates without filtering]* | | | |

Total candidate count N = *[integer]*

**Exit condition:** Phase 1 SHALL be declared complete when N is declared, all three anomaly
question slots are explicitly marked OPEN, and PCC-1 is issued.

---

### Phase 2 -- Sync Trigger Enumeration

**Entry condition:** Phase 2 SHALL begin when Phase 1 is complete, N declared, PCC-1 issued.
If PCC-1 absent: `[ENTRY CONDITION ABSENT: Phase 2 | FM-16]`.

**Job:** Enumerate all synchronous triggers. Every sync-tier candidate SHALL resolve to a
FIRING ENTRY or NON-FIRING ENTRY. Include at least one negative vocabulary example.
Order by execution priority, highest first.

**Negative vocabulary example (required):** `[VOCAB FAIL: "workflow" -> automated cloud flow | FM-08]`

**Sync Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 2 SHALL be declared complete when every sync-tier candidate has a
resolved entry with all schema slots populated and no blank slots remain.

---

### Phase 3 -- Async Trigger Enumeration

**Entry condition:** Phase 3 SHALL begin when Phase 2 is complete and Sync Trigger Table produced.

**Job:** Enumerate all asynchronous triggers. Order by connector tier, then priority. Annotate
latency tier per entry.

**Async Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Latency Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|-------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 3 SHALL be declared complete when all async-tier candidates have
resolved entries with all schema slots populated.

---

### Phase 4 -- Cascade Tracing

**Entry condition:** Phase 4 SHALL begin when Phase 2 and Phase 3 are complete and both
trigger tables are produced.

**Job:** Trace every cascade chain to its terminal. Assign chain IDs. Mark final row of each
chain [TERMINAL]. Apply back-edge detection. Every cascade entry carries [Depth: N/4] counter
against ART-05 budget.

**Cascade Chain Table:**

| Chain ID | Step | Originating Trigger | Side-Effect Action | Field Mutated | Downstream Trigger | Depth | Chain-Status |
|----------|------|--------------------|--------------------|---------------|-------------------|-------|-------------|

**Exit condition:** Phase 4 SHALL be declared complete when all side-effect writes are
evaluated, all chains carry Chain-Status, and back-edge detection has been applied.

---

### Phase 5 -- Anomaly Assessment

**Entry condition:** Phase 5 SHALL begin when Phase 4 is complete with all chains carrying
Chain-Status.

**Job:** Deliver evidence-anchored verdicts for all three anomaly classes. Cite evidence from
prior phases. Every confirmed anomaly SHALL have at least one concrete remediation step.

| Anomaly Class | Verdict | Evidence (row/chain citations) | Remediation |
|---------------|---------|-------------------------------|-------------|
| Trigger Storm | DETECTED / NOT DETECTED | | |
| Missing Trigger | DETECTED / NOT DETECTED | | |
| Circular Trigger | DETECTED / NOT DETECTED | | |

**Exit condition:** Phase 5 SHALL be declared complete when all three verdicts are issued with
cited evidence and every confirmed anomaly has at least one remediation step.

---

### Phase 6 -- Trigger Map and Closure

**Entry condition:** Phase 6 SHALL begin when Phase 5 is complete with all verdicts issued.

**Job:** Produce trigger map with execution-tier and Spawns columns. Perform denominator
closure.

**Trigger Map:**

| Trigger Name | Flow Type | Execution Tier | Fires On | Output Action | Spawns |
|-------------|-----------|----------------|----------|---------------|--------|

**Denominator Closure:**
Firing: {n1} + Non-firing: {n2} + Unresolved: {n3} = {N}
Status: CLOSED / GAP DETECTED

**Exit condition:** Phase 6 SHALL be declared complete when trigger map covers all triggers
with required columns and denominator closure is stated.
