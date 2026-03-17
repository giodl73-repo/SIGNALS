Now I have everything I need to construct the R9 variations. R8 V-05 is the baseline (13/21, composite 96.19); all 13 criteria are cracked and the rubric has no open criteria. R9 must hold all 13 while probing axes that surface new patterns for potential C-30+ expansion.

**Axes selected:**
- Single-axis: Phrasing register (V-01), Lifecycle emphasis / SLA per stage (V-02), Inertia framing / quantified accumulation rate (V-03)
- Combinations: V-02 + V-03 (V-04), all three (V-05)

---

# flow-resilience — Round 9 Variations

**Rubric**: v8 (21 aspirational criteria, denominator 21)
**R8 ceiling**: V-05 at 96.19 (13/21, composite 60 + 30 + 6.19)
**Open criteria entering R9**: none — C-28 and C-29 both cracked by R8 V-05
**R9 premise**: Hold all 13 criteria; probe three unexplored axes for new pattern candidates (C-30+)

---

## Axis Selection

| Axis | Single-axis variation | Rationale |
|------|----------------------|-----------|
| Phrasing register | V-01 | Unexplored; tests whether rubric compliance is structural (any register achieves 13/21) or stylistic (formal imperative required) |
| Lifecycle emphasis — SLA per stage | V-02 | C-28 measures sub-field completeness; adding time-budget targets (TTD/TTC/TTR/TTV) introduces a quantitative commitment dimension not yet captured by any criterion |
| Inertia framing — quantified accumulation | V-03 | C-29 requires chronic statement; adding three-component specification (metric / rate / horizon) strengthens the floor; candidate C-30 |

Single-axis: **V-01** (conversational), **V-02** (SLA stages), **V-03** (accumulation rate)
Combinations: **V-04** (V-02 + V-03), **V-05** (all three)

---

## V-01 — Phrasing Register: Conversational Imperative

**Variation axis**: Phrasing register — second-person conversational imperative throughout; all structural mechanisms preserved verbatim from R8 V-05 baseline
**Hypothesis**: Register is orthogonal to structural compliance. All 13 criteria (C-17 through C-29) hold in conversational register because the rubric measures mechanism presence, not tone. New excellence signal: register shift may improve instruction-following in chat-oriented deployment contexts, surfacing whether formal imperative grammar is load-bearing or incidental.

---

Simulate degraded conditions for: **{{topic}}**

You're working as two specialists — **D** (distributed systems) and **C** (commerce) — and your job is to document exactly what breaks, what survives, and what the path back looks like. Three failure classes, one row each, all three in a single table.

---

**Four things prevent you from skipping content. Read all four before producing a word of output:**

| Level | Mechanism | Scope | Artifact |
|-------|-----------|-------|---------|
| Table | Unified `#` column + no-split instruction | All three rows in one table | see **No-Split Instruction** section below |
| Section | Phase gate | All rows complete before Gap Register | see **Phase Gate** section below |
| Column | Column ownership contract | Every column named and owned | see **Column Contract** section below |
| Slot | In-row imperatives inside Row Descriptor | Each row, at cell granularity | inside the **Row Descriptor** section below |

---

### No-Split Instruction

Your scenario table is one table. Three rows, nine columns, no breaks.

**Don't create separate tables for D columns and C columns.** The switch from D-owned to C-owned columns isn't a section break, a sub-table trigger, or a structural boundary of any kind.

**Don't drop in a horizontal rule, heading, or blank-line break between rows when column ownership changes.** If you'd naturally write `---` or a bold header there — don't. That's a structural violation.

---

### Column Contract

Before you build any row, know what you owe for each column:

| Column | Owner | What to write |
|--------|-------|--------------|
| `#` | — | Row number (1, 2, 3). Required. No omission. |
| Scenario Class | — | Exactly one of: "Class 1 — Offline" / "Class 2 — Partial Failure" / "Class 3 — Split-Brain" |
| System State | D | Which components are unavailable, which data stores are in what consistency mode, which in-flight operations are affected. Name specific services — not "the system". |
| User Capability | C | Three statements minimum: what the user can do (positive), what fails silently (negative), what surfaces an error state (degraded). Use commerce verbs: checkout, reserve, authorize, fulfill. |
| Data at Risk | D | Specific entity names and failure modes. Not "data may be lost" — name the record type, the field, and whether it is lost, stale, or inconsistent. |
| Recovery Path | D+C | Four stages, all required: **Detect** (how the system knows it failed) / **Contain** (how further damage is stopped) / **Recover** (how consistency is restored) / **Validate** (how recovery is confirmed). One concrete mechanism per stage. |
| Severity | D | One word: DEGRADED / IMPAIRED / DOWN |
| Blast Radius | C | Which user segment, roughly what scope. Quantify where you can. |
| Status Quo Risk | C | What keeps accumulating if this gap is **never** fixed — not the per-incident impact, the carrying cost of inaction. Form: "if this gap is never addressed, [ongoing business consequence]." Give a specific accumulating metric: oversell rate, reconciliation backlog, duplicate charge count. |

---

### Phase Gate

**Write all three scenario rows before you write anything in the Gap Register.**

You can't start the Gap Register header, the first gap finding, or any section below the scenario table until all three rows are done — no placeholder rows, no partial rows.

---

### Row Descriptor

Here's what goes in each row, written at cell granularity to make omissions impossible:

| # | Scenario Class | Content Descriptor |
|---|---------------|--------------------|
| 1 | Class 1 — Offline | **Write this row now.** System State: describe the client-side connectivity state and which server-side operations are in flight at the moment of disconnection — specific service names, not "network unavailable". User Capability: name three commerce actions — one that completes from local cache, one that fails silently, one that surfaces an error. Data at Risk: name the specific entity (order record, cart state, payment token) at risk and whether it is lost or stale. Recovery Path: all four stages — Detect (client heartbeat failure detection), Contain (local write queue activation), Recover (sync on reconnect), Validate (server reconciliation confirms no duplicate orders). Status Quo Risk: name the business metric that grows if offline support is never built (e.g., cart abandonment rate compounds per connectivity event, with no natural ceiling without offline-first architecture). **Don't move to row 2 until every column in this row is filled, including all four Recovery Path stages (Detect/Contain/Recover/Validate).** |
| 2 | Class 2 — Partial Failure | **Write this row now.** System State: name the specific dependent service that's unavailable and which commerce operations depend on it. User Capability: distinguish operations that degrade gracefully (fallback to cached pricing) from operations that hard-fail (live payment auth required). Data at Risk: name the specific inventory reservation, payment authorization token, or order state at risk during the outage — entity + failure mode. Recovery Path: all four stages — Detect (health check or timeout threshold), Contain (circuit breaker or fallback routing), Recover (service restore + replay of queued operations), Validate (idempotency check confirms no duplicate state). Status Quo Risk: name the metric that accumulates if partial-failure handling is never implemented (e.g., authorization failure rate grows per service degradation event). **Don't move to row 3 until every column in this row is filled, including all four Recovery Path stages (Detect/Contain/Recover/Validate).** |
| 3 | Class 3 — Split-Brain | If node A's version wins the merge: inventory is oversold, cart total reflects stale pricing, payment is double-charged. If node B's version wins: order status reverts, coupon redemption is duplicated, fulfillment fires twice. If a naive merge runs: all three consequences compound. **Write this row now.** System State: describe the partition state — which nodes are isolated, what consistency level applies (eventual/strong/causal), what the conflict detection mechanism is. User Capability: name which commerce operations are safe under eventual consistency (read-only catalog browsing) vs. unsafe (inventory reservation, payment submission). Data at Risk: name the specific entity versions in conflict — order records, inventory counters, payment idempotency keys — and the conflict-resolution strategy. Recovery Path: all four stages — Detect (vector clock or CRDT divergence detection), Contain (write quorum enforcement or read-your-writes guarantee), Recover (conflict resolution: last-write-wins vs. merge vs. manual adjudication), Validate (post-merge audit confirms no oversell or double-charge). Status Quo Risk: if this split-brain scenario is never addressed, oversell rate accumulates per-deploy cycle, payment reconciliation backlog grows unbounded, and duplicate fulfillment charges compound indefinitely. **Don't complete this row without confirming all four Recovery Path stages are present and all three per-outcome consequences above are addressed in the row.** |

---

### Scenario Analysis Table

One table. All three rows. No sub-tables, no horizontal rules between rows, no role-sequence breaks.

| # | Scenario Class | System State | User Capability | Data at Risk | Recovery Path | Severity | Blast Radius | Status Quo Risk |

---

### Gap Register

After all three rows are complete, write the Gap Register. Three gap types, each labeled and actionable:

1. **Offline Experience Gap** — name the specific commerce flow that has no offline fallback, the user-visible failure mode, and the minimum viable fix.
2. **Data Consistency Violation** — name the specific entity that can become inconsistent, the consistency model that fails to prevent it, and the recommended consistency level.
3. **Missing Recovery Flow** — name the specific recovery step that is absent, which scenario class it affects, and the remediation.

"Offline support may be limited" is not a gap finding. Name the flow, the failure mode, the fix.

---

## V-02 — Lifecycle Emphasis: Recovery Path with SLA Budget per Stage

**Variation axis**: Lifecycle emphasis — Recovery Path stages gain explicit time-budget targets (TTD/TTC/TTR/TTV) in the Column Contract and all Row Descriptor cells. Each stage requires a named mechanism AND a time-to-resolution target. Generic stage descriptions without time budgets fail the column fill requirement.
**Hypothesis**: Stage-level time specification is a new structural pattern not captured by any current criterion. C-28 measures sub-field completeness (all four stages present); adding time-budget targets introduces a quantitative commitment dimension — the fill requirement is not just "write the stage" but "write the stage with a temporal commitment." Candidate C-30: Recovery SLA per stage — each stage in the Recovery Path column names a time-budget target alongside its mechanism.

---

Simulate degraded conditions for: **{{topic}}**

Two specialist roles contribute to this analysis:

**Distributed Systems Expert (D)** — owns partition mechanics, consistency models, CAP theorem trade-offs, retry semantics, idempotency requirements, conflict-resolution strategies, and operational SLA commitments.

**Commerce Expert (C)** — owns business consequence translation: what failure means in checkout, inventory reservation, payment processing, and order fulfillment terms.

---

## Anti-Omission Architecture

Four mechanisms prevent output omission at four distinct structural levels. Confirm all four before producing any output:

| Level | Mechanism | Scope | Artifact |
|-------|-----------|-------|---------|
| Table | Unified `#` column + anti-split instruction | All three scenario rows in one table | see **Anti-Boundary Instruction** section below |
| Section | Phase gate | All rows complete before Gap Register | see **Phase Gate** section below |
| Column | Column Contract with SLA-stage specification | All nine columns | see **Column Contract** section below |
| Slot | In-row bold imperatives inside Row Descriptor Table | Per row, at cell granularity | inside the **Row Descriptor Table** section below |

---

## Anti-Boundary Instruction

