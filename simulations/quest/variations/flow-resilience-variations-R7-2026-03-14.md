Written to `simulations/quest/variations/flow-resilience-variations-R7-2026-03-14.md`.

---

## flow-resilience R7 Variations

**Baseline**: V-05 R6, composite 94.21 under v7 (8/19 aspirational).

**Three open criteria** → 5 variations, single-axis first, then combined:

| Version | Axis | Target | Expected composite |
|---------|------|--------|--------------------|
| **V-01** | Architecture forward reference | C-26 only | 94.74 |
| **V-02** | Consequence-enumeration before fill | C-27 only | 94.74 |
| **V-03** | Per-row field table schema | C-19 only | 94.74 |
| **V-04** | Forward reference + consequence-enumeration | C-26 + C-27 | 95.26 |
| **V-05** | All three axes | C-19 + C-26 + C-27 | **95.79** |

### What each change does

**C-26 (V-01, V-04, V-05)** — The architecture table's Column and Slot row Mechanism entries now name downstream sections by exact title: "**Column Contract** section below" and "**Row Descriptors** / **Row Descriptor Table** section below." R6 V-05's Slot entry described the mechanism's function without naming the section title — C-26 requires the title pointer.

**C-27 (V-02, V-04, V-05)** — Row 3 gets a *Resolution-outcome stakes* paragraph *before* the bold `**Write this row now.**` imperative: "oversell if node A wins; double-charge if node B wins; duplicate fulfillment if merge is naive." R6 V-05 had these consequences embedded inside the fill instruction, not before it — C-27 requires the stakes to precede the fill.

**C-19 (V-03, V-05)** — The Row Descriptors prose section is replaced by a **Row Descriptor Table** (# | Scenario Class | Content Descriptor). The `**Write this row now.**` / `**Do not advance**` imperatives are now inside TABLE CELLS at cell granularity — the structural distinction C-19 requires. C-23 continues to pass since imperatives remain co-located at cell granularity; the container changes from prose paragraph to table cell.

### C-19 boundary note
The V-05 ceiling places the C-27 consequence-stakes sentence *inside* the Row Descriptor Table's Row 3 cell, before `**Write this row now.**` — satisfying both C-19 (table cell container) and C-27 (consequences before fill) simultaneously in one structure.
criptor). The **Write this row now.** / **Do not
advance** imperatives now appear inside TABLE CELLS at cell granularity — inside a per-row field
table schema, not prose adjacent to the output table. C-23 continues to pass because imperatives
remain co-located at cell granularity; C-19 now passes because the structural container is a
table, not prose.

---

## V-01 — Architecture-to-Contract Forward Reference (C-26 only)

**Axis**: Architecture forward reference
**Hypothesis**: Adding exact section title pointers to the Four-Level Anti-Omission Architecture
table's Mechanism column — naming "**Column Contract**" and "**Row Descriptors**" as the
downstream artifacts those mechanisms deliver — creates the verifiable closed-loop chain C-26
requires. A reader can confirm each named artifact exists; removing either section breaks the
chain visibly.

---

You are running the flow-resilience signal for topic: `{{topic}}`.

**Expert roles**: Commerce Domain Expert (C) | Distributed Systems Expert (D)

---

### Four-Level Anti-Omission Architecture

This prompt enforces output completeness through a **four-level anti-omission architecture**.
Each level addresses a distinct omission risk at a distinct structural level. No two levels
duplicate each other's function.

| Level | Name | Mechanism | Omission Risk Addressed |
|-------|------|-----------|------------------------|
| **Table** | Unified Index | `#` column — all three scenario rows in one numbered table | A scenario silently dropped when fragmented output creates an unlabeled gap |
| **Section** | Phase Gate | Explicit checkpoint before the Gap Register section | Gap Register written before the scenario table is complete |
| **Column** | Ownership Contract | Per-column Owner and Fill Requirement defined in the **Column Contract** section below | A column omitted when mid-row ownership transition is misread as a table boundary |
| **Slot** | In-Row Imperatives | Bold **Write this row now.** / **Do not advance** imperatives co-located inside the **Row Descriptors** section below | A row skipped after section gate is satisfied — imperatives enforce at cell granularity |

---

### Instructions

Simulate degraded conditions across three resilience classes for `{{topic}}`:

- **Class 1 — Full Client Offline**
- **Class 2 — Partial Service Failure**
- **Class 3 — Eventual Consistency / Split-Brain**

For each class, produce one scenario row following the Column Contract and Row Descriptors below.

---

### Column Contract

Read this table in full before constructing any row. A row is complete only when every column
listed here has a non-placeholder entry.

| Column | Owner | Fill Requirement |
|--------|-------|-----------------|
| # | — | Row number (1, 2, 3). |
| Scenario | Both | Name the failure event and the specific commerce operation affected (checkout, inventory reservation, payment confirmation, order fulfillment). |
| State | D | Describe the exact system state using distributed systems vocabulary. Name the partition state, service health, and the consistency guarantee in effect. |
| Capability | C | List every action the user can still take and every action blocked. Specify the commerce flow in progress. "User can retry" without naming preserved state is insufficient. |
| Data at Risk | C | Name specific entities at risk: which fields, which records, which reservation windows. State the staleness or conflict window where measurable. |
| Recovery Path | D | Name the recovery pattern (saga rollback, idempotent retry, read-repair, LWW, vector clock). State the trigger, the steps, and the terminal healthy state. |
| Severity | D | One of: degraded / impaired / down. |
| Blast Radius | C | Name the affected user segment and scale (all users / checkout-active users / <1% under split-brain). |

---

### Scenario Analysis Table

Produce the table below. Every cell must match the fill requirement in the Column Contract.

| # | Scenario | State *(D)* | Capability *(C)* | Data at Risk *(C)* | Recovery Path *(D)* | Severity *(D)* | Blast Radius *(C)* |
|---|----------|-------------|------------------|--------------------|---------------------|----------------|--------------------|
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |

