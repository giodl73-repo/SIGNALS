Now I'll generate all 5 complete variations. The R7 V-05 ceiling is 95.79 (11/11 aspirational, the v7 maximum). Round 8 explores structural axes while holding all 11 criteria.

**Axis selection:**
- V-01: Role sequence (D first, C second)
- V-02: Lifecycle emphasis (Recovery Path → 4-stage Detect/Contain/Recover/Validate)
- V-03: Inertia framing (Status Quo Risk as 10th column)
- V-04: V-01 + V-02
- V-05: V-01 + V-02 + V-03

---

# Round 8 Variations — flow-resilience

---

## V-01 — Role Sequence: Distributed Systems Expert First

**Variation axis**: Role sequence — D defined before C.

**Hypothesis**: DS-first ordering anchors the model on failure mechanics and partition behavior before commerce semantics are layered. The model encounters State and Recovery Path fill requirements as the "primary owner" perspective, improving failure-mode precision before commerce grounding follows.

---

You are playing two expert roles simultaneously:

- **D — Distributed Systems Expert**: Engineer specialized in distributed failure modes, partition behavior, consistency models (AP vs CP), idempotency requirements, circuit-breaker patterns, and recovery strategies.
- **C — Commerce Expert**: Analyst specialized in commerce operations, order lifecycle, payment processing, inventory management, cart state, and fulfillment systems.

---

### Anti-Omission Architecture

The following four-level stack coordinates anti-omission mechanisms across structural levels. Each level targets a distinct omission risk; no two levels duplicate each other's function.

| Level | Name | Mechanism | Omission Risk Addressed |
|-------|------|-----------|-------------------------|
| Table | Unified Row Index | `#` column in every row of a single table; see **Column Contract** section below for the unified-index column entry | A row disappears when column ownership transitions from D to C or C to D |
| Section | Phase Gate | Explicit instruction: complete all scenario rows before advancing to the Gap Register; see **Phase Gate** section below | Model writes Gap Register before completing all scenario rows |
| Column | Column Contract | Per-column expert-role label defined in the **Column Contract** section below | A column is omitted when ownership shifts between D and C |
| Slot | Row Imperatives | Bold **Write this row now.** / **Do not advance** imperatives co-located inside the **Row Descriptor Table** section below | A row is constructed with missing columns when the model advances prematurely |

---

### Column Contract

The following meta-table defines ownership and fill requirements for every column in the Scenario Analysis Table. Process this contract before constructing any row.

| Column | Owner | Fill Requirement |
|--------|-------|-----------------|
| # | — | Row index: 1, 2, 3 |
| Scenario | C | Named commerce operation and failure trigger (e.g., "Checkout — payment gateway unreachable") |
| Class | — | Class 1 / Class 2 / Class 3 |
| State | D | System partition state at failure onset; name the consistency guarantee in effect (AP or CP); state whether reads return stale data under this partition |
| Capability | C | What the user can still complete; what is blocked; name the specific user action that becomes unavailable |
| Data at Risk | D | Entities with stale, lost, or inconsistent state; name each entity and its risk type (stale / lost / inconsistent) |
| Recovery Path | D | Ordered recovery steps from failure to healthy state; name the recovery pattern (e.g., saga rollback, idempotent retry, last-write-wins, CRDT merge) |
| Severity | D | degraded / impaired / down |
| Blast Radius | C | Segment and estimated percentage of users affected |

---

### Scenario Analysis Table

Produce a single unified table with all nine columns in every row.

Do not create separate tables for Distributed Systems Expert columns and Commerce Expert columns. Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts.

| # | Scenario | Class | State | Capability | Data at Risk | Recovery Path | Severity | Blast Radius |
|---|----------|-------|-------|------------|--------------|---------------|----------|--------------|
| 1 | | | | | | | | |
| 2 | | | | | | | | |
| 3 | | | | | | | | |

---

### Phase Gate

Produce all three rows before writing the Gap Register. Before advancing to the Gap Register, confirm that all three rows are present and all nine columns contain non-placeholder content in every row. If any cell is missing or contains a placeholder, fill it before continuing.

---

### Row Descriptor Table

Each row has a governing descriptor positioned at the row it governs. The bold imperative in each descriptor is load-bearing — read it at the moment you construct that row.

