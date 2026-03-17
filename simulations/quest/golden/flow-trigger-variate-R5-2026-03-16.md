---
skill: flow-trigger
round: 5
rubric_version: 2
date: 2026-03-16
---

# flow-trigger — Round 5 (Rubric v2) Variations

**Skill**: flow-trigger — Simulate which automations fire when a record changes.
**Rubric**: v2 (C-01 through C-13)
**Date**: 2026-03-16

---

## Variation Design Notes

### R4 Scorecard Summary (Rubric v2, C-01–C-13)

| Variation | Score | All Essential | Axis | Key Gap |
|-----------|-------|---------------|------|---------|
| V-01 | 100 | YES | Role sequence — Authority Contracts (Scanner / Executor / Auditor) | None |
| V-02 | 100 | YES | Output format — Full Audit Ledger with gate-per-column | None |
| V-03 | 100 | YES | Phrasing register — FM catalog + gate tokens unified | None |
| V-04 | 100 | YES | Role sequence + Lifecycle emphasis — Four-role phase ownership | None |
| V-05 | 100 | YES | Inertia framing + Output format — Override model with format block | None |

**Root finding from R4**: All five structural strategies achieve 100 on rubric v2. Four independent
paths (role isolation, ledger, FM catalog, phase gates) and one motivational frame (inertia + format
block) all satisfy C-01 through C-13. The rubric is saturated by the R4 variation set.

### R4 Excellence Signals (Carry Forward — No Rediscovery)

| Signal | R4 Source | Mechanism |
|--------|-----------|-----------|
| Authority contract prohibitions | V-01 | Named prohibitions make scope creep detectable, not just discouraged |
| Gate-per-column ledger | V-02 | Empty required column = visible structural gap; no separate audit step needed |
| FM catalog + gate equivalence | V-03 | Each FM check IS a gate token; compliance is self-certifying |
| Artifact-gated phase progression | V-04 | Next phase cannot start until prior phase artifact exists |
| Inertia framing + format block | V-05 | Naming the default failure motivates; explicit format block enforces |
| `Reads:` / `Produces:` / `Writes:` slots | V-01–V-05 | Explicit named slots in firing entry; absent slot = structural gap |
| Pre-enumeration anomaly register | V-01–V-05 | Anomaly slots opened before Entry 1; C-04 structural precondition |
| Denominator declared before Entry 1 | V-01–V-05 | N declared in scan phase; completeness auditable without scorer's memory |
| Gap token `[NOT FIRED — reason]` | V-01–V-05 | Inline disposal of non-firing candidates; no silent omission |
| `Rows inspected: N–M` in verdict | V-01–V-05 | Mandatory row citation in every verdict block; C-13 structural |
| Cascade child row insertion | V-01–V-05 | Non-empty Writes field spawns a next-entry; C-10 structural |

### What R5 Must Achieve

R4 saturated rubric v2 with independent structural strategies. R5 explores three properties
not yet tested:

1. **Scenario decomposition gate** — forcing an explicit decomposition of the input scenario
   into trigger-registrable events (entity, message, changed field list) before the candidate
   scan begins. Tests whether scoping the scan reduces false-positive risk and improves
   denominator precision.

2. **Counterfactual pairing** — every candidate entry (firing or not) must include a
   counterfactual pair: the minimal input change that would flip the trigger's firing status.
   Tests whether counterfactuals make C-07 (conditional branch paths) and C-12 (gap tokens)
   structurally unavoidable rather than dependent on the author's thoroughness.

3. **Non-firer-first enumeration** — enumerate all non-firing candidates with gap tokens
   before the firing sequence. Tests whether reversing enumeration order makes C-12 a
   first-class obligation rather than a trailing cleanup step.

4. **Witness citation per entry** — every entry must cite the specific registered artifact
   (solution layer name, step name, flow solution name) that proves the trigger is registered
   for this entity/message. Tests whether grounding in named artifacts eliminates false
   positives and strengthens C-05.

| Variation | Axes | R5 Design Target |
|-----------|------|-----------------|
| V-01 | Scenario decomposition gate | Pre-scan gate decomposes scenario into registrable event tuple before any candidate is named. |
| V-02 | Counterfactual pairing | Every entry (firing or not) carries a `Would fire if / Would NOT fire if` pair. |
| V-03 | Non-firer-first enumeration | All non-firing candidates with gap tokens appear as Block 1; firing sequence is Block 2. |
| V-04 | Witness citation per entry | Every firing entry cites the specific registered artifact that proves it fires. |
| V-05 | Combined: scenario decomposition + counterfactual pairs + R4 V-01 authority contracts | Three new single-axis mechanisms added to R4's strongest structural foundation. |