**Column ownership is not a table boundary.** Do not create separate tables for Commerce Expert
columns and Distributed Systems Expert columns. All eight columns appear in every row of this
single unified table. Do not insert a horizontal rule, heading, or section break between rows
when column ownership shifts.

**Produce all three rows before writing the Gap Register.** No cell may be empty or placeholder.

---

### Row Descriptors

Construct each row using the descriptor below. Each bold imperative is co-located at the row
it governs — it is not a section-level instruction. Read it at the moment you construct that row.

---

**Row 1 — Full Client Offline**

**Write this row now.** Scenario *(Both)*: name a full client-offline event during a `{{topic}}`
commerce operation — checkout submission, cart lock acquisition, payment confirmation, or order
placement. State *(D)*: name the exact partition state, the consistency guarantee in effect
(strong / eventual / causal), and any lock or reservation TTL now running unobserved by the
client. Capability *(C)*: list every action still possible offline; list every action blocked;
name what UI state the client should show but may not. Data at Risk *(C)*: name the specific
fields, records, or reservation windows at risk — state the staleness window and whether loss is
silent or surfaced. Recovery Path *(D)*: name the recovery pattern (saga rollback, optimistic lock
release, idempotent replay); state the trigger (reconnect event, TTL expiry, reconciliation job);
walk the numbered steps; state the terminal healthy state. Severity *(D)*: degraded / impaired /
down. Blast Radius *(C)*: name the affected user segment and scale.

**Do not advance to Row 2 until all eight columns for Row 1 contain non-placeholder content.**

---

**Row 2 — Partial Service Failure**

**Write this row now.** Scenario *(Both)*: name a partial service failure where one named
downstream service is unavailable — inventory service, payment gateway, or fulfillment
orchestrator — while the `{{topic}}` client remains connected. State *(D)*: name the unavailable
service; describe cascading states (inventory reservation timeout, payment pre-auth orphaned,
fulfillment stuck in pending); name the consistency level the system degrades to. Capability *(C)*:
name which flows continue (browse, add-to-cart, saved order retrieval); name which are blocked
(new checkout, payment capture, fulfillment initiation); state whether degradation is graceful
(user informed) or silent (user submits into a black hole). Data at Risk *(C)*: name the specific
orphaned entity — reservation record, pre-authorization token, cart lock ID — and the TTL before
it causes harm. Recovery Path *(D)*: name the pattern; state whether recovery is automatic
(circuit breaker closes, saga compensates) or requires manual operator action; name the
idempotency key used to prevent double-processing on replay. Severity *(D)*: degraded / impaired
/ down. Blast Radius *(C)*: name affected segment.

**Do not advance to Row 3 until all eight columns for Row 2 contain non-placeholder content.**

---

**Row 3 — Eventual Consistency / Split-Brain**

**Write this row now.** Scenario *(Both)*: name a split-brain event where concurrent writes
create conflicting state in a specific `{{topic}}` entity — inventory count, cart total, order
status, or coupon redemption record. State *(D)*: describe the diverged state on each node; name
the conflict window duration; state the system's current conflict-resolution policy (LWW, vector
clock, application-level merge, none). Capability *(C)*: name what the user sees and can do
during the conflict window; name what is inconsistent or stale; name what the user cannot know is
wrong. Data at Risk *(C)*: name the specific field in conflict; state the business consequence of
each resolution outcome (oversell if A wins, double-charge if B wins, duplicate fulfillment if
merge is naive). Recovery Path *(D)*: name the resolution strategy; state who or what resolves;
describe the post-resolution downstream reconciliation. Severity *(D)*: degraded / impaired /
down. Blast Radius *(C)*: name affected segment and scale.

**Do not advance to the Gap Register until all eight columns for Row 3 contain non-placeholder content.**

---

**Section gate**: Before writing the Gap Register, confirm all three rows are present and all
eight columns are filled in every row. If any cell is missing, fill it before continuing.

---

### Gap Register

Identify three findings revealed by the scenario analysis:

**Offline Experience Gap**: Name the specific capability in `{{topic}}` unavailable when the
client is fully offline with no degraded fallback. Name the user action that fails silently or
without feedback. State what a minimal offline-capable design would require (local queue,
optimistic write, conflict token).

**Data Consistency Violation**: Name the specific entity and field in `{{topic}}` where concurrent
writes can produce irreconcilable state. State the resolution policy that is absent. Name the
business consequence (oversell, double-charge, duplicate fulfillment order).

**Missing Recovery Flow**: Name the failure entry point in `{{topic}}` that has no documented
recovery exit. Describe the scenario in which a user or automated process could be stuck
indefinitely. State the minimum recovery flow required: the trigger, the steps, and the terminal
state.

Each finding must be labeled, specific, and anchored to `{{topic}}`. Generic findings fail.

---

**Signal artifact**: Write output to `{{topic}}-flow-resilience-{{date}}.md`.

---

---

## V-02 — Consequence-Enumeration Before Fill (C-27 only)

**Axis**: Consequence-enumeration in slot-level descriptors
**Hypothesis**: Placing per-outcome business consequences as explicit stakes *before* the
**Write this row now.** imperative in Row 3 — as a *Resolution-outcome stakes* paragraph naming
what each resolution outcome costs — elevates the descriptor from content specification to outcome
specification. A model that reads named consequences before filling the cell faces a visible
standard of adequacy; a generic recovery path answer is inadequate against named stakes.

---

You are running the flow-resilience signal for topic: `{{topic}}`.

**Expert roles**: Commerce Domain Expert (C) | Distributed Systems Expert (D)

---

### Four-Level Anti-Omission Architecture

This prompt enforces output completeness through a **four-level anti-omission architecture**.
Each level addresses a distinct omission risk at a distinct structural level. No two levels
duplicate each other's function.

