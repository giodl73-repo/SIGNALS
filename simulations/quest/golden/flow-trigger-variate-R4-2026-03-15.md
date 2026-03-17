# Flow-Trigger Skill — Round 4 Variations (Rubric v4)

**Skill**: flow-trigger — Simulate which automations fire when a record changes.
**Rubric**: v4 (C-01 through C-22)
**Date**: 2026-03-15

---

## Variation Design Notes

### Pre-read of R3 Scorecard Evidence (Against Rubric v3, C-01 Through C-19)

From the rubric v4 version notes, three patterns surface from Round 3 output:

| Pattern | Where Observed in R3 | R3 Mechanism | R4 Gap |
|---------|---------------------|--------------|--------|
| Terminal-absence companion marker (C-20) | All three R3 variations | `[CHAIN OPEN: CH-NN — no terminal row produced; trace may be incomplete]` in Role C | R3 embedded the companion marker in a prose note. C-20 requires it to be a *named protocol-level marker* that fires when `[TERMINAL]` is absent — positively flagged, distinct from `[TERMINAL]` itself |
| Protocol-indexed failure mode catalog (C-21) | R3 V-03 (FM-01 through FM-14) | FM codes in protocol section headers as "addresses FM-NN" | FM codes must also cross-reference in output cells where violations occur. R3 had FM codes in instructions only; C-21 requires violations to be diagnosable by code from the output cell itself |
| Denominator-governed reconciliation section (C-22) | R3 V-01 (Role D-1), V-02 (Section 3) | Reconciliation embedded inside the Gatekeeper role (D-1) or inside Section 3 trigger notes | C-22 requires the reconciliation section to be *structurally independent* from both trigger analysis tables and verdict gating — reviewable without re-reading either |

### What Rubric v4 Adds (C-20 Through C-22)

| ID | Criterion | Pattern Source in R3 | R4 Design Obligation |
|----|-----------|---------------------|----------------------|
| C-20 | Terminal-absence companion marker | R3 used `[CHAIN OPEN: CH-NN]` as a prose note | Define `[CHAIN OPEN: CH-NN]` as a protocol-level marker: it occupies the same structural position `[TERMINAL]` would, fires positively when `[TERMINAL]` is absent |
| C-21 | Protocol-indexed failure mode catalog | R3 V-03 FM-01--FM-14 defined in preamble, referenced in section headers | Extend catalog to FM-17. Add cross-reference output rule: every violation in an output cell SHALL carry the FM code of the violated requirement |
| C-22 | Denominator-governed reconciliation section | R3 D-1 (inside gatekeeper role), Section 3 (inside cascade analysis) | Physical separation: own heading, own input contracts, own output table. Reviewable without reading any surrounding section |

### R4 Variation Map

All R3 100-scorers achieved C-01--C-19. The R4 challenge is adding C-20--C-22 without regressing those.

| Variation | Axes | New Criteria Targeted | Hypothesis |
|-----------|------|-----------------------|------------|
| V-01 | Role sequence | C-20, C-21, C-22 | A fifth role (Reconciliation Auditor) separates C-22 from the Gatekeeper's verdict tables. Role C's `Chain Status` column makes `[TERMINAL]` vs `[CHAIN OPEN: CH-NN]` a structural column value rather than a prose note (C-20). FM catalog extended to FM-17 with output cross-reference rule (C-21) |
| V-02 | Output format | C-20, C-22 | Pre-allocating a `Chain Status` column in every cascade sub-table makes terminal/open state a visible structural cell (C-20). Section 5 "Denominator Reconciliation" is separated by triple-rule boundaries and carries explicit independence instructions (C-22) |
| V-03 | Protocol-indexed failure mode catalog | C-20, C-21, C-22 | Extends FM catalog to FM-17: FM-15 (Chain-Open Blindness), FM-16 (Catalog Opacity), FM-17 (Reconciliation Capture). Primary axis is C-21: every output violation cell carries an FM code making diagnosis possible from the cell alone |
| V-04 | Role sequence + output format | C-20, C-21, C-22 | Five-role pipeline (V-01) + companion-column format (V-02) + FM output-cell cross-reference (V-03). Tests whether the three independent mechanisms compose cleanly in a single protocol |
| V-05 | Lifecycle emphasis + phrasing register | C-20, C-21, C-22 | Six explicit lifecycle phases (SETUP -> SCAN -> FIRE -> CLOSE -> RECONCILE -> GATE) with formal gate conditions between phases. RECONCILE is a distinct lifecycle phase with its own input contracts (C-22). `[CHAIN OPEN: CH-NN]` is a gate-blocking signal between CLOSE and RECONCILE (C-20). FM catalog in preamble with output cross-reference (C-21) |

**Foundation carried forward** (no rediscovery needed from R3):
- Vocabulary contract + `[NC: value]` inline markers (C-11)
- `[INSUFFICIENT]` / `[EVIDENCE: CONFIRMED -- {citation}]` verdict gates (C-12)
- Cascade termination condition instruction -- not fixed depth (C-13)
- Directed edge set for circular detection (C-14)
- Candidate denominator pre-scan -- conditions not evaluated during scan (C-15)
- `[TERMINAL]` per-chain row marker (C-16)
- Role-separated evidence gating -- gating role cannot write analysis (C-17)
- Sync/async structural table split (C-18)
- DFS back-edge detection with `in-path` set (C-19)

---

## V-01 -- Role Sequence: Five-Role Pipeline (Scanner -> Tracer -> Cascade Closer -> Gatekeeper -> Reconciliation Auditor)

**Variation axis**: Role sequence
**Hypothesis**: R3 V-01 used a four-role pipeline where Role D (Gatekeeper) owned both verdict gating and candidate reconciliation (D-1). D-1 was embedded inside the gating role, giving D a dual mandate that violated C-22's structural independence requirement. R4 V-01 extracts reconciliation into a dedicated fifth role -- Role E (Reconciliation Auditor) -- whose sole output is the independent reconciliation table. Role D retains verdict gating only and cannot produce reconciliation content. Role C picks up `[CHAIN OPEN: CH-NN]` as a column value (C-20). FM-15 through FM-17 extend the catalog in the preamble; a cross-reference output rule drives C-21.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert operating in five sequential roles. Complete each role in full before beginning the next. Do not merge roles. Do not carry work from a later role into an earlier one.

---

#### FAILURE MODE CATALOG (FM-01 through FM-17)

The seventeen failure modes below define what informal trigger analysis cannot prevent. Each maps to a protocol section.

**Output Cross-Reference Rule**: When an output cell contains a violation, the cell SHALL carry the FM code of the violated requirement: `[marker | FM-NN]`. Reviewers diagnose violations from the output cell alone -- they do not re-read the preamble to identify the violated requirement.

**FM-01 -- Undeclared Denominator**: Enumeration begins from the firing set; silent omissions leave no gap. *Response*: Role A pre-scan declares N before condition evaluation.

**FM-02 -- Closed-Set Pathology Scan**: Pathology verdict lacks a denominator to compare against. *Response*: Role E reconciliation produces the evidence base for all three pathology verdicts.

**FM-03 -- Vocabulary Drift**: Informal terms pass review. *Response*: Vocabulary contract in Role A; `[NC: value | FM-03]` in violating cells.

**FM-04 -- Branch Amnesia**: Skipped branch silently omitted. *Response*: Both branches required; missing skipped: `[NC: only taken branch | FM-04]`.

**FM-05 -- Latency Blindness**: Tier/latency omitted. *Response*: Tier and latency required; missing: `[NC: latency missing | FM-05]`.

**FM-06 -- Vocabulary Gap Without Enforcement**: Rules stated but no inline marker. *Response*: `[NC: value | FM-03]` in the violating cell.

**FM-07 -- Verdict Orphaning**: Verdicts lack evidence citations. *Response*: `[INSUFFICIENT: cite section + item | FM-07]` on bare assertions.

**FM-08 -- Cascade Truncation**: Chain ends at a fixed depth. *Response*: Trace until termination condition -- not a fixed depth; truncation: `[TRUNCATED | FM-08]`.

**FM-09 -- Prose-Only Cycle Reasoning**: Visual inspection misses length-3+ cycles. *Response*: DFS with `in-path` set; back-edge: `[BACK-EDGE: path | FM-09]`.

