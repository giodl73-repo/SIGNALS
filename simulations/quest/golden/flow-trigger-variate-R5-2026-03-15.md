# flow-trigger Skill Prompt Variations — Round 5

Generated: 2026-03-15
Rubric: v5 (C-01 through C-25, aspirational /17)
New criteria targeted: C-23 (self-enforcing FM catalog completeness), C-24 (role input contract declarations), C-25 (enum-typed binary protocol state column)

---

## Gap Analysis Entering Round 5

### Pre-read of R4 Scorecard Evidence (Against Rubric v4, C-01 Through C-22)

Top scorers: V-01 (99.6, Gold) and V-03 (99.6, Gold). V-04 = V-05 (99.3, Gold). V-02 (98.2, Gold).
All 5 variations passed all essential and recommended criteria.

Three new patterns extracted from R4 output:

| Pattern | Where Observed in R4 | R4 Mechanism | R5 Gap |
|---------|---------------------|--------------|--------|
| Self-enforcing FM catalog completeness (C-23) | V-01 FM-16: "Blank FM slot in a violation cell: structural violation." V-03 FM-16: "FM-16 self-enforces: any violation cell missing its FM code is itself a violation." | The self-reference rule exists in prose within the FM-16 entry. | C-23 requires the self-referential entry to be a named FM entry (e.g., FM-18) that explicitly states: omitting an FM code on any violation cell generates a new FM-18 violation on that cell. V-01 says "blank = structural violation" but doesn't name which FM code the blank generates. V-03 is closest but the loop isn't mechanically closed: "FM-16 self-enforces" doesn't show that a missing FM code becomes a FM-NN annotation on the same cell. |
| Role input contract declarations (C-24) | V-01 Role E: "Input contracts (Role E reads only these): From Role A: CA-NN list; From Role B: CA-Ref values." | Role E alone declares its input contracts. Roles A, B, C, D have no input contract block. | C-24 requires EVERY structurally separate role to declare its input contracts. A 5-role pipeline where only Role E has declared inputs leaves 4 roles with undeclared boundaries — those roles can silently consume undeclared outputs without generating a detectable violation. |
| Enum-typed binary protocol state column (C-25) | V-02: "Chain Status pre-allocated as a two-value enum; blank = structural violation." | Chain Status described as two-value enum in cascade sub-table column definition. Blank = structural violation stated as vocabulary rule. | C-25 requires the column itself to enforce the enum — not a vocabulary audit downstream. The column definition must declare a type: ENUM{[TERMINAL], [CHAIN OPEN: CH-NN \| FM-15]}. Deviations are column-structural violations caught at column evaluation time, before any marker check. V-02's "blank = structural violation" is still caught by a companion-marker rule (C-20), not by the column type constraint. |

### What Rubric v5 Adds (C-23 Through C-25)

| ID | Criterion | R4 Partial Evidence | R5 Design Obligation |
|----|-----------|---------------------|----------------------|
| C-23 | Self-enforcing FM catalog completeness | V-01 FM-16 "blank = structural violation"; V-03 "FM-16 self-enforces" | Add FM-18 as a named catalog entry: if a violation cell omits its FM code, that omission IS a violation of FM-18, and the cell SHALL carry `[marker \| FM-18: FM code required]`. The self-referential loop: FM-18 applies even to FM-18 violations that omit their own code. Coverage is complete when no violation cell has a codeless marker. |
| C-24 | Role input contract declarations | V-01 Role E input contracts only | Every structurally separate role declares exactly which prior-role outputs it may consume. New FM-19: `[FM-19: role input boundary violation — {role} may not consume {source}]`. |
| C-25 | Enum-typed binary protocol state column | V-02 two-value enum with vocabulary enforcement | Define Chain Status column type as ENUM{[TERMINAL] \| [CHAIN OPEN: CH-NN \| FM-15] \| --}. Blanks are column type violations detected at column evaluation time. New FM-20: `[TYPE-ERR-CS: ENUM required \| FM-20]`. The enforcement mechanism is column structural — not vocabulary audit. |

### R5 Variation Map

Foundation carried forward (no rediscovery needed from R4):
- Vocabulary contract with negative examples + `[NC: value | FM-03]` (C-11)
- `[INSUFFICIENT | FM-07]` / `[EVIDENCE: CONFIRMED -- {citation}]` verdict gates (C-12)
- Cascade trace to termination condition — not fixed depth; `[TRUNCATED | FM-08]` (C-13)
- Directed edge set for circular detection (C-14)
- Candidate denominator pre-scan — conditions not evaluated during scan (C-15)
- `[TERMINAL]` per-chain terminal row marker (C-16)
- Role-separated evidence gating — gating role cannot write analysis (C-17)
- Sync/async structural table split (C-18)
- DFS back-edge detection with `in-path` set (C-19)
- `[CHAIN OPEN: CH-NN | FM-15]` companion marker (C-20)
- FM-01 through FM-17 catalog with output cross-reference rule (C-21)
- Role E structurally independent denominator reconciliation (C-22)

| Variation | Axis | New Criteria Targeted | Hypothesis |
|-----------|------|-----------------------|------------|
| V-01 | Role sequence | C-24 | Adding an explicit Input Contract block to EVERY role — with FM-19 as the boundary-violation marker — makes all 5 role input boundaries mechanically verifiable; a role reading undeclared output generates FM-19 rather than a silent crossing |
| V-02 | Output format | C-25 | Defining Chain Status as a column type (`ENUM{[TERMINAL]\|[CHAIN OPEN]\|--}`) with FM-20 as the type-violation marker shifts enforcement from vocabulary audit to column-structural constraint; blanks become type violations rather than companion-marker failures |
| V-03 | Lifecycle emphasis | C-23 | Extending the FM catalog with a self-referential FM-18 entry — explicitly stating that any violation cell lacking an FM code IS a FM-18 violation and SHALL carry `[marker \| FM-18]` — closes the coverage loop; no violation cell can silently omit its FM code without generating a new detectable FM-18 violation |
| V-04 | Phrasing register | C-23 + C-24 | Formal Protocol Actor Contract language (Input Domain / Output Specification / Prohibited Actions / Violation Markers) makes input contracts a structured output artifact per role; FM-18 self-reference is explicit in formal invariant notation, making the self-referential loop machine-checkable |
| V-05 | Combined | C-23 + C-24 + C-25 + all prior | Full five-role pipeline: per-role input contracts on all roles (C-24) + enum-typed Chain Status (C-25) + self-referential FM-18 (C-23) + complete foundation from R4 V-01/V-03 + per-phase analytical instruction blocks from R5; each of the 17 aspirational criteria a named design obligation |

---

## V-01 — Role Sequence: Per-Role Input Contracts

**Variation axis**: Role sequence
**Hypothesis**: R4 V-01 achieved 99.6 Gold with Role E being the only role declaring input contracts. C-24 requires EVERY structurally separate role to declare its contracts. V-01 adds an Input Contract block to every role in the 5-role pipeline. FM-19 is added to the catalog as the boundary-violation marker. All other mechanisms from R4 V-01 are carried unchanged.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert operating in five sequential roles. Complete each role in full before beginning the next. Do not merge roles. Do not carry work from a later role into an earlier one.

---

#### FAILURE MODE CATALOG (FM-01 through FM-19)

The nineteen failure modes below define what informal trigger analysis cannot prevent. Each maps to a protocol section.

**Output Cross-Reference Rule**: When an output cell contains a violation, the cell SHALL carry the FM code of the violated requirement: `[marker | FM-NN]`. Reviewers diagnose violations from the output cell alone.

**FM-01 -- Undeclared Denominator**: Enumeration begins from the firing set; silent omissions undetectable. *Response*: Role A pre-scan declares N candidates before condition evaluation.

**FM-02 -- Closed-Set Pathology Scan**: Pathology verdict lacks a denominator. *Response*: Role E reconciliation produces the evidence base for all three pathology verdicts.

**FM-03 -- Vocabulary Drift**: Informal terms accepted. *Response*: Vocabulary contract in Role A; `[NC: actual_value | FM-03]` in violating cells.

**FM-04 -- Branch Amnesia**: Skipped branch silently omitted. *Response*: Both branches required; missing skipped: `[NC: only taken branch | FM-04]`.

**FM-05 -- Latency Blindness**: Tier/latency omitted. *Response*: Tier and latency required per firing row; missing: `[NC: latency missing | FM-05]`.

**FM-06 -- Vocabulary Gap Without Enforcement**: Rules stated but no inline marker. *Response*: `[NC: value | FM-03]` in every violating cell.

**FM-07 -- Verdict Orphaning**: Verdicts lack evidence citations. *Response*: `[INSUFFICIENT: state what evidence is needed and where | FM-07]` on bare assertions.

**FM-08 -- Cascade Truncation**: Chain ends at fixed depth. *Response*: Trace to termination condition, not fixed depth; truncation: `[TRUNCATED | FM-08]`.

**FM-09 -- Prose-Only Cycle Reasoning**: Visual inspection misses length-3+ cycles. *Response*: DFS with `in-path` set; back-edge: `[BACK-EDGE: path | FM-09]`.

**FM-10 -- Denominator Shrinkage**: Conditions evaluated during pre-scan reduce candidate count. *Response*: Pre-scan by entity/field/type only; violation: `[NC: condition evaluated during pre-scan | FM-10]`.

**FM-11 -- Orphaned Chains**: Cascade chains closed without a terminal marker. *Response*: `[TERMINAL]` required on terminal row.

**FM-12 -- Verdict Capture**: Analyst gates own assertions; gate is advisory. *Response*: Role D cannot generate analysis — only approve/flag. Violation: `[FM-12: self-gating; separate evidence role required]`.

**FM-13 -- Tier Blur**: Sync and async in a shared table. *Response*: Separate structural tables; violation: `[NC: wrong-tier trigger in table | FM-13]`.

**FM-14 -- Visual Cycle Inference**: Back-edge detection by eye. *Response*: DFS traversal steps required; skipped: `[FM-14: DFS steps not shown]`.

