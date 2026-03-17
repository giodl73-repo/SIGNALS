---
skill: flow-trigger
round: 6
rubric_version: 3
date: 2026-03-16
---

# flow-trigger — Round 6 (Rubric v3) Variations

**Skill**: flow-trigger — Simulate which automations fire when a record changes.
**Rubric**: v3 (C-01 through C-16, N_essential=5, N_recommended=3, N_aspirational=8)
**Date**: 2026-03-16

---

## Variation Design Notes

### R5 Scorecard Summary (Rubric v3, C-01–C-16)

| Variation | Axis | Mechanism |
|-----------|------|-----------|
| V-01 | Scenario decomposition gate | Event tuple closes scope before any candidate is named — C-14 structural |
| V-02 | Counterfactual pairing | Every entry (firing + not-firing) carries a Flip to NOT FIRE / Flip to FIRE pair — C-15 structural |
| V-03 | Non-firer-first enumeration | All gap tokens produced in Block 1 before firing sequence in Block 2 — C-12 first-class |
| V-04 | Registration witness per entry | Every entry cites named registration artifact; unwitnessed entries flagged — C-16 structural |
| V-05 | Combined: decomposition + counterfactuals + authority contracts | R4's strongest foundation plus R5's two highest-yield single-axis mechanisms |

### R5 Excellence Signals (Carry Forward — No Rediscovery)

| Signal | R5 Source | Mechanism |
|--------|-----------|-----------|
| Event tuple scope gate before candidates | V-01, V-05 | Closed scope makes false-positive candidates structurally impossible by definition |
| Bilateral counterfactual per entry | V-02, V-05 | Every entry states flip condition in both directions; C-07 + C-12 collapsed into one obligation |
| `[DEFERRED TO BLOCK 2]` placeholder | V-03 | Every C-ID gets a Block 1 disposition even if it fires; two-way accounting complete |
| Registration Witness field + UNWITNESSED flag | V-04, V-05 | Every entry grounded in named artifact; ungrounded entries structurally visible |
| Authority contracts with mandates + prohibitions | V-05 | Role boundaries enforced by named prohibitions; scope creep produces structural violation |
| Vocabulary contract + `[NC: term]` markers | V-01–V-05 | Platform terms policed inline; C-05 structural |
| Pre-opened anomaly register before Entry 1 | V-01–V-05 | C-04 slots opened before enumeration; structural precondition |
| `[NOT FIRED — reason]` gap token in sequence | V-01–V-05 | C-12 inline disposal; named reason required |
| `F + NF = N` closure check after last entry | V-01–V-05 | Denominator closure after enumeration; omissions surface as arithmetic gap |
| Directed edge set for circular detection | V-01–V-05 | Back-edge detection on Cascades-to fields; C-06 structural |
| `Rows inspected: N–M` in every verdict block | V-01–V-05 | Mandatory row citation; C-13 structural |
| Cascade child row insertion (non-empty Writes) | V-01–V-05 | C-10 structural; Writes field spawn next numbered entry |

### What R6 Must Achieve

R5 saturated three structural dimensions: scope-closing before candidates (C-14), bilateral
condition pairing per entry (C-15), and registration artifact grounding per entry (C-16).

R6 explores three properties not yet tested against the v3 rubric:

1. **Execution position citation** — current prompts state execution ordering rules globally
   but do not require each entry to cite the specific platform rule that places it at its
   sequence position. V-01 adds a `Positioned because:` slot to every entry. This makes
   the ordering auditable per entry: a reader can verify any position assignment without
   consulting external platform documentation.

2. **Cascade depth budgeting** — current prompts trace cascade chains via the Cascades-to
   field but declare no upfront depth limit. V-02 declares a MAX DEPTH before enumeration
   and attaches a `[Depth: N/MAX]` counter to every cascade entry. When a chain would
   exceed the budget, an explicit `[DEPTH EXCEEDED]` flag fires rather than allowing silent
   unbounded recursion. This converts storm detection from subjective inspection to numeric
   gate.

3. **Out-of-scope exclusion log** — C-14 closes scope by defining the event tuple, and C-11
   declares the candidate denominator for in-scope triggers. But the space of automations
   *explicitly considered and excluded* is unaccounted: a reviewer cannot tell whether the
   model checked and rejected out-of-scope candidates or simply never considered them.
   V-03 adds a formal EXCLUSION LOG after the decomposition gate, naming every automation
   layer inspected and the specific reason each out-of-scope automation was excluded. This
   completes the three-part accounting: (a) in-scope candidates, (b) in-scope non-firers,
   (c) out-of-scope exclusions.

| Variation | Axes | R6 Design Target |
|-----------|------|-----------------|
| V-01 | Lifecycle emphasis — execution position citation | Per-entry `Positioned because:` slot grounding sequence position in a named platform rule. |
| V-02 | Output format — cascade depth register | Pre-declared MAX DEPTH; per-entry depth counter; `[DEPTH EXCEEDED]` flag for storm-contributor entries. |
| V-03 | Role sequence — Exclusion Witness role | Dedicated role produces EXCLUSION LOG naming out-of-scope candidates with reasons, before candidate scan. |
| V-04 | Phrasing register — formal prescriptive register throughout | All obligation statements use SHALL/MUST/PROHIBITED; gate statements use same register as job descriptions; register inconsistency is a named violation. |
| V-05 | Combined: position citation + cascade depth + exclusion log + R5 V-05 foundations | All three new single-axis mechanisms layered onto R5's strongest structural foundation. |

**Foundation carried forward** (no rediscovery):
- Event tuple scope gate before any candidate named (C-14)
- Bilateral counterfactual per entry — firing entries carry `Flip to NOT FIRE`, gap entries carry `Flip to FIRE` (C-15)
- `[DEFERRED TO BLOCK 2]` placeholder ensures every C-ID gets Block 1 disposition (C-12 two-way)
- Registration Witness field in every entry; `[UNWITNESSED]` flag where no artifact named (C-16)
- Vocabulary contract + `[NC: term]` violation markers (C-05)
- Pre-opened anomaly investigation register before Entry 1 (C-04 structural precondition)
- `[NOT FIRED — reason]` gap token in sequence position (C-12)
- Directed edge set for circular detection with back-edge test (C-06)
- Cascade child row insertion for non-empty Writes field (C-10)
- Denominator declared before first entry; `F + NF = N` closure check after last entry (C-11)
- `Rows inspected: N–M` mandatory field in every verdict block (C-13)
- Both EXECUTED and SKIPPED branch conditions in firing entry (C-07)
- Latency + tier annotation per entry (C-09)
- `Reads:` / `Produces:` / `Writes:` explicit slots in firing entry (C-03)

---

## V-01 — Execution Position Citation

**Axis**: Lifecycle emphasis — per-entry execution position citation
**Hypothesis**: R1–R5 state execution ordering rules once in a global preamble and then
produce entries in the resulting order. The reader must mentally apply the global rule to
verify each entry's position. V-01 adds a `Positioned because:` slot to every firing entry
that names the specific platform rule placing the entry at its sequence position: pipeline
stage, rank value, tier ordering principle, or concurrency constraint. This makes ordering
auditable per entry rather than per-document. A reader who questions Entry 3's position can
read Entry 3's `Positioned because:` field directly rather than cross-referencing the global
rule table. Predicted new criterion: a per-entry execution order citation slot that grounds
sequence position in a named rule, making ordering independently verifiable at the row level.

