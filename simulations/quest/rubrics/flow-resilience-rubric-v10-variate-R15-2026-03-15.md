# flow-resilience — Round 15 Variations (Rubric v14)

**Target**: Push from R14 ceiling of 32/35 (99.14) toward 35/35 (100.00) by implementing the three new axes extracted from R14 structural patterns.

| New Criterion | Axis | What It Requires |
|---|---|---|
| C-41 | Inertia sub-part labeling | 1a/1b/1c or Act I/II/III labels inside the Inertia Assessment; row descriptors cross-reference by sub-part label |
| C-42 | SLA Budget pre-commitment | Named pre-table section commits TTD/TTC/TTR/TTV per class; Column Contract Recovery Path names it as reference source |
| C-43 | Failure Signature column | Column Contract includes Failure Signature: behavioral fingerprint during failure with ≥2 actor viewpoints per row; distinct from Trigger Condition and State |

| Variation | Axis | Hypothesis | C-41 | C-42 | C-43 | Predicted ceiling |
|---|---|---|---|---|---|---|
| V-01 | Inertia framing (1a/1b/1c labels) | Sub-part labeling satisfies C-41 without touching SLA or Failure Signature | PASS | — | — | 33/35 → 99.43 |
| V-02 | Lifecycle emphasis (SLA Budget step) | Dedicated Step 2 SLA Budget + Column Contract reference satisfies C-42 | — | PASS | — | 33/35 → 99.43 |
| V-03 | Role sequence (Failure Signature first in D-phase) | Failure Signature column with actor-differentiated fill requirement satisfies C-43 | — | — | PASS | 33/35 → 99.43 |
| V-04 | Output format (Investment Memo Acts + SLA Budget table) | Act I/II/III labeling + nested SLA Budget satisfies C-41+C-42 | PASS | PASS | — | 34/35 → 99.71 |
| V-05 | Phrasing register (formal, compact, all three axes) | All three axes in minimum token form satisfies C-41+C-42+C-43 | PASS | PASS | PASS | 35/35 → 100.00 |

---

## V-01 — Single-Axis: Inertia Sub-Part Labeling (C-41)

**Axis**: Inertia framing — explicit 1a / 1b / 1c internal structure added to the Inertia Assessment. Row descriptors cross-reference by sub-part label rather than section name.

**Hypothesis**: Labeling the three functional sub-divisions of the Inertia Assessment (framing / carrying cost / tipping point) and requiring row descriptors to reference "Step 1b" and "Step 1c" rather than just "the Inertia Assessment" satisfies C-41 without altering any other structural element.

---

You are a Commerce / distributed systems domain expert. Your task: simulate degraded conditions for {topic} across three structurally distinct failure classes. Produce a complete four-field failure scenario for each class, identify gaps, and assess inertia threat level.

---

### Step 1: Inertia Assessment

Complete all three sub-parts before beginning the scenario table. Sub-parts are labeled 1a / 1b / 1c. Row descriptors reference these sections by sub-part label — not by section name alone.

**Step 1a — Domain Fragility Framing**

Write 2–3 sentences establishing why {topic} in the commerce / distributed-systems domain is inherently fragile across all three failure classes: (1) client isolation creates invisible pending-state windows where in-flight transactions have no delivery signal; (2) distributed writes without idempotency produce duplicate side effects on retry; (3) concurrent node operation produces state divergence requiring business-level merge rules that are rarely pre-specified. Framing must be specific to {topic} — not generic.

**Step 1b — Per-Class Carrying Costs**

For each failure class, name the specific accumulating business consequence of inaction. Use rate / horizon / metric structure — all three components required per class.

- Class 1 (Connectivity Loss): [metric] accumulates at [rate qualifier — e.g., per-session, per-deploy] without [horizon qualifier — e.g., ceiling, bound]
- Class 2 (Data Consistency Violation): [metric] accumulates at [rate qualifier] [horizon qualifier]
- Class 3 (Split-Brain Conflict): [metric] accumulates at [rate qualifier] [horizon qualifier]

Examples: "cart-abandon events accumulate per intermittent-session without ceiling"; "oversell count compounds per deploy unbounded"; "reconciliation backlog grows per concurrent-checkout incident indefinitely." These metric names are the reference values for all Status Quo Risk column fills — do not author new values per row.

**Step 1c — Per-Class Tipping Point Signals**

For each failure class, specify the observable threshold at which deferral becomes indefensible. Each tipping point must include a quantified threshold expression AND a named metric being monitored. "Worsens over time" fails — quantified threshold required.

- Class 1 tipping point: [quantified threshold expression, e.g., "cart-abandon rate rises >2% above 30-day baseline"] — metric monitored: [named metric]
- Class 2 tipping point: [quantified threshold expression, e.g., "oversell-event count exceeds 50/month"] — metric monitored: [named metric]
- Class 3 tipping point: [quantified threshold expression, e.g., "reconciliation backlog exceeds 200 open items"] — metric monitored: [named metric]

---

### Anti-Omission Architecture

Five mechanisms prevent structural omission at five distinct levels. Each level targets a distinct risk. Each mechanism names a downstream artifact by exact section title.

| Level | Structural Unit | Mechanism | Artifact |
|-------|----------------|-----------|---------|
| Table | Entire output table | Unified row index (`#` column) + anti-split instruction | Output table (below) |
| Section | Table-to-Gap transition | Section-Level Phase Gate | Section Order Requirement (below) |
| Slot | Individual scenario row | In-Row Bold Imperatives + advance-inhibitor condition | Row Descriptors (below) |
| Column-Group | D-phase vs C-phase within a row | Intra-Row D-First Gate | Row Descriptors (below) |
| Column | Individual column | Column-Level Ownership Assignment | Column Contract (below) |

---

### Chaos Test Block Specification

Every scenario row is immediately followed by a Chaos Test Block co-located with that row. Each block contains four named components:

| Component | Fill Requirement |
|-----------|----------------|
| **Inject** | Named, reproducible failure condition activating the scenario. Specific to {topic} — not "network failure" but a named trigger (e.g., "TCP connection to inventory-service reset at 500ms with no retry budget remaining") |
| **Expected Behavior** | System response that should occur when failure is injected |
| **Pass Signal** | Named observable artifact confirming expected behavior occurred (log entry, metric value, or API response code) |
| **Fail Signal** | Named observable artifact confirming expected behavior did not occur |

All four components required per row. A chaos block missing any component fails the format requirement.

---

### Column Contract

Positioned before the scenario output table. Every output column must have a corresponding entry here.

| Name | Owner | Fill Requirement |
|------|-------|-----------------|
| `#` | — | Row index: 1, 2, 3 |
| Trigger Condition | D | **Threshold expression** (quantified activation condition) AND **detection signal** (how the system identifies the threshold being crossed). Both components required as distinct items. Qualitative-only descriptions fail. |
| Scenario Name | D | Named failure class: Class 1 Connectivity Loss / Class 2 Data Consistency Violation / Class 3 Split-Brain Conflict. Each must be distinct. |
| State | D | System configuration at failure onset (pre-failure state). Not the failure trigger — that is Trigger Condition. |
| Capability | C | What the user can still do during the failure, specific to {topic} commerce flows. |
| Data at Risk | C | What data may be lost, stale, or inconsistent. Name specific records or state fields. |
| Recovery Path | D+C | Four lifecycle stages, each with three components: **mechanism** (actor-chain prefixed: `client →`, `server →`, `operator →`, `user →`), **SLA target** (TTD / TTC / TTR / TTV), **Verification Signal** (named observable confirming stage completion — distinct from mechanism restatement). Stages: **Detect** (TTD) → **Contain** (TTC) → **Recover** (TTR) → **Validate** (TTV). At least 3 of 4 stages must carry a labeled actor-chain prefix. |
| Conflict Resolution | C | Canonical term only: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Free-text paraphrase fails — canonical term required as discrete label. |
| Status Quo Risk | C | **Must reference Step 1b by sub-part label.** Form: "Class N Step 1b carrying cost: [metric] accumulates at [rate], [horizon]." Do not author independently — draw from Step 1b. A fill that cites only "the Inertia Assessment" without the sub-part label (Step 1b) fails. |
| Severity / Blast Radius | C | Severity level (Degraded / Impaired / Down) and blast-radius estimate (segment or percentage affected). Both required. |