The Scenario Analysis Table is a single unified table. All three rows share the same structure.

**Do not create separate tables for Distributed Systems Expert columns and Commerce Expert columns.** The column ownership transition is not a sub-table boundary, not a role-sequence trigger, and not a structural break of any kind.

**Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts.** Any `---` separator, bold heading, or whitespace break between rows is a structural violation.

---

## Column Contract

| Name | Owner | Fill Requirement |
|------|-------|-----------------|
| `#` | — | Row index (1, 2, 3). Every row must carry this. No omission. |
| Scenario Class | — | Exactly one of: "Class 1 — Offline" / "Class 2 — Partial Failure" / "Class 3 — Split-Brain" |
| System State | D | Name specific components and their states: which services are unavailable, which data stores are in what consistency mode, which operations are in flight. "The system is offline" fails — name the service. |
| User Capability | C | Three statements minimum: what the user can do (positive), what fails silently (negative), what surfaces an error (degraded). Reference specific commerce operations. |
| Data at Risk | D | Name specific data entities, fields, and failure modes (lost / stale / inconsistent). Generic "data may be lost" fails. |
| Recovery Path | D+C | Four stages, all required, each with a **named mechanism AND a time-budget target**: **Detect** (how the system discovers failure; TTD target: ≤5 min) / **Contain** (how further damage is stopped; TTC target: ≤15 min) / **Recover** (how consistency is restored; TTR target: scenario-specific, must be stated explicitly) / **Validate** (how recovery is confirmed; TTV target: ≤10 min). A stage entry that names a mechanism without a time-budget target fails this column's fill requirement. "Monitor logs" without a TTD target fails. |
| Severity | D | DEGRADED / IMPAIRED / DOWN. One word. |
| Blast Radius | C | Affected user segment with scope estimate. Quantify where possible. |
| Status Quo Risk | C | What accumulates if this gap is never fixed: the chronic carrying cost of inaction. Form: "if this gap is never addressed, [accumulating metric and growth pattern]." A specific accumulating metric with growth context required — "oversell rate accumulates per-deploy" satisfies; "data integrity issues persist" fails. |

---

## Phase Gate

**Produce all three scenario rows before writing the Gap Register or any section that follows.**

The Gap Register header, the first gap finding, and any subsequent section must not appear until all three rows of the Scenario Analysis Table contain non-placeholder content in every column, including all four Recovery Path stages with time-budget targets.

---

## Row Descriptor Table

| # | Scenario Class | Content Descriptor |
|---|---------------|--------------------|
| 1 | Class 1 — Offline | **Write this row now.** System State: client-side connectivity state + specific server-side operations in flight at disconnection moment — service names required. User Capability: three commerce actions — one completes from local cache, one fails silently, one surfaces an error. Data at Risk: specific entity (order record, cart state, payment token) + whether lost, stale, or inconsistent. Recovery Path: all four stages with time-budget targets — **Detect**: client heartbeat failure threshold triggers offline mode (TTD ≤5 min); **Contain**: local write queue activation halts server-bound mutations (TTC ≤15 min); **Recover**: reconnect sync with server reconciliation of queued writes (TTR: state explicitly based on queue depth); **Validate**: server confirms no duplicate orders created, local queue empty and acknowledged (TTV ≤10 min). Status Quo Risk: name the accumulating metric and growth context if offline support is never built (e.g., cart abandonment count compounds per connectivity event with no natural resolution ceiling). **Do not advance to row 2 until this row contains non-placeholder content in every column, including all four Recovery Path stages with time-budget targets (Detect/TTD, Contain/TTC, Recover/TTR, Validate/TTV).** |
| 2 | Class 2 — Partial Failure | **Write this row now.** System State: name the specific dependent service unavailable + which commerce operations require it. User Capability: distinguish graceful-degradation operations (fallback to cached pricing) from hard-fail operations (live payment authorization requires live service). Data at Risk: specific inventory reservation, payment authorization token, or order state at risk — entity name + failure mode. Recovery Path: all four stages with time-budget targets — **Detect**: health check interval or timeout threshold (TTD ≤5 min); **Contain**: circuit breaker trip or fallback routing activation (TTC ≤15 min); **Recover**: service restoration + idempotent replay of queued operations with deduplication (TTR: state explicitly based on replay queue depth); **Validate**: idempotency check across all affected entities confirms no duplicate state (TTV ≤10 min). Status Quo Risk: name the accumulating metric and growth context if partial-failure handling is never implemented (e.g., authorization failure count grows per service degradation event with no circuit-breaker ceiling). **Do not advance to row 3 until this row contains non-placeholder content in every column, including all four Recovery Path stages with time-budget targets (Detect/TTD, Contain/TTC, Recover/TTR, Validate/TTV).** |
| 3 | Class 3 — Split-Brain | If node A's version wins the merge: inventory is oversold, cart total reflects stale pricing, payment is double-charged. If node B's version wins: order status reverts, coupon redemption is duplicated, fulfillment fires twice. If a naive merge runs: all three consequences compound. **Write this row now.** System State: partition state — which nodes isolated, what consistency level (eventual/strong/causal), what conflict detection mechanism operates. User Capability: which commerce operations are safe under eventual consistency (read-only catalog browsing) vs. require strong consistency (inventory reservation, payment submission). Data at Risk: specific entity versions in conflict — order records, inventory counters, payment idempotency keys — and the conflict-resolution strategy (last-write-wins / merge / adjudication). Recovery Path: all four stages with time-budget targets — **Detect**: divergence detection via vector clocks or CRDT write-set comparison (TTD ≤5 min after write-set conflict); **Contain**: write quorum enforcement or read-your-writes guarantee activation (TTC ≤15 min); **Recover**: conflict resolution with explicit strategy named and TTR stated based on conflict complexity; **Validate**: post-merge audit confirms no oversell, no double-charge, idempotency keys reconciled (TTV ≤10 min after resolution). Status Quo Risk: if this split-brain scenario is never addressed, oversell rate accumulates per-deploy cycle, payment reconciliation backlog grows unbounded, and duplicate fulfillment charges compound indefinitely. **Do not complete this row without confirming all four Recovery Path stages with time-budget targets (Detect/TTD, Contain/TTC, Recover/TTR, Validate/TTV) are present and all three per-outcome consequences above are addressed in the System State and Recovery Path cells.** |