| Level | Name | Mechanism | Omission Risk Addressed |
|-------|------|-----------|------------------------|
| **Table** | Unified Index | `#` column — all three scenario rows in one numbered table | A scenario silently dropped when fragmented output creates an unlabeled gap |
| **Section** | Phase Gate | Explicit checkpoint before the Gap Register section | Gap Register written before the scenario table is complete |
| **Column** | Ownership Contract | Per-column expert-role label defined in the Column Contract (below) | A column omitted when mid-row ownership transition is misread as a table boundary |
| **Slot** | In-Row Imperatives | Bold "Write this row now." / "Do not advance" embedded in each row's Content descriptor | A row skipped after section gate is satisfied — imperatives enforce at cell granularity |

---

### Instructions

Simulate degraded conditions across three resilience classes for `{{topic}}`:

- **Class 1 — Full Client Offline**
- **Class 2 — Partial Service Failure**
- **Class 3 — Eventual Consistency / Split-Brain**

For each class, produce one scenario row following the Column Contract and Row Descriptors below.

---

### Column Contract

Read this table in full before constructing any row. A row is complete only when every column
listed here has a non-placeholder entry.

| Column | Owner | Fill Requirement |
|--------|-------|-----------------|
| # | — | Row number (1, 2, 3). |
| Scenario | Both | Name the failure event and the specific commerce operation affected (checkout, inventory reservation, payment confirmation, order fulfillment). |
| State | D | Describe the exact system state using distributed systems vocabulary. Name the partition state, service health, and the consistency guarantee in effect. |
| Capability | C | List every action the user can still take and every action blocked. Specify the commerce flow in progress. "User can retry" without naming preserved state is insufficient. |
| Data at Risk | C | Name specific entities at risk: which fields, which records, which reservation windows. State the staleness or conflict window where measurable. |
| Recovery Path | D | Name the recovery pattern (saga rollback, idempotent retry, read-repair, LWW, vector clock). State the trigger, the steps, and the terminal healthy state. |
| Severity | D | One of: degraded / impaired / down. |
| Blast Radius | C | Name the affected user segment and scale (all users / checkout-active users / <1% under split-brain). |

---

### Scenario Analysis Table

Produce the table below. Every cell must match the fill requirement in the Column Contract.

| # | Scenario | State *(D)* | Capability *(C)* | Data at Risk *(C)* | Recovery Path *(D)* | Severity *(D)* | Blast Radius *(C)* |
|---|----------|-------------|------------------|--------------------|---------------------|----------------|--------------------|
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |

**Column ownership is not a table boundary.** Do not create separate tables for Commerce Expert
columns and Distributed Systems Expert columns. All eight columns appear in every row of this
single unified table. Do not insert a horizontal rule, heading, or section break between rows
when column ownership shifts.

**Produce all three rows before writing the Gap Register.** No cell may be empty or placeholder.

---

### Row Descriptors

Construct each row using the descriptor below. Each bold imperative is co-located at the row
it governs — it is not a section-level instruction. Read it at the moment you construct that row.

---

**Row 1 — Full Client Offline**

**Write this row now.** Scenario *(Both)*: name a full client-offline event during a `{{topic}}`
commerce operation — checkout submission, cart lock acquisition, payment confirmation, or order
placement. State *(D)*: name the exact partition state, the consistency guarantee in effect
(strong / eventual / causal), and any lock or reservation TTL now running unobserved by the
client. Capability *(C)*: list every action still possible offline; list every action blocked;
name what UI state the client should show but may not. Data at Risk *(C)*: name the specific
fields, records, or reservation windows at risk — state the staleness window and whether loss is
silent or surfaced. Recovery Path *(D)*: name the recovery pattern (saga rollback, optimistic lock
release, idempotent replay); state the trigger (reconnect event, TTL expiry, reconciliation job);
walk the numbered steps; state the terminal healthy state. Severity *(D)*: degraded / impaired /
down. Blast Radius *(C)*: name the affected user segment and scale.

**Do not advance to Row 2 until all eight columns for Row 1 contain non-placeholder content.**

---

**Row 2 — Partial Service Failure**

**Write this row now.** Scenario *(Both)*: name a partial service failure where one named
downstream service is unavailable — inventory service, payment gateway, or fulfillment
orchestrator — while the `{{topic}}` client remains connected. State *(D)*: name the unavailable
service; describe cascading states (inventory reservation timeout, payment pre-auth orphaned,
fulfillment stuck in pending); name the consistency level the system degrades to. Capability *(C)*:
name which flows continue (browse, add-to-cart, saved order retrieval); name which are blocked
(new checkout, payment capture, fulfillment initiation); state whether degradation is graceful
(user informed) or silent (user submits into a black hole). Data at Risk *(C)*: name the specific
orphaned entity — reservation record, pre-authorization token, cart lock ID — and the TTL before
it causes harm. Recovery Path *(D)*: name the pattern; state whether recovery is automatic
(circuit breaker closes, saga compensates) or requires manual operator action; name the
idempotency key used to prevent double-processing on replay. Severity *(D)*: degraded / impaired
/ down. Blast Radius *(C)*: name affected segment.

**Do not advance to Row 3 until all eight columns for Row 2 contain non-placeholder content.**

---

**Row 3 — Eventual Consistency / Split-Brain**

*Resolution-outcome stakes*: oversell if the inventory-count write from node A wins over node
B's concurrent reservation write; double-charge if a payment-authorization record on one node
survives while a capture transaction completes on the other; duplicate fulfillment order if a
naive merge commits two order records from the same cart event. These are distinct business
consequences — not technical errors — that make each resolution outcome non-equivalent. A vague
recovery path is inadequate against named stakes.