> **Constrained Conflict Resolution Vocabulary**: Permitted terms: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Free-text descriptions ("the most recent write wins", "reconcile manually") do not satisfy the constraint. The canonical term must appear as a discrete label in the cell.

---

### Anti-Boundary Instruction

**Do not split, divide, or boundary-insert the scenario table under any label. Specifically:**
1. Do not create separate tables for D-Expert columns and C-Expert columns — one unified table for all columns.
2. Do not insert a horizontal rule, heading, section break, or any divider between rows when column ownership shifts from D to C within a row.
3. Do not produce a standalone chaos section or standalone chaos-engineering table — each Chaos Test Block must appear immediately after its row, before the next row begins.
4. Do not produce a standalone observability section or standalone observability table — observability fields (Metric / Alert / Owner) must appear inline within each Gap Register finding.

---

### Section Order Requirement

Produce output in exactly this sequence:

1. **Step 1 Inertia Assessment** (sub-parts 1a / 1b / 1c) — complete before beginning the scenario table
2. **Scenario Table** — produce all three rows before writing any Gap Register content. Within each row: complete all D-owned columns first (D-first gate — do not begin any C-owned column until all D-owned columns for that row are complete), then complete all C-owned columns, then immediately write the row's Chaos Test Block. **Do not advance to Row N+1 until Row N's scenario columns AND its Chaos Test Block are both complete.**
3. **Gap Register** — produce all three findings before writing the Inertia Verdict
4. **Inertia Verdict** — after Gap Register
5. **Finding Completeness Checklist** — final section

Produce all 3 rows before writing the Gap Register.

---

### Row Descriptors

#### Row 1 — Class 1: Connectivity Loss

**Write this row now.** Failure class: client-side connectivity loss — the client cannot reach the server. Anchor to a specific {topic} commerce operation (checkout, cart persistence, payment initiation, or equivalent).

Consequence enumeration (write before filling columns):
- If no offline queue: cart contents lost on connection drop → customer-facing data loss, no recovery signal
- If naive retry without idempotency key: duplicate payment initiation on reconnect → double-charge
- If no pending-state signal: user cannot distinguish "processing" from "lost" → repeat submission risk

Chronic consequence: **Status Quo Risk = Class 1 Step 1b carrying cost** — use the metric and rate established in Step 1b. If this gap is never addressed, the metric named in Step 1b accumulates at the rate named in Step 1b without the ceiling named in Step 1b.

D-first gate: Write Trigger Condition, Scenario Name, State, Recovery Path (all four stages with mechanism + SLA + VS) before writing Capability, Data at Risk, Conflict Resolution, Status Quo Risk, Severity/Blast Radius.

**Do not advance to Row 2 until Row 1 contains non-placeholder content in every column, including all four Recovery Path stages each with labeled actor-chain mechanism, SLA target, and named Verification Signal, AND the Chaos Test Block for Row 1 (Inject / Expected Behavior / Pass Signal / Fail Signal) is complete.**

#### Row 2 — Class 2: Data Consistency Violation

**Write this row now.** Failure class: data consistency violation — the system processes a transaction that produces inconsistent state across storage (oversell, double-charge, phantom inventory, split-write outcome). This class is structurally distinct from Class 1 (no connectivity loss) and from Class 3 (no concurrent-node divergence — one node processes an operation against stale or incorrect state).

Consequence enumeration (write before filling columns):
- If no idempotency key: duplicate charge on retry → payment reconciliation required, dispute risk
- If oversell occurs: fulfillment impossible → cancel + refund triggered, SLA penalty exposure
- If phantom inventory: available signal on sold-out item → oversell on next checkout confirmation

Chronic consequence: **Status Quo Risk = Class 2 Step 1b carrying cost** — use the metric and rate established in Step 1b.

D-first gate: Write D-owned columns before C-owned columns.

**Do not advance to Row 3 until Row 2 contains non-placeholder content in every column, including all four Recovery Path stages each with labeled actor-chain mechanism, SLA target, and named Verification Signal, AND the Chaos Test Block for Row 2 is complete.**

#### Row 3 — Class 3: Split-Brain / Eventual Consistency Conflict

**Write this row now.** Failure class: split-brain or eventual-consistency conflict — two or more nodes independently process conflicting state updates that must later be reconciled. Structurally distinct from Class 2: requires concurrent multi-node operation and a reconciliation phase. Apply the constrained conflict-resolution vocabulary (`last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`) with a named business consequence per resolution outcome.

Consequence enumeration by resolution outcome (write before filling columns):
- `last-write-wins`: winning write survives, losing write discarded → may discard a fulfilled order or a legitimate reservation without signal
- `merge`: both writes applied via merge logic → undefined merge rules produce arbitrary state; defined merge may still yield an invalid inventory count
- `manual-reconcile`: operator resolves post-conflict → reconciliation backlog grows per incident at the rate named in Step 1b
- `reject-stale`: stale write rejected → customer receives "transaction not processed" without explanation

Chronic consequence: **Status Quo Risk = Class 3 Step 1b carrying cost** — use the metric and rate established in Step 1b.

D-first gate: Write D-owned columns before C-owned columns.

**Do not advance to the Gap Register until Row 3 contains non-placeholder content in every column, including all four Recovery Path stages each with labeled actor-chain mechanism, SLA target, and named Verification Signal, and the Conflict Resolution cell uses a canonical vocabulary term with an adequacy judgment citing the vocabulary constraint, AND the Chaos Test Block for Row 3 is complete.**

---

### Gap Register

Produce exactly three findings — one per required finding type. Observability fields must be inline with each finding. Do not produce a separate observability section.

**Finding format:**

```
[F-NN] [Finding type]: [Title]
Description: [Specific, actionable description — not generic]
Metric: [Named system or business metric]
Alert: [Named alert condition when metric threshold crossed]
Owner: [Responsible role — not "TBD"]
```

Required finding types (produce all three):
1. **Offline Experience Gap** — a specific user-facing capability absent under connectivity degradation
2. **Data Consistency Violation** — a specific scenario producing inconsistent state
3. **Missing Recovery Flow** — a specific recovery path absent or incomplete

**Finding types present: ___ of 3** ← fill this count after writing all three findings

---

### Inertia Verdict

After completing the Gap Register, synthesize gap findings and Step 1b carrying costs:

- **Inertia Threat Level**: HIGH / MEDIUM / LOW
- **Strongest argument against deferral** (2–3 sentences): Reference at least one Gap Register finding by its F-NN label and at least one Step 1b carrying cost by class. Name the tipping point signal from Step 1c that quantifies when deferral becomes indefensible.

---