**Foundation carried forward** (no rediscovery):
- Vocabulary contract + `[NC: term]` violation markers (C-05)
- Pre-opened anomaly investigation register before enumeration (C-04 structural precondition)
- Explicit gap token `[NOT FIRED — reason]` in sequence position (C-12)
- Directed edge set for circular detection (C-06)
- Cascade child row insertion for non-empty Writes field (C-10)
- Denominator declared before first entry (C-11)
- `Rows inspected: N–M` mandatory field in verdict blocks (C-13)
- Both EXECUTED and SKIPPED branches in firing entry (C-07)
- Latency + tier annotation per entry (C-09)
- `Reads:` / `Produces:` / `Writes:` explicit slots in firing entry (C-03)

---

## V-01 — Scenario Decomposition Gate

**Axis**: Scenario decomposition — pre-scan gate
**Hypothesis**: R1–R4 prompts begin candidate scanning immediately from the narrative
scenario. This produces denominator imprecision when the scenario describes a change
ambiguously (e.g., "the record is updated" without naming which fields changed, or
"the case is escalated" without naming the triggering entity + message). V-01 inserts
a mandatory DECOMPOSITION GATE before the candidate scan: the scenario is reduced to
a precise event tuple (entity, message, field deltas) that the scan uses as its sole
scope boundary. Any trigger outside the tuple's entity/message/field scope cannot enter
the candidate manifest. This eliminates false-positive candidates structurally — the
scope is closed by definition before the first candidate is named.

---

You are a Power Automate / Copilot Studio domain expert. Simulate which automations fire
when a record changes. Execute the three phases below in strict sequence. Each phase
must close before the next opens.

---

**VOCABULARY CONTRACT**

Use only these approved terms. Any unapproved term is a vocabulary violation: mark
`[NC: {term used}]` inline.

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

---

### PHASE 1 — DECOMPOSITION GATE

Before naming a single trigger candidate, decompose the scenario into a precise
event tuple. The tuple is the closed scope for all subsequent scanning. A candidate
that does not match the tuple is outside scope and cannot enter the manifest.

**Event Tuple** (fill every field from the scenario):

| Field | Value |
|---|---|
| Entity (logical name) | {entity logical name} |
| Trigger message | Create \| Update \| Delete \| Custom (name it) |
| Changed fields (for Update) | {field1}, {field2}, ... \| N/A for non-Update |
| Pre-image fields needed | {field1}: {before-value}, ... \| none |
| Post-image fields used | {field1}: {after-value}, ... \| none |
| Caller context | User \| System (async) \| Plugin chain (depth N) |
| Platform | {Dataverse / Power Automate / Copilot Studio — name it} |

**Scope Rule**: The candidate scan in Phase 2 is restricted to automations registered on
Entity = {entity} AND Message = {message}. Automations on other entities or messages are
out of scope even if they could theoretically observe this change via a downstream field write.
Out-of-scope candidates that appear in Phase 2 are a structural scope violation.

`[GATE 1: PASSED — event tuple complete, scope closed before candidate scan]`

Phase 1 complete. Proceed to Phase 2.

---

### PHASE 2 — CANDIDATE SCAN AND ENUMERATION

**Step 2a — Candidate Scan**

Using the Phase 1 event tuple as the only scope boundary, scan every automation layer
for candidates. Do not evaluate filter conditions. Assign each candidate a C-ID.

Layers to scan (in order):
1. Business rules on entity with field scope matching changed fields
2. Synchronous plugin steps registered on entity + message
3. Real-time workflows registered on entity + trigger event
4. Asynchronous plugin steps registered on entity + message
5. Background workflows registered on entity + trigger event
6. Automated flows with Dataverse connector trigger on entity + message
7. Other automation layers present in the scenario

**CANDIDATE MANIFEST**

| C-ID | Candidate Name | Layer | Registration Entity | Registration Message |
|------|----------------|-------|---------------------|----------------------|
| C-01 | {name} | {approved term} | {entity} | {message} |
| ... | | | | |

**DENOMINATOR: N = {count} candidates within scope of the Phase 1 event tuple.**

Open anomaly investigation register (do not close until Phase 3):

| Anomaly Class | Investigation Status |
|---|---|
| Trigger storm | OPEN — pending full enumeration |
| Missing trigger | OPEN — pending full enumeration |
| Circular dependency | OPEN — pending full enumeration |

**Step 2b — Enumeration**

Produce one entry for every C-ID in the manifest. Entries are ordered by execution tier
and sequence within tier. Every C-ID must appear exactly once — either as a firing entry
or a gap entry.

**Firing entry format**:

```
### Entry {#}: {Trigger Name}  [C-ID: C-{NN}]
- Type: {approved term}
- Execution tier: sync | async | scheduled
- Latency: Inline (same transaction) OR Post-commit (~{N} min) OR {N}-hr deferral window
- Fires because: {specific condition met by this event tuple}
- Condition (EXECUTED): {filter condition — what matches}
- Condition (SKIPPED would be): {what would need to be different for this NOT to fire}
- Reads: {Entity}.{Field} = {value} [all fields read]
- Produces: {connector — action — target — resulting state}
- Writes: {Entity}.{Field} = {new value} [all fields written; or "none"]
- Cascades to: Entry #{N} — {name} [if Writes triggers another C-ID] | None
```

**Gap entry format**:

```
### Entry {#}: [NOT FIRED — {Candidate Name}]  [C-ID: C-{NN}]
- Reason not fired: {specific condition in the event tuple that is not met}
- Condition (SKIPPED): {filter condition — what does not match}
- Condition (WOULD FIRE if): {minimal change to the event tuple that would flip this to firing}
```

After all N entries:

```
Firing entries:     F  = {count}
Non-firing entries: NF = {count}
F + NF              = {sum}  [must equal N]
```

`[GATE 2: PASSED — F + NF = N; all C-IDs from Phase 1 manifest accounted for]`
OR
`[GATE 2: FAILED — F + NF = {sum} ≠ N = {N}. Missing C-IDs: {list}]`

Phase 2 complete. Proceed to Phase 3.

---

### PHASE 3 — ANOMALY VERDICTS

Produce exactly three verdict blocks. Each verdict must cite Entry numbers from Phase 2.
A verdict block missing row citations is a structural gap.

**Verdict block format**:

```
### {Anomaly Class}: {DETECTED | NOT DETECTED}
- Rows inspected: Entry {#} through Entry {#}
- Evidence: {specific rows, fields, counts, or patterns that support the verdict}
- Finding: {description of what was found or confirmed absent}
- Remediation: {if DETECTED: one named, actionable fix. If NOT DETECTED: none required.}
```

**Trigger Storm**: Inspect all F firing entries. Five or more triggers per single event,
OR multiple entries writing the same field. Name the storm threshold used.

**Missing Trigger**: Inspect F firing entries against expected automation coverage for
this entity + message. Name any expected automation type that is absent.

**Circular Dependency**: Build the directed edge set: for each firing entry, create an
edge from the entry to each C-ID in its Cascades-to field. Detect back-edges. State
"no back-edges found" and show the edge list, or name the cycle path.

After all three verdict blocks:

`[GATE 3: PASSED — all three anomaly verdicts present with row citations]`
OR
`[GATE 3: FAILED — missing: {list}. Missing row citations: {list}]`

---

## V-02 — Counterfactual Pairing

**Axis**: Counterfactual pairing — every entry carries a flip condition
**Hypothesis**: R1–R4 required conditional branch paths (C-07) and gap tokens (C-12)
but treated them as separate obligations: C-07 for firing entries, C-12 for non-firing
entries. V-02 unifies them into a single COUNTERFACTUAL PAIR that every entry must carry,
regardless of firing status. A firing entry's counterfactual is the minimal input change
that would prevent it from firing. A non-firing entry's counterfactual is the minimal
input change that would make it fire. Both are structurally required. This makes C-07 and
C-12 inseparable obligations and ensures the model reasons about threshold conditions in
both directions for every candidate, not just the ones it remembered to flag as conditional.

---

You are a Power Automate / Copilot Studio domain expert. Simulate which automations fire
when a record changes. Use the counterfactual-pair protocol below.

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

### STEP 1 — CANDIDATE MANIFEST

Scan all automation layers for candidates registered on the triggering entity and message.
Do not evaluate conditions. Assign each a C-ID.

| C-ID | Candidate Name | Layer | Entity | Trigger Message |
|------|----------------|-------|--------|-----------------|
| C-01 | {name} | {approved term} | {entity} | {message} |
| ... | | | | |

**DENOMINATOR: N = {count} candidates.**

Open anomaly investigation register:

| Anomaly Class | Status |
|---|---|
| Trigger storm | OPEN |
| Missing trigger | OPEN |
| Circular dependency | OPEN |

Step 1 complete. Proceed to Step 2.

---

### STEP 2 — COUNTERFACTUAL ENUMERATION

Produce one entry for every C-ID. Entries are ordered by execution tier and sequence
within tier. Every entry — firing or not — must carry a COUNTERFACTUAL PAIR.

The counterfactual pair rule:
- If the entry FIRES: the `Flip to NOT FIRE` field states the minimal change to the input
  that would prevent this trigger from firing.
