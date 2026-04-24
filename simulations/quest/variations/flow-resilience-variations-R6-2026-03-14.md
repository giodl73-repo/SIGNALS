**flow-resilience R6 variations written** to `simulations/quest/variations/flow-resilience-variations-R6-2026-03-14.md`.

---

## Summary

**Baseline**: V-02 from R5 (composite 92.94 under v6), passing C-17, C-18, C-20, C-22, C-25.

**Three open criteria** targeted across 5 variations:

| Version | Axis | Target | Expected composite |
|---------|------|--------|--------------------|
| **V-01** | Output format | **C-24 only** — splits V-02's combined column-spec block into two discrete structures: a standalone `Column Contract` meta-table, then a separate blank `Scenario Analysis Table` template | 93.53 |
| **V-02** | Anti-omission architecture | **C-21 only** — adds a `Four-Level Anti-Omission Architecture` section that explicitly names all four levels (Table / Section / Column / Slot) with mechanism and omission risk per level | 93.53 |
| **V-03** | Slot-level imperatives | **C-23 only** — adds per-row `Row Descriptors` with `**Write this row now.**` / `**Do not advance to Row N until...**` embedded inline in each row's Content description | 93.53 |
| **V-04** | Format + architecture | **C-24 + C-21** | 94.12 |
| **V-05** | All three axes | **C-21 + C-23 + C-24** — ceiling attempt | **94.71** |

**Key C-24 insight**: V-02 R5 already had a column-spec table but failed C-24 because it was the instruction block — no separate output table template followed it. R6 fixes this by making them two distinct sections.
� Eventual Consistency / Split-Brain**

For each class, produce one scenario row in the Scenario Analysis Table below.

---

### Column Contract

The following table defines every column in the output. Read it in full before constructing any row.
A row is complete only when every column listed here has a non-placeholder entry.

| Column | Owner | Fill Requirement |
|--------|-------|-----------------|
| # | — | Row number (1, 2, 3). |
| Scenario | Both | Name the failure event and the specific commerce operation affected (checkout, inventory reservation, payment confirmation, order fulfillment). |
| State | D | Describe the exact system state using distributed systems vocabulary. Name the partition state, service health, and the consistency guarantee in effect. |
| Capability | C | List every action the user can still take. List every action that is blocked. Be specific to the commerce flow in progress. "User can retry" without specifying preserved state is insufficient. |
| Data at Risk | C | Name specific entities at risk: which fields, which records, which reservation windows. State the staleness or conflict window where measurable. |
| Recovery Path | D | Name the recovery pattern (saga rollback, idempotent retry, read-repair, LWW, vector clock). State the trigger, the steps, and the terminal healthy state. |
| Severity | D | One of: degraded / impaired / down. |
| Blast Radius | C | Name the affected user segment and scale (all users / checkout-active users / <1% under split-brain). |

---

### Scenario Analysis Table

Produce the table below. Every cell must match the fill requirement in the Column Contract above.

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

### Gap Register

After the table, identify three findings:

**Offline Experience Gap**: Name the specific capability unavailable when `{{topic}}` has no
network. Name the missing affordance and the user impact.

**Data Consistency Violation**: Name the specific entity and field where concurrent writes produce
irreconcilable state. State the missing resolution policy and the business consequence (oversell,
double-charge, duplicate fulfillment).

**Missing Recovery Flow**: Name the failure entry point in `{{topic}}` that has no documented
exit. State what a complete recovery flow would require.

Each finding must be labeled, specific, and anchored to `{{topic}}`.

---

**Signal artifact**: Write output to `{{topic}}-flow-resilience-{{date}}.md`.

---

---

## V-02 — Anti-Omission Architecture: Explicit Four-Level Stack Naming

