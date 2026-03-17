# flow-resilience — Round 5 Variations (V-01 through V-05)

---

## V-01 — Role Sequence: Commerce-First

**Axis**: Role sequence  
**Hypothesis**: Leading with the Commerce Domain Expert (who establishes domain-grounded failure scenarios) before the Distributed Systems Expert (who validates technical accuracy) produces better-anchored scenarios and reduces generic distributed-systems boilerplate in the State field.

---

You are running the flow-resilience signal for topic: `{{topic}}`.

**Roles (run in this sequence)**

1. **Commerce Domain Expert** — You understand e-commerce operations deeply: checkout flows, cart state management, inventory reservation windows, payment gateway interactions, order fulfillment pipelines, and the business consequences of each failure. Run first to establish grounded failure scenarios.
2. **Distributed Systems Expert** — You understand CAP theorem trade-offs, retry semantics, idempotency requirements, conflict-resolution strategies, and eventual consistency patterns. Run second to validate technical accuracy and enrich recovery paths.

---

### Commerce Domain Expert Pass

Identify three failure scenarios for `{{topic}}`, one from each resilience class:

- **Class 1 — Full Client Offline**: The user's device loses all network connectivity during a commerce operation.
- **Class 2 — Partial Service Failure**: One or more downstream services (inventory, payment, fulfillment) become unavailable while the client remains connected.
- **Class 3 — Eventual Consistency / Split-Brain**: Concurrent writes from multiple clients or nodes create conflicting state that must be resolved.

Anchor each scenario to a specific commerce operation (checkout, inventory reservation, payment processing, order fulfillment). Generic CRUD descriptions are not acceptable.

For each scenario, draft initial content for four fields:

- **State**: What is the system state when the failure occurs?
- **Capability**: What can the user still do?
- **Data at Risk**: What data may be lost, stale, or inconsistent?
- **Recovery Path**: How does the system return to a healthy state?

---

### Distributed Systems Expert Pass

Review each scenario drafted by the Commerce Domain Expert. For each:

1. Confirm or correct the State description using precise distributed systems terminology (partitioned, degraded, split-brain, consistency level in effect).
2. Validate the Recovery Path against known patterns (saga rollback, idempotent retry, read-repair, last-write-wins, vector clock resolution).
3. Add a **Severity** classification: degraded / impaired / down.
4. Add a **Blast Radius** estimate: which user segment is affected and at what scale.
5. Flag any CAP theorem inconsistency, impossible consistency guarantee, or fabricated protocol name.

---

### Output: Scenario Analysis Table

Produce a single unified table with columns:

| # | Scenario | Class | State | Capability | Data at Risk | Recovery Path | Severity | Blast Radius |

Every scenario must appear in this table. Do not split the table by scenario class or by expert role.

---

### Output: Gap Register

After the table, produce three labeled findings:

**Offline Experience Gap** — What specific capability is unavailable when `{{topic}}` operates with no network? Name the missing affordance and the user impact.

**Data Consistency Violation** — Name a specific entity, field, or reservation window where two concurrent writes could produce irreconcilable state. State what the system currently does (if anything) and why it is insufficient.

**Missing Recovery Flow** — Name a failure entry point in `{{topic}}` that has no documented recovery exit. Describe what a complete recovery flow would require.

Each finding must be labeled, specific, and anchored to `{{topic}}`. Generic statements fail.

---

**Signal artifact**: Write output to `{{topic}}-flow-resilience-{{date}}.md`.

---

---

## V-02 — Output Format: Column-Ownership Table

**Axis**: Output format  
**Hypothesis**: Assigning explicit expert-role ownership to each table column — printed in the column header — prevents the model from omitting columns when ownership transitions mid-row, and anchors each field to the correct domain knowledge base.

---

You are running the flow-resilience signal for topic: `{{topic}}`.

**Expert roles**: Commerce Domain Expert (C) | Distributed Systems Expert (D)

---

### Instructions

Simulate degraded conditions across three resilience classes for `{{topic}}`:

- **Class 1 — Full Client Offline**
- **Class 2 — Partial Service Failure**
- **Class 3 — Eventual Consistency / Split-Brain**

For each class, produce one scenario row in the analysis table below.

---

### Scenario Analysis Table

The table has eight columns. Each column carries an explicit owner:

| Column | Owner | Fill Requirement |
|--------|-------|-----------------|
| # | — | Row number. |
| Scenario | Both | Name the failure event and the specific commerce operation affected (checkout, inventory, payment, fulfillment). |
| State | D | Describe the exact system state using distributed systems vocabulary. Name the partition state, service health, and any consistency guarantee in effect. |
| Capability | C | List every action the user can still take. Be specific to the commerce flow in progress. "User can retry" without specifying preserved state is insufficient. |
| Data at Risk | C | Name specific entities at risk: which fields, which records, which reservation windows. State the staleness or conflict window where measurable. |
| Recovery Path | D | Name the recovery pattern (saga rollback, idempotent retry, read-repair, LWW, vector clock). State the trigger, the steps, and the terminal healthy state. |
| Severity | D | One of: degraded / impaired / down. |
| Blast Radius | C | Name the affected user segment and scale (all users / checkout-active users / <1% under split-brain). |

**Column ownership is not a table boundary.** Do not create separate tables for Commerce Expert columns and Distributed Systems Expert columns. All eight columns appear in every row of a single unified table. Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts.

**Produce all three rows before writing the Gap Register.** No cell may be empty or placeholder.

---

### Gap Register

After the table, identify three findings:

**Offline Experience Gap**: Name the specific capability unavailable when `{{topic}}` has no network. Name the missing affordance and the user impact.

**Data Consistency Violation**: Name the specific entity and field where concurrent writes produce irreconcilable state. State the missing resolution policy and the business consequence (oversell, double-charge, duplicate fulfillment).

**Missing Recovery Flow**: Name the failure entry point in `{{topic}}` that has no documented exit. State what a complete recovery flow would require.

Each finding must be labeled, specific, and anchored to `{{topic}}`.

---

**Signal artifact**: Write output to `{{topic}}-flow-resilience-{{date}}.md`.

---

---

## V-03 — Phrasing Register: Imperative Direct

**Axis**: Phrasing register  
**Hypothesis**: Replacing descriptive guidance with direct second-person imperatives reduces interpretive slack, produces denser output, and prevents the model from satisfying the letter of a criterion with a weak paraphrase.

---

You are running the flow-resilience signal for topic: `{{topic}}`.

You are a Commerce / Distributed Systems expert. You know checkout flows, inventory reservation windows, payment gateway interactions, order fulfillment pipelines, CAP theorem trade-offs, retry semantics, idempotency requirements, and conflict-resolution strategies.

---

### Step 1 — Name three failure scenarios

Name one scenario per class. Anchor each to a named commerce operation.

- **Scenario A**: A full client-offline event during a `{{topic}}` commerce operation. Name the operation (checkout, cart submission, payment confirmation, order placement).
- **Scenario B**: A downstream service failure while the `{{topic}}` client is connected. Name the service (inventory service, payment gateway, fulfillment orchestrator).
- **Scenario C**: A concurrent-write event creating conflicting state in a `{{topic}}` commerce entity. Name the entity (inventory count, cart total, order status).

Do not use abstract or domain-agnostic descriptions. If you cannot name the operation or entity, choose the most realistic one for `{{topic}}`.

---

### Step 2 — Fill the scenario table

Produce this table. Fill all three rows before advancing.

| # | Scenario | State | Capability | Data at Risk | Recovery Path | Severity | Blast Radius |
|---|----------|-------|------------|--------------|---------------|----------|--------------|
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |

Fill requirements:

- **State**: Name the exact failure state. Use distributed systems vocabulary. Name the partition, the consistency guarantee in effect, and what each side holds.
- **Capability**: List every action still possible. List every action that is blocked. Be exhaustive.
- **Data at Risk**: Name each field, record, or reservation window at risk. State the staleness or conflict window.
- **Recovery Path**: Name the pattern. State the trigger. Walk each step. State the terminal state.
- **Severity**: Choose one: degraded / impaired / down.
- **Blast Radius**: Name the affected segment. State a percentage or qualifier.

Place all three rows in one table. Do not start a new table for each scenario.

---

### Step 3 — Write the Gap Register

Write exactly three findings. Use these labels exactly:

**Offline Experience Gap**: Name the missing capability. Name the user action that fails silently or without feedback. State what a minimal offline-capable design would require.

**Data Consistency Violation**: Name the entity. Name the conflict. State what resolution policy is absent. Name the business consequence.

**Missing Recovery Flow**: Name the entry point. Describe how a user or system could be stuck indefinitely. State the minimum recovery flow required to close the gap.

Do not write generic findings. Each finding must name a specific entity, field, or flow in `{{topic}}`.

---

### Step 4 — Self-check before output

Verify before writing the artifact:

- [ ] Three scenario classes present, each in a distinct row
- [ ] All eight columns filled in every row — no empty cells, no "N/A"
- [ ] No distributed systems claim is technically incorrect (no impossible consistency guarantees, no fabricated protocols)
- [ ] At least two scenarios reference a named commerce operation
- [ ] All three gap types present, labeled, and specific

Only emit the signal artifact after all checks pass.

---

**Signal artifact**: Write output to `{{topic}}-flow-resilience-{{date}}.md`.

---

---

## V-04 — Combined: Role Sequence + Lifecycle Emphasis

**Axes**: Role sequence + lifecycle emphasis  
**Hypothesis**: Running four roles in strict lifecycle order (discovery → state analysis → recovery design → gap synthesis) and allocating proportional phase space to each lifecycle phase produces structurally complete output with no phase collapsed or merged into another.

---

You are running the flow-resilience signal for topic: `{{topic}}`.

Four roles run in lifecycle order. Each role owns a distinct phase. Complete each phase in full before advancing to the next.

---

### Phase 1 — Failure Discovery (Commerce Domain Expert)

You know `{{topic}}`'s commerce flows. Identify where failures can enter.

Name three failure events, one per resilience class:

| # | Class | Failure Event | Commerce Operation | Entry State |
|---|-------|---------------|--------------------|-------------|
| 1 | Full Client Offline | [name the event] | [checkout / cart / payment / fulfillment] | [what was in progress at failure] |
| 2 | Partial Service Failure | [name the event and the failing service] | [name the operation in flight] | [what was in progress at failure] |
| 3 | Eventual Consistency | [name the event and the conflicting operation] | [name the concurrent operation] | [what was in progress at failure] |

**Phase 1 gate ✓**: All three rows filled with named events and named commerce operations. Do not advance to Phase 2 until this table is complete.

---

### Phase 2 — State and Impact Analysis (Distributed Systems Expert)

For each failure event from Phase 1, describe the exact system state and user impact.

| # | Scenario | State | Capability | Data at Risk |
|---|----------|-------|------------|--------------|
| 1 | [Phase 1 row 1] | [partition state, service health, consistency guarantee in effect] | [what user can do; what is blocked] | [named entities, staleness or conflict window] |
| 2 | [Phase 1 row 2] | … | … | … |
| 3 | [Phase 1 row 3] | … | … | … |

Fill requirements:
- **State**: Use CAP theorem vocabulary. Name which partition is isolated. Name the consistency guarantee (strong / eventual / causal).
- **Capability**: Name every user action still possible. Name every action that is blocked.
- **Data at Risk**: Name specific fields and records. State the conflict or staleness window.

**Phase 2 gate ✓**: All three rows complete with non-trivial State, Capability, and Data at Risk. Do not advance to Phase 3 until this table is complete.

---

### Phase 3 — Recovery Design (Recovery Architect)

For each scenario, design the full recovery path.

| # | Scenario | Recovery Pattern | Trigger | Steps | Terminal State | Severity | Blast Radius |
|---|----------|-----------------|---------|-------|----------------|----------|--------------|
| 1 | [Scenario A] | [saga / idempotent retry / read-repair / LWW / vector clock] | [what triggers recovery] | [numbered steps] | [final healthy state] | [degraded / impaired / down] | [affected segment and scale] |
| 2 | [Scenario B] | … | … | … | … | … | … |
| 3 | [Scenario C] | … | … | … | … | … | … |

Fill requirements:
- **Recovery Pattern**: Name the canonical pattern. Do not invent one.
- **Trigger**: Name the signal that starts recovery (timeout, reconnect event, reconciliation job, operator action).
- **Steps**: Number each step. Include the idempotency key or saga ID used for replay where applicable.
- **Terminal State**: Describe the final consistent state, not just "system recovered."

**Phase 3 gate ✓**: All three rows complete with named pattern, explicit trigger, and described terminal state. Do not advance to Phase 4 until this table is complete.

---

### Phase 4 — Gap Analysis (Commerce Domain Expert + Distributed Systems Expert)

With all scenarios analyzed and recovery paths designed, identify the residual gaps.

**Offline Experience Gap**: Name a specific capability in `{{topic}}` that is unavailable offline and has no degraded fallback. Name the user action that fails and the business impact.

**Data Consistency Violation**: Name a specific entity where concurrent writes produce irreconcilable state and Phase 3 recovery is insufficient or absent. State what resolution policy is missing.

**Missing Recovery Flow**: Name a failure entry point that Phase 3 could not fully close. State what component, policy, or orchestration step is missing.

**Phase 4 gate ✓**: All three gap types present, labeled, and anchored to `{{topic}}`. This is the final phase.

---

### Final Output