**FM-15 -- Chain-Open Blindness**: A chain without `[TERMINAL]` detectable only by absence. *Response*: Final row of an unterminated chain SHALL carry `[CHAIN OPEN: CH-NN | FM-15]`. Non-termination is positively flagged, never inferred from absence.

**FM-16 -- Catalog Opacity**: FM codes in preamble only; violations described in prose. *Response*: All output violation cells SHALL carry the FM code inline. Format: `[marker | FM-NN]`. Blank FM slot: structural violation.

**FM-17 -- Reconciliation Capture**: Candidate reconciliation embedded inside gating role or trigger analysis. *Response*: Role E is structurally separate; embedding: `[FM-17: reconciliation must be independent section]`.

**FM-18 -- Catalog Coverage Gap (SELF-REFERENTIAL)**: Any output cell carrying a violation marker without an inline FM code is itself a violation of FM-18. *This entry is self-referential*: if an FM-18 violation omits its own FM code, that omission is also FM-18. *Response*: When a violation cell lacks its FM code, annotate: `[marker | FM-18: FM code required in this cell]`. The catalog achieves coverage completeness when no output cell contains a codeless violation marker. Distinct from FM-16 (which defines the output cross-reference rule); FM-18 names the specific violation generated when FM-16's rule is breached.

**FM-19 -- Role Input Boundary Violation**: A structurally separate role consumes outputs from a role outside its declared input contracts. *Response*: Each role declares its Input Contracts before executing. Violation: `[FM-19: {RoleN} may not consume {RoleM} output — not in input contracts]`. Consumption of undeclared inputs is a structural violation regardless of content correctness.

---

#### ROLE A -- SCANNER

**Input Contracts** (Role A reads from external system context only):
- Trigger registry: external (not a prior-role output)
- Change event scenario: external (not a prior-role output)
- Role A does not consume any prior-role output. All Role A content is externally sourced.

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
| **Condition Branch** | `Taken: [branch name] -- [reason this scenario satisfies it]` AND `Skipped: [branch name] -- [reason this scenario does not satisfy it]` (both required for conditional) \| `No condition` |
| **Input Payload** | `{Entity}.{Field}` pattern required |
| **Output Action** | Must open with: `Sets` \| `Creates` \| `Deletes` \| `Sends email via` \| `Calls HTTP` \| `Starts child flow:` \| `Posts adaptive card to` |
| **Side-Effect Writes** | `{Entity}.{Field} = {value}` or `None` (explicit) |
| **Chain Status** | `[TERMINAL]` \| `[CHAIN OPEN: CH-NN \| FM-15]` \| `--` (non-terminal progress rows) |

Negative examples (non-conforming terms that must be marked):
- Flow Type: `cloud flow`, `automated flow`, `PA flow` → `[NC: value | FM-03]`
- Latency: blank, `"varies"`, `"unknown"` → `[NC: latency missing | FM-05]`
- Condition Branch: `"Condition: True"`, `"Met"`, `"Applies"` → `[NC: only taken branch | FM-04]`
- Input Payload: `"the status field"`, `"current value"` → `[NC: value | FM-03]`
- Output Action: `"processes the record"`, `"sends a notification"` → `[NC: value | FM-03]`

**A-2 -- Candidate Pre-Scan** (FM-10 guard: entity/field/type match only — conditions NOT evaluated)

| CA-ID | Trigger Name | PA Flow Type | Tier | Matching Basis |
|---|---|---|---|---|
| CA-01 | | | | |

**Denominator Count: N** — Every CA-NN must appear in Role E with a disposition. Unresolved entries are structural gaps.

---

#### ROLE B -- TRACER

**Input Contracts** (Role B reads from Role A outputs only):
- A-0: Change scope pin
- A-1: Vocabulary contract (column constraints for Role B tables)
- A-2: Candidate list (CA-NN entries and denominator count)
- Role B may NOT consume Role C, D, or E outputs. Violation: `[FM-19: Role B may not consume Role C/D/E outputs]`

**Task**: Produce the sync and async firing tables. Assign Chain IDs to side-effect writes that could cascade. Do not walk cascade chains — that is Role C's function.

**B-1 -- Sync Firing Table**

Async triggers in this table: `[NC: async trigger in sync table | FM-13]`.

| Seq | CA-Ref | Trigger Name | PA Flow Type | Condition Branch | Input Payload | Output Action | Side-Effect Writes | Latency | Chain ID |
|---|---|---|---|---|---|---|---|---|---|

- **CA-Ref**: CA-NN from A-2. Not in pre-scan: `[NOT IN DENOMINATOR | FM-01]`.
- **Condition Branch**: Both branches required for conditional triggers. Missing skipped: `[NC: only taken branch | FM-04]`.
- **Chain ID**: If Side-Effect Writes could fire a downstream trigger from A-2: assign CH-01, CH-02, etc. Role C walks this chain. No match: `--`.

Sync total: N | Chain IDs assigned: (list)

**B-2 -- Async Firing Table**

Sync triggers in this table: `[NC: sync trigger in async table | FM-13]`.

Same column structure as B-1.

Async total: N

**B-3 -- Tracer Handoff Summary**

- Grand total fires: Sync N + Async N = N
- Chain IDs: CH-NN → root trigger → cascade field
- `[NOT IN DENOMINATOR]` entries: (list or "none")

---

#### ROLE C -- CASCADE CLOSER

**Input Contracts** (Role C reads from Role B outputs only):
- B-1: Sync firing table (chain IDs, side-effect writes)
- B-2: Async firing table (chain IDs, side-effect writes)
- B-3: Tracer handoff summary (chain ID list, grand total)
- Role C may NOT consume Role D or E outputs. Violation: `[FM-19: Role C may not consume Role D/E outputs]`

**Task**: Walk each CH-NN chain to termination. Populate `Chain Status`. Build directed edge set. Apply DFS back-edge detection.

**C-1 -- Cascade Chain Walk**

For each CH-NN:

**Chain CH-NN** | Root: `{trigger name}` | Cascade Field: `{Entity.Field}`

| Step | Trigger Name | Fires Because | Reads | Produces | Side-Effect Writes | Chain Status |
|---|---|---|---|---|---|---|

Column rules:
- **Fires Because**: `{Upstream Trigger} wrote {Entity.Field} = {value}`.
- **Chain Status** (permitted values per A-1 vocab; blank = `[NC: chain status missing | FM-11]`):
  - Terminal row: `[TERMINAL]`
  - Final row where termination not reached: `[CHAIN OPEN: CH-NN | FM-15]`
  - All other rows: `--`

**Termination condition**: A chain terminates when the current step's Side-Effect Writes matches no CA-NN candidate trigger condition, or is `None`. Fixed-depth stop: `[TRUNCATED | FM-08]`.

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

State result after completing traversal:
- `Graph property: DAG` — no back-edges found
- `Graph property: CYCLIC` — list each `[BACK-EDGE]` path

**C-4 -- Closer Handoff Summary**

- Chains walked: N | With `[TERMINAL]`: N | With `[CHAIN OPEN: CH-NN | FM-15]`: N (list)
- Edge set: (from C-2)
- Graph property: DAG | CYCLIC

---

#### ROLE D -- GATEKEEPER

**Input Contracts** (Role D reads from Role B, C, and E outputs only):
- B-3: Grand total fires, chain ID list
- C-4: Chains summary (terminal/open counts), edge set, graph property
- E-1: Disposition table (FLAGGED GAP entries for D-2)
- E-2: Reconciliation totals (FIRED / CONFIRMED ABSENT / FLAGGED GAP counts)
- Role D may NOT consume Role A outputs directly (Role E mediates A-2 access). Role D may NOT generate analysis — only approve or flag. Violation: `[FM-12: self-gating; separate evidence role required]`. Role D may NOT produce reconciliation content — that is Role E's function. Violation: `[FM-17: gatekeeper may not produce reconciliation content]`.

Role D emits only:
- `[EVIDENCE: CONFIRMED -- {specific citation of Role B row or Role C step}]`
- `[INSUFFICIENT: {state what evidence is needed and where} | FM-07]`

**D-1 -- Trigger Storm Gate**

- Grand total from B-3: N | Threshold: > 3 total fires or any `[BACK-EDGE]` in C-4
- B-3 total missing: `[INSUFFICIENT: Role B grand total required before storm verdict | FM-07]`
- Emit: `[EVIDENCE: CONFIRMED -- CLEARED; count = N per B-3; DAG per C-3 traversal]` | `[STORM DETECTED -- count = N; path: {C-4 back-edge}]`

**D-2 -- Missing Triggers Gate** (Role E must complete before D-2 can be issued)

- Role E not yet complete: `[INSUFFICIENT: Role E reconciliation required before missing trigger verdict | FM-07]`
- FLAGGED GAP entries from E-1: (count)
- Emit: `[EVIDENCE: CONFIRMED -- CLEARED; N candidates: N fired, N confirmed absent, 0 gaps per Role E]` | `[MISSING TRIGGER: name -- cause -- risk]` per FLAGGED GAP

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

**Input Contracts** (Role E reads from Role A and Role B outputs only):
- A-2: CA-NN candidate list and denominator count N
- B-1: CA-Ref values and Seq numbers (sync firing table)
- B-2: CA-Ref values and Seq numbers (async firing table)
- Role E may NOT consume Role C, D outputs. Violation: `[FM-19: Role E may not consume Role C/D outputs]`

Role E is structurally independent (FM-17 guard). It does not gate verdicts (Role D). It does not generate trigger analysis (Roles B and C). Its sole output is the denominator reconciliation table. Embedding this section inside Role D or any other role's output: `[FM-17: reconciliation must be independent section]`.

**E-1 -- Denominator Reconciliation Table**

For every CA-NN from Role A:

| CA-ID | Trigger Name | Tier | Disposition | Disposition Evidence |
|---|---|---|---|---|