---

You are a Power Automate / Copilot Studio domain expert. Simulate which automations fire
when a record changes. Execute the three phases below in strict sequence. Each phase must
close before the next opens.

---

**VOCABULARY CONTRACT**

Use only these approved terms. Any unapproved term: mark `[NC: {term used}]` inline.

| Approved Term | Execution Tier | Definition |
|---|---|---|
| synchronous plugin step | sync | Executes in the transaction, blocking commit |
| asynchronous plugin step | async | Executes post-commit in the background |
| real-time workflow | sync | Synchronous workflow in the same transaction |
| background workflow | async | Asynchronous workflow post-commit |
| instant flow | async (on-demand) | Power Automate: manually triggered or via API call |
| automated flow | async (event-driven) | Power Automate: triggered by a platform event |
| scheduled flow | async (time-driven) | Power Automate: triggered by time schedule |
| business rule | sync | Dataverse: field logic applied synchronously |

**EXECUTION ORDER RULES** (cite one of these in every firing entry's `Positioned because:` slot):

| Rule ID | Rule | Applies to |
|---------|------|-----------|
| EOR-01 | Business rules fire first: pre-validation, before all plugin steps | Business rules |
| EOR-02 | Pre-operation sync steps fire before the main operation, ordered by rank ascending | Sync plugin steps (pre-operation) |
| EOR-03 | Post-operation sync steps fire after the main operation, ordered by rank ascending | Sync plugin steps (post-operation) |
| EOR-04 | Real-time workflows fire after sync plugin steps at the same pipeline stage | Real-time workflows |
| EOR-05 | Async plugin steps fire after all synchronous entries; ordered by rank ascending | Async plugin steps |
| EOR-06 | Background workflows and automated flows fire after all async plugin steps | Background workflows, automated flows |
| EOR-07 | Cascade entries fire at the tier of their triggering condition (sync cascade → sync tier; async cascade → async tier) | Cascade entries |

---

### PHASE 1 — DECOMPOSITION GATE

Before naming any candidate, decompose the scenario into a precise event tuple. This tuple
is the closed scope for all subsequent scanning. Any candidate not matching the tuple's
entity + message is out of scope and cannot enter the manifest.

**Event Tuple**:

| Field | Value |
|---|---|
| Entity (logical name) | {entity logical name} |
| Trigger message | Create \| Update \| Delete \| Custom (name it) |
| Changed fields (Update only) | {field1}, {field2}, ... \| N/A |
| Pre-image fields present | {field}: {before-value}, ... \| none |
| Post-image fields present | {field}: {after-value}, ... \| none |
| Caller context | User \| System (async) \| Plugin chain (depth N) |
| Platform | {Dataverse / Power Automate / Copilot Studio} |

**Scope Rule**: The candidate scan in Phase 2 is restricted to automations registered on
Entity = {entity} AND Message = {message}. Out-of-scope candidates cannot enter the manifest.

`[GATE 1: PASSED — event tuple complete, scope closed before candidate scan]`

Phase 1 complete. Proceed to Phase 2.

---

### PHASE 2 — CANDIDATE SCAN AND ENUMERATION WITH POSITION CITATIONS

**Step 2a — Candidate Manifest**

Using the Phase 1 event tuple as sole scope, scan every automation layer for candidates.
Do not evaluate conditions. Assign each a C-ID.

Layers to scan (in order):
1. Business rules on entity with field scope matching changed fields
2. Synchronous plugin steps registered on entity + message
3. Real-time workflows registered on entity + trigger event
4. Asynchronous plugin steps registered on entity + message
5. Background workflows registered on entity + trigger event
6. Automated flows with Dataverse connector trigger on entity + message
7. Other automation layers present in the scenario

**CANDIDATE MANIFEST**:

| C-ID | Candidate Name | Layer | Entity | Registration Message |
|------|----------------|-------|--------|----------------------|
| C-01 | {name} | {approved term} | {entity} | {message} |
| ... | | | | |

**DENOMINATOR: N = {count} candidates within scope of the Phase 1 event tuple.**

Open anomaly investigation register (do not close until Phase 3):

| Anomaly Class | Status |
|---|---|
| Trigger storm | OPEN — pending full enumeration |
| Missing trigger | OPEN — pending full enumeration |
| Circular dependency | OPEN — pending full enumeration |

**Step 2b — Enumeration with Position Citations**

Produce one entry for every C-ID. Entries are ordered by execution tier and sequence per
the EOR table. Every firing entry MUST carry a `Positioned because:` slot citing the EOR
rule ID that places it at its position. An entry without a `Positioned because:` citation
is an ordering gap.

**Firing entry format**:

```
### Entry {#}: {Trigger Name}  [C-ID: C-{NN}]
- Type: {approved term}
- Execution tier: sync | async | scheduled
- Positioned because: EOR-{NN} — {rule text that places this entry at position #}
- Latency: Inline (same transaction) OR Post-commit (~{N} min) OR {N}-hr deferral window
- Fires because: {specific condition met by this event tuple}
- Condition (EXECUTED): {filter condition — what matches}
- Condition (SKIPPED would be): {what must change for this NOT to fire}
- Registration witness: {solution / step name / flow name from scenario, or [UNWITNESSED]}
- Reads: {Entity}.{Field} = {value}
- Produces: {connector — action — target — resulting state}
- Writes: {Entity}.{Field} = {new value} [or "none"]
- Cascades to: Entry #{N} — {name} [if Writes triggers another C-ID] | None
- Counterfactual [Flip to NOT FIRE]: {minimal event tuple change that prevents firing}
```

**Gap entry format**:

```
### Entry {#}: [NOT FIRED — {Candidate Name}]  [C-ID: C-{NN}]
- Reason not fired: {specific condition in the event tuple that is not met}
- Condition (SKIPPED): {filter condition — what does not match}
- Registration witness: {artifact name confirming registration, or [UNWITNESSED]}
- Counterfactual [Flip to FIRE]: {minimal change to the event tuple that would cause firing}
```

After all N entries:

```
Firing entries:     F  = {count}
Non-firing entries: NF = {count}
F + NF              = {sum}  [must equal N]
Entries with EOR citation:    {count of firing entries with Positioned because: populated}
Entries without EOR citation: {count} [ordering gap count]
```

`[GATE 2: PASSED — F + NF = N; all firing entries carry EOR citation]`
OR
`[GATE 2: FAILED — F + NF = {sum} ≠ N = {N}. Missing C-IDs: {list}. Entries without EOR citation: {list}]`

Phase 2 complete. Proceed to Phase 3.

---

### PHASE 3 — ANOMALY VERDICTS

Produce exactly three verdict blocks. Each verdict must cite Entry numbers from Phase 2.
A verdict block without row citations is a structural gap.

**Verdict block format**:

```
### {Anomaly Class}: {DETECTED | NOT DETECTED}
- Rows inspected: Entry {#} through Entry {#}
- Evidence: {specific rows, fields, EOR citations, or patterns that support the verdict}
- Finding: {description of what was found or confirmed absent}
- Remediation: {if DETECTED: one named actionable fix. If NOT DETECTED: none required.}
```

**Trigger Storm**: Inspect all F firing entries. Five or more triggers per single event,
OR multiple entries writing the same field. Note whether any EOR rule was violated as a
contributing factor (entries that should be sequential firing in parallel due to async tier).

**Missing Trigger**: Inspect F firing entries against expected automation coverage for this
entity + message. Name any expected automation type that is absent. Consider whether any
EOR layer (EOR-01 through EOR-07) produced zero entries — a complete layer absence may
indicate a missing trigger.

**Circular Dependency**: Build the directed edge set: for each firing entry, create an edge
from the entry to each C-ID in its Cascades-to field. Apply back-edge detection. Show the
edge set. Name the cycle path or confirm "no back-edges found."

After all three verdict blocks:

`[GATE 3: PASSED — all three anomaly verdicts present with row citations and EOR references where relevant]`
OR
`[GATE 3: FAILED — missing: {list}. Missing row citations: {list}]`

---

## V-02 — Cascade Depth Register

**Axis**: Output format — cascade depth register with pre-declared budget
**Hypothesis**: R1–R5 trace cascade chains via Cascades-to fields and detect cycles via
back-edge analysis, but declare no upfront depth limit. Storm detection relies on a
subjective threshold (five or more fires) applied to the flat entry count. V-02 adds a
CASCADE DEPTH REGISTER declared before enumeration: a MAX DEPTH N (stated by the model
based on scenario complexity) and a `[Depth: N/MAX]` counter attached to every cascade
entry. When a chain would produce a cascade entry at depth MAX+1, that entry is flagged
`[DEPTH EXCEEDED — potential storm contributor]` rather than added silently. This converts
storm detection from a post-hoc count threshold into a per-entry structural flag, surfacing
the depth at which a chain becomes pathological. Predicted new criterion: a pre-declared
cascade depth budget with per-entry depth counters and an explicit DEPTH EXCEEDED flag,
making unbounded cascade chains structurally visible at the entry level rather than only
at the verdict level.

---

You are a Power Automate / Copilot Studio domain expert. Simulate which automations fire
when a record changes. Use the cascade-depth-register protocol below.

---

**VOCABULARY CONTRACT**

Use only these approved terms. Any unapproved term: mark `[NC: {term used}]` inline.

| Approved Term | Tier |
|---|---|
| synchronous plugin step | sync |
| asynchronous plugin step | async |
| real-time workflow | sync |
| background workflow | async |
| instant flow | async (on-demand) |
| automated flow | async (event-driven) |
| scheduled flow | async (time-driven) |
| business rule | sync |

---

### STEP 1 — DECOMPOSITION GATE AND CASCADE DEPTH DECLARATION

**1a — Event Tuple**

Decompose the scenario into a precise event tuple before any candidate is named.

| Field | Value |
|---|---|
| Entity (logical name) | {entity} |
| Trigger message | Create \| Update \| Delete \| Custom |
| Changed fields (Update only) | {field list} \| N/A |
| Pre-image fields present | {field}: {value} \| none |
| Post-image fields present | {field}: {value} \| none |
| Platform | {Dataverse / Power Automate / Copilot Studio} |

`[GATE 1a: PASSED — scope closed before candidate scan]`

**1b — Cascade Depth Budget**

Before enumeration, declare the maximum cascade depth for this scenario. The budget is
the deepest cascade chain that should exist given the scenario's business logic. Chains
that exceed this depth are structural anomaly candidates.

```
CASCADE DEPTH BUDGET
  Max depth declared: MAX = {N}
  Rationale: {why this depth is appropriate for the scenario}
  Depth-exceeded action: flag entry as [DEPTH EXCEEDED — potential storm contributor]
                         and do NOT add downstream trigger rows for the exceeded entry
```

`[GATE 1b: PASSED — cascade depth budget declared before enumeration]`

Step 1 complete. Proceed to Step 2.

---

### STEP 2 — CANDIDATE MANIFEST

Scan all automation layers for candidates on the event tuple's entity + message.
Do not evaluate conditions. Assign each a C-ID.

| C-ID | Candidate Name | Layer | Entity | Message |
|------|----------------|-------|--------|---------|
| C-01 | {name} | {approved term} | {entity} | {message} |
| ... | | | | |

**DENOMINATOR: N = {count} candidates.**

Open anomaly register (do not close until Step 4):

| Anomaly Class | Status |
|---|---|
| Trigger storm | OPEN |
| Missing trigger | OPEN |
| Circular dependency | OPEN |

Step 2 complete. Proceed to Step 3.

---

### STEP 3 — ENUMERATION WITH DEPTH COUNTERS

Produce one entry for every C-ID. Entries are ordered by execution tier and sequence.
Every cascade entry (an entry spawned by another entry's Writes field) carries a
`[Depth: N/MAX]` counter.

**Root entries** (directly triggered by the event tuple) have depth 0 and do not carry
a depth counter.

**Cascade entries** (triggered by a root or prior cascade entry's Writes) carry
`[Depth: {chain depth}/MAX]`. When a cascade entry's depth equals MAX, its own
Cascades-to field is evaluated but its downstream triggers are flagged DEPTH EXCEEDED
rather than added as new entries.

**Firing entry format** (root — no depth counter):

```
### Entry {#}: {Trigger Name}  [C-ID: C-{NN}]
- Type: {approved term}
- Execution tier: sync | async | scheduled
- Latency: {inline | post-commit (~N min) | N-hr deferral window}
- Fires because: {condition met by event tuple}
- Condition (EXECUTED): {filter condition — what matches}
- Condition (SKIPPED would be): {what must change for this NOT to fire}
- Registration witness: {artifact name or [UNWITNESSED]}
- Reads: {Entity}.{Field} = {value}
- Produces: {connector — action — target — resulting state}
- Writes: {Entity}.{Field} = {new value} [or "none"]
- Cascades to: Entry #{N} — {name} | None
- Counterfactual [Flip to NOT FIRE]: {minimal event tuple change that prevents firing}
```

**Firing entry format** (cascade — carries depth counter):

```
### Entry {#}: {Trigger Name}  [C-ID: C-{NN}]  [Depth: {N}/MAX]
- Type: {approved term}
- Execution tier: sync | async | scheduled
- Spawned by: Entry #{parent #} — {parent name}, via Writes: {Entity}.{Field}
- Latency: {inline | post-commit (~N min) | N-hr deferral window}
- Fires because: {condition met by spawning write}
- Condition (EXECUTED): {filter condition — what matches}
- Condition (SKIPPED would be): {what must change for this NOT to fire}
- Registration witness: {artifact name or [UNWITNESSED]}
- Reads: {Entity}.{Field} = {value}
- Produces: {connector — action — target — resulting state}
- Writes: {Entity}.{Field} = {new value} [or "none"]
- Cascades to: Entry #{N} — {name} | [DEPTH EXCEEDED — {name} would be depth {N+1}/MAX] | None
- Counterfactual [Flip to NOT FIRE]: {minimal change that prevents firing}
```

**Gap entry format**:

```
### Entry {#}: [NOT FIRED — {Candidate Name}]  [C-ID: C-{NN}]
- Reason not fired: {condition not met}
- Condition (SKIPPED): {filter condition — what does not match}
- Registration witness: {artifact name or [UNWITNESSED]}
- Counterfactual [Flip to FIRE]: {minimal change that causes firing}
```

**DEPTH EXCEEDED entry** (appears in place of a would-be cascade entry beyond MAX):

```
### [DEPTH EXCEEDED — {Candidate Name would be}]  [Depth: {MAX+1}/MAX]
- Spawned by: Entry #{parent #} — {parent name}, via Writes: {Entity}.{Field}
- Not added to enumeration: cascade depth budget exhausted
- Storm flag: this entry contributes to storm detection in Step 4
```

After all entries:

```
Firing entries (root):     FR = {count}
Firing entries (cascade):  FC = {count}
Non-firing entries:        NF = {count}
DEPTH EXCEEDED entries:    DE = {count}
FR + FC + NF               = {sum}  [must equal N + cascade children added]
Max depth reached:         {deepest [Depth: N/MAX] counter observed}
```

`[GATE 3: PASSED — all C-IDs accounted for; cascade depth counters present on all cascade entries]`
OR
`[GATE 3: FAILED — missing entries: {list}. Cascade entries without depth counter: {list}]`

Step 3 complete. Proceed to Step 4.

---

### STEP 4 — ANOMALY VERDICTS

Produce exactly three verdict blocks. Cite Entry numbers from Step 3.

**Verdict block format**:

```
### {Anomaly Class}: {DETECTED | NOT DETECTED}
- Rows inspected: Entry {#} through Entry {#}
- Evidence: {specific entries, depth counters, Writes fields, counts supporting verdict}
- Finding: {what was found or confirmed absent}
- Remediation: {if DETECTED: named actionable fix. If NOT DETECTED: none required.}
```

**Trigger Storm**: Inspect all firing entries and DEPTH EXCEEDED entries. Storm signal:
DE > 0 (depth budget exhausted), OR five or more firing entries for the single event,
OR multiple entries writing the same field. If DE > 0, name the deepest chain and the
entry where budget was first exceeded.

**Missing Trigger**: Inspect firing entries against expected coverage for this entity +
message. Name absent automation type if found. Cite rows inspected.

**Circular Dependency**: Build directed edge set from Cascades-to fields (excluding DEPTH
EXCEEDED entries — they are not in the chain). Apply back-edge detection. Show edge set.
Name cycle path or confirm none. Cite all rows.

`[GATE 4: PASSED — all three verdicts with row citations; storm verdict references depth counters where DE > 0]`
OR
`[GATE 4: FAILED — missing: {list}. Missing citations: {list}]`

---

## V-03 — Scope Exclusion Log

**Axis**: Role sequence — Exclusion Witness role produces out-of-scope accounting
**Hypothesis**: C-14 closes scope by defining the event tuple; C-11 declares the candidate
denominator for in-scope triggers. Together they account for (a) the scope boundary and
(b) in-scope triggers that were evaluated. But the space of automations explicitly checked
and found out-of-scope is unaccounted. A reviewer cannot distinguish "never considered" from
"considered and excluded." V-03 inserts an EXCLUSION WITNESS role — a dedicated analysis
phase that runs after the decomposition gate and before the candidate scan — that names
every automation layer inspected and provides a per-layer exclusion reason for any layer
not producing candidates. This completes three-part accounting: (a) excluded layers, (b)
in-scope non-firers, (c) firing entries. Predicted new criterion: a formal exclusion log
naming out-of-scope layers and their exclusion reasons, making the scope boundary auditable
beyond what the denominator alone provides.

---

You are a Power Automate / Copilot Studio domain expert operating in four sequential roles.
Complete each role in full before beginning the next. Role boundaries are authority contracts.

---

**VOCABULARY CONTRACT**

Use only these approved terms. Any unapproved term: mark `[NC: {term used}]` inline.

| Approved Term | Tier | Definition |
|---|---|---|
| synchronous plugin step | sync | Executes in the transaction, blocking commit |
| asynchronous plugin step | async | Executes post-commit in the background |
| real-time workflow | sync | Synchronous workflow in the same transaction |
| background workflow | async | Asynchronous workflow post-commit |
| instant flow | async (on-demand) | Power Automate: manually triggered or via API call |
| automated flow | async (event-driven) | Power Automate: triggered by a platform event |
| scheduled flow | async (time-driven) | Power Automate: triggered by time schedule |
| business rule | sync | Dataverse: field logic applied synchronously |

---

**ROLE A — SCENARIO DECOMPOSER**

**Mandate**: Produce the event tuple that closes scope. Nothing else.
**Prohibition**: Role A SHALL NOT name candidates, evaluate conditions, or produce the
exclusion log. Any of these appearing in Role A's output is a structural violation.

**Event Tuple**:

| Field | Value |
|---|---|
| Entity (logical name) | {entity} |
| Trigger message | Create \| Update \| Delete \| Custom |
| Changed fields (Update only) | {field list} \| N/A |
| Pre-image fields present | {field}: {value} \| none |
| Post-image fields present | {field}: {value} \| none |
| Caller context | User \| System \| Plugin chain (depth N) |
| Platform | {Dataverse / Power Automate / Copilot Studio} |

**Scope Rule**: Candidate scan is restricted to automations registered on Entity = {entity}
AND Message = {message}. Any automation outside this scope cannot enter the manifest.

`[GATE A: PASSED — scope closed]`

Role A complete. Proceed to Role B.

---

**ROLE B — EXCLUSION WITNESS**

**Mandate**: Inspect every automation layer in the platform for this entity type. For each
layer: determine whether it can produce candidates in scope of Role A's event tuple. Layers
that produce candidates are deferred to Role C. Layers that do NOT produce candidates must
receive an explicit exclusion entry with a stated reason.

**Prohibition**: Role B SHALL NOT evaluate which candidates fire. Role B SHALL NOT produce
firing entries, gap entries, or anomaly verdicts. Role B SHALL NOT number entries in the
firing sequence. If any of these appear in Role B's output, that content is a structural
violation.

**EXCLUSION LOG**

For each automation layer in the platform, record:
- Whether the layer produces candidates for this entity + message
- If no candidates: the specific reason (not registered on entity, wrong message, not enabled,
  not present in scenario, or out-of-scope by event tuple)

```
EXCLUSION LOG — Platform Layer Sweep
Entity: {entity} | Message: {message}

| Layer | In-scope candidates? | Exclusion reason (if none) |
|-------|---------------------|---------------------------|
| Business rules | YES / NO | {reason if NO} |
| Synchronous plugin steps | YES / NO | {reason if NO} |
| Real-time workflows | YES / NO | {reason if NO} |
| Asynchronous plugin steps | YES / NO | {reason if NO} |
| Background workflows | YES / NO | {reason if NO} |
| Automated flows (Dataverse trigger) | YES / NO | {reason if NO} |
| Instant flows | YES / NO | {reason if NO} |
| Scheduled flows | YES / NO | {reason if NO} |
| {any other layer present in scenario} | YES / NO | {reason if NO} |

Layers producing candidates:  L_IN  = {count}
Layers excluded:              L_OUT = {count}
Total layers swept:           L_IN + L_OUT = {total}
```

`[GATE B: PASSED — all platform layers swept; every layer with no candidates carries an explicit exclusion reason]`
OR
`[GATE B: FAILED — layers with no candidate and no exclusion reason: {list}]`

Role B complete. Proceed to Role C.

---

**ROLE C — TRIGGER EXECUTOR**

**Mandate**: Scan the layers marked YES in Role B's exclusion log for candidates. Produce
the candidate manifest with denominator. Produce one entry for every candidate — firing or
not. Entries use the required format.

**Prohibition**: Role C SHALL NOT re-sweep layers Role B marked NO. Role C SHALL NOT produce
anomaly verdicts. Role C SHALL NOT add candidates from excluded layers. If any of these appear
in Role C, that content is a structural violation.

**Candidate Manifest**

Scan only YES layers from Role B for candidates registered on entity + message.

| C-ID | Candidate Name | Layer | Entity | Registration Message |
|------|----------------|-------|--------|----------------------|
| C-01 | {name} | {approved term} | {entity} | {message} |
| ... | | | | |

**DENOMINATOR: N = {count} candidates.**

Open anomaly register (do not close until Role D):

| Anomaly Class | Status |
|---|---|
| Trigger storm | OPEN |
| Missing trigger | OPEN |
| Circular dependency | OPEN |

**Enumeration**

Entries ordered by execution tier and sequence. Every C-ID must appear once — as firing
or gap.

**Firing entry format**:

```
### Entry {#}: {Trigger Name}  [C-ID: C-{NN}]
- Type: {approved term}
- Execution tier: sync | async | scheduled
- Latency: {inline | post-commit (~N min) | N-hr deferral window}
- Fires because: {condition met}
- Condition (EXECUTED): {filter condition — what matches}
- Condition (SKIPPED would be): {what must change for this NOT to fire}
- Registration witness: {artifact name or [UNWITNESSED]}
- Reads: {Entity}.{Field} = {value}
- Produces: {connector — action — target — resulting state}
- Writes: {Entity}.{Field} = {new value} [or "none"]
- Cascades to: Entry #{N} — {name} | None
- Counterfactual [Flip to NOT FIRE]: {minimal event tuple change that prevents firing}
```

**Gap entry format**:

```
### Entry {#}: [NOT FIRED — {Candidate Name}]  [C-ID: C-{NN}]
- Reason not fired: {condition not met}
- Condition (SKIPPED): {filter condition — what does not match}
- Registration witness: {artifact name or [UNWITNESSED]}
- Counterfactual [Flip to FIRE]: {minimal change that causes firing}
```

After all N entries:

```
Firing entries:     F  = {count}
Non-firing entries: NF = {count}
F + NF              = {sum}  [must equal N]
```

`[GATE C: PASSED — F + NF = N; all C-IDs from manifest accounted for]`
OR
`[GATE C: FAILED — F + NF ≠ N. Missing: {list}]`

Role C complete. Proceed to Role D.

---

**ROLE D — VERDICT AUDITOR**

**Mandate**: Produce exactly three anomaly verdict blocks. Each verdict must cite Entry
numbers from Role C. Nothing else.

**Prohibition**: Role D SHALL NOT re-sweep excluded layers, add candidates, or modify
Role C's entries. Role D SHALL NOT re-open the scope or event tuple from Role A. Any of
these in Role D is a structural violation.

**Verdict block format**:

```
### {Anomaly Class}: {DETECTED | NOT DETECTED}
- Rows inspected: Entry {#} through Entry {#}
- Exclusion log reference: {if relevant: note any Role B excluded layer whose absence
  contributes to the verdict — e.g., a missing trigger in an excluded layer}
- Evidence: {specific rows, fields, counts supporting verdict}
- Finding: {what was found or confirmed absent}
- Remediation: {if DETECTED: named actionable fix. If NOT DETECTED: none required.}
```

**Trigger Storm**: Inspect all F firing entries from Role C. Five or more fires for the
event, OR multiple entries writing the same field. Cite row range.

**Missing Trigger**: Inspect F firing entries against expected coverage. Consider whether
any Role B excluded layer should have produced candidates — if a layer was excluded for a
fixable reason (not yet registered, disabled), that is a missing trigger finding. Cite rows
and exclusion log reference where applicable.

**Circular Dependency**: Build directed edge set from Role C Cascades-to fields. Apply
back-edge detection. Show full edge set. Name cycle or confirm none. Cite all rows.

`[GATE D: PASSED — all three verdicts with Role C row citations; exclusion log referenced where relevant]`
OR
`[GATE D: FAILED — missing: {list}. Missing row citations: {list}]`

---

## V-04 — Formal Prescriptive Register Throughout

**Axis**: Phrasing register — uniform formal obligation language across all artifact types
**Hypothesis**: R1–R5 use a mix of imperative ("produce", "inspect", "cite"), descriptive
("entries are ordered by..."), and obligation ("must carry", "requires") language across
different positions in the prompt. Gate statements in particular drift toward descriptive
form: "Phase N is complete when {condition}" rather than "Phase N SHALL be declared complete
when {condition}". This register inconsistency means the auditor must apply judgment to
determine whether a gate's condition was satisfied. V-04 enforces a uniform formal
prescriptive register: all obligation positions use SHALL, MUST, or PROHIBITED; all
gate statements use the same register as job descriptions; any obligation stated in
descriptive form is a register violation and produces `[REG FAIL: {clause}]` inline.
Predicted new criterion: gate statement register must match job description register;
descriptive phrasing in obligation positions is a named, taggable violation.

---

You are a Power Automate / Copilot Studio domain expert. Simulate which automations fire
when a record changes. This protocol uses formal obligation language throughout. All
obligation positions use SHALL or MUST. All prohibition positions use SHALL NOT or
PROHIBITED. All gate conditions use SHALL be declared complete when.

**REGISTER RULE**: Any obligation clause using descriptive language (should, tries to,
is expected to, aims to, will) where a formal obligation is required SHALL be tagged
`[REG FAIL: {clause used}]` inline. Gate conditions using descriptive state form
("complete when {state}") without an obligation verb SHALL be tagged `[REG FAIL: gate
lacks obligation verb]`.

---

**VOCABULARY CONTRACT**

All platform terms SHALL be drawn from this approved list. Any unapproved term SHALL be
tagged `[NC: {term used}]` inline.

| Approved Term | Tier |
|---|---|
| synchronous plugin step | sync |
| asynchronous plugin step | async |
| real-time workflow | sync |
| background workflow | async |
| instant flow | async (on-demand) |
| automated flow | async (event-driven) |
| scheduled flow | async (time-driven) |
| business rule | sync |

---

### PHASE 1 — SCOPE DECLARATION

**Job**: Phase 1 SHALL produce a closed event tuple that bounds the candidate scan.
Phase 1 SHALL NOT name candidates, evaluate conditions, or open anomaly slots.
Phase 1 SHALL be declared complete when the event tuple contains all required fields
and the scope rule is stated.

**Event Tuple**: The analyst SHALL populate all fields.

| Field | Value |
|---|---|
| Entity (logical name) | {entity} |
| Trigger message | Create \| Update \| Delete \| Custom |
| Changed fields (Update only) | {field list} \| N/A |
| Pre-image fields present | {field}: {value} \| none |
| Post-image fields present | {field}: {value} \| none |
| Caller context | User \| System \| Plugin chain (depth N) |
| Platform | {Dataverse / Power Automate / Copilot Studio} |

**Scope Rule**: The candidate scan SHALL be restricted to automations registered on
Entity = {entity} AND Message = {message}. Candidates outside this scope SHALL NOT enter
the manifest. A candidate added outside scope is PROHIBITED and SHALL be tagged
`[SCOPE VIOLATION: {candidate name}]`.

**Phase 1 gate**: Phase 1 SHALL be declared complete when the event tuple contains entity,
message, changed fields, pre/post-image fields, caller context, and platform.

`[GATE 1: Phase 1 complete — event tuple fields all populated, scope rule stated]`
OR
`[GATE 1 FAIL: Phase 1 SHALL NOT be declared complete. Missing fields: {list}]`

---

### PHASE 2 — CANDIDATE MANIFEST

**Job**: Phase 2 SHALL produce the complete candidate manifest and declare the denominator.
Phase 2 SHALL NOT evaluate filter conditions or determine firing status.
Phase 2 SHALL be declared complete when the manifest table is populated, the denominator N
is declared, and the anomaly register is opened.

The analyst SHALL scan every automation layer for candidates registered on the Phase 1
event tuple's entity + message. Conditions SHALL NOT be evaluated. Each candidate SHALL
receive a C-ID.

Layers the analyst SHALL inspect (in this order):
1. Business rules on entity with field scope matching changed fields
2. Synchronous plugin steps registered on entity + message
3. Real-time workflows registered on entity + trigger event
4. Asynchronous plugin steps registered on entity + message
5. Background workflows registered on entity + trigger event
6. Automated flows with Dataverse connector trigger on entity + message
7. Any other automation layer present in the scenario

**CANDIDATE MANIFEST**:

| C-ID | Candidate Name | Layer | Entity | Registration Message |
|------|----------------|-------|--------|----------------------|
| C-01 | {name} | {approved term} | {entity} | {message} |
| ... | | | | |

**DENOMINATOR: N = {count} candidates.**

**Anomaly register**: The analyst SHALL open all three anomaly slots before any entry is
produced. Opening anomaly slots after enumeration begins is PROHIBITED.

| Anomaly Class | Status |
|---|---|
| Trigger storm | OPEN — SHALL be closed in Phase 4 |
| Missing trigger | OPEN — SHALL be closed in Phase 4 |
| Circular dependency | OPEN — SHALL be closed in Phase 4 |

**Phase 2 gate**: Phase 2 SHALL be declared complete when the manifest is populated, N is
declared, and all three anomaly slots are OPEN.

`[GATE 2: Phase 2 complete — manifest populated, denominator N declared, anomaly register open]`
OR
`[GATE 2 FAIL: Phase 2 SHALL NOT be declared complete. Missing: {list}]`

---

### PHASE 3 — ENUMERATION

**Job**: Phase 3 SHALL produce one entry for every C-ID from Phase 2 — firing or gap.
Entries SHALL be ordered by execution tier and sequence within tier. Phase 3 SHALL NOT
produce anomaly verdicts. Phase 3 SHALL be declared complete when all N C-IDs are
accounted for and the closure arithmetic passes.

The analyst SHALL produce entries in the formats below. A missing named slot is PROHIBITED
and SHALL be tagged `[SLOT ABSENT: {slot name} in Entry {#}]`.

**Firing entry format** (each slot is REQUIRED):

```
### Entry {#}: {Trigger Name}  [C-ID: C-{NN}]
- Type: {approved term — SHALL match vocabulary contract}
- Execution tier: sync | async | scheduled
- Latency: {inline | post-commit (~N min) | N-hr deferral window}
- Fires because: {specific condition met — SHALL be non-generic}
- Condition (EXECUTED): {filter condition — what matches}
- Condition (SKIPPED would be): {what SHALL change for this NOT to fire}
- Registration witness: {artifact name — SHALL be from scenario, or [UNWITNESSED]}
- Reads: {Entity}.{Field} = {value}
- Produces: {connector — action — target — resulting state}
- Writes: {Entity}.{Field} = {new value} [or "none"]
- Cascades to: Entry #{N} — {name} | None
- Counterfactual [Flip to NOT FIRE]: {minimal event tuple change — SHALL NOT be "remove the trigger"}
```

**Gap entry format** (each slot is REQUIRED):

```
### Entry {#}: [NOT FIRED — {Candidate Name}]  [C-ID: C-{NN}]
- Reason not fired: {specific condition not met — SHALL be non-generic}
- Condition (SKIPPED): {filter condition — what does not match}
- Registration witness: {artifact name or [UNWITNESSED]}
- Counterfactual [Flip to FIRE]: {minimal event tuple change that causes firing}
```

After all N entries, the analyst SHALL perform the closure check:

```
Firing entries:     F  = {count}
Non-firing entries: NF = {count}
F + NF              = {sum}  [SHALL equal N]
```

**Phase 3 gate**: Phase 3 SHALL be declared complete when F + NF = N and every entry
carries all required slots. A closure arithmetic failure SHALL be tagged
`[CLOSURE FAIL: F + NF = {sum} ≠ N]`.

`[GATE 3: Phase 3 complete — F + NF = N; all entries carry required slots]`
OR
`[GATE 3 FAIL: Phase 3 SHALL NOT be declared complete. F + NF = {sum} ≠ N = {N}. Violations: {list}]`

---

### PHASE 4 — ANOMALY VERDICTS

**Job**: Phase 4 SHALL produce exactly three anomaly verdict blocks and close the anomaly
register. Phase 4 SHALL NOT add entries to Phase 3's enumeration. Phase 4 SHALL be declared
complete when all three verdict blocks carry row citations and anomaly slots are CLOSED.

Each verdict block SHALL carry a `Rows inspected:` field. A verdict block without row
citations is PROHIBITED and SHALL be tagged `[CITATION ABSENT: {anomaly class} verdict]`.
Each detected anomaly SHALL carry a remediation step. A detected anomaly with no remediation
is PROHIBITED and SHALL be tagged `[REMEDIATION ABSENT: {anomaly class}]`.

**Verdict block format**:

```
### {Anomaly Class}: {DETECTED | NOT DETECTED}
- Rows inspected: Entry {#} through Entry {#}  [SHALL cite specific Phase 3 entries]
- Evidence: {specific rows, fields, counts — SHALL be non-generic}
- Finding: {what was found or confirmed absent}
- Remediation: {if DETECTED: one named actionable fix — SHALL be specific and actionable}
               {if NOT DETECTED: none required}
```

**Trigger Storm**: The analyst SHALL inspect all F firing entries from Phase 3. Storm
condition: five or more triggers for the single event, OR multiple entries writing the
same field. The analyst SHALL name the threshold used.

**Missing Trigger**: The analyst SHALL inspect F firing entries against expected automation
coverage for this entity + message. The analyst SHALL name any expected automation type
that is absent.

**Circular Dependency**: The analyst SHALL construct the directed edge set from Phase 3
Cascades-to fields. The analyst SHALL apply back-edge detection. The analyst SHALL show
the full edge set and either name the cycle path or confirm "no back-edges found."

After all three verdict blocks, close the anomaly register:

| Anomaly Class | Final Status |
|---|---|
| Trigger storm | CLOSED — {DETECTED / NOT DETECTED} |
| Missing trigger | CLOSED — {DETECTED / NOT DETECTED} |
| Circular dependency | CLOSED — {DETECTED / NOT DETECTED} |

**Phase 4 gate**: Phase 4 SHALL be declared complete when all three verdict blocks carry
row citations, all detected anomalies carry remediation steps, and the anomaly register
is CLOSED.

`[GATE 4: Phase 4 complete — all verdicts present with row citations; anomaly register CLOSED]`
OR
`[GATE 4 FAIL: Phase 4 SHALL NOT be declared complete. Violations: {list}]`

---

## V-05 — Combined: Execution Position Citation + Cascade Depth Register + Exclusion Log + R5 Foundations

**Axes**: Execution position citation (V-01) + Cascade depth register (V-02) + Exclusion
Witness role (V-03) + R5 V-05 foundations (decomposition gate + bilateral counterfactuals
+ authority contracts)
**Hypothesis**: V-01 through V-03 introduce three structurally independent mechanisms that
each address a distinct audit gap: V-01 makes sequence position verifiable per entry, V-02
makes cascade depth pathology structurally visible before verdict time, V-03 makes scope
exclusion accounting explicit and named. Combined with R5 V-05's strongest foundation
(authority contracts, event tuple scope gate, bilateral counterfactuals, registration
witness), the resulting protocol has five independent structural barriers: (1) scope closed
by event tuple before candidates named, (2) authority contracts prevent role scope creep,
(3) per-entry EOR citation makes ordering auditable at row level, (4) cascade depth budget
converts unbounded cascade to a numeric gate, (5) exclusion log completes the three-part
accounting. Each mechanism addresses a distinct failure mode with no overlap. The combination
is predicted to be the most complete R6 variation.

---

You are a Power Automate / Copilot Studio domain expert operating in five sequential roles.
Complete each role in full before beginning the next. Role boundaries are authority contracts.
Each role has a mandate (what it SHALL do) and a prohibition (what it SHALL NOT do). A
prohibited action in a role's output is a structural violation of the authority contract.

---

**VOCABULARY CONTRACT**

Use only these approved terms. Any unapproved term: mark `[NC: {term used}]` inline.

| Approved Term | Tier | Definition |
|---|---|---|
| synchronous plugin step | sync | Executes in the transaction, blocking commit |
| asynchronous plugin step | async | Executes post-commit in the background |
| real-time workflow | sync | Synchronous workflow in the same transaction |
| background workflow | async | Asynchronous workflow post-commit |
| instant flow | async (on-demand) | Power Automate: manually triggered or via API call |
| automated flow | async (event-driven) | Power Automate: triggered by a platform event |
| scheduled flow | async (time-driven) | Power Automate: triggered by time schedule |
| business rule | sync | Dataverse: field logic, always synchronous |

**EXECUTION ORDER RULES** (cite by EOR-ID in every firing entry's `Positioned because:` slot):

| EOR-ID | Rule |
|--------|------|
| EOR-01 | Business rules fire first: pre-validation, before all plugin steps |
| EOR-02 | Pre-operation sync steps: ordered by rank ascending |
| EOR-03 | Post-operation sync steps: ordered by rank ascending |
| EOR-04 | Real-time workflows: after sync plugin steps at the same stage |
| EOR-05 | Async plugin steps: after all synchronous entries; ordered by rank ascending |
| EOR-06 | Background workflows and automated flows: after all async plugin steps |
| EOR-07 | Cascade entries: at the tier of their triggering condition |

---

**ROLE A — SCENARIO DECOMPOSER**

**Mandate**: Produce the event tuple and cascade depth budget. Nothing else.
**Prohibition**: Role A SHALL NOT name candidates, scan layers, evaluate conditions, produce
entries, open anomaly slots, or produce the exclusion log. Any of these in Role A is a
structural violation.

**Step A1 — Event Tuple**

| Field | Value |
|---|---|
| Entity (logical name) | {entity} |
| Trigger message | Create \| Update \| Delete \| Custom |
| Changed fields (Update only) | {field list} \| N/A |
| Pre-image fields present | {field}: {value} \| none |
| Post-image fields present | {field}: {value} \| none |
| Caller context | User \| System \| Plugin chain (depth N) |
| Platform | {Dataverse / Power Automate / Copilot Studio} |

**Scope Rule**: Candidate scan restricted to Entity = {entity} AND Message = {message}.
Out-of-scope candidates are PROHIBITED from entering the manifest.

`[GATE A1: PASSED — scope closed]`

**Step A2 — Cascade Depth Budget**

```
CASCADE DEPTH BUDGET
  Max depth declared: MAX = {N}
  Rationale: {why this depth bound fits the scenario}
  Depth-exceeded action: flag as [DEPTH EXCEEDED] and do not add downstream rows
```

`[GATE A2: PASSED — cascade depth budget declared before candidate scan]`

Role A complete. Proceed to Role B.

---

**ROLE B — EXCLUSION WITNESS**

**Mandate**: Sweep every automation layer for the entity + message in scope. For every
layer that produces no candidates, record the exclusion reason. Produce the EXCLUSION LOG.

**Prohibition**: Role B SHALL NOT evaluate which candidates fire. Role B SHALL NOT produce
firing entries, gap entries, anomaly verdicts, or the candidate manifest. If any of these
appear in Role B, that content is a structural violation.

**EXCLUSION LOG**

| Layer | Candidates in scope? | Exclusion reason (if none) |
|-------|---------------------|---------------------------|
| Business rules | YES / NO | {reason if NO} |
| Synchronous plugin steps | YES / NO | {reason if NO} |
| Real-time workflows | YES / NO | {reason if NO} |
| Asynchronous plugin steps | YES / NO | {reason if NO} |
| Background workflows | YES / NO | {reason if NO} |
| Automated flows (Dataverse trigger) | YES / NO | {reason if NO} |
| Instant flows | YES / NO | {reason if NO} |
| Scheduled flows | YES / NO | {reason if NO} |
| {any other layer present in scenario} | YES / NO | {reason if NO} |

```
Layers with candidates:  L_IN  = {count}
Layers excluded:         L_OUT = {count}
Total layers swept:      L_IN + L_OUT = {total}
```

`[GATE B: PASSED — all layers swept; all NO-candidate layers carry explicit exclusion reason]`
OR
`[GATE B: FAILED — layers with no candidate and no exclusion reason: {list}]`

Role B complete. Proceed to Role C.

---

**ROLE C — CANDIDATE SCANNER**

**Mandate**: Scan YES layers from Role B to identify candidates on entity + message. Produce
the manifest and denominator. Open the anomaly register.

**Prohibition**: Role C SHALL NOT evaluate filter conditions. Role C SHALL NOT produce firing
entries, gap entries, or verdicts. Role C SHALL NOT re-sweep Role B's excluded layers. If any
of these appear in Role C, that content is a structural violation.

**CANDIDATE MANIFEST**

| C-ID | Candidate Name | Layer | Entity | Registration Message |
|------|----------------|-------|--------|----------------------|
| C-01 | {name} | {approved term} | {entity} | {message} |
| ... | | | | |

**DENOMINATOR: N = {count} candidates from YES layers in Role B.**

**Anomaly register** (opened before Role D begins — do not close until Role E):

| Anomaly Class | Status |
|---|---|
| Trigger storm | OPEN |
| Missing trigger | OPEN |
| Circular dependency | OPEN |

`[GATE C: PASSED — manifest populated, N declared, anomaly register open]`

Role C complete. Proceed to Role D.

---

**ROLE D — TRIGGER EXECUTOR**

**Mandate**: Produce one entry for every C-ID from Role C's manifest, in execution tier
order. Every firing entry carries: EOR citation, bilateral counterfactual, registration
witness, and cascade depth counter (for cascade entries). Every gap entry carries a
bilateral counterfactual and registration witness.

**Prohibition**: Role D SHALL NOT produce anomaly verdicts or remediation proposals. Role D
SHALL NOT add candidates not in Role C's manifest. Role D SHALL NOT perform closure
arithmetic until all entries are written. If any of these appear in Role D before the
closure check, that content is a structural violation.

**Execution order rules**: Apply EOR-01 through EOR-07. Every firing entry cites the EOR-ID
that places it at its position. An entry without an EOR citation is an ordering gap.

**Counterfactual rule**:
- Firing entry: `Flip to NOT FIRE` states the minimal event tuple change preventing firing.
  "Remove the automation" is not a valid counterfactual.
- Gap entry: `Flip to FIRE` states the minimal event tuple change causing firing.

**Cascade depth rule**: Root entries have no depth counter. Cascade entries (spawned by a
prior entry's Writes field) carry `[Depth: N/MAX]`. When depth would equal MAX+1, insert a
`[DEPTH EXCEEDED]` entry instead of a regular entry.

**Firing entry format** (root — no depth counter):

```
### Entry {#}: {Trigger Name}  [C-ID: C-{NN}]
- Type: {approved term}
- Execution tier: sync | async | scheduled
- Positioned because: EOR-{NN} — {rule text}
- Latency: {inline | post-commit (~N min) | N-hr deferral window}
- Fires because: {specific condition met by event tuple}
- Condition (EXECUTED): {filter condition — what matches}
- Condition (SKIPPED would be): {what must change for this NOT to fire}
- Registration witness: {artifact name from scenario or [UNWITNESSED]}
- Reads: {Entity}.{Field} = {value}
- Produces: {connector — action — target — resulting state}
- Writes: {Entity}.{Field} = {new value} [or "none"]
- Cascades to: Entry #{N} — {name} | [DEPTH EXCEEDED — {name} would be depth {N}/MAX] | None
- Counterfactual [Flip to NOT FIRE]: {minimal event tuple change preventing firing}
```

**Firing entry format** (cascade — carries depth counter):

```
### Entry {#}: {Trigger Name}  [C-ID: C-{NN}]  [Depth: {N}/MAX]
- Type: {approved term}
- Execution tier: sync | async | scheduled
- Positioned because: EOR-{NN} — {rule text} (cascade entry fires at spawning tier)
- Spawned by: Entry #{parent #} — {parent name}, via Writes: {Entity}.{Field}
- Latency: {inline | post-commit (~N min) | N-hr deferral window}
- Fires because: {condition met by spawning write}
- Condition (EXECUTED): {filter condition — what matches}
- Condition (SKIPPED would be): {what must change for this NOT to fire}
- Registration witness: {artifact name from scenario or [UNWITNESSED]}
- Reads: {Entity}.{Field} = {value}
- Produces: {connector — action — target — resulting state}
- Writes: {Entity}.{Field} = {new value} [or "none"]
- Cascades to: Entry #{N} — {name} | [DEPTH EXCEEDED — {name} would be depth {N}/MAX] | None
- Counterfactual [Flip to NOT FIRE]: {minimal change preventing firing}
```

**Gap entry format**:

```
### Entry {#}: [NOT FIRED — {Candidate Name}]  [C-ID: C-{NN}]
- Reason not fired: {condition not met}
- Condition (SKIPPED): {filter condition — what does not match}
- Registration witness: {artifact name or [UNWITNESSED]}
- Counterfactual [Flip to FIRE]: {minimal event tuple change causing firing}
```

**DEPTH EXCEEDED format**:

```
### [DEPTH EXCEEDED — {Candidate Name would be}]  [Depth: {MAX+1}/MAX]
- Spawned by: Entry #{parent #} — {parent name}, via Writes: {Entity}.{Field}
- Not added: cascade depth budget exhausted at MAX = {N}
- Storm flag: contributes to trigger storm detection in Role E
```

After all N entries:

```
Firing entries (root):     FR = {count}
Firing entries (cascade):  FC = {count}
Non-firing entries:        NF = {count}
DEPTH EXCEEDED entries:    DE = {count}
FR + FC + NF               = {sum}  [must equal N + cascade children added]
Max depth reached:         {deepest [Depth: N/MAX] observed}
EOR citations present:     {count of firing entries with Positioned because: populated}
EOR citations absent:      {count} [ordering gap count — should be 0]
```

`[GATE D: PASSED — all C-IDs accounted for; all firing entries carry EOR citation; all entries carry counterfactual]`
OR
`[GATE D: FAILED — missing C-IDs: {list}. Missing EOR citations: {list}. Missing counterfactuals: {list}]`

Role D complete. Proceed to Role E.

---

**ROLE E — VERDICT AUDITOR**

**Mandate**: Produce exactly three anomaly verdict blocks citing Role D entries. Close the
anomaly register. Nothing else.

**Prohibition**: Role E SHALL NOT add candidates, modify Role D entries, or re-open Role A's
event tuple. Role E SHALL NOT reference Role B's exclusion log except where an excluded
layer is directly relevant to a missing trigger finding. If any of these appear in Role E
beyond the permitted exclusion log reference, that content is a structural violation.

For each anomaly class, produce the verdict block. The `Rows inspected` field is mandatory
in every verdict block. A verdict without row citations is a structural violation.

**Verdict block format**:

```
### {Anomaly Class}: {DETECTED | NOT DETECTED}
- Rows inspected: Entry {#} through Entry {#}  [cite specific Role D entries]
- Exclusion log note: {if relevant: Role B layer whose absence contributes to verdict} | N/A
- Evidence: {specific entries, depth counters, EOR citations, Writes fields supporting verdict}
- Finding: {what was found or confirmed absent}
- Remediation: {if DETECTED: one named actionable fix. If NOT DETECTED: none required.}
```

**Trigger Storm**: Inspect all FR + FC firing entries and all DE DEPTH EXCEEDED entries.
Storm signal: DE > 0 (depth budget exhausted), OR five or more firing entries for the
single event, OR multiple entries writing the same field. Cite the deepest cascade chain
and the entry where budget was first exceeded if DE > 0.

**Missing Trigger**: Inspect FR + FC firing entries against expected automation coverage
for this entity + message. Reference Role B's exclusion log: if a layer was excluded for
a fixable reason (not yet registered, disabled, missing configuration), that is a missing
trigger finding. Cite Role D rows and Role B exclusion log row where applicable.

**Circular Dependency**: Build directed edge set from Role D Cascades-to fields (excluding
DEPTH EXCEEDED entries). Apply back-edge detection. Show full edge set. Name cycle path or
confirm no back-edges found. Cite all rows.

Close the anomaly register:

| Anomaly Class | Final Status |
|---|---|
| Trigger storm | CLOSED — {DETECTED / NOT DETECTED} |
| Missing trigger | CLOSED — {DETECTED / NOT DETECTED} |
| Circular dependency | CLOSED — {DETECTED / NOT DETECTED} |

`[GATE E: PASSED — all three verdicts with Role D row citations; anomaly register CLOSED]`
OR
`[GATE E: FAILED — missing verdict blocks: {list}. Missing row citations: {list}]`
