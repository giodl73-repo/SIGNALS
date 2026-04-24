Here are the five Round 4 variations for `flow-resilience`, written to `simulations/quest/variations/flow-resilience-variations-R4-2026-03-14.md`.

---

## Round 4 — Design Logic

**The core problem**: No R3 variation satisfies all four new v4 criteria simultaneously:
- V-01 passes C-17 (unified table) but has no C-18/C-19/C-20
- V-03 passes C-18 (phase gates) but its trace+chaos sub-tables fail C-17
- V-04 passes C-20 (ownership column) but the row-range preamble ("SME owns rows 1-4") creates an implicit structural boundary that breaks C-17
- V-05 passes C-17+C-18 but has no per-row slot imperatives (C-19) and no ownership column (C-20)

**Two new mechanisms introduced in R4:**

1. **Anti-boundary instruction** (targeting C-17/C-20 tension): Removes the range-based role preamble from V-04 R3 and replaces it with an explicit instruction: "The 'Owned by' column is a per-row metadata tag — not a section break, sub-table boundary, or role-sequence trigger." This is the hypothesis for why V-04 R3 fails C-17.

2. **In-row slot imperatives** (targeting C-19): Embeds bold imperative text directly in the Content field descriptor for rows 7 and 10/11: `**Write this row now. [specific requirement]. Do not advance to row N until [condition].**` The model reads the command exactly when filling that slot — genuinely co-located at row granularity, not above the table.

---

| Variation | Axis | New Criteria Targeted |
|-----------|------|-----------------------|
| V-01 | Output format — ownership column with anti-boundary instruction | C-17 + C-20 |
| V-02 | Lifecycle — phase gates verify structural integrity | C-17 + C-18 |
| V-03 | Phrasing register — in-row slot imperatives | C-17 + C-19 |
| V-04 | Combined: unified table + gates + ownership column | C-17 + C-18 + C-20 |
| V-05 | Full synthesis | C-17 + C-18 + C-19 + C-20 |

**Key discriminator for scoring**: C-19's pass condition requires imperatives at the first and last chaos row. V-03/V-04/V-05 put them directly in the Content descriptor at rows 7 and 10/11. V-02 doesn't attempt C-19. V-04 attempts three of four criteria — if it scores lower than V-05 only on C-19, that confirms the in-row imperative is the only remaining gap.
e Content field descriptor of rows 7 and 10 within the table itself — the model reads the imperative exactly when filling that row.

**Why V-05 R3 fails C-20**: V-05 R3 has no "Owned by" column. R4 adds it with the anti-boundary instruction.

**The combined bet in V-05 R4**: Anti-boundary instruction resolves the V-04 R3 C-17 failure. In-row imperatives ("[bold command] [fill-in instructions]" in the Content descriptor) satisfy C-19 without adding a column or blockquote. Phase gates from V-02 R4 carry over. These three mechanisms have never been tested together.

---

## V-01 — Axis: Output Format (Ownership Column in Unified Table)

**Axis**: Output format — unified sequential table with a dedicated "Owned by" column and an explicit anti-boundary instruction.

**Hypothesis**: C-17 and C-20 are simultaneously satisfiable. V-04 R3's C-17 failure was caused by the role preamble assigning row ranges ("SME owns rows 1-4"), not by the column itself. Removing the range preamble and replacing it with an anti-boundary instruction ("Owned by is a per-row tag — not a section marker, not a sub-table trigger") prevents the implicit structural break at row 5.

---

You are running a two-role resilience simulation for `{topic}`.

**Input**
- `{topic}` — the system or flow under analysis
- `{signal}` — read any existing signal artifacts for `{topic}` before starting

**Roles**
- **Commerce SME** — fills State, Capability, Data at risk, and Recovery rows. Grounds scenarios in commerce operations: cashier behavior, customer impact, manual workarounds.
- **Chaos Engineer** — fills Severity, Blast radius, and all chaos test rows. Applies CAP theorem trade-offs, retry semantics, idempotency analysis, and conflict resolution strategy assessment.

**Table structure rule**: Every scenario is one contract table with four columns: Row | Field | Content | Owned by. The "Owned by" column is a per-row metadata tag — it is not a section marker, not a sub-table boundary, and not a role-sequence trigger. Fill all rows in order (1 through 10, or 1 through 11 for Scenario 3) in a single top-to-bottom pass. Do not group rows by role. Do not insert a horizontal rule, blank row, or section header between rows where the Owned by value changes.

**Actor chain notation** (Commerce SME uses in all Recovery rows):
`client →` | `server →` | `operator →` | `user →`
Each step must begin with one of these four labels.

**Conflict resolution vocabulary** (Chaos Engineer selects in Scenario 3 row 5 only):
`last-write-wins` | `merge` | `manual-reconcile` | `reject-stale`
Select exactly one. Do not paraphrase.

---

### Scenario 1 — Full Connectivity Loss

The system loses network connectivity entirely during active commerce operations. Specify which operations continue locally, which fail immediately, and what is queued vs. discarded.

**Resilience contract** — fill all rows in sequence; do not split into sub-tables; do not move chaos rows to a separate section:

| Row | Field | Content | Owned by |
|-----|-------|---------|----------|
| 1 | State | [system state at point of failure: what is cached, what is lost, what is unknown — specific to `{topic}`'s local storage model] | SME |
| 2 | Capability | [what the cashier / customer / operator can still do, with named limitations — which screens still render, which transactions block] | SME |
| 3 | Data at risk | [named records at risk — receipts, offline basket, loyalty points, pending orders — not "transaction data"] | SME |
| 4 | Recovery | client → [action] / server → [action] / operator → [action] / user → [action] | SME |
| 5 | Severity | [degraded / impaired / down] | Chaos Eng |
| 6 | Blast radius | [scope and population affected — e.g., "all users on this store's network segment"] | Chaos Eng |
| 7 | Chaos injection | [exact failure injection: what to break, at which layer (OS / network / application), for how long — e.g., drop outbound TCP at OS firewall, block DNS mid-transaction] | Chaos Eng |
| 8 | Expected behavior | [correct system behavior during failure: queue depth, degraded-mode indicator surface, rejection semantics, fail-open vs. fail-closed decision] | Chaos Eng |
| 9 | Pass signal | [observable outcome confirming correct behavior — log event, UI state, metric value, queue depth reading] | Chaos Eng |
| 10 | Fail signal | [observable outcome indicating a gap — silent data loss, blocking error with no recovery path, incorrect state persisted] | Chaos Eng |

---

### Scenario 2 — Dependent Service Unavailable

One downstream service critical to `{topic}`'s commerce operations is returning 503s or timing out. Name the specific service (pricing, loyalty, inventory, payment gateway).

**Resilience contract**:

| Row | Field | Content | Owned by |
|-----|-------|---------|----------|
| 1 | State | | SME |
| 2 | Capability | | SME |
| 3 | Data at risk | | SME |
| 4 | Recovery | client → [action] / server → [action] / operator → [action] / user → [action] | SME |
| 5 | Severity | [degraded / impaired / down] | Chaos Eng |
| 6 | Blast radius | | Chaos Eng |
| 7 | Chaos injection | [how to inject: block service endpoint at proxy layer, return 503 after N requests, inject artificial latency above circuit-breaker timeout threshold] | Chaos Eng |
| 8 | Expected behavior | [circuit-break behavior, fallback data source, degraded-service indicator, specific rejection code and user-visible message] | Chaos Eng |
| 9 | Pass signal | | Chaos Eng |
| 10 | Fail signal | | Chaos Eng |

---

### Scenario 3 — Eventual Consistency Conflict

Two writes to the same record occurred in different partitions during the offline or failure window. Name the record type, the partition boundary, and the conflict-producing operation.

**Resilience contract**:

| Row | Field | Content | Owned by |
|-----|-------|---------|----------|
| 1 | State | | SME |
| 2 | Capability | | SME |
| 3 | Data at risk | | SME |
| 4 | Recovery | client → [action] / server → [action] / operator → [action] / user → [action] | SME |
| 5 | Conflict resolution | Strategy (select one): `last-write-wins \| merge \| manual-reconcile \| reject-stale` → Selected: ___ → Adequacy: [adequate / inadequate — if inadequate, name the failure mode this strategy produces for this record type] | Chaos Eng |
| 6 | Severity | [degraded / impaired / down] | Chaos Eng |
| 7 | Blast radius | | Chaos Eng |
| 8 | Chaos injection | [how to produce the conflict: take two nodes offline independently, write conflicting state to each, reconnect simultaneously — specify the conflicting write sequence and reconnect timing] | Chaos Eng |
| 9 | Expected behavior | [how conflict detection proceeds — which component detects, how operator is notified, what the resolution UI offers, resolution latency] | Chaos Eng |
| 10 | Pass signal | [record in correct final state, audit log entry present, operator notification sent within SLA] | Chaos Eng |
| 11 | Fail signal | [silent merge error, wrong writer wins, record left in split state, operator not notified, audit log missing] | Chaos Eng |

---

### Section 4 — Gap Identification

(mandatory — do not omit or merge with scenarios)

Each finding carries an observability hook on the line immediately after the finding entry. Do not collect hooks into a separate observability section.

**Offline Experience Gaps**

For each gap: name the operation, describe the forced workaround, state downstream risk.

- GAP-01: [name] — [description] — [downstream risk]
  `metric=[name]` | `alert=[condition that fires]` | `owner=[team or role]`
- GAP-02: ...

(minimum one; add as many as found)

**Data Consistency Violations**

For each violation: name the record, describe the inconsistency, state detectability (before / only after customer impact).

- DCV-01: [record] — [inconsistency] — [detectability]
  `metric=[name]` | `alert=[condition that fires]` | `owner=[team or role]`
- DCV-02: ...

(minimum one)

**Missing Recovery Flows**

For each: name the missing automated flow, describe the current manual workaround, estimate frequency x impact.

- MRF-01: [name] — [manual workaround] — [risk if stays manual]
  `metric=[name]` | `alert=[condition that fires]` | `owner=[team or role]`
- MRF-02: ...

(minimum one)

---

### Completeness Check

Include this block in the artifact. Fill all boxes and the count before writing the file.

- [ ] GAP subsection present with >=1 finding carrying inline metric/alert/owner
- [ ] DCV subsection present with >=1 finding carrying inline metric/alert/owner
- [ ] MRF subsection present with >=1 finding carrying inline metric/alert/owner

Finding types present: ___ of 3

Do not write the artifact until all three boxes are checked and the count reads "3 of 3".

---

### Output

Write the artifact to:
`simulations/flow/resilience/{topic}-resilience-{date}.md`

Include the Completeness Check block in the artifact with all three boxes checked and "Finding types present: 3 of 3" confirmed. Return the file path when done.

---

## V-02 — Axis: Lifecycle Emphasis (Phase Gates on Unified Table)

**Axis**: Lifecycle emphasis — V-01 R3's unified sequential table per scenario + PHASE 1 GATE / PHASE 2 GATE as named stop conditions. The Phase 1 Gate explicitly verifies row-index continuity and the absence of sub-table headers, converting C-17 from a format instruction into a verifiable gate condition.

**Hypothesis**: Phase gates become stronger C-17 enforcement when they explicitly check structural properties (row numbering is unbroken, no sub-table header appears between trace rows and chaos rows) rather than only content completeness. The gate condition names specific structural failures by their observable symptoms ("no horizontal rule appears between rows 1-6 and rows 7-10"), making it harder for a model to satisfy the gate without producing the correct structure. C-19 and C-20 are excluded to isolate the lifecycle axis.

---

You are a **Commerce / Distributed Systems domain expert** running a resilience simulation for `{topic}`.

**Input**
- `{topic}` — the system or flow under analysis
- `{signal}` — read any existing signal artifacts for `{topic}` before starting

This simulation runs in three phases. Satisfy each phase gate before advancing. Do not skip phases.

**Actor chain notation**: `client →` | `server →` | `operator →` | `user →`
Every Recovery row must prefix each step with one of these four labels. No prose recovery.

**Conflict vocabulary**: `last-write-wins` | `merge` | `manual-reconcile` | `reject-stale`
Select exactly one in Scenario 3 row 5. Do not paraphrase.

---

## PHASE 1 — Scenario Contracts

Write each scenario as a single contract table with columns Row | Field | Content. Fill every row. The chaos rows are rows in the same table — not a sub-table, not a separate section. Fill rows in sequence from 1 to 10 (or 1 to 11 for Scenario 3) without inserting headers, horizontal rules, or blank separator lines between rows.

### Scenario 1 — Full Connectivity Loss

The system loses network connectivity entirely during active commerce operations.

**Resilience contract**:

| Row | Field | Content |
|-----|-------|---------|
| 1 | State | [system state at point of failure: what is cached, lost, unknown] |
| 2 | Capability | [what the cashier / customer / operator can still do, with named limitations] |
| 3 | Data at risk | [named records at risk — receipts, offline basket, loyalty points — not "transaction data"] |
| 4 | Recovery | client → [action] / server → [action] / operator → [action] / user → [action] |
| 5 | Severity | [degraded / impaired / down] |
| 6 | Blast radius | [scope and population affected] |
| 7 | Chaos injection | [exact failure injection: layer (OS / network / application), failure type, duration] |
| 8 | Expected behavior | [correct system behavior: queue, reject, degrade, fail-open vs. fail-closed] |
| 9 | Pass signal | [observable outcome confirming correct behavior] |
| 10 | Fail signal | [observable outcome indicating a gap] |

---

### Scenario 2 — Dependent Service Unavailable

Name the specific service (pricing, loyalty, inventory, payment gateway) most critical to `{topic}`'s commerce operations.

**Resilience contract**:

| Row | Field | Content |
|-----|-------|---------|
| 1 | State | |
| 2 | Capability | |
| 3 | Data at risk | |
| 4 | Recovery | client → [action] / server → [action] / operator → [action] / user → [action] |
| 5 | Severity | [degraded / impaired / down] |
| 6 | Blast radius | |
| 7 | Chaos injection | [block endpoint, return 503 after N requests, inject latency above circuit-breaker threshold] |
| 8 | Expected behavior | [circuit-break behavior, fallback mode, degraded-service indicator] |
| 9 | Pass signal | |
| 10 | Fail signal | |

---

### Scenario 3 — Eventual Consistency Conflict

Name the record type, partition boundary, and conflict-producing operation.

**Resilience contract**:

| Row | Field | Content |
|-----|-------|---------|
| 1 | State | |
| 2 | Capability | |
| 3 | Data at risk | |
| 4 | Recovery | client → [action] / server → [action] / operator → [action] / user → [action] |
| 5 | Conflict resolution | Strategy (select one): `last-write-wins \| merge \| manual-reconcile \| reject-stale` → Selected: ___ → Adequacy: [adequate / inadequate — name the failure mode if inadequate] |
| 6 | Severity | [degraded / impaired / down] |
| 7 | Blast radius | |
| 8 | Chaos injection | [dual-partition write sequence — how to produce the conflict reproducibly] |
| 9 | Expected behavior | [conflict detection, operator notification, resolution UI] |
| 10 | Pass signal | [correct final state, audit log, operator notified within SLA] |
| 11 | Fail signal | [silent merge, wrong winner, split state, no notification] |

---

### PHASE 1 GATE — Stop

Verify each condition before advancing to Phase 2:

1. All three scenario tables are complete — no Content cell is empty
2. Row numbers are sequential and unbroken: Scenarios 1–2 rows 1–10, Scenario 3 rows 1–11
3. No sub-table header, no horizontal rule, and no blank separator line appears between rows 1–6 and rows 7–10 in any scenario table
4. Every Recovery row (row 4) begins each step with `client →`, `server →`, `operator →`, or `user →` — no prose recovery
5. Scenario 3 row 5 contains a selected conflict resolution term from the controlled vocabulary — not a paraphrase

**Do not begin Phase 2 until all five conditions are verified.**

---

## PHASE 2 — Gap Registry

Identify every gap surfaced by Phase 1. Write all three subsections. Every finding carries an inline observability hook on the line immediately following it — not in a separate observability section, not at the end of the registry.

**Offline Experience Gaps**

For each gap: name the operation, describe the forced workaround, state downstream risk.

- GAP-01: [name] — [description] — [downstream risk]
  `metric=[name]` | `alert=[condition that fires]` | `owner=[team or role]`
- GAP-02: ...

(minimum one)

**Data Consistency Violations**

For each violation: name the record, describe the inconsistency, state detectability.

- DCV-01: [record] — [inconsistency] — [detectable before / only after customer impact]
  `metric=[name]` | `alert=[condition that fires]` | `owner=[team or role]`
- DCV-02: ...

(minimum one)

**Missing Recovery Flows**

For each: name the missing automated flow, describe the manual workaround, estimate risk.

- MRF-01: [name] — [manual workaround] — [risk if stays manual]
  `metric=[name]` | `alert=[condition that fires]` | `owner=[team or role]`
- MRF-02: ...

(minimum one)

---

### PHASE 2 GATE — Stop

Verify each condition before advancing to Phase 3:

1. GAP, DCV, and MRF subsections are all present
2. Every finding entry is followed immediately by a hook line containing `metric=`, `alert=`, and `owner=`
3. No finding is missing any of the three hook fields
4. No hooks are consolidated into a standalone observability section

**Do not begin Phase 3 until all four conditions are verified.**

---

## PHASE 3 — Completeness Certification

Fill this checklist now. Include it in the artifact. Do not write the artifact file until all three boxes are checked and the count reads "3 of 3".

- [ ] GAP subsection present with >=1 finding carrying inline metric/alert/owner
- [ ] DCV subsection present with >=1 finding carrying inline metric/alert/owner
- [ ] MRF subsection present with >=1 finding carrying inline metric/alert/owner

Finding types present: ___ of 3

---

### Output

Write the artifact to:
`simulations/flow/resilience/{topic}-resilience-{date}.md`

The artifact must include all three Phase 1 scenario contracts (unified tables, chaos rows inside, no sub-table breaks), all Phase 2 gap findings (inline hooks), and the Phase 3 completeness checklist with all three boxes checked and "Finding types present: 3 of 3" confirmed.

Return the file path when done.

---

## V-03 — Axis: Phrasing Register (Slot-Level Imperatives Inside Table Rows)

**Axis**: Phrasing register — slot-level imperative commands embedded in the Content field descriptor for the first and last chaos rows per scenario. The imperative is co-located at the row where omission risk is highest, inside the unified table structure, without adding columns or placing blockquotes above the table.

**Hypothesis**: V-05 R3's scenario-level blockquotes ("> Write the table now. Fill all 10 rows.") apply to the entire table, not to individual rows — they fail C-19 because they are table-level, not slot-level. R4 embeds bold imperative text in the Content descriptor for rows 7 and 10/11: "**Write this row now. [specific field requirement]. Do not advance to row N until [condition].**" The model reads this imperative exactly when filling that slot. This is co-located at slot granularity (the row itself is the slot) without adding a column or breaking C-17's unified table structure.

---

You are a **Commerce / Distributed Systems domain expert** running a resilience simulation for `{topic}`.

**Input**
- `{topic}` — the system or flow under analysis
- `{signal}` — read any existing signal artifacts for `{topic}` before starting

Each failure scenario is a single resilience contract table. Fill every row. The four-field trace, severity, blast radius, and chaos test rows are all rows in the same table — do not split into sub-tables, do not move chaos rows to a separate section.

**Actor chain notation** (use in all Recovery rows):
`client →` | `server →` | `operator →` | `user →`
Each step must begin with one of these four labels.

**Conflict resolution vocabulary** (use in Scenario 3 row 5 only):
`last-write-wins` | `merge` | `manual-reconcile` | `reject-stale`
Select exactly one. Do not paraphrase.

---

### Scenario 1 — Full Connectivity Loss

The system loses network connectivity entirely during active commerce operations.

**Resilience contract**:

| Row | Field | Content |
|-----|-------|---------|
| 1 | State | [system state at point of failure: what is cached, what is lost, what is unknown] |
| 2 | Capability | [what the cashier / customer / operator can still do, with named limitations] |
| 3 | Data at risk | [named records at risk — receipts, offline basket, loyalty points — not "transaction data"] |
| 4 | Recovery | client → [action] / server → [action] / operator → [action] / user → [action] |
| 5 | Severity | [degraded / impaired / down] |
| 6 | Blast radius | [scope and population affected] |
| 7 | Chaos injection | **Write this row now. Name the injection layer (OS / network / application), the failure type, and the duration. Do not advance to row 8 until this field contains all three.** [e.g., block outbound TCP at OS firewall for 30s mid-transaction] |
| 8 | Expected behavior | [correct system behavior: queue depth, degraded-mode surface, rejection semantics, fail-open vs. fail-closed] |
| 9 | Pass signal | [observable outcome confirming correct behavior — log event, UI state, metric value] |
| 10 | Fail signal | **Write this row now. Name a specific observable failure indicator. Do not advance to Scenario 2 until row 10 contains a named, non-generic outcome.** [e.g., silent data loss, blocking error with no recovery path, incorrect state persisted] |

---

### Scenario 2 — Dependent Service Unavailable

Name the specific service (pricing, loyalty, inventory, payment gateway) most critical to `{topic}`'s operations.

**Resilience contract**:

| Row | Field | Content |
|-----|-------|---------|
| 1 | State | |
| 2 | Capability | |
| 3 | Data at risk | |
| 4 | Recovery | client → [action] / server → [action] / operator → [action] / user → [action] |
| 5 | Severity | [degraded / impaired / down] |
| 6 | Blast radius | |
| 7 | Chaos injection | **Write this row now. Specify the injection point (proxy / load balancer / service mesh) and the trigger condition. Do not advance to row 8 until both are named.** [block endpoint, return 503 after N requests, inject latency above circuit-breaker timeout threshold] |
| 8 | Expected behavior | [circuit-break behavior, fallback data source, degraded-service indicator, specific rejection code and user-visible message] |
| 9 | Pass signal | |
| 10 | Fail signal | **Write this row now. Name the observable failure indicator for this service's degradation. Do not advance to Scenario 3 until row 10 is filled with a specific outcome.** [e.g., transaction blocked without fallback, circuit breaker not tripping within SLA, no operator visibility] |

---

### Scenario 3 — Eventual Consistency Conflict

Name the record type, partition boundary, and conflict-producing operation.

**Resilience contract**:

| Row | Field | Content |
|-----|-------|---------|
| 1 | State | |
| 2 | Capability | |
| 3 | Data at risk | |
| 4 | Recovery | client → [action] / server → [action] / operator → [action] / user → [action] |
| 5 | Conflict resolution | Strategy (select one): `last-write-wins \| merge \| manual-reconcile \| reject-stale` → Selected: ___ → Adequacy: [adequate / inadequate — if inadequate, name the exact failure mode this strategy produces] |
| 6 | Severity | [degraded / impaired / down] |
| 7 | Blast radius | |
| 8 | Chaos injection | **Write this row now. Specify the conflicting write operations and the reconnect timing window. Do not advance to row 9 until both are named.** [dual-partition write sequence: take two nodes offline independently, write conflicting state, reconnect simultaneously] |
| 9 | Expected behavior | [how conflict is detected, what notification fires, what the resolution UI offers, resolution latency] |
| 10 | Pass signal | [record in correct final state, audit log entry present, operator notification sent within SLA] |
| 11 | Fail signal | **Write this row now. This is the last row of the last scenario. Fill it completely before advancing to Section 4.** [silent merge error, wrong writer wins, record left in split state, operator not notified, audit log missing] |

---

### Section 4 — Gap Identification

(mandatory — do not omit or merge with scenarios)

Each finding carries an observability hook on the line immediately after the finding entry. Do not collect hooks into a separate observability section.

**Offline Experience Gaps**

- GAP-01: [name] — [description] — [downstream risk]
  `metric=[name]` | `alert=[condition that fires]` | `owner=[team or role]`
- GAP-02: ...

(minimum one)

**Data Consistency Violations**

- DCV-01: [record] — [inconsistency] — [detectable before / only after customer impact]
  `metric=[name]` | `alert=[condition that fires]` | `owner=[team or role]`
- DCV-02: ...

(minimum one)

**Missing Recovery Flows**

- MRF-01: [name] — [manual workaround] — [risk if stays manual]
  `metric=[name]` | `alert=[condition that fires]` | `owner=[team or role]`
- MRF-02: ...

(minimum one)

---

### Completeness Check

Include this block in the artifact. Fill all boxes and the count before writing the file.

- [ ] GAP subsection present with >=1 finding carrying inline metric/alert/owner
- [ ] DCV subsection present with >=1 finding carrying inline metric/alert/owner
- [ ] MRF subsection present with >=1 finding carrying inline metric/alert/owner

Finding types present: ___ of 3

Do not write the artifact until all three boxes are checked and the count reads "3 of 3".

---

### Output

Write the artifact to:
`simulations/flow/resilience/{topic}-resilience-{date}.md`

Include the Completeness Check block with all three boxes checked and "Finding types present: 3 of 3" confirmed. Return the file path when done.

---

## V-04 — Combined: Unified Table + Phase Gates + Ownership Column (C-17 + C-18 + C-20)

**Axes combined**: Output format (C-17 unified table + C-20 ownership column, per V-01 R4's anti-boundary instruction) + Lifecycle emphasis (C-18 phase gates, per V-02 R4's gate architecture). C-19 excluded to isolate whether three of the four new criteria are structurally compatible.

**Hypothesis**: The Phase 1 Gate can verify ownership column completeness (every row has a non-blank Owned by value) alongside structural integrity (no sub-table breaks), making the gate a joint verifier of C-17 and C-20 simultaneously. The Phase 2 Gate carries forward the gap-registry verification from V-02 R4. This is the tightest three-criteria structure before adding slot-level imperative complexity.

---

You are running a two-role resilience simulation for `{topic}`.

**Input**
- `{topic}` — the system or flow under analysis
- `{signal}` — read any existing signal artifacts for `{topic}` before starting

**Roles**
- **Commerce SME** — fills State, Capability, Data at risk, and Recovery rows. Grounds scenarios in commerce operations.
- **Chaos Engineer** — fills Severity, Blast radius, and all chaos test rows. Applies CAP theorem analysis, retry semantics, idempotency requirements, and conflict resolution assessment.

**Table structure rule**: Every scenario is one contract table with four columns: Row | Field | Content | Owned by. The "Owned by" column is a per-row metadata tag — not a section break, sub-table boundary, or role-sequence trigger. Fill all rows in order (1 through 10, or 1 through 11 for Scenario 3) in a single top-to-bottom pass. Do not group rows by role or insert any structural separator between rows where the Owned by value changes.

This simulation runs in three phases. Satisfy each phase gate before advancing.

**Actor chain notation**: `client →` | `server →` | `operator →` | `user →`
Every Recovery row must prefix each step with one of these four labels.

**Conflict vocabulary**: `last-write-wins` | `merge` | `manual-reconcile` | `reject-stale`
Select exactly one in Scenario 3 row 5. Do not paraphrase.

---

## PHASE 1 — Scenario Contracts

### Scenario 1 — Full Connectivity Loss

The system loses network connectivity entirely during active commerce operations.

**Resilience contract**:

| Row | Field | Content | Owned by |
|-----|-------|---------|----------|
| 1 | State | [system state at point of failure: what is cached, lost, unknown] | SME |
| 2 | Capability | [what the cashier / customer / operator can still do, with named limitations] | SME |
| 3 | Data at risk | [named records at risk — receipts, offline basket, loyalty points] | SME |
| 4 | Recovery | client → [action] / server → [action] / operator → [action] / user → [action] | SME |
| 5 | Severity | [degraded / impaired / down] | Chaos Eng |
| 6 | Blast radius | [scope and population affected] | Chaos Eng |
| 7 | Chaos injection | [exact failure injection: layer, failure type, duration] | Chaos Eng |
| 8 | Expected behavior | [correct system behavior: queue, reject, degrade, fail-open vs. fail-closed] | Chaos Eng |
| 9 | Pass signal | [observable outcome confirming correct behavior] | Chaos Eng |
| 10 | Fail signal | [observable outcome indicating a gap] | Chaos Eng |

---

### Scenario 2 — Dependent Service Unavailable

Name the specific service (pricing, loyalty, inventory, payment gateway) most critical to `{topic}`'s operations.

**Resilience contract**:

| Row | Field | Content | Owned by |
|-----|-------|---------|----------|
| 1 | State | | SME |
| 2 | Capability | | SME |
| 3 | Data at risk | | SME |
| 4 | Recovery | client → [action] / server → [action] / operator → [action] / user → [action] | SME |
| 5 | Severity | [degraded / impaired / down] | Chaos Eng |
| 6 | Blast radius | | Chaos Eng |
| 7 | Chaos injection | [block endpoint, return 503 after N requests, inject latency above circuit-breaker threshold] | Chaos Eng |
| 8 | Expected behavior | [circuit-break behavior, fallback mode, degraded-service indicator] | Chaos Eng |
| 9 | Pass signal | | Chaos Eng |
| 10 | Fail signal | | Chaos Eng |

---

### Scenario 3 — Eventual Consistency Conflict

Name the record type, partition boundary, and conflict-producing operation.

**Resilience contract**:

| Row | Field | Content | Owned by |
|-----|-------|---------|----------|
| 1 | State | | SME |
| 2 | Capability | | SME |
| 3 | Data at risk | | SME |
| 4 | Recovery | client → [action] / server → [action] / operator → [action] / user → [action] | SME |
| 5 | Conflict resolution | Strategy (select one): `last-write-wins \| merge \| manual-reconcile \| reject-stale` → Selected: ___ → Adequacy: [adequate / inadequate — name the failure mode if inadequate] | Chaos Eng |
| 6 | Severity | [degraded / impaired / down] | Chaos Eng |
| 7 | Blast radius | | Chaos Eng |
| 8 | Chaos injection | [dual-partition write sequence — conflicting writes, reconnect timing] | Chaos Eng |
| 9 | Expected behavior | [conflict detection, operator notification, resolution UI] | Chaos Eng |
| 10 | Pass signal | [correct final state, audit log, operator notified within SLA] | Chaos Eng |
| 11 | Fail signal | [silent merge, wrong winner, split state, no notification] | Chaos Eng |

---

### PHASE 1 GATE — Stop

Verify each condition before advancing to Phase 2:

1. All three scenario tables are complete — no Content cell is empty
2. Every table has a sequential, unbroken Row index: Scenarios 1–2 rows 1–10, Scenario 3 rows 1–11
3. No sub-table header, horizontal rule, or blank separator line appears between any two consecutive rows in any scenario table
4. Every row has a non-blank "Owned by" value (SME or Chaos Eng)
5. Every Recovery row uses actor-chain notation for each step — no prose recovery
6. Scenario 3 row 5 contains one selected controlled-vocabulary conflict resolution term — not a paraphrase

**Do not begin Phase 2 until all six conditions are verified.**

---

## PHASE 2 — Gap Registry

Identify every gap surfaced by Phase 1. Write all three subsections. Every finding carries an inline observability hook on the line immediately following it — not consolidated into a separate observability section.

**Offline Experience Gaps**

- GAP-01: [name] — [description] — [downstream risk]
  `metric=[name]` | `alert=[condition that fires]` | `owner=[team or role]`
- GAP-02: ...

(minimum one)

**Data Consistency Violations**

- DCV-01: [record] — [inconsistency] — [detectable before / only after customer impact]
  `metric=[name]` | `alert=[condition that fires]` | `owner=[team or role]`
- DCV-02: ...

(minimum one)

**Missing Recovery Flows**

- MRF-01: [name] — [manual workaround] — [risk if stays manual]
  `metric=[name]` | `alert=[condition that fires]` | `owner=[team or role]`
- MRF-02: ...

(minimum one)

---

### PHASE 2 GATE — Stop

Verify each condition before advancing to Phase 3:

1. GAP, DCV, and MRF subsections are all present
2. Every finding entry is followed immediately by a hook line containing `metric=`, `alert=`, and `owner=`
3. No hooks are consolidated into a standalone section
4. Each gap is distinct — no two findings describe the same problem

**Do not begin Phase 3 until all four conditions are verified.**

---

## PHASE 3 — Completeness Certification

Fill this checklist now. Include it in the artifact. Do not write the artifact file until all three boxes are checked and the count reads "3 of 3".

- [ ] GAP subsection present with >=1 finding carrying inline metric/alert/owner
- [ ] DCV subsection present with >=1 finding carrying inline metric/alert/owner
- [ ] MRF subsection present with >=1 finding carrying inline metric/alert/owner

Finding types present: ___ of 3

---

### Output

Write the artifact to:
`simulations/flow/resilience/{topic}-resilience-{date}.md`

The artifact must include all three Phase 1 scenario contracts (four-column tables, all rows filled, sequential row index, no sub-table breaks), all Phase 2 gap findings (inline hooks), and the Phase 3 completeness checklist with all three boxes checked and "Finding types present: 3 of 3" confirmed. Return the file path when done.

---

## V-05 — Full Synthesis: All Four Axes (C-17 + C-18 + C-19 + C-20)

**Axes combined**: Output format (C-17 unified table), Role sequence (C-20 ownership column with anti-boundary instruction), Lifecycle emphasis (C-18 phase gates), Phrasing register (C-19 slot-level imperatives embedded in Content descriptors for first and last chaos rows per scenario).

**Hypothesis**: All four new criteria are simultaneously satisfiable. The anti-boundary instruction prevents the ownership column from breaking C-17. In-row imperative text ("**Write this row now. [specific field requirement]. Do not advance until [condition].**" in the Content descriptor for rows 7 and 10/11) satisfies C-19 without adding a column or external blockquote. Phase gates from V-04 carry over for C-18. The critical open question is whether in-row imperative text in the Content descriptor counts as "slot-level co-location" for C-19 — this is the discriminating test between V-05 R4 and all prior variations.

---

You are running a two-role resilience simulation for `{topic}`.

**Input**
- `{topic}` — the system or flow under analysis
- `{signal}` — read any existing signal artifacts for `{topic}` before starting

**Roles**
- **Commerce SME** — fills State, Capability, Data at risk, and Recovery rows. Grounds scenarios in commerce operations: cashier behavior, customer impact, manual workarounds.
- **Chaos Engineer** — fills Severity, Blast radius, and all chaos test rows. Applies CAP theorem trade-offs, retry semantics, idempotency requirements, and conflict resolution strategy assessment. Does not describe floor experience.

**Table structure rule**: Every scenario is one contract table with four columns: Row | Field | Content | Owned by. The "Owned by" column is a per-row metadata tag — not a section break, sub-table boundary, or role-sequence trigger. Fill all rows in order (1 through 10, or 1 through 11 for Scenario 3) in a single top-to-bottom pass. Do not group rows by role or insert any structural separator between rows where the Owned by value changes.

This simulation runs in three phases. Satisfy each phase gate before advancing.

**Fill every row in every table.** If a row's Content cell is empty in your output, stop and fill it before continuing. Empty rows are failures, not placeholders.

**Actor chain notation**: `client →` | `server →` | `operator →` | `user →`
Every Recovery row must prefix each step with one of these four labels. No prose recovery.

**Conflict vocabulary**: `last-write-wins` | `merge` | `manual-reconcile` | `reject-stale`
Select exactly one in Scenario 3 row 5. Do not paraphrase.

---

## PHASE 1 — Scenario Contracts

### Scenario 1 — Full Connectivity Loss

The system loses network connectivity entirely during active commerce operations. Specify which operations continue locally, which fail immediately, and what is queued vs. discarded.

**Resilience contract** — fill all rows in sequence 1 through 10; do not advance to Scenario 2 until all 10 rows are filled:

| Row | Field | Content | Owned by |
|-----|-------|---------|----------|
| 1 | State | [system state at point of failure: what is cached, what is lost, what is unknown] | SME |
| 2 | Capability | [what the cashier / customer / operator can still do, with named limitations — which screens render, which transactions block] | SME |
| 3 | Data at risk | [named records at risk — receipts, offline basket, loyalty points, pending orders — not "transaction data"] | SME |
| 4 | Recovery | client → [action] / server → [action] / operator → [action] / user → [action] | SME |
| 5 | Severity | [degraded / impaired / down] | Chaos Eng |
| 6 | Blast radius | [scope and population affected] | Chaos Eng |
| 7 | Chaos injection | **Write this row now. Name the injection layer (OS / network / application), the failure type, and the duration. Do not advance to row 8 until all three are present in this field.** [e.g., block outbound TCP at OS firewall for 30s mid-transaction] | Chaos Eng |
| 8 | Expected behavior | [correct system behavior: queue depth, degraded-mode surface, rejection semantics, fail-open vs. fail-closed] | Chaos Eng |
| 9 | Pass signal | [observable outcome confirming correct behavior — log event, UI state, metric value, queue depth] | Chaos Eng |
| 10 | Fail signal | **Write this row now. Name a specific observable failure indicator. Do not advance to Scenario 2 until row 10 contains a named, non-generic outcome.** [silent data loss, blocking error with no recovery path, incorrect state persisted] | Chaos Eng |

---

### Scenario 2 — Dependent Service Unavailable

One downstream service critical to `{topic}`'s commerce operations is returning 503s or timing out. Name the specific service (pricing, loyalty, inventory, payment gateway).

**Resilience contract** — fill all rows in sequence 1 through 10; do not advance to Scenario 3 until all 10 rows are filled:

| Row | Field | Content | Owned by |
|-----|-------|---------|----------|
| 1 | State | | SME |
| 2 | Capability | | SME |
| 3 | Data at risk | | SME |
| 4 | Recovery | client → [action] / server → [action] / operator → [action] / user → [action] | SME |
| 5 | Severity | [degraded / impaired / down] | Chaos Eng |
| 6 | Blast radius | | Chaos Eng |
| 7 | Chaos injection | **Write this row now. Specify the injection point (proxy / load balancer / service mesh) and the trigger condition. Do not advance to row 8 until both are named.** [block endpoint, return 503 after N requests, inject latency above circuit-breaker timeout threshold] | Chaos Eng |
| 8 | Expected behavior | [circuit-break behavior, fallback data source, degraded-service indicator, specific rejection code and user-visible message] | Chaos Eng |
| 9 | Pass signal | | Chaos Eng |
| 10 | Fail signal | **Write this row now. Name the observable failure indicator for this service's degradation. Do not advance to Scenario 3 until row 10 is filled.** [transaction blocked without fallback, circuit breaker not tripping within SLA, no operator visibility] | Chaos Eng |

---

### Scenario 3 — Eventual Consistency Conflict

Two writes to the same record occurred in different partitions during the failure window. Name the record type, the partition boundary, and the conflict-producing operation.

**Resilience contract** — fill all rows in sequence 1 through 11; do not advance to Phase 1 Gate until all 11 rows are filled:

| Row | Field | Content | Owned by |
|-----|-------|---------|----------|
| 1 | State | | SME |
| 2 | Capability | | SME |
| 3 | Data at risk | | SME |
| 4 | Recovery | client → [action] / server → [action] / operator → [action] / user → [action] | SME |
| 5 | Conflict resolution | Strategy (select one): `last-write-wins \| merge \| manual-reconcile \| reject-stale` → Selected: ___ → Adequacy: [adequate / inadequate — if inadequate, name the exact failure mode this strategy produces for this record type] | Chaos Eng |
| 6 | Severity | [degraded / impaired / down] | Chaos Eng |
| 7 | Blast radius | | Chaos Eng |
| 8 | Chaos injection | **Write this row now. Specify the conflicting write operations and the reconnect timing window. Do not advance to row 9 until both are named.** [dual-partition write sequence: take two nodes offline independently, write conflicting state, reconnect simultaneously] | Chaos Eng |
| 9 | Expected behavior | [how conflict is detected, what notification fires, what the resolution UI offers, resolution latency] | Chaos Eng |
| 10 | Pass signal | [record in correct final state, audit log entry present, operator notification sent within SLA] | Chaos Eng |
| 11 | Fail signal | **Write this row now. This is the last row of the last scenario. Fill it completely before advancing to Phase 1 Gate.** [silent merge error, wrong writer wins, record left in split state, operator not notified, audit log missing] | Chaos Eng |

---

### PHASE 1 GATE — Stop

Verify each condition before advancing to Phase 2:

1. All three scenario tables are complete — no Content cell is empty or contains only placeholder text
2. Every table has a sequential, unbroken Row index: Scenarios 1–2 rows 1–10, Scenario 3 rows 1–11
3. No sub-table header, horizontal rule, or blank separator line appears between any two consecutive rows in any scenario table
4. Every row has a non-blank "Owned by" value (SME or Chaos Eng)
5. Every Recovery row (row 4) uses actor-chain notation for each step — no prose recovery
6. Scenario 3 row 5 contains one selected controlled-vocabulary conflict resolution term — not a paraphrase

**Do not begin Phase 2 until all six conditions are verified.**

---

## PHASE 2 — Gap Registry

Identify every gap surfaced by Phase 1. Write all three subsections now. After each finding entry, write the observability hook on the very next line. Do not collect hooks into a separate observability section at the end.

**Offline Experience Gaps**

> Write GAP-01 now. Write the observability hook on the next line. Then write GAP-02 if applicable.

- GAP-01: [name] — [description] — [downstream risk]
  `metric=[name]` | `alert=[condition that fires]` | `owner=[team or role]`

(minimum one; add as many as found)

**Data Consistency Violations**

> Write DCV-01 now. Write the observability hook on the next line. Then write DCV-02 if applicable.

- DCV-01: [record] — [inconsistency] — [detectable before / only after customer impact]
  `metric=[name]` | `alert=[condition that fires]` | `owner=[team or role]`

(minimum one)

**Missing Recovery Flows**

> Write MRF-01 now. Write the observability hook on the next line. This is the last finding type.

- MRF-01: [name] — [manual workaround] — [risk if stays manual]
  `metric=[name]` | `alert=[condition that fires]` | `owner=[team or role]`

(minimum one)

---

### PHASE 2 GATE — Stop

Verify each condition before advancing to Phase 3:

1. GAP, DCV, and MRF subsections are all present
2. Every finding entry is followed immediately by a hook line containing `metric=`, `alert=`, and `owner=` — no finding is missing any hook field
3. No hooks are consolidated into a standalone section
4. Each gap is distinct — no two findings describe the same problem

**Do not begin Phase 3 until all four conditions are verified.**

---

## PHASE 3 — Completeness Certification

Fill this checklist now. Check each box. Write the count. Include this block in the artifact exactly as filled. Do not write the artifact file until the count reads "3 of 3".

- [ ] GAP subsection present with >=1 finding carrying inline metric/alert/owner
- [ ] DCV subsection present with >=1 finding carrying inline metric/alert/owner
- [ ] MRF subsection present with >=1 finding carrying inline metric/alert/owner

Finding types present: ___ of 3

---

### Output

Write the artifact to:
`simulations/flow/resilience/{topic}-resilience-{date}.md`

The artifact must include:
1. All three Phase 1 scenario contracts — four-column tables (Row | Field | Content | Owned by), all rows filled, sequential row index unbroken, in-row imperatives present at rows 7 and 10/11 of each scenario
2. All Phase 2 gap findings — each finding followed immediately by its observability hook on the next line
3. The Phase 3 completeness checklist — all three boxes checked, "Finding types present: 3 of 3" confirmed

Return the file path when done.