- If the entry does NOT FIRE: the `Flip to FIRE` field states the minimal change to the
  input that would cause this trigger to fire.

**Firing entry format**:

```
### Entry {#}: {Trigger Name}  [C-ID: C-{NN}]
- Type: {approved term}
- Execution tier: sync | async | scheduled
- Latency: {inline (blocks transaction) | post-commit (~N min) | N-hr deferral window}
- Fires because: {condition met by this input}
- Reads: {Entity}.{Field} = {value} [all fields read]
- Produces: {connector — action — target — resulting state}
- Writes: {Entity}.{Field} = {new value} [or "none"]
- Cascades to: Entry #{N} — {name} | None
- Counterfactual [Flip to NOT FIRE]: {minimal input change that would prevent firing}
```

**Gap entry format**:

```
### Entry {#}: [NOT FIRED — {Candidate Name}]  [C-ID: C-{NN}]
- Reason not fired: {condition NOT met by this input}
- Counterfactual [Flip to FIRE]: {minimal input change that would cause firing}
```

After all N entries:

```
Firing entries:     F  = {count}
Non-firing entries: NF = {count}
F + NF              = {sum}  [must equal N]
```

`[GATE 2: PASSED — all N C-IDs present; all entries carry counterfactual pair]`
OR
`[GATE 2: FAILED — missing C-IDs: {list}. Entries missing counterfactual: {list}]`

Step 2 complete. Proceed to Step 3.

---

### STEP 3 — ANOMALY VERDICTS

Produce exactly three verdict blocks. Cite Entry numbers from Step 2.

**Verdict block format**:

```
### {Anomaly Class}: {DETECTED | NOT DETECTED}
- Rows inspected: Entry {#} through Entry {#}
- Evidence: {specific row references, fields, counts that support verdict}
- Finding: {what was found or confirmed absent}
- Remediation: {if DETECTED: named actionable fix. If NOT DETECTED: none required.}
```

**Trigger Storm**: Five or more firing entries for a single change event, OR multiple
firing entries writing the same field. Inspect all F firing entries. Cite row range.

**Missing Trigger**: A trigger that business logic implies should exist does not appear
in the firing set. Inspect all F firing entries. Cite rows examined.

**Circular Dependency**: Construct the directed edge set from all Cascades-to fields.
Apply back-edge detection. Either name the cycle path and which rows form the loop,
or confirm no back-edges and show the full edge set. Cite all rows inspected.

After all three verdict blocks:

`[GATE 3: PASSED — all three anomaly verdicts present with row citations]`
OR
`[GATE 3: FAILED — missing verdicts: {list}. Missing citations: {list}]`

---

## V-03 — Non-Firer-First Enumeration

**Axis**: Non-firer-first enumeration — gap tokens appear as Block 1
**Hypothesis**: R1–R4 enumerate firing triggers first, then insert gap tokens for
non-firers after the firing sequence. This ordering makes C-12 a trailing cleanup
obligation — the author must remember to circle back and dispose of non-firing
candidates after the main enumeration. V-03 reverses the order: Block 1 is the
complete set of NON-FIRING candidates (all disposed of with gap tokens), and Block 2
is the firing sequence. This makes gap-token production a first-class obligation —
you cannot reach the firing sequence until all non-firers are disposed of. C-12
becomes structurally prior to C-01, C-02, and C-03 rather than trailing them.

---

You are a Power Automate / Copilot Studio domain expert. Simulate which automations fire
when a record changes. Use the non-firer-first protocol below.

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

### BLOCK 0 — CANDIDATE MANIFEST AND ANOMALY REGISTER

Scan all automation layers for candidates registered on the triggering entity and message.
Do not evaluate conditions. Assign each a C-ID.

| C-ID | Candidate Name | Layer | Entity | Trigger Message |
|------|----------------|-------|--------|-----------------|
| C-01 | {name} | {approved term} | {entity} | {message} |
| ... | | | | |

**DENOMINATOR: N = {count} candidates.**

Open anomaly slots (do not close until Block 2 is complete):

| Anomaly Class | Status |
|---|---|
| Trigger storm | OPEN — pending enumeration |
| Missing trigger | OPEN — pending enumeration |
| Circular dependency | OPEN — pending enumeration |

Block 0 complete.

---

### BLOCK 1 — NON-FIRING CANDIDATES (Gap Disposal)

Evaluate each C-ID against the triggering input. For every C-ID that does NOT fire,
produce a gap entry here. Block 1 must be complete before Block 2 begins.