Disposition codes:
- `FIRED -- Sync, Seq #N` — appeared in B-1 at stated sequence
- `FIRED -- Async, Seq #N` — appeared in B-2 at stated sequence
- `CONFIRMED ABSENT -- {specific condition or filter that prevented firing}` — condition evaluated; candidate excluded
- `FLAGGED GAP -- {reason expected to fire but not in Role B}` — expected to fire; no Role B entry found

Evidence must be specific enough to verify without reading Roles B--D. Generic "see Role B": `[INSUFFICIENT: specific row or condition required | FM-07]`.

**E-2 -- Reconciliation Totals**

- Total candidates (A-2): N
- FIRED: N | CONFIRMED ABSENT: N | FLAGGED GAP: N | Unresolved: N
- Verification: sum SHALL equal N. Mismatch: `[FM-17: N entries unaccounted for]`

**E-3 -- Open Chain Inventory**

- `[CHAIN OPEN: CH-NN | FM-15]` entries from C-4: (list or "none")
- For each: root trigger (CA-ID), cascade field, last step reached
- Cross-reference FLAGGED GAP entries in E-1 where applicable

---

Now receive the scenario and produce the output following this protocol. Apply input contracts at each role boundary. Before advancing from any role, verify that all FM codes are present in violation cells.

---

## V-02 — Output Format: Enum-Typed Chain Status Column

**Variation axis**: Output format
**Hypothesis**: R4 V-02 pre-allocated Chain Status as a two-value enum with blank = structural violation (caught by C-20 companion marker). C-25 distinguishes this: the column itself enforces the enum — blanks are column TYPE violations, not vocabulary violations. V-02 adds a formal Chain Status column type definition with FM-20 as the type-violation marker. Column type enforcement precedes vocabulary audit: a blank or off-enum value triggers FM-20 at column evaluation time, before any vocabulary or companion-marker check.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert operating in five sequential roles. Complete each role in full before beginning the next. Do not merge roles.

---

#### FAILURE MODE CATALOG (FM-01 through FM-20)

**Output Cross-Reference Rule**: Every violation cell SHALL carry its FM code inline: `[marker | FM-NN]`.

**FM-01** -- Undeclared Denominator. *Response*: Role A pre-scan with Denominator Count: N.

**FM-02** -- Closed-Set Pathology Scan. *Response*: Role E reconciliation as evidence base.

**FM-03** -- Vocabulary Drift. *Response*: `[NC: actual_value | FM-03]` in violating cells.

**FM-04** -- Branch Amnesia. *Response*: Both branches required; `[NC: only taken branch | FM-04]`.

**FM-05** -- Latency Blindness. *Response*: `[NC: latency missing | FM-05]`.

**FM-06** -- Vocabulary Gap Without Enforcement. *Response*: Inline marker in every violating cell.

**FM-07** -- Verdict Orphaning. *Response*: `[INSUFFICIENT: cite section + item | FM-07]`.

**FM-08** -- Cascade Truncation. *Response*: Termination condition, not fixed depth; `[TRUNCATED | FM-08]`.

**FM-09** -- Prose-Only Cycle Reasoning. *Response*: DFS with `in-path`; `[BACK-EDGE: path | FM-09]`.

**FM-10** -- Denominator Shrinkage. *Response*: `[NC: condition evaluated during pre-scan | FM-10]`.

**FM-11** -- Orphaned Chains. *Response*: `[TERMINAL]` or `[CHAIN OPEN: CH-NN | FM-15]` required on final row.

**FM-12** -- Verdict Capture. *Response*: `[FM-12: self-gating]`.

**FM-13** -- Tier Blur. *Response*: `[NC: wrong-tier trigger in table | FM-13]`.

**FM-14** -- Visual Cycle Inference. *Response*: `[FM-14: DFS steps not shown]`.

**FM-15** -- Chain-Open Blindness. *Response*: Final row of unterminated chain SHALL carry `[CHAIN OPEN: CH-NN | FM-15]`.

**FM-16** -- Catalog Opacity. *Response*: All violation cells carry FM code inline. Blank FM slot: structural violation.

**FM-17** -- Reconciliation Capture. *Response*: `[FM-17: reconciliation must be independent section]`.

**FM-18** -- Catalog Coverage Gap (SELF-REFERENTIAL). Any violation cell lacking an FM code is itself a violation of FM-18. *Response*: `[marker | FM-18: FM code required in this cell]`. FM-18 is self-referential: an FM-18 violation omitting its code also fires FM-18.

**FM-19** -- Role Input Boundary Violation. *Response*: `[FM-19: role input boundary violation]`.

**FM-20** -- Protocol State Column Type Violation. When a column typed as `ENUM{[TERMINAL] | [CHAIN OPEN: CH-NN | FM-15] | --}` contains a blank or off-enum value, the column type constraint is violated. *Response*: `[TYPE-ERR-CS: ENUM{[TERMINAL]|[CHAIN OPEN: CH-NN | FM-15]|--} required | FM-20]`. This violation is detected at column evaluation time — before vocabulary audit. The column type constraint makes blanks structurally invalid by column definition, not by a downstream marker check.

---

#### ROLE A -- SCANNER

**Task**: Establish analysis boundary. Declare candidate denominator. Define the Chain Status column type.

**A-0 -- Change Scope Pin**

> `{Entity} -- {Field} changed from {old value} to {new value} | context: {initiating action}`

**A-1 -- Vocabulary Contract**

All Role B output cells bound to these terms. Non-conforming: `[NC: actual_value | FM-03]`.

| Column | Permitted Values |
|---|---|
| **PA Flow Type** | `Automated -- Dataverse` \| `Automated -- SharePoint` \| `Automated -- HTTP` \| `Instant` \| `Scheduled` |
| **Tier** | `Sync` \| `Async` |
| **Latency (Sync)** | `Inline (blocks transaction)` |
| **Delay Estimate (Async)** | `~N min [standard\|premium] tier` (N required) |
| **Condition Branch** | `Taken: [branch] -- [reason]` AND `Skipped: [branch] -- [reason]` \| `No condition` |
| **Input Payload** | `{Entity}.{Field}` |
| **Output Action** | Opens with: `Sets` \| `Creates` \| `Deletes` \| `Sends email via` \| `Calls HTTP` \| `Starts child flow:` \| `Posts adaptive card to` |
| **Side-Effect Writes** | `{Entity}.{Field} = {value}` or `None` |

Negative examples:
- Flow Type: `cloud flow`, `automated flow` → `[NC: value | FM-03]`
- Latency: blank, `"varies"` → `[NC: latency missing | FM-05]`
- Branch: `"Condition: True"` → `[NC: only taken branch | FM-04]`
- Output Action: `"updates the status"` → `[NC: value | FM-03]`

**A-2 -- Chain Status Column Type Definition**

The Chain Status column in all Role C cascade tables is defined as a typed protocol column:

```
COLUMN: Chain Status
TYPE: ENUM{[TERMINAL] | [CHAIN OPEN: CH-NN | FM-15] | --}

Value semantics:
  [TERMINAL]              — final row: chain resolved; no downstream triggers fire
  [CHAIN OPEN: CH-NN | FM-15] — final row: chain not resolved; cascade may be incomplete
  --                      — non-final progress row: chain continues

Type constraint: every cell in this column must contain one of the three typed values.
  - Blank cells: COLUMN TYPE VIOLATION (detected at column evaluation time, before vocabulary audit)
    Marker: [TYPE-ERR-CS: ENUM{[TERMINAL]|[CHAIN OPEN: CH-NN | FM-15]|--} required | FM-20]
  - The type constraint is enforced by the column definition — not by a downstream companion-marker rule.
  - A final chain row carrying `--` is also a type violation: `--` is valid only for non-final steps.
```

**A-3 -- Candidate Pre-Scan** (FM-10 guard: entity/field/type only — conditions NOT evaluated)

| CA-ID | Trigger Name | PA Flow Type | Tier | Matching Basis |
|---|---|---|---|---|
| CA-01 | | | | |

**Denominator Count: N** — Every CA-NN must appear in Role E.

---

#### ROLE B -- TRACER

**Input Contracts**: Role A outputs only (A-0 scope pin, A-1 vocabulary, A-2 chain status type definition, A-3 candidate list).

**Task**: Produce sync and async firing tables. Assign Chain IDs to side-effect writes that could cascade.

**B-1 -- Sync Firing Table**

Wrong-tier: `[NC: async trigger in sync table | FM-13]`

| Seq | CA-Ref | Trigger Name | PA Flow Type | Condition Branch | Input Payload | Output Action | Side-Effect Writes | Latency | Chain ID |
|---|---|---|---|---|---|---|---|---|---|

Sync total: N | Chain IDs assigned: (list)

**B-2 -- Async Firing Table**

Wrong-tier: `[NC: sync trigger in async table | FM-13]`

Same columns as B-1, except Latency → Delay Estimate.

Async total: N

**B-3 -- Handoff Summary**: Grand total N | Chain IDs: (list) | `[NOT IN DENOMINATOR]` entries: (list or none)

---

#### ROLE C -- CASCADE CLOSER

**Input Contracts**: Role B outputs only (B-1, B-2, B-3 chain IDs).

**Task**: Walk each CH-NN chain to termination. Populate Chain Status column per the type definition in A-2. Build directed edge set. Apply DFS back-edge detection.

**C-1 -- Cascade Chain Walk**

**Chain CH-NN** | Root: `{trigger}` | Cascade Field: `{Entity.Field}`

| Step | Trigger Name | Fires Because | Reads | Produces | Side-Effect Writes | Chain Status |
|---|---|---|---|---|---|---|

**Chain Status enforcement** (per A-2 column type definition):
- Every cell must contain one of: `[TERMINAL]`, `[CHAIN OPEN: CH-NN | FM-15]`, or `--`
- Blank cells: `[TYPE-ERR-CS: ENUM{[TERMINAL]|[CHAIN OPEN: CH-NN | FM-15]|--} required | FM-20]`
- Final chain row carrying `--`: also `[TYPE-ERR-CS: -- invalid at chain terminus | FM-20]`

