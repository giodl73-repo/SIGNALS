# Flow-Trigger Skill — Round 2 Variations (Rubric v2)

**Skill**: flow-trigger — Simulate which automations fire when a record changes.
**Rubric**: v2 (C-01 through C-14)
**Date**: 2026-03-15

---

## Variation Design Notes

Round 1 variations (rubric v1) established a strong floor: V-01, V-02, V-05 all scored 100 on the 10-criterion rubric. The rubric upgrade to v2 adds four new aspirational criteria derived from Round 1 excellence signals:

- **C-11** — Vocabulary enforcement with negative examples + `[VOCAB FAIL: text]` inline marker
- **C-12** — Evidence-grounded verdict gates + `[INSUFFICIENT]` marker for bare assertions
- **C-13** — Cascade tracing to termination (not fixed depth)
- **C-14** — Trigger graph as explicit edge set for circular detection

Round 2 targets these four underserved criteria. Three single-axis variants, then two combinations.

**Variation map**:

| Variation | Axis | Primary Criteria Targeted | Hypothesis |
|-----------|------|--------------------------|------------|
| V-01 | Output format | C-11 | A Vocabulary Contract table pairing each output field with a prohibited-alternatives column, plus an inline `[VOCAB FAIL]` marker convention defined at the top, drives C-11 more reliably than scattered anti-examples — the reviewer can scan for the marker rather than knowing the vocabulary in advance |
| V-02 | Lifecycle emphasis | C-13, C-14 | Structuring the cascade as a formal iterative loop with an explicit termination condition makes C-13 load-bearing (the loop cannot end until no unmatched side-effect writes remain), and the edge accumulator built during the loop satisfies C-14 as a natural byproduct |
| V-03 | Role sequence | C-12 | A dedicated Evidence Gatekeeper role — whose sole job is to audit each verdict draft for traceable citations — enforces C-12 via structural separation: the same role cannot produce and self-validate evidence |
| V-04 | Combined (output format + lifecycle) | C-11, C-12, C-13, C-14 | A unified five-phase protocol integrating vocabulary contract (C-11), cascade-to-termination (C-13), trigger graph adjacency list (C-14), and evidence-citation gates (C-12) addresses all four new criteria without structural tension between phases |
| V-05 | Combined (phrasing register + inertia framing) | C-11, C-12, C-13, C-14 | Naming four new failure modes — Vocabulary Gap (C-11), Verdict Orphaning (C-12), Cascade Truncation (C-13), Prose-Only Cycle Reasoning (C-14) — and enforcing each with SHALL language creates a two-layer motivation: engineers understand why each requirement exists, and the normative language makes it non-negotiable |

---

## V-01 — Output Format: Vocabulary Contract with [VOCAB FAIL] Markers

**Variation axis**: Output format
**Hypothesis**: Round 1 V-02 (Structured Paragraph) and V-05 (Branch Amnesia + Latency Blindness) established vocabulary compliance via anti-examples and term sets in the output cells, but violations could still pass without a visible inline marker. V-01 introduces a Vocabulary Contract section that pairs each output field with an explicit prohibited-alternatives column and defines the `[VOCAB FAIL: actual text]` inline marker convention. A reviewer can scan for `[VOCAB FAIL]` occurrences rather than needing to know the vocabulary in advance. The hypothesis is that a visible wrong/right pair at the top — alongside a marking protocol that forces any violation to be flagged rather than silently substituted — drives C-11 more reliably than scattered anti-examples while preserving the full C-01 through C-10 mechanics from Round 1.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. Produce a trigger fire report following the protocol below. Execute all sections in order.

---

#### SECTION 0 — VOCABULARY CONTRACT

This contract governs every constrained output cell in Sections 2–4. Non-conforming values SHALL be marked `[VOCAB FAIL: actual text]` inline — preserve the non-conforming text for review; do not silently substitute the correct term.

| Cell | Permitted Values | Prohibited Alternatives (mark `[VOCAB FAIL: text]`) |
|---|---|---|
| **PA Flow Type** | `Automated – Dataverse` / `Automated – SharePoint` / `Automated – HTTP` / `Instant` / `Scheduled` | `cloud flow`, `automated flow`, `PA flow`, `triggered flow`, `scheduled flow`, `flow type: automated` |
| **Execution Tier** | `Sync` / `Async` | `synchronous`, `asynchronous`, `real-time`, `background`, `deferred`, `immediate` |
| **Latency (Async only)** | `~N min [standard\|premium] tier` (N must be numeric) | `unknown`, `varies`, `near real-time`, `shortly`, `eventually`, `fast` |
| **Input Payload Field Ref** | `{TableName}.{ColumnName}` (e.g., `Request.Status`) | Any reference omitting table name or column name: `"the status field"`, `"the record"`, `"relevant fields"`, `"current value"` |
| **Output Action** | Opens with `Sets` / `Creates` / `Deletes` / `Sends email via` / `Calls HTTP` / `Starts child flow:` / `Posts adaptive card to` + connector + target | `processes`, `notifies`, `updates`, `handles`, `triggers`, `executes`, any lead omitting connector and target |
| **Condition Branch** | Two lines required: `Taken: [branch] — [reason]` AND `Skipped: [branch] — [reason]` | Single-branch declaration; `"condition is checked"`, `"runs when condition is true"` |
| **Storm Verdict** | `CLEARED (count = N, no re-entry)` or `STORM DETECTED (count = N; group: [names]; re-entry: [path])` | Any assertion without explicit firing count |
| **Missing Verdict** | `CLEARED (N: N fired, N confirmed absent, 0 gaps)` or `MISSING TRIGGER: [name — gap cause — risk]` | `"nothing missing"`, any assertion without reconciliation reference |
| **Circular Verdict** | `CLEARED (DAG; edge set: {listed})` or `CIRCULAR TRIGGER: [cycle path]` | `"no circular triggers"`, any assertion without graph edge enumeration |

Wrong-vs-correct reference pairs (the left-hand value is a vocabulary violation):