**Rule**: If a C-ID fires, write `[DEFERRED TO BLOCK 2 — {candidate name}]` as its
placeholder here. All non-firing C-IDs must have a full gap entry. A C-ID absent from
both Block 1 and Block 2 is a structural omission.

**Gap entry format**:

```
### Gap {#}: [NOT FIRED — {Candidate Name}]  [C-ID: C-{NN}]
- Reason not fired: {specific condition not met}
- Condition (SKIPPED): {filter condition — what does not match}
- Condition (WOULD FIRE if): {what would need to be true for this to fire}
```

**Deferred entry format**:

```
### Gap {#}: [DEFERRED TO BLOCK 2 — {Candidate Name}]  [C-ID: C-{NN}]
```

After all N C-IDs disposed of or deferred:

```
Non-firing (gap entries):   NF = {count}
Deferred to Block 2:        D  = {count}
NF + D                       = {sum}  [must equal N]
```

`[GATE B1: PASSED — all N C-IDs disposed or deferred in Block 1]`
OR
`[GATE B1: FAILED — unaccounted C-IDs: {list}]`

Block 1 complete. Proceed to Block 2.

---

### BLOCK 2 — FIRING SEQUENCE

Produce one entry for each C-ID that was deferred in Block 1. Entries are ordered by
execution tier and sequence within tier. Number entries starting from 1.

**Firing entry format**:

```
### Entry {#}: {Trigger Name}  [C-ID: C-{NN}]
- Type: {approved term}
- Execution tier: sync | async | scheduled
- Latency: {inline (blocks transaction) | post-commit (~N min) | N-hr deferral window}
- Fires because: {specific condition met}
- Condition (EXECUTED): {filter condition — what matches}
- Condition (SKIPPED would be): {what must change for this NOT to fire}
- Reads: {Entity}.{Field} = {value} [all fields read]
- Produces: {connector — action — target — resulting state}
- Writes: {Entity}.{Field} = {new value} [or "none"]
- Cascades to: Entry #{N} — {name} | None
- Tier: sync | async | scheduled
- Latency note: {any throttle, deferral window, or concurrency constraint}
```

After all D entries:

```
Block 2 firing entries:     F  = {count}  [must equal D from Block 1]
Block 1 non-firing entries: NF = {count}  [from Block 1]
F + NF                       = {sum}  [must equal N]
```

`[GATE B2: PASSED — Block 1 + Block 2 accounts for all N C-IDs]`
OR
`[GATE B2: FAILED — discrepancy. Missing: {list}]`

Block 2 complete. Proceed to Block 3.

---

### BLOCK 3 — ANOMALY VERDICTS

Produce exactly three verdict blocks. Cite entry numbers from Blocks 1 and 2.
Block-prefixed references are required (e.g., "Block 2, Entry 3").

**Verdict block format**:

```
### {Anomaly Class}: {DETECTED | NOT DETECTED}
- Rows inspected: {Block N, Entry # through Entry #} [cite block + entry range]
- Evidence: {specific references that support the verdict}
- Finding: {what was found or confirmed absent}
- Remediation: {if DETECTED: named actionable fix. If NOT DETECTED: none required.}
```

**Trigger Storm**: Inspect all Block 2 firing entries. Five or more fires for one change,
OR multiple entries writing the same field. Cite Block 2 row range.

**Missing Trigger**: Inspect Block 2 firing entries against expected coverage. Cite rows.

**Circular Dependency**: Construct edge set from Block 2 Cascades-to fields. Apply back-edge
detection. Show edge list. Name cycle or confirm none. Cite all rows inspected.

`[GATE B3: PASSED — all three verdicts present with block-prefixed row citations]`
OR
`[GATE B3: FAILED — missing: {list}. Missing citations: {list}]`

---

## V-04 — Witness Citation Per Entry

**Axis**: Witness citation — every entry cites its registration artifact
**Hypothesis**: R1–R4 ask the model to determine which triggers fire based on
scenario description alone. This introduces a latent false-positive risk: the model
may infer that a trigger "should" exist given the scenario's domain rather than
because the scenario explicitly registers it. V-04 requires every firing entry to
cite the specific registered artifact — the solution name, plugin step name, flow
name, or workflow name — that proves the trigger is registered for this entity and
message. Non-firing entries must cite either the missing registration artifact or
the evaluated condition that blocks firing. This makes C-05 (platform grounding) a
per-entry obligation rather than a global declaration, and makes false positives
structurally detectable: an entry with no named registration artifact is ungrounded.

---

You are a Power Automate / Copilot Studio domain expert. Simulate which automations fire
when a record changes. Use the witness-citation protocol below. Every entry must be
grounded in a named registration artifact from the scenario.

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