**FM-10 -- Denominator Shrinkage**: Conditions evaluated during pre-scan reduce the candidate count. *Response*: Pre-scan by entity/field/type only; violation: `[NC: condition evaluated during pre-scan | FM-10]`.

**FM-11 -- Orphaned Chains**: Cascade chains closed without a terminal marker. *Response*: `[TERMINAL]` required on terminal row; see FM-15 for the complement.

**FM-12 -- Verdict Capture**: Analyst gates own assertions; gate is advisory. *Response*: Role D cannot generate analysis -- only approve/flag. Violation: `[FM-12: self-gating; separate evidence role required]`.

**FM-13 -- Tier Blur**: Sync and async in a shared table. *Response*: Separate structural tables; violation: `[NC: wrong-tier trigger in table | FM-13]`.

**FM-14 -- Visual Cycle Inference**: Back-edge detection by eye. *Response*: DFS traversal steps required; skipped: `[FM-14: DFS steps not shown]`.

**FM-15 -- Chain-Open Blindness** *(C-20)*: A chain without `[TERMINAL]` is detectable only by absence. *Response*: Final row of an unterminated chain SHALL carry `[CHAIN OPEN: CH-NN | FM-15]` -- where CH-NN is the chain identifier from Role B. Non-termination is positively flagged, never inferred from absence.

**FM-16 -- Catalog Opacity** *(C-21)*: FM codes in preamble only; violations in output cells described in prose; diagnosis requires cross-section reading. *Response*: All output violation cells SHALL carry the FM code inline. Format: `[marker | FM-NN]`. Blank FM slot in a violation cell: structural violation.

**FM-17 -- Reconciliation Capture** *(C-22)*: Candidate reconciliation embedded inside the gating role or trigger analysis sections. *Response*: Role E is structurally separate; it cannot gate verdicts (Role D) and cannot be a sub-section of any other role's output. Embedding: `[FM-17: reconciliation must be independent section]`.

---

#### ROLE A -- SCANNER

**Task**: Establish the analysis boundary and declare the candidate denominator. Do not evaluate conditions.

**A-0 -- Change Scope Pin**

> `{Entity} -- {Field} changed from {old value} to {new value} | context: {initiating action}`

This line is the analysis boundary. Any trigger whose entity, field, or trigger type does not match is out of scope.

**A-1 -- Vocabulary Contract**

All Role B output cells are bound to the following terms. Non-conforming: `[NC: actual_value | FM-03]`.

| Column | Permitted Values |
|---|---|
| **PA Flow Type** | `Automated -- Dataverse` \| `Automated -- SharePoint` \| `Automated -- HTTP` \| `Instant` \| `Scheduled` |
| **Tier** | `Sync` \| `Async` |
| **Latency** | Sync: `Inline (blocks transaction)` \| Async: `~N min [standard\|premium] tier` (N required) |
| **Condition Branch** | `Taken: [branch name] -- [reason]` AND `Skipped: [branch name] -- [reason]` (both required for conditional) \| `No condition` |
| **Input Payload** | `{Entity}.{Field}` pattern |
| **Output Action** | Leads with: `Sets` \| `Creates` \| `Deletes` \| `Sends email via` \| `Calls HTTP` \| `Starts child flow:` \| `Posts adaptive card to` |
| **Side-Effect Writes** | `{Entity}.{Field} = {value}` or `None` |
| **Chain Status** | `[TERMINAL]` \| `[CHAIN OPEN: CH-NN \| FM-15]` \| `--` (non-terminal rows) |

**A-2 -- Candidate Pre-Scan** (FM-10 guard: entity/field/type match only -- conditions not evaluated)

| CA-ID | Trigger Name | PA Flow Type | Tier | Matching Basis |
|---|---|---|---|---|
| CA-01 | | | | |

**Denominator Count: N** -- Pre-condition population. Every CA-NN must appear in Role E with a disposition. Unresolved entries are structural gaps (`[FM-17]`).

---

#### ROLE B -- TRACER

**Task**: Produce the sync and async firing tables. Assign Chain IDs to side-effect writes that could extend into cascades. Do not walk cascade chains -- that is Role C's function.

**B-1 -- Sync Firing Table**

Async triggers in this table: `[NC: async trigger in sync table | FM-13]`.

| Seq | CA-Ref | Trigger Name | PA Flow Type | Condition Branch | Input Payload | Output Action | Side-Effect Writes | Latency | Chain ID |
|---|---|---|---|---|---|---|---|---|---|

- **CA-Ref**: CA-NN from Role A. Not in pre-scan: `[NOT IN DENOMINATOR | FM-01]`.
- **Condition Branch**: Both branches required for conditional triggers. Missing skipped: `[NC: only taken branch | FM-04]`.
- **Chain ID**: If Side-Effect Writes matches any CA-NN candidate by field: assign CH-01, CH-02, etc. Role C walks this chain. No match: `--`.

Sync total: N | Chain IDs assigned: (list)

**B-2 -- Async Firing Table**

Sync triggers in this table: `[NC: sync trigger in async table | FM-13]`.

Same column structure as B-1.

Async total: N

**B-3 -- Tracer Handoff Summary**

- Grand total fires: Sync N + Async N = N
- Chain IDs: CH-NN -> root trigger -> cascade field
- `[NOT IN DENOMINATOR]` entries: (list or "none")

---

#### ROLE C -- CASCADE CLOSER

**Task**: Walk each CH-NN chain to termination. Populate `Chain Status` column with `[TERMINAL]` or `[CHAIN OPEN: CH-NN | FM-15]`. Build directed edge set. Apply DFS back-edge detection.

**C-1 -- Cascade Chain Walk**

For each CH-NN:

**Chain CH-NN** | Root: `{trigger name}` | Cascade Field: `{Entity.Field}`

| Step | Trigger Name | Fires Because | Reads | Produces | Side-Effect Writes | Chain Status |
|---|---|---|---|---|---|---|

Column rules:
- **Fires Because**: `{Upstream Trigger} wrote {Entity.Field} = {value}`.
- **Chain Status** (two permitted values; blank is structural violation `[NC: chain status missing | FM-11]`):
  - Terminal row (Side-Effect Writes = `None` or no CA-NN responds to written field): `[TERMINAL]`
  - Final row where termination condition is NOT met: `[CHAIN OPEN: CH-NN | FM-15]` -- where CH-NN is this chain's identifier
  - All other rows: `--`

**Termination condition**: A chain terminates when the current step's Side-Effect Writes field matches no CA-NN candidate's trigger condition, or is `None`. A fixed step depth is not a valid stopping rule; fixed-depth stop: `[TRUNCATED | FM-08]`.

**C-2 -- Directed Edge Set**

```
{Trigger A} -> writes {Entity.Field} -> fires {Trigger B}
{Trigger D} -> writes {Entity.Field} -> [NO DOWNSTREAM]
```

Every side-effect write from Roles B and C must appear.

**C-3 -- DFS Back-Edge Detection** (FM-14 guard: do not replace with visual inspection)

```
Initialize: visited = {}  |  in-path = {}
For each trigger T in edge set not yet in visited:
  1. Add T to in-path
  2. For each downstream trigger U that T fires:
     a. If U is in in-path: [BACK-EDGE: T -> ... -> U -> T | FM-09]
     b. If U not in visited: recurse (apply to U)
  3. Remove T from in-path; add T to visited
```

State result only after completing the traversal:
- `Graph property: DAG` -- no back-edges found
- `Graph property: CYCLIC` -- list each `[BACK-EDGE]` path

**C-4 -- Closer Handoff Summary**

- Chains walked: N | With `[TERMINAL]`: N | With `[CHAIN OPEN: CH-NN | FM-15]`: N (list)
- Edge set: (from C-2)
- Graph property: DAG | CYCLIC | Back-edge paths: (list or "none")

---

#### ROLE D -- GATEKEEPER

Role D **cannot generate new analysis**. It cannot write reconciliation content -- that is Role E's function. Doing so: `[FM-17: gatekeeper may not produce reconciliation content]`. Emits only:
- `[EVIDENCE: CONFIRMED -- {specific citation of Role B row or Role C step}]`
- `[INSUFFICIENT: {state what evidence is needed and where} | FM-07]`