---

## Scenario Analysis Table

One unified table. All three rows. No sub-tables, no horizontal rules between rows, no breaks on column ownership transitions.

| # | Scenario Class | System State | User Capability | Data at Risk | Recovery Path | Severity | Blast Radius | Status Quo Risk |

---

## Gap Register

After all three rows are complete, produce the Gap Register. Three gap types:

1. **Offline Experience Gap** — specific commerce flow with no offline fallback + user-visible failure mode + minimum viable fix including a TTR target.
2. **Data Consistency Violation** — specific entity that becomes inconsistent + consistency model that fails + recommended consistency level with expected TTD improvement.
3. **Missing Recovery Flow** — specific absent recovery step + scenario class affected + remediation with target TTC or TTR improvement.

Generic gap statements fail. Each finding requires: specific entity, specific failure mode, specific fix, temporal target.

---

## V-03 — Inertia Framing: Three-Component Accumulation Specification in Status Quo Risk

**Variation axis**: Inertia framing — Status Quo Risk column requires a three-part chronic specification: **(1) Metric** (the specific accumulating business metric), **(2) Rate** (the accumulation rate expressed per-event or per-time-unit), **(3) Horizon** (why there is no natural ceiling without intervention). Row Descriptor Table gains sub-field gate names referencing all three components, extending C-28's sub-field completeness pattern into the Status Quo Risk column.
**Hypothesis**: C-29 requires a chronic consequence statement but does not specify its internal structure. A three-component requirement (metric/rate/horizon) creates a new sub-field completeness gate within Status Quo Risk — parallel to C-28's gate within Recovery Path. Candidate C-30: Accumulation-rate specification — the chronic consequence names not just what accumulates but how fast and why it has no natural ceiling without intervention.

---

Simulate degraded conditions for: **{{topic}}**

Two specialist roles contribute:

**Distributed Systems Expert (D)** — partition mechanics, consistency models, CAP theorem trade-offs, retry semantics, idempotency requirements, conflict-resolution strategies.

**Commerce Expert (C)** — business consequence translation: what each failure mode means in checkout, inventory, payment, and fulfillment terms, including chronic cost-of-inaction quantification.

---

## Anti-Omission Architecture

Four mechanisms, four levels, zero overlap:

| Level | Mechanism | Scope | Artifact |
|-------|-----------|-------|---------|
| Table | Unified `#` column + anti-split instruction | All three rows in one table | see **Anti-Boundary Instruction** section below |
| Section | Phase gate | All rows before Gap Register | see **Phase Gate** section below |
| Column | Column Contract with three-component Status Quo Risk specification | All nine columns | see **Column Contract** section below |
| Slot | In-row bold imperatives inside Row Descriptor Table | Per row, at cell granularity | inside the **Row Descriptor Table** section below |

---

## Anti-Boundary Instruction

The Scenario Analysis Table is a single unified table.

**Do not create separate tables for Distributed Systems Expert columns and Commerce Expert columns.** Column ownership transitions are not sub-table boundaries, not role-sequence triggers, not structural breaks.

**Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts.** Any `---`, bold header, or spacing break between rows is a violation.

---

## Column Contract

| Name | Owner | Fill Requirement |
|------|-------|-----------------|
| `#` | — | Row index: 1, 2, 3. No row may omit this. |
| Scenario Class | — | Exactly: "Class 1 — Offline" / "Class 2 — Partial Failure" / "Class 3 — Split-Brain" |
| System State | D | Named components and states: which services unavailable, which data stores in what consistency mode, which operations in flight. No generic "the system". |
| User Capability | C | Three statements: positive (what works), negative (what fails silently), degraded (what errors). Specific commerce operations. |
| Data at Risk | D | Specific entities and failure modes: entity name + lost/stale/inconsistent. Not generic. |
| Recovery Path | D+C | Four stages, all required: **Detect** / **Contain** / **Recover** / **Validate**. One concrete mechanism per stage. |
| Severity | D | DEGRADED / IMPAIRED / DOWN |
| Blast Radius | C | Segment + scope estimate. Quantify where possible. |
| Status Quo Risk | C | Three-component chronic specification — all three required: **(1) Metric**: the specific business metric that accumulates (e.g., "oversell count", "reconciliation queue depth", "duplicate charge count"); **(2) Rate**: how fast it accumulates, in what units (e.g., "per deploy", "per hour of outage", "per concurrent write conflict"); **(3) Horizon**: why there is no natural ceiling without an explicit intervention (e.g., "with no idempotency gate, each new deployment resets the exposure window without clearing the prior backlog"). A Status Quo Risk cell that names (1) only, without stating (2) and (3), fails this column's fill requirement. |

---

## Phase Gate

**Produce all three scenario rows before writing the Gap Register or any subsequent section.**

No Gap Register header, no gap finding, no subsequent content until all three rows contain non-placeholder content in every column, including all three Status Quo Risk components.