**Axis**: Anti-omission architecture (C-21 only)
**Hypothesis**: Explicitly naming all four anti-omission levels as a coordinated architecture
section — and assigning a distinct mechanism and omission risk to each level — makes the
system's intent legible: the model can reason about the architecture rather than treating each
constraint as an isolated instruction, closing the gap C-21 targets.

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
| **Table** | Unified Index | `#` column — all three scenario rows in one numbered table | A scenario silently dropped when fragmented output leaves an unlabeled gap |
| **Section** | Phase Gate | Explicit checkpoint instruction before the Gap Register section | Gap Register skipped when the model infers "complete" from the scenario table alone |
| **Column** | Ownership Assignment | Per-column expert-role label in every column header | A column omitted when a mid-row ownership transition is misread as a structural table boundary |
| **Slot** | Fill Contract | Stated fill requirement per column in the column specification | A cell left empty or placeholder when the requirement is only implied by context |

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
| Scenario | Both | Name the failure event and the specific commerce operation affected (checkout, inventory reservation, payment, fulfillment). |
| State | D | Describe the exact system state using distributed systems vocabulary. Name the partition state, service health, and any consistency guarantee in effect. |
| Capability | C | List every action the user can still take and every action that is blocked. Be specific to the commerce flow in progress. |
| Data at Risk | C | Name specific entities at risk: which fields, which records, which reservation windows. State the staleness or conflict window where measurable. |
| Recovery Path | D | Name the recovery pattern (saga rollback, idempotent retry, read-repair, LWW, vector clock). State the trigger, the steps, and the terminal healthy state. |
| Severity | D | One of: degraded / impaired / down. |
| Blast Radius | C | Name the affected user segment and scale. |

**Column ownership is not a table boundary.** Do not create separate tables for Commerce Expert
columns and Distributed Systems Expert columns. All eight columns appear in every row of a single
unified table. Do not insert a horizontal rule, heading, or section break between rows when
column ownership shifts.

**Produce all three rows before writing the Gap Register.** No cell may be empty or placeholder.

---

### Gap Register

After the table, identify three findings:

**Offline Experience Gap**: Name the specific capability unavailable when `{{topic}}` has no
network. Name the missing affordance and the user impact.

**Data Consistency Violation**: Name the specific entity and field where concurrent writes produce
irreconcilable state. State the missing resolution policy and the business consequence (oversell,
double-charge, duplicate fulfillment).

**Missing Recovery Flow**: Name the failure entry point in `{{topic}}` that has no documented
exit. State what a complete recovery flow would require.

Each finding must be labeled, specific, and anchored to `{{topic}}`.

---

**Signal artifact**: Write output to `{{topic}}-flow-resilience-{{date}}.md`.

---

---

## V-03 — Phrasing Register: Slot-Level Bold Imperatives

**Axis**: Phrasing register / slot-level imperatives (C-23 only)
**Hypothesis**: Embedding bold "Write this row now." imperatives inside each row's Content
descriptor — co-located at cell granularity rather than in table preamble or section gates —
closes the omission risk that section-level gates leave open: a model that has satisfied the
section gate could still skip a row; the in-row imperative makes skipping that specific row
unambiguous rather than implicit.

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
| Scenario | Both | Name the failure event and the specific commerce operation affected (checkout, inventory reservation, payment, fulfillment). |
| State | D | Describe the exact system state using distributed systems vocabulary. Name the partition state, service health, and any consistency guarantee in effect. |
| Capability | C | List every action the user can still take and every action that is blocked. Be specific to the commerce flow in progress. |
| Data at Risk | C | Name specific entities at risk: which fields, which records, which reservation windows. State the staleness or conflict window where measurable. |
| Recovery Path | D | Name the recovery pattern (saga rollback, idempotent retry, read-repair, LWW, vector clock). State the trigger, the steps, and the terminal healthy state. |
| Severity | D | One of: degraded / impaired / down. |
| Blast Radius | C | Name the affected user segment and scale. |

**Column ownership is not a table boundary.** Do not create separate tables for Commerce Expert
columns and Distributed Systems Expert columns. All eight columns appear in every row of a single
unified table. Do not insert a horizontal rule, heading, or section break between rows when
column ownership shifts.

**Produce all three rows before writing the Gap Register.** No cell may be empty or placeholder.

---

### Row Descriptors

Construct each row using the descriptor below. The bold imperative in each descriptor is
load-bearing — it is not decoration. Read it at the moment you construct that row.

---

**Row 1 — Full Client Offline**

**Write this row now.** Scenario *(Both)*: name a full client-offline event during a `{{topic}}`
commerce operation — use a specific operation: checkout submission, cart lock acquisition, payment
confirmation, or order placement. State *(D)*: name the exact partition state, name the
consistency guarantee in effect (strong / eventual / causal), and name any lock or reservation TTL
now running unobserved by the client. Capability *(C)*: list every action still possible offline;
list every action blocked; name what UI state the client should show but may not. Data at Risk
*(C)*: name the specific fields, records, or reservation windows at risk — state the staleness
window and whether loss is silent or surfaced. Recovery Path *(D)*: name the recovery pattern
(saga rollback, optimistic lock release, idempotent replay); state the trigger (reconnect event,
TTL expiry, reconciliation job); walk the numbered steps; state the terminal healthy state.
Severity *(D)*: degraded / impaired / down. Blast Radius *(C)*: name the affected user segment
and scale.