| # | Scenario Class | Content Descriptor |
|---|---------------|-------------------|
| 1 | Class 1 — Full Connectivity Loss | Row 1 covers a commerce operation where the client loses all network connectivity mid-flow (e.g., checkout initiated, device goes offline before payment confirmation). State: name the local cache state and what data was last durably written before the connection dropped; identify whether the system behaves AP or CP under this failure. Capability: enumerate what the user can still interact with locally versus what requires a server round-trip. Data at Risk: identify which cart, session, reservation, or loyalty data has no durable write and may be silently lost on reconnect. Recovery Path: describe the sync-on-reconnect strategy; state whether each replayed operation is idempotent and what happens if the replay is triggered twice. **Write this row now.** Fill all nine columns before continuing. **Do not advance to Row 2 until Row 1 contains non-placeholder content in every column.** |
| 2 | Class 2 — Partial Service Failure | Row 2 covers a commerce operation where one dependent service (inventory service, payment gateway, or fulfillment orchestrator) becomes unavailable while the rest of the system operates normally. State: identify which service is down and what downstream state is now stale or unconfirmed. Capability: identify what the user can still complete in the degraded system versus what is blocked; name the specific user action that fails. Data at Risk: identify reservation counts, payment tokens, or order states that may be inconsistent between the calling service and the failed dependency. Recovery Path: name the circuit-breaker or bulkhead strategy in use and whether it produces a fail-fast or queue-and-retry outcome. **Write this row now.** Fill all nine columns before continuing. **Do not advance to Row 3 until Row 2 contains non-placeholder content in every column.** |
| 3 | Class 3 — Concurrent Writes / Split-Brain | If node A's version of the conflicted entity wins the merge: inventory count is oversold, cart total reflects stale pricing, and the payment authorization is double-charged. If node B's version wins: order status reverts to pre-confirmation, coupon redemption is duplicated, and fulfillment fires twice against the same order. If a naive merge runs: all three consequences compound into an unrecoverable inconsistency. **Write this row now.** State: name the conflict window duration and the resolution policy in effect (last-write-wins, vector-clock merge, application-level reconciliation). Capability: identify what the user sees during the conflict window — is the conflict visible or silent at the UI layer? Data at Risk: name the specific entities at risk per resolution outcome branch. Recovery Path: describe the resolution strategy selected and its specific commerce consequence. **Do not advance to the Gap Register until Row 3 contains non-placeholder content in every column.** |

---

### Anti-Boundary Instruction

All nine columns appear in every row of a single unified table. Column ownership shifts within the row — it is not a sub-table boundary. When filling transitions from D to C or C to D mid-row, do not treat the transition as a role-sequence trigger. Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts.

---

### Gap Register

After completing all three rows of the Scenario Analysis Table, identify exactly three gaps — one of each type:

1. **Offline Experience Gap** — a specific user action that the system cannot support during full offline conditions (Class 1), named to the commerce flow and the specific UI interaction that fails.
2. **Data Consistency Violation** — a specific entity whose state may diverge between replicas (Class 2 or Class 3), with the named consistency violation type (dirty read, lost update, phantom read, or write skew).
3. **Missing Recovery Flow** — a specific scenario where no recovery path exists, the recovery path is incomplete, or the recovery path is non-idempotent under replay.

---

### Findings

Summarize findings in order of business impact (highest first). Each finding must reference its scenario row number from the Scenario Analysis Table and name the specific commerce operation at risk.

---

---

## V-02 — Lifecycle Emphasis: 4-Stage Recovery Timeline

**Variation axis**: Lifecycle emphasis — Recovery Path column expanded to a four-stage timeline (Detect → Contain → Recover → Validate) in the Column Contract and Row Descriptor Table.

**Hypothesis**: Phase-decomposed recovery forces enumeration of distinct actions at each lifecycle stage rather than a single recovery-pattern label, producing richer and more actionable per-scenario recovery specifications.

---

You are playing two expert roles simultaneously:

- **C — Commerce Expert**: Analyst specialized in commerce operations, order lifecycle, payment processing, inventory management, cart state, and fulfillment systems.
- **D — Distributed Systems Expert**: Engineer specialized in distributed failure modes, partition behavior, consistency models (AP vs CP), idempotency requirements, circuit-breaker patterns, and recovery strategies.

---

### Anti-Omission Architecture

The following four-level stack coordinates anti-omission mechanisms across structural levels. Each level targets a distinct omission risk; no two levels duplicate each other's function.

| Level | Name | Mechanism | Omission Risk Addressed |
|-------|------|-----------|-------------------------|
| Table | Unified Row Index | `#` column in every row of a single table; see **Column Contract** section below for the unified-index column entry | A row disappears when column ownership transitions between C and D |
| Section | Phase Gate | Explicit instruction: complete all scenario rows before advancing to the Gap Register; see **Phase Gate** section below | Model writes Gap Register before completing all scenario rows |
| Column | Column Contract | Per-column expert-role label defined in the **Column Contract** section below | A column is omitted when ownership shifts between C and D |
| Slot | Row Imperatives | Bold **Write this row now.** / **Do not advance** imperatives co-located inside the **Row Descriptor Table** section below | A row is constructed with missing columns when the model advances prematurely |

---

### Column Contract

The following meta-table defines ownership and fill requirements for every column in the Scenario Analysis Table. Process this contract before constructing any row.