### PASS 1 — CANDIDATE MANIFEST

Scan all automation layers for candidates registered on the triggering entity and message.
For each candidate, record the registration artifact that proves it is scoped to this
entity/message. If no artifact is named in the scenario, mark `[UNWITNESSED]`.

| C-ID | Candidate Name | Layer | Registration Artifact | Entity | Message |
|------|----------------|-------|-----------------------|--------|---------|
| C-01 | {name} | {approved term} | {artifact name or [UNWITNESSED]} | {entity} | {message} |
| ... | | | | | |

**DENOMINATOR: N = {count} candidates.**

**UNWITNESSED count: U = {count}** (triggers inferred from domain, not from scenario text).
An unwitnessed candidate may still appear in the firing sequence if the scenario's
narrative implies it, but its unwitnessed status is a grounding flag.

Open anomaly register:

| Anomaly Class | Status |
|---|---|
| Trigger storm | OPEN |
| Missing trigger | OPEN |
| Circular dependency | OPEN |

Pass 1 complete.

---

### PASS 2 — WITNESSED ENUMERATION

Produce one entry for every C-ID. Entries are ordered by execution tier and sequence.
The `Registration Witness` field is mandatory in every entry. An entry without a named
registration artifact is an ungrounded entry.

**Firing entry format**:

```
### Entry {#}: {Trigger Name}  [C-ID: C-{NN}]
- Type: {approved term}
- Execution tier: sync | async | scheduled
- Registration witness: {solution / step name / flow name / workflow name from scenario}
  [or: [UNWITNESSED — inferred from domain] if no artifact named]
- Fires because: {specific condition met}
- Condition (EXECUTED): {filter condition — what matches}
- Condition (SKIPPED would be): {what must change for this NOT to fire}
- Reads: {Entity}.{Field} = {value} [all fields read]
- Produces: {connector — action — target — resulting state}
- Writes: {Entity}.{Field} = {new value} [or "none"]
- Cascades to: Entry #{N} — {name} | None
- Latency: {inline (blocks transaction) | post-commit (~N min) | N-hr deferral window}
```

**Gap entry format**:

```
### Entry {#}: [NOT FIRED — {Candidate Name}]  [C-ID: C-{NN}]
- Registration witness: {artifact name [to confirm it IS registered, just not firing] or [UNWITNESSED]}
- Reason not fired: {condition not met OR registration artifact absent from scenario}
- Condition (SKIPPED): {filter condition — what does not match}
- Condition (WOULD FIRE if): {what would need to be true}
```

After all N entries:

```
Firing entries:       F  = {count}
Non-firing entries:   NF = {count}
F + NF                = {sum}  [must equal N]
Unwitnessed entries:  U  = {count}  [grounding health metric]
```

`[GATE 2: PASSED — all N C-IDs present; registration witness field populated in every entry]`
OR
`[GATE 2: FAILED — missing C-IDs: {list}. Entries without registration witness: {list}]`

Pass 2 complete.

---

### PASS 3 — ANOMALY VERDICTS

Produce exactly three verdict blocks. Cite Entry numbers and, where relevant,
the registration witness field that grounds the verdict.

**Verdict block format**:

```
### {Anomaly Class}: {DETECTED | NOT DETECTED}
- Rows inspected: Entry {#} through Entry {#}
- Evidence: {specific entries, fields, registration witnesses, counts supporting verdict}
- Finding: {what was found or confirmed absent}
- Remediation: {if DETECTED: named actionable fix. If NOT DETECTED: none required.}
```

**Trigger Storm**: Inspect all F firing entries. Five or more fires, or shared Writes
fields. Cite row range. Note whether any unwitnessed entries inflate the count.

**Missing Trigger**: Inspect F firing entries. Consider whether any expected automation
type for this entity/message is absent from the manifest. Unwitnessed candidates that did
not fire may represent implicit missing triggers — cite them if relevant.

**Circular Dependency**: Construct edge set from all Cascades-to fields. Apply back-edge
detection. Show edge list. Name cycle or confirm none. Cite rows.

`[GATE 3: PASSED — all three verdicts with row citations and witness grounding]`
OR
`[GATE 3: FAILED — missing: {list}. Missing citations: {list}]`

---

## V-05 — Combined: Scenario Decomposition + Counterfactual Pairs + Authority Contracts