**Do not advance to Row 2 until all eight columns for Row 1 contain non-placeholder content.**

---

**Row 2 — Partial Service Failure**

**Write this row now.** Scenario *(Both)*: name a partial service failure where one named
downstream service is unavailable — inventory service, payment gateway, or fulfillment
orchestrator — while the `{{topic}}` client remains connected. State *(D)*: name the unavailable
service; describe the cascading states (inventory reservation timeout, payment pre-auth orphaned,
fulfillment stuck in pending); name the consistency level the system degrades to. Capability *(C)*:
name which commerce flows continue (browse, add-to-cart, saved order retrieval); name which are
blocked (new checkout, payment capture, fulfillment initiation); state whether degradation is
graceful (user informed) or silent (user submits into a black hole). Data at Risk *(C)*: name the
specific orphaned entity — reservation record, pre-authorization token, cart lock ID — and the TTL
before it causes harm. Recovery Path *(D)*: name the pattern; state whether recovery is automatic
(circuit breaker closes, saga compensates) or requires manual operator action; name the idempotency
key used to prevent double-processing on replay. Severity *(D)*: degraded / impaired / down.
Blast Radius *(C)*: name affected segment.

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

### Gap Register

**Section gate**: Before writing the Gap Register, confirm all three rows are present and all
eight columns are filled in every row. If any cell is missing, fill it before continuing.

After confirming, identify three findings:

**Offline Experience Gap**: Name the specific capability unavailable when `{{topic}}` has no
network. Name the missing affordance and the user impact.

**Data Consistency Violation**: Name the specific entity and field where concurrent writes produce
irreconcilable state. State the missing resolution policy and the business consequence (oversell,
double-charge, duplicate fulfillment).

**Missing Recovery Flow**: Name the failure entry point in `{{topic}}` that has no documented
exit. State what a complete recovery flow would require.

Each finding must be labeled, specific, and anchored to `{{topic}}`.

---

**Signal artifact**: Write output to `{{topic}}-flow-resilience-{{date}}.md`.

---

---

## V-04 — Combined: Discrete Pre-Output Meta-Table + Four-Level Architecture Naming

**Axes**: Output format + anti-omission architecture (C-24 + C-21)
**Hypothesis**: Combining an explicit standalone meta-table (pre-output contract) with a named
four-level anti-omission architecture achieves both structural pre-commitment (C-24) and
architecture legibility (C-21) simultaneously. The meta-table creates the contract obligation
before row construction; the architecture section makes the system of constraints readable as an
integrated design rather than a list of rules.

---

You are running the flow-resilience signal for topic: `{{topic}}`.

**Expert roles**: Commerce Domain Expert (C) | Distributed Systems Expert (D)

---

### Four-Level Anti-Omission Architecture

This prompt enforces output completeness through a **four-level anti-omission architecture**.
Each level addresses a distinct omission risk at a distinct structural level.

| Level | Name | Mechanism | Omission Risk Addressed |
|-------|------|-----------|------------------------|
| **Table** | Unified Index | `#` column — all three scenario rows in one numbered table | A scenario silently dropped when fragmented output leaves an unlabeled gap |
| **Section** | Phase Gate | Explicit checkpoint instruction before the Gap Register section | Gap Register skipped when the model infers "complete" from the scenario table alone |
| **Column** | Ownership Assignment | Per-column expert-role label defined in the Column Contract | A column omitted when a mid-row ownership transition is misread as a table boundary |
| **Slot** | Fill Contract | Stated fill requirement per column in the Column Contract | A cell left empty or placeholder when the requirement is only implied by context |

---

### Instructions

Simulate degraded conditions across three resilience classes for `{{topic}}`:

- **Class 1 — Full Client Offline**
- **Class 2 — Partial Service Failure**
- **Class 3 — Eventual Consistency / Split-Brain**

For each class, produce one scenario row in the Scenario Analysis Table below.

---

### Column Contract

Read this table in full before constructing any row. A row is complete only when every column
listed here has a non-placeholder entry.

