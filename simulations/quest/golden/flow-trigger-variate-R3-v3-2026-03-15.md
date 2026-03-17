# Flow-Trigger Skill — Round 3 Variations (Rubric v3)

**Skill**: flow-trigger — Simulate which automations fire when a record changes.
**Rubric**: v3 (C-01 through C-19)
**Date**: 2026-03-15

---

## Variation Design Notes

### Pre-read of R2 Scorecard Evidence (Against Rubric v2, C-01 Through C-14)

| Variation | Score | Missed Criteria | Key Mechanism |
|-----------|-------|-----------------|---------------|
| V-01 | 98.3 | C-12 | Vocabulary contract + [VOCAB FAIL] markers. Evidence guidance but no [INSUFFICIENT] gate. |
| V-02 | 98.3 | C-12 | Cascade-to-termination loop engine. Verdict format strings embed citations but no [INSUFFICIENT] protocol. |
| V-03 | 100 | none | Three-role pipeline where Role C can only approve/flag — structural separation prevents self-validation. |
| V-04 | 100 | none | Sync/async split tables + explicit [INSUFFICIENT] marker with phase+item citation requirement. |
| V-05 | 100 | none | Nine failure mode catalog (FM-01–FM-09) + SHALL language + structural table split. |

### What Rubric v3 Adds (C-15 Through C-19)

| ID | Criterion | Pattern Source in R2 | R3 Design Obligation |
|----|-----------|---------------------|----------------------|
| C-15 | Candidate denominator declaration | All R2 variations had a pre-scan; v3 formalizes the count as a structural mechanism | Declared count must be pre-condition evaluation — conditions evaluated during the scan reduce the denominator below the true candidate population |
| C-16 | Per-chain terminal row marker | R2 V-01/V-03 used `[TERMINAL]` at row level | Each cascade chain closes with `[TERMINAL]` at row level — distinct from C-13 (termination condition instruction) |
| C-17 | Role-separated evidence gating | R2 V-03's Role C could only approve/flag, not write | Structural separation: the gating role cannot generate analysis, only emit `[EVIDENCE: CONFIRMED]` or `[INSUFFICIENT: ...]` |
| C-18 | Sync/async structural table split | R2 V-04's separate firing tables | Separate tables, not a single table with a Tier column — tier is table membership |
| C-19 | Back-edge detection in trigger graph | R2 V-04's explicit detection step | Algorithmic DFS with `in-path` set — not visual inspection of the edge set |

### R3 Variation Map

All five R2 100-scorers achieved C-01–C-14. The R3 challenge is adding C-15–C-19 without regressing those. Three single-axis variations explore the new criteria independently; two combinations integrate them.

| Variation | Axes | New Criteria Targeted | Hypothesis |
|-----------|------|-----------------------|------------|
| V-01 | Role sequence | C-15, C-16, C-19, C-17 | A four-role pipeline distributes the new criteria across dedicated structural roles: Scanner owns the denominator (C-15), Cascade Closer owns chain termination + [TERMINAL] markers (C-16) + DFS detection (C-19), Gatekeeper owns structural evidence separation (C-17) |
| V-02 | Output format | C-15, C-16, C-18, C-19 | Dual-tree format — one tree per execution tier (C-18) — makes [TERMINAL] leaves visible per chain (C-16), denominator declared before tree construction (C-15), and DFS back-edge detection applied to the unified edge set (C-19) |
| V-03 | Phrasing register | C-15, C-16, C-17, C-18, C-19 | Extending the failure-mode catalog to FM-10 through FM-14 (addressing all five new criteria) and pairing each with SHALL language creates structural obligations grounded in named failure consequences |
| V-04 | Output format + lifecycle emphasis | C-15, C-16, C-17, C-18, C-19 | Sync/async structural split (C-18) as primary document spine, with lifecycle ordering — denominator before cascades, termination before pathology — pulling all five new criteria into the structural flow |
| V-05 | Phrasing register + inertia framing | C-15, C-16, C-17, C-18, C-19 | Reframing all five new criteria as "structural guarantees" — properties that informal analysis cannot provide — paired with SHALL language makes each criterion a protocol obligation rather than a quality target |

**Foundation carried forward** (no rediscovery needed from R2):
- Vocabulary contract + `[NC: value]` markers (C-11)
- `[INSUFFICIENT]` or `[EVIDENCE: CONFIRMED]` for verdict gates (C-12)
- Cascade termination condition instruction (C-13)
- Directed edge set for circular detection (C-14)

---

## V-01 — Role Sequence: Four-Role Pipeline (Scanner → Tracer → Cascade Closer → Gatekeeper)

**Variation axis**: Role sequence
**Hypothesis**: R2's best role-sequence variation (V-03) used three roles: Scanner/Tracer/Gatekeeper. The Tracer owned cascade tracing AND chain termination simultaneously, which worked for C-13 but left C-16 (per-chain `[TERMINAL]` markers) as an implicit consequence rather than a structural requirement. V-01 adds a dedicated Cascade Closer role between the Tracer and the Gatekeeper. The Closer's sole job is to walk each chain to termination, mark the terminal row of each chain, build the directed edge set, and apply the DFS back-edge detection algorithm. This gives C-16 and C-19 their own structural home — neither can be skipped without the Closer producing visibly incomplete output. The denominator declaration (C-15) is the Scanner's primary deliverable. The Gatekeeper (C-17) is preserved from R2 V-03 unchanged: it cannot write analysis, only approve or flag.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert operating in four sequential roles. Complete each role in full before beginning the next. Do not merge roles. Do not carry work from a later role into an earlier one.

---

#### ROLE A — SCANNER

**Task**: Establish the analysis boundary and declare the candidate denominator. Do not evaluate conditions. Do not determine which triggers fire.

**A-0 — Change Scope Pin**

Restate the change event in one line:

> `{Entity} — {Field} changed from {old value} to {new value} | context: {initiating action}`

This scope line is the analysis boundary. Any trigger whose trigger type, entity filter, or field filter does not match this entity + field is out of scope for Role B.

**A-1 — Candidate Pre-Scan**

From the trigger registry, list every trigger that *could* fire based on entity, field, and trigger type alone. Do not check conditions. Do not assess outcomes. A trigger with a condition is still a candidate — condition evaluation happens in Role B.

| Candidate ID | Trigger Name | PA Trigger Type | Matching Basis |
|---|---|---|---|
| A-01 | | | |
| A-02 | | | |

Permitted values for **PA Trigger Type**: `Automated – Dataverse` | `Automated – SharePoint` | `Automated – HTTP` | `Instant` | `Scheduled`. Non-conforming values are marked `[NC: actual_value]`.

**Denominator Count: N** — This is the pre-condition population. Conditions have not been evaluated. This count governs Role C's reconciliation and Role D's verdict gate audit. If Role C reports fewer resolutions than this count, the discrepancy is a structural gap.

---

#### ROLE B — TRACER

**Task**: For each candidate that actually fires, produce the complete execution record — inputs, outputs, tier, timing, side-effect writes, and cascade chain identifier. Do not walk cascade chains here; assign a Chain ID to any trigger that writes a side-effect field that matches a candidate, then move on. Role C owns cascade chain traversal and termination.

**B-1 — Vocabulary Contract**

All Role B column cells are bound to the following terms. Non-conforming values are marked `[NC: actual_value]`.

| Column | Permitted Values | Non-Conforming Examples |
|---|---|---|
| **PA Flow Type** | `Automated – Dataverse`, `Automated – SharePoint`, `Automated – HTTP`, `Instant`, `Scheduled` | `cloud flow`, `automated flow`, `PA flow` |
| **Tier** | `Sync`, `Async` | blank, `"unknown"` |
| **Latency** | Sync → `Inline (blocks transaction)` \| Async → `~N min [standard\|premium] tier` (numeric N required) | `"varies"`, `"unknown"`, blank for Async |
| **Condition Branch** | `Taken: [branch name] — [reason]` AND `Skipped: [branch name] — [reason]` (both required for conditional triggers) \| `No condition` for unconditional | Stating only the taken branch → `[NC: only taken branch declared]` |
| **Input Payload** | `{Entity}.{Field}` pattern, comma-separated | `"the record"`, `"status field"`, `"relevant fields"` |
| **Output Action** | Opens with: `Sets` \| `Creates` \| `Deletes` \| `Sends email via` \| `Calls HTTP` \| `Starts child flow:` \| `Posts adaptive card to` — followed by connector name and specific target | `"processes"`, `"notifies"`, `"updates"`, `"triggers"` |
| **Side-Effect Writes** | `{Entity}.{Field} = {value}` for each write that could trigger another flow. `None` if no such writes. | Generic descriptions omitting entity or field |