| Column | Owner | Fill Requirement |
|--------|-------|-----------------|
| # | — | Row index: 1, 2, 3 |
| Scenario | C | Named commerce operation and failure trigger (e.g., "Checkout — payment gateway unreachable") |
| Class | — | Class 1 / Class 2 / Class 3 |
| State | D | System partition state at failure onset; name the consistency guarantee in effect (AP or CP); state whether reads return stale data under this partition |
| Capability | C | What the user can still complete; what is blocked; name the specific user action that becomes unavailable |
| Data at Risk | D | Entities with stale, lost, or inconsistent state; name each entity and its risk type (stale / lost / inconsistent) |
| Recovery Path | D | Four-stage recovery timeline — **Stage 1 / Detect**: how the system identifies the failure (timeout, health check signal, error-rate threshold). **Stage 2 / Contain**: what isolation mechanism prevents cascading (circuit breaker trip, bulkhead saturation, queue backpressure). **Stage 3 / Recover**: ordered steps to restore state; name the recovery pattern (saga rollback, idempotent retry, last-write-wins, CRDT merge). **Stage 4 / Validate**: how the system confirms recovery completed without data loss or corruption (reconciliation run, idempotency token verification, consistency-check query). Write all four stages. |
| Severity | D | degraded / impaired / down |
| Blast Radius | C | Segment and estimated percentage of users affected |

---

### Scenario Analysis Table

Produce a single unified table with all nine columns in every row.

Do not create separate tables for Commerce Expert columns and Distributed Systems Expert columns. Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts.

| # | Scenario | Class | State | Capability | Data at Risk | Recovery Path | Severity | Blast Radius |
|---|----------|-------|-------|------------|--------------|---------------|----------|--------------|
| 1 | | | | | | | | |
| 2 | | | | | | | | |
| 3 | | | | | | | | |

---

### Phase Gate

Produce all three rows before writing the Gap Register. Before advancing to the Gap Register, confirm that all three rows are present and all nine columns contain non-placeholder content in every row. If the Recovery Path cell in any row is missing any of the four stages, complete it before continuing.

---

### Row Descriptor Table

Each row has a governing descriptor positioned at the row it governs. The bold imperative in each descriptor is load-bearing — read it at the moment you construct that row.

| # | Scenario Class | Content Descriptor |
|---|---------------|-------------------|
| 1 | Class 1 — Full Connectivity Loss | Row 1 covers a commerce operation where the client loses all network connectivity mid-flow. State: name the local cache state and what data was last durably written before the connection dropped. Capability: enumerate what the user can still interact with locally versus what requires server round-trip. Data at Risk: identify which cart, session, or reservation data has no durable write. Recovery Path: provide all four stages — Detect (how the app knows connectivity is gone), Contain (how in-flight writes are queued or discarded), Recover (sync-on-reconnect strategy; state whether each replayed operation is idempotent), Validate (how the system confirms no duplicate or lost write occurred after reconnect). **Write this row now.** Fill all nine columns before continuing. **Do not advance to Row 2 until Row 1 contains non-placeholder content in every column including all four Recovery Path stages.** |
| 2 | Class 2 — Partial Service Failure | Row 2 covers a commerce operation where one dependent service (inventory service, payment gateway, or fulfillment orchestrator) becomes unavailable. State: identify which service is down and what downstream state is now stale. Capability: name the specific user action that fails. Data at Risk: identify reservation counts, payment tokens, or order states at risk of inconsistency. Recovery Path: provide all four stages — Detect (how the calling service identifies the dependency is down), Contain (circuit-breaker or bulkhead behavior — does it fail-fast or queue?), Recover (retry or saga rollback steps), Validate (idempotency check or reconciliation step that confirms no double-execution). **Write this row now.** Fill all nine columns before continuing. **Do not advance to Row 3 until Row 2 contains non-placeholder content in every column including all four Recovery Path stages.** |
| 3 | Class 3 — Concurrent Writes / Split-Brain | If node A's version wins: inventory is oversold, cart total is stale, and payment is double-charged. If node B's version wins: order status reverts, coupon redemption is duplicated, and fulfillment fires twice. If naive merge runs: all three consequences compound. **Write this row now.** State: name the conflict window duration and the resolution policy in effect. Capability: identify what the user sees during the conflict window. Data at Risk: name the specific entities at risk per resolution outcome branch. Recovery Path: provide all four stages — Detect (how the conflict is detected — vector clock divergence, checksum mismatch, application-level assertion), Contain (how conflicting writes are quarantined), Recover (resolution strategy and its specific commerce consequence per outcome branch), Validate (how the system confirms post-merge state is consistent — no oversell, no duplicate fulfillment, no double-charge outstanding). **Do not advance to the Gap Register until Row 3 contains non-placeholder content in every column including all four Recovery Path stages.** |

---

### Anti-Boundary Instruction

All nine columns appear in every row of a single unified table. Column ownership shifts within the row — it is not a sub-table boundary. When filling transitions from C to D or D to C mid-row, do not treat the transition as a role-sequence trigger. Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts.

---

### Gap Register

After completing all three rows of the Scenario Analysis Table, identify exactly three gaps — one of each type:

1. **Offline Experience Gap** — a specific user action that the system cannot support during full offline conditions (Class 1), named to the commerce flow and the specific UI interaction that fails.
2. **Data Consistency Violation** — a specific entity whose state may diverge between replicas (Class 2 or Class 3), with the named consistency violation type (dirty read, lost update, phantom read, or write skew).
3. **Missing Recovery Flow** — a specific scenario where a Recovery Path stage is absent, incomplete, or non-idempotent under replay.

---

### Findings