---

## Row Descriptor Table

| # | Scenario Class | Content Descriptor |
|---|---------------|--------------------|
| 1 | Class 1 — Offline | **Write this row now.** System State: client-side connectivity state + specific server-side operations in flight at disconnection — service names required. User Capability: three commerce actions — one completes from cache, one fails silently, one errors. Data at Risk: specific entity (order record, cart, payment token) + failure mode (lost/stale/inconsistent). Recovery Path: all four stages — Detect (client heartbeat failure), Contain (local write queue), Recover (reconnect sync), Validate (server reconciliation confirms no duplicate orders). Status Quo Risk: **(1)** name the accumulating metric (e.g., abandoned cart instance count); **(2)** state the accumulation rate (e.g., "per connectivity event affecting a checkout session in progress"); **(3)** explain the unbounded horizon (e.g., "no natural resolution without offline-first architecture — each connectivity failure adds to the total regardless of session frequency"). **Do not advance to row 2 until this row contains non-placeholder content in every column, including all four Recovery Path stages (Detect/Contain/Recover/Validate) and all three Status Quo Risk components (metric / rate / horizon).** |
| 2 | Class 2 — Partial Failure | **Write this row now.** System State: name the specific dependent service + which commerce operations require it. User Capability: graceful-degradation operations vs. hard-fail operations, each named. Data at Risk: specific entity + failure mode. Recovery Path: all four stages — Detect (health check or timeout threshold), Contain (circuit breaker or fallback routing), Recover (service restore + idempotent replay of queued operations), Validate (idempotency check confirms no duplicate state). Status Quo Risk: **(1)** name the accumulating metric (e.g., failed payment authorization count); **(2)** state the accumulation rate (e.g., "per service degradation event that overlaps an active checkout session"); **(3)** explain the unbounded horizon (e.g., "auth failure backlog has no auto-remediation path without circuit-breaker policy — failed attempts accumulate across events"). **Do not advance to row 3 until this row contains non-placeholder content in every column, including all four Recovery Path stages (Detect/Contain/Recover/Validate) and all three Status Quo Risk components (metric / rate / horizon).** |
| 3 | Class 3 — Split-Brain | If node A's version wins the merge: inventory is oversold, cart total reflects stale pricing, payment is double-charged. If node B's version wins: order status reverts, coupon redemption is duplicated, fulfillment fires twice. If a naive merge runs: all three consequences compound. **Write this row now.** System State: partition state — which nodes isolated, what consistency level (eventual/strong/causal), how conflicts are detected. User Capability: commerce operations safe under eventual consistency vs. requiring strong consistency. Data at Risk: specific entity versions in conflict — order records, inventory counters, payment idempotency keys — with conflict-resolution strategy. Recovery Path: all four stages — Detect (vector clock or CRDT divergence), Contain (write quorum or read-your-writes guarantee), Recover (conflict resolution: last-write-wins vs. merge vs. manual adjudication), Validate (post-merge audit confirms no oversell or double-charge). Status Quo Risk: **(1)** metrics — oversell count + reconciliation queue depth + duplicate charge count (three distinct accumulating metrics, all required); **(2)** rates — oversell rate per-deploy cycle, reconciliation records per concurrent write conflict, duplicate charges per unresolved partition event; **(3)** horizon — no natural ceiling without explicit conflict-resolution policy and idempotency key enforcement: each deploy cycle adds to oversell exposure, each conflict event extends reconciliation backlog, each unresolved partition adds duplicate charges. **Do not complete this row without confirming all four Recovery Path stages (Detect/Contain/Recover/Validate) are present, all three per-outcome consequences above are addressed, and all three Status Quo Risk components (metric / rate / horizon) are named with the specificity above.** |

---

## Scenario Analysis Table

One unified table. All three rows. No sub-tables, no horizontal rules between rows, no structural breaks between column ownership blocks.

| # | Scenario Class | System State | User Capability | Data at Risk | Recovery Path | Severity | Blast Radius | Status Quo Risk |

---

## Gap Register

After all three rows are complete, write the Gap Register. Three gap types:

1. **Offline Experience Gap** — specific commerce flow with no offline fallback + user-visible failure mode + minimum viable fix.
2. **Data Consistency Violation** — specific entity that becomes inconsistent + failing consistency model + recommended consistency level.
3. **Missing Recovery Flow** — specific absent recovery step + scenario class affected + remediation.

Each finding must name the Status Quo Risk metric from the corresponding row that the fix will stop accumulating. Generic gap statements fail.

---

## V-04 — Lifecycle Emphasis + Inertia Framing (V-02 + V-03)

**Variation axis**: V-02 SLA budget per Recovery Path stage + V-03 three-component Status Quo Risk specification
**Hypothesis**: SLA stages and quantified accumulation rate address independent specification gaps in different columns. Combined, they produce a two-dimensional operational commitment: Recovery Path becomes a temporal specification (when the system will recover) and Status Quo Risk becomes an economic accumulation specification (what the cost grows to if it never recovers). Together these constitute a candidate two-criterion expansion: C-30 (Recovery SLA per stage) + C-31 (Accumulation rate in chronic consequence).

---

Simulate degraded conditions for: **{{topic}}**

Two specialist roles:

**Distributed Systems Expert (D)** — partition mechanics, consistency models, CAP theorem trade-offs, retry semantics, idempotency requirements, conflict-resolution strategies, and operational SLA commitments.

**Commerce Expert (C)** — business consequence translation: failure modes in checkout, inventory, payment, and fulfillment terms, including chronic cost-of-inaction quantification with accumulation rate specification.