**B-2 — Firing Execution Table**

List firing triggers in execution order. Sync before Async. Within each tier, list in priority/sequence order; note `[NON-DETERMINISTIC: reason]` if order cannot be determined.

| Seq # | Trigger Name | Candidate Ref | PA Flow Type | Tier | Latency | Condition Branch | Input Payload | Output Action | Side-Effect Writes | Chain ID |
|---|---|---|---|---|---|---|---|---|---|---|

Column notes:
- **Candidate Ref**: A-NN from Role A. If a firing trigger was not in the candidate pre-scan, write `[NOT IN DENOMINATOR: reason]`.
- **Chain ID**: If this trigger's Side-Effect Writes field matches any candidate in Role A: assign CH-01, CH-02, etc. Role C will walk this chain. If no side-effect write matches a candidate, write `—`.

**B-3 — Tracer Summary (Role C handoff)**

- Total Sync fires: N (list by name)
- Total Async fires: N (list by name)
- Grand total fires: N
- Side-effect field writes: [list as `{Trigger} writes {Entity.Field} = {value}`, or "none"]
- Chain IDs assigned: N (list: CH-NN → root trigger name → cascade field)
- `[NOT IN DENOMINATOR]` triggers: [list, or "none"]

---

#### ROLE C — CASCADE CLOSER

**Task**: For each Chain ID assigned in Role B, walk the cascade chain to termination. Mark the terminal row of each chain with `[TERMINAL]`. Build the complete directed edge set from Role B's side-effect writes and the chain walks. Apply DFS back-edge detection to the edge set. Do not add new triggers to the firing set; if a cascade trigger was not in Role B, flag it as a gap.

**C-1 — Cascade Chain Walk**

For each CH-NN chain, produce the following sub-table:

---

**Chain CH-NN** | Root: `{trigger name}` | Cascade Field: `{Entity.Field}`

| Step | Trigger Name | Fires Because | Reads | Produces | Writes | Terminal? |
|---|---|---|---|---|---|---|

Column rules:
- **Fires Because**: cite the upstream write: `{Upstream Trigger} wrote {Entity.Field} = {value}`.
- **Writes**: any side-effect write that extends the chain. If none, write `None`.
- **Terminal?**: The final row of each chain — the row where **Writes** = `None` OR where no candidate in Role A responds to the written field — MUST contain `[TERMINAL]`. Any other row writes `—`.

If a chain has no `[TERMINAL]` row: mark `[CHAIN OPEN: CH-NN — no terminal row produced; trace may be incomplete]`.

**Termination condition**: A chain terminates when the current step writes a field that does not match any Role A candidate's trigger condition, or writes `None`. A fixed step depth is not a valid stopping rule.

**C-2 — Directed Edge Set**

From Role B's Side-Effect Writes and Role C's chain steps, build the complete directed edge set:

```
{Trigger A} → writes {Entity.Field} → fires {Trigger B}
{Trigger B} → writes {Entity.Field} → fires {Trigger C}
{Trigger D} → writes {Entity.Field} → [NO DOWNSTREAM]
```

Every side-effect write from Role B must appear in the edge set — as a directed edge or as `[NO DOWNSTREAM]`.

**C-3 — DFS Back-Edge Detection**

Apply the following algorithmic detection procedure to the edge set from C-2. Do not replace this step with visual inspection.

```
Initialize: visited = {}  |  in-path = {}
For each trigger T in the edge set not yet in visited:
  1. Add T to in-path
  2. For each downstream trigger U that T fires:
     a. If U is in in-path: back-edge found → mark [BACK-EDGE: {T → ... → U → T}]
     b. Else if U is not in visited: recurse (apply procedure to U)
  3. Remove T from in-path; add T to visited
After all nodes processed: state graph property
```

State result:
- `Graph property: DAG` — no back-edges found during traversal; confirm edge set listed in C-2
- `Graph property: CYCLIC` — one or more `[BACK-EDGE]` markers found; list each cycle path

Do not write `DAG` or `CYCLIC` without completing the procedure above.

**C-4 — Role C Summary (Role D handoff)**

- Chains walked: N
- Chains with `[TERMINAL]` rows: N
- `[CHAIN OPEN]` gaps: N (list, or "none")
- Full edge set: [from C-2]
- Graph property: DAG | CYCLIC
- `[BACK-EDGE]` paths: [list, or "none"]
- `[NOT IN DENOMINATOR]` triggers from B-3: [list, or "none"]

---

#### ROLE D — GATEKEEPER

Role D **cannot generate new analysis**. It can only audit Role B and C output and emit one of two verdicts per check:
- `[EVIDENCE: CONFIRMED — {specific citation}]` — the finding is directly supported by a named Role B row or Role C step
- `[INSUFFICIENT: {state exactly what evidence is needed and where it should appear}]` — the finding lacks a traceable evidence chain

Role D cannot rewrite Role B or C content. If a finding is insufficient, Role D marks it and moves on. A single role that both writes and gates its own assertions is a structural violation — Role D's physical separation from Role B and C is the enforcement mechanism.

**D-1 — Candidate Reconciliation**

Resolve every Role A candidate:

| Candidate ID | Trigger Name | Resolution | Role D Evidence Gate |
|---|---|---|---|

Resolution codes: `FIRED (Seq #N in B-2)` | `CONFIRMED ABSENT ([specific condition or filter that prevented firing])` | `FLAGGED GAP ([reason expected to fire])`

For each `FLAGGED GAP`:
> `[INSUFFICIENT: expected trigger {name} not found in Role B firing set — gap cause and risk level required before pathology verdict can be issued]`

Totals: N FIRED, N CONFIRMED ABSENT, N FLAGGED GAP

**D-2 — Trigger Storm Gate**

- Firing count from B-3: N (list by name)
- Storm threshold: > 3 total executions per change event, or any `[BACK-EDGE]` found
- Back-edge evidence: from C-4

Role D emits:
- If count ≤ 3 and no `[BACK-EDGE]`: `[EVIDENCE: CONFIRMED — CLEARED; firing count = N per B-3; DAG per C-3 traversal]`
- If count > 3 or `[BACK-EDGE]` exists: `[STORM DETECTED — count = N; re-entry path: {C-4 path or "none"}]`
- If B-3 grand total was not stated: `[INSUFFICIENT: Role B did not produce a grand total firing count in B-3; count is required before storm verdict]`

**D-3 — Missing Triggers Gate**

- `FLAGGED GAP` entries from D-1: [list or "none"]
- For each gap: trigger name, gap cause, risk level

Role D emits:
- If 0 gaps: `[EVIDENCE: CONFIRMED — CLEARED; N candidates: N fired, N confirmed absent, 0 flagged gaps, per D-1 reconciliation table]`
- If gaps exist: `[MISSING TRIGGER: {name} — {gap cause} — {risk level}]`
- For any verdict not traceable to a D-1 row: `[INSUFFICIENT: verdict not traceable to reconciliation table; D-1 entry required]`

**D-4 — Circular Triggers Gate**

- Graph property from C-4: DAG | CYCLIC
- Evidence: C-2 edge set + C-3 DFS traversal

Role D emits:
- If DAG: `[EVIDENCE: CONFIRMED — CLEARED; DAG per C-3 DFS traversal; edge set: {from C-2}]`
- If CYCLIC: `[CIRCULAR TRIGGER: {cycle path from C-3}; Risk = Critical]`
- If C-3 DFS step was not completed: `[INSUFFICIENT: Role C did not complete the DFS back-edge detection procedure; graph property cannot be stated from edge set inspection alone — C-3 traversal steps must be shown]`

**D-5 — Risk-Ranked Pathology Summary**

Using only evidence-confirmed findings from D-2, D-3, D-4:

| Rank | Pathology | Risk Level | Operational Impact | Mitigation |
|---|---|---|---|---|

Critical first. If all confirmed clear: `No pathologies confirmed — all three classes gated by Role D with evidence citations.`

---

Now receive the scenario and trigger registry. Execute Role A in full, then Role B in full, then Role C in full, then Role D in full.

---

## V-02 — Output Format: Dual-Tree Structure (Sync Tree + Async Tree)

**Variation axis**: Output format
**Hypothesis**: R2's V-02 (cascade execution tree) made C-06 and C-14 strong but collapsed sync and async into a single tree, making C-18 (structural table split) impossible. R3 V-02 builds two separate execution trees — Sync Tree and Async Tree. A trigger's timing tier is its tree membership, not a column annotation. Each tree independently closes cascade chains with `[TERMINAL]` leaf nodes (C-16). The DFS back-edge detection step is applied to the unified edge set from both trees (C-19). The candidate denominator is declared before either tree is built (C-15). Evidence verdicts require section citations (C-12), but evidence gating is inline rather than role-separated (this variation does not target C-17 — see V-01 and V-04 for role-separated gating).

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. Produce a trigger fire analysis using the dual-tree structure below. The two trees — Sync Execution Tree and Async Execution Tree — are the primary document structure. Sync triggers appear only in the Sync Tree; Async triggers appear only in the Async Tree.

---

#### SECTION 0 — ANALYSIS SETUP

**0-A Change Scope Pin**

> **Scope**: `{Entity}` — `{Field}` changed from `{old value}` to `{new value}` (context: `{initiating action}`)

Only triggers whose trigger type, entity filter, and field filter match this entity + field belong in either tree.

**0-B Vocabulary Contract**

All tree node cells are bound to the following terms. Non-conforming values are marked `[NC: actual_value]`.

| Column | Permitted Values | Non-Conforming Examples |
|---|---|---|
| **PA Flow Type** | `Automated – Dataverse`, `Automated – SharePoint`, `Automated – HTTP`, `Instant`, `Scheduled` | `cloud flow`, `automated flow`, `PA flow` |
| **Condition** | `Taken: [branch] — [reason]` AND `Skipped: [branch] — [reason]` (both required for conditional) \| `No condition` | Stating only the taken branch |
| **Reads** | `{Entity}.{Field}` pattern | `"the record"`, `"status field"` |
| **Produces** | Opens with: `Sets` \| `Creates` \| `Deletes` \| `Sends email via` \| `Calls HTTP` \| `Starts child flow:` \| `Posts adaptive card to` | `"processes"`, `"notifies"`, `"updates"` |
| **Writes** | `{Entity}.{Field} = {value}` for downstream-triggering writes. `None` if none. | Generic descriptions |

**0-C Candidate Pre-Scan**

Before building either tree, enumerate the full candidate set. Do not evaluate conditions — a trigger with a condition is still a candidate.

| Candidate ID | Trigger Name | PA Flow Type | Tier (Sync/Async) | Matching Basis |
|---|---|---|---|---|
| CP-01 | | | | |

**Denominator Count: N** — This count governs Section 3 reconciliation. Every CP-NN must appear there, resolved as FIRED, CONFIRMED ABSENT, or FLAGGED GAP. Unresolved entries are structural gaps.

---

#### SECTION 1 — SYNC EXECUTION TREE

The Sync Execution Tree contains all triggers that execute in the `Sync` tier — those that block the originating transaction.

**Cascade Rule**: If a Sync trigger's `Writes` field causes another trigger to fire, that downstream trigger appears as a child node immediately beneath its parent, before moving to the next sibling. Walk the cascade to termination before listing the next independent (sibling) trigger.

**Termination Condition**: A cascade chain terminates when the current node writes a field that does not match any CP-NN candidate's trigger condition, or when the node writes `None`. A fixed depth is not a valid stopping rule — state this explicitly.

**Terminal Marker Rule**: The final node of each cascade chain carries `[TERMINAL]` on its own line, at the node level. Every chain must close with `[TERMINAL]` before the tree continues. A chain without `[TERMINAL]` is marked `[CHAIN OPEN: trace may be incomplete]`.

**Tree Format**:

```
SYNC EXECUTION TREE — {Entity.Field}: {old value} → {new value}
|
+-- [Sync Primary] {Trigger Name} ({PA Flow Type})
|     Condition: {Taken: ... — ... / Skipped: ... — ...} | {No condition}
|     Reads: {Entity.Field}, {Entity.Field}
|     Produces: {Sets | Creates | ...} {connector} {target} {resulting state}
|     Writes: {Entity.Field = value}  ← causes cascade below
|     Chain: CH-NN
|       |
|       +-- [Sync Cascade from CH-NN] {Trigger Name} ({PA Flow Type})
|             Condition: {No condition}
|             Reads: {Entity.Field}
|             Produces: {action}
|             Writes: None
|             [TERMINAL]
|
+-- [Sync Primary] {Trigger Name} ({PA Flow Type})
|     Condition: ...
|     Reads: ...
|     Produces: ...
|     Writes: None
|     [TERMINAL]
```

**Sync Tree Summary**:
- Sync fires: N (list by name)
- Sync edge set: `{Trigger} → writes {Entity.Field} → fires {Trigger}` for each Writes entry that matches a candidate. `{Trigger} → writes {Entity.Field} → [NO DOWNSTREAM]` for writes that match no candidate.

---

#### SECTION 2 — ASYNC EXECUTION TREE

The Async Execution Tree contains all triggers that execute in the `Async` tier — fire-and-forget.

**Latency Rule**: Every Async node must include `Latency: ~N min [standard|premium] tier`. Numeric N is required. "Unknown" and blank are not permitted.

**Same cascade rule, termination condition, and `[TERMINAL]` marker rule as Section 1 apply.**

**Tree Format**:

```
ASYNC EXECUTION TREE — {Entity.Field}: {old value} → {new value}
|
+-- [Async Primary] {Trigger Name} ({PA Flow Type})
|     Latency: ~N min [standard|premium] tier
|     Condition: {Taken: ... — ... / Skipped: ... — ...} | {No condition}
|     Reads: {Entity.Field}, {Entity.Field}
|     Produces: {action}
|     Writes: {Entity.Field = value}  ← causes cascade below
|     Chain: CH-NN
|       |
|       +-- [Async Cascade from CH-NN] {Trigger Name} ({PA Flow Type})
|             Latency: ~N min [standard|premium] tier
|             Condition: ...
|             Reads: ...
|             Produces: ...
|             Writes: None
|             [TERMINAL]
|
+-- [Async Primary] {Trigger Name} ({PA Flow Type})
|     Latency: ~N min [standard|premium] tier
|     ...
|     [TERMINAL]
```

**Async Tree Summary**:
- Async fires: N (list by name)
- Async edge set: `{Trigger} → writes {Entity.Field} → fires {Trigger}` for each applicable Writes entry.

---

#### SECTION 3 — CANDIDATE RECONCILIATION

Resolve every CP-NN from Section 0-C:

| Candidate ID | Trigger Name | Resolution | Evidence Citation |
|---|---|---|---|

Resolution codes:
- `FIRED (Sync Tree — {node description})` — cite the specific tree node
- `FIRED (Async Tree — {node description})` — cite the specific tree node
- `CONFIRMED ABSENT ([specific condition or filter that prevented firing])` — name the specific reason
- `FLAGGED GAP ([reason expected to fire])` — trigger expected but absent; investigation required

Totals: N FIRED, N CONFIRMED ABSENT, N FLAGGED GAP

---

#### SECTION 4 — BACK-EDGE DETECTION

**4-A Unified Edge Set**

Combine the Sync edge set (Section 1) and Async edge set (Section 2):

```
Full edge set:
- {Trigger A} → writes {Entity.Field} → fires {Trigger B}
- {Trigger B} → writes {Entity.Field} → fires {Trigger C}
- {Trigger D} → writes {Entity.Field} → [NO DOWNSTREAM]
```

**4-B DFS Back-Edge Detection Algorithm**

Apply the following detection procedure to the unified edge set. Do not replace this step with visual inspection.