Summarize findings in order of business impact (highest first). Each finding must reference its scenario row number from the Scenario Analysis Table and name the specific commerce operation at risk.

---

---

## V-03 — Inertia Framing: Status Quo Risk Column

**Variation axis**: Inertia framing — Add "Status Quo Risk" as a 10th column (owned by C) that names what the system looks like with no resilience investment for that failure class.

**Hypothesis**: Making the cost of inaction visible in every scenario row anchors Gap Register findings to concrete no-resilience baselines, elevating findings from descriptive to decision-driving. The status quo is the primary competitor — naming it per row makes vague gap descriptions visibly inadequate against the named inertia cost.

---

You are playing two expert roles simultaneously:

- **C — Commerce Expert**: Analyst specialized in commerce operations, order lifecycle, payment processing, inventory management, cart state, and fulfillment systems.
- **D — Distributed Systems Expert**: Engineer specialized in distributed failure modes, partition behavior, consistency models (AP vs CP), idempotency requirements, circuit-breaker patterns, and recovery strategies.

---

### Anti-Omission Architecture

The following four-level stack coordinates anti-omission mechanisms across structural levels. Each level targets a distinct omission risk; no two levels duplicate each other's function.

| Level | Name | Mechanism | Omission Risk Addressed |
|-------|------|-----------|-------------------------|
| Table | Unified Row Index | `#` column in every row of a single table; see **Column Contract** section below for the unified-index column entry | A row disappears when column ownership transitions between C and D |
| Section | Phase Gate | Explicit instruction: complete all scenario rows before advancing to the Gap Register; see **Phase Gate** section below | Model writes Gap Register before completing all scenario rows |
| Column | Column Contract | Per-column expert-role label defined in the **Column Contract** section below | A column is omitted when ownership shifts between C and D |
| Slot | Row Imperatives | Bold **Write this row now.** / **Do not advance** imperatives co-located inside the **Row Descriptor Table** section below | A row is constructed with missing columns when the model advances prematurely |

---

### Column Contract

The following meta-table defines ownership and fill requirements for every column in the Scenario Analysis Table. Process this contract before constructing any row.

| Column | Owner | Fill Requirement |
|--------|-------|-----------------|
| # | — | Row index: 1, 2, 3 |
| Scenario | C | Named commerce operation and failure trigger (e.g., "Checkout — payment gateway unreachable") |
| Class | — | Class 1 / Class 2 / Class 3 |
| State | D | System partition state at failure onset; name the consistency guarantee in effect (AP or CP); state whether reads return stale data under this partition |
| Capability | C | What the user can still complete; what is blocked; name the specific user action that becomes unavailable |
| Data at Risk | D | Entities with stale, lost, or inconsistent state; name each entity and its risk type (stale / lost / inconsistent) |
| Recovery Path | D | Ordered recovery steps from failure to healthy state; name the recovery pattern (e.g., saga rollback, idempotent retry, last-write-wins, CRDT merge) |
| Severity | D | degraded / impaired / down |
| Blast Radius | C | Segment and estimated percentage of users affected |
| Status Quo Risk | C | What the commerce operation looks like with no resilience investment for this failure class: name the specific user-visible outcome (e.g., silent cart loss, duplicate charge, hard error page) and the commerce operation most directly exposed. This is the cost of inaction — the outcome the system currently delivers without recovery investment. |

---

### Scenario Analysis Table

Produce a single unified table with all ten columns in every row.

Do not create separate tables for Commerce Expert columns and Distributed Systems Expert columns. Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts.

| # | Scenario | Class | State | Capability | Data at Risk | Recovery Path | Severity | Blast Radius | Status Quo Risk |
|---|----------|-------|-------|------------|--------------|---------------|----------|--------------|-----------------|
| 1 | | | | | | | | | |
| 2 | | | | | | | | | |
| 3 | | | | | | | | | |

---

### Phase Gate

Produce all three rows before writing the Gap Register. Before advancing to the Gap Register, confirm that all three rows are present and all ten columns contain non-placeholder content in every row. If any cell is missing or contains a placeholder, fill it before continuing.

---

### Row Descriptor Table

Each row has a governing descriptor positioned at the row it governs. The bold imperative in each descriptor is load-bearing — read it at the moment you construct that row.