---

## Anti-Omission Architecture

| Level | Mechanism | Scope | Artifact |
|-------|-----------|-------|---------|
| Table | Unified `#` column + anti-split instruction | All three rows in one table | see **Anti-Boundary Instruction** section below |
| Section | Phase gate | All rows complete before Gap Register | see **Phase Gate** section below |
| Column | Column Contract with SLA-stage + three-component Status Quo Risk specification | All nine columns | see **Column Contract** section below |
| Slot | In-row bold imperatives inside Row Descriptor Table | Per row, at cell granularity | inside the **Row Descriptor Table** section below |

---

## Anti-Boundary Instruction

Single unified Scenario Analysis Table.

**Do not create separate tables for Distributed Systems Expert columns and Commerce Expert columns.** Ownership transitions are not sub-table boundaries, not role-sequence triggers, not structural breaks.

**Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts.** `---`, bold headers, and spacing breaks between rows are structural violations.

---

## Column Contract

| Name | Owner | Fill Requirement |
|------|-------|-----------------|
| `#` | — | Row index 1, 2, 3. Required, no omission. |
| Scenario Class | — | Exactly: "Class 1 — Offline" / "Class 2 — Partial Failure" / "Class 3 — Split-Brain" |
| System State | D | Named components and consistency states. Specific service names required. |
| User Capability | C | Three statements: positive / negative / degraded, with specific commerce operations. |
| Data at Risk | D | Specific entity name + failure mode (lost/stale/inconsistent). |
| Recovery Path | D+C | Four stages, all required, each with **named mechanism AND time-budget target**: **Detect** (TTD ≤5 min) / **Contain** (TTC ≤15 min) / **Recover** (TTR: stated explicitly, scenario-specific) / **Validate** (TTV ≤10 min). A stage entry without its time-budget target fails this column's fill requirement. |
| Severity | D | DEGRADED / IMPAIRED / DOWN |
| Blast Radius | C | Segment + scope, quantified where possible. |
| Status Quo Risk | C | Three-component chronic specification, all required: **(1) Metric** — specific accumulating business metric by name; **(2) Rate** — accumulation rate per event or per time unit; **(3) Horizon** — why no natural ceiling exists without intervention. Naming only (1) without (2) and (3) fails. |

---

## Phase Gate

**Produce all three rows before writing the Gap Register or any following section.**

No gap content until every column of every row contains non-placeholder content, including all four Recovery Path stages with time-budget targets and all three Status Quo Risk components.

---

## Row Descriptor Table

| # | Scenario Class | Content Descriptor |
|---|---------------|--------------------|
| 1 | Class 1 — Offline | **Write this row now.** System State: client-side connectivity state + specific in-flight server operations at disconnection. User Capability: three commerce actions — cache-complete / silent-fail / error. Data at Risk: specific entity + failure mode. Recovery Path: all four stages with time budgets — **Detect**: client heartbeat failure threshold triggers offline detection (TTD ≤5 min); **Contain**: local write queue activated, all server-bound mutations halted (TTC ≤15 min); **Recover**: reconnect triggers sync with server, queued writes replayed with deduplication (TTR: state explicitly based on queue depth and bandwidth); **Validate**: server confirms queue empty, no duplicate orders created, session state reconciled (TTV ≤10 min). Status Quo Risk: (1) metric name (e.g., abandoned cart count); (2) accumulation rate (e.g., per connectivity event affecting an active checkout session); (3) unbounded horizon (e.g., no natural resolution ceiling without offline-first architecture — each event adds regardless of prior events). **Do not advance to row 2 until this row contains non-placeholder content in every column, including all four Recovery Path stages with time-budget targets (Detect/TTD, Contain/TTC, Recover/TTR, Validate/TTV) and all three Status Quo Risk components (metric / rate / horizon).** |
| 2 | Class 2 — Partial Failure | **Write this row now.** System State: specific dependent service + dependent commerce operations. User Capability: graceful-degrade vs. hard-fail operations — name each. Data at Risk: specific entity + failure mode. Recovery Path: all four stages with time budgets — **Detect**: health check interval or timeout threshold (TTD ≤5 min); **Contain**: circuit breaker trips to fallback routing or degraded mode (TTC ≤15 min); **Recover**: service restore + idempotent replay of queued operations with deduplication (TTR: stated explicitly based on replay queue depth); **Validate**: idempotency check across all affected entities confirms no duplicate state (TTV ≤10 min). Status Quo Risk: (1) metric name (e.g., failed authorization count); (2) accumulation rate (e.g., per service degradation event overlapping an active checkout); (3) unbounded horizon (e.g., auth failure backlog has no auto-remediation path without circuit-breaker policy). **Do not advance to row 3 until this row contains non-placeholder content in every column, including all four Recovery Path stages with time-budget targets (Detect/TTD, Contain/TTC, Recover/TTR, Validate/TTV) and all three Status Quo Risk components (metric / rate / horizon).** |
| 3 | Class 3 — Split-Brain | If node A's version wins the merge: inventory is oversold, cart total reflects stale pricing, payment is double-charged. If node B's version wins: order status reverts, coupon redemption is duplicated, fulfillment fires twice. If a naive merge runs: all three consequences compound. **Write this row now.** System State: partition state — isolated nodes, consistency level (eventual/strong/causal), conflict detection mechanism. User Capability: safe vs. unsafe operations under eventual consistency. Data at Risk: conflicting entity versions — order records, inventory counters, payment idempotency keys — with resolution strategy named. Recovery Path: all four stages with time budgets — **Detect**: divergence detection via vector clocks or CRDT write-set comparison (TTD ≤5 min after write-set conflict); **Contain**: write quorum enforcement or read-your-writes guarantee activation (TTC ≤15 min); **Recover**: conflict resolution strategy named explicitly (last-write-wins / merge / adjudication) with TTR stated based on conflict complexity; **Validate**: post-merge audit — no oversell, no double-charge, idempotency keys reconciled (TTV ≤10 min after resolution). Status Quo Risk: (1) metrics — oversell count + reconciliation queue depth + duplicate charge count (all three required); (2) rates — oversell rate per-deploy cycle, reconciliation records per conflict event, duplicate charges per unresolved partition; (3) horizon — no natural ceiling without explicit conflict-resolution policy: each deploy adds oversell exposure, each conflict extends reconciliation backlog, each partition adds duplicate charges. **Do not complete this row without confirming all four Recovery Path stages with time-budget targets (Detect/TTD, Contain/TTC, Recover/TTR, Validate/TTV), all three per-outcome consequences above addressed in the row, and all three Status Quo Risk components (metric / rate / horizon) present.** |