**Write this row now.** Scenario *(Both)*: name a split-brain event where concurrent writes
create conflicting state in a specific `{{topic}}` entity — inventory count, cart total, order
status, or coupon redemption record. State *(D)*: describe the diverged state on each node; name
the conflict window duration; state the system's current conflict-resolution policy (LWW, vector
clock, application-level merge, none). Capability *(C)*: name what the user sees and can do
during the conflict window; name what is inconsistent or stale; name what the user cannot know is
wrong. Data at Risk *(C)*: name the specific field in conflict and its conflict window duration.
Recovery Path *(D)*: name the resolution strategy; state who or what resolves; describe the
post-resolution downstream reconciliation required to address the consequence named above.
Severity *(D)*: degraded / impaired / down. Blast Radius *(C)*: name affected segment and scale.

**Do not advance to the Gap Register until all eight columns for Row 3 contain non-placeholder content.**

---

**Section gate**: Before writing the Gap Register, confirm all three rows are present and all
eight columns are filled in every row. If any cell is missing, fill it before continuing.

---

### Gap Register

Identify three findings revealed by the scenario analysis:

**Offline Experience Gap**: Name the specific capability in `{{topic}}` unavailable when the
client is fully offline with no degraded fallback. Name the user action that fails silently or
without feedback. State what a minimal offline-capable design would require (local queue,
optimistic write, conflict token).

**Data Consistency Violation**: Name the specific entity and field in `{{topic}}` where concurrent
writes can produce irreconcilable state. State the resolution policy that is absent. Name the
business consequence (oversell, double-charge, duplicate fulfillment order).

**Missing Recovery Flow**: Name the failure entry point in `{{topic}}` that has no documented
recovery exit. Describe the scenario in which a user or automated process could be stuck
indefinitely. State the minimum recovery flow required: the trigger, the steps, and the terminal
state.

Each finding must be labeled, specific, and anchored to `{{topic}}`. Generic findings fail.

---

**Signal artifact**: Write output to `{{topic}}-flow-resilience-{{date}}.md`.

---

---

## V-03 — Per-Row Field Table Schema (C-19 only)

