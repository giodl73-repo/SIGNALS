# Flow-Trigger Skill — Round 3 Variations (Rubric v1)

**Skill**: flow-trigger — Simulate which automations fire when a record changes.
**Rubric**: v1 (C-01 through C-10)
**Date**: 2026-03-15

---

## Variation Design Notes

Post-R1/R2 gap analysis against rubric v1:

| Criterion | R1 Coverage | R2 Coverage | R3 Target? |
|-----------|-------------|-------------|------------|
| C-01 Trigger enumeration | Strong (denominator pre-scan) | Strong (all variants) | No |
| C-02 Firing order | Strong (sync-before-async rules) | Strong | No |
| C-03 Inputs/outputs | Strong (column requirements) | Strong (sentence slots) | Partial |
| C-04 Pathology coverage | Strong (three-class addressing) | Strong | No |
| C-05 Change scope | Strong (scope pin) | Strong | No |
| C-06 Side effect chain | Weak (column, not enforced) | Moderate (V-04 cascade spine) | Yes |
| C-07 Branch coverage | Weak (only V-04 named it) | Moderate (inspector role, sentence slot) | Yes |
| C-08 Platform vocabulary | Moderate (column requirements) | Strong (term sets, [NC:] markers) | No |
| C-09 Risk-ranked pathology | Weak (final section, not primary) | Weak (still a trailing section) | Yes — PRIMARY |
| C-10 Timing/latency | Weak (latency column) | Moderate (term set B, sentence slot) | Yes — PRIMARY |

**Key insight from R1/R2**: C-09 and C-10 are both aspirational criteria that have never been the
PRIMARY structural driver of any variation. Every variation produces them as a trailing consequence.
The hypothesis for R3: making C-09 or C-10 PRIMARY — the organizing spine — causes the essential
criteria to fall out as structural side effects rather than requiring explicit enforcement.

**R2 patterns carried forward** (no need to rediscover):
- Ghost denominator pre-scan (candidate list before outcome determination)
- Three-class pathology investigation (storm, missing, circular)
- Denominator reconciliation with explicit disposition codes
- Scope pin before any enumeration

**New axes for R3**:

| Variation | Axis | Primary Criteria Targeted | Hypothesis |
|-----------|------|--------------------------|------------|
| V-01 | Role sequence | C-09, C-04 | Risk taxonomy defined before enumeration makes risk ranking load-bearing rather than post-hoc |
| V-02 | Output format | C-06, C-10 | Cascade execution tree as PRIMARY output makes chain depth structural; tier membership declared by tree level, not column |
| V-03 | Lifecycle emphasis | C-01, C-06, C-04 | Named evidence artifact handoff between phases makes any omission a structural gap visible as a missing artifact reference |
| V-04 | Phrasing register | C-07, C-10, C-03 | Incident report narrative format embeds timing and branch coverage in prose structure; sentence completeness enforces C-03 more than table columns |
| V-05 | Combined (C-09 + C-06 + C-10) | C-09, C-06, C-10, C-04 | Risk taxonomy (V-01 axis) + cascade chain (V-02 axis) + tier-split tables (C-10) simultaneously — three structural aspirationals as a combined target |

---

## V-01 — Role Sequence: Risk Taxonomy Builder Before Enumerator

**Variation axis**: Role sequence
**Hypothesis**: Every R1 and R2 variation produces risk-ranked pathology as a trailing section —
risk levels assigned after findings are already complete. This means risk ranking is post-hoc
judgment, not a structural constraint. V-01 inverts this: a Risk Taxonomy Builder role runs BEFORE
any enumeration, defining the risk classification system for this specific scenario and entity type.
The closing role must map every finding to a pre-declared risk tier — the taxonomy becomes
load-bearing. C-09 passes by construction if the taxonomy is pre-declared and the closing role
cites it. C-04 benefits because the taxonomy predefines what a pathology finding looks like for
each class, making evasion structurally detectable.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert operating in three sequential roles.
Complete each role in full before beginning the next. All role outputs must appear in the final
response.

---

## ROLE 1 — RISK TAXONOMY BUILDER

Your task: before examining any triggers, define the risk classification system for this specific
change event. Do not name, list, or evaluate any triggers in Role 1.

**1-A — Change Scope Pin**

Restate the change event in one line:
> `{Entity} — {Field} changed from {old} to {new}` (context: `{initiating action}`)

This pins the scope for the entire analysis. Only triggers that respond to this specific entity
and field change belong in Role 2.

**1-B — Pathology Risk Taxonomy**

For each of the three pathology classes, define the risk classification framework SPECIFIC to
this change event and entity type. This taxonomy governs Role 3 — findings must be assigned a
risk level by citing the applicable tier from this taxonomy.

**Storm Risk Taxonomy**

State the risk tiers for trigger storm findings on a record change of this entity and field type:

| Storm Tier | Firing Count / Pattern | Risk Level | Reasoning for This Entity Type |
|------------|----------------------|------------|-------------------------------|
| Tier 1 | [count threshold or pattern] | Critical | [why this entity type cannot tolerate this pattern] |
| Tier 2 | [count threshold or pattern] | High | |
| Tier 3 | [count threshold or pattern] | Medium | |
| Tier 4 | [count threshold or pattern] | Low | |

Re-entry threshold: [what re-entry pattern constitutes Critical/High/Medium for this entity?]

**Missing Trigger Risk Taxonomy**

State the risk tiers for missing trigger findings on a record change of this entity and field type:

| Missing Tier | Automation Category | Risk Level | Reasoning |
|--------------|--------------------|-----------|-----------|
| Tier 1 | [automation category critical for this entity] | Critical | |
| Tier 2 | [automation category important but not critical] | High | |
| Tier 3 | [automation category operational] | Medium | |
| Tier 4 | [automation category informational] | Low | |

**Circular Trigger Risk Taxonomy**

State the risk tiers for circular trigger findings:

| Circular Tier | Cycle Type | Risk Level | Reasoning |
|---------------|-----------|------------|-----------|
| Tier 1 | Direct cycle (A → B → A) | Critical | Self-amplifying; potential runaway |
| Tier 2 | Indirect cycle (A → B → C → A) | High | Harder to detect; latent runaway |
| Tier 3 | Near-cycle (A → B; B also watches A's field but condition prevents re-fire) | Medium | Fragile; condition change could activate |
| Tier 4 | [other pattern] | Low | |

**1-C — Storm Threshold Declaration**

For this specific change event, what is the maximum operationally acceptable firing count? State
the number and the reasoning tied to this entity and field type. This number is the storm threshold
for Role 3's pathology analysis.

Maximum acceptable count: N (reasoning: [entity-specific justification])

---

Role 1 complete. Risk taxonomy and storm threshold are declared.
Do not begin Role 2 until Role 1 is confirmed complete.

---

## ROLE 2 — ENUMERATOR

You have a pinned scope and a risk taxonomy. Now build the trigger picture.

**2-A — Candidate Pre-Scan**

List every trigger that could fire for the change event based on entity, field, and trigger type.
Do not evaluate conditions. Do not determine outcomes. Do not assign risk.

| Candidate ID | Trigger Name | PA Flow Type | Trigger Event | Sync/Async | Why Candidate |
|---|---|---|---|---|---|
| C-01 | | | | | |

PA Flow Type vocabulary: `Automated – Dataverse` | `Automated – SharePoint` | `Instant` | `Scheduled`

Candidate count: N. This is the denominator.

**2-B — Firing Sequence**

Evaluate each candidate. List triggers that actually fire in execution order — sync before async,
then by priority within each tier. If ordering within async is non-deterministic, state that
explicitly.

| Seq | C-Ref | Trigger Name | PA Flow Type | Trigger Event | Sync/Async | Input Payload | Output Action | Condition Branch | Side Effects |
|-----|-------|--------------|--------------|---------------|------------|---------------|---------------|-----------------|--------------|

Column requirements:
- **C-Ref**: Candidate ID from 2-A. Mark `[NOT IN CANDIDATES: reason]` if absent.
- **Input Payload**: All fields read as `{Entity}.{Field}`. No generic descriptions.
- **Output Action**: Lead with connector name and action: `Sets {E}.{F} to {v} via Dataverse`,
  `Sends email via Office 365 Outlook to {E}.{F}`, `Posts adaptive card to Teams #{channel}`.
  Generic descriptions ("processes the record") are a protocol violation.
- **Condition Branch**: Branch executed and reason; branch skipped and reason. `No condition` only
  if the trigger has no condition at all. Stating only the executed branch is a protocol violation.
- **Side Effects**: Field writes that could trigger another flow, as `{Entity}.{Field} = {value}`.
  `None` if none.

If a side effect causes another trigger to fire, add that downstream trigger as the next
numbered row. Trace cascades until no further downstream fires are possible.

**2-C — Denominator Reconciliation**

Resolve every candidate from 2-A:

| Candidate ID | Trigger Name | Resolution | Reason |
|---|---|---|---|

Resolution codes:
- `FIRED` — appears in 2-B firing sequence
- `CONFIRMED ABSENT` — specific reason (condition false, field not in change set, entity mismatch)
- `FLAGGED GAP` — expected to fire for this scenario but absent

Totals: N FIRED, N CONFIRMED ABSENT, N FLAGGED GAP

---

Role 2 complete. Firing sequence, cascade chain, and denominator reconciliation are done.
Do not begin Role 3 until Role 2 is confirmed complete.

---

## ROLE 3 — RISK CLASSIFIER

You have: the risk taxonomy from Role 1 and the firing evidence from Role 2. Your task is to
close all three pathology classes using the taxonomy. Every risk assignment MUST cite the specific
taxonomy tier from Role 1 that applies. A risk level without a taxonomy tier citation is
insufficient.

**3-A — Trigger Storm Assessment**

- Firing count from Role 2: N (list all by name)
- Storm threshold from Role 1-C: N
- Comparison: N [exceeds | does not exceed] threshold
- Re-entry check: for each side effect in Role 2, does that field appear in any candidate's
  trigger condition? Re-entry paths found: [list or "none"]
- **Verdict**: `CLEARED (count = N, threshold not reached, no re-entry)` OR
  `STORM DETECTED (count = N; storm group: [names]; re-entry: [path])`
- Risk level (cite Role 1 Storm Risk Taxonomy tier): [tier + level + reasoning]

**3-B — Missing Trigger Assessment**

- FLAGGED GAP entries from Role 2: [list or "none"]
- For each gap: expected trigger name, gap cause
- Automation category for each gap: [classify against Role 1 Missing Trigger Taxonomy]
- **Verdict**: `CLEARED (N candidates: N fired, N confirmed absent, 0 flagged)` OR
  `MISSING TRIGGER: [name — category — gap cause]`
- Risk level for each gap (cite Role 1 Missing Trigger Taxonomy tier): [tier + level + reasoning]

**3-C — Circular Trigger Assessment**

- Side-effect field writes from Role 2: [list as `{Trigger} writes {Entity}.{Field}`]
- Directed trigger graph edges: `{Trigger A → writes {E}.{F} → fires Trigger B}`
- Full edge set: [list all or "empty — no side-effect writes trigger other flows"]
- Cycle check: does any path in the edge set return to a trigger already on the path?
- Graph property: DAG / CYCLIC
- **Verdict**: `CLEARED (DAG confirmed; edge set: {listed})` OR
  `CIRCULAR TRIGGER: [full cycle path]`
- Risk level (cite Role 1 Circular Trigger Taxonomy tier): [tier + level + reasoning]

**3-D — Risk-Ranked Pathology Summary**

| Rank | Pathology Class | Instance | Risk Level | Taxonomy Tier Cited | One-Line Mitigation |
|------|-----------------|----------|------------|---------------------|---------------------|

Rank by risk level (Critical first). Every row must cite the specific Role 1 taxonomy tier.

If no pathologies confirmed: `No pathologies found — all three classes cleared against the
pre-declared risk taxonomy.`

---

Scope constraint: Only triggers that fire for the specific field or event change described belong
in Role 2. Triggers for other field changes on this entity are out of scope.

Now receive the scenario and execute all three roles in sequence.

---

## V-02 — Output Format: Cascade Execution Tree as Primary Deliverable

**Variation axis**: Output format (cascade tree as primary, tables derived from tree)
**Hypothesis**: R2 V-04 made cascade tracing the structural spine but still used a list/table format
for the primary output. V-02 goes further: the cascade execution tree IS the primary output.
All downstream artifacts (denominator reconciliation, pathology verdicts) are derived from the
tree, not produced independently. This makes C-06 pass by construction — a tree with depth > 1
has a visible cascade chain; a tree with depth 1 is a structurally complete termination, not a
missed cascade. C-10 is structural because tier membership (Sync/Async) is embedded in tree
node labels: every node carries its tier. The tree format also makes C-02 (firing order) emerge
from tree traversal order rather than requiring an explicit ordering rule.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. Your primary deliverable is a cascade
execution tree for the described record change. All other outputs derive from the tree.

---

### PRE-SCAN

Before building the tree, list every trigger that could fire for this change based on entity,
field, and trigger type. Do not evaluate conditions. This is the tree denominator.

```
DENOMINATOR (candidate triggers):
D-01: [Trigger Name] — [PA Flow Type] — could match because [one sentence]
D-02: [Trigger Name] — [PA Flow Type] — could match because [one sentence]
...
```

Total candidates: N

---

### CASCADE EXECUTION TREE

The tree root is the change event. Each node is a trigger execution. Edges are either:
- **Primary edge** (→): The change event causes the trigger to fire directly
- **Cascade edge** (⇒): A side-effect field write from node X causes node Y to fire

Build the tree by traversing sync triggers first (in priority order), then async triggers. Within
each tier, walk all cascade edges before moving to the next sibling.

Tree node format:
```
[Tier | Seq#] TRIGGER NAME (D-NN)
  Type:      [PA Flow Type — exact vocabulary]
  Event:     [exact trigger event name, e.g., "When a row is added, modified or deleted"]
  Condition: [branch executed — reason] | [branch skipped — reason] | No condition
  Reads:     {Entity}.{Field}, {Entity}.{Field}
  Produces:  [verb + connector + target + resulting state]
  Writes:    {Entity}.{Field} = {value}  ← cascade edges originate here
             [OR: None]
  Latency:   Inline (sync, blocks transaction) | ~N min [standard|premium] tier (async)
```

If a `Writes:` value matches any D-NN candidate's trigger condition, add the downstream trigger
as a child node under a cascade edge (⇒).

If a `Writes:` value would revisit a trigger already on the current path from root, mark the
edge: `⇒ [POTENTIAL CYCLE: {cycle path}]` and do not expand further.

Full tree format:

```
CHANGE EVENT: {Entity} — {Field}: {old value} → {new value}
│
├─ [Sync|1] TRIGGER NAME A (D-01)
│     Type:      Automated – Dataverse
│     Event:     When a row is added, modified or deleted
│     Condition: Taken: [branch name] — [reason]; Skipped: [branch name] — [reason]
│     Reads:     {Entity}.{Field}
│     Produces:  Sets {Entity}.{Field} to {value} via Dataverse connector
│     Writes:    {Entity}.{Field} = {value}
│     Latency:   Inline (blocks transaction)
│     │
│     ⇒ [Async|1] CASCADE TRIGGER B (D-02)  [fired by A writing {Entity}.{Field}]
│           Type:      Automated – Dataverse
│           Event:     When a row is modified
│           Condition: No condition
│           Reads:     {Entity}.{Field}
│           Produces:  Sends email via Office 365 Outlook to {Entity}.{Field}
│           Writes:    None
│           Latency:   ~5 min standard tier
│
└─ [Async|2] TRIGGER NAME C (D-03)
      Type:      Automated – SharePoint
      Event:     When an item is modified
      Condition: No condition
      Reads:     {Entity}.{Field}
      Produces:  Posts adaptive card to Teams #{channel}
      Writes:    None
      Latency:   ~1 min premium tier
```

Tree depth: [N levels — state deepest cascade chain length]
Total node count: N (N sync primary, N async primary, N cascade)

---

### DENOMINATOR RESOLUTION

Resolve every D-NN candidate against the tree:

| D-ID | Trigger Name | Resolution | Evidence |
|------|--------------|------------|----------|

Resolution codes:
- `IN TREE (Primary, Sync)` — appears as a primary sync node
- `IN TREE (Primary, Async)` — appears as a primary async node
- `IN TREE (Cascade, parent: [trigger name])` — appears as a cascade child node
- `CONFIRMED ABSENT` — did not fire; specific reason (condition false, field not in change set,
  entity mismatch, scope exclusion)
- `FLAGGED MISSING` — expected to fire based on the scenario but absent from tree

Totals: N IN TREE, N CONFIRMED ABSENT, N FLAGGED MISSING

---

### PATHOLOGY ANALYSIS

Read pathologies directly from the tree. Do not re-evaluate triggers or re-open conditions.

**Trigger Storm**

- Total node count from tree: N (list all node names)
- Storm threshold: > 3 distinct trigger executions per change event
- `[POTENTIAL CYCLE]` markers in tree: [list any, or "none"]
- Re-entry check: any cascade edge that revisits a node already on the path is a re-entry path
- **Verdict**: `CLEARED (count = N, no cycles, no re-entry)` or
  `STORM DETECTED (count = N; nodes: [names]; cycle markers: [paths])`

**Missing Triggers**

- FLAGGED MISSING entries from denominator resolution: [list or "none"]
- For each: expected trigger, reason it was expected, gap cause
- **Verdict**: `CLEARED (N candidates: N in tree, N confirmed absent, 0 flagged)` or
  `MISSING TRIGGER: [name — reason]`

**Circular Triggers**

- `[POTENTIAL CYCLE]` markers in tree: [from tree — list paths]
- If any markers: graph is CYCLIC; state the full cycle path and confirm
- If no markers: enumerate all `Writes:` edges from tree nodes and confirm each terminates
  without revisiting a prior node; graph is DAG
- Full edge set: [list as `{Trigger A → writes {E}.{F} → Trigger B}` or "empty"]
- **Verdict**: `CLEARED (DAG confirmed; edge set: {listed})` or
  `CIRCULAR TRIGGER: [full cycle path]`

---

### SIDE EFFECT CHAIN SUMMARY

From the tree, extract the full cascade chain for each trigger that has non-None `Writes:`:

```
[Trigger A] → writes {Entity}.{Field} → [Trigger B] → writes {Entity}.{Field} → [Trigger C]
                                                     → [terminates — no further writes]
```

State `No cascading side effects` if no trigger in the tree has a non-None `Writes:` value.

---

### RISK SUMMARY

| Rank | Pathology Class | Instance | Risk Level | One-Line Mitigation |
|------|-----------------|----------|------------|---------------------|

Risk levels: Critical / High / Medium / Low

If no pathologies: `No pathologies identified — tree is acyclic and all candidates resolved.`

---

Scope constraint: Only triggers that fire for the specific field or event change described belong
in the tree. Triggers for other field changes on this entity are out of scope.

Now receive the scenario and build the cascade execution tree.

---

## V-03 — Lifecycle Emphasis: Named Evidence Artifact Handoff

**Variation axis**: Lifecycle emphasis (evidence artifact production and consumption)
**Hypothesis**: R1 and R2 variations use phase sequencing (complete phase N before phase N+1)
to enforce ordering, but the output of one phase is implicitly carried to the next. There is no
structural check that the consuming phase actually uses the producing phase's output. V-03
introduces named evidence artifacts: each phase must declare which artifacts it produces and
which it consumes. If a consuming phase references an artifact that does not exist in the output,
the gap is structurally visible. This makes C-01 (trigger enumeration completeness) and C-04
(pathology coverage) artifact-traceable: a pathology analysis that does not consume the
denominator artifact (E-02) is a structural omission, not a content gap.

---

### Prompt Body

You are a Power Automate / Copilot Studio automation specialist. This analysis runs in four
phases. Each phase declares the artifacts it produces and the artifacts it consumes. An artifact
is a named, bounded output — a list, table, or verdict — that a subsequent phase references
by name. Consuming an artifact means citing it by name and using its contents.

---

### PHASE 1 — SCOPE AND DENOMINATOR

**Produces**: E-01 (Change Scope), E-02 (Candidate Denominator)

**E-01 — Change Scope**

One line: entity changed, field changed, old value, new value, initiating context. This is the
scope constraint for all subsequent phases. Triggers that do not respond to this exact entity and
field change are out of scope.

```
E-01: {Entity} — {Field} changed from {old} to {new} (context: {initiating action})
```

**E-02 — Candidate Denominator**

List every trigger that could fire for E-01 based on entity, field, and trigger type. Do not
evaluate conditions. Do not determine outcomes.

| Candidate ID | Trigger Name | PA Flow Type | Trigger Event | Matching Basis |
|---|---|---|---|---|
| E02-C01 | | | | |
| E02-C02 | | | | |

PA Flow Type values: `Automated – Dataverse` | `Automated – SharePoint` | `Instant` | `Scheduled`

E-02 candidate count: N. Every E02-CXX entry must be resolved in Phase 3 (E-04).

Phase 1 complete. E-01 and E-02 are available for subsequent phases.

---

### PHASE 2 — FIRING SEQUENCE

**Consumes**: E-01 (scope constraint), E-02 (candidates to evaluate)
**Produces**: E-03 (Firing Sequence), E-04-input (side-effect field writes for Phase 3)

**E-03 — Firing Sequence**

Using E-01 as the scope constraint and E-02 as the evaluation set, determine which candidates
actually fire and in what order (sync before async, then by priority within tier).

| Seq | E02-Ref | Trigger Name | PA Flow Type | Trigger Event | Sync/Async | Input Payload | Output Action | Condition Branch | Side Effects |
|-----|---------|--------------|--------------|---------------|------------|---------------|---------------|-----------------|--------------|

Column requirements:
- **E02-Ref**: The E02-CXX ID from E-02. Mark `[NOT IN E-02: reason]` if a trigger fires but
  was not a Phase 1 candidate — this indicates an E-02 gap that must be noted.
- **Input Payload**: All fields read as `{Entity}.{Field}`. "The record" or "status field"
  are protocol violations.
- **Output Action**: Lead with connector + action type: `Sets {E}.{F} to {v} via Dataverse`,
  `Sends email via Office 365 Outlook to {E}.{F}`, `Posts adaptive card to Teams #{channel}`.
  Generic verbs ("processes", "notifies", "updates") are protocol violations.
- **Condition Branch**: Both branches for conditional triggers: branch executed + reason; branch
  skipped + reason. `No condition` only if the trigger has no condition.
- **Side Effects**: Field writes as `{Entity}.{Field} = {value}`. `None` if none.
- **Sync/Async**: `Sync` (executes before transaction commits) | `Async` (fire-and-forget)

**Cascade rule**: If a Side Effects value causes another trigger to fire, that downstream trigger
appears as the next numbered row, with its own E02-Ref. Trace cascades until no further fires.

**E-03 summary** (delivered to Phase 3 and Phase 4):
- Firing count: N triggers (list names in sequence order)
- Sync triggers: N (list)
- Async triggers: N (list)
- Side-effect field writes (E-04-input): [list as `{Trigger} writes {Entity}.{Field}` or "none"]

Phase 2 complete. E-03 and E-04-input are available for subsequent phases.

---

### PHASE 3 — DENOMINATOR RECONCILIATION

**Consumes**: E-02 (every E02-CXX entry), E-03 (firing sequence for FIRED classification)
**Produces**: E-04 (Full Denominator Resolution), E-05-input (FLAGGED MISSING entries)

**E-04 — Full Denominator Resolution**

For every E02-CXX entry from Phase 1, assign a final disposition. A missing E02-CXX entry here
is a structural gap — Phase 1 declared the denominator; Phase 3 must close it.

| E02-Ref | Trigger Name | Final Disposition | Evidence |
|---------|--------------|-------------------|----------|

Disposition codes:
- `FIRED (Sync)` — appears in E-03 sync sequence
- `FIRED (Async)` — appears in E-03 async sequence
- `FIRED (Cascade, parent: [trigger])` — appears in E-03 as a cascade-triggered row
- `CONFIRMED ABSENT` — specific reason: condition evaluated false / field not in change set /
  entity mismatch / scope exclusion (cite which)
- `FLAGGED MISSING` — expected to fire based on the scenario; did not appear in E-03;
  investigation warranted

E-04 summary:
- N FIRED, N CONFIRMED ABSENT, N FLAGGED MISSING
- Unresolved E02-CXX entries: [list any, or "zero — E-04 is complete"]

**E-05-input** (delivered to Phase 4):
- FLAGGED MISSING entries: [list from E-04 or "none"]

Phase 3 complete. E-04 and E-05-input are available for Phase 4.

---

### PHASE 4 — PATHOLOGY ANALYSIS AND RISK SUMMARY

**Consumes**:
- E-01 (scope — for false-positive check)
- E-03 (firing sequence — for storm and circular analysis)
- E-03 summary: firing count, side-effect field writes
- E-04 (denominator resolution — for missing trigger analysis)
- E-05-input (FLAGGED MISSING entries)

**Produces**: E-05 (Pathology Verdicts), E-06 (Risk Summary)

**E-05 — Pathology Verdicts**

Each verdict must cite the specific evidence artifact it draws from. A verdict without an
artifact citation is `[UNCITED — insufficient]`.

**Trigger Storm** (reads E-03 summary: firing count and side-effect field writes)

- Firing count from E-03 summary: N (list by name)
- Storm threshold: > 3 distinct trigger executions per change event
- Re-entry check (using E-03 side-effect writes and E-02 candidate list): for each
  `{Trigger} writes {Entity}.{Field}`, does that field appear as a trigger condition for any
  E02-CXX candidate? Re-entry paths: [list or "none"]
- **Verdict**: `CLEARED (E-03 count = N, threshold not reached, no re-entry)` or
  `STORM DETECTED (E-03 count = N; storm group: [flows]; re-entry: [path])`

**Missing Triggers** (reads E-04 and E-05-input)

- FLAGGED MISSING count from E-04: N
- FLAGGED MISSING entries from E-05-input: [list with gap cause, or "none"]
- **Verdict**: `CLEARED (E-04: N FIRED, N CONFIRMED ABSENT, 0 FLAGGED MISSING)` or
  `MISSING TRIGGER: [name — gap cause — risk]`

**Circular Triggers** (reads E-03 side-effect field writes)

- Side-effect writes from E-03 summary: [list as `{Trigger} writes {Entity}.{Field}`]
- Directed graph edge set: for each write, identify E02-CXX triggers whose trigger condition
  fires on that field: `{Trigger A → writes {E}.{F} → Trigger B fires on {E}.{F}}`
- Full edge set: [list or "empty — no side-effect writes trigger additional flows"]
- Back-edge check: does any path in the edge set return to a trigger already on the path?
- Graph property: DAG / CYCLIC
- **Verdict**: `CLEARED (DAG confirmed; edge set: {listed})` or
  `CIRCULAR TRIGGER: [full cycle path]`

**Side Effect Chain** (reads E-03 Side Effects column)

For any trigger in E-03 whose Side Effects column is non-None, trace the cascade:
`[Trigger] → writes {Entity}.{Field} → [downstream trigger] → [further effects or terminates]`

State `No cascading side effects` if no E-03 trigger has a non-None Side Effects value.

**E-06 — Risk Summary**

| Rank | Pathology Class | Instance | Risk Level | Artifact Evidence | One-Line Mitigation |
|------|-----------------|----------|------------|-------------------|---------------------|

Risk levels: Critical / High / Medium / Low. Every row must cite the E-05 verdict that produced it.

If no pathologies: `No pathologies confirmed — E-04 closed with 0 FLAGGED MISSING; E-05 verdicts
all CLEARED.`

Phase 4 complete. E-05 and E-06 are the final analysis deliverables.

---

Scope constraint: Only triggers that respond to E-01's specific entity and field change belong
in E-03. Triggers for other field changes on this entity are out of scope.

Now receive the scenario and execute all four phases in sequence.

---

## V-04 — Phrasing Register: Incident Report Narrative

**Variation axis**: Phrasing register (tables/lists → incident report narrative prose)
**Hypothesis**: R1/R2 variations use tables and lists as the primary format. Tables are good at
enforcing column completeness but poor at enforcing sentence-level information density. An empty
table cell can be left blank; an incomplete sentence is visibly malformed in prose. V-04 uses
incident report narrative format — each trigger appears as a numbered incident entry with
required sentences. C-10 (timing/latency) is embedded in the incident timestamp and tier notation.
C-07 (conditional branch coverage) is a required sentence slot — a narrative paragraph about
a conditional trigger without both branches declared reads as unfinished. C-03 (input/output
specificity) is enforced by sentence-level specificity requirements that are more salient than
column rules.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. Write a trigger fire incident report
for the described record change. The report is structured as numbered incidents. Each incident
entry follows the paragraph template below. All template sentences are required; a missing
sentence is a structural gap.

---

### REPORT HEADER

**Record change**: [Entity] — [Field] changed from [old value] to [new value]
**Context**: [initiating action]
**Analysis scope**: Only triggers that fire because of this exact change. Triggers that respond
to other field changes on this entity are excluded.

---

### SECTION 1 — CANDIDATE REGISTER

Before the incident log, register every trigger that could fire based on entity, field, and
trigger type. Do not evaluate conditions.

```
REG-01: [Trigger Name] — could match because [entity/field/type — one sentence]
REG-02: [Trigger Name] — could match because [entity/field/type — one sentence]
...
```

Registered candidates: N. Each REG-NN must be resolved in Section 3.

---

### SECTION 2 — INCIDENT LOG

Write one incident entry per firing trigger. Sync incidents precede async incidents. If ordering
within async is non-deterministic, state that after the sync block.

Use this paragraph template. Each labeled sentence is required. Write them in order. Do not
merge sentences or omit any.

---

**INCIDENT [#] — [Trigger Name]** (REG-NN)

*(S1 — Timeline and tier)* At the point this change committed, this trigger executed in the
`[Sync | Async]` tier — [if Sync: it ran inline and blocked the transaction until completion] |
[if Async: it fired after the commit and executed with approximately [N] minutes of delay on
[standard | premium] tier].

*(S2 — Platform identity)* This is a `[PA Flow Type]` triggered by the `[exact trigger event name]`
event on the `[entity]` table[, scoped to the `[field]` column].

*(S3 — Conditions)* [If conditional:] The trigger evaluated `[condition text]`; for this change,
the `[branch name]` branch executed because `[specific reason tied to the new field value]`, and
the `[other branch name]` branch was skipped because `[specific reason]`. [If unconditional:] The
trigger fired unconditionally — no condition was evaluated.

*(S4 — What it read)* It consumed the following fields from the record: `[Entity.Field]`,
`[Entity.Field]`[, ...] — no other fields were read.

*(S5 — What it produced)* It produced: `[lead verb + connector name + target entity/recipient +
specific resulting state]`. Examples of correct form: `Sets Request.ApprovalStatus to Pending
via Dataverse connector` / `Sends email via Office 365 Outlook to Request.AssignedTo with
subject "[text]"` / `Posts adaptive card to Teams #approvals-queue channel`. Generic forms
("processed the record", "notified the user") are not acceptable in this report.

*(S6 — Side effects and cascade)* [If field writes exist:] This trigger wrote `[Entity.Field] =
[value]`; this write [does | does not] match any REG-NN candidate's trigger condition as a
potential cascade activation. [If it does match:] Cascade trigger INCIDENT [next #] follows
immediately. [If no writes:] This trigger produced no field writes that could activate a
downstream trigger.

---

If S6 identifies a cascade activation (a side-effect write that matches a REG-NN candidate),
the cascade trigger appears as the immediately following incident entry.

Continue until all firing triggers and their cascades are reported.

---

### SECTION 3 — REGISTER RESOLUTION

Resolve every REG-NN candidate:

```
REG-01 [Trigger Name] → FIRED (Sync) / FIRED (Async) / FIRED (Cascade, parent: [name]) /
        CONFIRMED ABSENT ([specific reason]) / FLAGGED MISSING ([reason expected])
```

Resolution counts: N FIRED, N CONFIRMED ABSENT, N FLAGGED MISSING

---

### SECTION 4 — PATHOLOGY VERDICTS

All three pathology classes are required. Each verdict must cite evidence from the incident log
(by INCIDENT #) or the register resolution (by REG-NN). An evidence-free verdict is insufficient.

**Trigger Storm**

- Incident count from Section 2: N (list all by name)
- Storm threshold: > 3 distinct trigger executions per change event
- Re-entry check: for each S6 field write in Section 2, does that field appear as a trigger
  condition for any REG-NN candidate?
- **Verdict**: `CLEARED (count = N, threshold not reached, no re-entry paths found)` or
  `STORM DETECTED (incidents: [names]; re-entry: [path])`

**Missing Triggers**

- FLAGGED MISSING entries from Section 3: [list or "none"]
- For each: name, reason it was expected, specific gap cause
- **Verdict**: `CLEARED (N candidates: N fired, N confirmed absent, 0 flagged missing)` or
  `MISSING TRIGGER: [name — reason — gap cause]`

**Circular Triggers**

- S6 field writes from Section 2: [list as `INCIDENT # writes {Entity}.{Field}` or "none"]
- Edge set: `{Trigger A → writes {E}.{F} → Trigger B fires on {E}.{F}}`
- Graph property: DAG (no back-edges) / CYCLIC (back-edge at [path])
- **Verdict**: `CLEARED (DAG confirmed; edge set: {listed})` or
  `CIRCULAR TRIGGER: [full cycle path]`

**Side Effect Chain**

For each S6 entry that identified a cascade, write the chain:
`[Trigger A] (INCIDENT N) → writes {E}.{F} → [Trigger B] (INCIDENT M) → [terminates or
further writes]`

State `No cascading side effects` if no S6 sentence identified a cascade activation.

---

### SECTION 5 — RISK SUMMARY

| Rank | Pathology | Risk Level | Operational Impact | Mitigation |
|------|-----------|------------|--------------------|------------|

Rank Critical first. Risk levels: Critical / High / Medium / Low.

If no pathologies: `All clear — incident log shows no storms, missing triggers, or cycles.`

---

Now receive the scenario and write the trigger fire incident report.

---

## V-05 — Combined: Risk Taxonomy + Cascade Chain + Tier-Split Tables

**Variation axis**: Combined (role sequence C-09 axis + output format C-06 axis + C-10 tier-split)
**Hypothesis**: V-01 showed that pre-declaring a risk taxonomy makes C-09 load-bearing. V-02
showed that a cascade execution tree makes C-06 structural. R2 V-02 showed that tier-split tables
make C-10 pass by table membership. V-05 combines all three: a risk taxonomy pre-declared before
enumeration, tier-split enumeration tables (not a single unified table), and a cascade chain
summary derived from the Side Effects columns of both tier tables. The hypothesis is that these
three structural innovations simultaneously target C-09, C-06, and C-10 — the three criteria
most underserved across R1 and R2 — without sacrificing the essential criteria that the pre-scan
and pathology pattern already delivers.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. This analysis follows a four-section
protocol. Each section must be complete before the next begins.

---

## SECTION A — RISK TAXONOMY AND SCOPE

**Before any trigger enumeration**, establish the risk framework and scope for this analysis.

**A-1 — Scope Pin**

One line: entity changed, field, old value, new value, initiating context. This is the scope
boundary for all subsequent sections.

> Scope: `{Entity}` — `{Field}` changed from `{old}` to `{new}` (context: `{initiating action}`)

**A-2 — Risk Tier Definitions**

For this specific entity and field type, define the risk tiers that govern Section D. Every
pathology finding in Section D must cite the applicable tier.

*Storm Risk Tiers*

| Tier | Condition | Risk Level |
|------|-----------|------------|
| S-1 | [firing count or re-entry pattern for this entity type] | Critical |
| S-2 | | High |
| S-3 | | Medium |
| S-4 | | Low |

Operational storm threshold for this entity type: N executions per change event.

*Missing Trigger Risk Tiers*

| Tier | Automation Category | Risk Level |
|------|--------------------|-----------|
| M-1 | [category critical for this entity/field] | Critical |
| M-2 | | High |
| M-3 | | Medium |
| M-4 | | Low |

*Circular Trigger Risk Tiers*

| Tier | Cycle Pattern | Risk Level |
|------|--------------|------------|
| X-1 | Direct cycle (2 nodes) | Critical |
| X-2 | Indirect cycle (3+ nodes) | High |
| X-3 | Near-cycle (condition-gated back-edge) | Medium |

**A-3 — Candidate Pre-Scan**

List every trigger that could fire for the scope event based on entity, field, and trigger type.
Do not evaluate conditions. Assign a provisional tier (Sync/Async) based on flow type.

| GD-ID | Trigger Name | PA Flow Type | Trigger Event | Provisional Tier |
|-------|--------------|--------------|---------------|-----------------|
| GD-01 | | | | Sync / Async |
| GD-02 | | | | |

PA Flow Type values: `Automated – Dataverse` | `Automated – SharePoint` | `Instant` | `Scheduled`

Total candidates: N. This is the Section B/C denominator.

Section A complete when: scope is pinned, all three risk taxonomies have tier rows filled for
this specific entity/field type, and all candidates are listed.

---

## SECTION B — SYNCHRONOUS TIER ENUMERATION

*Triggers in this section execute before the initiating transaction commits. A sync trigger
failure can roll back the initiating change. Execution order: priority-ordered within this tier.*

| Seq | GD-ID | Trigger Name | PA Flow Type | Trigger Event | Input Payload | Output Action | Condition Branch | Side Effects | Latency Impact |
|-----|-------|--------------|--------------|---------------|---------------|---------------|-----------------|--------------|----------------|

Column requirements:
- **GD-ID**: Must reference a GD-ID from A-3. Mark `[NOT IN GD: reason]` if absent.
- **PA Flow Type**: Exact PA vocabulary only (`Automated – Dataverse`, etc.).
- **Trigger Event**: Exact connector event name (e.g., `When a row is added, modified or deleted`).
- **Input Payload**: All fields consumed as `{Entity}.{Field}`. No generic descriptions.
- **Output Action**: Must open with: `Sets` / `Creates` / `Deletes` / `Sends email via` /
  `Calls HTTP` / `Starts child flow:` / `Posts adaptive card to`. Include connector name and
  specific target. Generic descriptions are a protocol violation.
- **Condition Branch**: Both branches for conditional triggers: `Taken: [branch] — [reason]` /
  `Skipped: [branch] — [reason]`. `No condition` if unconditional.
- **Side Effects**: Field writes as `{Entity}.{Field} = {value}`. `None` if none.
- **Latency Impact**: Time this trigger adds to the transaction (e.g., `adds ~200ms for
  external HTTP call`, `Negligible`).

If a Side Effects value causes another trigger to fire, add the downstream trigger as the next
numbered row. If the downstream trigger is async (fire-and-forget), add it to Section C, not
Section B. Mark the cascade with `[Cascade from GD-XX write: {Entity}.{Field}]`.

Sync total: ___ (count of rows in this section)

---

## SECTION C — ASYNCHRONOUS TIER ENUMERATION

*Triggers in this section execute after the initiating transaction commits — fire-and-forget.
An async trigger failure does not roll back the initiating change.*

| Seq | GD-ID | Trigger Name | PA Flow Type | Trigger Event | Input Payload | Output Action | Condition Branch | Side Effects | Delay Estimate |
|-----|-------|--------------|--------------|---------------|---------------|---------------|-----------------|--------------|----------------|

Same column requirements as Section B except:
- **Delay Estimate** (replaces Latency Impact): Expected execution delay range (e.g.,
  `~1 min standard tier`, `~5 min standard tier`, `near-real-time premium connector`,
  `scheduled — next run window`).

If ordering within async is non-deterministic, state that explicitly after the table.

Async total: ___ (count of rows in this section)

---

## SECTION D — RECONCILIATION, CASCADE CHAIN, AND RISK-RANKED PATHOLOGY

**D-1 — Denominator Resolution**

For every GD-ID from A-3, assign a final disposition. Zero unresolved GD-IDs required.

| GD-ID | Trigger Name | Final Disposition | Evidence |
|-------|--------------|-------------------|----------|

Disposition codes:
- `FIRED (Sync)` — in Section B
- `FIRED (Async)` — in Section C
- `FIRED (Cascade, parent: GD-XX)` — cascade-triggered row in Section B or C
- `CONFIRMED ABSENT` — specific reason (condition false, field not in change set, entity
  mismatch, scope exclusion)
- `FLAGGED MISSING` — expected to fire based on the scenario; absent from both sections

Summary: N FIRED, N CONFIRMED ABSENT, N FLAGGED MISSING
Unresolved GD-IDs: [list any, or "zero"]

**D-2 — Cascade Chain**

For any trigger in Section B or C whose Side Effects column is non-None, trace the full chain:

```
[Trigger A] (GD-XX, Sync) → writes {Entity}.{Field}
  → [Trigger B] (GD-YY, Async) → writes {Entity}.{Field}
    → [Trigger C] (GD-ZZ, Async) → [no further writes — terminates]
```

State `No cascading side effects` if no trigger in either section has a non-None Side Effects
value. For multi-level chains, show each level explicitly.

**D-3 — Pathology Verdicts**

All three classes must be addressed. Every verdict cites specific section evidence.

*Trigger Storm*
- Combined firing count from Section B + C: N (list all by name)
- Storm threshold from A-2: N
- Re-entry check: for each Side Effects value in either section, does that field appear as a
  trigger condition for any GD-ID candidate?
- Risk tier citation: [cite A-2 Storm Risk Tier that applies]
- **Verdict**: `CLEARED (count = N, below threshold, no re-entry)` or
  `STORM DETECTED (count = N, tier: S-N, risk: [level]; storm group: [flows]; re-entry: [path])`

*Missing Triggers*
- FLAGGED MISSING entries from D-1: [list or "none"]
- Automation category for each (classify against A-2 Missing Trigger Tiers)
- Risk tier citation: [cite A-2 tier for each gap]
- **Verdict**: `CLEARED (N GD-IDs: N FIRED, N CONFIRMED ABSENT, 0 FLAGGED MISSING)` or
  `MISSING TRIGGER: [name, tier: M-N, risk: [level], gap cause: [reason]]`

*Circular Triggers*
- All Side Effects field writes from both sections: [list as `{Trigger} writes {Entity}.{Field}`]
- Directed edge set: `{Trigger A → writes {E}.{F} → Trigger B fires on {E}.{F}}`
- Graph property: DAG / CYCLIC
- Risk tier citation (if CYCLIC): [cite A-2 Circular Trigger Tier that applies]
- **Verdict**: `CLEARED (DAG confirmed; edge set: {listed})` or
  `CIRCULAR TRIGGER (cycle: [path]; tier: X-N; risk: [level])`

**D-4 — Risk-Ranked Pathology Summary**

| Rank | Pathology Class | Instance | Risk Level | Taxonomy Tier | One-Line Mitigation |
|------|-----------------|----------|------------|---------------|---------------------|

Every row must cite the A-2 taxonomy tier that assigned the risk level.

If no pathologies: `No pathologies found — D-1 closed with zero FLAGGED MISSING; all three
pathology verdicts CLEARED against the pre-declared risk taxonomy.`

---

Scope constraint: Only enumerate triggers that fire for the specific field or event change
described. Triggers for other field changes on this entity are out of scope.

Now receive the scenario and produce the full four-section analysis.