```
Initialize: visited = {}  |  in-path = {}
For each trigger T in the edge set not yet in visited:
  Step 1: Add T to in-path
  Step 2: For each trigger U that T fires:
     a. If U is in in-path: BACK-EDGE FOUND → emit [BACK-EDGE: T → ... → U → T]
     b. If U not in visited: recurse (Step 1 for U)
  Step 3: Remove T from in-path; add T to visited
```

State result after completing the procedure:
- `Graph property: DAG` — no back-edges found
- `Graph property: CYCLIC` — one or more `[BACK-EDGE]` markers found; cite each cycle path

Do not write `DAG` or `CYCLIC` without completing Steps 1–3 for all edge-set nodes.

---

#### SECTION 5 — PATHOLOGY ANALYSIS

Each verdict must cite specific evidence from Sections 1–4. A bare assertion without a citation is marked `[INSUFFICIENT: cite the section and item that supports this verdict]`.

**Trigger Storm**
- Firing count: Sync N + Async N = N total (by name)
- Storm threshold: > 3 total executions or any `[BACK-EDGE]` in Section 4-B
- Re-entry: cite Section 4-B result
- Verdict: `CLEARED (count = N; DAG per 4-B DFS; edge set per 4-A)` | `STORM DETECTED (count = N; back-edge: {path from 4-B})`

**Missing Triggers**
- `FLAGGED GAP` entries from Section 3: [list or "none"]
- For each gap: trigger name, gap cause, risk level
- Verdict: `CLEARED (N: N fired, N confirmed absent, 0 flagged gaps, per Section 3)` | `MISSING TRIGGER: {name — gap cause — risk}`

**Circular Triggers**
- Graph property from Section 4-B: DAG | CYCLIC
- Edge set from 4-A cited
- Verdict: `CLEARED (DAG per 4-B DFS; edge set: {from 4-A})` | `CIRCULAR TRIGGER: {cycle path from 4-B}`

---

#### SECTION 6 — RISK-RANKED PATHOLOGY SUMMARY

| Rank | Pathology | Risk Level | Operational Impact | Mitigation |
|---|---|---|---|---|

Critical first. If all cleared: `All three pathology classes cleared — dual-tree analysis complete.`

---

Now receive the scenario and trigger registry, then produce the analysis.

---

## V-03 — Phrasing Register: Extended Failure Mode Catalog (FM-01 Through FM-14) with SHALL Language

**Variation axis**: Phrasing register
**Hypothesis**: R2 V-05's failure-mode catalog (FM-01 through FM-09, addressing C-01 through C-14) achieved 100 points by naming the specific failure each protocol section prevents, then governing it with SHALL language. Rubric v3 adds five new criteria (C-15 through C-19). R3 V-03 extends the catalog to FM-14, adding FM-10 (Denominator Shrinkage, C-15), FM-11 (Orphaned Chains, C-16), FM-12 (Verdict Capture, C-17), FM-13 (Tier Blur, C-18), and FM-14 (Visual Cycle Inference, C-19). The pattern from R2 holds: naming the failure mode makes the requirement self-explaining, and the SHALL language makes it non-negotiable. The hypothesis is that the extended catalog drives all five new criteria by the same mechanism that drove C-11–C-14 in R2.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. This document is the trigger fire analysis protocol. Normative keywords: **SHALL** = mandatory; **SHALL NOT** = prohibited; **SHOULD** = strongly recommended.

---

#### FOURTEEN FAILURE MODES OF INFORMAL TRIGGER ANALYSIS

The fourteen failure modes below define what informal trigger analysis cannot prevent. Each maps to a SHALL-governed protocol section.

**FM-01 — Undeclared Denominator**
*What goes wrong*: Enumeration begins by listing what fires. Triggers never considered leave silence, not visible gaps. C-01 violations (missed triggers) are structurally undetectable.
*Protocol response*: Candidate pre-scan runs before any outcome determination (Section 1).

**FM-02 — Closed-Set Pathology Scan**
*What goes wrong*: Pathology identification happens after the firing set locks in with no denominator to compare against. C-04 violations (missed pathology classes) and C-05 violations (false positives) go unnoticed.
*Protocol response*: Denominator reconciliation produces the evidence base for all three pathology verdicts (Section 4).

**FM-03 — Vocabulary Drift**
*What goes wrong*: Descriptions like "sends a notification" or "updates the record" pass informal review. C-08 violations go unreported.
*Protocol response*: Vocabulary term sets defined at Section 0; non-conforming values → `[NC: value]`.

**FM-04 — Branch Amnesia**
*What goes wrong*: Conditional triggers document the taken branch; the skipped branch is silently omitted. C-07 violations go unnoticed.
*Protocol response*: Both branches SHALL be declared for every conditional trigger (Section 2, Term Set E).

**FM-05 — Latency Blindness**
*What goes wrong*: Sync and async triggers are mixed without tier labels; async latency is omitted. C-10 violations produce integration design errors.
*Protocol response*: Every trigger SHALL declare Sync/Async tier; Async triggers SHALL include latency range (Section 2).

**FM-06 — Vocabulary Gap Without Enforcement**
*What goes wrong*: Vocabulary requirements are stated but no inline violation marker exists. Non-conforming values pass because the reviewer must already know the correct term. C-11 violations pass silently.
*Protocol response*: All vocabulary violations SHALL be marked `[NC: actual_value]` inline — in the cell where the violation occurs.

**FM-07 — Verdict Orphaning**
*What goes wrong*: Pathology verdicts state conclusions without citing the analysis that produced them. C-12 violations occur when a verdict has no traceable evidence chain.
*Protocol response*: Every verdict SHALL include a citation. Bare assertions SHALL be marked `[INSUFFICIENT: cite Section N item M]`.

**FM-08 — Cascade Truncation**
*What goes wrong*: Side-effect chains are traced "one level deep" by convention, not because no further triggers exist. C-13 violations occur when early truncation is mistaken for complete tracing.
*Protocol response*: Cascades SHALL be traced until the termination condition is met — "trace until no written field matches any candidate's trigger condition." A fixed depth SHALL NOT be used as a stopping rule.

**FM-09 — Prose-Only Cycle Reasoning**
*What goes wrong*: Circular trigger detection relies on reading the prose and noticing a cycle. Non-obvious cycles (length ≥ 3) are missed by visual inspection. C-14 violations occur.
*Protocol response*: Circular detection SHALL be grounded in an explicit directed edge set; graph property is stated from the edge set, not from prose inspection.

**FM-10 — Denominator Shrinkage**
*What goes wrong*: Conditions are evaluated during the candidate pre-scan, silently reducing the denominator below the true candidate population. The declared count is smaller than the actual candidate set, so silent omissions remain structurally undetectable even when a count is present. C-15 violations occur.
*Protocol response*: The candidate pre-scan SHALL enumerate triggers by entity/field/type match only. Conditions SHALL NOT be evaluated during pre-scan. The declared count is the true pre-condition upper bound.

**FM-11 — Orphaned Chains**
*What goes wrong*: Cascade chains are walked but not explicitly closed. The analysis ends at a fixed depth or when the model exhausts downstream candidates, without a per-chain marker. A reviewer cannot distinguish complete chains from truncated ones. C-16 violations occur.
*Protocol response*: Every cascade chain SHALL close with a `[TERMINAL]` row marker at the row level. A chain without `[TERMINAL]` is structurally open and SHALL be flagged `[CHAIN OPEN: trace may be incomplete]`.

**FM-12 — Verdict Capture**
*What goes wrong*: The analyst who produces the analysis also gates their own verdicts. Even with an `[INSUFFICIENT]` marker defined, the analyst can satisfy the gate by retrofitting citations rather than citing pre-existing evidence. The gate is advisory, not enforced. C-17 violations occur because no structural constraint prevents self-validation.
*Protocol response*: The evidence gate function SHALL be a structurally separate role that cannot generate analysis — it can only approve (`[EVIDENCE: CONFIRMED — {citation}]`) or flag (`[INSUFFICIENT: state what evidence is needed and where]`).

**FM-13 — Tier Blur**
*What goes wrong*: Sync and async triggers share a table, with tier as a row-level annotation. Tier-level properties (latency, execution guarantee, connector tier) require per-row parsing rather than being addressable as column attributes. C-18 violations occur.
*Protocol response*: Sync and async triggers SHALL occupy separate structural tables. A trigger's timing tier is its table membership.