| Wrong | Right |
|---|---|
| "Updates the status" | `Sets Request.Status to 'Under Review' via Dataverse connector` |
| "Sends a notification" | `Sends email via Office 365 Outlook to Request.AssignedTo with subject 'Action Required'` |
| "Runs if status matches" | `Taken: True branch — Status changed to 'Submitted'; Skipped: False branch — value was not 'Submitted'` |
| "cloud flow" | `Automated – Dataverse` |
| "background process, eventually" | `Async (~5 min standard tier)` |

---

#### SECTION 1 — CHANGE SCOPE AND CANDIDATES

**1-A — Change Scope Pin**

State the change event:
> `{Entity}` — `{Field}` changed from `{old value}` to `{new value}` (context: `{initiating action}`)

This is the analysis boundary. Any trigger that does not respond to this entity + field combination is out of scope and must not appear in Section 2.

**1-B — Candidate Pre-Scan**

Before evaluating any trigger condition, list all triggers that *could* fire based on entity, field, and trigger type alone:

| Candidate ID | Trigger Name | PA Flow Type | Has Condition? |
|---|---|---|---|
| C-01 | | | `Yes` / `No` |

Candidate count: N (analysis denominator — every candidate resolved in Section 3).

---

#### SECTION 2 — FIRING SEQUENCE

List every trigger that actually fires, sync before async. For each trigger in the firing set, complete a full row. All cells are governed by the Section 0 Vocabulary Contract.

| # | C-Ref | Trigger Name | PA Flow Type | Tier / Latency | Condition Branch | Input Payload | Output Action | Side Effects |
|---|---|---|---|---|---|---|---|---|

Column rules:
- **C-Ref**: Candidate ID from Section 1-B. If absent: `[NOT IN CANDIDATES: reason]`.
- **PA Flow Type**: Contract-permitted value. Non-conforming → `[VOCAB FAIL: text]`.
- **Tier / Latency**: `Sync` or `Async (~N min [tier])`. Non-conforming → `[VOCAB FAIL: text]`.
- **Condition Branch**: Both Taken and Skipped lines required for conditional triggers. Unconditional → `No condition`. Single-branch → `[VOCAB FAIL: only taken branch declared]`.
- **Input Payload**: All fields consumed as `{TableName}.{ColumnName}`. Non-conforming → `[VOCAB FAIL: text]`.
- **Output Action**: Contract lead verb + connector + target. Non-conforming → `[VOCAB FAIL: text]`.
- **Side Effects**: `{Entity}.{Field} = {value}` per field written that could trigger another flow. No writes → `None`.

**Cascade rule**: If any Side Effects value matches an untriggered candidate's trigger condition, that candidate becomes the immediately next row before any other independent trigger. Continue until no side effect in the current firing set matches any untriggered candidate — this is the termination condition. Mark each cascade chain's final row `[TERMINAL: no further fires]`.

---

#### SECTION 3 — CANDIDATE RECONCILIATION

Resolve every candidate from Section 1-B:

| Candidate ID | Trigger Name | Resolution | Reason |
|---|---|---|---|

Resolution: `FIRED` / `CONFIRMED ABSENT ([specific condition that excluded it])` / `FLAGGED GAP ([reason expected to fire])`

Totals: N FIRED, N CONFIRMED ABSENT, N FLAGGED GAP

---

#### SECTION 4 — PATHOLOGY ANALYSIS

All three pathology classes required. Absence must be stated explicitly with supporting evidence — do not omit a class.

**Trigger Storm**

- Firing count from Section 2: N (list by name)
- Storm threshold: > 3 executions per change event
- Re-entry check: for each Side Effects value in Section 2, does that field appear in any Section 1-B candidate's trigger condition?
- Evidence: [cite Section 2 rows and Section 1-B candidates checked]
- Verdict (Contract § Storm Verdict): `CLEARED (count = N, no re-entry)` or `STORM DETECTED (count = N; group: [names]; re-entry: [path])`

**Missing Triggers**

- FLAGGED GAP entries from Section 3: [list by candidate ID, or "none"]
- Evidence: [cite Section 3 resolution rows]
- Verdict (Contract § Missing Verdict): `CLEARED (N: N fired, N confirmed absent, 0 gaps)` or `MISSING TRIGGER: [name — gap cause — risk]`

**Circular Triggers**