**Axes**: Scenario decomposition (V-01) + Counterfactual pairing (V-02) + R4 V-01 authority
contracts
**Hypothesis**: The three single-axis mechanisms from R5 V-01 and V-02, combined with R4's
strongest structural mechanism (authority contracts with prohibitions), create a fully
self-enforcing protocol with distinct structural barriers at three points:
(1) the scenario decomposition gate closes scope before candidates are named,
(2) authority contracts prevent scope creep between roles,
(3) mandatory counterfactual pairs force bilateral condition reasoning for every candidate
(making C-07 and C-12 unavoidable rather than author-dependent).
The combination is predicted to be the most reliable R5 variation because each mechanism
addresses a different failure mode: imprecise scope (remedied by decomposition), role
drift (remedied by authority contracts), and selective condition coverage (remedied by
counterfactual pairs).

---

You are a Power Automate / Copilot Studio domain expert operating in three sequential roles.
Complete each role in full before beginning the next. Role boundaries are authority contracts.
Each role has a mandate (what it SHALL do) and a prohibition (what it SHALL NOT do under
any circumstances). A prohibited action appearing in a role's output is a structural violation.

---

**VOCABULARY CONTRACT**

Use only these approved terms. Any unapproved term: mark `[NC: {term used}]` inline.

| Approved Term | Tier | Definition |
|---|---|---|
| synchronous plugin step | sync | Executes in the transaction, blocking commit |
| asynchronous plugin step | async | Executes post-commit in the background |
| real-time workflow | sync | Synchronous workflow in the same transaction |
| background workflow | async | Asynchronous workflow post-commit |
| instant flow | async (on-demand) | Power Automate: manually triggered or via API |
| automated flow | async (event-driven) | Power Automate: triggered by a platform event |
| scheduled flow | async (time-driven) | Power Automate: triggered by time schedule |
| business rule | sync | Dataverse: field logic, always synchronous |

---

**ROLE A — SCENARIO DECOMPOSER AND CANDIDATE SCANNER**

**Mandate**: Produce the event tuple (scope definition) and the candidate manifest with
denominator count. Nothing else.

**Prohibition**: Role A SHALL NOT evaluate conditions. Role A SHALL NOT determine which
candidates fire. Role A SHALL NOT describe inputs, outputs, side effects, timing, or
counterfactuals. Role A SHALL NOT open anomaly investigations. Any of these appearing
in Role A's output is a structural violation of the authority contract.

**Step A1 — Event Tuple**

Decompose the scenario into a precise event tuple. This tuple is the closed scope for
the candidate scan. No candidate outside entity + message scope may enter the manifest.

| Field | Value |
|---|---|
| Entity (logical name) | {entity} |
| Trigger message | Create \| Update \| Delete \| Custom |
| Changed fields (Update only) | {field1}, {field2}, ... \| N/A |
| Pre-image fields present | {field}: {value}, ... \| none |
| Post-image fields present | {field}: {value}, ... \| none |
| Caller context | User \| System \| Plugin chain (depth N) |
| Platform | {Dataverse / Power Automate / Copilot Studio} |

`[GATE A1: PASSED — scope closed; entity = {entity}, message = {message}]`

**Step A2 — Candidate Manifest**

Scan every automation layer for candidates registered on the tuple's entity + message.
Do not evaluate filter conditions. Assign each a C-ID.

Layers to scan (in order):
1. Business rules on entity with field scope matching changed fields
2. Synchronous plugin steps registered on entity + message
3. Real-time workflows registered on entity + trigger event
4. Asynchronous plugin steps registered on entity + message
5. Background workflows registered on entity + trigger event
6. Automated flows with Dataverse connector trigger on entity + message
7. Other automation layers present in the scenario

**CANDIDATE MANIFEST**

| C-ID | Candidate Name | Layer | Entity | Registration Message |
|------|----------------|-------|--------|----------------------|
| C-01 | {name} | {approved term} | {entity} | {message} |
| ... | | | | |

**DENOMINATOR: N = {count} candidates within tuple scope.**

`[GATE A2: PASSED — N candidates declared; denominator set before enumeration]`

Role A complete. Proceed to Role B.

---

**ROLE B — TRIGGER EXECUTOR WITH COUNTERFACTUAL PAIRS**

**Mandate**: Produce one numbered entry for every C-ID in Role A's manifest — whether
it fires or not. Entries are ordered by execution tier and sequence. Every entry carries
a COUNTERFACTUAL PAIR. Entries use the required format.

**Prohibition**: Role B SHALL NOT produce anomaly verdicts or remediation proposals.
Role B SHALL NOT add candidates not in Role A's manifest. Role B SHALL NOT produce
a reconciliation summary or denominator check until the end of Role B's output. If any
of these appear in Role B, that content is a structural violation.

**Counterfactual pair rule**:
- Firing entry: the `Flip to NOT FIRE` field states the minimal input change that would
  prevent this trigger from firing. "Remove the automation registration" is not a valid
  counterfactual — it must be a change to the triggering event, field value, or condition.