| # | Scenario Class | Content Descriptor |
|---|---------------|-------------------|
| 1 | Class 1 — Full Connectivity Loss | Row 1 covers a commerce operation where the client loses all network connectivity mid-flow. State: name the local cache state and what data was last durably written before the connection dropped. Capability: enumerate what the user can still interact with locally. Data at Risk: identify which cart, session, reservation, or loyalty data has no durable write. Recovery Path: describe the sync-on-reconnect strategy; state whether replayed operations are idempotent. Status Quo Risk: name the specific outcome when no offline-support investment exists (e.g., silent cart abandonment, order not placed, no user feedback that the operation failed). **Write this row now.** Fill all ten columns before continuing. **Do not advance to Row 2 until Row 1 contains non-placeholder content in every column.** |
| 2 | Class 2 — Partial Service Failure | Row 2 covers a commerce operation where one dependent service becomes unavailable. State: identify which service is down and what downstream state is now stale. Capability: name the specific user action that fails. Data at Risk: identify reservation counts, payment tokens, or order states at risk of inconsistency. Recovery Path: name the circuit-breaker or bulkhead strategy. Status Quo Risk: name the specific outcome when no circuit-breaker or fallback exists — does the failure cascade (e.g., all checkout attempts time out), does it produce a duplicate charge, or does it leave orphaned inventory reservations? **Write this row now.** Fill all ten columns before continuing. **Do not advance to Row 3 until Row 2 contains non-placeholder content in every column.** |
| 3 | Class 3 — Concurrent Writes / Split-Brain | If node A's version wins: inventory is oversold, cart total is stale, and payment is double-charged. If node B's version wins: order status reverts, coupon redemption is duplicated, and fulfillment fires twice. If naive merge runs: all three consequences compound. **Write this row now.** State: name the conflict window duration and the resolution policy in effect. Capability: identify what the user sees during the conflict window. Data at Risk: name specific entities per resolution outcome branch. Recovery Path: describe the resolution strategy and its specific commerce consequence. Status Quo Risk: name what currently happens in the absence of any conflict-resolution investment — which of the three merge outcomes is the system's default behavior today, and what is its business cost (oversell rate, chargeback rate, duplicate fulfillment cost). **Do not advance to the Gap Register until Row 3 contains non-placeholder content in every column.** |

---

### Anti-Boundary Instruction

All ten columns appear in every row of a single unified table. Column ownership shifts within the row — it is not a sub-table boundary. When filling transitions from C to D or D to C mid-row, do not treat the transition as a role-sequence trigger. Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts.

---

### Gap Register

After completing all three rows of the Scenario Analysis Table, identify exactly three gaps — one of each type. Each gap finding must reference the Status Quo Risk column entry for its row as the named baseline against which the gap is measured.

1. **Offline Experience Gap** — a specific user action that the system cannot support during full offline conditions (Class 1), named to the commerce flow and anchored to the no-resilience baseline in the Status Quo Risk column.
2. **Data Consistency Violation** — a specific entity whose state may diverge between replicas (Class 2 or Class 3), with the named consistency violation type and a reference to the status-quo consequence of leaving it unresolved.
3. **Missing Recovery Flow** — a specific scenario where no recovery path exists or the recovery path is incomplete, with the status-quo outcome (the current default behavior) named explicitly.

---

### Findings

Summarize findings in order of business impact (highest first). Each finding must reference its scenario row number from the Scenario Analysis Table, name the specific commerce operation at risk, and state the cost of inaction from the Status Quo Risk column.

---

---

## V-04 — Role Sequence + Lifecycle Emphasis (V-01 + V-02)

**Variation axes**: D defined first + Recovery Path expanded to 4-stage Detect/Contain/Recover/Validate.

**Hypothesis**: DS-first anchoring combined with lifecycle-structured recovery produces the most technically dense output — the model leads with partition mechanics, then builds per-stage recovery depth before Commerce layers business grounding.

---

You are playing two expert roles simultaneously:

- **D — Distributed Systems Expert**: Engineer specialized in distributed failure modes, partition behavior, consistency models (AP vs CP), idempotency requirements, circuit-breaker patterns, and recovery strategies.
- **C — Commerce Expert**: Analyst specialized in commerce operations, order lifecycle, payment processing, inventory management, cart state, and fulfillment systems.

---

### Anti-Omission Architecture

The following four-level stack coordinates anti-omission mechanisms across structural levels. Each level targets a distinct omission risk; no two levels duplicate each other's function.

| Level | Name | Mechanism | Omission Risk Addressed |
|-------|------|-----------|-------------------------|
| Table | Unified Row Index | `#` column in every row of a single table; see **Column Contract** section below for the unified-index column entry | A row disappears when column ownership transitions between D and C |
| Section | Phase Gate | Explicit instruction: complete all scenario rows before advancing to the Gap Register; see **Phase Gate** section below | Model writes Gap Register before completing all scenario rows |
| Column | Column Contract | Per-column expert-role label defined in the **Column Contract** section below | A column is omitted when ownership shifts between D and C |
| Slot | Row Imperatives | Bold **Write this row now.** / **Do not advance** imperatives co-located inside the **Row Descriptor Table** section below | A row is constructed with missing columns when the model advances prematurely |

---

### Column Contract

The following meta-table defines ownership and fill requirements for every column in the Scenario Analysis Table. Process this contract before constructing any row.

| Column | Owner | Fill Requirement |
|--------|-------|-----------------|
| # | — | Row index: 1, 2, 3 |
| Scenario | C | Named commerce operation and failure trigger |
| Class | — | Class 1 / Class 2 / Class 3 |
| State | D | System partition state at failure onset; name the consistency guarantee in effect (AP or CP); state whether reads return stale data |
| Capability | C | What the user can still complete; what is blocked; name the specific user action that becomes unavailable |
| Data at Risk | D | Entities with stale, lost, or inconsistent state; name each entity and its risk type |
| Recovery Path | D | Four-stage recovery timeline — **Stage 1 / Detect**: how the system identifies the failure (timeout threshold, health check, error-rate trip). **Stage 2 / Contain**: what isolation mechanism prevents cascading (circuit-breaker trip, bulkhead saturation, backpressure). **Stage 3 / Recover**: ordered steps to restore state; name the recovery pattern (saga rollback, idempotent retry, last-write-wins, CRDT merge). **Stage 4 / Validate**: how the system confirms recovery completed without data loss or corruption (reconciliation query, idempotency token check, consistency assertion). Write all four stages. |
| Severity | D | degraded / impaired / down |
| Blast Radius | C | Segment and estimated percentage of users affected |