**FM-14 — Visual Cycle Inference**
*What goes wrong*: Back-edge detection is performed by visual inspection of the directed edge set — reading paths by eye. Non-obvious cycles (length ≥ 3) are missed by visual inspection. C-19 violations occur when the detection procedure is described but not algorithmic.
*Protocol response*: Back-edge detection SHALL be applied as an explicit DFS traversal with an `in-path` set — not visual inspection. The traversal steps SHALL be explicitly shown.

The protocol below addresses each failure mode at its structural root.

---

#### SECTION 0 — VOCABULARY CONTRACT (addresses FM-03, FM-06)

The analyst SHALL define and bind all term sets before beginning Section 1. Non-conforming values in output tables SHALL be marked `[NC: actual_value]`.

**Term Set A — PA Flow Type**
Permitted: `Automated – Dataverse` | `Automated – SharePoint` | `Automated – HTTP` | `Instant` | `Scheduled`
Non-conforming: `cloud flow` | `automated flow` | `PA flow` | `button flow`

**Term Set B — Execution Tier and Latency** (addresses FM-05, FM-13)
| Code | Tier | Latency Requirement |
|---|---|---|
| B-01 | `Sync` | Write `Inline (blocks transaction)` |
| B-02 | `Async` | Write `~N min [standard\|premium] tier` where N is a numeric estimate |

Non-conforming: blank latency | `"varies"` | `"unknown"` for Async.

**Term Set C — Input Payload Reference**
Pattern: `{EntityName}.{ColumnName}` (e.g., `Request.Status`).
Non-conforming: `"the status field"` | `"the record"` | `"relevant fields"` | any reference omitting the table name.

**Term Set D — Output Action Lead**
Permitted: `Sets` | `Creates` | `Deletes` | `Sends email via` | `Calls HTTP` | `Starts child flow:` | `Posts adaptive card to`
Non-conforming: `"processes"` | `"notifies"` | `"updates"` | `"triggers"` | `"handles"`

**Term Set E — Branch Coverage Declaration** (addresses FM-04)
For conditional triggers, the Condition cell SHALL contain:
- `Taken: [branch name] — [reason]`
- `Skipped: [branch name] — [reason]`
Both lines are required. Stating only the taken branch → `[NC: only taken branch declared]`.
For unconditional triggers: `No condition`.

---

#### SECTION 1 — CANDIDATE PRE-SCAN (addresses FM-01, FM-10)

The analyst SHALL pin the change scope before scanning:
> **Scope**: `{Entity}` — `{Field}` changed from `{old value}` to `{new value}` (context: `{initiating action}`)

The analyst SHALL enumerate all trigger candidates. Pre-scan rule (FM-10 guard): **A trigger is a candidate if and only if its trigger type, entity filter, and field filter could match the change event. The analyst SHALL NOT evaluate conditions during this step.** A trigger with a condition is still a candidate; condition evaluation happens in Section 2.

| Candidate ID | Trigger Name | Type (Term Set A) | Tier (B-01 or B-02) | Matching Basis |
|---|---|---|---|---|
| C-01 | | | | |

**Denominator Count: N** — This is the pre-condition population. Every C-NN SHALL appear in Section 4 with a resolution. Unresolved entries are structural gaps indicating denominator shrinkage.

---

#### SECTION 2 — SYNC FIRING TABLE (addresses FM-04, FM-05, FM-08, FM-11, FM-13)

The analyst SHALL list all triggers that fire in the `Sync` tier in this table. Async triggers SHALL NOT appear in this table (FM-13 guard).

| Seq | C-Ref | Trigger Name | Type (Term Set A) | Condition (Term Set E) | Input Payload (Term Set C) | Output Action (Term Set D) | Side-Effect Writes | Latency (Term Set B) |
|---|---|---|---|---|---|---|---|---|

**Cascade Rule (addresses FM-08)**: If a row's Side-Effect Writes field matches any Section 1 candidate's trigger condition, the downstream trigger SHALL appear as the immediately next row, before continuing to the next independent trigger. The analyst SHALL trace cascades until the termination condition is reached: "the current row writes a field that does not match any Section 1 candidate's trigger condition, or writes None." A fixed depth SHALL NOT be used as a stopping rule.

**Terminal Row Rule (addresses FM-11)**: The final row of each cascade sequence SHALL contain `[TERMINAL]` in the Side-Effect Writes column. A cascade sequence without a `[TERMINAL]` row is structurally open — mark `[CHAIN OPEN: trace may be incomplete]`.

Sync total: N

---

#### SECTION 3 — ASYNC FIRING TABLE (addresses FM-04, FM-05, FM-08, FM-11, FM-13)

The analyst SHALL list all triggers that fire in the `Async` tier in this table. Sync triggers SHALL NOT appear in this table (FM-13 guard).

| Seq | C-Ref | Trigger Name | Type (Term Set A) | Condition (Term Set E) | Input Payload (Term Set C) | Output Action (Term Set D) | Side-Effect Writes | Latency (Term Set B) |
|---|---|---|---|---|---|---|---|---|

**Same cascade and terminal row rules as Section 2 apply.**

Async total: N

---

#### SECTION 4 — CANDIDATE RECONCILIATION (addresses FM-02)

The analyst SHALL resolve every Section 1 candidate:

| Candidate ID | Trigger Name | Resolution | Reason |
|---|---|---|---|

Resolution codes: `FIRED (Sync, Seq #N)` | `FIRED (Async, Seq #N)` | `CONFIRMED ABSENT ([specific reason])` | `FLAGGED GAP ([reason expected])`

Totals: N FIRED, N CONFIRMED ABSENT, N FLAGGED GAP

---

#### SECTION 5 — DIRECTED EDGE SET AND BACK-EDGE DETECTION (addresses FM-09, FM-14)

**5-A Edge Set Construction**

The analyst SHALL construct the complete directed edge set from Sections 2–3 side-effect writes:

```
{Trigger A} → writes {Entity.Field} → fires {Trigger B}
{Trigger D} → writes {Entity.Field} → [NO DOWNSTREAM]
```

Every side-effect write SHALL appear in the edge set — as a directed edge or as `[NO DOWNSTREAM]`.

**5-B DFS Back-Edge Detection** (FM-14 guard — visual inspection SHALL NOT replace this step)

The analyst SHALL apply the following algorithmic procedure:

```
Initialize: visited = {}  |  in-path = {}
For each trigger T not yet in visited:
  1. Add T to in-path
  2. For each downstream trigger U that T fires (per 5-A edge set):
     a. If U is in in-path: record [BACK-EDGE: T → ... → U → T]
     b. Else if U not in visited: recurse (apply procedure to U)
  3. Remove T from in-path; add T to visited
```

State result: `Graph property: DAG` (no back-edges found) | `Graph property: CYCLIC` ([BACK-EDGE] found; cite path).

The analyst SHALL NOT write `DAG` or `CYCLIC` without completing Steps 1–3 for all nodes.

---

#### SECTION 6 — PATHOLOGY ANALYSIS (addresses FM-02, FM-07, FM-12)

All three pathology classes SHALL be addressed. Each verdict SHALL cite specific Section 1–5 evidence. A bare assertion without a citation SHALL be marked `[INSUFFICIENT: cite Section N item M]` (FM-07 guard).

**Evidence Gate Note (addresses FM-12)**: The analyst SHALL treat this section as a self-audit step. Before issuing any verdict, the analyst SHALL verify that a traceable evidence chain exists in Sections 1–5. If the chain is incomplete, the analyst SHALL write `[INSUFFICIENT: state what evidence is needed and where]` and SHALL NOT issue the verdict.

**6-A Trigger Storm**
- Firing count: Sync N + Async N = N total (cite Sections 2–3 totals by name)
- Storm threshold: > 3 total executions or any `[BACK-EDGE]` found in Section 5-B
- Re-entry: cite Section 5-B result
- Verdict: `CLEARED (count = N, no back-edge per Section 5-B DFS, evidence: Sections 2–3 totals)` | `STORM DETECTED (count = N; path: {5-B back-edge path or "none"})`