Merge Phases 2, 3, and 4 into a single consolidated artifact:

1. A unified scenario table combining columns from Phases 2 and 3: Scenario | State | Capability | Data at Risk | Recovery Path | Severity | Blast Radius
2. The Gap Register from Phase 4

Do not emit the per-phase scratch tables in the final artifact.

**Signal artifact**: Write output to `{{topic}}-flow-resilience-{{date}}.md`.

---

---

## V-05 — Combined: Four-Level Anti-Omission Architecture + Symptom Negations + In-Row Imperatives

**Axes**: Output format + anti-omission architecture  
**Hypothesis**: Explicitly naming all four structural levels of the anti-omission stack (table, section, slot, column), including at least two symptom-level negations in the anti-boundary instruction, and embedding bold **"Write this row now."** / **"Do not advance to row N until [condition]."** imperatives inside the Content field descriptor of each scenario row achieves the C-21/C-22/C-23 ceiling.

---

You are running the flow-resilience signal for topic: `{{topic}}`.

**Expert role**: Commerce / Distributed Systems expert. You understand checkout flows, inventory reservation windows, payment gateway interactions, order fulfillment pipelines, CAP theorem trade-offs, retry semantics, idempotency requirements, and conflict-resolution strategies.

---

## Anti-Omission Architecture

This prompt uses a **four-level anti-omission architecture**. Each level targets a distinct omission risk at a distinct structural level. No two levels duplicate each other.

| Level | Mechanism | Omission risk addressed |
|-------|-----------|------------------------|
| **Table level** | Unified scenario index — all three scenario rows in one numbered table | A scenario omitted silently when fragmented output creates an unlabeled gap |
| **Section level** | Phase gate — explicit ✓ checkpoint before the Gap Register section | The Gap Register section skipped when the model infers "complete" from the scenario table |
| **Slot level** | In-row bold imperatives — **Write this row now.** embedded inside the Content field descriptor of each scenario row | A row skipped when the model reads the section gate or table preamble as license to continue without filling that specific row |
| **Column level** | Ownership markers — each column header names the responsible expert role | A column omitted when the ownership transition within a row is misread as a structural table boundary |

---

## Anti-Boundary Instruction

All three scenarios appear in a **single unified table**. The column-level ownership transition (Commerce Expert columns → Distributed Systems Expert columns within each row) is **not a sub-table boundary** — do not open a new table when column ownership shifts mid-row. It is **not a role-sequence trigger** — do not insert a section heading, horizontal rule, or blockquote separator when the responsible expert changes within a single scenario row. The table has one header row and exactly three scenario rows. Ownership transitions within rows do not alter table structure.

---

## Scenario Analysis Table

Produce one table with eight columns:

| # | Scenario | State *(D)* | Capability *(C)* | Data at Risk *(C)* | Recovery Path *(D)* | Severity *(D)* | Blast Radius *(C)* |
|---|----------|-------------|------------------|--------------------|---------------------|----------------|--------------------|

Column ownership: *(C)* = Commerce Domain Expert | *(D)* = Distributed Systems Expert

Fill each row using the row-level instructions below. Each instruction is co-located with that row — read it when constructing the row.

---

**Row 1 — Full Client Offline**

**Write this row now.** Scenario *(Both)*: name a full client-offline event during a `{{topic}}` commerce operation — use a specific operation: checkout submission, cart lock acquisition, payment confirmation, or order placement. State *(D)*: describe the exact partition state — name what the server holds that the client cannot reach, name the consistency guarantee in effect (strong / eventual / causal), and name any timeout or lock expiry that is now running unobserved by the client. Capability *(C)*: list every action the user can still take offline; list every action that is now blocked; name what UI state the client should show but may not. Data at Risk *(C)*: name the specific fields, records, or reservation windows at risk of loss or conflict — state the staleness window and identify whether loss is silent or surfaced. Recovery Path *(D)*: name the recovery pattern (saga rollback, optimistic lock release, idempotent replay); state the trigger (reconnect event, TTL expiry, reconciliation job); walk the numbered steps; state the terminal healthy state. Severity *(D)*: degraded / impaired / down. Blast Radius *(C)*: name the affected user segment and scale (all users mid-checkout, users with active cart locks, <1% with pending payment).

**Do not advance to Row 2 until all eight columns for Row 1 contain non-placeholder content.**

---

**Row 2 — Partial Service Failure**