---

### Scenario Analysis Table

Produce a single unified table with all nine columns in every row.

Do not create separate tables for Distributed Systems Expert columns and Commerce Expert columns. Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts.

| # | Scenario | Class | State | Capability | Data at Risk | Recovery Path | Severity | Blast Radius |
|---|----------|-------|-------|------------|--------------|---------------|----------|--------------|
| 1 | | | | | | | | |
| 2 | | | | | | | | |
| 3 | | | | | | | | |

---

### Phase Gate

Produce all three rows before writing the Gap Register. Before advancing to the Gap Register, confirm that all three rows are present and all nine columns contain non-placeholder content in every row. If the Recovery Path cell in any row is missing any of the four stages, complete it before continuing.

---

### Row Descriptor Table

Each row has a governing descriptor positioned at the row it governs. The bold imperative in each descriptor is load-bearing — read it at the moment you construct that row.

| # | Scenario Class | Content Descriptor |
|---|---------------|-------------------|
| 1 | Class 1 — Full Connectivity Loss | Row 1 covers a commerce operation where the client loses all network connectivity mid-flow (e.g., checkout initiated, device goes offline before payment confirmation). State: name the local cache state and what data was last durably written before the connection dropped; identify whether the system is AP or CP under this failure. Capability: enumerate what the user can still interact with locally versus what requires server round-trip. Data at Risk: identify which cart, session, or reservation data has no durable write. Recovery Path: provide all four stages — Detect (how the app knows connectivity is lost), Contain (how in-flight writes are queued or discarded), Recover (sync-on-reconnect strategy; state whether each replayed operation is idempotent), Validate (how the system confirms no duplicate or lost write after reconnect). **Write this row now.** Fill all nine columns before continuing. **Do not advance to Row 2 until Row 1 contains non-placeholder content in every column including all four Recovery Path stages.** |
| 2 | Class 2 — Partial Service Failure | Row 2 covers a commerce operation where one dependent service (inventory service, payment gateway, or fulfillment orchestrator) becomes unavailable while the rest of the system operates normally. State: identify which service is down and what downstream state is now stale or unconfirmed. Capability: name the specific user action that fails. Data at Risk: identify reservation counts, payment tokens, or order states that may be inconsistent between the calling service and the failed dependency. Recovery Path: provide all four stages — Detect (how the calling service identifies the dependency is unavailable), Contain (circuit-breaker or bulkhead behavior — fail-fast or queue?), Recover (retry or saga rollback steps and their idempotency guarantee), Validate (reconciliation step confirming no double-execution or orphaned reservation). **Write this row now.** Fill all nine columns before continuing. **Do not advance to Row 3 until Row 2 contains non-placeholder content in every column including all four Recovery Path stages.** |
| 3 | Class 3 — Concurrent Writes / Split-Brain | If node A's version wins: inventory is oversold, cart total is stale, and payment is double-charged. If node B's version wins: order status reverts, coupon redemption is duplicated, and fulfillment fires twice. If naive merge runs: all three consequences compound into an unrecoverable inconsistency. **Write this row now.** State: name the conflict window duration and the resolution policy in effect (last-write-wins, vector-clock merge, application-level reconciliation). Capability: identify what the user sees during the conflict window — visible or silent? Data at Risk: name the specific entities at risk per resolution outcome branch. Recovery Path: provide all four stages — Detect (how conflict is identified — vector clock divergence, checksum mismatch, assertion failure), Contain (how conflicting writes are quarantined pending resolution), Recover (resolution strategy and its specific commerce consequence per outcome branch), Validate (post-merge consistency confirmation — no outstanding oversell, no duplicate fulfillment, no double-charge). **Do not advance to the Gap Register until Row 3 contains non-placeholder content in every column including all four Recovery Path stages.** |

---

### Anti-Boundary Instruction

All nine columns appear in every row of a single unified table. Column ownership shifts within the row — it is not a sub-table boundary. When filling transitions from D to C or C to D mid-row, do not treat the transition as a role-sequence trigger. Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts.

---

### Gap Register

After completing all three rows of the Scenario Analysis Table, identify exactly three gaps — one of each type:

1. **Offline Experience Gap** — a specific user action that the system cannot support during full offline conditions (Class 1), named to the commerce flow.
2. **Data Consistency Violation** — a specific entity whose state may diverge between replicas (Class 2 or Class 3), with the named consistency violation type.
3. **Missing Recovery Flow** — a specific scenario where a Recovery Path stage is absent, incomplete, or non-idempotent under replay.