---

## Scenario Analysis Table

One unified table. Three rows. No sub-tables, no horizontal rules, no breaks between column ownership blocks.

| # | Scenario Class | System State | User Capability | Data at Risk | Recovery Path | Severity | Blast Radius | Status Quo Risk |

---

## Gap Register

After all three rows are complete:

1. **Offline Experience Gap** — specific flow + failure mode + minimum viable fix with TTR improvement target.
2. **Data Consistency Violation** — specific entity + failing consistency model + recommended consistency level.
3. **Missing Recovery Flow** — specific absent recovery step + scenario class + remediation with TTC or TTR improvement target.

Each finding names the Status Quo Risk metric from its row and estimates the expected reduction in accumulation rate the fix delivers.

---

## V-05 — All Three Axes: Conversational + SLA Stages + Quantified Accumulation

**Variation axis**: V-01 (phrasing register) + V-02 (SLA budget per stage) + V-03 (three-component Status Quo Risk specification)
**Hypothesis**: Register shift is structurally neutral. Combining SLA specification with three-component accumulation rate produces the highest operational density variation in R9: Recovery Path becomes a temporal commitment (when recovery completes) and Status Quo Risk becomes an economic accumulation commitment (what the carrying cost grows to). Combined with conversational register, this tests whether the new structural patterns (candidate C-30/C-31) are register-independent. All 13 criteria hold; new candidates surfaced: (1) Recovery SLA per stage; (2) Accumulation-rate specification in chronic consequence.

---

You're simulating failure scenarios for: **{{topic}}**

Two specialists work this analysis — **D** (distributed systems) and **C** (commerce). Three failure classes, one row each, all three in a single table. Every cell must earn its place.

---

**Four mechanisms prevent you from skipping content. Read all four before writing anything:**

| Level | Mechanism | Scope | Artifact |
|-------|-----------|-------|---------|
| Table | One unified table with `#` column; no splits allowed | All three rows | see **No-Split Instruction** below |
| Section | Phase gate — all rows before gap findings | Three rows, then gaps | see **Phase Gate** below |
| Column | Column contract naming every column's owner and fill requirement | All nine columns | see **Column Contract** below |
| Slot | Row-level imperatives inside the Row Descriptor, at cell granularity | Each row | inside the **Row Descriptor** below |

---

### No-Split Instruction

One table. Three rows. Nine columns. Nothing between them.

**Don't split D columns and C columns into separate tables.** The ownership transition from D to C isn't a table break, a sub-section, or any kind of boundary.

**Don't put a horizontal rule, heading, or spacing break between rows when column ownership changes.** If you'd put a `---` there, don't — that's a structural violation.

---

### Column Contract

| Column | Owner | What to write |
|--------|-------|--------------|
| `#` | — | 1, 2, 3. Every row. |
| Scenario Class | — | Exactly "Class 1 — Offline" / "Class 2 — Partial Failure" / "Class 3 — Split-Brain" |
| System State | D | Specific components and states. Name the service — not "the system". |
| User Capability | C | Three statements: what works (positive), what fails silently (negative), what errors (degraded). Use commerce verbs. |
| Data at Risk | D | Entity name + failure mode. Not generic. |
| Recovery Path | D+C | Four stages, each with a **mechanism AND a time-budget target**: **Detect** (TTD ≤5 min) / **Contain** (TTC ≤15 min) / **Recover** (TTR: state explicitly — no default) / **Validate** (TTV ≤10 min). A stage without its TTx target fails. |
| Severity | D | DEGRADED / IMPAIRED / DOWN |
| Blast Radius | C | Segment + scope estimate |
| Status Quo Risk | C | Three parts, all required: **(1) Metric** — which specific business metric accumulates; **(2) Rate** — how fast, in what units (per deploy, per hour, per conflict event); **(3) Horizon** — why there's no natural ceiling without a fix. Naming just (1) without (2) and (3) fails. |

---

### Phase Gate

**Finish all three rows before you write anything in the Gap Register.**

No gap heading, no first gap bullet, no "Findings" section — not until all three rows are done, no placeholders, no partial rows.

---

### Row Descriptor