**6-B Missing Triggers**
- `FLAGGED GAP` entries from Section 4: [list or "none"]
- For each gap: trigger name, gap cause, risk level
- Verdict: `CLEARED (N: N fired, N confirmed absent, 0 gaps, per Section 4 reconciliation)` | `MISSING TRIGGER: {name — gap cause — risk}`

**6-C Circular Triggers**
- Graph property from Section 5-B: DAG | CYCLIC
- Edge set from 5-A cited
- Verdict: `CLEARED (DAG per 5-B DFS; edge set: {from 5-A})` | `CIRCULAR TRIGGER: {cycle path from 5-B}`

---

#### SECTION 7 — RISK-RANKED PATHOLOGY SUMMARY

| Rank | Pathology | Risk Level | Operational Impact | Mitigation |
|---|---|---|---|---|

Critical first. If all cleared: `No pathologies confirmed — all fourteen failure modes addressed without findings.`

---

Now receive the scenario and trigger registry, then produce the analysis following this protocol.

---

## V-04 — Combined: Output Format + Lifecycle Emphasis (Structural Split as Primary Spine with Role-Separated Gatekeeper)

**Variation axes**: Output format + lifecycle emphasis
**Hypothesis**: R2 V-04 (sync/async split tables + cascade engine + [INSUFFICIENT] gate) achieved 100 points. Rubric v3 adds C-15, C-16, C-17, C-18, C-19. R3 V-04 strengthens the R2 design along all five new axes simultaneously: the denominator is declared with an explicit pre-condition count (C-15); each cascade chain closes with a `[TERMINAL]` row marker before the next chain begins (C-16); a separate gatekeeper role — structurally incapable of writing analysis — gates all verdict cells (C-17); sync and async remain in separate structural tables as the primary document spine (C-18); and the DFS back-edge detection procedure is applied with explicit traversal steps (C-19). Lifecycle ordering enforces the evidence dependency chain: denominator before tables, tables before edge accumulator, edge accumulator before DFS, DFS before pathology.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert operating in two sequential phases — Analysis Phase and Gate Phase. Complete the Analysis Phase in full before beginning the Gate Phase.

The document has two primary structural sections — the Sync Firing Section and the Async Firing Section. A trigger's timing tier is its section membership: sync triggers appear only in Section 2, async triggers appear only in Section 3. This is a structural constraint, not a labeling convention.

---

#### PHASE 0 — SETUP

**0-A Change Scope Pin**

> **Scope**: `{Entity}` — `{Field}` changed from `{old value}` to `{new value}` (context: `{initiating action}`)

**0-B Vocabulary Contract**

All table cells in Sections 1–4 are bound. Non-conforming values are marked `[NC: actual_value]`.

| Term Set | Column | Permitted Values | Non-Conforming |
|---|---|---|---|
| A | PA Flow Type | `Automated – Dataverse`, `Automated – SharePoint`, `Automated – HTTP`, `Instant`, `Scheduled` | `cloud flow`, `automated flow`, `PA flow` |
| B | Latency | Sync: `Inline (blocks transaction)` \| Async: `~N min [standard\|premium] tier` | blank, `"varies"`, `"unknown"` |
| C | Input Payload | `{Entity}.{Field}` pattern | `"the record"`, `"status field"` |
| D | Output Action | Opens with: `Sets` \| `Creates` \| `Deletes` \| `Sends email via` \| `Calls HTTP` \| `Starts child flow:` \| `Posts adaptive card to` | `"processes"`, `"notifies"`, `"updates"` |
| E | Condition Branch | `Taken: [branch] — [reason]` AND `Skipped: [branch] — [reason]` (both required for conditional) \| `No condition` | Only taken branch stated → `[NC: only taken branch declared]` |

**0-C Candidate Pre-Scan**

Before populating either firing section, declare the full candidate set. Do not evaluate conditions — a trigger with a condition is still a candidate.

| Candidate ID | Trigger Name | Type (Term Set A) | Tier | Matching Basis |
|---|---|---|---|---|
| D-01 | | | Sync or Async | |

**Denominator Count: N** — pre-condition, pre-evaluation. Every D-NN must appear in Section 4 (reconciliation). The count makes silent omissions detectable: if N candidates are declared and M < N are resolved in Section 4, the N-M unresolved entries are structural gaps.

---

#### SECTION 2 — SYNC FIRING TABLE

Sync triggers only. For each trigger that fires in the Sync tier:

| Seq | D-Ref | Trigger Name | Type (Term Set A) | Condition (Term Set E) | Input Payload (Term Set C) | Output Action (Term Set D) | Side-Effect Writes | Chain ID | Latency (Term Set B) |
|---|---|---|---|---|---|---|---|---|---|

**Cascade Rule**: If a row's Side-Effect Writes field causes another trigger to fire, assign a Chain ID (CH-NN) and trace the cascade immediately — the downstream trigger appears as the next row. Continue until the termination condition is met: "the current row writes a field that does not match any D-NN candidate's trigger condition, or writes None." A fixed depth is not a valid stopping rule.

**Terminal Row Rule**: The final row of each cascade sequence SHALL contain `[TERMINAL]` in the Side-Effect Writes column. A sequence without `[TERMINAL]` is marked `[CHAIN OPEN: trace may be incomplete]`.

Sync edge accumulator (running — add after each Side-Effect Write): `{Trigger} → writes {Entity.Field} → fires {Trigger}` | `{Trigger} → writes {Entity.Field} → [NO DOWNSTREAM]`

Sync total: N fires

---

#### SECTION 3 — ASYNC FIRING TABLE

Async triggers only. Same format as Section 2. The Latency column is active — every row requires `~N min [standard|premium] tier` with a numeric N.

| Seq | D-Ref | Trigger Name | Type (Term Set A) | Condition (Term Set E) | Input Payload (Term Set C) | Output Action (Term Set D) | Side-Effect Writes | Chain ID | Latency (Term Set B) |
|---|---|---|---|---|---|---|---|---|---|

**Same cascade rule, termination condition, and `[TERMINAL]` marker rule as Section 2.**

Async edge accumulator: `{Trigger} → writes {Entity.Field} → fires {Trigger}` | `[NO DOWNSTREAM]`

Async total: N fires

---

#### SECTION 4 — CANDIDATE RECONCILIATION

Every D-NN from Phase 0-C SHALL appear here:

| Candidate ID | Trigger Name | Resolution | Reason |
|---|---|---|---|

Resolution codes: `FIRED (Sync, Seq #N)` | `FIRED (Async, Seq #N)` | `CONFIRMED ABSENT ([specific condition or filter])` | `FLAGGED GAP ([reason expected])`

Totals: N FIRED, N CONFIRMED ABSENT, N FLAGGED GAP

---

#### SECTION 5 — UNIFIED EDGE SET AND DFS DETECTION

**5-A Unified Edge Set**

Combine Section 2 sync edge accumulator and Section 3 async edge accumulator:

```
{Trigger A} → writes {Entity.Field} → fires {Trigger B}
{Trigger B} → writes {Entity.Field} → fires {Trigger C}
{Trigger D} → writes {Entity.Field} → [NO DOWNSTREAM]
```

**5-B DFS Back-Edge Detection**

Apply the following algorithmic procedure to the 5-A edge set. Do not replace with visual inspection.

```
Initialize: visited = {}  |  in-path = {}
For each trigger T not yet in visited:
  1. Add T to in-path
  2. For each trigger U that T fires:
     a. If U in in-path: emit [BACK-EDGE: T → ... → U → T]
     b. Else if U not in visited: recurse (Step 1 for U)
  3. Remove T from in-path; add T to visited
```

Graph property: `DAG` (no back-edges found after complete traversal) | `CYCLIC` ([BACK-EDGE] emitted; cite path).

---

#### GATE PHASE — EVIDENCE GATEKEEPER

The Gate Phase is a structurally separate function. It cannot generate new analysis, cannot add triggers to the firing set, and cannot modify Sections 2–5. It can only emit one of two verdicts per check:

- `[EVIDENCE: CONFIRMED — {specific citation to section and item}]` — the finding is directly supported
- `[INSUFFICIENT: {state exactly what evidence is needed and where it should appear}]` — the finding lacks a traceable evidence chain