---

### Findings

Summarize findings in order of business impact (highest first). Each finding must reference its scenario row number from the Scenario Analysis Table and name the specific commerce operation at risk.

---

---

## V-05 — Role Sequence + Lifecycle Emphasis + Inertia Framing (V-01 + V-02 + V-03)

**Variation axes**: D defined first + 4-stage recovery timeline + Status Quo Risk as 10th column.

**Hypothesis**: All three axes together maximize decision-support value. DS-first role sequence produces precision in failure analysis; lifecycle structure in recovery produces depth per stage; explicit inertia cost framing per row anchors the Gap Register to named business consequences of doing nothing.

---

You are playing two expert roles simultaneously:

- **D — Distributed Systems Expert**: Engineer specialized in distributed failure modes, partition behavior, consistency models (AP vs CP), idempotency requirements, circuit-breaker patterns, and recovery strategies.
- **C — Commerce Expert**: Analyst specialized in commerce operations, order lifecycle, payment processing, inventory management, cart state, and fulfillment systems.

---

### Anti-Omission Architecture

The following four-level stack coordinates anti-omission mechanisms across structural levels. Each level targets a distinct omission risk; no two levels duplicate each other's function.

| Level | Name | Mechanism | Omission Risk Addressed |
|-------|------|-----------|-------------------------|
| Table | Unified Row Index | `#` column in every row of a single table; see **Column Contract** section below for the unified-index column entry | A row disappears when column ownership transitions between D and C |
| Section | Phase Gate | Explicit instruction: complete all scenario rows before advancing to the Gap Register; see **Phase Gate** section below | Model writes Gap Register before completing all scenario rows |
| Column | Column Contract | Per-column expert-role label defined in the **Column Contract** section below | A column is omitted when ownership shifts between D and C |
| Slot | Row Imperatives | Bold **Write this row now.** / **Do not advance** imperatives co-located inside the **Row Descriptor Table** section below | A row is constructed with missing columns when the model advances prematurely |

---

### Column Contract

The following meta-table defines ownership and fill requirements for every column in the Scenario Analysis Table. Process this contract before constructing any row.

| Column | Owner | Fill Requirement |
|--------|-------|-----------------|
| # | — | Row index: 1, 2, 3 |
| Scenario | C | Named commerce operation and failure trigger |
| Class | — | Class 1 / Class 2 / Class 3 |
| State | D | System partition state at failure onset; name the consistency guarantee in effect (AP or CP); state whether reads return stale data under this partition |
| Capability | C | What the user can still complete; what is blocked; name the specific user action that becomes unavailable |
| Data at Risk | D | Entities with stale, lost, or inconsistent state; name each entity and its risk type (stale / lost / inconsistent) |
| Recovery Path | D | Four-stage recovery timeline — **Stage 1 / Detect**: how the system identifies the failure (timeout, health check, error-rate trip). **Stage 2 / Contain**: what isolation mechanism prevents cascading (circuit-breaker trip, bulkhead saturation, backpressure). **Stage 3 / Recover**: ordered steps to restore state; name the recovery pattern (saga rollback, idempotent retry, last-write-wins, CRDT merge). **Stage 4 / Validate**: how the system confirms recovery completed without data loss or corruption (reconciliation query, idempotency token check, consistency assertion). Write all four stages. |
| Severity | D | degraded / impaired / down |
| Blast Radius | C | Segment and estimated percentage of users affected |
| Status Quo Risk | C | What the commerce operation looks like with no resilience investment for this failure class: name the specific user-visible outcome (e.g., silent cart loss, duplicate charge, hard error page, undetected oversell) and the commerce flow most directly exposed. This is the cost of inaction — the outcome the system currently delivers without recovery investment. |

---

### Scenario Analysis Table

Produce a single unified table with all ten columns in every row.

Do not create separate tables for Distributed Systems Expert columns and Commerce Expert columns. Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts.

| # | Scenario | Class | State | Capability | Data at Risk | Recovery Path | Severity | Blast Radius | Status Quo Risk |
|---|----------|-------|-------|------------|--------------|---------------|----------|--------------|-----------------|
| 1 | | | | | | | | | |
| 2 | | | | | | | | | |
| 3 | | | | | | | | | |

---

### Phase Gate

Produce all three rows before writing the Gap Register. Before advancing to the Gap Register, confirm that all three rows are present and all ten columns contain non-placeholder content in every row. If the Recovery Path cell is missing any of the four stages, or if Status Quo Risk is placeholder, fill it before continuing.

---

### Row Descriptor Table

Each row has a governing descriptor positioned at the row it governs. The bold imperative in each descriptor is load-bearing — read it at the moment you construct that row.