**Termination condition**: No CA-NN candidate fires on current step's Side-Effect Writes field, or Side-Effect Writes = `None`. Fixed-depth stop: `[TRUNCATED | FM-08]`.

**C-2 -- Directed Edge Set** (all side-effect writes from Roles B and C)

**C-3 -- DFS Back-Edge Detection** (FM-14 guard: DFS traversal steps required)

```
Initialize: visited = {}  |  in-path = {}
For each trigger T not yet in visited:
  1. Add T to in-path
  2. For each downstream U:
     a. U in in-path: [BACK-EDGE: path | FM-09]
     b. U not in visited: recurse
  3. Remove T from in-path; add T to visited
```

Graph property: DAG | CYCLIC

**C-4 -- Closer Handoff Summary**: Chains N | TERMINAL N | CHAIN OPEN N (list) | Edge set | Graph property

---

#### ROLE D -- GATEKEEPER

**Input Contracts**: Role B (B-3), Role C (C-4), Role E (E-1, E-2). Cannot generate new analysis: `[FM-12]`. Cannot produce reconciliation: `[FM-17]`.

Emits only `[EVIDENCE: CONFIRMED -- {citation}]` or `[INSUFFICIENT: {what is needed} | FM-07]`.

**D-1 -- Trigger Storm Gate**: B-3 grand total vs. threshold > 3 | Re-entry via back-edges from C-3.

**D-2 -- Missing Triggers Gate** (Role E must complete first): FLAGGED GAP count from E-1.

**D-3 -- Circular Triggers Gate**: Graph property from C-4; DFS not done: `[INSUFFICIENT: DFS steps required | FM-14]`.

**D-4 -- Risk-Ranked Pathology Summary**

| Rank | Pathology | Risk Level | Operational Impact | Mitigation |
|---|---|---|---|---|

---

#### ROLE E -- RECONCILIATION AUDITOR

**Input Contracts**: Role A (A-3 candidate list) and Role B (B-1, B-2 CA-Refs) only. May NOT consume Role C, D outputs: `[FM-19: Role E input boundary violation]`.

Role E is structurally independent (FM-17). Sole output: denominator reconciliation. Embedding inside any other role: `[FM-17: reconciliation must be independent section]`.

**E-1 -- Denominator Reconciliation Table**

| CA-ID | Trigger Name | Tier | Disposition | Evidence |
|---|---|---|---|---|

Codes: `FIRED -- Sync/Async, Seq #N` | `CONFIRMED ABSENT -- {condition}` | `FLAGGED GAP -- {reason}`

**E-2 -- Totals**: FIRED: N | ABSENT: N | FLAGGED GAP: N | Unresolved: N | Sum = N ✓

**E-3 -- Open Chain Inventory**: `[CHAIN OPEN]` entries from C-4 cross-referenced to E-1 FLAGGED GAP entries.

---

Now receive the scenario and produce the output. Apply Chain Status type constraints from A-2 throughout Role C.

---

## V-03 — Lifecycle Emphasis: Self-Referential FM Catalog

**Variation axis**: Lifecycle emphasis
**Hypothesis**: R4 V-03 achieved 99.6 Gold with FM-16 "self-enforces" and the strongest C-11 (explicit negative examples). C-23 requires the self-referential rule to be a named FM catalog entry: FM-18. The key addition: FM-18 explicitly states that a violation cell lacking its FM code generates a new FM-18 violation on that same cell, making the catalog coverage rule mechanically verifiable and self-closing. V-03 extends the R4 V-03 FM catalog to FM-18, preserving all vocabulary negative examples.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. Execute the six-section protocol below. Sections run in order. Each section produces a structured output before the next begins.

---

#### FAILURE MODE CATALOG (FM-01 through FM-18)

**Output Cross-Reference Rule**: Every violation marker in an output cell SHALL include the FM code inline. Format: `[marker | FM-NN]`. The FM code IS the cross-reference — no preamble lookup required. FM-18 governs the coverage completeness of this rule.

**Term Set A — PA Flow Type** [TS-A]
| Code | Term | When to Use |
|---|---|---|
| A-01 | `Automated -- Dataverse` | Triggered by Dataverse table row event |
| A-02 | `Automated -- SharePoint` | Triggered by SharePoint list item event |
| A-03 | `Automated -- HTTP` | Triggered by inbound HTTP request |
| A-04 | `Instant` | Manually triggered |
| A-05 | `Scheduled` | Triggered by recurrence schedule |

Non-conforming: `cloud flow` | `automated flow` | `PA flow` | `button flow` → `[NC: value | FM-03]`

**Term Set B — Execution Tier + Latency** [TS-B]
| Code | Term | Latency Semantics |
|---|---|---|
| B-01 | `Sync` | `Inline (blocks transaction)` — Latency column value |
| B-02 | `Async` | `~N min [standard\|premium] tier` — Delay Estimate column value |

Non-conforming latency: blank | `"varies"` | `"unknown"` | `"fast"` → `[NC: latency missing | FM-05]`

**Term Set C — Input/Output Payload Pattern** [TS-C]
- Input: `{TableName}.{ColumnName}` — e.g., `Request.Status`, `cr123_approval.ownerid`
- Output: must open with `Sets` | `Creates` | `Deletes` | `Sends email via` | `Calls HTTP` | `Starts child flow:` | `Posts adaptive card to`
- Non-conforming input: `"the status field"`, `"record status"` → `[NC: value | FM-03]`
- Non-conforming output: `"processes the record"`, `"sends a notification"` → `[NC: value | FM-03]`

**Term Set D — Condition Branch Form** [TS-D]
- Required: `Taken: [branch] -- [reason scenario satisfies it]` AND `Skipped: [branch] -- [reason scenario does not satisfy it]`
- Non-conforming: `"Condition: True"` | `"Met"` | `"Applies"` → `[NC: only taken branch | FM-04]`

**Term Set E — Pathology Form** [TS-E]
| Code | Term |
|---|---|
| E-01 | `Trigger Storm` |
| E-02 | `Missing Trigger` |
| E-03 | `Circular Trigger` |
| E-99 | `None` |

**Term Set F — Chain Status** [TS-F]
| Value | Meaning |
|---|---|
| `[TERMINAL]` | Terminal row: chain resolved; no further downstream triggers |
| `[CHAIN OPEN: CH-NN \| FM-15]` | Final row: chain not resolved; FM-15 companion marker fires |
| `--` | Non-terminal progress row |
Non-conforming: blank → `[NC: chain status missing | FM-11]`

---

**FM-01** -- Undeclared Denominator: Triggers enumerated from firing set; silent omissions leave no gap. *Expected*: Section 1 pre-scan with explicit count N. *Marker*: `[NOT IN DENOMINATOR | FM-01]`.

**FM-02** -- Closed-Set Pathology Scan: Verdicts lack denominator evidence. *Expected*: Section 4 reconciliation produces evidence base. *Marker*: `[INSUFFICIENT: denominator reconciliation missing | FM-02]`.

**FM-03** -- Vocabulary Drift: Informal terms pass review. *Expected*: TS-A through TS-E in all constrained columns. *Marker*: `[NC: actual_value | FM-03]`.

**FM-04** -- Branch Amnesia: Skipped branch silently omitted. *Expected*: Both branches per TS-D. *Marker*: `[NC: only taken branch | FM-04]`.

**FM-05** -- Latency Blindness: Tier/latency omitted or informal. *Expected*: TS-B latency in every row. *Marker*: `[NC: latency missing | FM-05]`.

**FM-06** -- Vocabulary Gap Without Enforcement: Rules stated but no inline marker applied. *Expected*: Inline `[NC: ... | FM-NN]` in every violating cell. *Marker*: `[FM-06: vocabulary rule stated without enforcement marker]`.

**FM-07** -- Verdict Orphaning: Verdicts lack evidence citations. *Expected*: Citation to specific section + item number. *Marker*: `[INSUFFICIENT: cite section + item | FM-07]`.

**FM-08** -- Cascade Truncation: Chain ends at fixed depth without termination condition. *Expected*: Trace until no CA-NN candidate fires on Side-Effect Writes. *Marker*: `[TRUNCATED | FM-08]`.

**FM-09** -- Prose-Only Cycle Reasoning: Cycles identified visually; length-3+ cycles may be missed. *Expected*: DFS traversal with `in-path` set. *Marker*: `[BACK-EDGE: T -> ... -> T | FM-09]`.

**FM-10** -- Denominator Shrinkage: Condition evaluated during pre-scan reduces candidate count. *Expected*: Section 1 scan by entity/field/type only. *Marker*: `[NC: condition evaluated during pre-scan | FM-10]`.

**FM-11** -- Orphaned Chains: Cascade chains closed without terminal marker. *Expected*: `[TERMINAL]` or `[CHAIN OPEN: CH-NN | FM-15]` per TS-F on final row. *Marker*: `[NC: chain status missing | FM-11]`.

**FM-12** -- Verdict Capture: Analyst gates own assertions. *Expected*: Section 6 verdict gating role cannot generate analysis. *Marker*: `[FM-12: self-gating; separate evidence section required]`.

**FM-13** -- Tier Blur: Sync and async in shared table. *Expected*: Section 2 (Sync) and Section 3 (Async) structurally separate. *Marker*: `[NC: wrong-tier trigger in table | FM-13]`.

**FM-14** -- Visual Cycle Inference: Back-edge detection by eye. *Expected*: DFS traversal steps shown explicitly. *Marker*: `[FM-14: DFS steps not shown]`.

**FM-15** -- Chain-Open Blindness: Unterminated chain detectable only by absence of `[TERMINAL]`. *Expected*: Final row of unterminated chain carries `[CHAIN OPEN: CH-NN | FM-15]`. Non-termination positively flagged. *Marker*: `[CHAIN OPEN: CH-NN | FM-15]` on final unterminated row.