**D-1 -- Trigger Storm Gate**

- Grand total from B-3: N | Threshold: > 3 total fires or any `[BACK-EDGE]` in C-4
- Emit: `[EVIDENCE: CONFIRMED -- CLEARED; count = N per B-3; DAG per C-3 traversal; edge set per C-2]` | `[STORM DETECTED -- count = N; path: {C-4}]`
- B-3 total missing: `[INSUFFICIENT: Role B grand total required before storm verdict | FM-07]`

**D-2 -- Missing Triggers Gate**

- FLAGGED GAP entries from Role E (Role E must complete before D-2 can be issued)
- Role E not yet complete: `[INSUFFICIENT: Role E reconciliation required before missing trigger verdict | FM-07]`
- Emit: `[EVIDENCE: CONFIRMED -- CLEARED; N candidates: N fired, N confirmed absent, 0 gaps per Role E]` | `[MISSING TRIGGER: name -- cause -- risk]` per gap

**D-3 -- Circular Triggers Gate**

- Graph property from C-4: DAG | CYCLIC
- DFS not completed: `[INSUFFICIENT: Role C DFS traversal steps required | FM-14]`
- Emit: `[EVIDENCE: CONFIRMED -- CLEARED; DAG per C-3 DFS; edge set: {C-2}]` | `[CIRCULAR TRIGGER: path; Risk = Critical]`

**D-4 -- Risk-Ranked Pathology Summary**

| Rank | Pathology | Risk Level | Operational Impact | Mitigation |
|---|---|---|---|---|

Critical first. All cleared: `No pathologies confirmed -- all three classes gated with evidence citations.`

---

#### ROLE E -- RECONCILIATION AUDITOR

Role E is structurally independent (FM-17 guard). It does not gate verdicts (Role D). It does not generate trigger analysis (Roles B and C). Its sole output is the denominator reconciliation table. Embedding this section inside Role D or any other role's output: `[FM-17: reconciliation must be independent section]`.

**Input contracts** (Role E reads only these):
- From Role A: CA-NN list and count N
- From Role B: CA-Ref values and Seq numbers from B-1 and B-2

**E-1 -- Denominator Reconciliation Table**

For every CA-NN from Role A:

| CA-ID | Trigger Name | Tier | Disposition | Disposition Evidence |
|---|---|---|---|---|

Disposition codes:
- `FIRED -- Sync, Seq #N` -- appeared in Role B-1 at stated sequence number
- `FIRED -- Async, Seq #N` -- appeared in Role B-2 at stated sequence number
- `CONFIRMED ABSENT -- {specific condition or filter that prevented firing}` -- condition evaluated; candidate excluded
- `FLAGGED GAP -- {reason expected to fire but not in Role B}` -- expected to fire; no Role B entry found

Evidence: specific enough to verify without reading Roles B--D (e.g., `B-1 Seq #3` or `condition: Status was Draft; requires Active`). Generic `see Role B`: `[INSUFFICIENT: specific row or condition required | FM-07]`.

**E-2 -- Reconciliation Totals**

- Total candidates (A-2): N
- FIRED: N | CONFIRMED ABSENT: N | FLAGGED GAP: N | Unresolved: N
- Verification: sum SHALL equal N. Mismatch: `[FM-17: N entries unaccounted for]`

**E-3 -- Open Chain Inventory**

- `[CHAIN OPEN: CH-NN | FM-15]` entries from C-4: (list or "none")
- For each: root trigger (CA-ID), cascade field, last step reached
- Cross-reference FLAGGED GAP entries in E-1 where applicable

---

Execute Role A in full, then Role B, then Role C, then Role D, then Role E.

---

## V-02 -- Output Format: Companion-Column Cascade Tables + Independent Reconciliation Section

**Variation axis**: Output format
**Hypothesis**: R3 V-02 used a dual-tree structure where terminal markers appeared as row-level notes and the companion marker was a prose annotation following the sub-table. For C-20, the companion marker needs to be a positively-flagged structural cell, not inferred from absence. V-02 pre-allocates a `Chain Status` column in every cascade sub-table, with exactly two permitted cell values: `[TERMINAL]` or `[CHAIN OPEN: CH-NN]`. A blank cell is a structural violation. For C-22, Section 5 is the "Denominator Reconciliation" section, physically separated from trigger analysis sections by `===` boundary markers and carrying an explicit independence instruction. The dual-tree structure (C-18), DFS detection (C-19), and vocabulary contract (C-11) carry forward from R3 V-02. Evidence gates are inline (not role-separated); this variation does not target C-17.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. Produce a trigger fire analysis using the sectioned structure below. Sections are separated by `===` boundary markers. Each section is self-contained -- no section requires reading another section to interpret its output.

---

#### SECTION 0 -- ANALYSIS SETUP

**0-A Change Scope Pin**

> **Scope**: `{Entity}` -- `{Field}` changed from `{old value}` to `{new value}` (context: `{initiating action}`)

Only triggers whose entity, field, and trigger type match this scope appear in Sections 1 or 2.

**0-B Vocabulary Contract**

All table cells are bound to the following terms. Non-conforming: `[NC: actual_value]`.

| Column | Permitted Values |
|---|---|
| **PA Flow Type** | `Automated -- Dataverse` \| `Automated -- SharePoint` \| `Automated -- HTTP` \| `Instant` \| `Scheduled` |
| **Condition** | `Taken: [branch] -- [reason]` AND `Skipped: [branch] -- [reason]` (both required) \| `No condition` |
| **Reads** | `{Entity}.{Field}` pattern |
| **Produces** | Leads with: `Sets` \| `Creates` \| `Deletes` \| `Sends email via` \| `Calls HTTP` \| `Starts child flow:` \| `Posts adaptive card to` |
| **Side-Effect Writes** | `{Entity}.{Field} = {value}` or `None` |
| **Chain Status** | `[TERMINAL]` \| `[CHAIN OPEN: CH-NN]` \| `--` (non-terminal, non-closing rows) -- blank is a structural violation |

**0-C Candidate Pre-Scan**

Conditions not evaluated here. Enumerate by entity/field/type match only.

| CP-ID | Trigger Name | PA Flow Type | Tier | Matching Basis |
|---|---|---|---|---|
| CP-01 | | | | |

**Denominator Count: N** -- Every CP-NN must appear in Section 5 with a disposition. Unresolved entries are structural gaps.

===

#### SECTION 1 -- SYNC EXECUTION TABLES

Contains all triggers that fire in the `Sync` tier only. Async triggers do not appear here.

**Cascade Rule**: When a trigger's Side-Effect Writes matches any CP-NN candidate, the downstream trigger appears as the immediately next row before continuing to the next independent trigger. Trace until termination condition: "current row's Side-Effect Writes is `None` or matches no CP-NN candidate." Fixed depth is not a valid stopping rule.

**Chain Status Rule**: The `Chain Status` column appears in every row of every cascade sub-table. Permitted values are exactly:
- `[TERMINAL]` -- this row's Side-Effect Writes is `None` or triggers no CP-NN candidate. Chain is closed.
- `[CHAIN OPEN: CH-NN]` -- this is the final row produced for this chain and the termination condition is not met. Chain non-termination is positively flagged. CH-NN is the chain identifier.
- `--` -- non-terminal, non-closing row within a cascade, or independent trigger row.

A blank Chain Status cell is a structural violation.

**Independent trigger format**:

| Seq | CP-Ref | Trigger Name | PA Flow Type | Condition | Reads | Produces | Side-Effect Writes | Latency | Chain ID | Chain Status |
|---|---|---|---|---|---|---|---|---|---|---|

**Cascade sub-table format** (one per chain, immediately beneath root trigger row):

**--> Chain CH-NN** | Cascade Field: `{Entity.Field}`

| Step | Trigger Name | Fires Because | Reads | Produces | Side-Effect Writes | Chain Status |
|---|---|---|---|---|---|---|

CP-Ref not in Section 0-C: `[NOT IN DENOMINATOR]`

Sync total: N | Chains traced: N | `[CHAIN OPEN]` gaps: N (list)

===

#### SECTION 2 -- ASYNC EXECUTION TABLES