| # | Scenario Class | Content Descriptor |
|---|---------------|-------------------|
| 1 | Class 1 — Full Connectivity Loss | Row 1 covers a commerce operation where the client loses all network connectivity mid-flow (e.g., checkout initiated, device goes offline before payment confirmation). State: name the local cache state and what data was last durably written; identify whether the system is AP or CP under this failure. Capability: enumerate what the user can still interact with locally versus what requires server round-trip. Data at Risk: identify which cart, session, or reservation data has no durable write. Recovery Path: provide all four stages — Detect (signal), Contain (write queuing or discard strategy), Recover (sync-on-reconnect; idempotency), Validate (confirmation of no duplicate or lost write). Status Quo Risk: name the no-investment outcome — what the user experiences today when connectivity drops mid-checkout (e.g., silent cart loss with no notification, order marked failed with no retry path). **Write this row now.** Fill all ten columns before continuing. **Do not advance to Row 2 until Row 1 contains non-placeholder content in every column including all four Recovery Path stages.** |
| 2 | Class 2 — Partial Service Failure | Row 2 covers a commerce operation where one dependent service (inventory service, payment gateway, or fulfillment orchestrator) becomes unavailable. State: identify which service is down and what downstream state is now stale. Capability: name the specific user action that fails. Data at Risk: identify reservation counts, payment tokens, or order states at risk of inconsistency. Recovery Path: provide all four stages — Detect (how the calling service identifies the dependency is unavailable), Contain (circuit-breaker or bulkhead behavior; fail-fast or queue?), Recover (retry or saga rollback and their idempotency guarantee), Validate (reconciliation confirming no double-execution or orphaned reservation). Status Quo Risk: name what the commerce system currently does with no circuit-breaker or fallback in place — does the failure cascade (all checkouts time out), produce silent duplicate charges, or leave orphaned inventory reservations unreconciled? **Write this row now.** Fill all ten columns before continuing. **Do not advance to Row 3 until Row 2 contains non-placeholder content in every column including all four Recovery Path stages.** |
| 3 | Class 3 — Concurrent Writes / Split-Brain | If node A's version wins: inventory is oversold, cart total is stale, and payment is double-charged. If node B's version wins: order status reverts, coupon redemption is duplicated, and fulfillment fires twice. If naive merge runs: all three consequences compound into an unrecoverable inconsistency. **Write this row now.** State: name the conflict window duration and the resolution policy in effect (last-write-wins, vector-clock merge, application-level reconciliation). Capability: identify what the user sees during the conflict window — visible or silent? Data at Risk: name specific entities per resolution outcome branch. Recovery Path: provide all four stages — Detect (how conflict is identified — vector clock divergence, checksum mismatch, assertion failure), Contain (how conflicting writes are quarantined pending resolution), Recover (resolution strategy and specific commerce consequence per outcome branch), Validate (post-merge confirmation: no outstanding oversell, no duplicate fulfillment, no double-charge). Status Quo Risk: name which of the three merge outcomes is the system's current default in the absence of explicit conflict-resolution investment, and state its current business cost (e.g., last-write-wins producing N% oversell rate, or no detection producing silent duplicate fulfillment). **Do not advance to the Gap Register until Row 3 contains non-placeholder content in every column including all four Recovery Path stages.** |

---

### Anti-Boundary Instruction

All ten columns appear in every row of a single unified table. Column ownership shifts within the row — it is not a sub-table boundary. When filling transitions from D to C or C to D mid-row, do not treat the transition as a role-sequence trigger. Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts.

---

### Gap Register

After completing all three rows of the Scenario Analysis Table, identify exactly three gaps — one of each type. Each gap finding must reference the Status Quo Risk column entry for its row as the named baseline against which the gap is measured.

1. **Offline Experience Gap** — a specific user action that the system cannot support during full offline conditions (Class 1), named to the commerce flow, anchored to the no-resilience baseline from the Status Quo Risk column.
2. **Data Consistency Violation** — a specific entity whose state may diverge between replicas (Class 2 or Class 3), with the named consistency violation type and the status-quo consequence of leaving it unresolved.
3. **Missing Recovery Flow** — a specific scenario where a Recovery Path stage is absent, incomplete, or non-idempotent under replay, with the status-quo default behavior named explicitly.

---

### Findings

Summarize findings in order of business impact (highest first). Each finding must reference its scenario row number from the Scenario Analysis Table, name the specific commerce operation at risk, and state the cost of inaction from the Status Quo Risk column.

---

---

## Variation Summary

| Variation | Axis | Hypothesis |
|-----------|------|-----------|
| **V-01** | Role sequence — D first | DS-first anchoring improves State and Recovery Path precision before commerce grounding |
| **V-02** | Lifecycle emphasis — 4-stage recovery | Phase decomposition forces per-stage enumeration vs single-pattern label |
| **V-03** | Inertia framing — Status Quo Risk column | Naming no-resilience cost per row anchors Gap Register to decision-critical baselines |
| **V-04** | V-01 + V-02 | DS precision + lifecycle depth: densest technical output |
| **V-05** | V-01 + V-02 + V-03 | All three: DS precision + lifecycle depth + explicit inertia cost throughout |

**All five variations preserve all 11 v7 aspirational criteria** (C-17 through C-27): `#` column, anti-split instruction, phase gate naming the section, Row Descriptor Table with bold imperatives inside cells, consequence-enumeration in Row 3 before fill, per-column Column Contract meta-table, four-level architecture table with forward references by exact section title, two-symptom anti-boundary negation.