**FM-16** -- Catalog Opacity: FM codes in preamble only; output cell violations described in prose; diagnosis requires cross-section reading. *Expected*: Every violation cell carries FM code inline per Output Cross-Reference Rule. *Marker*: `[marker | FM-NN]` format required; blank FM slot is structural violation of FM-18.

**FM-17** -- Reconciliation Capture: Candidate reconciliation embedded inside verdict gating or trigger analysis sections. *Expected*: Section 4 is structurally separate with own heading and input contracts. *Marker*: `[FM-17: reconciliation must be independent section]`.

**FM-18 -- Catalog Coverage Gap (SELF-REFERENTIAL)**: This entry closes the FM catalog's own coverage loop. Any output cell that carries a violation marker without an inline FM code is itself a violation of FM-18. *This rule is recursive*: if a cell contains `[some marker]` without an FM code, the corrected form is `[some marker | FM-18: FM code required in this cell]`. If the FM-18 correction itself omits the FM code, that too is a FM-18 violation. The catalog achieves coverage completeness when no output cell contains a codeless violation marker — every violation either carries its own FM code or carries FM-18. *Expected behavior*: a reviewer inspecting output tables can verify catalog coverage mechanically: any codeless violation marker is immediately a FM-18 violation, requiring no cross-section lookup. *Marker*: `[original-marker | FM-18: FM code required in this cell]`. Distinct from FM-16 (which states the output cross-reference rule); FM-18 names the specific failure mode generated when FM-16's rule is breached, making the breach itself diagnosable by code.

---

#### SECTION 1 — CANDIDATE PRE-SCAN

Enumerate all candidates whose flow type, entity filter, and field filter could match the change event. Do NOT evaluate conditions (FM-10 guard).

| Candidate ID | Flow Name | Flow Type [TS-A] | Trigger Condition | Candidate Basis |
|---|---|---|---|---|
| CP-01 | | | | |

**Candidate Count**: N — Every CP-NN must be resolved in Section 4.

---

#### SECTION 2 — INVESTIGATION CASES (Open)

Open before enumeration. Cases remain OPEN until Section 5.

**Case E-01 — Trigger Storm**
*Charge*: More than 3 distinct trigger executions, or re-entry via side-effect chain?
*Evidence Standard*: (a) Firing count (Sections 2–3 totals by name); (b) re-entry check for non-None Side Effects against Section 1 candidates; (c) count ≤ 3 / > 3 and re-entry found / not found.
*Status*: OPEN

**Case E-02 — Missing Triggers**
*Charge*: Expected automation absent from firing set?
*Evidence Standard*: (a) Section 1 candidate count; (b) Section 4 per-candidate disposition (FIRED / ABSENT / GAP); (c) sum = Section 1 count; (d) FLAGGED GAP count = 0 to clear.
*Status*: OPEN

**Case E-03 — Circular Triggers**
*Charge*: Any trigger writing a field that creates a directed cycle?
*Evidence Standard*: (a) All field writes from Sections 2–3 in `{Entity}.{Field}` syntax; (b) directed graph edge set; (c) graph property DAG or CYCLIC with DFS traversal steps.
*Status*: OPEN

---

#### SECTION 3 — TRIGGER INVENTORY (Sync | Async — Structural Split)

**Sync Tier** (B-01: executes inline; failure rolls back transaction)

Wrong-tier: `[NC: async trigger in sync table | FM-13]`

| Seq | CP-Ref | Flow Name | Flow Type [TS-A] | Condition Branch [TS-D] | Input Payload [TS-C] | Output Action [TS-C] | Side-Effect Writes [TS-C] | Latency [TS-B] |
|---|---|---|---|---|---|---|---|---|

Sync total: N

**Async Tier** (B-02: fire-and-forget; does not block transaction)

Wrong-tier: `[NC: sync trigger in async table | FM-13]`

| Seq | CP-Ref | Flow Name | Flow Type [TS-A] | Condition Branch [TS-D] | Input Payload [TS-C] | Output Action [TS-C] | Side-Effect Writes [TS-C] | Delay Estimate [TS-B] |
|---|---|---|---|---|---|---|---|---|

Async total: N

**Cascade Chains** — For each Chain CH-NN assigned in Sections 2–3:

**Chain CH-NN** | Root: `{flow}` | Cascade Field: `{Entity.Field}`

| Step | Flow Name | Fires Because | Input Payload [TS-C] | Output Action [TS-C] | Side-Effect Writes [TS-C] | Chain Status [TS-F] |
|---|---|---|---|---|---|---|

Chain Status rules (TS-F): `[TERMINAL]` on resolved final row | `[CHAIN OPEN: CH-NN | FM-15]` on unresolved final row | `--` on progress rows | blank = `[NC: chain status missing | FM-11]`

Termination condition: Side-Effect Writes = `None` or no CP-NN fires on the written field. Fixed-depth stop: `[TRUNCATED | FM-08]`.

**Directed Edge Set** (all side-effect writes from Sections 2–3 + cascade chains):
```
{Flow A} -> writes {Entity.Field} -> fires {Flow B}
{Flow C} -> writes {Entity.Field} -> [NO DOWNSTREAM]
```

**DFS Back-Edge Detection** (FM-14 guard: traversal steps required; do not replace with visual inspection):
```
Initialize: visited = {}  |  in-path = {}
For each trigger T not yet in visited:
  1. Add T to in-path
  2. For each downstream U:
     a. U in in-path: [BACK-EDGE: T -> ... -> U -> T | FM-09]
     b. U not visited: recurse
  3. Remove T from in-path; mark T visited
```
Graph property: DAG | CYCLIC

---

#### SECTION 4 — DENOMINATOR RECONCILIATION (Structurally Independent — FM-17 Guard)

This section is structurally separate from Sections 3 and 5. It does not gate verdicts (Section 5). It does not generate trigger analysis (Section 3). Input contracts: Section 1 (candidate list) and Sections 2–3 (CP-Ref values and Seq numbers). Embedding inside Section 3 or Section 5: `[FM-17: reconciliation must be independent section]`.

| Candidate ID | Flow Name | Tier [TS-B] | Disposition | Evidence |
|---|---|---|---|---|

Codes: `FIRED -- Sync/Async, Seq #N` | `CONFIRMED ABSENT -- {condition}` | `FLAGGED GAP -- {reason expected but missing}`

Totals: FIRED N | ABSENT N | FLAGGED GAP N | Unresolved N | Sum = N (must equal Section 1 count)

---

#### SECTION 5 — VERDICT GATING

This section cannot generate new analysis — only approve or flag findings from Sections 3–4. Emits only:
- `[EVIDENCE: CONFIRMED -- {specific citation}]`
- `[INSUFFICIENT: {what is needed and where} | FM-07]`

**5-A — Trigger Storm**: Count from Section 3 totals | Re-entry from edge set analysis.

**5-B — Missing Triggers**: FLAGGED GAP count from Section 4 (Section 4 must complete first).

**5-C — Circular Triggers**: Graph property from Section 3 DFS (DFS steps must be present per FM-14).

---

#### SECTION 6 — RISK-RANKED SUMMARY

| Rank | Pathology [TS-E] | Risk Level | Operational Impact | Mitigation |
|---|---|---|---|---|

Critical first. All cleared: single row, `E-99 None`.

---

Now receive the scenario and produce the output following this protocol.

---

## V-04 — Phrasing Register: Formal Protocol Actor Contracts

**Variation axis**: Phrasing register
**Hypothesis**: Expressing each role as a "Protocol Actor Contract" — with formal Input Domain, Output Specification, Prohibited Actions, and Violation Markers — makes input contracts (C-24) a structured first-class output artifact rather than an inline prose constraint. The FM catalog uses formal invariant notation with FM-18 self-reference made explicit as a logical closure rule, making the self-referential loop checkable without prose interpretation.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. Execute the Formal Trigger Analysis Protocol below. Each Protocol Actor is defined by a contract specifying its input domain, output specification, prohibited actions, and violation markers. Execute actors in sequence. Do not violate actor contracts.

---

#### PROTOCOL INVARIANT REGISTRY (PIR)

Each invariant maps a requirement to its detection trigger, expected behavior, and violation marker.

**PIR-01** | *Invariant*: Trigger enumeration begins only after a denominator is declared. | *Trigger*: Enumeration without prior pre-scan. | *Marker*: `[NOT IN DENOMINATOR | PIR-01]`.

**PIR-02** | *Invariant*: Pathology verdicts require denominator evidence. | *Trigger*: Verdict issued without reconciliation section complete. | *Marker*: `[INSUFFICIENT: reconciliation required before verdict | PIR-02]`.

**PIR-03** | *Invariant*: Output cells in constrained columns use only declared vocabulary terms. | *Trigger*: Non-declared term in constrained column. | *Marker*: `[NC: actual_value | PIR-03]`.

**PIR-04** | *Invariant*: Conditional triggers document both the taken and the skipped branch with scenario-specific reasons. | *Trigger*: Branch column contains only the taken branch. | *Marker*: `[NC: only taken branch | PIR-04]`.

**PIR-05** | *Invariant*: Each trigger row carries a latency annotation appropriate to its tier. | *Trigger*: Latency cell blank or non-conforming. | *Marker*: `[NC: latency missing | PIR-05]`.

**PIR-06** | *Invariant*: Every vocabulary rule is enforced by an inline marker, not stated without enforcement. | *Trigger*: Vocabulary rule stated in preamble but no marker applied to violating cell. | *Marker*: `[PIR-06: vocabulary rule stated without enforcement]`.

**PIR-07** | *Invariant*: Verdict cells cite the specific evidence source that justifies the verdict. | *Trigger*: Verdict cell lacks traceable citation. | *Marker*: `[INSUFFICIENT: cite section + item | PIR-07]`.

**PIR-08** | *Invariant*: Cascade chains trace to a termination condition, not a fixed depth. | *Trigger*: Chain stops at row N without checking if downstream triggers fire. | *Marker*: `[TRUNCATED | PIR-08]`.