**Axis**: Slot-level imperatives inside per-row field table schema
**Hypothesis**: Converting the Row Descriptors prose section into a Row Descriptor Table
(# | Scenario Class | Content Descriptor) places the **Write this row now.** /
**Do not advance** imperatives inside TABLE CELLS at cell granularity. This satisfies C-19's
structural requirement — the imperative inside a per-row field table schema, not in prose adjacent
to the output table. C-23 continues to pass because the imperatives remain co-located at cell
granularity; the container changes from prose paragraph to table cell.

---

You are running the flow-resilience signal for topic: `{{topic}}`.

**Expert roles**: Commerce Domain Expert (C) | Distributed Systems Expert (D)

---

### Four-Level Anti-Omission Architecture

This prompt enforces output completeness through a **four-level anti-omission architecture**.
Each level addresses a distinct omission risk at a distinct structural level. No two levels
duplicate each other's function.

| Level | Name | Mechanism | Omission Risk Addressed |
|-------|------|-----------|------------------------|
| **Table** | Unified Index | `#` column — all three scenario rows in one numbered table | A scenario silently dropped when fragmented output creates an unlabeled gap |
| **Section** | Phase Gate | Explicit checkpoint before the Gap Register section | Gap Register written before the scenario table is complete |
| **Column** | Ownership Contract | Per-column expert-role label defined in the Column Contract (below) | A column omitted when mid-row ownership transition is misread as a table boundary |
| **Slot** | In-Row Imperatives | Bold "Write this row now." / "Do not advance" embedded inside each row's cell in the Row Descriptor Table below | A row skipped after section gate is satisfied — imperatives enforce at cell granularity |

---

### Instructions

Simulate degraded conditions across three resilience classes for `{{topic}}`:

- **Class 1 — Full Client Offline**
- **Class 2 — Partial Service Failure**
- **Class 3 — Eventual Consistency / Split-Brain**

For each class, produce one scenario row following the Column Contract and Row Descriptor Table below.

---

### Column Contract

Read this table in full before constructing any row. A row is complete only when every column
listed here has a non-placeholder entry.

| Column | Owner | Fill Requirement |
|--------|-------|-----------------|
| # | — | Row number (1, 2, 3). |
| Scenario | Both | Name the failure event and the specific commerce operation affected (checkout, inventory reservation, payment confirmation, order fulfillment). |
| State | D | Describe the exact system state using distributed systems vocabulary. Name the partition state, service health, and the consistency guarantee in effect. |
| Capability | C | List every action the user can still take and every action blocked. Specify the commerce flow in progress. "User can retry" without naming preserved state is insufficient. |
| Data at Risk | C | Name specific entities at risk: which fields, which records, which reservation windows. State the staleness or conflict window where measurable. |
| Recovery Path | D | Name the recovery pattern (saga rollback, idempotent retry, read-repair, LWW, vector clock). State the trigger, the steps, and the terminal healthy state. |
| Severity | D | One of: degraded / impaired / down. |
| Blast Radius | C | Name the affected user segment and scale (all users / checkout-active users / <1% under split-brain). |

---

### Scenario Analysis Table

Produce the table below. Every cell must match the fill requirement in the Column Contract.

| # | Scenario | State *(D)* | Capability *(C)* | Data at Risk *(C)* | Recovery Path *(D)* | Severity *(D)* | Blast Radius *(C)* |
|---|----------|-------------|------------------|--------------------|---------------------|----------------|--------------------|
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |

**Column ownership is not a table boundary.** Do not create separate tables for Commerce Expert
columns and Distributed Systems Expert columns. All eight columns appear in every row of this
single unified table. Do not insert a horizontal rule, heading, or section break between rows
when column ownership shifts.

**Produce all three rows before writing the Gap Register.** No cell may be empty or placeholder.

---

### Row Descriptor Table

The table below specifies fill requirements for each output row. The bold imperative inside each
Content Descriptor cell is co-located at cell granularity — it governs that row, not this section.
Read each imperative at the moment you construct that row.

| # | Scenario Class | Content Descriptor |
|---|---------------|-------------------|
| 1 | Full Client Offline | **Write this row now.** Scenario (Both): name a full client-offline event during a `{{topic}}` commerce operation — checkout submission, cart lock acquisition, payment confirmation, or order placement. State (D): name the exact partition state, the consistency guarantee in effect (strong / eventual / causal), and any lock or reservation TTL now running unobserved by the client. Capability (C): list every action still possible offline; list every action blocked; name what UI state the client should show but may not. Data at Risk (C): name the specific fields, records, or reservation windows at risk — state the staleness window and whether loss is silent or surfaced. Recovery Path (D): name the recovery pattern (saga rollback, optimistic lock release, idempotent replay); state the trigger (reconnect event, TTL expiry, reconciliation job); walk the numbered steps; state the terminal healthy state. Severity (D): degraded / impaired / down. Blast Radius (C): name the affected user segment and scale. **Do not advance to Row 2 until all eight columns for Row 1 contain non-placeholder content.** |
| 2 | Partial Service Failure | **Write this row now.** Scenario (Both): name a partial service failure where one named downstream service is unavailable — inventory service, payment gateway, or fulfillment orchestrator — while the `{{topic}}` client remains connected. State (D): name the unavailable service; describe cascading states (reservation timeout, payment pre-auth orphaned, fulfillment stuck in pending); name the consistency level the system degrades to. Capability (C): name which flows continue (browse, add-to-cart, saved order retrieval); name which are blocked (new checkout, payment capture, fulfillment initiation); state whether degradation is graceful (user informed) or silent (user submits into a black hole). Data at Risk (C): name the specific orphaned entity — reservation record, pre-authorization token, cart lock ID — and the TTL before it causes harm. Recovery Path (D): name the pattern; state whether recovery is automatic (circuit breaker closes, saga compensates) or requires manual operator action; name the idempotency key used to prevent double-processing on replay. Severity (D): degraded / impaired / down. Blast Radius (C): name affected segment. **Do not advance to Row 3 until all eight columns for Row 2 contain non-placeholder content.** |
| 3 | Eventual Consistency / Split-Brain | **Write this row now.** Scenario (Both): name a split-brain event where concurrent writes create conflicting state in a specific `{{topic}}` entity — inventory count, cart total, order status, or coupon redemption record. State (D): describe the diverged state on each node; name the conflict window duration; state the system's current conflict-resolution policy (LWW, vector clock, application-level merge, none). Capability (C): name what the user sees and can do during the conflict window; name what is inconsistent or stale; name what the user cannot know is wrong. Data at Risk (C): name the specific field in conflict; state the business consequence of each resolution outcome (oversell if A wins, double-charge if B wins, duplicate fulfillment if merge is naive). Recovery Path (D): name the resolution strategy; state who or what resolves; describe the post-resolution downstream reconciliation. Severity (D): degraded / impaired / down. Blast Radius (C): name affected segment and scale. **Do not advance to the Gap Register until all eight columns for Row 3 contain non-placeholder content.** |

---

**Section gate**: Before writing the Gap Register, confirm all three rows are present and all
eight columns are filled in every row. If any cell is missing, fill it before continuing.

---

### Gap Register

Identify three findings revealed by the scenario analysis:

**Offline Experience Gap**: Name the specific capability in `{{topic}}` unavailable when the
client is fully offline with no degraded fallback. Name the user action that fails silently or
without feedback. State what a minimal offline-capable design would require (local queue,
optimistic write, conflict token).

**Data Consistency Violation**: Name the specific entity and field in `{{topic}}` where concurrent
writes can produce irreconcilable state. State the resolution policy that is absent. Name the
business consequence (oversell, double-charge, duplicate fulfillment order).

**Missing Recovery Flow**: Name the failure entry point in `{{topic}}` that has no documented
recovery exit. Describe the scenario in which a user or automated process could be stuck
indefinitely. State the minimum recovery flow required: the trigger, the steps, and the terminal
state.

Each finding must be labeled, specific, and anchored to `{{topic}}`. Generic findings fail.

---

**Signal artifact**: Write output to `{{topic}}-flow-resilience-{{date}}.md`.

---

---

## V-04 — Architecture Forward Reference + Consequence-Enumeration (C-26 + C-27)

**Axes**: Architecture forward reference + consequence-enumeration before fill
**Hypothesis**: Combining exact section title pointers in the architecture table (C-26) with a
consequence-stakes paragraph before Row 3's bold imperative (C-27) targets two of the three R7
open criteria without structural interference. C-26 changes only the architecture table Mechanism
column; C-27 adds a consequence paragraph before Row 3's **Write this row now.**. Neither
change disrupts the other or the 8 inherited passing criteria.

---

You are running the flow-resilience signal for topic: `{{topic}}`.

**Expert roles**: Commerce Domain Expert (C) | Distributed Systems Expert (D)

---

### Four-Level Anti-Omission Architecture

This prompt enforces output completeness through a **four-level anti-omission architecture**.
Each level addresses a distinct omission risk at a distinct structural level. No two levels
duplicate each other's function.

| Level | Name | Mechanism | Omission Risk Addressed |
|-------|------|-----------|------------------------|
| **Table** | Unified Index | `#` column — all three scenario rows in one numbered table | A scenario silently dropped when fragmented output creates an unlabeled gap |
| **Section** | Phase Gate | Explicit checkpoint before the Gap Register section | Gap Register written before the scenario table is complete |
| **Column** | Ownership Contract | Per-column Owner and Fill Requirement defined in the **Column Contract** section below | A column omitted when mid-row ownership transition is misread as a table boundary |
| **Slot** | In-Row Imperatives | Bold **Write this row now.** / **Do not advance** imperatives co-located inside the **Row Descriptors** section below | A row skipped after section gate is satisfied — imperatives enforce at cell granularity |

---

### Instructions

Simulate degraded conditions across three resilience classes for `{{topic}}`:

- **Class 1 — Full Client Offline**
- **Class 2 — Partial Service Failure**
- **Class 3 — Eventual Consistency / Split-Brain**

For each class, produce one scenario row following the Column Contract and Row Descriptors below.

---

### Column Contract

Read this table in full before constructing any row. A row is complete only when every column
listed here has a non-placeholder entry.

| Column | Owner | Fill Requirement |
|--------|-------|-----------------|
| # | — | Row number (1, 2, 3). |
| Scenario | Both | Name the failure event and the specific commerce operation affected (checkout, inventory reservation, payment confirmation, order fulfillment). |
| State | D | Describe the exact system state using distributed systems vocabulary. Name the partition state, service health, and the consistency guarantee in effect. |
| Capability | C | List every action the user can still take and every action blocked. Specify the commerce flow in progress. "User can retry" without naming preserved state is insufficient. |
| Data at Risk | C | Name specific entities at risk: which fields, which records, which reservation windows. State the staleness or conflict window where measurable. |
| Recovery Path | D | Name the recovery pattern (saga rollback, idempotent retry, read-repair, LWW, vector clock). State the trigger, the steps, and the terminal healthy state. |
| Severity | D | One of: degraded / impaired / down. |
| Blast Radius | C | Name the affected user segment and scale (all users / checkout-active users / <1% under split-brain). |

---

### Scenario Analysis Table

Produce the table below. Every cell must match the fill requirement in the Column Contract.

| # | Scenario | State *(D)* | Capability *(C)* | Data at Risk *(C)* | Recovery Path *(D)* | Severity *(D)* | Blast Radius *(C)* |
|---|----------|-------------|------------------|--------------------|---------------------|----------------|--------------------|
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |

**Column ownership is not a table boundary.** Do not create separate tables for Commerce Expert
columns and Distributed Systems Expert columns. All eight columns appear in every row of this
single unified table. Do not insert a horizontal rule, heading, or section break between rows
when column ownership shifts.

**Produce all three rows before writing the Gap Register.** No cell may be empty or placeholder.

---

### Row Descriptors

Construct each row using the descriptor below. Each bold imperative is co-located at the row
it governs — it is not a section-level instruction. Read it at the moment you construct that row.

---

**Row 1 — Full Client Offline**

**Write this row now.** Scenario *(Both)*: name a full client-offline event during a `{{topic}}`
commerce operation — checkout submission, cart lock acquisition, payment confirmation, or order
placement. State *(D)*: name the exact partition state, the consistency guarantee in effect
(strong / eventual / causal), and any lock or reservation TTL now running unobserved by the
client. Capability *(C)*: list every action still possible offline; list every action blocked;
name what UI state the client should show but may not. Data at Risk *(C)*: name the specific
fields, records, or reservation windows at risk — state the staleness window and whether loss is
silent or surfaced. Recovery Path *(D)*: name the recovery pattern (saga rollback, optimistic lock
release, idempotent replay); state the trigger (reconnect event, TTL expiry, reconciliation job);
walk the numbered steps; state the terminal healthy state. Severity *(D)*: degraded / impaired /
down. Blast Radius *(C)*: name the affected user segment and scale.

**Do not advance to Row 2 until all eight columns for Row 1 contain non-placeholder content.**

---

**Row 2 — Partial Service Failure**

**Write this row now.** Scenario *(Both)*: name a partial service failure where one named
downstream service is unavailable — inventory service, payment gateway, or fulfillment
orchestrator — while the `{{topic}}` client remains connected. State *(D)*: name the unavailable
service; describe cascading states (inventory reservation timeout, payment pre-auth orphaned,
fulfillment stuck in pending); name the consistency level the system degrades to. Capability *(C)*:
name which flows continue (browse, add-to-cart, saved order retrieval); name which are blocked
(new checkout, payment capture, fulfillment initiation); state whether degradation is graceful
(user informed) or silent (user submits into a black hole). Data at Risk *(C)*: name the specific
orphaned entity — reservation record, pre-authorization token, cart lock ID — and the TTL before
it causes harm. Recovery Path *(D)*: name the pattern; state whether recovery is automatic
(circuit breaker closes, saga compensates) or requires manual operator action; name the
idempotency key used to prevent double-processing on replay. Severity *(D)*: degraded / impaired
/ down. Blast Radius *(C)*: name affected segment.

**Do not advance to Row 3 until all eight columns for Row 2 contain non-placeholder content.**

---

**Row 3 — Eventual Consistency / Split-Brain**

*Resolution-outcome stakes*: oversell if the inventory-count write from node A wins over node
B's concurrent reservation write; double-charge if a payment-authorization record on one node
survives while a capture transaction completes on the other; duplicate fulfillment order if a
naive merge commits two order records from the same cart event. These are distinct business
consequences — not technical errors — that make each resolution outcome non-equivalent. A vague
recovery path is inadequate against named stakes.

**Write this row now.** Scenario *(Both)*: name a split-brain event where concurrent writes
create conflicting state in a specific `{{topic}}` entity — inventory count, cart total, order
status, or coupon redemption record. State *(D)*: describe the diverged state on each node; name
the conflict window duration; state the system's current conflict-resolution policy (LWW, vector
clock, application-level merge, none). Capability *(C)*: name what the user sees and can do
during the conflict window; name what is inconsistent or stale; name what the user cannot know is
wrong. Data at Risk *(C)*: name the specific field in conflict and its conflict window duration.
Recovery Path *(D)*: name the resolution strategy; state who or what resolves; describe the
post-resolution downstream reconciliation required to address the consequence named above.
Severity *(D)*: degraded / impaired / down. Blast Radius *(C)*: name affected segment and scale.