### Finding Completeness Checklist

```
[ ] Offline Experience Gap finding present (F-__)
[ ] Data Consistency Violation finding present (F-__)
[ ] Missing Recovery Flow finding present (F-__)
Finding types present: ___ of 3
```

---

## V-02 — Single-Axis: SLA Budget Pre-Commitment (C-42)

**Axis**: Lifecycle emphasis — a dedicated pre-table SLA Budget step commits TTD / TTC / TTR / TTV values per failure class before any scenario row is written. The Column Contract Recovery Path entry names this section as the sole reference source for SLA fills.

**Hypothesis**: A named Step 2 SLA Budget containing a class × stage lookup table, with the Column Contract Recovery Path entry explicitly naming "Step 2 SLA Budget" as the reference source, satisfies C-42 without requiring sub-part labeling (C-41) or a Failure Signature column (C-43).

---

You are a Commerce / distributed systems domain expert. Simulate degraded conditions for {topic} across three failure classes. Produce a complete four-field failure scenario for each class, identify gaps, and assess inertia threat level.

---

### Step 1: Inertia Assessment

Establish per-class carrying costs and tipping point signals before the scenario table.

**Carrying Costs (Per Class)**

For each failure class, name the accumulating business consequence of inaction using rate / horizon / metric structure:
- Class 1 (Connectivity Loss): [metric] accumulates at [rate] [horizon]
- Class 2 (Data Consistency Violation): [metric] accumulates at [rate] [horizon]
- Class 3 (Split-Brain Conflict): [metric] accumulates at [rate] [horizon]

**Tipping Point Signals (Per Class)**

For each class, specify the quantified observable threshold at which deferral is indefensible. Threshold expression + named metric required per class. Qualitative-only statements fail.

---

### Step 2: SLA Budget

Pre-commit Recovery Path SLA targets before the scenario table. The scenario table must not author SLA values independently — all SLA fills must reference this budget by class.

| Failure Class | TTD (Time to Detect) | TTC (Time to Contain) | TTR (Time to Recover) | TTV (Time to Validate) |
|---|---|---|---|---|
| Class 1 — Connectivity Loss | [commit value, e.g., ≤2 min] | [commit value] | [commit value] | [commit value] |
| Class 2 — Data Consistency Violation | [commit value] | [commit value] | [commit value] | [commit value] |
| Class 3 — Split-Brain Conflict | [commit value] | [commit value] | [commit value] | [commit value] |

Fill all twelve cells with specific time commitments. "TBD" or blank cells fail. These values are the authoritative SLA reference for the Recovery Path column — per-row SLA invention is a contract violation against this table.

---

### Anti-Omission Architecture

| Level | Structural Unit | Mechanism | Artifact |
|-------|----------------|-----------|---------|
| Table | Entire output table | Unified row index + anti-split instruction | Output table (below) |
| Section | Table-to-Gap transition | Section-Level Phase Gate | Section Order Requirement (below) |
| Slot | Individual row | In-Row Bold Imperatives + advance-inhibitor | Row Descriptors (below) |
| Column-Group | D-phase vs C-phase within row | Intra-Row D-First Gate | Row Descriptors (below) |
| Column | Individual column | Column-Level Ownership Assignment | Column Contract (below) |

---

### Chaos Test Block Specification

| Component | Fill Requirement |
|-----------|----------------|
| **Inject** | Named, reproducible failure condition specific to {topic} |
| **Expected Behavior** | System response when failure is injected |
| **Pass Signal** | Named observable confirming expected behavior occurred |
| **Fail Signal** | Named observable confirming expected behavior did not occur |

All four required per row. Co-located immediately after its row, not in a separate chaos section.

---

### Column Contract

| Name | Owner | Fill Requirement |
|------|-------|-----------------|
| `#` | — | Row index: 1, 2, 3 |
| Trigger Condition | D | Threshold expression AND detection signal — both required as distinct components. Qualitative-only fails. |
| Scenario Name | D | Named failure class: Class 1 / Class 2 / Class 3. Each distinct. |
| State | D | System configuration at failure onset (pre-failure). Not the trigger. |
| Capability | C | What user can still do — specific to {topic} commerce flows. |
| Data at Risk | C | Named records or state fields at risk of loss, staleness, or inconsistency. |
| Recovery Path | D+C | Four stages: **Detect** / **Contain** / **Recover** / **Validate**. Each stage: mechanism (actor-chain prefixed: `client →`, `server →`, `operator →`, `user →`) + **SLA target from Step 2 SLA Budget (above) — reference by class row and stage column, do not author independently** + Verification Signal (named observable distinct from mechanism restatement). At least 3 of 4 stages must carry a labeled actor-chain prefix. |
| Conflict Resolution | C | Canonical term: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Free-text fails. |
| Status Quo Risk | C | Carrying cost of inaction from Step 1 — rate / horizon / metric structure. Draw from Step 1 carrying costs; do not author independently. |
| Severity / Blast Radius | C | Severity (Degraded / Impaired / Down) + blast-radius estimate. Both required. |

> **Constrained Conflict Resolution Vocabulary**: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Free-text descriptions fail. Canonical term as discrete label required.

---

### Anti-Boundary Instruction

**One unified table. No structural splits:**
1. Do not create separate tables for D-Expert columns and C-Expert columns.
2. Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts.
3. Do not produce a standalone chaos section or standalone chaos-engineering table — Chaos Test Block follows its row immediately.
4. Do not produce a standalone observability section — observability fields (Metric / Alert / Owner) are inline per Gap Register finding.

---

### Section Order Requirement

1. **Step 1 Inertia Assessment** — complete (carrying costs + tipping points) before Step 2
2. **Step 2 SLA Budget** — complete all twelve cells before beginning the scenario table
3. **Scenario Table** — all three rows, each with D-first gate then C-columns then Chaos Block, before Gap Register. **Do not advance to Row N+1 until Row N scenario columns AND its Chaos Test Block are complete.**
4. **Gap Register** — all findings before Inertia Verdict
5. **Inertia Verdict**
6. **Finding Completeness Checklist**

Produce all 3 rows before writing the Gap Register.

---

### Row Descriptors

#### Row 1 — Class 1: Connectivity Loss

**Write this row now.** Client cannot reach server. Anchor to a specific {topic} commerce operation.

Consequence enumeration:
- No offline queue → cart contents lost on drop, no recovery signal
- Naive retry without idempotency → double-charge on reconnect
- No pending-state signal → repeat submission risk

Chronic: Status Quo Risk = Class 1 carrying cost from Step 1 (rate + horizon + metric).

D-first gate: Trigger Condition → Scenario Name → State → Recovery Path (all four stages; **SLA targets from Step 2 SLA Budget, Class 1 row**) before Capability → Data at Risk → Conflict Resolution → Status Quo Risk → Severity/Blast Radius.

**Do not advance to Row 2 until Row 1 contains non-placeholder content in every column, including all four Recovery Path stages each with actor-chain mechanism, SLA target referencing Step 2 SLA Budget, and named Verification Signal, AND Row 1 Chaos Test Block is complete.**

#### Row 2 — Class 2: Data Consistency Violation

**Write this row now.** System processes a transaction producing inconsistent state (oversell, double-charge, phantom inventory). Distinct from Class 1 (no connectivity loss) and Class 3 (no concurrent-node divergence).

Consequence enumeration:
- No idempotency key → double-charge on retry → reconciliation required
- Oversell → fulfillment impossible → cancel/refund, SLA exposure
- Phantom inventory → oversell on next checkout confirmation