- Side-effect writes from Section 2: [list by row #]
- Trigger graph edge set: for each write, construct `{Source Trigger} → {Entity.Field} → fires → {Downstream Candidate(s)}`
- Complete edge set: `{listed}`
- Graph property: `DAG` / `CYCLIC`
- Evidence: [cite Section 2 side effects and Section 1-B candidate conditions checked]
- Verdict (Contract § Circular Verdict): `CLEARED (DAG; edge set: {listed})` or `CIRCULAR TRIGGER: [cycle path]`

---

#### SECTION 5 — RISK-RANKED PATHOLOGY SUMMARY

| Rank | Pathology | Risk Level | Operational Impact | Mitigation |
|---|---|---|---|---|

Critical first. If all cleared: `All three pathology classes cleared.`

---

Now receive the scenario and trigger registry, then produce the full report.

---

## V-02 — Lifecycle Emphasis: Cascade-to-Termination Engine

**Variation axis**: Lifecycle emphasis
**Hypothesis**: Round 1 variations addressed C-06 (side effects traced "at least one level deep") but expressed cascade depth as a fixed-depth requirement rather than a termination-driven loop. V-02 restructures the cascade phase into a formal iterative engine: an expanding firing set governed by a loop that continues until no unmatched side-effect writes remain. This makes C-13 (cascade tracing to termination) structurally impossible to fail — the protocol cannot close until the loop terminates. The edge accumulator maintained during the loop also produces the explicit edge set needed for C-14 (trigger graph) as a natural byproduct, without requiring a separate section.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. Execute the protocol below in phase order.

---

#### PHASE 0 — CHANGE SCOPE

State the change event:
> `{Entity}.{Field}` changed from `{old value}` to `{new value}` — context: `{initiating action}`

---

#### PHASE 1 — CANDIDATE REGISTRY

Before evaluating any trigger condition, enumerate every trigger that *could* fire based on entity, field, and trigger type alone. Do not check conditions. Do not determine outcomes.

| Candidate ID | Trigger Name | PA Trigger Type | Entity Filter | Field Filter | Has Condition? |
|---|---|---|---|---|---|
| TRG-01 | | | | | `Yes` / `No` |

**PA Trigger Type permitted values**: `Automated – Dataverse`, `Automated – SharePoint`, `Automated – HTTP`, `Instant`, `Scheduled`. Non-conforming values: mark `[VOCAB FAIL: text]`. Do not write `cloud flow`, `automated flow`, `PA flow`, or any non-list value.

Candidate count: N (denominator — every TRG-NN resolved in Phase 3).

---

#### PHASE 2 — CASCADE FIRING ENGINE

The cascade engine builds the complete trigger execution set through an iterative loop. The loop runs until the firing set is closed under the termination condition.

**Initialization**: Empty firing set. Empty edge accumulator.

**Loop rule** (repeat until termination):

1. Identify all unexecuted candidates whose trigger condition is satisfied by (a) the original change event, or (b) any side-effect field write currently in the edge accumulator.
2. For each newly matched trigger: add it to the firing set and complete its execution row (full entry below).
3. For each side-effect write produced: add to the edge accumulator as `{Writing Trigger} → {Entity.Field}`. Check whether `{Entity.Field}` matches any unexecuted candidate's field filter.
4. **Termination condition**: if step 3 produces no new candidate matches — no side-effect write in the accumulator matches any unexecuted candidate — the firing set is closed. Stop.
5. If new candidates matched in step 3: continue to next iteration (step 1).

**Firing set table** (sync before async within each iteration; append rows as the loop progresses):

| Iter | # | Trigger Name | PA Flow Type | Tier / Latency | Condition Branch | Input Payload | Output Action | Side Effects |
|---|---|---|---|---|---|---|---|---|

Column specifications:
- **PA Flow Type**: `Automated – Dataverse` / `Automated – SharePoint` / `Automated – HTTP` / `Instant` / `Scheduled`. Non-conforming → `[VOCAB FAIL: text]`.
- **Tier / Latency**: `Sync` (blocks transaction) or `Async (~N min [standard|premium] tier)`. N must be numeric. Non-conforming → `[VOCAB FAIL: text]`.
- **Condition Branch**: For conditional triggers — `Taken: [branch] — [reason]; Skipped: [branch] — [reason]`. For unconditional — `No condition`. Single-branch declaration → `[VOCAB FAIL: only taken branch declared]`.
- **Input Payload**: All consumed fields as `{Entity}.{Field}`. Non-conforming reference → `[VOCAB FAIL: text]`.
- **Output Action**: Opens with `Sets` / `Creates` / `Deletes` / `Sends email via` / `Calls HTTP` / `Starts child flow:` / `Posts adaptive card to` + connector + target. Non-conforming → `[VOCAB FAIL: text]`.
- **Side Effects**: `{Entity}.{Field} = {value}` per field write. No writes → `None`.

Mark the final row of each cascade chain `[TERMINAL: no further fires from this write]`.

**Loop termination notice** (required after the final row):
> `Cascade engine closed. Iterations: N. Total fires: N. Termination condition: no side-effect write in the accumulator matches any unexecuted candidate.`

---

#### PHASE 3 — TRIGGER GRAPH AND RECONCILIATION

**3-A — Trigger Graph (from edge accumulator)**

From Phase 2, enumerate the complete directed edge set — one edge per side-effect write:

```
{Writing Trigger} → {Entity.Field} → fires → {Downstream Candidate(s) from Phase 1}
```

If any downstream candidate's field filter is satisfied by a write from a trigger already in the current chain: mark `[CYCLE: {path}]`.

Graph property: `DAG` (no back-edges) / `CYCLIC` (back-edge exists — path: `{cycle}`)

**3-B — Candidate Reconciliation**

Resolve every Phase 1 candidate:

| Candidate ID | Trigger Name | Resolution | Reason |
|---|---|---|---|

Resolution: `FIRED (iter N, row M)` / `CONFIRMED ABSENT ([specific condition])` / `FLAGGED GAP ([reason expected to fire])`

Totals: N FIRED, N CONFIRMED ABSENT, N FLAGGED GAP

---

#### PHASE 4 — PATHOLOGY ANALYSIS

All three pathology classes required. Each verdict must reference specific evidence from Phases 2–3.

**Trigger Storm**

- Firing count: N (Phase 2 total — list by name)
- Re-entry evidence: any `[CYCLE]` marker in Phase 3-A, or total fires > 3
- Verdict: `CLEARED (count = N, no re-entry — Phase 2 engine closed at N iterations, Phase 3-A = DAG)` or `STORM DETECTED (count = N; group: [names]; re-entry: [path] — Phase 3-A CYCLE at [edge])`

**Missing Triggers**

- FLAGGED GAP entries from Phase 3-B: [list by candidate ID, or "none"]
- Verdict: `CLEARED (N: N fired, N confirmed absent, 0 gaps — Phase 3-B reconciliation complete)` or `MISSING TRIGGER: [name — gap cause — risk — Phase 3-B candidate TRG-NN]`

**Circular Triggers**

- Phase 3-A graph property: DAG / CYCLIC
- Edge set: `{from Phase 3-A}`
- Verdict: `CLEARED (DAG confirmed — edge set: {Phase 3-A set})` or `CIRCULAR TRIGGER: [cycle path — Phase 3-A CYCLE marker at edge: {edge}]`

---

#### PHASE 5 — RISK-RANKED PATHOLOGY SUMMARY

| Rank | Pathology | Risk Level | Operational Impact | Mitigation |
|---|---|---|---|---|

Critical first. If all cleared: `No pathologies. Cascade engine terminated cleanly after N iterations; trigger graph = DAG.`

---

Now receive the scenario and trigger registry, then produce the report.

---

## V-03 — Role Sequence: Evidence Gatekeeper (Third Role)

**Variation axis**: Role sequence
**Hypothesis**: Round 1 V-01 (Scanner → Tracer → Inspector) separated branch coverage into a dedicated role and scored 100. V-03 applies the same separation principle to verdict quality. In prior variations, the role that produces the analysis also produces the verdict — there is no structural check that the verdict is grounded in the analysis. V-03 adds a dedicated Evidence Gatekeeper (Role C) whose sole job is to audit each pathology verdict for a traceable evidence chain. The gatekeeper cannot generate new analysis; it can only approve a verdict that cites specific prior-role items or flag a bare assertion as `[INSUFFICIENT: cite section and item]`. This structural separation drives C-12 without requiring the Pathology Analyst to self-check evidence quality.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert operating in three sequential roles. Complete each role fully before starting the next. Do not merge roles or use later-role output while executing an earlier role.

---

#### ROLE A — TRIGGER TRACER

**A-0 — Change Scope Pin**

State the change event:
> `{Entity}` — `{Field}` changed from `{old}` to `{new}` (context: `{initiating action}`)

This scope boundary governs the entire analysis. Triggers that do not respond to this entity + field combination are out of scope.

**A-1 — Candidate Pre-Scan**

Enumerate every trigger that *could* fire based on entity, field, and trigger type alone. Do not evaluate conditions.

| Candidate ID | Trigger Name | PA Flow Type | Has Condition? |
|---|---|---|---|
| A-01 | | | `Yes` / `No` |

**PA Flow Type permitted values**: `Automated – Dataverse`, `Automated – SharePoint`, `Automated – HTTP`, `Instant`, `Scheduled`. Non-conforming → `[VOCAB FAIL: text]`. Do not use: `cloud flow`, `automated flow`, `PA flow`.

Candidate count: N (denominator — governs Role A-3 reconciliation).

**A-2 — Firing Sequence**

List every trigger that actually fires, sync before async:

| # | Candidate Ref | Trigger Name | PA Flow Type | Tier / Latency | Condition Branch | Input Payload | Output Action | Side Effects |
|---|---|---|---|---|---|---|---|---|

Column rules:
- **PA Flow Type**: From A-1 permitted list. Non-conforming → `[VOCAB FAIL: text]`.
- **Tier / Latency**: `Sync` (blocks transaction) or `Async (~N min [standard|premium] tier)`. N numeric.
- **Condition Branch**: If conditional — `Taken: [branch] — [reason]` AND `Skipped: [branch] — [reason]` (both required). If unconditional — `No condition`. Single-branch → `[VOCAB FAIL: only taken branch declared]`.
- **Input Payload**: `{Entity}.{Field}` per field consumed. Non-conforming → `[VOCAB FAIL: text]`.
- **Output Action**: Opens with `Sets` / `Creates` / `Deletes` / `Sends email via` / `Calls HTTP` / `Starts child flow:` / `Posts adaptive card to` + connector + target. Non-conforming → `[VOCAB FAIL: text]`.
- **Side Effects**: `{Entity}.{Field} = {value}` per write. No writes → `None`.

**Cascade rule**: If any Side Effects value matches an untriggered candidate's trigger condition, add that trigger as the immediately next row. Continue until no side effect in the current firing set matches any unexecuted candidate — this is the termination condition. Mark each chain's final row `[TERMINAL]`.

**A-3 — Side-Effect Write Registry**

| Write # | Source Row # | Field Written | Value | Downstream Candidate Match |
|---|---|---|---|---|

**A-4 — Candidate Reconciliation**

| Candidate ID | Trigger Name | Resolution | Reason |
|---|---|---|---|

Resolution: `FIRED (row N)` / `CONFIRMED ABSENT ([specific condition])` / `FLAGGED GAP ([reason])`

Totals: N FIRED, N CONFIRMED ABSENT, N FLAGGED GAP

**A-5 — Trigger Graph Edge Set**

From A-3, construct directed graph edges:

```
{Source Trigger (row #)} → {Entity.Field} → fires → {Downstream Trigger(s)}
```

If any edge would revisit a trigger already on the current chain: mark `[POTENTIAL CYCLE: path]`.

Graph property: `DAG` / `CYCLIC`

---

#### ROLE B — PATHOLOGY ANALYST

Role B produces draft verdicts using only Role A output. Role B does not re-enumerate triggers or re-evaluate conditions. For each verdict, Role B notes the specific Role A section and item it is drawing from. If Role B cannot cite specific Role A evidence, it marks the verdict `[NEEDS EVIDENCE: describe what is missing]` — this signals Role C that the verdict requires investigation before acceptance.

**B-1 — Trigger Storm Draft**

- Firing count: N (from A-2 row count — list by name)
- Storm threshold: > 3 distinct trigger executions
- Re-entry evidence: any `[POTENTIAL CYCLE]` in A-5, or firing count > 3
- Evidence drawn: [cite A-2 rows and A-3 write registry]
- Draft verdict: `CLEARED (count = N, no re-entry — A-2 rows confirmed, A-5 edge set = DAG)` or `STORM DETECTED (group: [names] — A-2 rows N; re-entry from A-5)`

**B-2 — Missing Triggers Draft**

- FLAGGED GAP entries: [from A-4 by candidate ID]
- Evidence drawn: [cite A-4 reconciliation rows]
- Draft verdict: `CLEARED (N: N fired, N confirmed absent, 0 gaps — A-4 reconciliation complete)` or `MISSING TRIGGER: [name — gap cause — risk — A-4 row M]`

**B-3 — Circular Triggers Draft**

- Edge set: [from A-5]
- Graph property from A-5: DAG / CYCLIC
- Evidence drawn: [cite A-5 edge set and A-3 write registry]
- Draft verdict: `CLEARED (DAG confirmed — edge set from A-5: {listed})` or `CIRCULAR TRIGGER: [cycle path from A-5 POTENTIAL CYCLE marker]`

---

#### ROLE C — EVIDENCE GATEKEEPER

Role C audits each Role B draft verdict. For each verdict, Role C performs one check:
- **Approved**: the draft verdict cites specific Role A items (section letter + item number or row number). Mark `[EVIDENCE: CONFIRMED]` and accept the verdict as final.
- **Gated**: the draft verdict contains a bare assertion without a Role A citation, or the citation is imprecise (e.g., "from the analysis" without a specific identifier). Mark `[INSUFFICIENT: state what evidence is needed and where it should be found in Role A]` and note that the verdict is not final until the citation is supplied.

Role C does not rewrite verdicts. Role C does not generate new analysis. Role C's output is an audit record.

**C-1 — Storm Verdict Gate**

Role B draft: [copy B-1 draft verdict verbatim]

Evidence audit:
- Citation present: `Yes (Role A A-2 row count confirmed; A-5 graph property stated)` / `No (bare assertion)`
- Gate result: `[EVIDENCE: CONFIRMED]` or `[INSUFFICIENT: specific citation required — e.g., A-2 rows 1–N listed; A-5 DAG/CYCLIC stated explicitly]`

**Final Storm Verdict**: [approved B-1 text, or flagged as `[GATED: evidence citation required]`]

**C-2 — Missing Triggers Verdict Gate**

Role B draft: [copy B-2 draft verdict verbatim]

Evidence audit:
- Citation present: `Yes (A-4 reconciliation rows cited)` / `No`
- Gate result: `[EVIDENCE: CONFIRMED]` or `[INSUFFICIENT: A-4 reconciliation table rows by candidate ID required]`

**Final Missing Triggers Verdict**: [approved or gated]

**C-3 — Circular Triggers Verdict Gate**

Role B draft: [copy B-3 draft verdict verbatim]

Evidence audit:
- Citation present: `Yes (A-5 edge set enumerated)` / `No`
- Gate result: `[EVIDENCE: CONFIRMED]` or `[INSUFFICIENT: A-5 full edge set enumeration required before DAG/CYCLIC assertion is accepted]`

**Final Circular Triggers Verdict**: [approved or gated]

**C-4 — Risk-Ranked Pathology Summary**

Using only evidence-confirmed verdicts:

| Rank | Pathology | Risk Level | Operational Impact | Mitigation |
|---|---|---|---|---|

Critical first. If all cleared: `All three pathology classes cleared — all verdicts evidence-confirmed by Role C gate.`

---

Now receive the scenario and trigger registry. Execute Role A (complete), then Role B, then Role C.

---

## V-04 — Combined: Output Format + Lifecycle Emphasis

**Variation axis**: Output format + lifecycle emphasis
**Hypothesis**: V-01 established the Vocabulary Contract + `[VOCAB FAIL]` pattern for C-11. V-02 established the cascade-to-termination engine for C-13 and C-14. V-03 established the Evidence Gatekeeper for C-12. V-04 integrates all four into a unified five-phase protocol without separate role sequencing: Vocabulary Contract → Candidates → Cascade Engine (with edge accumulator) → Reconciliation + Trigger Graph → Pathology with Evidence Gates → Summary. The hypothesis is that a single linear protocol (no role-switching overhead) handles all 14 criteria cleanly when the contract, engine, graph, and evidence gate are each given dedicated phases.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. Execute the five phases below in order. Do not advance to a later phase before completing the current one.

---

#### PHASE 0 — VOCABULARY CONTRACT

The vocabulary contract governs all constrained output cells throughout this protocol. Non-conforming values SHALL be marked `[VOCAB FAIL: actual text]` inline — preserve the non-conforming text; do not silently substitute. Wrong-vs-correct pairs define the standard for each field.

| Cell | Permitted Values | Prohibited Alternatives (mark `[VOCAB FAIL: text]`) |
|---|---|---|
| **PA Flow Type** | `Automated – Dataverse` / `Automated – SharePoint` / `Automated – HTTP` / `Instant` / `Scheduled` | `cloud flow`, `automated flow`, `triggered flow`, `scheduled flow`, `PA flow` |
| **Execution Tier** | `Sync` / `Async` | `synchronous`, `asynchronous`, `real-time`, `background`, `deferred`, `immediate` |
| **Latency (Async)** | `~N min [standard\|premium] tier` (N numeric) | `unknown`, `varies`, `near real-time`, `shortly`, `eventually` |
| **Input Payload** | `{TableName}.{ColumnName}` (e.g., `Request.Status`) | `"the status field"`, `"the record"`, `"current value"`, any reference without table+column |
| **Output Action** | `Sets` / `Creates` / `Deletes` / `Sends email via` / `Calls HTTP` / `Starts child flow:` / `Posts adaptive card to` + connector + target | `processes`, `notifies`, `updates`, `handles`, `triggers`, `executes` |
| **Condition Branch** | `Taken: [branch] — [reason]` AND `Skipped: [branch] — [reason]` (both lines) | Single-branch declaration; `"condition is checked"` |
| **Storm Verdict** | `CLEARED (count=N, no re-entry)` or `STORM DETECTED (count=N; group: [names]; re-entry: [path])` | Any count-free assertion |
| **Missing Verdict** | `CLEARED (N: N fired, N absent, 0 gaps)` or `MISSING TRIGGER: [name — cause — risk]` | Any assertion without reconciliation reference |
| **Circular Verdict** | `CLEARED (DAG; edge set: {listed})` or `CIRCULAR TRIGGER: [cycle path]` | Any assertion without edge enumeration |

Wrong-vs-correct reference pairs:

| Wrong | Right |
|---|---|
| "Updates the status" | `Sets Request.Status to 'Under Review' via Dataverse connector` |
| "Notifies the assignee" | `Sends email via Office 365 Outlook to Request.AssignedTo with subject 'Action Required'` |
| "Runs if approved" | `Taken: True branch — Status = 'Approved'; Skipped: False branch — Status not 'Approved'` |
| "cloud flow" | `Automated – Dataverse` |

---

#### PHASE 1 — CHANGE SCOPE AND CANDIDATES

**Scope pin**: `{Entity}.{Field}` changed from `{old}` to `{new}` — context: `{initiating action}`

**Candidate table** (entity + field + type match only — do not evaluate conditions):

| Candidate ID | Trigger Name | PA Flow Type | Field Filter | Has Condition? |
|---|---|---|---|---|
| R-01 | | Phase 0 Contract | | `Yes` / `No` |

Denominator: N candidates. Every R-NN must be resolved in Phase 3.

---

#### PHASE 2 — CASCADE FIRING ENGINE

Build the complete firing set through an iterative loop. Maintain an edge accumulator for Phase 3.

**Initialization**: Empty firing set. Empty edge accumulator.

**Loop rule** (repeat until termination):
1. Identify all unexecuted candidates whose trigger condition is satisfied by the change event or any write in the edge accumulator.
2. For each newly matched trigger: complete one execution row below.
3. Add each side-effect write to the edge accumulator.
4. **Termination check**: does any write in the accumulator match an unexecuted candidate's field filter?
5. If yes: next iteration. If no: **termination condition met** — firing set is closed.

Mark the final row of each cascade chain `[TERMINAL: no further fires]`.

**Firing set — Sync (blocks transaction):**

| Iter | # | R-Ref | Trigger Name | PA Flow Type | Tier | Condition Branch | Input Payload | Output Action | Side Effects |
|---|---|---|---|---|---|---|---|---|---|

**Firing set — Async (fire-and-forget):**

| Iter | # | R-Ref | Trigger Name | PA Flow Type | Latency | Condition Branch | Input Payload | Output Action | Side Effects |
|---|---|---|---|---|---|---|---|---|---|

All cells governed by Phase 0 Contract. R-Ref must reference Phase 1 candidate ID; mark `[NOT IN CANDIDATES]` if absent.

**Loop termination notice** (required after the final row):
> `Cascade engine closed. Iterations: N. Total fires: N sync + N async = N. Termination: no unmatched side-effect writes in edge accumulator.`

---

#### PHASE 3 — RECONCILIATION AND TRIGGER GRAPH

**3-A — Candidate Reconciliation**

| Candidate ID | Trigger Name | Resolution | Evidence Ref |
|---|---|---|---|

Resolution: `FIRED (iter N, row M)` / `CONFIRMED ABSENT ([condition])` / `FLAGGED GAP ([reason])`

Totals: N FIRED, N CONFIRMED ABSENT, N FLAGGED GAP

**3-B — Trigger Graph Adjacency List**

Construct directed edges from the Phase 2 edge accumulator:

```
{Source Trigger (row #)} → {Entity.Field} → fires → {Downstream Candidate(s) from Phase 1}
```

List every edge. Back-edge detection: if any downstream trigger is an ancestor in the current chain, mark `[CYCLE: {path}]`.

Graph property: `DAG` (no back-edges) / `CYCLIC` (back-edge — path: `{cycle}`)

---

#### PHASE 4 — PATHOLOGY ANALYSIS WITH EVIDENCE GATES

All three pathology classes required. Each verdict must cite specific evidence from Phases 2–3 by phase number and row/candidate identifier. A verdict without a citation is marked `[INSUFFICIENT: cite Phase N item M]` — the verdict is not accepted as final until the citation is present.

**Trigger Storm**

- Count: N (Phase 2 total fires — list by name)
- Storm threshold: > 3 executions; re-entry: any `[CYCLE]` in Phase 3-B or count > 3
- Evidence citation: `[Phase 2 firing set: N rows across N iterations; Phase 3-B graph property stated]`
- Verdict (Phase 0 Contract): `CLEARED (count=N, no re-entry — Phase 2 N rows, Phase 3-B DAG confirmed)` or `STORM DETECTED (count=N; group: [names]; re-entry: [path] — Phase 3-B CYCLE at [edge])`

**Missing Triggers**

- FLAGGED GAP entries: [Phase 3-A by candidate ID, or "none"]
- Evidence citation: `[Phase 3-A reconciliation rows for each FLAGGED GAP by candidate ID]`
- Verdict (Phase 0 Contract): `CLEARED (N: N fired, N absent, 0 gaps — Phase 3-A N candidates reconciled)` or `MISSING TRIGGER: [name — cause — risk — Phase 3-A candidate R-NN]`

**Circular Triggers**

- Phase 3-B graph property: DAG / CYCLIC
- Evidence citation: `[Phase 3-B adjacency list; back-edge trace if CYCLIC]`
- Verdict (Phase 0 Contract): `CLEARED (DAG — edge set: {Phase 3-B set})` or `CIRCULAR TRIGGER: [cycle path — Phase 3-B CYCLE at edge: {edge}]`

---

#### PHASE 5 — RISK-RANKED PATHOLOGY SUMMARY

| Rank | Pathology | Risk Level | Operational Impact | Mitigation |
|---|---|---|---|---|

Critical first. If all cleared: `No pathologies. Cascade engine closed after N iterations; trigger graph = DAG; all verdicts evidence-cited.`

---

Now receive the scenario and trigger registry, then execute all five phases.

---

## V-05 — Combined: Phrasing Register + Inertia Framing (Nine Failure Modes)

**Variation axis**: Phrasing register (SHALL/MUST normative) + inertia framing (nine named failure modes)
**Hypothesis**: Round 1 V-05 named five failure modes (Undeclared Denominator, Closed-Set Pathology Scan, Vocabulary Drift, Branch Amnesia, Latency Blindness) and scored 100 by pairing each named failure with normative language and an inline marker convention. V-05 extends the catalog with four new failure modes that map to the v2 aspirational criteria: **Vocabulary Gap** (C-11 — permitted values listed but prohibited alternatives absent, no inline violation marker), **Verdict Orphaning** (C-12 — assertions without evidence chains), **Cascade Truncation** (C-13 — fixed-depth stopping rule instead of termination condition), and **Prose-Only Cycle Reasoning** (C-14 — circular analysis by narrative without an explicit edge set). Each failure mode is named and paired with a SHALL-governed protocol response, creating a two-layer motivation: engineers understand *why* the requirement exists, and the normative language makes it non-negotiable.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert conducting a trigger fire analysis.

---

#### NINE FAILURE MODES OF INFORMAL TRIGGER ANALYSIS

Before the protocol, note the nine failure modes that informal trigger analysis cannot prevent. Each is addressed by a specific section below.

**FM-1 — Undeclared Denominator**
Enumeration starts by listing what fires. Triggers never considered leave silence, not a visible gap. Reviewers cannot distinguish "considered and excluded" from "never considered." Consequence: missed triggers (C-01 violations) are structurally undetectable.
*Protocol response: candidate pre-scan (Section 1) runs before any outcome determination.*

**FM-2 — Closed-Set Pathology Scan**
Pathology runs after the firing set locks in, with no obligation to compare against a declared denominator. Consequence: missed pathology classes (C-04) and false positives (C-05) go unnoticed.
*Protocol response: Section 3 denominator reconciliation is the evidence base for all pathology verdicts.*

**FM-3 — Vocabulary Drift**
Descriptions like "sends a notification" or "updates the record" pass informal review. Only a reviewer who already knows the correct vocabulary can catch violations. Consequence: C-08 violations pass unreported.
*Protocol response: vocabulary contract defined at Section 0; non-conforming values marked `[VOCAB FAIL: text]`.*

**FM-4 — Branch Amnesia**
Conditional triggers get their "runs when true" path documented; the "skipped when false" path is omitted. The skipped branch may reveal automation gaps or false confidence. Consequence: C-07 violations go unnoticed.
*Protocol response: every conditional trigger SHALL declare both branches with reasons.*

**FM-5 — Latency Blindness**
Sync and async triggers are mixed without tier labels. Async latency is omitted. Consequence: integration design errors when stakeholders assume automations are blocking when they are fire-and-forget (C-10 violations).
*Protocol response: every trigger SHALL declare tier; async triggers SHALL include numeric latency.*

**FM-6 — Vocabulary Gap**
Term sets list permitted values but not prohibited alternatives. Without a prohibited list, a reviewer cannot detect violations without already knowing the wrong value. No inline marker convention exists to surface violations at review time. Consequence: C-11 cannot be structurally enforced — violations depend entirely on reviewer prior knowledge.
*Protocol response: the vocabulary contract SHALL include a prohibited-alternatives column for every field AND SHALL define the `[VOCAB FAIL: actual text]` inline marker convention.*

**FM-7 — Verdict Orphaning**
Pathology verdicts assert a conclusion without citing the evidence from the firing sequence or candidate reconciliation. The verdict floats disconnected from the analysis that produced it. Consequence: C-12 violations — a false "CLEARED" verdict cannot be challenged without re-running the full analysis.
*Protocol response: every pathology verdict SHALL cite specific Section 2/3 items by section and identifier. Bare assertions SHALL be marked `[INSUFFICIENT: cite section and item]`.*

**FM-8 — Cascade Truncation**
Side-effect cascade instructions specify "at least one level deep" or "trace one hop." Analysis stops at a fixed depth. A storm or cycle visible only at depth 3 is never discovered. Consequence: C-13 violations — incomplete cascade coverage is structurally guaranteed by the stopping rule.
*Protocol response: the cascade engine SHALL continue tracing until no side-effect write in the current firing set matches any unexecuted candidate — this termination condition is the only valid stopping rule.*

**FM-9 — Prose-Only Cycle Reasoning**
Circular trigger analysis is conducted by narrative inspection: "I don't see a cycle here." Without an explicit edge set, cycles spanning multiple intermediate triggers are invisible. Consequence: C-14 violations — cycle detection is dependent on the analyst's mental model rather than on a verifiable graph structure.
*Protocol response: circular analysis SHALL construct a directed edge set `{Trigger} → {Entity.Field} → {Downstream Trigger}` and SHALL state the graph property (DAG/CYCLIC) from the set, not from prose inspection.*

---

#### SECTION 0 — VOCABULARY CONTRACT (addresses FM-3, FM-6)

The analyst SHALL define and follow this vocabulary contract throughout all output cells. Non-conforming values SHALL be marked `[VOCAB FAIL: actual text]` — the non-conforming text is preserved for review, not silently corrected.

**Term Set A — PA Flow Type**

| Code | Permitted Term | Prohibited Alternatives (these SHALL trigger `[VOCAB FAIL]`) |
|---|---|---|
| A-01 | `Automated – Dataverse` | `cloud flow`, `automated cloud flow on Dataverse`, `Dataverse trigger`, `when a row is added` |
| A-02 | `Automated – SharePoint` | `SharePoint trigger`, `when a file is created` |
| A-03 | `Automated – HTTP` | `webhook trigger`, `HTTP trigger` |
| A-04 | `Instant` | `manual flow`, `button flow`, `instant cloud flow` |
| A-05 | `Scheduled` | `recurrence trigger`, `scheduled cloud flow`, `timer flow` |

The analyst SHALL NOT write any Term Set A prohibited alternative. A non-conforming cell SHALL be marked `[VOCAB FAIL: actual text]`.

**Term Set B — Execution Tier and Latency**

| Code | Permitted Term | Timing Cell Value | Prohibited Alternatives |
|---|---|---|---|
| B-01 | `Sync` | `Inline (blocks transaction)` | `synchronous`, `real-time`, `immediate`, `blocking`, `in-transaction` |
| B-02 | `Async` | `~N min [standard\|premium] tier` (N numeric) | `asynchronous`, `background`, `deferred`, `unknown`, `eventually`, `near real-time` |

For Async triggers, `~N min` SHALL contain a numeric estimate. The analyst SHALL NOT write "unknown" or leave the latency estimate blank.

**Term Set C — Input Payload Field Reference**

Pattern: `{TableName}.{ColumnName}` (example: `Request.Status`).
Prohibited: any reference that omits the table name (`"the status field"`) or the column name (`"the Request record"`, `"the entity"`). Non-conforming → `[VOCAB FAIL: text]`.

**Term Set D — Output Action Lead Verbs**

| Permitted Lead | Example |
|---|---|
| `Sets` | `Sets Request.Status to 'Approved' via Dataverse connector` |
| `Creates` | `Creates a new Task record via Dataverse connector` |
| `Deletes` | `Deletes the draft record via Dataverse connector` |
| `Sends email via` | `Sends email via Office 365 Outlook to Request.Owner` |
| `Calls HTTP` | `Calls HTTP POST to api.example.com/notify` |
| `Starts child flow:` | `Starts child flow: Approval-Escalation-Flow` |
| `Posts adaptive card to` | `Posts adaptive card to Teams channel #approvals` |

Prohibited: `processes`, `notifies`, `updates`, `handles`, `triggers`, `executes`. Non-conforming → `[VOCAB FAIL: text]`.

**Term Set E — Condition Branch Declaration** (addresses FM-4)

For every conditional trigger, the Condition Branch cell SHALL contain both:
```
Taken: [branch name] — [reason this change satisfies it]
Skipped: [branch name] — [reason this change does not satisfy it]
```
Stating only the taken branch is non-conforming: `[VOCAB FAIL: only taken branch declared]`. The analyst SHALL NOT write only the branch that executes.

---

#### SECTION 1 — CANDIDATE PRE-SCAN (addresses FM-1)

The analyst SHALL enumerate ALL trigger candidates before any outcome determination. A trigger is a candidate if and only if its trigger type, entity filter, and field filter could match the change event under standard Power Automate evaluation rules.

The analyst SHALL NOT evaluate conditions. The analyst SHALL NOT determine which triggers fire.

| Candidate ID | Trigger Name | PA Flow Type (Term Set A) | Entity Filter | Field Filter | Has Condition? |
|---|---|---|---|---|---|
| C-01 | | | | | `Yes` / `No` |

**Denominator count**: N. Every C-NN candidate SHALL be resolved in Section 3. An unresolved candidate is a structural gap indicating a declared denominator with a silently dropped entry.

---

#### SECTION 2 — CASCADE FIRING ENGINE (addresses FM-3, FM-4, FM-5, FM-8)

The analyst SHALL build the complete firing set through an iterative cascade loop.

**Termination condition** (FM-8 response): the loop continues until no side-effect write in the current firing set matches the trigger condition of any unexecuted candidate. A fixed depth is not a valid stopping rule. The analyst SHALL NOT stop the cascade because "one level has been traced" — the loop runs until the set is closed.

**Sync tier (B-01 — Term Set B, Inline):**

| # | C-Ref | Trigger Name | Flow Type (A) | Tier | Condition Branch (E) | Input Payload (C) | Output Action (D) | Side Effects |
|---|---|---|---|---|---|---|---|---|

**Async tier (B-02 — Term Set B, ~N min):**

| # | C-Ref | Trigger Name | Flow Type (A) | Latency | Condition Branch (E) | Input Payload (C) | Output Action (D) | Side Effects |
|---|---|---|---|---|---|---|---|---|

Column rules:
- **C-Ref**: Section 1 candidate ID. Mark `[NOT IN DENOMINATOR: reason]` if absent.
- **Flow Type (A)**: Term Set A. Non-conforming → `[VOCAB FAIL: text]`.
- **Tier / Latency**: Term Set B. Non-conforming → `[VOCAB FAIL: text]`.
- **Condition Branch (E)**: Term Set E. Single-branch declaration → `[VOCAB FAIL: only taken branch declared]`.
- **Input Payload (C)**: Term Set C. Non-conforming → `[VOCAB FAIL: text]`.
- **Output Action (D)**: Term Set D lead verb required. Non-conforming → `[VOCAB FAIL: text]`.
- **Side Effects**: `{Entity}.{Field} = {value}` per write. No writes → `None`.

**Cascade rule**: If any Side Effects value matches an unexecuted candidate's field filter, that candidate SHALL appear as the immediately next row in the appropriate tier table. The analyst SHALL trace the cascade until the termination condition is met. Each cascade chain's final row SHALL be marked `[TERMINAL: no further fires]`.

**Loop termination notice** (required immediately after the final firing row):
> `Cascade engine closed after N iterations. Final count: N sync + N async = N total. Termination: no unmatched side-effect writes remain.`

---

#### SECTION 3 — DENOMINATOR RECONCILIATION (addresses FM-2)

Every Section 1 candidate SHALL appear in this table. An unresolved candidate is a structural gap.

| Candidate ID | Trigger Name | Resolution | Reason |
|---|---|---|---|

Resolution codes: `FIRED (sync row M)` / `FIRED (async row M)` / `CONFIRMED ABSENT ([specific condition])` / `FLAGGED GAP ([reason expected])`

Totals: N FIRED, N CONFIRMED ABSENT, N FLAGGED GAP

---

#### SECTION 4 — TRIGGER GRAPH AND PATHOLOGY (addresses FM-7, FM-9)

**4-A — Trigger Graph Edge Set (FM-9 response)**

The analyst SHALL construct a directed edge set from Section 2 side-effect writes. The graph property SHALL be stated from the edge set, not from prose inspection.

```
{Source Trigger (row #)} → {Entity.Field} → fires → {Downstream Candidate(s) from Section 1}
```

Full edge set:
```
[list all edges here; if no side-effect writes, state "Empty — no side-effect field writes in Section 2"]
```

Back-edge detection: if any path revisits a trigger already in the current chain, the analyst SHALL mark `[CYCLE: {full path}]`.

Graph property: `DAG` (no back-edges found in full edge set) / `CYCLIC` (back-edge exists — path: `{cycle}`)

**4-B — Pathology Analysis (FM-7 response)**

All three pathology classes SHALL be addressed. Each verdict SHALL cite specific evidence from Sections 2–3 by section letter and row/candidate identifier. A bare assertion without a citation SHALL be marked `[INSUFFICIENT: cite Section N row/candidate M]`.

**Trigger Storm**

- Firing count: N (Section 2 total rows — list by trigger name)
- Storm threshold: > 3 distinct trigger executions or any re-entry path
- Re-entry evidence: `[CYCLE]` marker in Section 4-A, or count > 3
- Evidence citation: `[Section 2: N rows across N iterations; Section 4-A graph property = DAG/CYCLIC]`
- Verdict: `CLEARED (count=N, threshold not reached, no re-entry — Section 2 N rows; Section 4-A = DAG)` or `STORM DETECTED (count=N; group: [names]; re-entry: [path] — Section 4-A CYCLE at [edge])`

**Missing Triggers**

- FLAGGED GAP entries: [Section 3 by candidate ID, or "none"]
- Evidence citation: `[Section 3 FLAGGED GAP rows by candidate ID: C-NN, ...]`
- Verdict: `CLEARED (N: N fired, N absent, 0 gaps — Section 3 reconciliation complete: all C-NN resolved)` or `MISSING TRIGGER: [name — gap cause — risk — Section 3 candidate C-NN]`

**Circular Triggers**

- Section 4-A graph property: `DAG` / `CYCLIC`
- Evidence citation: `[Section 4-A full edge set: {listed}]`
- Verdict: `CLEARED (DAG confirmed — full edge set: {Section 4-A})` or `CIRCULAR TRIGGER: [cycle path — Section 4-A CYCLE marker at edge: {edge}]`

---

#### SECTION 5 — RISK-RANKED PATHOLOGY SUMMARY

| Rank | Pathology | Risk Level | Operational Impact | Mitigation |
|---|---|---|---|---|

Critical first. If all cleared: `No pathologies confirmed — nine failure modes addressed; cascade engine terminated cleanly; trigger graph = DAG; all verdicts evidence-cited.`

---

Now receive the scenario and trigger registry, then execute all five sections.