| Column | Owner | Fill Requirement |
|--------|-------|-----------------|
| # | — | Row number (1, 2, 3). |
| Scenario | Both | Name the failure event and the specific commerce operation affected (checkout, inventory reservation, payment confirmation, order fulfillment). |
| State | D | Describe the exact system state using distributed systems vocabulary. Name the partition state, service health, and the consistency guarantee in effect. |
| Capability | C | List every action the user can still take and every action that is blocked. Be specific to the commerce flow in progress. |
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

### Gap Register

After the table, identify three findings:

**Offline Experience Gap**: Name the specific capability unavailable when `{{topic}}` has no
network. Name the missing affordance and the user impact.

**Data Consistency Violation**: Name the specific entity and field where concurrent writes produce
irreconcilable state. State the missing resolution policy and the business consequence (oversell,
double-charge, duplicate fulfillment).

**Missing Recovery Flow**: Name the failure entry point in `{{topic}}` that has no documented
exit. State what a complete recovery flow would require.

Each finding must be labeled, specific, and anchored to `{{topic}}`.

---

**Signal artifact**: Write output to `{{topic}}-flow-resilience-{{date}}.md`.

---

---

## V-05 — Ceiling Attempt: Four-Level Architecture + Slot Imperatives + Pre-Output Meta-Table

**Axes**: Anti-omission architecture + slot-level imperatives + output format (C-21 + C-23 + C-24)
**Hypothesis**: Stacking all three open criteria on top of V-02's existing passes (C-17, C-18,
C-20, C-22, C-25) achieves the R6 ceiling at 8/17 aspirational. The architecture section names
the four-level stack (C-21); the Column Contract is a standalone meta-table before the output
table (C-24); per-row descriptors embed "Write this row now." inside each Content descriptor
(C-23). No criterion is targeted twice; no level duplicates another's omission coverage.

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
commerce operation — use a specific operation: checkout submission, cart lock acquisition, payment
confirmation, or order placement. State *(D)*: name the exact partition state, name the
consistency guarantee in effect (strong / eventual / causal), and name any lock or reservation TTL
now running unobserved by the client. Capability *(C)*: list every action still possible offline;
list every action blocked; name what UI state the client should show but may not. Data at Risk
*(C)*: name the specific fields, records, or reservation windows at risk — state the staleness
window and whether loss is silent or surfaced. Recovery Path *(D)*: name the recovery pattern
(saga rollback, optimistic lock release, idempotent replay); state the trigger (reconnect event,
TTL expiry, reconciliation job); walk the numbered steps; state the terminal healthy state.
Severity *(D)*: degraded / impaired / down. Blast Radius *(C)*: name the affected user segment
and scale.

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

## Variation Summary

| Version | Axes | Open Criteria Targeted | Expected Aspirational | Expected Composite |
|---------|------|------------------------|----------------------|--------------------|
| V-01 | Output format | C-24 only | 6/17 = 3.53 | 93.53 |
| V-02 | Anti-omission architecture | C-21 only | 6/17 = 3.53 | 93.53 |
| V-03 | Slot-level imperatives | C-23 only | 6/17 = 3.53 | 93.53 |
| V-04 | Output format + architecture | C-24 + C-21 | 7/17 = 4.12 | 94.12 |
| V-05 | Architecture + imperatives + format | C-21 + C-23 + C-24 | 8/17 = 4.71 | **94.71** |

**Inherited passes in all variations** (from V-02 R5 baseline): C-17, C-18, C-20, C-22, C-25.

**C-24 implementation note**: V-01, V-04, V-05 satisfy C-24 by splitting the column specification
into two discrete structures: (1) a "Column Contract" section as a standalone meta-table, followed
by (2) a separate "Scenario Analysis Table" with the blank output template. V-02 R5 failed C-24
because its column spec table served as both the contract and the instruction block — no separate
output table template appeared after it.

**C-21 implementation note**: V-02, V-04, V-05 satisfy C-21 by including a "Four-Level
Anti-Omission Architecture" section that names all four levels (Table, Section, Column, Slot)
explicitly in a table with named mechanism and omission risk per level.

**C-23 implementation note**: V-03, V-05 satisfy C-23 by adding per-row Content descriptors
after the column spec/output table, each containing "**Write this row now.**" embedded inline
in the Content description text, followed by "**Do not advance to Row N until [condition].**"
co-located at that row's granularity.