- Non-firing entry: the `Flip to FIRE` field states the minimal input change that would
  cause this trigger to fire.

**Pre-enumeration anomaly register** (open before Entry 1 — not counted in firing sequence):

| Anomaly Class | Status | Open Note |
|---|---|---|
| Trigger storm | OPEN | Evaluate after all entries |
| Missing trigger | OPEN | Evaluate after all entries |
| Circular dependency | OPEN | Evaluate after all entries |

**Execution order rules**:
- Business rules: pre-validation (first in sequence)
- Synchronous plugin steps: ordered by pipeline stage (pre-operation before
  post-operation), then by rank within stage (lowest rank first)
- Real-time workflows: after sync plugin steps at the same pipeline stage
- Asynchronous plugin steps: after all synchronous entries
- Background workflows and automated flows: after async plugin steps
- State the ordering rationale explicitly within each tier

**Firing entry format**:

```
### Entry {#}: {Trigger Name}  [C-ID: C-{NN}]
- Type: {approved term}
- Execution tier: sync | async | scheduled
- Latency: {inline (blocks transaction) | post-commit (~N min) | N-hr deferral window}
- Fires because: {specific condition met by the event tuple}
- Condition (EXECUTED): {filter condition — value that matches}
- Condition (SKIPPED would be): {what must change for this NOT to fire}
- Reads: {Entity}.{Field} = {value} [all fields read]
- Produces: {connector — action — target — resulting state}
- Writes: {Entity}.{Field} = {new value} [or "none"]
- Cascades to: Entry #{N} — {name} [if Writes triggers another C-ID] | None
- Counterfactual [Flip to NOT FIRE]: {minimal event tuple change that prevents firing}
```

**Gap entry format**:

```
### Entry {#}: [NOT FIRED — {Candidate Name}]  [C-ID: C-{NN}]
- Reason not fired: {specific condition not met}
- Condition (SKIPPED): {filter condition — value that does not match}
- Counterfactual [Flip to FIRE]: {minimal event tuple change that causes firing}
```

After all N entries:

```
Firing entries:     F  = {count}
Non-firing entries: NF = {count}
F + NF              = {sum}  [must equal N]
```

`[GATE B: PASSED — F + NF = N; all C-IDs from Role A accounted for; all entries carry counterfactual pair]`
OR
`[GATE B: FAILED — F + NF = {sum} ≠ N = {N}. Missing C-IDs: {list}. Missing counterfactuals: {list}]`

Role B complete. Proceed to Role C.

---

**ROLE C — VERDICT AUDITOR**

**Mandate**: Produce exactly three anomaly verdict blocks. Each verdict block must cite
specific Entry numbers from Role B. Nothing else.

**Prohibition**: Role C SHALL NOT enumerate new triggers. Role C SHALL NOT add or modify
entries in Role B's firing sequence. Role C SHALL NOT re-open or change Role A's manifest
or event tuple. If any of these appear in Role C, that content is a structural violation.

For each anomaly class, produce the verdict block in the format below. The `Rows inspected`
field is mandatory — a verdict block without row citations is a structural violation.

**Verdict block format**:

```
### {Anomaly Class}: {DETECTED | NOT DETECTED}
- Rows inspected: Entry {#} through Entry {#}  [cite specific Role B entries reviewed]
- Evidence: {specific fields, values, counts, patterns from cited rows}
- Finding: {what was found or confirmed absent}
- Remediation: {if DETECTED: one named, actionable fix — debounce, registration,
  cycle-break, re-sequencing, or concurrency control. If NOT DETECTED: none required.}
```

**Trigger Storm**: Five or more triggers fire for a single field change, OR multiple
firing entries write the same output field, creating signal amplification. Inspect all
F firing entries from Role B. Cite the row range. Name the storm threshold used.

**Missing Trigger**: A trigger that business logic implies should exist does not appear
in Role B's firing set. Inspect Role B's firing entries against expected automation
coverage for this entity + message. Compare to the Phase 1 event tuple scope. Cite rows.

**Circular Dependency**: Any trigger's Writes field could re-fire a trigger already in
the cascade chain — creating a loop. Build the directed edge set: for each firing entry,
create an edge from that entry to each entry listed in its Cascades-to field. Apply
back-edge detection. Show the full edge set. Either name the cycle path and the entries
forming the loop, or confirm "no back-edges found" with the edge list. Cite all rows.

After all three verdict blocks:

`[GATE C: PASSED — all three anomaly verdict blocks present with Entry citations from Role B]`
OR
`[GATE C: FAILED — missing verdict block(s): {list}. Missing row citations: {list}]`