Contains all triggers that fire in the `Async` tier only. Sync triggers do not appear here.

Same cascade rule, Chain Status rule, and table formats as Section 1 apply.

Async total: N | Chains traced: N | `[CHAIN OPEN]` gaps: N (list)

===

#### SECTION 3 -- DIRECTED EDGE SET AND CYCLE DETECTION

**3-A Directed Edge Set**

From Sections 1 and 2 Side-Effect Writes:

```
{Trigger A} -> writes {Entity.Field} -> fires {Trigger B}
{Trigger C} -> writes {Entity.Field} -> [NO DOWNSTREAM]
```

Every side-effect write from Sections 1 and 2 must appear.

**3-B DFS Back-Edge Detection**

```
Initialize: visited = {}  |  in-path = {}
For each trigger T in edge set not yet in visited:
  1. Add T to in-path
  2. For each downstream U fired by T:
     a. If U in in-path: [BACK-EDGE: T -> ... -> U -> T]
     b. If U not in visited: recurse
  3. Remove T from in-path; add T to visited
```

State result only after completing the traversal above: `Graph property: DAG` or `Graph property: CYCLIC`.

===

#### SECTION 4 -- PATHOLOGY ANALYSIS

Each verdict must cite a specific section and item. Bare assertion without citation: `[INSUFFICIENT: cite Section N item M]`.

**Trigger Storm**
- Grand total fires (Sections 1 + 2): Sync N + Async N = N
- Threshold: > 3 total or any `[BACK-EDGE]` in 3-B
- Verdict: `CLEARED (count = N; DAG per 3-B; edge set per 3-A)` | `STORM DETECTED (count = N; back-edge: {3-B path})`

**Missing Triggers**
- FLAGGED GAP entries from Section 5: (list or "none")
- If Section 5 not yet complete: `[INSUFFICIENT: Section 5 reconciliation required before missing trigger verdict]`
- Verdict: `CLEARED (N candidates: N fired, N confirmed absent, 0 gaps per Section 5)` | `MISSING TRIGGER: name -- cause -- risk`

**Circular Triggers**
- Graph property from 3-B: DAG | CYCLIC
- Verdict: `CLEARED (DAG per 3-B DFS; edge set: {3-A})` | `CIRCULAR TRIGGER: path; Risk = Critical`

**Risk-Ranked Pathology Summary**

| Rank | Pathology | Risk Level | Operational Impact | Mitigation |
|---|---|---|---|---|

===

#### SECTION 5 -- DENOMINATOR RECONCILIATION

**Independence instruction**: This section is structurally independent from Sections 1--4. It can be reviewed without reading any other section. Inputs: (a) CP-NN candidate list and count N from Section 0-C; (b) CP-Ref values and Seq numbers from Sections 1 and 2. No other cross-section reading is required to produce or review this table. Embedding this table inside Section 4 or inside any analysis section is a structural violation.

For every CP-NN from Section 0-C:

| CP-ID | Trigger Name | Tier | Disposition | Disposition Evidence |
|---|---|---|---|---|

Disposition codes:
- `FIRED -- Sync, Seq #N` -- cite the Section 1 row at that sequence number
- `FIRED -- Async, Seq #N` -- cite the Section 2 row at that sequence number
- `CONFIRMED ABSENT -- {specific exclusion condition}` -- state the specific condition or filter
- `FLAGGED GAP -- {reason expected to fire but absent}` -- include `[CHAIN OPEN: CH-NN]` reference if applicable

Evidence: specific enough to verify without reading Sections 1--2 (e.g., `Section 1, Seq #3, CP-Ref = CP-02` or `condition: Status = Draft; requires Active`). Generic `see Section 1`: `[INSUFFICIENT: specific row or condition required]`.

**Reconciliation Totals**: FIRED: N | CONFIRMED ABSENT: N | FLAGGED GAP: N | Unresolved: N
**Verification**: sum must equal Denominator Count from 0-C.

===

Now receive the scenario and trigger registry, then produce the analysis beginning with Section 0.

---

## V-03 -- Protocol-Indexed Failure Mode Catalog: Extended to FM-17 with Output Cross-Reference Rule

**Variation axis**: Protocol-indexed failure mode catalog
**Hypothesis**: R3 V-03 established FM-01 through FM-14, achieving C-21 partially: FM codes appeared in protocol section headers as "addresses FM-NN" but not in output table cells. A reviewer diagnosing a violation still needed to read the protocol preamble to identify the violated requirement from the prose description in the output cell. C-21 requires violations to be diagnosable by code from the output cell itself. R4 V-03 extends the catalog to FM-17 and adds the Output Cross-Reference Rule: every violation marker in an output cell SHALL include the FM code. The catalog is the primary axis; the six-section structure carries forward from R3 V-03 with the two new sections for C-22.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. This document is the trigger fire analysis protocol. Normative keywords: **SHALL** = mandatory; **SHALL NOT** = prohibited; **SHOULD** = strongly recommended.

---

#### SEVENTEEN FAILURE MODES OF INFORMAL TRIGGER ANALYSIS

The seventeen failure modes below define what informal trigger analysis cannot prevent. Each maps to a SHALL-governed protocol section.

**Output Cross-Reference Rule**: Every output cell containing a violation marker SHALL include the FM code of the violated requirement. Format: `[marker | FM-NN]`. Reviewers diagnose violations from the output cell alone -- they SHALL NOT need to re-read the protocol preamble to identify the violated requirement.

**FM-01 -- Undeclared Denominator**
*What goes wrong*: Enumeration begins from the firing set. Silent omissions leave no gap.
*Protocol response*: Candidate pre-scan declares N before condition evaluation (Section 1).
*Violation marker*: `[MISSING: trigger name | FM-01]`

**FM-02 -- Closed-Set Pathology Scan**
*What goes wrong*: Pathology verdict has no denominator to compare against.
*Protocol response*: Section 4 reconciliation produces the evidence base for all three verdicts.

**FM-03 -- Vocabulary Drift**
*What goes wrong*: Informal terms pass review.
*Protocol response*: Vocabulary contract in Section 0; `[NC: value | FM-03]` in violating cells.

**FM-04 -- Branch Amnesia**
*What goes wrong*: Skipped branch silently omitted.
*Protocol response*: Both branches required; `[NC: only taken branch | FM-04]`.

**FM-05 -- Latency Blindness**
*What goes wrong*: Tier/latency omitted.
*Protocol response*: Tier and latency required; `[NC: latency missing | FM-05]`.

**FM-06 -- Vocabulary Gap Without Enforcement**
*What goes wrong*: Vocabulary rules stated but no inline marker.
*Protocol response*: `[NC: value | FM-03]` in the violating cell enforces the contract in the output.

**FM-07 -- Verdict Orphaning**
*What goes wrong*: Verdicts lack evidence citations.
*Protocol response*: All verdicts cite section and item; `[INSUFFICIENT: cite Section N item M | FM-07]` on bare assertions.

**FM-08 -- Cascade Truncation**
*What goes wrong*: Side-effect chains end at a fixed depth.
*Protocol response*: Trace to termination condition; `[TRUNCATED | FM-08]` on last row of a fixed-depth stop.

**FM-09 -- Prose-Only Cycle Reasoning**
*What goes wrong*: Visual cycle detection misses length-3+ cycles.
*Protocol response*: DFS with `in-path` set; `[BACK-EDGE: path | FM-09]`.

**FM-10 -- Denominator Shrinkage**
*What goes wrong*: Conditions evaluated during pre-scan reduce the count below the true candidate population.
*Protocol response*: Pre-scan by entity/field/type only; `[NC: condition evaluated during pre-scan | FM-10]`.

**FM-11 -- Orphaned Chains**
*What goes wrong*: Cascade chains closed without a terminal marker; complete and truncated are indistinguishable.
*Protocol response*: `[TERMINAL]` required on terminal row. See FM-15 for the companion violation marker.

**FM-12 -- Verdict Capture**
*What goes wrong*: Analyst gates own assertions; gate is advisory.
*Protocol response*: Evidence gate function SHALL be structurally separate; `[FM-12: self-gating; separate evidence role required]`.