**G-1 — Trigger Storm Gate**
- Total fires: Sync N + Async N = N (cite Section 2 and 3 totals)
- Storm threshold: > 3 executions or any `[BACK-EDGE]` in 5-B
- Gate verdict:
  - If count ≤ 3 and no `[BACK-EDGE]`: `[EVIDENCE: CONFIRMED — CLEARED; total fires = N per Sections 2–3; DAG per 5-B DFS]`
  - If count > 3 or `[BACK-EDGE]`: `[STORM DETECTED — count = N; re-entry: {5-B back-edge path or "none"}]`
  - If Section 2/3 totals were not stated: `[INSUFFICIENT: Sections 2–3 did not produce a named firing total; count required before storm verdict]`

**G-2 — Missing Triggers Gate**
- `FLAGGED GAP` entries from Section 4: [list or "none"]
- Gate verdict:
  - If 0 gaps: `[EVIDENCE: CONFIRMED — CLEARED; N candidates: N fired, N confirmed absent, 0 gaps, per Section 4 reconciliation]`
  - If gaps: `[MISSING TRIGGER: {name} — {gap cause} — {risk level}]`
  - If Section 4 totals not stated: `[INSUFFICIENT: Section 4 did not produce resolution totals; reconciliation required before missing-trigger verdict]`

**G-3 — Circular Triggers Gate**
- Graph property from Section 5-B: DAG | CYCLIC
- Gate verdict:
  - If DAG: `[EVIDENCE: CONFIRMED — CLEARED; DAG per 5-B DFS traversal; edge set: {from 5-A}]`
  - If CYCLIC: `[CIRCULAR TRIGGER: {cycle path from 5-B}; Risk = Critical]`
  - If 5-B DFS step was not completed: `[INSUFFICIENT: Section 5 did not show DFS traversal steps; graph property cannot be confirmed from edge set inspection alone]`

**G-4 — Risk-Ranked Pathology Summary**

Using only evidence-confirmed findings from G-1, G-2, G-3:

| Rank | Pathology | Risk Level | Operational Impact | Mitigation |
|---|---|---|---|---|

Critical first. If all confirmed clear: `No pathologies confirmed — all three classes gated with evidence citations.`

---

Now receive the scenario and trigger registry. Execute Phase 0, then Section 2, then Section 3, then Section 4, then Section 5, then the Gate Phase.

---

## V-05 — Combined: Phrasing Register + Inertia Framing (Five Structural Guarantees)

**Variation axes**: Phrasing register + inertia framing
**Hypothesis**: R2 V-05's inertia framing named nine failure modes as the compliance strategy and achieved 100. Rubric v3 adds five new criteria (C-15 through C-19). R3 V-05 reframes these five criteria not as failure modes to prevent, but as *structural guarantees* — properties that a correct trigger analysis provides that informal analysis structurally cannot. The distinction is subtle but load-bearing: a failure mode framing says "here is what can go wrong without this requirement"; a guarantee framing says "here is what a correct analysis promises, and here is the structural mechanism that makes the promise verifiable." The hypothesis is that guarantee framing drives compliance more reliably than failure-mode framing for the new criteria, because it positions the analyst as a promisor rather than a defender — shifting from "don't miss things" to "make specific, verifiable commitments."

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. This document defines the trigger fire analysis protocol. Normative keywords: **SHALL** = mandatory; **SHALL NOT** = prohibited.

---

#### NINE FAILURE MODES OF INFORMAL TRIGGER ANALYSIS

These failure modes define what informal analysis cannot prevent. The protocol below addresses each at its structural root.

**FM-01 — Undeclared Denominator**: Enumeration starts with outcomes; unexamined triggers leave silence. *Protocol response*: Candidate pre-scan before outcome determination (Section 1).

**FM-02 — Closed-Set Pathology Scan**: Pathology comparison has no denominator. *Protocol response*: Denominator reconciliation as evidence base (Section 4).

**FM-03 — Vocabulary Drift**: Generic descriptions pass review unnoticed. *Protocol response*: Term sets defined at Section 0; `[NC: value]` inline markers.

**FM-04 — Branch Amnesia**: Skipped branches silently omitted. *Protocol response*: Both branches SHALL be declared (Term Set E).

**FM-05 — Latency Blindness**: Tier and latency omitted for async triggers. *Protocol response*: Tier = table membership; numeric latency required in Async table.

**FM-06 — Vocabulary Gap Without Enforcement**: Vocabulary stated but no inline violation flag. *Protocol response*: `[NC: value]` required in the cell of violation.

**FM-07 — Verdict Orphaning**: Verdicts issued without traceable evidence chains. *Protocol response*: `[INSUFFICIENT: cite Section N item M]` for bare assertions.

**FM-08 — Cascade Truncation**: Chains stopped at fixed depth rather than at structural termination. *Protocol response*: Termination condition governs — not depth.

**FM-09 — Prose-Only Cycle Reasoning**: Cycles detected by reading order, not graph structure. *Protocol response*: Explicit directed edge set; graph property from the set.

---

#### FIVE STRUCTURAL GUARANTEES

A structural guarantee is a property that a correct trigger analysis makes verifiable. Informal analysis cannot provide these guarantees because it relies on the analyst's attention rather than structural constraints. The protocol below makes each guarantee mechanically verifiable.

**Guarantee G-1: Declared Pre-Condition Upper Bound** (addresses C-15)

*What informal analysis provides*: An enumeration of candidates that fires, filtered by judgment. Silent omissions are invisible.
*What this analysis guarantees*: A declared count of all entity/field/type-matching triggers before any condition is evaluated. This count is the upper bound — if fewer triggers fire, the non-firing entries must each be individually accounted for. Omissions cannot be silent; they must be resolved as `CONFIRMED ABSENT` or `FLAGGED GAP`.
*Structural mechanism*: Candidate pre-scan in Section 1 evaluates entity, field, and trigger type only. Conditions SHALL NOT be evaluated during pre-scan. The declared count is the pre-condition denominator.
*Verifiability check*: Count the Section 1 rows. Count the Section 4 resolutions. If they are unequal, the guarantee is not met.

**Guarantee G-2: Per-Chain Closure Evidence** (addresses C-16)

*What informal analysis provides*: Cascade chains traced to "sufficient depth" — a judgment call.
*What this analysis guarantees*: Every cascade chain produces a `[TERMINAL]` marker at its final row. A reviewer can verify per-chain completeness by inspecting the chain, not by re-running the analysis.
*Structural mechanism*: The final row of each cascade sequence SHALL contain `[TERMINAL]` in the Side-Effect Writes column. The presence of `[TERMINAL]` in a row is mechanical evidence that the chain was traced to structural termination. Its absence is a structural gap — mark `[CHAIN OPEN: trace may be incomplete]`.
*Verifiability check*: Every Chain ID assigned in the Sync or Async table has a downstream row with `[TERMINAL]`. Chains without it are structurally open.

**Guarantee G-3: Verdict Structural Independence** (addresses C-17)

*What informal analysis provides*: Verdicts self-reviewed by the analyst who produced them. Even with an evidence citation requirement, the analyst can retrofit citations or write `[INSUFFICIENT]` for their own work and then resolve it in the same step.
*What this analysis guarantees*: The entity that gates verdicts cannot generate analysis. Structural separation prevents the analyst from approving their own conclusions.
*Structural mechanism*: The Gate Phase (Section 6) is a structurally separate role from the Analysis Phase (Sections 1–5). The Gate Phase SHALL NOT write new triggers, add analysis, or modify Sections 1–5. It SHALL only emit `[EVIDENCE: CONFIRMED — {citation}]` or `[INSUFFICIENT: {state what evidence is needed and where}]`.
*Verifiability check*: If any Gate Phase step adds information not already present in Sections 1–5, the structural independence guarantee is violated.

**Guarantee G-4: Tier as Table Membership** (addresses C-18)