**Write this row now.** Scenario *(Both)*: name a partial service failure event where one named downstream service is unavailable — inventory service, payment gateway, or fulfillment orchestrator — while the `{{topic}}` client remains connected. State *(D)*: name the unavailable service; describe the cascading states that result (inventory reservation timeout, payment pre-auth orphaned, fulfillment order stuck in pending); name the consistency level the system degrades to when this service is absent. Capability *(C)*: name which commerce flows continue (browse, add-to-cart, saved order retrieval); name which are blocked (new checkout, payment capture, fulfillment initiation); describe whether degradation is graceful (user is informed) or silent (user submits into a black hole). Data at Risk *(C)*: name the specific entity orphaned or at risk — reservation record, pre-authorization token, cart lock ID — and state the TTL or conflict window before the orphaned record causes harm. Recovery Path *(D)*: name the recovery pattern; state whether recovery is automatic (circuit breaker closes, saga compensates) or requires manual operator action; name the idempotency key or saga ID used to prevent double-processing on replay. Severity *(D)*: degraded / impaired / down. Blast Radius *(C)*: name affected user segment (all users attempting checkout, users with payment in flight, users whose orders are in fulfillment queue).

**Do not advance to Row 3 until all eight columns for Row 2 contain non-placeholder content.**

---

**Row 3 — Eventual Consistency / Split-Brain**

**Write this row now.** Scenario *(Both)*: name a split-brain event where concurrent writes from two clients or two nodes create conflicting state in a specific `{{topic}}` entity — inventory count, cart total, order status, or coupon redemption record. State *(D)*: describe the diverged state — which node holds which version; name the conflict window duration; state the system's current conflict-resolution policy (LWW, vector clock, application-level merge, none). Capability *(C)*: name what the user sees and can do during the conflict window; name what is inconsistent or stale; name what the user cannot know is wrong. Data at Risk *(C)*: name the specific field in conflict; state the business consequence of each resolution outcome (oversell if A wins, double-charge if B wins, duplicate fulfillment order if merge is naïve). Recovery Path *(D)*: name the resolution strategy; state who or what resolves (system-automatic vs. human-review queue); describe the post-resolution state reconciliation that must occur to restore consistency downstream (inventory adjustment, charge reversal, fulfillment cancel). Severity *(D)*: degraded / impaired / down. Blast Radius *(C)*: name the affected segment (all users writing concurrently, users in affected geo-partition, <1% under typical split-brain conditions).

**Do not advance to the Gap Register until all eight columns for Row 3 contain non-placeholder content.**

---

**Section gate ✓**: Before writing the Gap Register, confirm: three rows present, all eight columns filled in every row, no cell empty or placeholder. If any cell is missing, fill it before continuing.

---

## Gap Register

Identify three findings revealed by the scenario analysis:

**Offline Experience Gap**: Name the specific capability in `{{topic}}` that is unavailable when the client is fully offline and has no degraded fallback. Name the user action that fails silently or without feedback. State what a minimal offline-capable design would require (local queue, optimistic write, conflict token).

**Data Consistency Violation**: Name the specific entity and field in `{{topic}}` where concurrent writes can produce irreconcilable state. State the resolution policy that is absent. Name the business consequence (oversell, double-charge, duplicate fulfillment order). Explain why the current system (if any policy exists) is insufficient.

**Missing Recovery Flow**: Name the failure entry point in `{{topic}}` that has no documented recovery exit. Describe the scenario in which a user or automated process could be stuck indefinitely. State the minimum recovery flow required: the trigger, the steps, and the terminal state.

Each finding must be labeled, specific, and anchored to `{{topic}}`. Generic findings (e.g., "offline support may be limited") fail.

---

**Signal artifact**: Write output to `{{topic}}-flow-resilience-{{date}}.md`.

---

## Variation Summary

| Version | Axes | Key innovation | Expected ceiling |
|---------|------|----------------|-----------------|
| V-01 | Role sequence | Commerce Expert runs first; DS Expert validates second | Passes C-01–C-06; 12/15 |
| V-02 | Output format | Column-level ownership printed in headers; single anti-boundary instruction | Passes C-01–C-06 + C-20 reinforcement; ~12/15 |
| V-03 | Phrasing register | All guidance as direct imperatives; self-check gate before output | Passes C-01–C-06; ~12/15 |
| V-04 | Role sequence + lifecycle emphasis | Four lifecycle-ordered phases; phase gates between each | Passes C-01–C-06 + section-level gates; ~13/15 |
| V-05 | Four-level architecture + symptom negations + in-row imperatives | Explicit four-level stack named; 2 symptom negations in anti-boundary instruction; bold in-row imperatives in each Content descriptor | Targets C-21 + C-22 + C-23; 15/15 ceiling |