Chronic: Status Quo Risk = Class 2 carrying cost from Step 1.

D-first gate: All D-owned columns (SLA targets from Step 2 SLA Budget, Class 2 row) before C-owned columns.

**Do not advance to Row 3 until Row 2 contains non-placeholder content in every column, including all four Recovery Path stages with SLA targets referencing Step 2 SLA Budget, AND Row 2 Chaos Test Block is complete.**

#### Row 3 — Class 3: Split-Brain / Eventual Consistency Conflict

**Write this row now.** Two or more nodes process conflicting state updates requiring reconciliation. Distinct from Class 2 — requires concurrent multi-node operation and post-conflict reconciliation. Apply constrained conflict-resolution vocabulary.

Consequence by resolution outcome:
- `last-write-wins` → losing write discarded without signal; may discard fulfilled order
- `merge` → undefined merge rules produce arbitrary state
- `manual-reconcile` → backlog grows per incident
- `reject-stale` → customer receives unexplained rejection

Chronic: Status Quo Risk = Class 3 carrying cost from Step 1.

D-first gate: All D-owned columns (SLA targets from Step 2 SLA Budget, Class 3 row) before C-owned columns.

**Do not advance to Gap Register until Row 3 columns AND Chaos Test Block are complete, including Conflict Resolution using a canonical vocabulary term and Recovery Path SLA targets drawn from Step 2 SLA Budget Class 3 row.**

---

### Gap Register

Three findings, one per type. Observability inline. No separate observability section.

```
[F-NN] [Finding type]: [Title]
Description: [Specific, actionable]
Metric: [Named metric]
Alert: [Named alert condition]
Owner: [Named role]
```

Types required: Offline Experience Gap / Data Consistency Violation / Missing Recovery Flow.

**Finding types present: ___ of 3**

---

### Inertia Verdict

- **Inertia Threat Level**: HIGH / MEDIUM / LOW
- **Strongest argument against deferral** (2–3 sentences): Reference at least one Gap finding (F-NN label) and at least one Step 1 carrying cost by class.

---

### Finding Completeness Checklist

```
[ ] Offline Experience Gap (F-__)
[ ] Data Consistency Violation (F-__)
[ ] Missing Recovery Flow (F-__)
Finding types present: ___ of 3
```

---

## V-03 — Single-Axis: Failure Signature Column (C-43)

**Axis**: Role sequence — Failure Signature is the first D-phase column in the Column Contract. The D-expert commits to a behaviorally characterized failure fingerprint per row before writing State, Trigger Condition, or any C-phase column.

**Hypothesis**: Positioning Failure Signature first in the D-phase and requiring a fill specification of behavioral fingerprint with ≥2 named actor viewpoints — explicitly distinguished from Trigger Condition (entry threshold) and State (pre-failure config) — satisfies C-43 without requiring sub-part labeling (C-41) or SLA Budget (C-42).

---

You are a Commerce / distributed systems domain expert. Simulate degraded conditions for {topic} across three failure classes. Produce a complete four-field failure scenario for each class, identify gaps, and assess inertia threat level.

---

### Step 1: Inertia Assessment

Establish per-class carrying costs and tipping point signals before the scenario table.

**Carrying Costs**: For each of the three failure classes, name the accumulating business consequence of inaction. Rate / horizon / metric structure required (all three components per class).

**Tipping Point Signals**: For each class, specify the quantified observable threshold at which deferral becomes indefensible. Threshold expression + named metric required. "Worsens over time" fails.

---

### Anti-Omission Architecture

| Level | Structural Unit | Mechanism | Artifact |
|-------|----------------|-----------|---------|
| Table | Entire output table | Unified row index + anti-split | Output table (below) |
| Section | Table-to-Gap transition | Section-Level Phase Gate | Section Order Requirement (below) |
| Slot | Individual row | In-Row Bold Imperatives + advance-inhibitor | Row Descriptors (below) |
| Column-Group | D-phase vs C-phase within row | Intra-Row D-First Gate | Row Descriptors (below) |
| Column | Individual column | Column-Level Ownership Assignment | Column Contract (below) |

---

### Chaos Test Block Specification

| Component | Fill Requirement |
|-----------|----------------|
| **Inject** | Named, reproducible failure condition specific to {topic} |
| **Expected Behavior** | System response on failure injection |
| **Pass Signal** | Named observable confirming expected behavior |
| **Fail Signal** | Named observable confirming failure of expected behavior |

Co-located immediately after each row. Not in a separate chaos section.

---

### Column Contract

The Failure Signature column is positioned first in the D-phase. The model must commit to an operationally specific behavioral fingerprint per row before writing any other column — closing the scenario-drift escape where Class 2 and Class 3 both produce "service unavailable" fills without distinguishing telemetry.

| Name | Owner | Fill Requirement |
|------|-------|-----------------|
| `#` | — | Row index: 1, 2, 3 |
| **Failure Signature** | **D** | **Behavioral fingerprint WHILE the failure is in progress. NOT the entry threshold (that is Trigger Condition). NOT pre-failure configuration (that is State). Describe what the failure looks like to each system actor during the failure. Name at least two distinct actor viewpoints per row: `client view` / `server view`, or `node-A view` / `node-B view`, or `user view` / `operator view`. Each viewpoint must describe a specific observable: a named metric value, log pattern, connection behavior, or queue depth anomaly. Generic fills ("system unavailable", "service degraded") without named actors and specific observables fail.** Example for Class 1: "client view: repeated connection timeouts (TCP SYN→no ACK), request retry exhausted; server view: no inbound connection registered, request queue depth static." |
| Trigger Condition | D | Threshold expression (quantified activation condition) AND detection signal (how the system identifies threshold being crossed). Both required. Qualitative-only fails. The Trigger Condition bounds the ENTRY to the failure — when the failure starts. The Failure Signature (above) describes what happens DURING the failure. These are distinct. |
| Scenario Name | D | Named failure class: Class 1 / Class 2 / Class 3. Each distinct. |
| State | D | System configuration at failure onset — pre-failure configuration. Not the trigger, not the in-progress behavior (those are Trigger Condition and Failure Signature). |
| Capability | C | What user can still do during the failure. Specific to {topic} commerce flows. |
| Data at Risk | C | Named records or state fields at risk. |
| Recovery Path | D+C | Four stages (Detect / Contain / Recover / Validate) each with: mechanism (actor-chain prefix: `client →`, `server →`, `operator →`, `user →`) + SLA target (TTD / TTC / TTR / TTV) + named Verification Signal (observable distinct from mechanism restatement). At least 3 of 4 stages with labeled actor prefix. |
| Conflict Resolution | C | Canonical term: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Free-text fails. |
| Status Quo Risk | C | Carrying cost from Step 1. Rate / horizon / metric structure. Draw from Step 1 values. |
| Severity / Blast Radius | C | Severity (Degraded / Impaired / Down) + blast-radius estimate. Both required. |

> **Constrained Conflict Resolution Vocabulary**: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Free-text fails. Canonical term as discrete label required.

> **Failure Signature — Class Boundary Discriminator**: The three Failure Signature fills must be operationally distinct. Class 2 and Class 3 must not share the same observable fingerprint. Class 3 (split-brain) requires at least two node-perspective viewpoints (node-A / node-B) showing diverging state; Class 2 (consistency violation on a single transaction) requires client-or-user viewpoint showing a transaction-level anomaly. A Class 2 and Class 3 Failure Signature that both read "service returns 500 errors" without actor differentiation fails the class-boundary discriminator requirement.