*What informal analysis provides*: A trigger table with a Tier column. Tier-level properties (latency, execution guarantee, connector tier) require per-row parsing.
*What this analysis guarantees*: A trigger's execution tier is its table membership. Tier-level properties are column attributes of the tier's table — addressable at the column level without per-row parsing.
*Structural mechanism*: Sync triggers appear in the Sync Firing Table (Section 2) only. Async triggers appear in the Async Firing Table (Section 3) only. A trigger in the wrong table is a structural error.
*Verifiability check*: No row with `Sync` in its tier indicator appears in Section 3. No row with `Async` appears in Section 2.

**Guarantee G-5: Algorithmic Cycle Detection** (addresses C-19)

*What informal analysis provides*: A directed edge set inspected visually. Non-obvious cycles (length ≥ 3) are missed by eye.
*What this analysis guarantees*: Cycle detection is performed by an algorithmic DFS traversal with an `in-path` set. The traversal is O(V+E) and deterministic. Cycles of any length are detectable.
*Structural mechanism*: Section 5-B applies the DFS procedure with explicit traversal steps. The graph property is stated from the traversal result, not from visual inspection of the edge set.
*Verifiability check*: Section 5-B shows explicit `in-path` state transitions. The graph property (`DAG` or `CYCLIC`) is attributed to the traversal result with a path citation if `CYCLIC`.

---

#### SECTION 0 — VOCABULARY CONTRACT

The analyst SHALL bind all term sets before Section 1. Non-conforming values SHALL be marked `[NC: actual_value]` inline.

**Term Set A — PA Flow Type**
Permitted: `Automated – Dataverse` | `Automated – SharePoint` | `Automated – HTTP` | `Instant` | `Scheduled`
Non-conforming: `cloud flow` | `automated flow` | `PA flow` | `button flow`

**Term Set C — Input Payload**: `{EntityName}.{ColumnName}`. Non-conforming: omitting entity or column name.

**Term Set D — Output Action Lead**: `Sets` | `Creates` | `Deletes` | `Sends email via` | `Calls HTTP` | `Starts child flow:` | `Posts adaptive card to`. Non-conforming: `"processes"`, `"notifies"`, `"updates"`.

**Term Set E — Branch Coverage**: Both `Taken: [branch] — [reason]` AND `Skipped: [branch] — [reason]` required for conditional triggers. Unconditional: `No condition`. Single-branch declaration → `[NC: only taken branch declared]`.

---

#### SECTION 1 — CANDIDATE PRE-SCAN (provides Guarantee G-1)

> **Scope**: `{Entity}` — `{Field}` changed from `{old value}` to `{new value}` (context: `{initiating action}`)

The analyst SHALL enumerate all triggers matching the scope by entity, field, and trigger type. The analyst SHALL NOT evaluate conditions during this step.

| Candidate ID | Trigger Name | Type (Term Set A) | Tier | Matching Basis |
|---|---|---|---|---|
| C-01 | | | Sync | |

**Denominator Count: N** — pre-condition upper bound. This count governs Section 4 reconciliation. Each of the N entries must appear in Section 4 with a resolution.

---

#### SECTION 2 — SYNC FIRING TABLE (provides Guarantee G-2 for Sync chains; Guarantee G-4)

Sync triggers only. The analyst SHALL NOT place Async triggers in this table.

| Seq | C-Ref | Trigger Name | Type (Term Set A) | Condition (Term Set E) | Input Payload (Term Set C) | Output Action (Term Set D) | Side-Effect Writes | Chain ID |
|---|---|---|---|---|---|---|---|---|

**Cascade rule**: If a row's Side-Effect Writes field matches a Section 1 candidate's trigger condition, trace the cascade immediately — downstream trigger appears as next row. Trace until termination: "no written field matches any Section 1 candidate's trigger condition, or Writes = None." A fixed depth SHALL NOT be used as a stopping rule.

**Per-chain terminal marker** (Guarantee G-2): The final row of each cascade sequence SHALL contain `[TERMINAL]` in the Side-Effect Writes column. A sequence without `[TERMINAL]` is structurally open — mark `[CHAIN OPEN: trace may be incomplete]`.

Sync latency is `Inline (blocks transaction)` — this applies to all rows in this table.
Sync total: N

---

#### SECTION 3 — ASYNC FIRING TABLE (provides Guarantee G-2 for Async chains; Guarantee G-4)

Async triggers only. The analyst SHALL NOT place Sync triggers in this table.

| Seq | C-Ref | Trigger Name | Type (Term Set A) | Condition (Term Set E) | Input Payload (Term Set C) | Output Action (Term Set D) | Side-Effect Writes | Chain ID | Latency |
|---|---|---|---|---|---|---|---|---|---|

Latency column: `~N min [standard|premium] tier`. Numeric N required. "Unknown" is not permitted.

**Same cascade and `[TERMINAL]` rules as Section 2 apply.**

Async total: N

---

#### SECTION 4 — CANDIDATE RECONCILIATION

Every Section 1 candidate SHALL be resolved:

| Candidate ID | Trigger Name | Resolution | Reason |
|---|---|---|---|

Resolution codes: `FIRED (Sync, Seq #N)` | `FIRED (Async, Seq #N)` | `CONFIRMED ABSENT ([specific reason])` | `FLAGGED GAP ([reason expected])`

Totals: N FIRED, N CONFIRMED ABSENT, N FLAGGED GAP

---

#### SECTION 5 — UNIFIED EDGE SET AND BACK-EDGE DETECTION (provides Guarantee G-5)

**5-A Unified Edge Set**

The analyst SHALL collect all side-effect writes from Sections 2–3:

```
{Trigger A} → writes {Entity.Field} → fires {Trigger B}
{Trigger C} → writes {Entity.Field} → [NO DOWNSTREAM]
```

**5-B DFS Back-Edge Detection** (Guarantee G-5 — visual inspection SHALL NOT replace this step)

```
Initialize: visited = {}  |  in-path = {}
For each trigger T not yet in visited:
  1. Add T to in-path
  2. For each trigger U that T fires (per 5-A):
     a. If U in in-path: emit [BACK-EDGE: T → ... → U → T]
     b. Else if U not in visited: recurse (Step 1 for U)
  3. Remove T from in-path; add T to visited
```

State: `Graph property: DAG` (no back-edges, complete traversal) | `Graph property: CYCLIC` ([BACK-EDGE] found; cite path).

---

#### SECTION 6 — GATE PHASE (provides Guarantee G-3)

The Gate Phase is structurally separate from Sections 1–5. It SHALL NOT add triggers, generate analysis, or modify prior sections. It can only emit:
- `[EVIDENCE: CONFIRMED — {specific citation}]`
- `[INSUFFICIENT: {state what evidence is needed and where}]`

**G-1 — Trigger Storm**
- Total fires from Sections 2–3: N
- Threshold: > 3 or any `[BACK-EDGE]` in 5-B
- Gate verdict: `[EVIDENCE: CONFIRMED — CLEARED; count = N; DAG per 5-B DFS]` | `[STORM DETECTED — count = N; path: {5-B path or "none"}]` | `[INSUFFICIENT: firing total not stated in Sections 2–3]`

**G-2 — Missing Triggers**
- `FLAGGED GAP` entries from Section 4
- Gate verdict: `[EVIDENCE: CONFIRMED — CLEARED; N candidates: N fired, N absent, 0 gaps, per Section 4]` | `[MISSING TRIGGER: {name — gap cause — risk}]` | `[INSUFFICIENT: Section 4 reconciliation totals not stated]`

**G-3 — Circular Triggers**
- Graph property from Section 5-B
- Gate verdict: `[EVIDENCE: CONFIRMED — CLEARED; DAG per 5-B DFS; edge set: {from 5-A}]` | `[CIRCULAR TRIGGER: {cycle path from 5-B}; Risk = Critical]` | `[INSUFFICIENT: Section 5-B DFS traversal steps not shown; graph property cannot be confirmed from edge set inspection alone]`

**G-4 — Risk-Ranked Pathology Summary**

Using only evidence-confirmed findings from G-1, G-2, G-3:

| Rank | Pathology | Risk Level | Operational Impact | Mitigation |
|---|---|---|---|---|

Critical first. If all confirmed clear: `No pathologies confirmed — all nine failure modes addressed, all five structural guarantees verified.`

---

Now receive the scenario and trigger registry, then produce the full analysis (Sections 0–5) followed by the Gate Phase (Section 6).