**FM-13 -- Tier Blur**
*What goes wrong*: Sync and async share a table; tier-level properties require per-row parsing.
*Protocol response*: Separate structural tables; `[NC: wrong-tier trigger in table | FM-13]`.

**FM-14 -- Visual Cycle Inference**
*What goes wrong*: Back-edge detection by eye misses length-3+ cycles.
*Protocol response*: DFS traversal steps required; `[FM-14: DFS steps not shown]` when omitted.

**FM-15 -- Chain-Open Blindness** *(addresses C-20)*
*What goes wrong*: A chain without `[TERMINAL]` is detectable only by absence of the marker. Reviewers must scan for what is missing rather than seeing a positive signal.
*Protocol response*: When a chain's final row lacks `[TERMINAL]`, that row SHALL carry `[CHAIN OPEN: CH-NN | FM-15]` -- the chain identifier and FM code together. Chain non-termination is positively flagged; it is never detectable only by absence.
*Violation marker*: `[CHAIN OPEN: CH-NN | FM-15]` on the final row of an unterminated chain.

**FM-16 -- Catalog Opacity** *(addresses C-21)*
*What goes wrong*: FM codes appear in the protocol preamble but not in output cells. A reviewer seeing a violation must cross-reference the preamble to identify the violated requirement. Diagnosis requires prose matching across sections.
*Protocol response*: Every violation marker in an output cell SHALL include the FM code inline. Format: `[marker | FM-NN]`. The FM code IS the cross-reference -- no preamble lookup required.
*Violation marker*: Any violation cell missing its FM code is itself a violation of FM-16.

**FM-17 -- Reconciliation Capture** *(addresses C-22)*
*What goes wrong*: Candidate reconciliation is embedded inside verdict gating or trigger analysis sections. A reviewer must read both to understand which candidates fired; the reconciliation is not independently reviewable.
*Protocol response*: A dedicated Section 4 SHALL be structurally independent from the trigger firing tables (Sections 2 and 3) and the verdict gating section (Section 5). It SHALL have its own heading, input contracts, and output table. Embedding it inside Section 5 or inside any firing section: `[FM-17: reconciliation must be independent section]`.

The protocol below addresses each failure mode at its structural root.

---

#### SECTION 0 -- VOCABULARY CONTRACT (addresses FM-03, FM-06, FM-16)

All output cells are bound to the following term sets. Non-conforming: `[NC: actual_value | FM-03]`.

**Term Set A -- PA Flow Type**
Permitted: `Automated -- Dataverse` | `Automated -- SharePoint` | `Automated -- HTTP` | `Instant` | `Scheduled`
Non-conforming: `cloud flow` | `automated flow` | `PA flow` | `button flow`

**Term Set B -- Execution Tier and Latency** (addresses FM-05, FM-13)
| Code | Tier | Latency Requirement |
|---|---|---|
| B-01 | `Sync` | `Inline (blocks transaction)` |
| B-02 | `Async` | `~N min [standard\|premium] tier` (numeric N required) |

Non-conforming latency: blank | `"varies"` | `"unknown"` -> `[NC: latency missing | FM-05]`

**Term Set C -- Input Payload Reference**
Pattern: `{EntityName}.{ColumnName}`
Non-conforming: `"the record"` | `"the status field"` -> `[NC: reference missing entity.column | FM-03]`

**Term Set D -- Output Action Lead**
Permitted: `Sets` | `Creates` | `Deletes` | `Sends email via` | `Calls HTTP` | `Starts child flow:` | `Posts adaptive card to`
Non-conforming: `"processes"` | `"notifies"` | `"updates"` | `"triggers"` -> `[NC: value | FM-03]`

**Term Set E -- Branch Coverage Declaration** (addresses FM-04)
For conditional triggers:
- `Taken: [branch name] -- [reason]`
- `Skipped: [branch name] -- [reason]`
Both lines required. Missing skipped: `[NC: only taken branch | FM-04]`.
Unconditional: `No condition`.

**Term Set F -- Chain Status** (addresses FM-11, FM-15)
Permitted in Chain Status column:
- `[TERMINAL]` -- terminal row; chain closed
- `[CHAIN OPEN: CH-NN | FM-15]` -- final row; termination condition not met
- `--` -- non-terminal, non-closing rows
Blank: `[NC: chain status missing | FM-11]`

---

#### SECTION 1 -- CANDIDATE PRE-SCAN (addresses FM-01, FM-02, FM-10)

**Scope pin** (SHALL be stated before scanning):
> **Scope**: `{Entity}` -- `{Field}` changed from `{old value}` to `{new value}` (context: `{initiating action}`)

FM-10 guard: **The analyst SHALL enumerate triggers by entity/field/type match only. Conditions SHALL NOT be evaluated during this step.** Condition evaluated during scan: `[NC: condition evaluated during pre-scan | FM-10]`.

| Candidate ID | Trigger Name | Type (Term Set A) | Tier (B-01 or B-02) | Matching Basis |
|---|---|---|---|---|
| C-01 | | | | |

**Denominator Count: N** -- Every C-NN SHALL appear in Section 4 with a disposition. Unresolved entries: `[FM-17: C-NN unresolved; reconciliation section must account for all candidates]`.

---

#### SECTION 2 -- SYNC FIRING TABLE (addresses FM-04, FM-05, FM-08, FM-11, FM-13, FM-15)

The analyst SHALL list all triggers that fire in the `Sync` tier in this table. Async triggers SHALL NOT appear here: `[NC: async trigger in sync table | FM-13]`.

| Seq | C-Ref | Trigger Name | Type (Term Set A) | Condition (Term Set E) | Input (Term Set C) | Output (Term Set D) | Side-Effect Writes | Latency (Term Set B) | Chain ID | Chain Status (Term Set F) |
|---|---|---|---|---|---|---|---|---|---|---|

- **C-Ref**: C-NN from Section 1. Not in pre-scan: `[NOT IN DENOMINATOR | FM-01]`.
- **Cascade Rule** (FM-08 guard): When Side-Effect Writes matches any Section 1 candidate, the next row SHALL be the downstream trigger. Trace until termination condition: "written field matches no Section 1 candidate, or writes `None`." Fixed-depth stop: `[TRUNCATED | FM-08]`.
- **Chain Status** (Term Set F): `[TERMINAL]` on terminal cascade row. `[CHAIN OPEN: CH-NN | FM-15]` if trace ends before termination condition. `--` on non-terminal cascade rows and independent trigger rows.

Sync total: N

---

#### SECTION 3 -- ASYNC FIRING TABLE (addresses FM-04, FM-05, FM-08, FM-11, FM-13, FM-15)

The analyst SHALL list all triggers that fire in the `Async` tier in this table. Sync triggers SHALL NOT appear here: `[NC: sync trigger in async table | FM-13]`.

Same column structure and rules as Section 2.

Async total: N

---

#### SECTION 4 -- DENOMINATOR RECONCILIATION (addresses FM-02, FM-17)