**Do not advance to the Gap Register until all eight columns for Row 3 contain non-placeholder content.**

---

**Section gate**: Before writing the Gap Register, confirm all three rows are present and all
eight columns are filled in every row. If any cell is missing, fill it before continuing.

---

### Gap Register

Identify three findings revealed by the scenario analysis:

**Offline Experience Gap**: Name the specific capability in `{{topic}}` unavailable when the
client is fully offline with no degraded fallback. Name the user action that fails silently or
without feedback. State what a minimal offline-capable design would require (local queue,
optimistic write, conflict token).

**Data Consistency Violation**: Name the specific entity and field in `{{topic}}` where concurrent
writes can produce irreconcilable state. State the resolution policy that is absent. Name the
business consequence (oversell, double-charge, duplicate fulfillment order).

**Missing Recovery Flow**: Name the failure entry point in `{{topic}}` that has no documented
recovery exit. Describe the scenario in which a user or automated process could be stuck
indefinitely. State the minimum recovery flow required: the trigger, the steps, and the terminal
state.

Each finding must be labeled, specific, and anchored to `{{topic}}`. Generic findings fail.

---

**Signal artifact**: Write output to `{{topic}}-flow-resilience-{{date}}.md`.

---

---

## V-05 — Ceiling Attempt: Per-Row Field Table Schema + Forward References + Consequence-Enumeration (C-19 + C-26 + C-27)