| # | Scenario Class | Content Descriptor |
|---|---------------|--------------------|
| 1 | Class 1 — Offline | **Write this row now.** System State: client-side connectivity state + which specific server operations are in flight at disconnection — service names required. User Capability: three commerce actions — one completes from cache, one fails silently, one errors out. Data at Risk: specific entity (order record, cart state, payment token) + whether it's lost, stale, or inconsistent. Recovery Path: four stages with time budgets — **Detect**: client heartbeat failure triggers offline detection (TTD ≤5 min); **Contain**: local write queue activated, server-bound mutations halted (TTC ≤15 min); **Recover**: reconnect sync + server reconciliation of queued writes (TTR: state explicitly based on queue depth); **Validate**: server confirms queue empty + no duplicate orders created (TTV ≤10 min). Status Quo Risk: (1) name the metric (e.g., abandoned cart count); (2) state the rate (e.g., per connectivity event affecting an active checkout session); (3) explain the horizon (e.g., no natural resolution ceiling without offline-first architecture — each event adds regardless of prior recovery). **Don't move to row 2 until every column is filled, including all four Recovery Path stages with time-budget targets (Detect/TTD, Contain/TTC, Recover/TTR, Validate/TTV) and all three Status Quo Risk components (metric / rate / horizon).** |
| 2 | Class 2 — Partial Failure | **Write this row now.** System State: name the specific dependent service + which commerce operations need it. User Capability: what degrades gracefully (cached pricing fallback) vs. hard-fails (live payment auth). Data at Risk: specific entity + failure mode. Recovery Path: four stages with time budgets — **Detect**: health check interval or timeout threshold (TTD ≤5 min); **Contain**: circuit breaker trips or fallback routing activates (TTC ≤15 min); **Recover**: service restore + idempotent replay of queued ops with deduplication (TTR: state explicitly based on replay queue depth); **Validate**: idempotency confirm across all affected entities — no duplicate state (TTV ≤10 min). Status Quo Risk: (1) metric (e.g., failed authorization count); (2) rate (e.g., per service degradation event overlapping an active checkout); (3) horizon (e.g., auth failure backlog grows without circuit-breaker policy — no auto-remediation path exists). **Don't move to row 3 until every column is filled, including all four Recovery Path stages with time-budget targets (Detect/TTD, Contain/TTC, Recover/TTR, Validate/TTV) and all three Status Quo Risk components (metric / rate / horizon).** |
| 3 | Class 3 — Split-Brain | If node A's version wins the merge: inventory is oversold, cart total is stale, payment is double-charged. If node B's version wins: order status reverts, coupon redemption is duplicated, fulfillment fires twice. If a naive merge runs: all three compound. **Write this row now.** System State: partition state — which nodes are isolated, what consistency level (eventual/strong/causal), how conflicts are detected. User Capability: safe operations under eventual consistency vs. operations requiring strong consistency. Data at Risk: specific conflicting entity versions — order records, inventory counters, payment idempotency keys — with resolution strategy. Recovery Path: four stages with time budgets — **Detect**: divergence detection via vector clocks or CRDT write-set comparison (TTD ≤5 min after write conflict detected); **Contain**: write quorum or read-your-writes guarantee activated (TTC ≤15 min); **Recover**: conflict resolution strategy named explicitly with TTR stated based on conflict depth; **Validate**: post-merge audit — no oversell, no double-charge, idempotency keys reconciled (TTV ≤10 min after resolution). Status Quo Risk: (1) metrics — oversell count + reconciliation queue depth + duplicate charge count (all three); (2) rates — oversell rate per-deploy cycle, reconciliation records per conflict event, duplicate charges per unresolved partition; (3) horizon — no natural ceiling without conflict-resolution policy: every deploy adds oversell exposure, every conflict extends the backlog, every partition adds duplicate charges. **Don't complete this row without all four Recovery Path stages with time-budget targets (Detect/TTD, Contain/TTC, Recover/TTR, Validate/TTV), all three per-outcome consequences above addressed, and all three Status Quo Risk components (metric / rate / horizon) present.** |

---

### Scenario Analysis Table

One table. Three rows. No sub-tables, no dividers, no section breaks between D columns and C columns.

| # | Scenario Class | System State | User Capability | Data at Risk | Recovery Path | Severity | Blast Radius | Status Quo Risk |

---

### Gap Register

Write this only after all three rows are complete.

1. **Offline Experience Gap** — specific commerce flow + user-visible failure + minimum viable fix with TTR improvement target.
2. **Data Consistency Violation** — specific entity + consistency model that fails + recommended consistency level.
3. **Missing Recovery Flow** — specific absent recovery step + scenario class + remediation with temporal target.

Each finding names the Status Quo Risk metric from its row that the fix will stop accumulating, and estimates the reduction in accumulation rate.

---

## Variation Summary

| # | Axis / Label | Single or Combined | New pattern candidates | Criteria expected |
|---|---|---|---|---|
| V-01 | Phrasing register: conversational imperative | Single | None — register neutrality test | 13/21 (all inherited) |
| V-02 | Lifecycle emphasis: SLA budget per Recovery Path stage (TTD/TTC/TTR/TTV) | Single | C-30: Recovery SLA per stage — temporal commitment inside Recovery Path column | 13/21 + C-30 candidate |
| V-03 | Inertia framing: three-component Status Quo Risk (metric / rate / horizon) | Single | C-30: Accumulation-rate specification in chronic consequence — sub-field gate in Status Quo Risk column | 13/21 + C-30 candidate |
| V-04 | V-02 + V-03: SLA stages + quantified accumulation | Combined | C-30 (Recovery SLA) + C-31 (Accumulation rate) — two-dimensional operational commitment | 13/21 + C-30 + C-31 candidates |
| V-05 | V-01 + V-02 + V-03: all three axes | Combined | Register-independence test for C-30/C-31 candidates | 13/21 + C-30 + C-31 candidates |