**PIR-09** | *Invariant*: Cycle detection uses DFS with an `in-path` set. Visual inspection is not permitted. | *Trigger*: Cycle detection by visual inspection or prose reasoning. | *Marker*: `[BACK-EDGE: path | PIR-09]` (back-edges); `[PIR-09: DFS steps required]` (visual inspection).

**PIR-10** | *Invariant*: Pre-scan evaluates entity/field/type match only — conditions are not evaluated. | *Trigger*: Condition evaluated during pre-scan, reducing denominator. | *Marker*: `[NC: condition evaluated during pre-scan | PIR-10]`.

**PIR-11** | *Invariant*: Each cascade chain's final row carries a terminal state marker. | *Trigger*: Final chain row without `[TERMINAL]` or `[CHAIN OPEN]`. | *Marker*: `[NC: chain status missing | PIR-11]`.

**PIR-12** | *Invariant*: The verdict gating actor cannot generate new analysis. | *Trigger*: Verdict gating actor produces content that is not `[EVIDENCE: CONFIRMED]` or `[INSUFFICIENT]`. | *Marker*: `[PIR-12: verdict actor may not generate analysis]`.

**PIR-13** | *Invariant*: Sync and async triggers occupy structurally separate tables. | *Trigger*: Trigger appears in wrong-tier table. | *Marker*: `[NC: wrong-tier trigger | PIR-13]`.

**PIR-14** | *Invariant*: DFS traversal steps must appear in output — not summary only. | *Trigger*: Back-edge analysis result stated without showing traversal steps. | *Marker*: `[PIR-14: DFS traversal steps not shown]`.

**PIR-15** | *Invariant*: Unterminated chain non-termination is positively flagged, not inferred from absence of `[TERMINAL]`. | *Trigger*: Final row of unterminated chain lacks companion marker. | *Marker*: `[CHAIN OPEN: CH-NN | PIR-15]`.

**PIR-16** | *Invariant*: Every violation in an output cell carries its PIR code inline. | *Trigger*: Violation cell describes failure in prose without PIR code. | *Marker*: `[marker | PIR-NN]` format required.

**PIR-17** | *Invariant*: Denominator reconciliation occupies a structurally independent section. | *Trigger*: Reconciliation embedded inside verdict gating or trigger analysis actors. | *Marker*: `[PIR-17: reconciliation must be independent actor output]`.

**PIR-18 (SELF-REFERENTIAL CLOSURE)** | *Invariant*: The Protocol Invariant Registry is coverage-complete — every violation cell must carry a PIR code. | *Formal closure rule*: If any output cell carries a violation marker without a PIR code, that omission is itself a violation of PIR-18. The corrected form: `[original-marker | PIR-18: PIR code required in this cell]`. *Self-reference*: PIR-18 applies to itself — a PIR-18 violation cell that omits its PIR code is also PIR-18. The registry achieves coverage completeness when, for any output cell, either (a) the PIR code is present, or (b) PIR-18 fires and makes the absence visible. *Trigger*: Violation cell without PIR code. *Marker*: `[original-marker | PIR-18: PIR code required]`.

**PIR-19 (ROLE INPUT BOUNDARY)** | *Invariant*: Each Protocol Actor consumes only outputs declared in its Input Domain contract. Consumption of undeclared inputs is a boundary violation regardless of content correctness. | *Trigger*: Actor consumes output from an actor not listed in its Input Domain. | *Marker*: `[PIR-19: {Actor} may not consume {Source} output — not in input domain]`.

---

#### PROTOCOL ACTOR CONTRACTS

---

**ACTOR: SCANNER**

```
INPUT DOMAIN:
  - External: change event scenario (entity, field, old/new values)
  - External: trigger registry (list of all flows configured in the environment)
  - No prior-actor output consumed.

OUTPUT SPECIFICATION:
  - Scanner Output A: Change scope pin (entity, field, direction)
  - Scanner Output B: Vocabulary contract (term sets for all constrained columns)
  - Scanner Output C: Candidate pre-scan table (CP-NN entries, denominator count N)

PROHIBITED ACTIONS:
  - Evaluate conditions or determine firing outcomes
  - Reference any prior-actor output (there are none)

VIOLATION MARKER (input boundary): N/A — Scanner has no prior actors
```

**ACTOR: TRACER**

```
INPUT DOMAIN:
  - Scanner Output A: Change scope pin
  - Scanner Output B: Vocabulary contract
  - Scanner Output C: Candidate list (CP-NN, count N)
  [May NOT consume Cascade Closer, Gatekeeper, or Auditor outputs — PIR-19]

OUTPUT SPECIFICATION:
  - Tracer Output A: Sync Firing Table (Seq, CP-Ref, flow name, type, branches, payload,
                     output action, side effects, latency, chain ID)
  - Tracer Output B: Async Firing Table (same columns, Delay Estimate in place of Latency)
  - Tracer Output C: Handoff Summary (grand total, chain ID list)

PROHIBITED ACTIONS:
  - Walk cascade chains (Cascade Closer's function)
  - Evaluate conditions not bound to the specific change event
  - Consume Cascade Closer, Gatekeeper, or Auditor outputs

VIOLATION MARKER (input boundary): [PIR-19: Tracer may not consume {source} output]
```

**ACTOR: CASCADE CLOSER**

```
INPUT DOMAIN:
  - Tracer Output A: Sync firing table (chain IDs, side-effect writes)
  - Tracer Output B: Async firing table (chain IDs, side-effect writes)
  - Tracer Output C: Chain ID list
  [May NOT consume Gatekeeper or Auditor outputs — PIR-19]

OUTPUT SPECIFICATION:
  - Cascade Closer Output A: Per-chain cascade walk tables (Step, Trigger, Fires Because,
                              Reads, Produces, Side-Effect Writes, Chain Status [PIR-11/PIR-15])
  - Cascade Closer Output B: Directed edge set
  - Cascade Closer Output C: DFS back-edge detection (traversal steps + graph property)
  - Cascade Closer Output D: Handoff Summary (chains N, terminal N, open N, edge set, graph property)

PROHIBITED ACTIONS:
  - Walk chains not assigned a Chain ID in Tracer output
  - Substitute visual inspection for DFS traversal [PIR-14]
  - Stop chains at fixed depth [PIR-08]
  - Consume Gatekeeper or Auditor outputs

VIOLATION MARKERS:
  - Chain status missing: [NC: chain status missing | PIR-11]
  - Unterminated final row: [CHAIN OPEN: CH-NN | PIR-15]
  - Fixed-depth stop: [TRUNCATED | PIR-08]
  - Back-edge: [BACK-EDGE: path | PIR-09]
  - Input boundary: [PIR-19: Cascade Closer may not consume {source} output]
```

**ACTOR: GATEKEEPER**

```
INPUT DOMAIN:
  - Tracer Output C: Grand total fires, NOT-IN-DENOMINATOR list
  - Cascade Closer Output C: DFS graph property
  - Cascade Closer Output D: Handoff summary (chain terminal/open counts)
  - Auditor Output A: Disposition table (FLAGGED GAP entries for missing trigger verdict)
  - Auditor Output B: Reconciliation totals (FIRED / ABSENT / GAP counts)
  [May NOT consume Scanner Output C directly — Auditor mediates denominator access — PIR-19]

OUTPUT SPECIFICATION:
  - For each pathology class: [EVIDENCE: CONFIRMED -- {citation}] OR [INSUFFICIENT: {needed} | PIR-07]
  - Risk-ranked pathology summary table (after all three classes resolved)

PROHIBITED ACTIONS:
  - Generate new analysis content [PIR-12]
  - Produce reconciliation content (Auditor's function) [PIR-17]
  - Issue missing-trigger verdict before Auditor completes [PIR-02]

VIOLATION MARKERS:
  - Self-gating: [PIR-12: verdict actor may not generate analysis]
  - Reconciliation in gatekeeper: [PIR-17: reconciliation must be independent actor output]
  - Bare assertion: [INSUFFICIENT: cite section + item | PIR-07]
  - Input boundary: [PIR-19: Gatekeeper may not consume {source} output]
```

**ACTOR: AUDITOR**

```
INPUT DOMAIN:
  - Scanner Output C: CP-NN candidate list and count N
  - Tracer Output A: CP-Ref values and Seq numbers from sync table
  - Tracer Output B: CP-Ref values and Seq numbers from async table
  [May NOT consume Cascade Closer or Gatekeeper outputs — PIR-19]

OUTPUT SPECIFICATION:
  - Auditor Output A: Denominator reconciliation table (CP-ID, name, tier, disposition, evidence)
  - Auditor Output B: Reconciliation totals (FIRED / ABSENT / GAP / Unresolved; sum verification)
  - Auditor Output C: Open chain inventory (CHAIN OPEN entries from Cascade Closer Output D)

PROHIBITED ACTIONS:
  - Gate verdicts (Gatekeeper's function) [PIR-12]
  - Generate trigger analysis (Tracer/Cascade Closer functions) [PIR-17]
  - Be embedded inside Gatekeeper or any other actor output [PIR-17]

VIOLATION MARKERS:
  - Self-gating: [PIR-12]
  - Embedded in other actor: [PIR-17: reconciliation must be independent actor output]
  - Generic evidence: [INSUFFICIENT: specific row or condition required | PIR-07]
  - Input boundary: [PIR-19: Auditor may not consume {source} output]
```

---

#### EXECUTION INSTRUCTIONS

Execute actors in order: SCANNER → TRACER → CASCADE CLOSER → AUDITOR → GATEKEEPER.

Before executing each actor, state: "Executing [ACTOR NAME]. Input domain: [list consumed inputs]."

After each actor, verify: (a) all output specification items produced; (b) no prohibited actions taken; (c) all violation cells carry PIR codes.

Apply PIR-18 throughout: any violation cell lacking a PIR code generates `[original-marker | PIR-18: PIR code required]`.

Now receive the scenario and execute the protocol.

---

## V-05 — Combined: All Three New Criteria + Full Stack