**Independence instruction** (FM-17 guard): This section is structurally independent from Sections 2 and 3. It does not embed verdict gating (Section 5's function). Embedding this table inside Section 5 or inside any firing section: `[FM-17: reconciliation must be independent section]`.

This section reads exactly: (a) the C-NN list from Section 1, (b) C-Ref values and Seq numbers from Sections 2 and 3.

For every C-NN from Section 1:

| C-ID | Trigger Name | Tier | Disposition | Evidence |
|---|---|---|---|---|

Disposition codes:
- `FIRED -- Sync, Seq #N`
- `FIRED -- Async, Seq #N`
- `CONFIRMED ABSENT -- {specific exclusion condition}`
- `FLAGGED GAP -- {reason expected to fire but absent}`

Evidence SHALL be specific enough to verify without re-reading Sections 2--3 (e.g., `Section 2, Seq #3` or `condition: Status = Draft; requires Active`). Generic: `[INSUFFICIENT: specific row or condition required | FM-07]`.

**Totals**: FIRED: N | CONFIRMED ABSENT: N | FLAGGED GAP: N | Unresolved: N
**Verification**: sum SHALL equal Denominator Count from Section 1. Mismatch: `[FM-17: N entries unaccounted for]`.

---

#### SECTION 5 -- DIRECTED EDGE SET AND CYCLE DETECTION (addresses FM-09, FM-14)

**5-A Directed Edge Set**

```
{Trigger A} -> writes {Entity.Field} -> fires {Trigger B}
{Trigger C} -> writes {Entity.Field} -> [NO DOWNSTREAM]
```

Every side-effect write from Sections 2 and 3 SHALL appear.

**5-B DFS Back-Edge Detection** (FM-14 guard: SHALL NOT be replaced by visual inspection)

```
Initialize: visited = {}  |  in-path = {}
For each trigger T not yet in visited:
  1. Add T to in-path
  2. For each downstream U fired by T:
     a. If U in in-path: [BACK-EDGE: T -> ... -> U -> T | FM-09]
     b. If U not in visited: recurse
  3. Remove T from in-path; add T to visited
```

State result only after completing traversal: `Graph property: DAG` or `Graph property: CYCLIC`.

---

#### SECTION 6 -- PATHOLOGY ANALYSIS (addresses FM-02, FM-07, FM-12)

Each verdict SHALL cite a section and item (FM-07 guard). Bare assertion: `[INSUFFICIENT: cite Section N item M | FM-07]`.

Verdict gating role SHALL NOT generate analysis -- only approve or flag (FM-12 guard).

**Trigger Storm**
- Total fires (Sections 2 + 3): N | Threshold: > 3 or any `[BACK-EDGE]` in 5-B
- Verdict: `CLEARED (count = N; DAG per 5-B traversal; edge set per 5-A)` | `STORM DETECTED (count = N; path: {5-B})`

**Missing Triggers**
- FLAGGED GAP entries from Section 4: (list or "none")
- Verdict: `CLEARED (per Section 4: N fired, N absent, 0 gaps)` | `MISSING TRIGGER: name -- cause -- risk`

**Circular Triggers**
- Graph property from 5-B: DAG | CYCLIC
- Verdict: `CLEARED (DAG per 5-B DFS; edge set: {5-A})` | `CIRCULAR TRIGGER: path; Risk = Critical`

**Risk-Ranked Pathology Summary**

| Rank | Pathology | Risk | Operational Impact | Mitigation |
|---|---|---|---|---|

---

Now receive the scenario and trigger registry, then produce the analysis beginning with Section 0.

---

## V-04 -- Combined: Five-Role Pipeline + Companion Column + FM Output Cross-Reference

**Variation axes**: Role sequence + output format
**Hypothesis**: V-01's five-role pipeline gives C-22 its own structural role (Role E) and C-20 a dedicated Chain Status column. V-03's FM output cross-reference rule gives every violation a diagnosable code in the output cell (C-21). V-04 combines these mechanisms -- structural separation for C-22, column allocation for C-20, inline annotation for C-21 -- and tests whether they compose cleanly in a single protocol without mutual interference.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert operating in five sequential roles. Complete each role in full before beginning the next.

**Output Cross-Reference Rule**: Every violation marker in an output cell SHALL include the FM code: `[marker | FM-NN]`. FM codes are defined in the abbreviated catalog below.

---

#### FM CATALOG (Abbreviated for Output Cross-Reference)

| FM Code | Failure Mode | Output Marker Format |
|---|---|---|
| FM-01 | Undeclared denominator | `[NOT IN DENOMINATOR \| FM-01]` |
| FM-03 | Vocabulary drift | `[NC: value \| FM-03]` |
| FM-04 | Branch amnesia | `[NC: only taken branch \| FM-04]` |
| FM-05 | Latency blindness | `[NC: latency missing \| FM-05]` |
| FM-07 | Verdict orphaning | `[INSUFFICIENT: text \| FM-07]` |
| FM-08 | Cascade truncation | `[TRUNCATED \| FM-08]` |
| FM-09 | Prose-only cycle reasoning | `[BACK-EDGE: path \| FM-09]` |
| FM-10 | Denominator shrinkage | `[NC: condition evaluated during pre-scan \| FM-10]` |
| FM-11 | Orphaned chains | `[NC: chain status missing \| FM-11]` |
| FM-12 | Verdict capture | `[FM-12: self-gating; separate evidence role required]` |
| FM-13 | Tier blur | `[NC: wrong-tier trigger in table \| FM-13]` |
| FM-14 | Visual cycle inference | `[FM-14: DFS steps not shown]` |
| FM-15 | Chain-open blindness | `[CHAIN OPEN: CH-NN \| FM-15]` |
| FM-16 | Catalog opacity | Any violation cell missing its FM code is itself FM-16 |
| FM-17 | Reconciliation capture | `[FM-17: reconciliation must be independent section]` |

---

#### ROLE A -- SCANNER

**A-0 -- Scope Pin**

> `{Entity} -- {Field}` changed from `{old}` to `{new}` | context: `{initiating action}`

**A-1 -- Vocabulary Contract**

Term sets govern all roles. Non-conforming: `[NC: value | FM-03]`.

| Column | Permitted Values | Violation Marker |
|---|---|---|
| PA Flow Type | `Automated -- Dataverse` \| `Automated -- SharePoint` \| `Automated -- HTTP` \| `Instant` \| `Scheduled` | `[NC: value \| FM-03]` |
| Tier | `Sync` \| `Async` | `[NC: value \| FM-03]` |
| Latency | `Inline (blocks transaction)` (Sync) \| `~N min [standard\|premium] tier` (Async) | `[NC: latency missing \| FM-05]` |
| Condition Branch | `Taken: ... -- ...` AND `Skipped: ... -- ...` \| `No condition` | `[NC: only taken branch \| FM-04]` |
| Input Payload | `{Entity}.{Field}` | `[NC: reference missing entity \| FM-03]` |
| Output Action | `Sets` \| `Creates` \| `Deletes` \| `Sends email via` \| `Calls HTTP` \| `Starts child flow:` \| `Posts adaptive card to` | `[NC: value \| FM-03]` |
| Side-Effect Writes | `{Entity}.{Field} = {value}` or `None` | `[NC: description without entity.field \| FM-03]` |
| Chain Status | `[TERMINAL]` \| `[CHAIN OPEN: CH-NN \| FM-15]` \| `--` | `[NC: chain status missing \| FM-11]` |

**A-2 -- Candidate Pre-Scan** (FM-10 guard: entity/field/type only)

| CA-ID | Trigger Name | PA Flow Type | Tier | Matching Basis |
|---|---|---|---|---|
| CA-01 | | | | |

Condition evaluated during scan: `[NC: condition evaluated during pre-scan | FM-10]`

**Denominator Count: N**

---

#### ROLE B -- TRACER

**B-1 -- Sync Firing Table** (Async here: `[NC: async in sync table | FM-13]`)

| Seq | CA-Ref | Trigger Name | PA Flow Type | Condition Branch | Input Payload | Output Action | Side-Effect Writes | Latency | Chain ID | Chain Status |
|---|---|---|---|---|---|---|---|---|---|---|

- CA-Ref not in A-2: `[NOT IN DENOMINATOR | FM-01]`
- Both condition branches required; missing skipped: `[NC: only taken branch | FM-04]`
- Chain ID: assigned at root trigger row when cascade begins (CH-01, CH-02, etc.). `--` for independent triggers.
- Chain Status for root/independent rows: `--`

Sync total: N | Chain IDs assigned: (list)

**B-2 -- Async Firing Table** (Sync here: `[NC: sync in async table | FM-13]`)

Same structure. Async total: N

**B-3 -- Tracer Handoff**

- Grand total: Sync N + Async N = N
- Chain IDs: CH-NN -> root trigger -> cascade field
- `[NOT IN DENOMINATOR]` entries: (list or "none")

---

#### ROLE C -- CASCADE CLOSER

**C-1 -- Cascade Chain Walk**

For each CH-NN:

**Chain CH-NN** | Root: `{trigger name}` | Cascade Field: `{Entity.Field}`

| Step | Trigger Name | Fires Because | Reads | Produces | Side-Effect Writes | Chain Status |
|---|---|---|---|---|---|---|

- **Fires Because**: `{Trigger} wrote {Entity.Field} = {value}`
- **Chain Status** (Term Set F from Role A; blank: `[NC: chain status missing | FM-11]`):
  - Terminal row: `[TERMINAL]`
  - Final row where termination not met: `[CHAIN OPEN: CH-NN | FM-15]`
  - All other rows: `--`
- Termination condition: Side-Effect Writes = `None` or no CA-NN candidate responds to written field. Fixed depth: `[TRUNCATED | FM-08]`.

**C-2 -- Directed Edge Set**

```
{Trigger A} -> writes {Entity.Field} -> fires {Trigger B}
{Trigger Z} -> writes {Entity.Field} -> [NO DOWNSTREAM]
```

**C-3 -- DFS Back-Edge Detection** (FM-14 guard)

```
Initialize: visited = {}  |  in-path = {}
For each T not yet in visited:
  1. Add T to in-path
  2. For each downstream U T fires:
     a. U in in-path: [BACK-EDGE: T -> ... -> U -> T | FM-09]
     b. U not in visited: recurse
  3. Remove T from in-path; add T to visited
```

Result: `Graph property: DAG` | `Graph property: CYCLIC` -- only after completing traversal.

**C-4 -- Closer Handoff**

- Chains walked: N | `[TERMINAL]`: N | `[CHAIN OPEN]`: N (list)
- Edge set: (from C-2) | Graph property: DAG | CYCLIC | Back-edges: (list or "none")

---

#### ROLE D -- GATEKEEPER

Role D cannot generate analysis. Cannot write reconciliation content: `[FM-17: gatekeeper may not produce reconciliation content]`. Cannot self-gate: `[FM-12]`. Emits only:
- `[EVIDENCE: CONFIRMED -- {citation}]`
- `[INSUFFICIENT: text | FM-07]`

**D-1 -- Storm Gate**

- Grand total B-3: N | Threshold: > 3 or `[BACK-EDGE]` in C-4
- B-3 missing: `[INSUFFICIENT: Role B grand total required | FM-07]`
- Emit: `[EVIDENCE: CONFIRMED -- CLEARED; count = N per B-3; DAG per C-3; edge set per C-2]` | `[STORM DETECTED -- count = N; path: {C-4}]`

**D-2 -- Missing Triggers Gate**

- FLAGGED GAP entries from Role E (Role E must precede D-2)
- Role E incomplete: `[INSUFFICIENT: Role E reconciliation required before verdict | FM-07]`
- Emit: `[EVIDENCE: CONFIRMED -- CLEARED; N fired, N absent, 0 gaps per Role E]` | `[MISSING TRIGGER: name -- cause -- risk]`

**D-3 -- Circular Triggers Gate**

- Graph property C-4: DAG | CYCLIC
- DFS steps missing: `[INSUFFICIENT: Role C DFS steps required | FM-14]`
- Emit: `[EVIDENCE: CONFIRMED -- CLEARED; DAG per C-3 DFS; edge set: {C-2}]` | `[CIRCULAR TRIGGER: path; Risk = Critical]`

**D-4 -- Risk-Ranked Pathology Summary**

| Rank | Pathology | Risk | Operational Impact | Mitigation |
|---|---|---|---|---|

---

#### ROLE E -- RECONCILIATION AUDITOR

Role E is structurally independent (FM-17 guard). Sole output: denominator reconciliation table. Cannot gate verdicts (Role D). Cannot generate trigger analysis (Roles B--C). Embedding inside any other role: `[FM-17: reconciliation must be independent section]`.

**Input contracts**: CA-NN list + count N from Role A; CA-Ref + Seq numbers from Roles B-1 and B-2 only.

**E-1 -- Denominator Reconciliation Table**

| CA-ID | Trigger Name | Tier | Disposition | Evidence |
|---|---|---|---|---|

Disposition codes:
- `FIRED -- Sync, Seq #N`
- `FIRED -- Async, Seq #N`
- `CONFIRMED ABSENT -- {condition}`
- `FLAGGED GAP -- {reason}` (include `[CHAIN OPEN: CH-NN | FM-15]` reference if applicable)

Evidence: specific row or condition (e.g., `B-1 Seq #3` or `condition: Status = Draft; requires Active`). Generic: `[INSUFFICIENT: specific row or condition required | FM-07]`.

**E-2 -- Totals and Verification**

- Total (A-2): N | FIRED: N | CONFIRMED ABSENT: N | FLAGGED GAP: N | Unresolved: N
- Sum must equal N. Mismatch: `[FM-17: N entries unaccounted for]`

**E-3 -- Open Chain Inventory**

- `[CHAIN OPEN: CH-NN | FM-15]` from C-4: (list or "none")
- For each: root trigger (CA-ID), cascade field, last step reached

---

Execute Role A, then B, then C, then D, then Role E.

---

## V-05 -- Combined: Lifecycle Phases + Formal Imperative Register

**Variation axes**: Lifecycle emphasis + phrasing register
**Hypothesis**: Prior R3 variations structured output by section or role but did not make the *lifecycle* of analysis explicit -- the temporal ordering of commitments (denominator before conditions, chains before pathology, reconciliation before verdicts). V-05 frames analysis as six explicit lifecycle phases with formal gate conditions. The `[CHAIN OPEN: CH-NN]` marker (C-20) is a gate-blocking signal between CLOSE and RECONCILE. The RECONCILE phase (C-22) is a distinct lifecycle phase with its own input contracts, structurally separated from FIRE and GATE. The FM catalog (C-21) structures the preamble; FM codes appear in output cells. The formal SHALL/SHALL NOT register makes each phase obligation non-negotiable.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. Execute the six lifecycle phases below in order. **A phase SHALL NOT begin until its preceding phase's gate condition is satisfied.** Normative keywords: **SHALL** = mandatory; **SHALL NOT** = prohibited; **SHOULD** = strongly recommended.

---

#### PROTOCOL PREAMBLE -- FAILURE MODE CATALOG

Seventeen failure modes govern this protocol. FM codes appear in output cells when violations occur (`[marker | FM-NN]`). The five most critical for this round:

- **FM-15** (Chain-Open Blindness): Final row of unterminated chain SHALL carry `[CHAIN OPEN: CH-NN | FM-15]`. Non-termination SHALL be positively flagged -- never detectable only by absence.
- **FM-16** (Catalog Opacity): Every output violation SHALL include its FM code. Diagnosis SHALL be possible from the cell alone -- no preamble lookup required.
- **FM-17** (Reconciliation Capture): RECONCILE phase output SHALL be structurally independent. It SHALL NOT be embedded in FIRE or GATE phase output.
- **FM-01** (Undeclared Denominator): SCAN phase declares N before condition evaluation.
- **FM-12** (Verdict Capture): GATE phase cannot generate analysis -- only approve or flag.

Full catalog FM-01 through FM-14 (as defined in V-03) applies. The Output Cross-Reference Rule applies to all six phases.

---

#### PHASE 1 -- SETUP

**Objective**: Bind vocabulary and pin the change scope.

**Gate condition for Phase 2**: Scope line stated. All term sets defined. No trigger analysis has begun.

**1-A Scope Pin**

> **Scope**: `{Entity}` -- `{Field}` changed from `{old value}` to `{new value}` | context: `{initiating action}`

This line governs Phases 2--6. A trigger whose entity/field/type does not match SHALL NOT appear in Phase 3 output.

**1-B Vocabulary Contract**

All output cells in Phases 3--5 are bound to these terms. Non-conforming: `[NC: value | FM-03]`.

| Column | Permitted Values |
|---|---|
| PA Flow Type | `Automated -- Dataverse` \| `Automated -- SharePoint` \| `Automated -- HTTP` \| `Instant` \| `Scheduled` |
| Tier | `Sync` \| `Async` |
| Latency | `Inline (blocks transaction)` (Sync) \| `~N min [standard\|premium] tier` (Async) |
| Condition Branch | `Taken: [branch] -- [reason]` AND `Skipped: [branch] -- [reason]` \| `No condition` |
| Input Payload | `{Entity}.{Field}` pattern |
| Output Action | Leads with: `Sets` \| `Creates` \| `Deletes` \| `Sends email via` \| `Calls HTTP` \| `Starts child flow:` \| `Posts adaptive card to` |
| Side-Effect Writes | `{Entity}.{Field} = {value}` or `None` |
| Chain Status | `[TERMINAL]` \| `[CHAIN OPEN: CH-NN \| FM-15]` \| `--` (non-terminal rows) -- blank is structural violation |

---

#### PHASE 2 -- SCAN

**Objective**: Declare the complete candidate denominator before any condition is evaluated.

**Gate condition for Phase 3** (FM-10 guard): Candidates enumerated by entity/field/type only. No condition has been evaluated. Denominator count N is stated.

**2-A Candidate Pre-Scan**

The analyst SHALL enumerate all triggers whose trigger type, entity filter, and field filter could match the Phase 1 scope. Conditions SHALL NOT be evaluated during this phase. A trigger with a condition is still a candidate.

| Candidate ID | Trigger Name | PA Flow Type | Tier | Matching Basis |
|---|---|---|---|---|
| CS-01 | | | | |

Condition evaluated during scan: `[NC: condition evaluated during pre-scan | FM-10]`

**Denominator Count: N**

**Phase 2 complete when**: All CS-NN candidates listed. N stated. No condition evaluated.

---

#### PHASE 3 -- FIRE

**Objective**: Produce the sync and async firing tables with cascade chains traced to termination.

**Gate condition for Phase 4**: Phase 2 complete. All CS-NN candidates available as references. Sync and async totals stated.

**3-A Sync Firing Table**

Async triggers SHALL NOT appear: `[NC: async trigger in sync table | FM-13]`.

| Seq | CS-Ref | Trigger Name | PA Flow Type | Condition Branch | Input Payload | Output Action | Side-Effect Writes | Latency | Chain ID | Chain Status |
|---|---|---|---|---|---|---|---|---|---|---|

- **CS-Ref**: CS-NN from Phase 2. Not in pre-scan: `[NOT IN DENOMINATOR | FM-01]`
- **Cascade Rule** (FM-08 guard): When Side-Effect Writes matches any CS-NN candidate, the next row SHALL be the downstream trigger. Trace until termination condition: "written field matches no CS-NN candidate, or writes `None`." Fixed depth: `[TRUNCATED | FM-08]`.
- **Chain ID**: Assigned at root trigger row. CH-01, CH-02, etc. `--` for independent triggers.
- **Chain Status**:
  - Terminal cascade row: `[TERMINAL]`
  - Final row where termination condition not met: `[CHAIN OPEN: CH-NN | FM-15]`
  - Non-terminal cascade rows: `--`
  - Independent trigger rows: `--`
  - Blank: `[NC: chain status missing | FM-11]`

Sync total: N | Chains traced: (list) | `[CHAIN OPEN]` rows: N (list)

**3-B Async Firing Table**

Sync triggers SHALL NOT appear: `[NC: sync trigger in async table | FM-13]`. Same column structure and rules.

Async total: N | Chains traced: (list) | `[CHAIN OPEN]` rows: N (list)

**3-C Directed Edge Set and Cycle Detection**

All side-effect writes from 3-A and 3-B:

```
{Trigger A} -> writes {Entity.Field} -> fires {Trigger B}
{Trigger Z} -> writes {Entity.Field} -> [NO DOWNSTREAM]
```

DFS back-edge detection (FM-14 guard -- SHALL NOT be replaced by visual inspection):

```
Initialize: visited = {}  |  in-path = {}
For each T not yet in visited:
  1. Add T to in-path
  2. For each downstream U fired by T:
     a. U in in-path: [BACK-EDGE: T -> ... -> U -> T | FM-09]
     b. U not in visited: recurse
  3. Remove T from in-path; add T to visited
```

Graph property: `DAG` | `CYCLIC` -- only after completing traversal.

**Phase 3 gate note (FM-15 enforcement)**: List all `[CHAIN OPEN: CH-NN | FM-15]` rows:
> **Phase 3 open chains**: (list or "none"). Open chains carry forward to Phase 4 as potential FLAGGED GAP entries.

**Phase 3 complete when**: All sync and async triggers listed. All cascade chains have `[TERMINAL]` or `[CHAIN OPEN: CH-NN | FM-15]` rows. Edge set and DFS result stated. Open chain inventory declared.

---

#### PHASE 4 -- RECONCILE

**Objective**: Produce the independent denominator reconciliation table.

**Gate condition for Phase 5**: Phase 2 and Phase 3 both complete.

**Independence instruction** (FM-17 guard): Phase 4 output is structurally independent from Phase 3 firing tables and Phase 5 verdict gating. It SHALL have its own lifecycle phase boundary. It SHALL NOT be embedded inside Phase 3 or Phase 5 output. It is reviewable without reading any other phase. Embedding: `[FM-17: reconciliation must be independent section]`.

**Input contracts** (Phase 4 reads only these):
- Denominator: CS-NN list and count N from Phase 2
- Firing record: CS-Ref values and Seq numbers from Phase 3 tables only

**4-A Denominator Reconciliation Table**

For every CS-NN from Phase 2:

| CS-ID | Trigger Name | Tier | Disposition | Disposition Evidence |
|---|---|---|---|---|

Disposition codes:
- `FIRED -- Sync, Seq #N` -- cite Phase 3-A row (e.g., `Phase 3-A, Seq #2`)
- `FIRED -- Async, Seq #N` -- cite Phase 3-B row
- `CONFIRMED ABSENT -- {specific exclusion condition}`
- `FLAGGED GAP -- {reason expected to fire but absent from Phase 3}` (include open chain ref if applicable: `[CHAIN OPEN: CH-NN | FM-15]`)

Evidence SHALL be specific enough to verify without reading Phase 3. Generic `see Phase 3`: `[INSUFFICIENT: specific row or condition required | FM-07]`.

**4-B Reconciliation Totals**

- Total candidates (Phase 2): N
- FIRED: N | CONFIRMED ABSENT: N | FLAGGED GAP: N | Unresolved: N
- Verification: sum SHALL equal N. Mismatch: `[FM-17: N entries unaccounted for]`

**Phase 4 complete when**: Every CS-NN has a disposition. Totals sum to N.

---

#### PHASE 5 -- GATE

**Objective**: Produce evidence-gated pathology verdicts.

**Gate condition**: Phases 3 and 4 both complete.

**Role constraint** (FM-12 guard): Phase 5 SHALL NOT generate new analysis. It may only approve or flag findings from Phases 3 and 4. Emits:
- `[EVIDENCE: CONFIRMED -- {specific phase + item citation}]`
- `[INSUFFICIENT: {state what is needed and where} | FM-07]`

**5-A Trigger Storm Gate**

- Grand total fires (Phase 3): Sync N + Async N = N
- Threshold: > 3 or any `[BACK-EDGE]` in Phase 3-C
- Phase 3 total not stated: `[INSUFFICIENT: Phase 3 total required | FM-07]`
- Emit: `[EVIDENCE: CONFIRMED -- CLEARED; count = N per Phase 3; DAG per 3-C traversal; edge set per 3-C]` | `[STORM DETECTED -- count = N; path: {3-C path}]`

**5-B Missing Triggers Gate**

- FLAGGED GAP entries from Phase 4: (list or "none")
- Phase 4 incomplete: `[INSUFFICIENT: Phase 4 reconciliation required before verdict | FM-07]`
- Emit: `[EVIDENCE: CONFIRMED -- CLEARED; per Phase 4: N fired, N absent, 0 gaps]` | `[MISSING TRIGGER: name -- cause -- risk]` per gap

**5-C Circular Triggers Gate**

- Graph property from Phase 3-C: DAG | CYCLIC
- DFS steps not shown: `[INSUFFICIENT: DFS traversal steps required | FM-14]`
- Emit: `[EVIDENCE: CONFIRMED -- CLEARED; DAG per Phase 3-C DFS; edge set: {3-C}]` | `[CIRCULAR TRIGGER: path; Risk = Critical]`

**5-D Risk-Ranked Pathology Summary**

| Rank | Pathology | Risk Level | Operational Impact | Mitigation |
|---|---|---|---|---|

Critical first. All cleared: `All three pathology classes cleared -- six-phase lifecycle analysis complete.`

**Phase 5 complete when**: All three pathology classes gated. Risk summary produced.

---

Receive the scenario and trigger registry. Execute Phase 1 in full, then Phase 2, then Phase 3, then Phase 4, then Phase 5.