---

### Anti-Boundary Instruction

**One unified table. No structural splits:**
1. Do not create separate tables for D-Expert columns and C-Expert columns.
2. Do not insert a horizontal rule, heading, or section break between rows when ownership shifts.
3. Do not produce a standalone chaos section or standalone chaos-engineering table.
4. Do not produce a standalone observability section — observability fields inline per Gap Register finding.

---

### Section Order Requirement

1. **Step 1 Inertia Assessment** — complete before scenario table
2. **Scenario Table** — all three rows. For each row: D-first gate (Failure Signature first, then Trigger Condition → Scenario Name → State → Recovery Path), then C-phase columns, then Chaos Test Block. **Do not advance to Row N+1 until Row N scenario columns AND Chaos Test Block are complete.**
3. **Gap Register** — all findings before Inertia Verdict
4. **Inertia Verdict**
5. **Finding Completeness Checklist**

---

### Row Descriptors

#### Row 1 — Class 1: Connectivity Loss

**Write this row now.** Client-side connectivity loss — client cannot reach server. Anchor to a specific {topic} commerce operation.

**Failure Signature first**: before writing Trigger Condition or State, write the Failure Signature for Class 1. Name at least two actor viewpoints describing what each observes while the failure is in progress. Example: "client view: connection attempt returns ETIMEDOUT after 30s, no server ACK received; server view: no request registered in access log, health probe returns 200 (server is healthy but unreachable from this client)."

Consequence enumeration:
- No offline queue → cart lost on drop, no recovery signal
- No idempotency key → double-charge on retry
- No pending-state signal → repeat submission

Chronic: Status Quo Risk = Class 1 carrying cost (rate + horizon + metric from Step 1).

D-first gate: Failure Signature → Trigger Condition → Scenario Name → State → Recovery Path (all four stages) before Capability → Data at Risk → Conflict Resolution → Status Quo Risk → Severity/Blast Radius.

**Do not advance to Row 2 until Row 1 contains non-placeholder content in every column including a Failure Signature with ≥2 named actor viewpoints, all four Recovery Path stages with actor-chain mechanism, SLA, and named VS, AND Row 1 Chaos Test Block is complete.**

#### Row 2 — Class 2: Data Consistency Violation

**Write this row now.** System processes a transaction producing inconsistent state. Distinct from Class 1 (no connectivity loss) and Class 3 (no concurrent-node divergence).

**Failure Signature first**: Class 2 Failure Signature must be operationally distinct from Class 1. Name the behavioral fingerprint for a consistency violation: what does the client see, what does the server-side transaction log show? Example: "client view: checkout returns HTTP 200 with order confirmation, but a second GET /order/{id} returns 404; server view: order-write succeeded on primary, replication lag caused read-your-own-writes violation on secondary."

Consequence enumeration:
- No idempotency key → double-charge on retry → reconciliation required
- Oversell → fulfillment impossible → cancel/refund, SLA exposure
- Phantom inventory → oversell on next confirmation

Chronic: Status Quo Risk = Class 2 carrying cost from Step 1.

D-first gate: Failure Signature → Trigger Condition → Scenario Name → State → Recovery Path before C-phase.

**Do not advance to Row 3 until Row 2 complete including Failure Signature with ≥2 named actor viewpoints distinct from Row 1, AND Row 2 Chaos Test Block complete.**

#### Row 3 — Class 3: Split-Brain / Eventual Consistency Conflict

**Write this row now.** Two or more nodes process conflicting updates requiring reconciliation. Distinct from Class 2 — requires concurrent multi-node operation. The Failure Signature must use node-A / node-B viewpoint framing to show diverging state on each node.

**Failure Signature first**: Class 3 must include two node viewpoints showing diverging state, not just a service-unavailable signal. Example: "node-A view: checkout completed with inventory decremented to 0, write committed; node-B view: inventory still shows 1 unit available (replication not yet received), second checkout accepted; observability view: no conflict event logged during window — divergence invisible until reconciliation job runs."

Consequence by resolution outcome:
- `last-write-wins` → losing write discarded silently; may discard fulfilled order
- `merge` → undefined merge rules → arbitrary state
- `manual-reconcile` → backlog grows per incident
- `reject-stale` → unexplained rejection to customer

Chronic: Status Quo Risk = Class 3 carrying cost from Step 1.

D-first gate: Failure Signature (node-A/node-B viewpoints) → Trigger Condition → Scenario Name → State → Recovery Path before C-phase.

**Do not advance to Gap Register until Row 3 complete including Failure Signature with ≥2 node viewpoints showing diverging state (not generic service-unavailable), Conflict Resolution using canonical vocabulary term, all four Recovery Path stages, AND Row 3 Chaos Test Block complete.**

---

### Gap Register

Three findings, one per type. Observability inline per finding. No separate observability section.

```
[F-NN] [Finding type]: [Title]
Description: [Specific, actionable]
Metric: [Named metric]
Alert: [Named alert condition]
Owner: [Named role]
```

**Finding types present: ___ of 3**

---

### Inertia Verdict

- **Inertia Threat Level**: HIGH / MEDIUM / LOW
- **Strongest argument against deferral** (2–3 sentences): Reference at least one Gap finding by F-NN label and at least one Step 1 carrying cost by class.

---

### Finding Completeness Checklist

```
[ ] Offline Experience Gap (F-__)
[ ] Data Consistency Violation (F-__)
[ ] Missing Recovery Flow (F-__)
Finding types present: ___ of 3
```

---

## V-04 — Dual-Axis: Investment Memo Acts + SLA Budget Table (C-41 + C-42)

**Axis**: Output format — the Inertia Assessment is structured as an Investment Memo using Act I / Act II / Act III labels (narrative register), with the SLA Budget rendered as a class × stage lookup table nested inside the memo. Both pre-commitment documents appear before the scenario table; row descriptors cross-reference by act label and SLA Budget class row.