**Axes**: All three R7 open criteria
**Hypothesis**: Stacking C-19 (Row Descriptor Table replaces prose Row Descriptors — imperatives
inside table cells), C-26 (architecture table Mechanism column names downstream artifacts by
exact section title — **Column Contract** and **Row Descriptor Table**), and C-27 (Row 3
consequence-stakes enumerated before the bold imperative, inside the table cell) on top of V-05
R6's 8 inherited passing criteria achieves 11/19 = 5.79 aspirational, composite 95.79. Each
criterion targets a distinct structural level; no two changes interfere with each other or the
inherited mechanisms.

---

You are running the flow-resilience signal for topic: `{{topic}}`.

**Expert roles**: Commerce Domain Expert (C) | Distributed Systems Expert (D)

---

### Four-Level Anti-Omission Architecture

This prompt enforces output completeness through a **four-level anti-omission architecture**.
Each level addresses a distinct omission risk at a distinct structural level. No two levels
duplicate each other's function.

| Level | Name | Mechanism | Omission Risk Addressed |
|-------|------|-----------|------------------------|
| **Table** | Unified Index | `#` column — all three scenario rows in one numbered table | A scenario silently dropped when fragmented output creates an unlabeled gap |
| **Section** | Phase Gate | Explicit checkpoint before the Gap Register section | Gap Register written before the scenario table is complete |
| **Column** | Ownership Contract | Per-column Owner and Fill Requirement defined in the **Column Contract** section below | A column omitted when mid-row ownership transition is misread as a table boundary |
| **Slot** | In-Row Imperatives | Bold **Write this row now.** / **Do not advance** imperatives co-located inside cells of the **Row Descriptor Table** section below | A row skipped after section gate is satisfied — imperatives enforce at cell granularity inside the per-row field table schema |

---

### Instructions

Simulate degraded conditions across three resilience classes for `{{topic}}`:

- **Class 1 — Full Client Offline**
- **Class 2 — Partial Service Failure**
- **Class 3 — Eventual Consistency / Split-Brain**

For each class, produce one scenario row following the Column Contract and Row Descriptor Table below.

---

### Column Contract

Read this table in full before constructing any row. A row is complete only when every column
listed here has a non-placeholder entry.

| Column | Owner | Fill Requirement |
|--------|-------|-----------------|
| # | — | Row number (1, 2, 3). |
| Scenario | Both | Name the failure event and the specific commerce operation affected (checkout, inventory reservation, payment confirmation, order fulfillment). |
| State | D | Describe the exact system state using distributed systems vocabulary. Name the partition state, service health, and the consistency guarantee in effect. |
| Capability | C | List every action the user can still take and every action blocked. Specify the commerce flow in progress. "User can retry" without naming preserved state is insufficient. |
| Data at Risk | C | Name specific entities at risk: which fields, which records, which reservation windows. State the staleness or conflict window where measurable. |
| Recovery Path | D | Name the recovery pattern (saga rollback, idempotent retry, read-repair, LWW, vector clock). State the trigger, the steps, and the terminal healthy state. |
| Severity | D | One of: degraded / impaired / down. |
| Blast Radius | C | Name the affected user segment and scale (all users / checkout-active users / <1% under split-brain). |

---

### Scenario Analysis Table

Produce the table below. Every cell must match the fill requirement in the Column Contract.

| # | Scenario | State *(D)* | Capability *(C)* | Data at Risk *(C)* | Recovery Path *(D)* | Severity *(D)* | Blast Radius *(C)* |
|---|----------|-------------|------------------|--------------------|---------------------|----------------|--------------------|
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |

**Column ownership is not a table boundary.** Do not create separate tables for Commerce Expert
columns and Distributed Systems Expert columns. All eight columns appear in every row of this
single unified table. Do not insert a horizontal rule, heading, or section break between rows
when column ownership shifts.

**Produce all three rows before writing the Gap Register.** No cell may be empty or placeholder.

---

### Row Descriptor Table

The table below specifies fill requirements and imperatives for each output row. The bold
imperative inside each Content Descriptor cell is co-located at cell granularity — it governs
that row, not this section. Read each imperative at the moment you construct that row.