**Variation axis**: Combined
**Hypothesis**: Full five-role pipeline with all three new criteria simultaneously:
- C-23: Self-referential FM-18 in the catalog (every violation cell without a code generates FM-18)
- C-24: Per-role input contracts on ALL 5 roles (FM-19 as boundary marker)
- C-25: Enum-typed Chain Status column with FM-20 as type-violation marker

Plus complete foundation: vocabulary negative examples (C-11), evidence gates (C-12), cascade termination (C-13), trigger graph (C-14), denominator pre-scan (C-15), terminal markers (C-16), role-separated gating (C-17), tier split (C-18), DFS back-edge (C-19), companion marker (C-20), FM catalog (C-21), independent reconciliation (C-22). Per-phase analytical instruction blocks from R5 V-05 to bind analytical work to each role. Each of the 17 aspirational criteria is a named design obligation.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert operating in five sequential roles. Complete each role in full before beginning the next. Do not merge roles. Do not carry work from a later role into an earlier one.

---

#### FAILURE MODE CATALOG (FM-01 through FM-20)

**Output Cross-Reference Rule**: Every output cell containing a violation SHALL carry the FM code inline: `[marker | FM-NN]`. FM-18 governs the completeness of this rule.

**FM-01** -- Undeclared Denominator. *Response*: Role A pre-scan with Denominator Count N. *Marker*: `[NOT IN DENOMINATOR | FM-01]`.

**FM-02** -- Closed-Set Pathology Scan. *Response*: Role E reconciliation as evidence base. *Marker*: `[INSUFFICIENT: reconciliation required | FM-02]`.

**FM-03** -- Vocabulary Drift. *Response*: Vocabulary contract; `[NC: actual_value | FM-03]`.

**FM-04** -- Branch Amnesia. *Response*: Both branches; `[NC: only taken branch | FM-04]`.

**FM-05** -- Latency Blindness. *Response*: Latency per row; `[NC: latency missing | FM-05]`.

**FM-06** -- Vocabulary Gap Without Enforcement. *Response*: Inline marker every violating cell. *Marker*: `[FM-06: rule stated without enforcement]`.

**FM-07** -- Verdict Orphaning. *Response*: `[INSUFFICIENT: cite section + item | FM-07]`.

**FM-08** -- Cascade Truncation. *Response*: Termination condition not fixed depth; `[TRUNCATED | FM-08]`.

**FM-09** -- Prose-Only Cycle Reasoning. *Response*: DFS with `in-path`; `[BACK-EDGE: path | FM-09]`.

**FM-10** -- Denominator Shrinkage. *Response*: `[NC: condition evaluated during pre-scan | FM-10]`.

**FM-11** -- Orphaned Chains. *Response*: `[TERMINAL]` or `[CHAIN OPEN: CH-NN | FM-15]` on final row; `[NC: chain status missing | FM-11]` if absent.

**FM-12** -- Verdict Capture. *Response*: `[FM-12: self-gating; separate evidence role required]`.

**FM-13** -- Tier Blur. *Response*: `[NC: wrong-tier trigger in table | FM-13]`.

**FM-14** -- Visual Cycle Inference. *Response*: `[FM-14: DFS traversal steps required]`.

**FM-15** -- Chain-Open Blindness. *Response*: `[CHAIN OPEN: CH-NN | FM-15]` on final unterminated row.

**FM-16** -- Catalog Opacity. *Response*: FM code inline in every violation cell; blank FM slot is FM-18.

**FM-17** -- Reconciliation Capture. *Response*: `[FM-17: reconciliation must be independent section]`.

**FM-18 -- Catalog Coverage Gap (SELF-REFERENTIAL)**: Any output cell carrying a violation marker without an inline FM code is itself a violation of FM-18. *Formal rule*: the cell SHALL carry `[original-marker | FM-18: FM code required in this cell]`. This rule is recursive: an FM-18 violation cell that omits FM-18's own code is also FM-18. Coverage completeness is achieved when no violation cell lacks an FM code — any codeless violation marker is immediately flagged as FM-18. Distinct from FM-16 (which states the output cross-reference obligation); FM-18 names the specific failure mode generated when FM-16's rule is breached, making the breach diagnosable by code without re-reading the preamble.

**FM-19 -- Role Input Boundary Violation**: A structurally separate role consumes outputs from a role outside its declared Input Contracts. *Response*: `[FM-19: {Role N} may not consume {Role M} output — not in input contracts]`. Undeclared input consumption is a structural boundary violation regardless of content correctness.

**FM-20 -- Protocol State Column Type Violation**: A column typed as `ENUM{[TERMINAL] | [CHAIN OPEN: CH-NN | FM-15] | --}` contains a blank or off-enum value. *Response*: `[TYPE-ERR-CS: ENUM{[TERMINAL]|[CHAIN OPEN: CH-NN | FM-15]|--} required | FM-20]`. Enforcement is at column evaluation time — before vocabulary audit. Blanks are column-structural violations by column definition, not vocabulary failures.

---

#### ROLE A -- SCANNER

**Input Contracts** (Role A reads from external system context only):
- Change event scenario: external
- Trigger registry: external
- Role A consumes no prior-role output.

**Task**: Establish analysis boundary. Declare candidate denominator. Define vocabulary and Chain Status column type.

**A-0 -- Change Scope Pin**

> `{Entity} -- {Field} changed from {old value} to {new value} | context: {initiating action}`

**A-1 -- Vocabulary Contract**

Non-conforming values in constrained columns: `[NC: actual_value | FM-03]`.

| Column | Permitted Values |
|---|---|
| **PA Flow Type** | `Automated -- Dataverse` \| `Automated -- SharePoint` \| `Automated -- HTTP` \| `Instant` \| `Scheduled` |
| **Tier** | `Sync` \| `Async` |
| **Latency (Sync rows)** | `Inline (blocks transaction)` |
| **Delay Estimate (Async rows)** | `~N min [standard\|premium] tier` (N required) |
| **Condition Branch** | `Taken: [branch] -- [reason scenario satisfies]` AND `Skipped: [branch] -- [reason scenario does not satisfy]` (both required for conditional) \| `No condition` |
| **Input Payload** | `{Entity}.{Field}` syntax required |
| **Output Action** | Opens with: `Sets` \| `Creates` \| `Deletes` \| `Sends email via` \| `Calls HTTP` \| `Starts child flow:` \| `Posts adaptive card to` |
| **Side-Effect Writes** | `{Entity}.{Field} = {value}` or `None` (explicit) |

Negative examples (must be marked `[NC: value | FM-03]`):
- Flow Type: `cloud flow`, `automated flow`, `PA flow`, `button flow`
- Latency: blank, `"varies"`, `"unknown"`, `"fast"`
- Condition Branch: `"Condition: True"`, `"Met"`, `"Applies"`, `"Evaluates to True"`
- Input Payload: `"the status field"`, `"record status"`, `"current value"`
- Output Action: `"processes the record"`, `"sends a notification"`, `"updates the status"`
- Side-Effect Writes: empty cell (must be `None` if no writes)

**A-2 -- Chain Status Column Type Definition**

```
COLUMN: Chain Status
COLUMN TYPE: ENUM{[TERMINAL] | [CHAIN OPEN: CH-NN | FM-15] | --}

Permitted values and semantics:
  [TERMINAL]                  — final row: chain has resolved; no downstream triggers fire
  [CHAIN OPEN: CH-NN | FM-15] — final row: chain has not resolved; FM-15 companion fires
  --                          — non-final progress row: chain step in progress

Column type constraint (enforced at column evaluation time, before vocabulary audit):
  - Blank cells: [TYPE-ERR-CS: ENUM{[TERMINAL]|[CHAIN OPEN: CH-NN | FM-15]|--} required | FM-20]
  - Off-enum values: [TYPE-ERR-CS: value not in ENUM{[TERMINAL]|[CHAIN OPEN: CH-NN | FM-15]|--} | FM-20]
  - Final chain row carrying "--": [TYPE-ERR-CS: "--" invalid at chain terminus; ENUM{[TERMINAL]|[CHAIN OPEN]} required | FM-20]

The type constraint is defined at the column level — not enforced by a downstream companion-marker rule.
```

**A-3 -- Candidate Pre-Scan** (FM-10 guard: entity/field/type only — conditions NOT evaluated)

| CA-ID | Trigger Name | PA Flow Type | Tier | Matching Basis |
|---|---|---|---|---|
| CA-01 | | | | |

**Denominator Count: N** — Every CA-NN must appear in Role E. Unresolved entries: structural gaps (`[FM-17]`).

---

#### ROLE B -- TRACER

**Input Contracts** (Role B reads from Role A outputs only):
- A-0: Change scope pin (analysis boundary)
- A-1: Vocabulary contract (column constraints for B-1/B-2)
- A-2: Chain Status column type definition
- A-3: Candidate list (CA-NN entries and denominator count N)
- Role B may NOT consume Role C, D, or E outputs. Violation: `[FM-19: Role B may not consume Role C/D/E outputs]`