**Hypothesis**: Act I / Act II / Act III internal labeling (narrative variant of C-41's 1a/1b/1c requirement) plus a nested SLA Budget table with Column Contract reference satisfies C-41 + C-42. Failure Signature column (C-43) is not present — only one new axis is being tested vs C-43.

---

You are a Commerce / distributed systems domain expert. Simulate degraded conditions for {topic} across three failure classes. Produce a complete four-field failure scenario for each class, identify gaps, and assess inertia threat level.

---

### Investment Memo: Pre-Committed Constraints for {topic} Resilience Analysis

Complete this memo before beginning the scenario table. The memo establishes three types of pre-committed constraints that the scenario table must draw from — not author independently.

---

**Act I — Domain Fragility Framing**

*(Functional role: establishes why this domain is inherently fragile — applies to all three failure classes. Source for the domain-context preamble in the Inertia Verdict.)*

Write 2–3 sentences establishing why {topic} in the commerce / distributed-systems domain is inherently fragile. Address the structural cause for each class: (1) client isolation creates an invisible pending-state window where in-flight transactions have no delivery signal; (2) distributed writes without idempotency produce duplicate side effects on retry without detection; (3) concurrent node operation produces state divergence requiring business-level merge rules that are rarely pre-specified. Specific to {topic}.

---

**Act II — Per-Class Carrying Costs**

*(Functional role: pre-commits the accumulating cost of inaction per class — source values for Status Quo Risk column fills. Row descriptors reference "Act II Class N carrying cost.")*

For each failure class, state the carrying cost in rate / horizon / metric form. All three components required.

- **Class 1 (Connectivity Loss)**: [metric] accumulates [rate qualifier — e.g., per-session] [horizon qualifier — e.g., without ceiling]
- **Class 2 (Data Consistency Violation)**: [metric] accumulates [rate qualifier] [horizon qualifier]
- **Class 3 (Split-Brain Conflict)**: [metric] accumulates [rate qualifier] [horizon qualifier]

---

**Act III — Per-Class Tipping Point Signals**

*(Functional role: pre-commits the observable exit condition per class — the threshold at which deferral is indefensible. Row descriptors may reference "Act III Class N tipping point.")*

For each class: quantified threshold expression + named metric being monitored. "Worsens over time" fails.

- **Class 1 tipping point**: [quantified threshold] — metric: [named metric]
- **Class 2 tipping point**: [quantified threshold] — metric: [named metric]
- **Class 3 tipping point**: [quantified threshold] — metric: [named metric]

---

**Act IV — SLA Budget**

*(Functional role: pre-commits Recovery Path SLA targets per failure class — source values for all Recovery Path SLA fills. The scenario table must not author SLA values independently; all SLA fills reference the corresponding cell in this table.)*

| Failure Class | TTD | TTC | TTR | TTV |
|---|---|---|---|---|
| Class 1 — Connectivity Loss | | | | |
| Class 2 — Data Consistency Violation | | | | |
| Class 3 — Split-Brain Conflict | | | | |

Fill all twelve cells with specific time commitments. "TBD" fails. This is the SLA Budget. Recovery Path column fills for SLA targets must cite "SLA Budget Act IV, Class N row" — not independently authored values.

---

### Anti-Omission Architecture

| Level | Structural Unit | Mechanism | Artifact |
|-------|----------------|-----------|---------|
| Table | Entire output table | Unified row index + anti-split | Output table (below) |
| Section | Table-to-Gap transition | Section-Level Phase Gate | Section Order Requirement (below) |
| Slot | Individual row | In-Row Bold Imperatives + advance-inhibitor | Row Descriptors (below) |
| Column-Group | D-phase vs C-phase within row | Intra-Row D-First Gate | Row Descriptors (below) |
| Column | Individual column | Column-Level Ownership Assignment | Column Contract (below) |

---

### Chaos Test Block Specification

| Component | Fill Requirement |
|-----------|----------------|
| **Inject** | Named, reproducible failure condition for {topic} |
| **Expected Behavior** | System response on injection |
| **Pass Signal** | Named observable confirming expected behavior |
| **Fail Signal** | Named observable confirming failure |

Co-located immediately after its row. Not a separate section.

---

### Column Contract

| Name | Owner | Fill Requirement |
|------|-------|-----------------|
| `#` | — | Row index: 1, 2, 3 |
| Trigger Condition | D | Threshold expression AND detection signal — both required. Qualitative fails. |
| Scenario Name | D | Named failure class: Class 1 / Class 2 / Class 3. Distinct. |
| State | D | Pre-failure system configuration. Not the trigger. |
| Capability | C | What user can still do — specific to {topic} commerce flows. |
| Data at Risk | C | Named records or state fields at risk. |
| Recovery Path | D+C | Four stages (Detect / Contain / Recover / Validate) each with: mechanism (actor-chain prefix: `client →`, `server →`, `operator →`, `user →`) + **SLA target — must reference SLA Budget Act IV above, citing class row and stage column; do not author independently** + named Verification Signal (observable, distinct from mechanism). ≥3 of 4 stages with labeled actor prefix. |
| Conflict Resolution | C | Canonical term: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Free-text fails. |
| Status Quo Risk | C | **Must reference Investment Memo Act II by act label.** Form: "Class N Act II carrying cost: [metric] accumulates [rate], [horizon]." A fill citing only "the Inertia Assessment" without the act label (Act II) fails. |
| Severity / Blast Radius | C | Severity (Degraded / Impaired / Down) + blast-radius estimate. Both required. |

> **Constrained Conflict Resolution Vocabulary**: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Free-text descriptions fail.

---

### Anti-Boundary Instruction

**One unified table:**
1. Do not create separate tables for D-Expert and C-Expert columns.
2. Do not insert a horizontal rule, heading, or section break between rows when ownership shifts.
3. Do not produce a standalone chaos section — Chaos Block follows its row immediately.
4. Do not produce a standalone observability section — observability fields inline per Gap Register finding.

---

### Section Order Requirement

1. **Investment Memo** (Acts I / II / III / IV) — complete all four acts before beginning scenario table
2. **Scenario Table** — all three rows. Each row: D-first gate (all D-owned columns before C-owned), then Chaos Block. **Do not advance to Row N+1 until Row N scenario columns AND Chaos Block are complete.**
3. **Gap Register** — all findings before Inertia Verdict
4. **Inertia Verdict**
5. **Finding Completeness Checklist**

---

### Row Descriptors

#### Row 1 — Class 1: Connectivity Loss

**Write this row now.** Client-side connectivity loss. Anchor to a specific {topic} commerce operation.

Consequence enumeration:
- No offline queue → cart lost, no recovery signal
- No idempotency key → double-charge on retry
- No pending-state signal → repeat submission risk

Chronic: **Status Quo Risk = Class 1 Act II carrying cost** — use metric/rate/horizon from Investment Memo Act II, Class 1.

D-first gate: Trigger Condition → Scenario Name → State → Recovery Path (SLA targets from **SLA Budget Act IV, Class 1 row**) before C-phase.

**Do not advance to Row 2 until Row 1 contains non-placeholder content in every column — Status Quo Risk citing Class 1 Act II by label, Recovery Path SLA targets citing SLA Budget Act IV Class 1 row, all four stages with actor mechanism and named VS — AND Row 1 Chaos Block is complete.**

#### Row 2 — Class 2: Data Consistency Violation

**Write this row now.** Inconsistent state produced by a transaction (oversell, double-charge, phantom inventory). Distinct from Class 1 and Class 3.

Consequence enumeration:
- No idempotency key → double-charge → reconciliation required
- Oversell → fulfillment impossible → cancel/refund, SLA exposure
- Phantom inventory → oversell on confirmation

Chronic: **Status Quo Risk = Class 2 Act II carrying cost** — from Investment Memo Act II, Class 2.

D-first gate: Trigger Condition → Scenario Name → State → Recovery Path (**SLA Budget Act IV, Class 2 row**) before C-phase.

**Do not advance to Row 3 until Row 2 complete, Status Quo Risk citing Class 2 Act II, Recovery Path SLA from Act IV Class 2, AND Row 2 Chaos Block complete.**

#### Row 3 — Class 3: Split-Brain / Eventual Consistency Conflict

**Write this row now.** Two or more nodes process conflicting updates. Concurrent multi-node operation + reconciliation phase. Constrained conflict-resolution vocabulary required.

Consequence by resolution outcome:
- `last-write-wins` → silent discard of losing write
- `merge` → undefined merge → arbitrary state
- `manual-reconcile` → backlog grows per incident (Act II Class 3 rate)
- `reject-stale` → unexplained rejection

Chronic: **Status Quo Risk = Class 3 Act II carrying cost** — from Investment Memo Act II, Class 3.

D-first gate: Trigger Condition → Scenario Name → State → Recovery Path (**SLA Budget Act IV, Class 3 row**) before C-phase.

**Do not advance to Gap Register until Row 3 complete — Status Quo Risk citing Class 3 Act II, Recovery Path SLA citing Act IV Class 3, Conflict Resolution with canonical vocabulary term and adequacy judgment, AND Row 3 Chaos Block complete.**

---

### Gap Register

Three findings, inline observability, no separate observability section.

```
[F-NN] [Finding type]: [Title]
Description: [Specific, actionable]
Metric: [Named metric]
Alert: [Named alert condition]
Owner: [Named role]
```

**Finding types present: ___ of 3**

---

### Inertia Verdict

- **Inertia Threat Level**: HIGH / MEDIUM / LOW
- **Strongest argument against deferral** (2–3 sentences): Reference at least one Gap finding (F-NN) and at least one Act II carrying cost by act label. Note the Act III tipping point threshold that quantifies when deferral becomes indefensible.

---

### Finding Completeness Checklist

```
[ ] Offline Experience Gap (F-__)
[ ] Data Consistency Violation (F-__)
[ ] Missing Recovery Flow (F-__)
Finding types present: ___ of 3
```

---

## V-05 — Triple-Axis: All Three New Criteria, Compact Form (C-41 + C-42 + C-43)

**Axis**: Phrasing register — formal/technical, maximum pre-commitment density, minimum structural redundancy. All three new axes integrated into a single unified pre-commitment document. Compact: every element earns its place; no criterion is satisfied by prose when a structured entry can do it.

**Hypothesis**: Integrating all three axes (1a/1b/1c sub-part labeling, SLA Budget as a class × stage table positioned as Step 1d, and Failure Signature as the first D-phase column with actor-differentiated fill requirement) in a compact, formally specified prompt satisfies C-41 + C-42 + C-43 simultaneously, achieving the full 35/35 ceiling.

---

You are a Commerce / distributed systems domain expert. Task: simulate degraded conditions for {topic} across three failure classes. Produce one complete four-field scenario per class, identify gaps, and assess inertia threat level.

---

### Step 1: Pre-Commitment Document

Four named sub-parts. Complete all before the scenario table. The scenario table must draw from these sub-parts — per-row independent authoring of values established here is a contract violation.

**Step 1a — Domain Fragility Framing** *(Context — applies to all three classes)*

2–3 sentences. Why is {topic} in the commerce / distributed-systems domain inherently fragile? Address all three classes: (1) client isolation creates invisible pending-state windows; (2) distributed writes without idempotency produce duplicate side effects; (3) concurrent node operation produces diverging state requiring pre-specified merge rules. Specific to {topic}.

**Step 1b — Per-Class Carrying Costs** *(Rate / horizon / metric per class — source for Status Quo Risk column)*

| Failure Class | Metric | Rate Qualifier | Horizon Qualifier |
|---|---|---|---|
| Class 1 — Connectivity Loss | [named metric] | [rate, e.g., per-session] | [horizon, e.g., without ceiling] |
| Class 2 — Data Consistency Violation | [named metric] | [rate] | [horizon] |
| Class 3 — Split-Brain Conflict | [named metric] | [rate] | [horizon] |

Status Quo Risk column fills **must reference this table by sub-part label and class** — e.g., "Class 1 Step 1b carrying cost: [metric] accumulates [rate], [horizon]." A fill citing only "the Inertia Assessment" without "Step 1b" fails.

**Step 1c — Per-Class Tipping Point Signals** *(Quantified exit condition — source for Inertia Verdict)*

| Failure Class | Threshold Expression | Named Metric Monitored |
|---|---|---|
| Class 1 | [quantified, e.g., "cart-abandon rate >2% above 30-day baseline"] | [named metric] |
| Class 2 | [quantified] | [named metric] |
| Class 3 | [quantified] | [named metric] |

Qualitative thresholds ("worsens over time") fail. All three rows required.

**Step 1d — SLA Budget** *(Pre-committed Recovery Path SLA targets — source for Recovery Path column)*

| Failure Class | TTD | TTC | TTR | TTV |
|---|---|---|---|---|
| Class 1 — Connectivity Loss | | | | |
| Class 2 — Data Consistency Violation | | | | |
| Class 3 — Split-Brain Conflict | | | | |

Fill all twelve cells with specific time commitments. Recovery Path SLA fills **must reference this table by class row and stage column** — e.g., "TTD: per Step 1d Class 1 budget." Per-row SLA invention is a contract violation.

---

### Anti-Omission Architecture

| Level | Structural Unit | Mechanism | Artifact |
|-------|----------------|-----------|---------|
| Table | Entire output table | Unified `#` index + anti-split | Output table (below) |
| Section | Table → Gap boundary | Section-Level Phase Gate | Section Order Requirement (below) |
| Slot | Individual row | Bold write-imperative + advance-inhibitor | Row Descriptors (below) |
| Column-Group | D-phase vs C-phase within row | D-First Gate | Row Descriptors (below) |
| Column | Individual column | Column-Level Ownership | Column Contract (below) |

---

### Chaos Test Block Specification

| Component | Fill Requirement |
|-----------|----------------|
| **Inject** | Named, reproducible failure condition specific to {topic} — not "network failure" |
| **Expected Behavior** | System response on injection |
| **Pass Signal** | Named observable confirming expected behavior |
| **Fail Signal** | Named observable confirming failure |

Co-located immediately after its row. Not a separate section or table.

---

### Column Contract

All output columns. D = Distributed Systems Expert. C = Commerce Expert.

| Name | Owner | Fill Requirement |
|------|-------|-----------------|
| `#` | — | 1, 2, 3 |
| **Failure Signature** | **D** | **Behavioral fingerprint WHILE the failure is in progress. NOT the entry threshold (Trigger Condition, below). NOT pre-failure config (State, below). Name ≥2 actor viewpoints per row — e.g., `client view` / `server view`, or `node-A view` / `node-B view`. Each viewpoint: named observable (metric value, log pattern, queue depth, connection behavior) during the failure. Generic fills without actor differentiation ("system unavailable") fail. Class 2 and Class 3 Failure Signatures must be operationally distinct — Class 3 requires node-A / node-B framing showing diverging state.** |
| Trigger Condition | D | Threshold expression (quantified) AND detection signal — both as distinct items. Qualitative-only fails. Bounds entry to the failure; distinct from Failure Signature (in-progress fingerprint). |
| Scenario Name | D | Class 1 / Class 2 / Class 3. Each class structurally distinct. |
| State | D | Pre-failure system configuration — not the trigger, not the in-progress fingerprint. |
| Capability | C | What the user can still do during the failure — {topic}-specific commerce operations. |
| Data at Risk | C | Named records or state fields at risk (loss / staleness / inconsistency). |
| Recovery Path | D+C | Stages: **Detect (TTD) → Contain (TTC) → Recover (TTR) → Validate (TTV)**. Each stage: mechanism (`client →`, `server →`, `operator →`, `user →` prefix) + **SLA target from Step 1d, class row, stage column** + named Verification Signal (observable, distinct from mechanism). ≥3 of 4 stages with labeled actor prefix. |
| Conflict Resolution | C | Canonical term: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Free-text fails. |
| Status Quo Risk | C | **Reference Step 1b by sub-part label and class.** Form: "Class N Step 1b carrying cost: [metric] [rate] [horizon]." Citing only "the Inertia Assessment" without "Step 1b" fails. |
| Severity / Blast Radius | C | Severity (Degraded / Impaired / Down) + blast-radius. Both required. |

> **Constrained Conflict Resolution Vocabulary**: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Free-text fails. Canonical term as discrete label.

> **Failure Signature — Class Boundary Discriminator**: Class 2 shows a transaction-level anomaly from a single write path (client view + server/log view). Class 3 shows concurrent-node state divergence (node-A view + node-B view + optional observability view showing absence of conflict event). A Failure Signature that applies to both Class 2 and Class 3 without actor differentiation fails.

---

### Anti-Boundary Instruction

**One unified table — four consolidation escape routes closed simultaneously:**
1. No separate tables for D-Expert columns and C-Expert columns.
2. No horizontal rule, heading, or section break between rows when ownership shifts within a row.
3. No standalone chaos section or standalone chaos-engineering table — each Chaos Test Block is co-located immediately after its row.
4. No standalone observability section or standalone observability table — observability fields (Metric / Alert / Owner) are inline within each Gap Register finding.

---

### Section Order Requirement

1. **Step 1 Pre-Commitment Document** (1a / 1b / 1c / 1d) — all four sub-parts complete before the scenario table
2. **Scenario Table** — all three rows in sequence. Per row: write Failure Signature first, then remaining D-phase columns (Trigger Condition → Scenario Name → State → Recovery Path), then C-phase columns (Capability → Data at Risk → Conflict Resolution → Status Quo Risk → Severity/Blast Radius), then the row's Chaos Test Block. **Do not advance to Row N+1 until Row N scenario columns AND its Chaos Test Block are both complete.**
3. **Gap Register** — all three findings before the Inertia Verdict
4. **Inertia Verdict** — after Gap Register
5. **Finding Completeness Checklist** — final

---

### Row Descriptors

#### Row 1 — Class 1: Connectivity Loss

**Write this row now.** Client cannot reach server. Anchor to a specific {topic} commerce operation (checkout, cart persistence, payment initiation, or equivalent).

Failure Signature instruction: Write the Class 1 Failure Signature first. At minimum: `client view` describing what the client observes (connection behavior, timeout pattern, error signal) + `server view` or `operator view` describing what is observable server-side during the same failure window. Both views must name specific observables, not generic descriptions.

Consequence enumeration (write before filling columns):
- No offline queue → cart contents lost on drop, no recovery signal
- No idempotency key → double-charge on reconnect
- No pending-state signal → user repeats submission believing prior attempt failed

Chronic: **Status Quo Risk = Class 1 Step 1b carrying cost** — use metric, rate, and horizon from Step 1b Class 1 row.

D-first gate: Failure Signature → Trigger Condition → Scenario Name → State → Recovery Path (**SLA targets from Step 1d, Class 1 row**) before Capability → Data at Risk → Conflict Resolution → Status Quo Risk (citing Step 1b Class 1) → Severity/Blast Radius.

**Do not advance to Row 2 until Row 1 contains non-placeholder content in every column — Failure Signature with ≥2 named actor viewpoints, Trigger Condition with threshold expression + detection signal, Status Quo Risk citing Step 1b Class 1 by sub-part label, Recovery Path SLA targets citing Step 1d Class 1 by sub-part label, all four stages with actor-chain mechanism and named VS — AND Row 1 Chaos Test Block (Inject / Expected Behavior / Pass Signal / Fail Signal) is complete.**

#### Row 2 — Class 2: Data Consistency Violation

**Write this row now.** System processes a transaction producing inconsistent state (oversell, double-charge, phantom inventory, or equivalent). Distinct from Class 1 (no connectivity loss) and Class 3 (no concurrent-node divergence — a single write path produces an incorrect outcome against existing state).

Failure Signature instruction: Class 2 Failure Signature must be distinct from Class 1 and must use transaction-level viewpoints. Name what the client sees (e.g., HTTP 200 on a write that produced an incorrect outcome) and what a server-side log or consistency check shows (e.g., inventory count at -1, idempotency key absent from deduplication store). Both viewpoints must name specific observables.

Consequence enumeration:
- No idempotency key → double-charge on retry → dispute and reconciliation required
- Oversell → fulfillment impossible → cancel/refund, SLA breach exposure
- Phantom inventory → oversell on checkout confirmation

Chronic: **Status Quo Risk = Class 2 Step 1b carrying cost** — from Step 1b Class 2 row.

D-first gate: Failure Signature → Trigger Condition → Scenario Name → State → Recovery Path (**Step 1d, Class 2 row**) before C-phase.

**Do not advance to Row 3 until Row 2 complete — Failure Signature with ≥2 viewpoints distinct from Row 1, Status Quo Risk citing Step 1b Class 2, Recovery Path SLA from Step 1d Class 2 — AND Row 2 Chaos Block complete.**

#### Row 3 — Class 3: Split-Brain / Eventual Consistency Conflict

**Write this row now.** Two or more nodes process conflicting state updates requiring reconciliation. Requires concurrent multi-node operation — structurally distinct from Class 2. Failure Signature must use node-A / node-B framing showing diverging committed state on each node. Apply constrained conflict-resolution vocabulary.

Failure Signature instruction: Class 3 Failure Signature must show diverging state across nodes, not a service-unavailable signal. Use `node-A view` (what node-A has committed) + `node-B view` (what node-B has committed, diverging from A) + optionally `observability view` (e.g., no conflict event logged — divergence invisible). All three node views name specific state values, not generic descriptions.

Consequence by resolution outcome:
- `last-write-wins` → losing write discarded silently; may discard a fulfilled order without customer notification
- `merge` → undefined merge rules produce arbitrary inventory state; defined merge may still yield invalid count
- `manual-reconcile` → reconciliation backlog grows per incident at the rate committed in Step 1b Class 3
- `reject-stale` → customer receives unexplained rejection; re-submission risks duplicate

Chronic: **Status Quo Risk = Class 3 Step 1b carrying cost** — from Step 1b Class 3 row.

D-first gate: Failure Signature (node-A/node-B viewpoints showing diverging state) → Trigger Condition → Scenario Name → State → Recovery Path (**Step 1d, Class 3 row**) before C-phase.

**Do not advance to Gap Register until Row 3 complete — Failure Signature with ≥2 node viewpoints showing distinct committed state on each node, Status Quo Risk citing Step 1b Class 3 by sub-part label, Recovery Path SLA from Step 1d Class 3, Conflict Resolution with canonical vocabulary term and adequacy judgment, all four Recovery Path stages with actor mechanism + SLA + named VS — AND Row 3 Chaos Block complete.**

---

### Gap Register

Three findings — one per required type. Observability fields inline with each finding. No separate observability section.

```
[F-NN] [Finding type]: [Title]
Description: [Specific, actionable — not generic]
Metric: [Named metric to monitor]
Alert: [Named alert condition — not "TBD"]
Owner: [Named responsible role]
```

Required types: **Offline Experience Gap** / **Data Consistency Violation** / **Missing Recovery Flow**

**Finding types present: ___ of 3** ← fill after writing all findings

---

### Inertia Verdict

After completing the Gap Register, produce:

- **Inertia Threat Level**: HIGH / MEDIUM / LOW
- **Strongest argument against deferral** (2–3 sentences): Reference at least one Gap finding by F-NN label, at least one Step 1b carrying cost by class and sub-part label, and at least one Step 1c tipping point threshold as the quantified exit condition.

---

### Finding Completeness Checklist

```
[ ] Offline Experience Gap present (F-__)
[ ] Data Consistency Violation present (F-__)
[ ] Missing Recovery Flow present (F-__)
Finding types present: ___ of 3
```
