# Flow-Trigger Skill — Round 1 Variations (Rubric v1, C-01..C-10)

**Skill**: flow-trigger — Simulate which automations fire when a record changes.
**Rubric**: v1 (C-01 through C-10, canonical)
**Date**: 2026-03-15

---

## Variation Design Notes

Round 1 targets the v1 canonical rubric. Ten criteria are in play.

Key tensions in the rubric:
- C-01 (trigger enumeration) and C-04 (all three anomaly class verdicts) pull against each other — a
  prompt that opens with pathology questions tends to rush enumeration; one that drives completeness
  tends to retrofit anomaly verdicts against a closed list.
- C-03 (inputs/outputs per trigger) is where generic descriptions most often leak through: "sends a
  notification" instead of "Sends email via Office 365 Outlook to Request.AssignedTo".
- C-04 is structurally the most brittle: all three verdicts must appear even when the scenario is
  clean. A prompt that drives completeness via list-making tends to drop the empty-set case.
- C-07 (conditional branch paths) requires stating both the firing branch AND at least one skipped
  branch — naturally satisfied when the prompt mandates a "Fires When / Not When" column.
- C-10 (cascade completeness) formalizes what many prompts already state as a rule ("add downstream
  trigger as next row") — but without explicit C-10 targeting, cascade rows frequently become
  annotations rather than numbered entries in the sequence.

**Single-axis variations**: V-01 (role sequence), V-02 (output format), V-03 (phrasing register).
**Combined variations**: V-04 (lifecycle emphasis + role sequence), V-05 (inertia framing + output format).

**Variation map**:

| Variation | Axis | Primary Criteria Targeted | Hypothesis |
|-----------|------|--------------------------|------------|
| V-01 | Role sequence | C-04, C-01, C-10, C-08 | A dedicated Cascade Mapper role that traces write-to-fire pathways before the Trigger Enumerator begins means C-10 cascade rows are pre-committed as named entries, not added as afterthoughts. The Auditor role then closes all three anomaly questions against a complete chain. |
| V-02 | Output format | C-01, C-02, C-03, C-07, C-10 | A two-tier firing table (sync / async) with a required Cascade Depth column forces cascade chains to be explicit entries. PA vocabulary column headers make C-03 and C-07 violations structurally visible as empty or non-conforming cells rather than hidden omissions. |
| V-03 | Phrasing register | C-03, C-05, C-06, C-07, C-09 | A conversational register with compact named-slot blocks per trigger and one-line constraint slots removes scaffolding noise. Named fields (Reads, Produces, Side effects, Fires when, Tier) make absent values visible as blank lines rather than hidden omissions. |
| V-04 | Lifecycle emphasis + role sequence | C-01, C-04, C-10, C-02 | A four-pass protocol where Pass 1 = candidate scan, Pass 2 = cascade map (dedicated), Pass 3 = fire evaluation, Pass 4 = pathology scan treats cascade tracing as its own structural pass. Passing cascade row outputs forward as required inputs to Pass 3 ensures C-10 is load-bearing. |
| V-05 | Inertia framing + output format | C-01, C-04, C-07, C-08, C-10 | Naming the four failure modes of informal trigger analysis before the protocol motivates each structural requirement. A table format that marks vocabulary violations inline (VOCAB FAIL cells) and mandates a Cascade Chain column creates two enforcement layers: motivational (why) and structural (visible failure). |

---

## V-01 — Role Sequence: Cascade Mapper Before Enumerator

**Variation axis**: Role sequence
**Hypothesis**: Running a Cascade Mapper role first — which traces all write-to-fire pathways
before any trigger is numbered — precommits cascade rows as named entries in the sequence
rather than dangling annotations. The Enumerator then builds the firing sequence with the cascade
chain already mapped. The Auditor closes all three anomaly questions against the complete chain,
preventing C-04 from being retrofitted against a shorter list.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert operating in three sequential roles. Complete each role fully before beginning the next. Do not merge roles.

---

#### ROLE A — CASCADE MAPPER

Your task: before any trigger fires, map every write-to-fire pathway from the change event outward.

**A-1 — Pin the Change**

Restate the change event in one line: entity, field changed, old value → new value. This anchors scope.

**A-2 — Write-to-Fire Graph**

Starting from the initiating change, trace every field write that could fire downstream automation. Build a directed graph where each node is a field state and each edge is a trigger execution.

```
Layer 0 (initiating change):
  {Entity}.{Field}: {old value} → {new value}

Layer 1 (triggers that fire directly on this change):
  - {Trigger Name}: fires because {entity + field + trigger type match}
    → Side effect writes: {Entity}.{Field} = {value} (or NONE)

Layer 2 (triggers fired by Layer 1 side effects):
  - {Trigger Name}: fires because Layer 1 trigger writes {Entity.Field} = {value}
    → Side effect writes: {Entity}.{Field} = {value} (or NONE)

Layer N:
  (continue until no new side-effect writes remain that could fire additional triggers)
```

**A-3 — Cascade Chain Summary**

List the complete ordered firing chain from the graph:

```
Chain: [{Trigger-1}] → [{Trigger-2}] → [{Trigger-3}] → ... → END
Side-effect field writes: [{Trigger} writes {Entity.Field} = {value}; ...]
Total execution count: N
```

If no cascades exist: `Chain: [{Trigger-1}, {Trigger-2}, ...] (no cascade — all triggers fire independently on the initiating change, no side-effect field writes fire additional triggers)`

**Role A output to Role B**: Complete cascade chain, layer count N, side-effect field writes.

---

#### ROLE B — TRIGGER ENUMERATOR

You have the cascade chain from Role A. Enumerate every trigger in the chain with full detail.
Number them in the order established in Role A. Cascaded triggers must appear as consecutive numbered entries — a trigger spawned by a side-effect write in row N must appear at row N+1. Do not annotate cascades separately.

For each trigger in the chain, in execution order (sync before async within each layer):

**[#] [Trigger Name]** *(Layer [N] — cascade from: [parent trigger or "initiating change"])*

- **PA Flow Type**: `Automated – Dataverse` / `Automated – SharePoint` / `Instant` / `Scheduled` — exact terms only
- **Execution Tier**: `Sync` (blocks transaction commit) or `Async` (~[latency] on [standard|premium] tier)
- **Fires When**: The condition(s) that evaluated true for this change. State at least one condition that would cause this trigger NOT to fire.
- **Reads**: All input fields as `{Entity}.{Field}`. No generic descriptions. No "the record" or "relevant fields".
- **Produces**: Specific verb + connector + target:
  - `Sets {Entity}.{Field} to {value} via Dataverse connector`
  - `Sends email via Office 365 Outlook to {Entity}.{Field}` with subject `"{text}"`
  - `Posts adaptive card to Microsoft Teams {channel} with {payload fields}`
  - `Creates {Entity} record via Dataverse with fields: [{field list}]`
  - `Calls HTTP POST to {endpoint} with payload: [{field list}]`
- **Side Effect Writes**: From Role A Layer [N+1] for this trigger: `writes {Entity}.{Field} = {value}`. `None` if none.
- **Cascade Spawns**: Trigger(s) at row N+1 that fire because of this trigger's side-effect writes. `None` if no downstream triggers.

**Role B output to Role C**: Complete numbered firing sequence, all side-effect writes enumerated.

---

#### ROLE C — PATHOLOGY AUDITOR

You have the complete firing sequence from Role B and the cascade chain from Role A. Evaluate all three anomaly classes. Every class requires a named verdict — even when clean.

**C-1 — Candidate Pre-Scan**

List every trigger that *could* fire for the change event based on entity, field, and trigger type alone. This is the denominator for missing-trigger detection.

```
Candidates:
- [Trigger Name]: could match because [entity + field + trigger type match reason]
```

Candidate count: N.

**C-2 — Candidate Reconciliation**

Resolve every candidate against the Role B firing sequence:

```
[Trigger Name] → FIRED / CONFIRMED ABSENT ([specific reason]) / FLAGGED GAP ([why expected])
```

Totals: N FIRED, N CONFIRMED ABSENT, N FLAGGED GAP.

**C-3 — Trigger Storm Verdict**

- Role B total distinct executions: N (list by trigger name)
- Storm threshold: > 3 distinct executions, or any single trigger executes more than once
- Re-entry check: for each side-effect field write in Role B, identify any candidate in C-1 whose input condition fires on the written field. List any re-entry paths.
- **Verdict**: `STORM: CLEARED (count = N, no re-entry)` or `STORM DETECTED (group: [trigger names]; re-entry path: [details])`
  A verdict without a named count is insufficient.

**C-4 — Missing Trigger Verdict**

- FLAGGED GAP entries from C-2: [list, or "none"]
- For each gap: expected trigger name, specific gap cause, risk level
- **Verdict**: `MISSING: CLEARED (N candidates — N fired, N confirmed absent, 0 flagged gaps)` or `MISSING TRIGGER: [name — cause — risk]`

**C-5 — Circular Trigger Verdict**

- Side-effect field writes from Role B: [list as `{Trigger} writes {Entity}.{Field} = {value}`]
- Directed edge set: `{Trigger A} → writes {Entity.Field} → fires {Trigger B}`
- Back-edge check: does any path return to a node already in the chain?
- Graph property: DAG (no back-edges) / CYCLIC (back-edge at [path])
- **Verdict**: `CIRCULAR: CLEARED (DAG confirmed; edge set: {listed})` or `CIRCULAR TRIGGER: [full cycle path]`
  "No circular triggers" without an edge-set enumeration is insufficient.

**C-6 — Pathology Summary**

| Rank | Pathology | Status | Risk Level | Operational Impact | Mitigation |
|------|-----------|--------|------------|--------------------|------------|

Rank: Critical > High > Medium > Low. If all cleared: `All three anomaly classes cleared.`

---

Now receive the scenario and trigger registry. Execute Role A completely, then Role B, then Role C.

---

## V-02 — Output Format: Two-Tier Firing Table with Cascade Depth Column

**Variation axis**: Output format
**Hypothesis**: A two-tier firing table (sync / async) with a required Cascade Depth column
forces cascade chains to be explicit numbered entries rather than prose annotations, directly
targeting C-10. Required PA vocabulary in column headers makes C-03 and C-07 violations
structurally visible as empty or non-conforming cells. Pathology analysis reads off the table
rather than being reconstructed from prose, making C-04 anomaly verdicts dependent on table
evidence and therefore harder to omit.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. Produce a trigger fire report for the stated change event. Execute all five sections in order. Do not skip sections.

---

#### SECTION 1 — CHANGE EVENT PIN

| Parameter | Value |
|-----------|-------|
| Entity | |
| Changed Field | |
| Old Value | |
| New Value | |
| Initiating Context | |
| Trigger registry source | |

Triggers that do NOT fire for this exact field change are out of scope. Do not include them in Section 2.

---

#### SECTION 2 — FIRING SEQUENCE TABLES

List every trigger that actually fires. All columns required. Generic descriptions are a failure.

Cascade rule: if a trigger's Side Effect Write causes another trigger to fire, that triggered
trigger must appear as the **immediately next numbered row** in its tier, with Cascade Depth
incremented. It is never acceptable to annotate a cascade trigger in a note or footnote — it
must be a numbered row.

**Sync tier** — executes inline, blocks transaction commit:

| # | Cascade Depth | Trigger Name | PA Flow Type | Fires When | Not When | Input Fields | Output Action | Side Effect Writes |
|---|--------------|-------------|--------------|-----------|---------|--------------|---------------|--------------------|

Sync row count: N

**Async tier** — fire-and-forget, does not block transaction:

| # | Cascade Depth | Trigger Name | PA Flow Type | Fires When | Not When | Input Fields | Output Action | Side Effect Writes | Latency |
|---|--------------|-------------|--------------|-----------|---------|--------------|---------------|--------------------|---------|

Async row count: N

**Column requirements**:

- **Cascade Depth**: `0` for triggers that fire directly on the initiating change. `1` for triggers
  fired by a Depth-0 side effect. `2` for triggers fired by a Depth-1 side effect. Etc. A trigger
  spawned by a side-effect write must appear at depth N+1 immediately after the parent row.
- **PA Flow Type**: Exactly one of: `Automated – Dataverse`, `Automated – SharePoint`, `Instant`,
  `Scheduled`. No other forms accepted.
- **Fires When**: The condition(s) that evaluated true. Must be stated as a testable condition
  (`Request.Status = "Submitted"`, `Record created`, `Approval.Decision = "Reject"`). No prose.
- **Not When**: At least one condition that would cause this trigger NOT to fire. `Unconditional`
  only if the trigger truly has no conditions.
- **Input Fields**: All fields read as `{Entity}.{Field}`. Multiple fields: comma-separated. Never
  write "the record", "relevant fields", "current data".
- **Output Action**: Must open with one of these required verbs:
  `Sets`, `Creates`, `Deletes`, `Updates`, `Sends email via`, `Calls HTTP`, `Starts child flow:`,
  `Posts adaptive card to`, `Sends push notification via`.
  Disallowed: "processes", "notifies", "handles", "manages", "updates the record", "sends a notification".
- **Side Effect Writes**: Every field write with downstream trigger potential, as
  `{Entity}.{Field} = {value}`. `None` if none. If multiple: semicolon-separated.
- **Latency** (async only): `~N min standard tier` or `~N min premium tier`. `N/A` for sync rows.

---

#### SECTION 3 — TRIGGER REGISTRY RECONCILIATION

Every trigger in the registry must appear in this table. An unresolved entry is a structural gap.

| Trigger Name | Resolution | Specific Reason |
|-------------|------------|-----------------|

Resolution codes:
- `FIRED (Sync, row #N)` — appears in Section 2 sync tier at row N
- `FIRED (Async, row #N)` — appears in Section 2 async tier at row N
- `CONFIRMED ABSENT` — did not fire; specific reason required (condition false, field not in change
  scope, entity mismatch, disabled, etc.)
- `FLAGGED GAP` — expected to fire for this scenario but absent; investigation required

Totals: FIRED: N (Sync: N, Async: N), CONFIRMED ABSENT: N, FLAGGED GAP: N

---

#### SECTION 4 — PATHOLOGY ANALYSIS

All three anomaly class verdicts required. Each verdict must cite specific rows from Sections 2–3.
A verdict without row-level evidence is a partial fail.

**Trigger Storm**
- Section 2 total distinct trigger executions: N (list by trigger name + row number)
- Storm threshold: > 3 total executions, or any single trigger fires more than once
- Re-entry check: for each Side Effect Write in Section 2, identify registry triggers whose input
  condition fires on the written field. List all re-entry paths found, or "none found".
- **Verdict**: `STORM: CLEARED (count = N, no re-entry detected)` or `STORM DETECTED (count = N; group: [trigger names + rows]; re-entry path: [field → trigger → field chain])`

**Missing Triggers**
- FLAGGED GAP entries from Section 3: [list, or "none"]
- For each gap: expected trigger name, gap cause, risk level (Critical / High / Medium / Low)
- **Verdict**: `MISSING: CLEARED (N registry entries — N fired, N absent, 0 gaps)` or `MISSING TRIGGER: [name — cause — risk]`

**Circular Triggers**
- Side-effect field writes from Section 2 Side Effect Writes column: [enumerate all non-None entries as `row#N: {Trigger} writes {Entity.Field} = {value}`]
- Directed edge set: for each write, find registry triggers that fire on that field — add edge `{Writing Trigger (row N)} → {Entity.Field} → {Triggered Trigger}`
- Full edge set: [list all edges, or "empty — no side-effect writes trigger additional flows"]
- Back-edge check: does any edge create a path back to a trigger already earlier in the firing sequence?
- Graph property: DAG / CYCLIC
- **Verdict**: `CIRCULAR: CLEARED (DAG confirmed; edge set: {listed})` or `CIRCULAR TRIGGER: [full cycle path with row numbers]`

---

#### SECTION 5 — PATHOLOGY SUMMARY

| Rank | Pathology | Risk Level | Operational Impact | Recommended Mitigation |
|------|-----------|------------|--------------------|------------------------|

Risk: Critical (system correctness / data corruption), High (data integrity / process failure), Medium (performance / latency), Low (noise / UX).

If no pathologies confirmed: `No pathologies confirmed — all three anomaly classes cleared.`

---

**Anti-examples — these fail column requirements**:

| Wrong | Correct |
|-------|---------|
| `"Automated flow"` | `Automated – Dataverse` |
| `"Updates the record status"` | `Sets Request.Status to Under Review via Dataverse connector` |
| `"Sends a notification"` | `Sends email via Office 365 Outlook to Request.AssignedTo` |
| `"Relevant fields"` | `Request.Status, Request.AssignedTo` |
| `"No circular triggers"` | `CIRCULAR: CLEARED (DAG confirmed; edge set: {OnSubmit → writes Request.Status → no trigger in registry fires on Request.Status})` |
| *(cascade trigger as footnote)* | *(cascade trigger as numbered row at Depth 1)* |

---

Now receive the scenario and trigger registry. Produce the full output following this protocol.

---

## V-03 — Phrasing Register: Conversational Named-Slot Blocks

**Variation axis**: Phrasing register (formal/technical → direct conversational)
**Hypothesis**: Stripping structural scaffolding and adopting compact, question-driven named-slot
blocks per trigger reduces cognitive overhead and makes absent values visible as blank lines
rather than hidden omissions. Each slot maps directly to a rubric criterion. The conversational
register targets C-03 (per-trigger inputs/outputs), C-07 (conditional branches), C-09 (execution
tier), and C-10 (cascade completeness) by naming exactly what must appear in each slot.

---

### Prompt Body

You are a Power Automate expert. A record just changed. Walk through every automation that fires.

Do the five steps below in order. Do not skip any step.

---

**STEP 1 — Pin it**

One line: entity, field, old value → new value. Everything you list in Step 2 must fire for this exact change.

---

**STEP 2 — Candidates first**

Before deciding what fires, list every trigger that *could* fire based on entity, field, and trigger type. No condition evaluation yet.

```
- [Trigger Name]: could match because [one-line reason — entity + field + trigger type]
```

Total: N candidates. This is your denominator for Step 4-Q2.

---

**STEP 3 — Every firing trigger, in order**

Number them in execution order — sync first, then async. For each one, fill every named slot. Empty slots are failures.

**[#] [Trigger Name]**
*(Depth: [0 if fires directly on initiating change | N+1 if fires from a prior trigger's side-effect write on: {Entity.Field}])*

- **Type**: `Automated – Dataverse` / `Automated – SharePoint` / `Instant` / `Scheduled`
- **Tier**: `Sync` or `Async (~[N] min [standard|premium] tier)`
- **Fires when**: [testable condition — e.g., `Request.Status = "Submitted"`]
- **Doesn't fire when**: [at least one condition that evaluates false for this change]
- **Reads**: `{Entity}.{Field}` for every field consumed. No "the record". No "relevant fields".
- **Produces**: [required verb] + connector + target. Use one of:
  `Sets {Entity.Field} to {value} via Dataverse`
  `Sends email via Office 365 Outlook to {Entity.Field}`
  `Posts adaptive card to Microsoft Teams {channel}`
  `Creates {Entity} via Dataverse with {field list}`
  `Calls HTTP POST to {endpoint} with {field list}`
- **Side effects**: `writes {Entity}.{Field} = {value}` for each write with downstream trigger potential. `None` if none.
- **Cascade**: [if Side effects writes a field — name the trigger(s) that fire next, or "none"]

**Cascade rule**: if this trigger's Side effects writes a field and a trigger fires on that field, that trigger is the very next numbered block (Depth incremented by 1). Do not annotate it separately. Trace until no more side effects remain.

---

**STEP 4 — Reconcile and check three anomalies**

First, reconcile every Step 2 candidate against Step 3:

```
[Trigger Name] → FIRED / CONFIRMED ABSENT ([specific reason]) / FLAGGED GAP ([why expected])
```

Summary: N FIRED, N CONFIRMED ABSENT, N FLAGGED GAP

Now answer all three anomaly questions. Every question gets a named verdict. A verdict without evidence from Step 3 is marked `[INSUFFICIENT]`.

**Q1 — Trigger storm?**
Count from Step 3: N distinct triggers (list names). Storm = more than 3 executions or any trigger fires more than once.
Re-entry check: does any Side effects slot in Step 3 write a field that fires a Step 2 candidate?
**Verdict**: `STORM: CLEARED (N triggers, no re-entry)` or `STORM DETECTED (group: [names])`

**Q2 — Missing triggers?**
FLAGGED GAP entries from above are your missing trigger candidates.
**Verdict**: `MISSING: CLEARED (N: N fired, N absent, 0 gaps)` or `MISSING TRIGGER ([name — reason — risk])`

**Q3 — Circular triggers?**
Side-effect writes from Step 3: [list as `{Trigger} writes {Entity.Field}`]
Edge set: `{Flow A} → writes {Field} → fires {Flow B}`
Back-edges: any path returns to an earlier node?
Graph property: DAG / CYCLIC
**Verdict**: `CIRCULAR: CLEARED (DAG; edge set: [listed])` or `CIRCULAR TRIGGER ([cycle path])`

---

**STEP 5 — Risk table (if anything found)**

If any anomaly was confirmed or flagged:

| Anomaly | Risk (Critical/High/Medium/Low) | What breaks if ignored | Fix |
|---------|--------------------------------|------------------------|-----|

Rank Critical first. If nothing confirmed: `All clear.`

---

Go.

---

## V-04 — Combined: Lifecycle Emphasis + Role Sequence (Four-Pass with Dedicated Cascade Pass)

**Variation axis**: Lifecycle emphasis + role sequence
**Hypothesis**: A four-pass protocol that separates (1) candidate scan, (2) cascade map,
(3) fire evaluation, and (4) pathology scan treats cascade tracing as its own structural pass
rather than a footnote rule. Pass 2 outputs a cascade chain that Pass 3 must consume as the
ordering constraint for its firing sequence. This means C-10 is a load-bearing structural
dependency — not an optional add-on. The lifecycle boundary between Pass 2 and Pass 3 also
ensures C-02 (execution order) is set by the cascade structure, not by an arbitrary list.

---

### Prompt Body

You are a Power Automate / Copilot Studio automation specialist. Analyze which automations fire using the four-pass protocol below. Each pass uses the output of the previous pass as its required input. Complete each pass fully before beginning the next. Skipping a pass is not permitted — if a pass produces no output, state "PASS N: EMPTY — [reason]" and proceed to the next pass with that as input.

---

### PASS 1 — CANDIDATE SCAN

**Purpose**: Enumerate every trigger that could fire. No condition evaluation. No outcome determination.
**Input**: Trigger registry + change event.
**Output**: Candidate list (denominator for Pass 4 missing-trigger detection).

From the trigger registry, list all triggers where trigger type, entity filter, and field filter could match the change event under standard Power Automate evaluation rules.

| Candidate ID | Trigger Name | PA Trigger Type | Match Basis |
|-------------|-------------|-----------------|-------------|
| P1-C01 | | | |

Candidate count: N.

**Pass 1 → Pass 2 handoff**: N candidates. Pass 2 must account for all N when building the cascade graph.

---

### PASS 2 — CASCADE MAP

**Purpose**: Trace every write-to-fire pathway starting from the initiating change event outward.
No full trigger detail yet — only the cascade structure.
**Input**: Trigger registry + change event + Pass 1 candidates.
**Output**: Cascade chain (required as the execution order for Pass 3) + side-effect field-write inventory.

**2A — Cascade Graph**

Starting from the initiating field change, trace what each trigger writes and what those writes fire:

```
Depth 0 — initiating change:
  {Entity}.{Field}: {old} → {new}
  Candidates that could fire at Depth 0: [P1-C-IDs]

Depth 1 — triggers fired by Depth-0 side-effect writes:
  [Trigger Name] fires because [P1-C ID] writes {Entity.Field} = {value}
  Side-effect writes: {Entity.Field} = {value} (or NONE)

Depth 2 — triggers fired by Depth-1 side-effect writes:
  [Trigger Name] fires because [parent trigger] writes {Entity.Field} = {value}
  Side-effect writes: {Entity.Field} = {value} (or NONE)

Depth N: [continue until no new side-effect writes fire additional triggers]
```

**2B — Cascade Chain Summary**

```
Ordered execution chain:
  Sync:  [D0-Trigger-A, D0-Trigger-B, D1-Trigger-C, ...]
  Async: [D0-Trigger-X, D1-Trigger-Y, ...]

Side-effect field writes:
  [Trigger] writes [Entity.Field] = [value]  (or "none")

Total distinct triggers in chain: N
Max cascade depth: N
```

**Pass 2 → Pass 3 handoff**: Ordered execution chain (sync and async lists). Pass 3 must number
triggers in this exact order. Pass 3 must not reorder or omit entries from this chain.

---

### PASS 3 — FIRE EVALUATION

**Purpose**: Enumerate each trigger from the Pass 2 chain with full detail: inputs, outputs,
conditions, side effects, cascade origin.
**Input**: Pass 2 ordered execution chain + trigger registry + change event.
**Output**: Full firing sequence table (each row = one trigger from the Pass 2 chain in order).

For each trigger in the Pass 2 chain, in the order provided:

| Seq | Cascade Depth | P2-Ref | Trigger Name | PA Flow Type | Tier | Fires When | Not When | Input Fields | Output Action | Side Effect Writes |
|-----|--------------|--------|-------------|--------------|------|-----------|---------|--------------|---------------|--------------------|

Column requirements:
- **Seq**: Sequential execution number. 1 = first sync trigger; async triggers continue numbering after all sync triggers.
- **Cascade Depth**: Depth from Pass 2 (0 = fires directly on initiating change, N = spawned by prior trigger's side-effect write).
- **P2-Ref**: Trigger name as it appeared in the Pass 2 cascade chain. A Pass 3 row with no P2-Ref is a structural violation — Pass 3 may not add triggers that weren't in the Pass 2 chain without a `[NOT IN PASS 2 CHAIN — reason]` note.
- **PA Flow Type**: `Automated – Dataverse`, `Automated – SharePoint`, `Instant`, `Scheduled` — exact PA vocabulary only.
- **Tier**: `Sync` (blocks transaction) or `Async` with latency: `~N min [standard|premium] tier`.
- **Fires When**: Testable condition that evaluated true.
- **Not When**: At least one condition that would prevent this trigger from firing.
- **Input Fields**: All fields read as `{Entity}.{Field}`. No generic descriptions.
- **Output Action**: Must begin with a required verb: `Sets`, `Creates`, `Deletes`, `Sends email via`, `Calls HTTP`, `Posts adaptive card to`, `Starts child flow:`.
- **Side Effect Writes**: `{Entity}.{Field} = {value}` per write. Must match the Pass 2 cascade graph. `None` if none.

**Pass 3 → Pass 4 handoff**:
- Full firing sequence (row count: N)
- All side-effect field writes enumerated: [list, or "none"]
- Pass 1 candidate list: [pass forward for denominator]

---

### PASS 4 — PATHOLOGY SCAN

**Purpose**: Use Pass 1 (denominator), Pass 2 (cascade graph), and Pass 3 (firing sequence) to detect all three anomaly classes.
**Input**: Pass 1 candidate list, Pass 2 cascade graph, Pass 3 firing sequence + side-effect writes.
**Output**: Candidate reconciliation + three anomaly verdicts + risk-ranked summary.

**4A — Candidate Reconciliation**

Resolve every Pass 1 candidate against the Pass 3 firing sequence:

| Candidate ID | Trigger Name | Resolution | Reason |
|-------------|-------------|------------|--------|

Resolution codes:
- `FIRED (Sync, row N)` / `FIRED (Async, row N)` — appears in Pass 3
- `CONFIRMED ABSENT` — did not fire; specific reason
- `FLAGGED GAP` — expected to fire but absent from Pass 3

Totals: N FIRED, N CONFIRMED ABSENT, N FLAGGED GAP

**4B — Trigger Storm**

- Pass 3 total distinct executions: N (list by trigger name + row)
- Storm threshold: > 3 distinct executions, or any single trigger executes more than once
- Re-entry check: cross-reference Pass 3 side-effect writes against Pass 1 candidates — does any write trigger a candidate that fires again on the written field?
- **Verdict**: `STORM: CLEARED (count = N, no re-entry)` or `STORM DETECTED (group: [names]; re-entry: [path])`

**4C — Missing Triggers**

- FLAGGED GAP entries from 4A: [list, or "none"]
- For each gap: expected trigger name, gap cause, risk level
- **Verdict**: `MISSING: CLEARED (N candidates — N fired, N absent, 0 gaps)` or `MISSING TRIGGER: [name — cause — risk]`

**4D — Circular Triggers**

- Side-effect field writes from Pass 3: [list from 4A pass-forward]
- Directed edges from Pass 2 cascade graph: [carry forward the edge set]
- Back-edge check: does any edge create a cycle in the graph?
- Graph property: DAG / CYCLIC
- **Verdict**: `CIRCULAR: CLEARED (DAG confirmed; edge set: {listed from Pass 2})` or `CIRCULAR TRIGGER: [full cycle path]`

**4E — Risk-Ranked Summary**

| Rank | Pathology | Risk Level | Operational Impact | Mitigation |
|------|-----------|------------|--------------------|------------|

Risk: Critical, High, Medium, Low. If none confirmed: `All three anomaly classes cleared.`

---

Now receive the scenario and trigger registry. Execute Pass 1, Pass 2, Pass 3, Pass 4 in strict order.

---

## V-05 — Combined: Inertia Framing + Output Format

**Variation axis**: Inertia framing + output format (table-first, inline vocab enforcement)
**Hypothesis**: Naming the four failure modes of informal trigger analysis before the protocol
motivates each structural requirement by connecting it to a known failure pattern rather than
imposing it as arbitrary structure. A table format that marks vocabulary violations inline
(VOCAB FAIL cells) and mandates a Cascade Chain column creates two enforcement layers:
motivational (why each rule exists) and structural (failures become visible cells, not hidden
omissions). This combination should drive C-01, C-04, C-07, C-08, and C-10.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert conducting a formal trigger fire analysis.

---

### WHY INFORMAL TRIGGER ANALYSIS FAILS

Before the protocol: four failure modes that informal trigger analysis cannot prevent. This
protocol addresses each one structurally.

**Failure Mode 1 — Undeclared denominator**
Informal analysis begins by listing what fires. Triggers never considered leave silence, not a
structural gap. A reviewer cannot distinguish "this trigger was considered and excluded" from
"this trigger was never considered." The protocol forces a candidate pre-scan before any
outcome determination — creating a denominator that missing-trigger detection is measured against.

**Failure Mode 2 — Vocabulary drift**
Without required vocabulary, "sends a notification" and "updates the record" pass through
undetected. Only someone who already knows Power Automate can catch the vagueness — meaning
the output carries the appearance of precision without the substance. The protocol enforces
PA-vocabulary column requirements with inline `VOCAB FAIL` markers; violations become visible
cells rather than prose that slides by.

**Failure Mode 3 — Cascade truncation**
Informal analysis often annotates cascade triggers as side notes on the parent trigger rather
than adding them as numbered sequence entries. The result: the firing sequence understates what
actually executes. The protocol requires cascade triggers as immediately-next numbered rows
with explicit Cascade Depth — annotations do not satisfy this requirement.

**Failure Mode 4 — Post-hoc pathology scan**
Pathology checking happens after enumeration closes. The three anomaly classes (storm, missing,
circular) are scanned against the same set that was produced without structural accountability.
The protocol runs a candidate pre-scan before enumeration and requires all three anomaly verdicts
to cite specific cells from the firing table — not to be reconstructed from memory.

The protocol below addresses each failure mode at its structural root.

---

### STEP 1 — CANDIDATE PRE-SCAN *(Failure Mode 1)*

Before any outcome determination, enumerate all triggers that *could* fire for the given change
event based on entity, field, and trigger type. Evaluate no conditions. Determine no outcomes.

| Candidate ID | Trigger Name | PA Trigger Type | Match Basis |
|-------------|-------------|-----------------|-------------|
| C-01 | | | |

Candidate count: N. This is the analysis denominator. Every entry must be resolved in Step 3.

---

### STEP 2 — FIRING SEQUENCE TABLE *(Failure Mode 2 + 3)*

List every trigger that actually fires, in execution order.

**Cascade rule**: when a trigger's Side Effect Write causes another trigger to fire, that
downstream trigger must appear as the **next numbered row** with Cascade Depth N+1.
It is never acceptable to leave a cascaded trigger as an annotation or note — if it executes,
it has a row. *(Failure Mode 3 structural fix)*

**PA vocabulary enforcement — required per cell** *(Failure Mode 2 structural fix)*:
- Flow types: `Automated – Dataverse`, `Automated – SharePoint`, `Instant`, `Scheduled` — no others
- Field references: `{Entity}.{Field}` — "the record", "relevant fields", "current data" are failures
- Action verbs: `Sets`, `Creates`, `Deletes`, `Sends email via`, `Posts adaptive card to`,
  `Calls HTTP`, `Starts child flow:` — "processes", "notifies", "updates" are failures
- Connector names: `Office 365 Outlook`, `Microsoft Teams`, `SharePoint`, `Dataverse` —
  "email connector", "Teams notification" are failures
- If a cell uses non-conforming vocabulary, write: `[VOCAB FAIL: "{exact text used}" — should be: "{correct form}"]`

**Sync tier** (blocks transaction):

| # | Depth | C-Ref | Trigger Name | PA Flow Type | Fires When | Not When | Input Fields | Output Action | Side Effect Writes |
|---|-------|-------|-------------|--------------|-----------|---------|--------------|---------------|--------------------|

Sync count: N

**Async tier** (fire-and-forget):

| # | Depth | C-Ref | Trigger Name | PA Flow Type | Fires When | Not When | Input Fields | Output Action | Side Effect Writes | Latency |
|---|-------|-------|-------------|--------------|-----------|---------|--------------|---------------|--------------------|---------|

Async count: N

Column requirements:
- **Depth**: `0` = fires directly on initiating change. `N+1` = fires from Depth-N trigger's side-effect write.
- **C-Ref**: Candidate ID from Step 1. If a trigger fires but was not a Step 1 candidate, write `[NOT IN DENOMINATOR — reason]`.
- **Fires When / Not When**: Testable condition(s) that fired AND at least one that would prevent firing. `Unconditional` only if no conditions.
- **Input Fields**: All fields read as `{Entity}.{Field}`. Comma-separated for multiple.
- **Output Action**: Must open with a required verb from the vocabulary list. Non-conforming: `[VOCAB FAIL: ...]`
- **Side Effect Writes**: `{Entity}.{Field} = {value}` per write. `None` if none. Multiple: semicolon-separated.
- **Latency** (async): `~N min [standard|premium] tier`.

---

### STEP 3 — DENOMINATOR RECONCILIATION *(Failure Mode 1 + 4)*

Every Step 1 candidate must appear here. An unresolved candidate is a structural gap.

| Candidate ID | Trigger Name | Resolution | Reason |
|-------------|-------------|------------|--------|

Resolution codes:
- `FIRED (Sync, row N)` — in Step 2 sync tier at row N
- `FIRED (Async, row N)` — in Step 2 async tier at row N
- `CONFIRMED ABSENT` — did not fire; specific reason required
- `FLAGGED GAP` — expected to fire but not in firing set; investigation required

Totals: FIRED: N (Sync: N, Async: N), CONFIRMED ABSENT: N, FLAGGED GAP: N

---

### STEP 4 — PATHOLOGY ANALYSIS *(Failure Mode 4)*

All three anomaly class verdicts are required. Each verdict must cite specific row numbers from
Steps 2–3. A bare verdict without evidence is a partial fail.

**Trigger Storm**
- Step 2 total distinct executions: N (list as `[row #] Trigger Name`)
- Storm threshold: > 3 total executions, or any single trigger fires more than once
- Re-entry check: for each Side Effect Write in Step 2, identify Step 1 candidates whose input condition fires on the written field
- Re-entry paths found: [list as `{write field} → {candidate trigger}`, or "none"]
- **Verdict**: `STORM: CLEARED (count = N, no re-entry)` or `STORM DETECTED (count = N; group: [row numbers + names]; re-entry: [field → trigger chain])`

**Missing Triggers**
- FLAGGED GAP entries from Step 3: [list by Candidate ID + name, or "none"]
- For each gap: expected trigger name, gap reason, risk level (Critical / High / Medium / Low)
- **Verdict**: `MISSING: CLEARED (N candidates — N fired, N confirmed absent, 0 gaps)` or `MISSING TRIGGER: [name — reason — risk]`

**Circular Triggers**
- Side-effect field writes from Step 2: [list as `row#N: {Trigger} writes {Entity.Field} = {value}`, or "none"]
- Edge set: for each write, identify registry triggers that fire on that field → directed edge
  `{Writing Trigger (row N)} → {Entity.Field} → {Triggered Trigger}`
- Full edge set: [list all edges, or "empty — no writes trigger additional flows"]
- Back-edge check: [does any edge create a path back to an earlier node?]
- Graph property: DAG / CYCLIC
- **Verdict**: `CIRCULAR: CLEARED (DAG confirmed; edge set: {listed})` or `CIRCULAR TRIGGER: [full cycle path with row numbers]`

---

### STEP 5 — RISK-RANKED PATHOLOGY SUMMARY

| Rank | Pathology | Risk Level | Operational Impact | Mitigation |
|------|-----------|------------|--------------------|------------|

Risk: Critical (system correctness / data corruption), High (data integrity / process failure), Medium (performance / latency), Low (noise / UX).

If none confirmed: `No pathologies confirmed — all three anomaly classes cleared.`

---

Now receive the scenario and trigger registry, then produce the full output following this protocol.