**Analytical obligations before producing any table row:**
- For every conditional trigger: identify both the taken branch AND the skipped branch with scenario-specific reasons (addresses FM-04; required by vocabulary contract A-1)
- For every trigger: identify all fields written by output actions in `{Entity}.{Field}` syntax; write `None` explicitly if no fields written (addresses FM-11 precondition; required for Role C's cascade chain work)

**Task**: Produce sync and async firing tables. Assign Chain IDs to side-effect writes that could cascade. Do not walk cascade chains.

**B-1 -- Sync Firing Table**

Wrong-tier: `[NC: async trigger in sync table | FM-13]`

| Seq | CA-Ref | Trigger Name | PA Flow Type | Condition Branch | Input Payload | Output Action | Side-Effect Writes | Latency | Chain ID |
|---|---|---|---|---|---|---|---|---|---|

- **CA-Ref**: CA-NN from A-3. Not in pre-scan: `[NOT IN DENOMINATOR | FM-01]`
- **Condition Branch**: Both branches required. Missing skipped: `[NC: only taken branch | FM-04]`
- **Side-Effect Writes**: `{Entity}.{Field} = {value}` or `None` (never blank)
- **Chain ID**: If Side-Effect Writes could match any CA-NN trigger condition: assign CH-01, CH-02, etc. No match: `--`

Sync total: N | Chain IDs assigned: (list)

**B-2 -- Async Firing Table**

Wrong-tier: `[NC: sync trigger in async table | FM-13]`

Same columns as B-1, Latency → Delay Estimate.

Async total: N

**B-3 -- Tracer Handoff Summary**

- Grand total: Sync N + Async N = N
- Chain IDs: CH-NN → root trigger → cascade field
- `[NOT IN DENOMINATOR]` entries: (list or "none")

---

#### ROLE C -- CASCADE CLOSER

**Input Contracts** (Role C reads from Role B outputs only):
- B-1: Sync firing table (trigger names, side-effect writes, chain IDs)
- B-2: Async firing table (trigger names, side-effect writes, chain IDs)
- B-3: Tracer handoff summary (chain ID list)
- Role C may NOT consume Role D or E outputs. Violation: `[FM-19: Role C may not consume Role D/E outputs]`

**Analytical obligations before producing any cascade table:**
- For every CH-NN: trace from root trigger until the termination condition is satisfied — Side-Effect Writes = `None` or the written field matches no CA-NN candidate. Do not stop at a fixed step depth.
- For every chain step: apply Chain Status column type from A-2. Final rows must carry `[TERMINAL]` or `[CHAIN OPEN: CH-NN | FM-15]`; blanks are FM-20 type violations.
- After all chains complete: build directed edge set and apply DFS back-edge detection.

**Task**: Walk each CH-NN chain to termination. Enforce Chain Status column type (A-2). Build directed edge set. Apply DFS back-edge detection.

**C-1 -- Cascade Chain Walk**

For each CH-NN:

**Chain CH-NN** | Root: `{trigger name}` | Cascade Field: `{Entity.Field}`

| Step | Trigger Name | Fires Because | Reads | Produces | Side-Effect Writes | Chain Status |
|---|---|---|---|---|---|---|

**Chain Status enforcement** (column type ENUM from A-2):
- Blank: `[TYPE-ERR-CS: ENUM{[TERMINAL]|[CHAIN OPEN: CH-NN | FM-15]|--} required | FM-20]`
- Final row with `--`: `[TYPE-ERR-CS: -- invalid at chain terminus | FM-20]`
- Non-final rows: `--`
- Terminal final row: `[TERMINAL]`
- Unresolved final row: `[CHAIN OPEN: CH-NN | FM-15]`

**Termination condition**: Side-Effect Writes = `None` OR written field matches no CA-NN candidate trigger condition. Fixed-depth stop: `[TRUNCATED | FM-08]`.

**C-2 -- Directed Edge Set**

```
{Trigger A} -> writes {Entity.Field} -> fires {Trigger B}
{Trigger C} -> writes {Entity.Field} -> [NO DOWNSTREAM]
```

Every side-effect write from Roles B and C must appear. If no side effects: `{}`.

**C-3 -- DFS Back-Edge Detection** (FM-14 guard: traversal steps required; visual inspection prohibited)

```
Initialize: visited = {}  |  in-path = {}
For each trigger T in edge set not yet in visited:
  1. Add T to in-path
  2. For each downstream trigger U that T fires:
     a. If U is in in-path: [BACK-EDGE: T -> ... -> U -> T | FM-09]
     b. If U not in visited: recurse (apply DFS to U)
  3. Remove T from in-path; mark T as visited
```

After traversal, state:
- `Graph property: DAG` — no back-edges found
- `Graph property: CYCLIC` — list each `[BACK-EDGE]` path

**C-4 -- Closer Handoff Summary**

- Chains walked: N | With `[TERMINAL]`: N | With `[CHAIN OPEN: CH-NN | FM-15]`: N (list)
- Edge set: (from C-2)
- Graph property: DAG | CYCLIC

---

#### ROLE D -- GATEKEEPER

**Input Contracts** (Role D reads from Role B, C, and E outputs only):
- B-3: Grand total fires, `[NOT IN DENOMINATOR]` entries
- C-4: Chains handoff (terminal/open counts), edge set, graph property
- E-1: Disposition table (FLAGGED GAP entries — Role D-2 requires Role E to complete first)
- E-2: Reconciliation totals (FIRED / CONFIRMED ABSENT / FLAGGED GAP counts)
- Role D may NOT consume Role A-3 directly — Role E mediates denominator access.
- Role D may NOT generate new analysis: `[FM-12: self-gating; separate evidence role required]`
- Role D may NOT produce reconciliation content: `[FM-17: gatekeeper may not produce reconciliation content]`

Role D emits only:
- `[EVIDENCE: CONFIRMED -- {specific citation to Role B row or Role C step}]`
- `[INSUFFICIENT: {state exactly what evidence is needed and where} | FM-07]`

**D-1 -- Trigger Storm Gate**

- Grand total from B-3: N | Storm threshold: > 3 total fires or any `[BACK-EDGE]` in C-4
- B-3 total absent: `[INSUFFICIENT: Role B grand total required before storm verdict | FM-07]`
- Back-edge analysis absent: `[INSUFFICIENT: Role C DFS traversal required before storm verdict | FM-14]`
- Emit: `[EVIDENCE: CONFIRMED -- CLEARED; count = N per B-3; DAG per C-3; no re-entry path]` | `[STORM DETECTED -- count = N per B-3; path: {C-4}; Risk = {level}; mitigation: {one line}]`

**D-2 -- Missing Triggers Gate** (Role E MUST complete before D-2 can be issued)

- Role E not complete: `[INSUFFICIENT: Role E reconciliation required before missing trigger verdict | FM-07]`
- FLAGGED GAP count from E-1: N
- Emit: `[EVIDENCE: CONFIRMED -- CLEARED; N candidates: N fired, N absent, 0 gaps per Role E]` | `[MISSING TRIGGER: {name} -- {cause} -- {risk}]` per FLAGGED GAP

**D-3 -- Circular Triggers Gate**

- Graph property from C-4: DAG | CYCLIC
- DFS not shown: `[INSUFFICIENT: Role C DFS traversal steps required | FM-14]`
- Emit: `[EVIDENCE: CONFIRMED -- CLEARED; DAG per C-3 DFS; edge set: {C-2}]` | `[CIRCULAR TRIGGER: {path}; Risk = Critical; mitigation: {one line}]`

**D-4 -- Risk-Ranked Pathology Summary**

| Rank | Pathology | Risk Level | Operational Impact | Mitigation |
|---|---|---|---|---|

Critical first. All cleared: `No pathologies confirmed -- all three classes gated with evidence citations.`

---

#### ROLE E -- RECONCILIATION AUDITOR

**Input Contracts** (Role E reads from Role A and Role B outputs only):
- A-3: CA-NN candidate list and denominator count N
- B-1: CA-Ref values and Seq numbers from sync firing table
- B-2: CA-Ref values and Seq numbers from async firing table
- Role E may NOT consume Role C, D outputs. Violation: `[FM-19: Role E may not consume Role C/D outputs]`

Role E is structurally independent (FM-17 guard). It does not gate verdicts (Role D). It does not generate trigger analysis (Roles B and C). Sole output: denominator reconciliation. Embedding inside any other role: `[FM-17: reconciliation must be independent section]`.

**Analytical obligations before producing the reconciliation table:**
- For every CA-NN in A-3: assign a disposition based on B-1/B-2 CA-Ref values. Do not read Role C or D to make this determination — only A-3 and B-1/B-2 are in input contracts.
- Evidence must be specific enough to verify without reading Roles B–D: `B-1 Seq #3` or `condition: Status was Draft; requires Active` — not `"see Role B"`.

**E-1 -- Denominator Reconciliation Table**

For every CA-NN from A-3:

| CA-ID | Trigger Name | Tier | Disposition | Disposition Evidence |
|---|---|---|---|---|

Disposition codes:
- `FIRED -- Sync, Seq #N` — appeared in B-1 at stated sequence
- `FIRED -- Async, Seq #N` — appeared in B-2 at stated sequence
- `CONFIRMED ABSENT -- {specific condition or filter that prevented firing}` — condition evaluated; excluded
- `FLAGGED GAP -- {reason expected to fire but not in Role B}` — expected to fire; no Role B entry

Generic evidence: `[INSUFFICIENT: specific row or condition required | FM-07]`

**E-2 -- Reconciliation Totals**

- Total candidates (A-3): N
- FIRED: N | CONFIRMED ABSENT: N | FLAGGED GAP: N | Unresolved: N
- Verification: sum SHALL equal N. Mismatch: `[FM-17: N entries unaccounted for]`

**E-3 -- Open Chain Inventory**

- `[CHAIN OPEN: CH-NN | FM-15]` entries from Role C-4: (list or "none")
- For each: root trigger (CA-ID), cascade field, last step reached, cross-reference to any E-1 FLAGGED GAP

---

**EXECUTION RULE**: Apply FM-18 throughout. Before advancing from any role, scan all violation cells: any cell containing a marker without an FM code SHALL be updated to `[marker | FM-18: FM code required in this cell]`. No violation cell may close with a codeless marker.

Now receive the scenario and produce the output following this protocol.

---

## Version Notes

**v1 → v2 changes**: Four new aspirational criteria from R1 excellence signals.

**v2 → v3 changes**: C-13 (cascade termination), C-14 (trigger graph), C-15 (denominator pre-scan), C-16 (terminal row marker), C-17 (role-separated gating), C-18 (tier split), C-19 (DFS back-edge).

**v3 → v4 changes**: C-20 (terminal-absence companion marker), C-21 (protocol-indexed FM catalog), C-22 (denominator-governed reconciliation section).

**v4 → v5 changes (this round)**: C-23 (self-enforcing FM catalog — FM-18 entry), C-24 (per-role input contract declarations — FM-19), C-25 (enum-typed binary protocol state column — FM-20). Scoring denominator: 14 aspirational → 17 aspirational.
