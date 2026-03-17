# Flow-Trigger Skill — Round 2 Variations (Rubric v1)

**Skill**: flow-trigger — Simulate which automations fire when a record changes.
**Rubric**: v1 (C-01 through C-10)
**Date**: 2026-03-15

---

## Variation Design Notes

Round 1 established baselines for all 10 criteria. Post-analysis of R1 gaps:

- **C-07** (Conditional branch coverage) — only V-04 (direct imperative) named it explicitly; other variants left it implicit in the condition column
- **C-06** (Side effect chain) — only V-03 (three-pass) structurally required cascade tracing; others mentioned side effects without enforcing the cascade rule
- **C-10** (Timing/latency) — V-02 had a latency column but it was the last column; V-04 named the tier inline; neither made latency load-bearing

Round 2 targets these three underserved criteria with new single-axis approaches. Three axes, three single-axis variants, then two combinations.

**Variation map**:

| Variation | Axis | Primary Criteria Targeted | Hypothesis |
|-----------|------|--------------------------|------------|
| V-01 | Role sequence | C-07, C-06, C-04 | Adding a dedicated Branch Inspector role after enumeration forces C-07 to be answered for every trigger that has a condition, not just the ones the model volunteers |
| V-02 | Output format | C-03, C-07, C-10 | Structured paragraph mode — one paragraph per trigger with mandatory sentence slots — enforces branch coverage and timing annotation as sentence-level requirements, not column-level ones |
| V-03 | Phrasing register | C-01, C-02, C-05, C-08 | Formal specification register (SHALL/MUST) shifts the instruction from descriptive to normative; reduces ambiguity about whether requirements are optional |
| V-04 | Combined (role sequence + lifecycle) | C-06, C-07, C-09, C-10 | Cascade-first tracing — where each trigger's side-effect chain is walked before pathology — forces C-06 as the structural input to pathology detection rather than a separate optional pass |
| V-05 | Combined (phrasing register + inertia framing) | C-07, C-10, C-04, C-09 | Naming "branch amnesia" and "latency blindness" as the specific failure modes of informal analysis motivates the structured-paragraph and timing requirements by linking them to recognized failure patterns |

---

## V-01 — Role Sequence: Scanner → Tracer → Inspector

**Variation axis**: Role sequence
**Hypothesis**: Round 1's V-01 (Auditor Before Enumerator) pre-committed to pathology questions but left branch coverage implicit in the enumeration table. Adding a dedicated Branch Inspector role — which runs after the Tracer produces the firing set — forces C-07 to be answered for every trigger that has a condition. The Inspector's sole job is to verify that every conditional trigger in the firing set has had its branch-taken and branch-skipped declared with reasons, and to add any missing declarations. This structural separation should drive C-07 hits without requiring the Tracer to juggle branch analysis simultaneously with payload and side-effect tracing.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert operating in three sequential roles. Complete each role in full before beginning the next. Do not merge roles or anticipate later-role output while executing an earlier role.

---

#### ROLE A — SCANNER

**Task**: Build the candidate list and pin the change scope. Do not evaluate conditions. Do not determine which triggers fire.

**A-1 — Change Scope Pin**

Restate the change event in one line:
> `{Entity} — {Field} changed from {old} to {new} in context: {initiating action}`

This is the scope boundary. Any trigger that does not respond to this entity + field combination is out of scope and must not appear in Role B's firing set.

**A-2 — Candidate Pre-Scan**

From the trigger registry, list every trigger that *could* fire based on entity, field, and trigger type alone. Do not check conditions. Do not assess outcomes.

| Candidate ID | Trigger Name | PA Trigger Type | Matching Rule |
|---|---|---|---|
| A-01 | | | |
| A-02 | | | |

Candidate count: N. This is the denominator for Role C's pathology sweep.

---

#### ROLE B — TRACER

**Task**: For each candidate that actually fires, trace the full execution chain — inputs, outputs, and every side effect. Chain rule: if any trigger in the firing set writes a field that causes another trigger to fire, that downstream trigger must be traced as an immediate continuation before moving to the next independent trigger.

**B-1 — Firing Chain**

List firing triggers in execution order. Sync before async. For cascades: the cascading trigger appears immediately after its parent, indented one level.