| # | Scenario Class | Content Descriptor |
|---|---------------|-------------------|
| 1 | Full Client Offline | **Write this row now.** Scenario (Both): name a full client-offline event during a `{{topic}}` commerce operation — checkout submission, cart lock acquisition, payment confirmation, or order placement. State (D): name the exact partition state, the consistency guarantee in effect (strong / eventual / causal), and any lock or reservation TTL now running unobserved by the client. Capability (C): list every action still possible offline; list every action blocked; name what UI state the client should show but may not. Data at Risk (C): name the specific fields, records, or reservation windows at risk — state the staleness window and whether loss is silent or surfaced. Recovery Path (D): name the recovery pattern (saga rollback, optimistic lock release, idempotent replay); state the trigger (reconnect event, TTL expiry, reconciliation job); walk the numbered steps; state the terminal healthy state. Severity (D): degraded / impaired / down. Blast Radius (C): name the affected user segment and scale. **Do not advance to Row 2 until all eight columns for Row 1 contain non-placeholder content.** |
| 2 | Partial Service Failure | **Write this row now.** Scenario (Both): name a partial service failure where one named downstream service is unavailable — inventory service, payment gateway, or fulfillment orchestrator — while the `{{topic}}` client remains connected. State (D): name the unavailable service; describe cascading states (reservation timeout, payment pre-auth orphaned, fulfillment stuck in pending); name the consistency level the system degrades to. Capability (C): name which flows continue (browse, add-to-cart, saved order retrieval); name which are blocked (new checkout, payment capture, fulfillment initiation); state whether degradation is graceful (user informed) or silent (user submits into a black hole). Data at Risk (C): name the specific orphaned entity — reservation record, pre-authorization token, cart lock ID — and the TTL before it causes harm. Recovery Path (D): name the pattern; state whether recovery is automatic (circuit breaker closes, saga compensates) or requires manual operator action; name the idempotency key used to prevent double-processing on replay. Severity (D): degraded / impaired / down. Blast Radius (C): name affected segment. **Do not advance to Row 3 until all eight columns for Row 2 contain non-placeholder content.** |
| 3 | Eventual Consistency / Split-Brain | *Resolution-outcome stakes*: oversell if the inventory-count write from node A wins over node B's concurrent reservation write; double-charge if a payment-authorization record on one node survives while a capture transaction completes on the other; duplicate fulfillment order if a naive merge commits two order records from the same cart event. These are distinct business consequences — not technical errors — that make each resolution outcome non-equivalent. **Write this row now.** Scenario (Both): name a split-brain event where concurrent writes create conflicting state in a specific `{{topic}}` entity — inventory count, cart total, order status, or coupon redemption record. State (D): describe the diverged state on each node; name the conflict window duration; state the system's current conflict-resolution policy (LWW, vector clock, application-level merge, none). Capability (C): name what the user sees and can do during the conflict window; name what is inconsistent or stale; name what the user cannot know is wrong. Data at Risk (C): name the specific field in conflict and its conflict window duration. Recovery Path (D): name the resolution strategy; state who or what resolves; describe the post-resolution downstream reconciliation required to address the consequence named above. Severity (D): degraded / impaired / down. Blast Radius (C): name affected segment and scale. **Do not advance to the Gap Register until all eight columns for Row 3 contain non-placeholder content.** |

---

**Section gate**: Before writing the Gap Register, confirm all three rows are present and all
eight columns are filled in every row. If any cell is missing, fill it before continuing.

---

### Gap Register

Identify three findings revealed by the scenario analysis:

**Offline Experience Gap**: Name the specific capability in `{{topic}}` unavailable when the
client is fully offline with no degraded fallback. Name the user action that fails silently or
without feedback. State what a minimal offline-capable design would require (local queue,
optimistic write, conflict token).

**Data Consistency Violation**: Name the specific entity and field in `{{topic}}` where concurrent
writes can produce irreconcilable state. State the resolution policy that is absent. Name the
business consequence (oversell, double-charge, duplicate fulfillment order).

**Missing Recovery Flow**: Name the failure entry point in `{{topic}}` that has no documented
recovery exit. Describe the scenario in which a user or automated process could be stuck
indefinitely. State the minimum recovery flow required: the trigger, the steps, and the terminal
state.

Each finding must be labeled, specific, and anchored to `{{topic}}`. Generic findings fail.

---

**Signal artifact**: Write output to `{{topic}}-flow-resilience-{{date}}.md`.

---

## Variation Summary

| Version | Axes | Open Criteria Targeted | Expected Aspirational | Expected Composite |
|---------|------|------------------------|----------------------|--------------------|
| V-01 | Architecture forward reference | C-26 only | 9/19 = 4.74 | 94.74 |
| V-02 | Consequence-enumeration before fill | C-27 only | 9/19 = 4.74 | 94.74 |
| V-03 | Per-row field table schema | C-19 only | 9/19 = 4.74 | 94.74 |
| V-04 | Forward reference + consequence-enumeration | C-26 + C-27 | 10/19 = 5.26 | 95.26 |
| V-05 | Field table schema + forward reference + consequence-enumeration | C-19 + C-26 + C-27 | 11/19 = 5.79 | **95.79** |

**Inherited passes in all variations** (from V-05 R6 baseline): C-17, C-18, C-20, C-21, C-22, C-23, C-24, C-25.

**C-19 boundary**: V-03 and V-05 replace the Row Descriptors prose section with a Row Descriptor
Table (# | Scenario Class | Content Descriptor). Imperatives are now inside TABLE CELLS,
satisfying C-19's "per-row field table schema" requirement. C-23 continues to pass because
imperatives remain at cell granularity. V-01, V-02, V-04 retain prose Row Descriptors — C-23
passes, C-19 fails.

**C-26 boundary**: V-01, V-04, V-05 update the architecture table's Column and Slot row Mechanism
entries to name downstream artifacts by exact section title ("**Column Contract**" and
"**Row Descriptors**" or "**Row Descriptor Table**"). V-02 and V-03 retain R6 V-05's architecture
table — Slot entry describes mechanism function without a section title pointer, C-26 fails.

**C-27 boundary**: V-02, V-04, V-05 place a *Resolution-outcome stakes* paragraph (or sentence
block in the table cell) before the **Write this row now.** imperative in Row 3, enumerating
per-outcome consequences before the fill instruction. V-01 and V-03 retain R6 V-05's Row 3
structure — consequences embedded within the fill instruction, not before it, C-27 fails.