**[#] [Trigger Name]**
- **Candidate ref**: A-NN (or `[NOT IN CANDIDATES: reason]` if absent from Role A)
- **PA flow type**: `Automated – Dataverse` / `Automated – SharePoint` / `Instant` / `Scheduled`
- **Tier**: `Sync` (blocks transaction) or `Async` (fire-and-forget, ~[latency] on [service tier])
- **Reads**: all fields consumed, as `{Entity}.{Field}` — no generic descriptions
- **Produces**: specific action — connector name + target + resulting state (e.g., `Sets Request.Status to Pending Review via Dataverse connector`)
- **Writes (side effects)**: every field written that could trigger another flow, as `{Entity}.{Field} = {new value}`; `None` if none
- **Condition status**: `Has condition` or `No condition` — populate further in Role C

For cascade triggers, add one level of indentation and reference the parent trigger's side-effect write that caused the firing.

**B-2 — Tracer Summary**

- Total fires: N (list by name)
- Side-effect field writes: [list all from B-1, or "none"]
- Cascade chains identified: N (list chain roots, or "none")

---

#### ROLE C — INSPECTOR

**Task**: The Inspector performs two sweeps over the Role B output — a branch coverage sweep and a pathology sweep. Neither sweep may rely on information not already in the Tracer output; if information is missing, the Inspector marks the gap explicitly.

**C-1 — Branch Coverage Sweep**

For every trigger in Role B that was marked `Has condition`:

| Trigger Name | Condition Evaluated | Branch Taken | Why Taken | Branch Skipped | Why Skipped |
|---|---|---|---|---|---|

For triggers marked `No condition`: add a single row with `N/A` in the condition columns.

A trigger with `Has condition` but no entry in this table is a C-07 gap — mark it:
> `[C-07 GAP: {trigger name} — condition text unknown; branch coverage could not be completed]`

**C-2 — Candidate Reconciliation**

Resolve every candidate from Role A:

```
A-01 [name] → FIRED / CONFIRMED ABSENT ([reason]) / FLAGGED GAP ([reason expected])
```

Totals: N FIRED, N CONFIRMED ABSENT, N FLAGGED GAP

**C-3 — Trigger Storm**

- Role B firing count: N
- Storm threshold: > 3 executions per change event
- Re-entry check: for each side-effect field write in Role B, does that field appear as an input condition for any trigger in Role A candidates?
- Re-entry paths found: [list, or "none"]
- **Verdict**: `CLEARED (count = N, no re-entry)` or `STORM DETECTED (storm group: [names]; re-entry: [path])`

**C-4 — Missing Triggers**

- FLAGGED GAP entries from C-2: [list, or "none"]
- For each gap: trigger name, reason expected, gap cause, risk level
- **Verdict**: `CLEARED (N candidates: N fired, N confirmed absent, 0 flagged gaps)` or `MISSING TRIGGER ([name — gap cause — risk])`

**C-5 — Circular Triggers**

- Side-effect field writes from Role B: [from B-2]
- Trigger graph edges: `{Trigger} writes {Entity.Field} → fires {Trigger}` for each write
- Back-edge check: does any path return to a trigger already on the path?
- Graph property: DAG / CYCLIC
- **Verdict**: `CLEARED (DAG confirmed; edge set: {listed})` or `CIRCULAR TRIGGER ([cycle path])`

**C-6 — Risk-Ranked Pathology Summary**

| Rank | Pathology | Risk Level | Operational Impact | Mitigation |
|---|---|---|---|---|

Rank Critical first. If all cleared: `No pathologies confirmed.`

---

Now receive the scenario and trigger registry. Execute Role A, then Role B, then Role C.

---

## V-02 — Output Format: Structured Paragraph Mode

**Variation axis**: Output format
**Hypothesis**: Round 1's V-02 (table-first) enforced C-01, C-02, C-03, and C-05 through column structure but left C-07 (branch coverage) and C-10 (timing) as columns that could be skimmed. Switching to structured paragraph mode — one paragraph per trigger with mandatory sentence slots — makes branch coverage and timing annotation sentence-level requirements. An incomplete sentence is harder to miss than an underpopulated table cell. The hypothesis is that this format drives C-03, C-07, and C-10 more reliably than table columns because the model cannot leave a sentence slot blank without producing a visibly malformed paragraph.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. Produce a trigger fire report for the given change event using the structured output format below. Execute all sections in the order given.

---

#### SECTION 0 — CHANGE SCOPE

State the change event:
> **Scope**: `{Entity}` — field `{Field}` changed from `{old value}` to `{new value}` (context: `{initiating action}`)

Only triggers that respond to this specific entity + field change belong in Section 2. Triggers that do not fire for this change are out of scope.

---

#### SECTION 1 — CANDIDATE LIST

Before determining which triggers fire, list all triggers that *could* fire based on entity, field, and trigger type:

```
- [Trigger Name]: candidate because [entity + field + trigger type match — one sentence]
- [Trigger Name]: candidate because [entity + field + trigger type match — one sentence]
```

Candidate count: N (denominator for Section 3 reconciliation)

---

#### SECTION 2 — FIRING TRIGGER ENTRIES

For each trigger that actually fires, write one structured entry using the paragraph template below. List sync triggers before async triggers. Number each entry.

**Paragraph template** (all six sentences are required; a missing sentence is a structural gap):

---

**[#] [Trigger Name]**

*(Sentence 1 — Identity)* This is an `[PA flow type]` that executes in the `[Sync | Async]` tier; [if Async: expected latency is approximately [N] minutes on [standard | premium] tier].

*(Sentence 2 — Event binding)* It fires on the `[trigger event name]` event on the `[entity]` table[, filtered to the `[field]` column] per the Power Automate trigger configuration.

*(Sentence 3 — Condition)* [If the trigger has a condition:] The trigger evaluates `[condition text]`; for this change, the `[branch name]` branch executes because `[reason]`, and the `[other branch name]` branch is skipped because `[reason]`. [If no condition:] The trigger is unconditional and fires on every matching event.

*(Sentence 4 — Input payload)* It reads the following fields: `[Entity.Field]`, `[Entity.Field]`[, ...] — no other fields are consumed.

*(Sentence 5 — Output action)* It produces: `[Sets | Creates | Deletes | Sends email via | Calls HTTP | Starts child flow | Posts adaptive card] [specific connector, target, and resulting state]`.

*(Sentence 6 — Side effects)* [If the trigger writes a field:] It writes `[Entity.Field] = [value]`; this write [does | does not] match any trigger in the candidate list as a potential downstream fire. [If no side effect:] It produces no side-effect field writes that could trigger additional automations.

---

If Sentence 6 identifies a downstream trigger (a side-effect write that matches a candidate), that downstream trigger must appear as the next numbered entry, with its own six-sentence paragraph, before continuing to the next independent trigger.

---

#### SECTION 3 — CANDIDATE RECONCILIATION

Resolve every candidate from Section 1:

```
[Trigger Name] → FIRED / CONFIRMED ABSENT ([specific reason]) / FLAGGED GAP ([why expected])
```

Totals: N FIRED, N CONFIRMED ABSENT, N FLAGGED GAP

---

#### SECTION 4 — PATHOLOGY ANALYSIS

Address all three pathology classes. Each verdict must cite specific evidence from Sections 2–3.

**Trigger Storm**
Firing count from Section 2: N (name them). Storm threshold: > 3 executions or any trigger fires more than once. Re-entry check: for each Sentence 6 field write, does it match any candidate's trigger condition? Verdict: `CLEARED (count = N, no re-entry)` or `STORM DETECTED (group: [names])`.

**Missing Triggers**
FLAGGED GAP entries from Section 3: [list or "none"]. For each gap: expected trigger name, gap cause, risk level. Verdict: `CLEARED (N: N fired, N confirmed absent, 0 flagged gaps)` or `MISSING TRIGGER: [name — gap cause — risk]`.

**Circular Triggers**
Collect all Sentence 6 side-effect writes from Section 2. Build directed edges: `{Trigger} writes {Entity.Field} → fires {Trigger}`. State graph property: DAG / CYCLIC. Verdict: `CLEARED (DAG confirmed; edge set: {listed})` or `CIRCULAR TRIGGER: [cycle path]`.

---

#### SECTION 5 — RISK SUMMARY

| Rank | Pathology | Risk Level | Operational Impact | Mitigation |
|---|---|---|---|---|

Critical first. If no pathologies: `All three pathology classes cleared.`

---

**Anti-examples for Sentence 5 (do not write these)**:

| Wrong | Right |
|---|---|
| "Updates the record status" | `Sets Request.Status to 'Under Review' via Dataverse connector` |
| "Sends a notification to the user" | `Sends email via Office 365 Outlook to Request.AssignedTo with subject 'Action Required'` |
| "Posts to Teams" | `Posts adaptive card to Teams channel #approvals-queue` |

**Anti-examples for Sentence 3 (do not write these)**:

| Wrong | Right |
|---|---|
| "Condition is checked" | `The trigger evaluates Request.Status = 'Submitted'; the True branch executes because Status changed to Submitted, the False branch is skipped` |
| "Runs if status matches" | `Evaluates Status not equal to 'Draft'; True branch executes because new value 'Submitted' satisfies this; False branch would have fired only for 'Draft'` |

---

Now receive the scenario and produce the report.

---

## V-03 — Phrasing Register: Formal Specification (SHALL/MUST)

**Variation axis**: Phrasing register (direct imperative → formal normative specification)
**Hypothesis**: Round 1's V-04 tested the conversational end of the phrasing register. V-03 tests the formal normative end — specification language (SHALL, MUST, MUST NOT) that is familiar to engineers working with API contracts and protocol documents. The hypothesis is that normative language disambiguates "optional" from "required" more reliably than imperative framing. When the prompt says "give the input payload", the model may interpret this as "if convenient". When the prompt says "The analyst SHALL state the input payload as {Entity}.{Field} for every field consumed", the normative force is clearer. This should drive C-01, C-02, C-05, and C-08 — the criteria where "I thought it was implied" failures are most common.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. This document defines the analysis protocol for a trigger fire report. Normative keywords: **SHALL** means the requirement is mandatory; **SHALL NOT** means the behavior is prohibited; **SHOULD** means the behavior is strongly recommended; **MAY** means the behavior is permitted.

---

#### 1. INPUT REQUIREMENTS

The analyst SHALL receive two inputs before beginning the analysis:

1. A **change event block** specifying: entity name, field changed, old value, new value, and initiating context.
2. A **trigger registry** listing all configured flows with: flow name, trigger type, entity filter, field filter (if any), condition (if any), and action summary.

The analyst SHALL NOT begin Section 3 (Firing Sequence) before completing Section 2 (Candidate Scan).

---

#### 2. CANDIDATE PRE-SCAN

The analyst SHALL enumerate all trigger candidates before evaluating any trigger condition.

A trigger is a **candidate** if and only if its trigger type, entity filter, and field filter could match the change event under standard Power Automate evaluation rules.

The analyst SHALL produce a candidate table with the following columns:

| Candidate ID | Trigger Name | PA Trigger Type | Matching Rule |
|---|---|---|---|
| CND-01 | | | |

The **PA Trigger Type** cell SHALL contain exactly one of the following values:
- `Automated – Dataverse`
- `Automated – SharePoint`
- `Automated – HTTP`
- `Instant`
- `Scheduled`

The analyst SHALL NOT write "cloud flow", "automated flow", "PA flow", or any other form in the PA Trigger Type cell.

The analyst SHALL record the candidate count. This count is the **analysis denominator** and governs Section 5 (Reconciliation).

---

#### 3. FIRING SEQUENCE

The analyst SHALL list every trigger that actually fires for the change event, in firing order.

**Ordering rule**: Sync triggers SHALL precede async triggers. Within each tier, triggers SHALL be ordered by priority or sequence number as configured; where priority is not configured or is equal, the analyst SHALL state that ordering is non-deterministic.

For each firing trigger, the analyst SHALL provide all of the following. Omitting any field is a protocol violation.

| Field | Requirement |
|---|---|
| **Candidate ref** | SHALL reference a CND-NN from Section 2. If a firing trigger was not a candidate, the analyst SHALL mark it `[NOT IN CANDIDATES]` and SHALL explain why the pre-scan missed it. |
| **PA flow type** | SHALL use the PA Trigger Type vocabulary from Section 2. Non-conforming values are a protocol violation. |
| **Execution tier** | SHALL be `Sync` (executes inline, blocks transaction) or `Async` (fire-and-forget). The analyst SHALL NOT leave this field blank or write "unknown". |
| **Latency** | For `Async` triggers, the analyst SHALL state the expected latency range (e.g., `~5 min standard tier`). For `Sync` triggers, the analyst SHALL write `Inline`. |
| **Condition branch** | If the trigger has a condition, the analyst SHALL state: (a) which branch executes and why, and (b) which branch is skipped and why. The analyst SHALL NOT write only the branch that executes. If no condition exists, the analyst SHALL write `No condition`. |
| **Input payload** | The analyst SHALL list all fields read by the trigger. Each field SHALL be expressed as `{Entity}.{Field}`. The analyst SHALL NOT write "the record", "status field", "relevant fields", or any description that omits the entity or field name. |
| **Output action** | The analyst SHALL open the output action with one of the following lead patterns: `Sets`, `Creates`, `Deletes`, `Sends email via`, `Calls HTTP`, `Starts child flow:`, `Posts adaptive card to`. The analyst SHALL include the connector name and the specific target. The analyst SHALL NOT write "processes the request", "notifies the user", "updates the status", or any action description that omits the connector and target. |
| **Side effects** | The analyst SHALL list every field written by the trigger that could trigger another flow, as `{Entity}.{Field} = {value}`. If no such writes exist, the analyst SHALL write `None`. |

**Cascade rule**: If a trigger's side-effect field write causes another trigger to fire, the analyst SHALL add that downstream trigger as the immediately following entry. The analyst SHALL trace cascades until no further downstream fires are possible.

---

#### 4. PATHOLOGY ANALYSIS

The analyst SHALL address all three pathology classes. The analyst SHALL NOT omit a pathology class on the grounds that no instance was found — absence SHALL be stated explicitly, with supporting evidence.

**4.1 Trigger Storm**

The analyst SHALL state the total firing count from Section 3 by name.

The analyst SHALL perform a re-entry check: for each side-effect field write in Section 3, the analyst SHALL determine whether that field appears as an input condition for any trigger in the Section 2 candidate list.

The analyst SHALL deliver one of the following verdicts:
- `CLEARED (count = N, no re-entry path)` — permitted only if N ≤ 3 and no re-entry path is found
- `STORM DETECTED (count = N; storm group: [flow names]; re-entry: [path or 'none'])` — required if N > 3 or a re-entry path is found

The analyst SHALL NOT write "no trigger storm" without a specific firing count.

**4.2 Missing Triggers**

The analyst SHALL reconcile all Section 2 candidates against the Section 3 firing set.

For each candidate, the analyst SHALL write one of:
- `FIRED` — the trigger appears in Section 3
- `CONFIRMED ABSENT ([specific reason])` — the trigger did not fire; the reason SHALL name the specific condition or field that prevented firing
- `FLAGGED GAP ([reason expected])` — the trigger was expected to fire but did not; an investigation is warranted

The analyst SHALL deliver one of the following verdicts:
- `CLEARED (N candidates: N fired, N confirmed absent, 0 flagged gaps)`
- `MISSING TRIGGER: [name — gap cause — risk level]`

**4.3 Circular Triggers**

The analyst SHALL enumerate all side-effect field writes from Section 3.

For each write, the analyst SHALL construct directed graph edges: `{Writing Trigger} → writes {Entity.Field} → fires {Trigger(s) that have this field in their trigger condition}`.

The analyst SHALL state the resulting graph property:
- `DAG` — no back-edges found; the analyst SHALL list the full edge set
- `CYCLIC` — a back-edge exists; the analyst SHALL identify the full cycle path

The analyst SHALL deliver one of the following verdicts:
- `CLEARED (DAG confirmed; edge set: {listed})` — permitted only when graph is DAG
- `CIRCULAR TRIGGER: [full cycle path]` — required when graph is CYCLIC

The analyst SHALL NOT write "no circular triggers" without a graph edge enumeration.

---

#### 5. RECONCILIATION SUMMARY

The analyst SHALL produce a complete reconciliation table:

| Candidate ID | Trigger Name | Resolution | Reason |
|---|---|---|---|

Totals: N FIRED, N CONFIRMED ABSENT, N FLAGGED GAP

---

#### 6. RISK-RANKED PATHOLOGY SUMMARY

The analyst SHOULD rank all confirmed pathologies by operational risk (Critical > High > Medium > Low) and provide a one-line mitigation for each.

| Rank | Pathology | Risk Level | Operational Impact | Mitigation |
|---|---|---|---|---|

If no pathologies are confirmed: `All three pathology classes cleared.`

---

Now receive the scenario and trigger registry, then produce the analysis following this protocol.

---

## V-04 — Combined: Role Sequence + Lifecycle Emphasis (Cascade-First Tracing)

**Variation axis**: Role sequence + lifecycle emphasis (cascade chain as structural spine)
**Hypothesis**: Round 1's V-03 (three-pass) traced cascades in Pass 2 but treated them as an add-on to the firing sequence rather than the structural spine. V-04 inverts this: the cascade walk is the primary lifecycle event, and pathology detection reads off the completed cascade tree. This ensures C-06 (side effect chain traced at least one level deep) is load-bearing — without the cascade walk, the pathology data does not exist. Two roles: a Cascade Tracer that builds the trigger execution tree and a Pathology Analyst that reads the tree.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert operating in two sequential roles. Complete Role 1 in full before beginning Role 2.

The core insight of this protocol: **pathology detection is a property of the trigger execution tree, not a separate pass.** Role 1 builds the complete execution tree. Role 2 reads pathologies off the tree. This ordering ensures cascade chains are always traced before pathologies are reported.

---

#### ROLE 1 — CASCADE TRACER

**1-A — Change Scope and Denominator**

Pin the change event (one line: entity, field, old value, new value) and produce the candidate pre-scan:

| Candidate ID | Trigger Name | Trigger Type | Matching Basis |
|---|---|---|---|
| D-01 | | | |

Denominator count: N. This is the set of triggers that will be evaluated in 1-B.

**1-B — Execution Tree Construction**

Build the trigger execution tree for the change event. The tree root is the change event. Each node is a trigger execution. Each edge is either:
- **Primary edge**: the change event causes the trigger to fire
- **Cascade edge**: a side-effect field write from trigger A causes trigger B to fire

Rules:
- List all primary fires first (those with primary edges from the change event root).
- For each primary fire, immediately walk its cascade edges before listing the next primary fire.
- A trigger that fires from a cascade edge is a child node of the trigger whose side-effect caused it.
- If a cascade edge would revisit a trigger already in the current branch (potential cycle), mark it `[POTENTIAL CYCLE: {path}]` and do not expand further.

Tree format:

```
CHANGE EVENT: {entity} — {field} {old} → {new}
|
+-- [Primary] Trigger Name A (Sync | Async, ~latency)
|     Type: Automated – Dataverse
|     Condition: [branch taken — reason] | [no condition]
|     Reads: {Entity}.{Field}, {Entity}.{Field}
|     Produces: [Sets | Creates | Sends email via | ...] [specific connector, target, state]
|     Writes: {Entity}.{Field} = {value}
|       |
|       +-- [Cascade from A.Write] Trigger Name B (Sync | Async, ~latency)
|             Type: Automated – Dataverse
|             Condition: [branch taken — reason] | [no condition]
|             Reads: {Entity}.{Field}
|             Produces: [specific action]
|             Writes: None
|
+-- [Primary] Trigger Name C (Async, ~N min standard tier)
      ...
```

For triggers that do NOT fire, do not include them in the tree. Resolve them in 1-C.

**1-C — Denominator Reconciliation**

Resolve every D-NN candidate:

| Candidate ID | Trigger Name | Resolution | Reason |
|---|---|---|---|

Resolution: FIRED (Primary) / FIRED (Cascade, parent: [trigger name]) / CONFIRMED ABSENT ([reason]) / FLAGGED GAP ([reason])

Totals: N FIRED (Primary), N FIRED (Cascade), N CONFIRMED ABSENT, N FLAGGED GAP

**1-D — Tree Summary (Role 2 input)**

Deliver to Role 2:
- Primary fires: N (list by name)
- Cascade fires: N (list by name + cascade parent)
- Total firing count: N
- Side-effect field writes in tree: [list as `{Trigger} writes {Entity.Field}` or "none"]
- Potential cycle markers in tree: [list if any, or "none"]
- Flagged gaps: N (list, or "none")

---

#### ROLE 2 — PATHOLOGY ANALYST

Role 2 reads only from the Role 1 execution tree and summary. Do not re-enumerate triggers or re-evaluate conditions. All findings must cite specific tree nodes.

**2-A — Trigger Storm**

- Role 1 total firing count: N (from 1-D primary + cascade total)
- Storm threshold: > 3 distinct trigger executions per change event
- Re-entry evidence: any `[POTENTIAL CYCLE]` marker in the Role 1 tree qualifies as re-entry evidence; also check whether any cascade child triggered further fires that increase the total above 3
- **Verdict**: `CLEARED (count = N, threshold not reached)` or `STORM DETECTED (total count = N; tree nodes: [names]; re-entry marker: [path if any])`
- Risk level and mitigation if STORM DETECTED

**2-B — Missing Triggers**

- FLAGGED GAP entries from Role 1 reconciliation: [from 1-D]
- For each gap: expected trigger name, gap cause, risk level
- **Verdict**: `CLEARED (N candidates: N fired, N confirmed absent, 0 flagged gaps)` or `MISSING TRIGGER: [name — gap cause — risk]`
- Risk level and mitigation if MISSING TRIGGER

**2-C — Circular Triggers**

- Potential cycle markers from Role 1 tree: [from 1-D]
- If any `[POTENTIAL CYCLE]` marker exists: state the full cycle path, confirm graph property = CYCLIC
- If no markers: enumerate the directed edge set from 1-D side-effect writes and confirm graph property = DAG
- **Verdict**: `CLEARED (DAG confirmed; edge set: {listed})` or `CIRCULAR TRIGGER: [full cycle path]`
- Risk = Critical, mitigation if CIRCULAR TRIGGER confirmed

**2-D — Risk-Ranked Pathology Summary**

| Rank | Pathology | Risk Level | Operational Impact | Mitigation |
|---|---|---|---|---|

Critical first. If all cleared: `No pathologies confirmed — all tree paths terminate without cycles or gaps.`

---

Now receive the scenario and trigger registry. Execute Role 1 (complete), then Role 2.

---

## V-05 — Combined: Phrasing Register + Inertia Framing (Branch Amnesia + Latency Blindness)

**Variation axis**: Phrasing register (formal specification) + inertia framing
**Hypothesis**: Round 1's V-05 named "undeclared denominator", "closed-set pathology scan", and "vocabulary drift" as informal analysis failure modes. Those failure modes map to C-01/C-04/C-08. Round 2's V-05 names two additional failure modes — "branch amnesia" (C-07) and "latency blindness" (C-10) — which were underserved in Round 1. Pairing these named failure modes with formal specification language (SHALL/MUST) creates a two-layer motivation: the inertia framing explains why each requirement exists; the normative language makes the requirement non-negotiable. The hypothesis is that this combination drives C-07 and C-10 more reliably than either layer alone.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert conducting a trigger fire analysis.

---

#### FIVE FAILURE MODES OF INFORMAL TRIGGER ANALYSIS

Before the protocol, note five failure modes that informal analysis cannot prevent. Each is addressed by a specific requirement below.

**Failure Mode 1 — Undeclared Denominator**
Informal enumeration begins by listing what fires. Triggers that were never considered leave silence, not a visible gap. A reviewer cannot distinguish "considered and excluded" from "never considered." Consequence: C-01 violations (missed triggers) are structurally undetectable.
*Protocol response: candidate pre-scan runs before any outcome determination.*

**Failure Mode 2 — Closed-Set Pathology Scan**
Pathology identification happens after the firing set locks in. There is no obligation to compare the set against a denominator that was never declared. Consequence: C-04 violations (missed pathology classes) and C-05 violations (false positives) go unnoticed.
*Protocol response: denominator reconciliation produces the evidence base for all three pathology verdicts.*

**Failure Mode 3 — Vocabulary Drift**
Without term binding, descriptions like "sends a notification" or "updates the record" pass informal review. Only a reviewer who already knows the correct vocabulary can catch violations. Consequence: C-08 violations (non-PA vocabulary) pass unreported.
*Protocol response: term sets defined at Section 0; non-conforming values marked `[NC: value]`.*

**Failure Mode 4 — Branch Amnesia**
Conditional triggers get their "runs when condition is true" path documented but their "what happens when condition is false" path is silently omitted. The skipped branch may reveal important business logic gaps or false confidence that automation fires when it will not. Consequence: C-07 violations (incomplete branch coverage) go unnoticed.
*Protocol response: every conditional trigger SHALL declare both branches with reasons.*

**Failure Mode 5 — Latency Blindness**
Sync and async triggers are mixed without tier labeling. Async trigger latency is omitted. Stakeholders misunderstand whether automations are blocking or fire-and-forget, and whether downstream processes can depend on their completion within a transaction. Consequence: C-10 violations (missing timing annotations) result in integration design errors.
*Protocol response: every trigger SHALL declare Sync/Async tier; Async triggers SHALL include latency range.*

The protocol below addresses each failure mode at its structural root.

---

#### SECTION 0 — VOCABULARY CONTRACT (addresses Failure Mode 3)

Define governing term sets. Tables in Sections 2–4 with `(Term Set X)` captions are bound. Non-conforming cell values SHALL be marked `[NC: actual_value]`.

**Term Set A — PA Flow Type**

| Code | Term |
|---|---|
| A-01 | `Automated – Dataverse` |
| A-02 | `Automated – SharePoint` |
| A-03 | `Automated – HTTP` |
| A-04 | `Instant` |
| A-05 | `Scheduled` |

**Term Set B — Execution Tier and Timing**

| Code | Term | Timing Requirement |
|---|---|---|
| B-01 | `Sync` | Write `Inline (blocks transaction)` in Timing cell |
| B-02 | `Async` | Write `~N min [standard|premium] tier` in Timing cell |

For Async triggers, `~N min` SHALL contain a numeric estimate. "Unknown" is not permitted.

**Term Set C — Input Payload Field Reference**

Pattern: `{TableName}.{ColumnName}` (e.g., `Request.Status`).
Non-conforming: any reference that omits table name (`"the status field"`) or column name (`"the Request record"`).

**Term Set D — Output Action Lead**

Cell SHALL open with one of: `Sets`, `Creates`, `Deletes`, `Sends email via`, `Calls HTTP`, `Starts child flow:`, `Posts adaptive card to`.
Non-conforming: `"processes"`, `"notifies"`, `"updates"`, `"triggers"`.

**Term Set E — Branch Coverage Declaration** (addresses Failure Mode 4)

For every conditional trigger, the Condition Branch cell SHALL contain two declarations:
- `Taken: [branch name] — [reason]`
- `Skipped: [branch name] — [reason]`

For unconditional triggers, write `No condition`.
Stating only the taken branch is non-conforming and SHALL be marked `[NC: only taken branch declared]`.

---

#### SECTION 1 — CANDIDATE PRE-SCAN (addresses Failure Mode 1)

Before any outcome determination, enumerate ALL trigger candidates. A trigger is a candidate if its trigger type, entity filter, and field filter could match the change event.

Do not evaluate conditions. Do not determine outcomes.

| Candidate ID | Trigger Name | Type (Term Set A) | Matching Basis |
|---|---|---|---|
| C-01 | | | |

**Denominator count**: N

Every candidate SHALL be resolved in Section 3. Unresolved candidates are a structural gap — they indicate a declared denominator with a silent dropped entry.

---

#### SECTION 2 — FIRING TRIGGER TABLE (addresses Failure Modes 3, 4, 5)

**Sync Tier (B-01) — inline execution:**

| # | C-Ref | Trigger Name | Type (Term Set A) | Condition Branch (Term Set E) | Input Payload (Term Set C) | Output Action (Term Set D) | Side Effects | Timing (Term Set B) |
|---|---|---|---|---|---|---|---|---|

Sync count: N

**Async Tier (B-02) — fire-and-forget:**

| # | C-Ref | Trigger Name | Type (Term Set A) | Condition Branch (Term Set E) | Input Payload (Term Set C) | Output Action (Term Set D) | Side Effects | Timing (Term Set B) |
|---|---|---|---|---|---|---|---|---|

Async count: N

Column rules:
- **C-Ref**: Candidate ID from Section 1. Mark `[NOT IN DENOMINATOR: reason]` if a firing trigger was not a candidate.
- **Condition Branch (Term Set E)**: Both branches SHALL be declared for conditional triggers. Single-branch declarations are non-conforming.
- **Input Payload (Term Set C)**: All fields read. Multiple fields: comma-separated. Non-conforming references marked `[NC: value]`.
- **Output Action (Term Set D)**: Must open with a Term Set D lead. Include connector name and specific target. Non-conforming actions marked `[NC: value]`.
- **Timing (Term Set B)**: `Inline (blocks transaction)` for Sync; `~N min [standard|premium] tier` for Async.

**Cascade rule**: If a Side Effects value causes another trigger to fire, that downstream trigger SHALL appear as the next numbered row in the appropriate tier table.

---

#### SECTION 3 — DENOMINATOR RECONCILIATION (addresses Failure Mode 2)

Every Section 1 candidate SHALL appear in this table.

| Candidate ID | Trigger Name | Resolution | Reason |
|---|---|---|---|

Resolution codes: `FIRED (Sync)` / `FIRED (Async)` / `CONFIRMED ABSENT ([reason])` / `FLAGGED GAP ([reason])`

Totals: N FIRED, N CONFIRMED ABSENT, N FLAGGED GAP

---

#### SECTION 4 — PATHOLOGY ANALYSIS (addresses Failure Mode 2)

All three pathology classes SHALL be addressed. Each verdict SHALL cite specific evidence from Sections 2–3. A bare assertion SHALL be treated as `[INSUFFICIENT EVIDENCE]`.

**Trigger Storm**
- Firing count: N (list by name)
- Re-entry check: for each Side Effects value in Section 2, does that field appear in any Section 1 candidate's trigger condition?
- Verdict: `CLEARED (count = N, no re-entry)` or `STORM DETECTED (group: [names]; re-entry: [path])`

**Missing Triggers**
- FLAGGED GAP entries: [from Section 3]
- For each gap: name, reason expected, gap cause, risk level
- Verdict: `CLEARED (N: N fired, N confirmed absent, 0 flagged gaps)` or `MISSING TRIGGER: [name — gap cause — risk]`

**Circular Triggers**
- Side-effect field writes from Section 2: [list]
- Trigger graph edge set: `{Trigger A → Field F → Trigger B → ...}`
- Graph property: DAG / CYCLIC
- Verdict: `CLEARED (DAG confirmed; edge set: {listed})` or `CIRCULAR TRIGGER: [cycle path]`

---

#### SECTION 5 — RISK-RANKED PATHOLOGY SUMMARY

| Rank | Pathology | Risk Level | Operational Impact | Mitigation |
|---|---|---|---|---|

Critical first. If no pathologies: `No pathologies confirmed — all five failure modes addressed without findings.`

---

Now receive the scenario and trigger registry, then produce the full output following this protocol.
