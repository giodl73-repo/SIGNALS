# Flow-Resilience Skill — Round 11 Variations (Rubric v11)

**Skill**: flow-resilience — Simulate degraded conditions: offline, partial failure, eventual
consistency.
**Rubric**: v11 (C-01 through C-35, essential/recommended/aspirational tiers)
**Date**: 2026-03-15

---

## Round 11 Context

**New criteria entering R11**: none — all three criteria added in v11 (C-33, C-34, C-35)
were cracked by R10 V-05.

**Persistent uncracked**: C-09 (chaos engineering test cases) and C-10 (observability hooks
tied to named gaps) — unaddressed across all rounds through R10.

**R10 ceiling**: V-05 at 50/54 uncapped aspirational (all criteria PASS except C-09 and
C-10). Composite 100/100.

**R11 targets**: Crack C-09 and C-10 to push ceiling toward 54/54.

**Variation axes selected**:
- V-01: Single axis — Output format: Gate 2b (Chaos Engineering Table) between Gate 2 and
  Gate 3; each chaos row cites the Trigger Condition threshold from Gate 2 as activation
  boundary
- V-02: Single axis — Lifecycle emphasis: Observable Signal column co-located in each Gate 3
  gap table row; observability absence emitted as MRF-OBS-NN finding
- V-03: Single axis — Phrasing register: direct conversational imperative throughout; same
  Gate 2b + observability structure as V-01+V-02 but with "Write this now" directive
  phrasing replacing formal gate declarations
- V-04: Combination — Role sequence + lifecycle emphasis: Act 3 SRE Reliability Expert owns
  Gate 6 (Chaos Engineering) and Gate 7 (Observability Manifest); RULE-CHAOS-INJECT and
  RULE-OBS-GAP added to registry, owned by SRE Expert (Act 3)
- V-05: Full integration — Gate 2b (chaos) + Gate 3 Observable Signal column + all 6 rules
  in RULE REGISTRY + bypass chain extended to cover new rules + post-analysis audit covers
  all 6 rules

---

## V-01

**Variation axis**: Output format — A dedicated Gate 2b (Chaos Engineering Specification) is
inserted between Gate 2 (scenario analysis) and Gate 3 (gap identification). Gate 2b is gated
on Gate 2 STATUS: CLOSED. It produces a three-column table with one row per Include scenario:
**Inject** (named fault mechanism + parameters), **Expected Observable** (in-fault system
behavior at named observation granularity), **Pass-Fail Signal** (binary named artifact
terminating the test). Each chaos row references the Trigger Condition threshold expression
from the corresponding Gate 2 row as its activation boundary, creating a shared threshold
between the monitoring specification and the test specification.

**Hypothesis**: C-09 is persistently uncracked because chaos engineering has no structural
home — it appears as a suggestion, if at all. Gate 2b gives it a formal gate with entry
conditions (Gate 2 CLOSED, all scenarios enumerated), exit conditions (every Include scenario
has a chaos row with all three required fields), and gate status (CLOSED/OPEN with blocking
reason). Making chaos specification a gated phase forces the three required C-09 elements by
column-contract enforcement: a row with a missing Pass-Fail Signal is a gate violation, not
an omission. The Trigger Condition reference also prevents chaos tests from being written at
a different threshold than the monitoring spec, making C-09 and C-34 jointly falsifiable.

---

You are running the **flow-resilience** skill for `{topic}`.

This analysis runs in two sequential acts. Act 1 is the Distributed Systems Expert.
Act 2 is the Commerce Domain Validator. Each act closes with a formal sign-off.
Do not blend the acts.

---

### RULE REGISTRY

| Rule ID | Trigger Condition | Action Required | Bypass Owner |
|---|---|---|---|
| RULE-CR-DCV | Concurrent state modification by multiple actors without a coordination mechanism | Emit DCV-NN in Gate 3; cite rule inline at trigger point | DS Expert (Act 1) |
| RULE-BARRED-CG | Discovery entry confidence basis cannot be resolved from available context | Mark BARRED; emit CG-NN in coverage log | DS Expert (Act 1) |
| RULE-NIL-SUPERSEDE | Downstream finding introduced in a category that held a typed nil | Annotate nil SUPERSEDED citing new finding ID | DS Expert (Act 1) |
| RULE-COMMERCE-ANCHOR | Include scenario references a generic operation with no named commerce flow | Amend to name specific operation; record amendment | Commerce Validator (Act 2) |

**Bypass Owner column**: If a rule shows RULE-BYPASSED in the registry audit, the named
owner is responsible for invoking the bypass gate-reopening protocol. Commerce Validator
cannot reopen Act 1 gates; DS Expert cannot reopen Act 2 gates.

---

### BYPASS GATE-REOPENING PROTOCOL

**Authority**: DS Expert owns this protocol for Act 1 rules; Commerce Validator for Act 2
rules. Cross-act invocation is not permitted.

When any rule shows RULE-BYPASSED in the Post-Analysis Rule Registry Audit:

1. Bypass Owner emits: `GATE N-bypass: REOPENED — [rule ID] — bypass at [gate, entry ID]`
2. Bypass Owner applies the rule: produces DCV-NN, CG-NN, SUPERSEDED annotation, or
   commerce anchor amendment as the rule requires.
3. Bypass Owner emits: `GATE N-bypass: AMENDED — CLOSED — [rule now applied]`
4. Bypass Owner updates the audit row: Status → INVOKED; BYPASS-TRIGGER →
   "RESOLVED — [sub-gate reference]"; Citations += sub-gate reference.

**COMPLETE may not be declared** while any RULE-BYPASSED entry remains unresolved in any act.

---

### ANTI-OMISSION ARCHITECTURE

| Level | Anti-Omission Mechanism | Omission Risk Targeted | Mechanism Location |
|---|---|---|---|
| Table | Unified row index (`#`) + anti-split instruction | Row fragmentation across ownership transitions | `#` column; anti-split instruction in Gate 2 |
| Section | Phase gate — all rows complete before Gap Identification section | Premature section advance before row set is exhausted | Section gate in Gate 2 |
| Slot | In-row bold imperative: **"Write this row now."** / **"Do not advance to Row N+1 until..."** | Row omission under token pressure | Row Descriptors (below) |
| Column-Group | Intra-row ownership phase gate: C-phase columns complete before D-phase columns begin within the same row | Mid-row D-phase omission when ownership shifts from Commerce Expert to DS Expert | Row Descriptors: Column-Group Gate (below) |
| Column | Column ownership per header (defined in Column Contract, below) | Individual column omission under ownership confusion | Column Contract (below) |

**Anti-split instruction**: Do not create separate sub-tables for Commerce Expert columns and
DS Expert columns. Do not insert a horizontal rule, heading, or section break between rows
when column ownership shifts from C-phase to D-phase within a row.

---

### COLUMN CONTRACT

Place this table before any scenario output. Every column in the Gate 2 scenario table must
have an entry here. A column missing from this contract is a contract violation.

| Column Name | Owner | Phase | Fill Requirement |
|---|---|---|---|
| `#` | Shared | — | Sequential integer; no gaps; no reuse across scenario classes |
| `ID` | Shared | — | FS-NN format; unique per scenario |
| `Trigger Condition` | DS Expert | C-phase | **Two required components**: (1) threshold expression — a quantified condition activating the scenario (e.g., "inventory count falls below safety-stock threshold", "payment API p99 latency exceeds 500ms"); (2) detection signal — the named observable mechanism by which the threshold crossing is confirmed in production (e.g., "inventory-service health probe returns degraded", "payment-provider timeout counter exceeds N/window"). Qualitative trigger descriptions without a threshold expression fail. |
| `State` | Commerce Expert | C-phase | Specific system configuration when failure occurs; name components and their states; not "degraded" |
| `Capability` | Commerce Expert | C-phase | Named commerce operations the user can still complete; not "partial functionality" |
| `Data at Risk` | DS Expert | D-phase | Named data type + consistency failure mode (lost / stale / inconsistent with mechanism) |
| `Recovery Path` | DS Expert | D-phase | Four stages, each with three required components: mechanism (with named actor) \| SLA target \| VS (Verification Signal — named observable artifact confirming stage completion independent of SLA elapse). Format: Detect (mechanism \| actor \| TTD target \| VS: [named observable]); Contain (mechanism \| actor \| TTC target \| VS: [named observable]); Recover (mechanism \| actor \| TTR target \| VS: [named observable]); Validate (mechanism \| actor \| TTV target \| VS: [named observable]). VS must be named (not generic), observable (system state / log entry / metric / response code), and distinct from the mechanism. |
| `Severity` | DS Expert | D-phase | `degraded` / `impaired` / `down` |
| `Blast Radius` | DS Expert | D-phase | Fraction or named segment of users affected |
| `Rule Applied` | DS Expert | D-phase | Rule ID invoked at this row or `—` |

---

### Pre-Analysis: Commerce Operation Scope Declaration

Declare before Gate 1. Minimum four operations from: checkout, inventory reservation,
payment processing, order fulfillment, cart state, loyalty redemption, return/refund.

```
SCOPE DECLARATION
Operations in scope: [list each]
Operations explicitly excluded (with reason): [list or "none"]
SCOPE DECLARATION COMPLETE
```

### Pre-Analysis: Coverage Accountability Roster

| Degradation Class | Committed Minimum | DS Primitive for Impossibility |
|---|---|---|
| Network partition / offline | 2 | [required if slot unfillable] |
| Partial service failure | 2 | |
| Eventual consistency | 2 | |

---

```
ACT 1 OPEN — Distributed Systems Expert
Scope: Gates 1–4 + Gate 2b + Act 1 Registry Audit + Nil Supersession Log +
       Scope Verification + ACT 1 CLOSE
```

### GATE 1: Discovery and Triage

```
GATE 1 OPEN
Preconditions:
  [ ] SCOPE DECLARATION COMPLETE present
  [ ] Coverage Accountability Roster committed
Entry confirmed: [yes / no]
```

| # | ID | Failure Class | Confidence Basis | Disposition | Rule Applied | Notes |
|---|---|---|---|---|---|---|
| 1 | FS-01 | | | Include / BARRED / Argued-Impossible | RULE-BARRED-CG or — | |

BARRED: cite RULE-BARRED-CG inline; emit CG-NN.
Argued-Impossible: name DS Primitive by name (CAP theorem constraint, synchrony guarantee,
topology bound). "Topic does not mention X" is not a DS Primitive.

**Gate 1b — BARRED Resolution**

| BARRED ID | Confidence Basis | Resolved? | Resolution Mechanism | New Disposition |
|---|---|---|---|---|

No BARRED entries: `Gate 1b: none.`

```
GATE 1 CLOSE
Exit postconditions:
  [ ] Every candidate has one named disposition
  [ ] Every BARRED entry has CG-NN emitted
  [ ] Every Argued-Impossible cites DS Primitive by name
  [ ] Coverage Accountability Roster counts updated
Gate 1 STATUS: CLOSED / OPEN — [reason if open]
```

---

### GATE 2: Four-Field Scenario Analysis

```
GATE 2 OPEN
Preconditions:
  [ ] Gate 1 STATUS: CLOSED
Entry confirmed: [yes / no]
```

**Anti-split**: Produce the single scenario table below. Do not create separate sub-tables
for Commerce Expert columns and DS Expert columns. Do not insert a horizontal rule, heading,
or section break between rows when column ownership shifts from C-phase to D-phase within a
row.

**Section gate**: Produce all scenario rows before writing the Gap Identification section.

**Column-group gate**: Within each row, complete all C-phase columns (Trigger Condition,
State, Capability) before writing any D-phase column (Data at Risk, Recovery Path, Severity,
Blast Radius, Rule Applied). The C-phase to D-phase transition must be confirmed inline in
each row descriptor before D-phase columns are written.

Use the Row Descriptors below to construct each row.

---

#### Row Descriptors

**Row 1 — FS-01: [Scenario Name]**

Consequence context: [acute consequences per resolution branch — oversell / double-charge /
duplicate fulfillment depending on how concurrent writes resolve]. Chronic if never addressed:
[rate per transaction] / [horizon: unbounded] / [metric accumulates].

**Write this row now.**
Fill Trigger Condition: (1) threshold expression naming the quantified condition that
activates this scenario; (2) detection signal naming the observable mechanism confirming the
threshold is crossed. Example: "inventory count < safety-stock threshold /
inventory-service health probe returns degraded."
C-phase (Commerce Expert): fill State with the exact system configuration when this failure
occurs — name the components involved and their specific states (not "system is degraded").
Fill Capability with the named commerce operations the user can still complete in this state.
**C-phase complete check: do not begin D-phase columns until Trigger Condition, State, and
Capability contain non-placeholder content.**
D-phase (DS Expert): fill Data at Risk with named data type and consistency failure mode.
Fill Recovery Path with all four stages, each with three required components: mechanism
(named actor) | SLA target | VS (Verification Signal — named observable artifact confirming
stage completion independent of SLA elapse). Example VS entries: Detect VS —
"inventory-service health probe returns degraded"; Contain VS — "reserve-lock acquired,
inventory-reservation-lock-count metric increments"; Recover VS — "inventory-service
heartbeat returns 200 for 30s"; Validate VS — "inventory-accuracy metric returns to baseline
± 0.5%". Fill Severity and Blast Radius. Record rule invocation in Rule Applied.
**Do not advance to Row 2 until this row contains non-placeholder content in every column
including both Trigger Condition components, all four Recovery Path stages each with
mechanism, SLA target, and named VS.**

---

**Row 2 — FS-02: [Scenario Name]**

Consequence context: [payment idempotency miss → double-charge if payment provider receives
duplicate request; loyalty double-redemption if split-brain resolves both redemption writes
as valid]. Chronic: reconciliation backlog per-incident / without ceiling / dispute-count
metric accumulates.

**Write this row now.**
Fill Trigger Condition with threshold expression + detection signal per Column Contract.
C-phase (Commerce Expert): fill State and Capability.
**C-phase complete check: do not begin D-phase columns until C-phase is non-placeholder.**
D-phase (DS Expert): fill Data at Risk, Recovery Path (all four stages: mechanism | actor |
SLA target | VS), Severity, Blast Radius, Rule Applied.
**Do not advance to Row 3 until this row contains non-placeholder content in all columns
including all four Recovery Path stages with mechanism, SLA target, and named VS.**

---

Continue this pattern for all remaining Include scenarios from Gate 1. Every row must have
its own consequence context, column-group gate checkpoint, and advance inhibitor.

Scenario table (single table, all rows):

| # | ID | Trigger Condition | State | Capability | Data at Risk | Recovery Path | Severity | Blast Radius | Rule Applied |
|---|---|---|---|---|---|---|---|---|---|
| 1 | FS-01 | [threshold expr] / [detection signal] | | | | Detect: [mech\|actor\|TTD\|VS]; Contain: [mech\|actor\|TTC\|VS]; Recover: [mech\|actor\|TTR\|VS]; Validate: [mech\|actor\|TTV\|VS] | | | |

```
GATE 2 CLOSE
Exit postconditions:
  [ ] Every Include scenario has all four fields with non-trivial content
  [ ] Every row has Trigger Condition with both threshold expression and detection signal
  [ ] Every row has severity and blast radius labeled
  [ ] Every recovery path has all four stages with mechanism, SLA target, and named VS
  [ ] All RULE-CR-DCV triggers recorded in Rule Applied
  [ ] Column-group gate checkpoint confirmed for every row
Gate 2 STATUS: CLOSED / OPEN — [reason if open]
```

---

### GATE 2b: Chaos Engineering Specification

```
GATE 2b OPEN
Preconditions:
  [ ] Gate 2 STATUS: CLOSED
  [ ] All Include scenarios enumerated in Gate 1
Entry confirmed: [yes / no]
```

For each Include scenario from Gate 1, produce one row in the table below. Three columns are
required:

- **Trigger Condition Reference**: copy the threshold expression from Gate 2 for this
  scenario ID. The chaos test activates at this same threshold — not at an independently
  chosen condition. A test that fires at a different condition than the monitoring spec is
  not a valid chaos test for this scenario.

- **Inject**: the specific fault mechanism to introduce, named to parameter granularity.
  Format: `[fault type]: [named mechanism] — [parameter]`. Examples: "Network partition:
  block all TCP egress from payment-service pod — duration: 60s"; "Latency spike: inject
  2000ms artificial delay on payment-provider API ingress — rate: 100% of requests";
  "Service kill: SIGTERM inventory-service process — restart policy: manual (no auto-restart)".
  Generic descriptions ("make the service unavailable") are not valid.

- **Expected Observable**: what the system must exhibit during the fault, named at
  observation granularity. This is in-fault behavior, not post-recovery state. Example:
  "Cart accepts items; checkout attempt returns HTTP 503 with Retry-After header set;
  inventory-reservation-pending count does not increment beyond pre-fault value."

- **Pass-Fail Signal**: the binary artifact that terminates the test with a named outcome.
  Must name a specific metric, API response code, log entry, system state, or dashboard
  indicator. Example: "PASS if payment-idempotency-key-collision-count == 0 at test end and
  no duplicate charge-events appear in the audit log; FAIL if any charge is recorded more
  than once for the same order ID." Generic outcomes ("system recovers correctly") fail.

| # | Scenario ID | Trigger Condition Reference | Inject | Expected Observable | Pass-Fail Signal |
|---|---|---|---|---|---|
| 1 | FS-01 | [threshold expression from Gate 2 FS-01] | | | |

```
GATE 2b CLOSE
Exit postconditions:
  [ ] One chaos row per Include scenario from Gate 1; no scenarios without a row
  [ ] Every row has Trigger Condition Reference citing Gate 2 threshold expression
  [ ] Every row has Inject with named fault type, mechanism, and parameter (not generic)
  [ ] Every row has Expected Observable at named in-fault observation granularity
  [ ] Every row has Pass-Fail Signal naming a specific binary artifact
Gate 2b STATUS: CLOSED / OPEN — [reason if open]
```

---

### GATE 3: Gap Identification

```
GATE 3 OPEN
Preconditions:
  [ ] Gate 2 STATUS: CLOSED
Entry confirmed: [yes / no]
```

**OEG — Offline Experience Gaps**

| ID | Scenario Ref | Gap Description | Status-Quo Carrying Cost | Actionable Recommendation |
|---|---|---|---|---|
| OEG-01 | FS-NN | | [rate per session/deploy/transaction \| horizon: unbounded/session-scoped \| user-visible failure] | |

No OEG: `OEG-NIL-1: [scope rationale — specific deployment constraint that forecloses
offline experience gaps]`

**DCV — Data Consistency Violations**

| ID | Source | Data Type | Failure Mode | Conflict Resolution Strategy | Adequacy | Status-Quo Carrying Cost | Rule Applied |
|---|---|---|---|---|---|---|---|
| DCV-01 | FS-NN | | | last-write-wins / merge / manual-reconcile / reject-stale / undefined | adequate / inadequate / undefined | [rate \| horizon \| metric] | |

Inadequate or undefined resolution: invoke RULE-CR-DCV; emit DCV-CR-NN.
No DCV: `DCV-NIL-1: [scope rationale]`

**MRF — Missing Recovery Flows**

| ID | Scenario Ref | Absent Mechanism | Status-Quo Carrying Cost | Why No Current Path Exists |
|---|---|---|---|---|
| MRF-01 | FS-NN | | [rate \| horizon \| user-visible failure mode] | |

No MRF: `MRF-NIL-1: [scope rationale]`

```
GATE 3 CLOSE
Exit postconditions:
  [ ] All three gap categories present (OEG, DCV, MRF)
  [ ] Every category has at least one named finding or a typed nil with scope rationale
  [ ] Every typed nil has a unique identifier
  [ ] All pending RULE-CR-DCV entries have DCV-NN assignments
  [ ] Conflict resolution verdict present for every eventual-consistency scenario
  [ ] Status-Quo Carrying Cost populated for every named finding (rate + horizon + metric)
Gate 3 STATUS: CLOSED / OPEN — [reason if open]
```

---

### GATE 4: Amendment Pass

```
GATE 4 OPEN
Preconditions:
  [ ] Gate 3 STATUS: CLOSED
Entry confirmed: [yes / no]
```

| AMD ID | Entry ID | Original (summary) | Amended (summary) | Rule Invoked | Gate Re-Opened? |
|---|---|---|---|---|---|
| AMD-01 | | | | RULE-NIL-SUPERSEDE / — | Gate N: AMENDED / no |

No amendments: `Gate 4: no amendments required. No gate re-opens triggered.`

```
GATE 4 CLOSE
Exit postconditions:
  [ ] All recovery paths have minimum two actor-labeled steps
  [ ] Every superseded nil has SUPERSEDED annotation with finding ID
  [ ] Every late DCV finding is in Gate 3: AMENDED with re-close confirmation
Gate 4 STATUS: CLOSED / OPEN — [reason if open]
```

---

### Act 1 Terminal: Post-Analysis Rule Registry Audit

**BYPASS-TRIGGER column**: A RULE-BYPASSED status cell requires a non-empty BYPASS-TRIGGER
entry. An empty BYPASS-TRIGGER cell beside a RULE-BYPASSED status is itself an audit failure.

| Rule ID | Invocations | Citations (gate, entry) | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-CR-DCV | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | [empty or trigger citation] |
| RULE-BARRED-CG | | | | |
| RULE-NIL-SUPERSEDE | | | | |

If any BYPASS-TRIGGER cell is non-empty — invoke bypass gate-reopening protocol now before
ACT 1 CLOSE.

POST-ANALYSIS REGISTRY AUDIT (ACT 1) COMPLETE: [confirm no RULE-BYPASSED entries remain]

---

### Act 1 Terminal: Nil Supersession Log

| Nil ID | Gap Type | State | Superseded By | Gate |
|---|---|---|---|---|

No supersessions: `No supersessions in this run.`

---

### Act 1 Terminal: Scope Verification

| Declared Operation | Covered | Gap Finding |
|---|---|---|
| [operation] | Yes / No | SV-GAP-NN / — |

SCOPE VERIFICATION COMPLETE

---

```
ACT 1 CLOSE (sign-off)
(1) All gates within Act 1 CLOSED:
    Gate 1:     [CLOSED / OPEN — reason]
    Gate 1b:    [CLOSED / N/A — no BARRED entries]
    Gate 2:     [CLOSED / OPEN — reason]
    Gate 2b:    [CLOSED / OPEN — reason]
    Gate 3:     [CLOSED / OPEN — reason]
    Gate 4:     [CLOSED / OPEN — reason]
    GATE N-bypass blocks (if triggered): [CLOSED / none triggered]
    Act 1 Registry Audit: [CLOSED / OPEN — reason]
(2) Act 1 scope exhausted: [yes / list any unresolved items]
(3) No RULE-BYPASSED conditions remain unresolved within Act 1: [yes / exception detail]
ACT 1 STATUS: CLOSED / OPEN
```

---

```
ACT 2 OPEN — Commerce Domain Validator
Entry condition: ACT 1 STATUS: CLOSED
Scope: Gate 5 + Act 2 Registry Audit + Inertia Synthesis + ACT 2 CLOSE
```

### GATE 5: Commerce Domain Validation

```
GATE 5 OPEN
Preconditions:
  [ ] ACT 1 STATUS: CLOSED
Entry confirmed: [yes / no]
```

| Scenario ID | Commerce Operation Named? | Amended Operation (RULE-COMMERCE-ANCHOR) | CV Finding Issued |
|---|---|---|---|
| FS-01 | Yes / No | | — / CV-DCV-01 / CV-OEG-01 / CV-MRF-01 |

Commerce-domain finding targets (check each):
- Inventory oversell under partition: [present / absent — rationale]
- Payment idempotency window expiry: [present / absent — rationale]
- Loyalty point double-redemption under split-brain: [present / absent — rationale]
- Order state divergence under partial fulfillment failure: [present / absent — rationale]

```
GATE 5 CLOSE
Exit postconditions:
  [ ] Every Include scenario anchored to a named commerce operation
  [ ] All RULE-COMMERCE-ANCHOR invocations recorded
  [ ] All four commerce-domain targets checked (present or rationale)
Gate 5 STATUS: CLOSED / OPEN — [reason if open]
```

---

### Act 2 Terminal: Post-Analysis Rule Registry Audit

| Rule ID | Invocations | Citations | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-COMMERCE-ANCHOR | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | [empty or `GATE 5-bypass: REOPEN now`] |

If BYPASS-TRIGGER non-empty — Commerce Validator resolves before ACT 2 CLOSE.

POST-ANALYSIS REGISTRY AUDIT (ACT 2) COMPLETE

---

### Inertia Synthesis — What Does Doing Nothing Cost?

**Per-finding carrying cost** (from Gate 3 Status-Quo Carrying Cost column):
For each named gap (OEG-NN, DCV-NN, MRF-NN): state the failure mode, the rate (per session
/ deploy / transaction), the horizon (unbounded / session-scoped / compound growth), and the
named metric that accumulates. One entry per finding.

**Overall synthesis**:
Urgency: HIGH / MEDIUM / LOW
Highest-risk finding: [gap ID] — [carrying cost from Gate 3]
Status-quo option: [what "do nothing" looks like for `{topic}` specifically — not generic]
Intervention recommendation: [owner + threshold + consequence of missing threshold]

```
ACT 2 CLOSE (sign-off)
(1) All gates within Act 2 CLOSED:
    Gate 5: [CLOSED / OPEN — reason]
    GATE 5-bypass blocks (if triggered): [CLOSED / none triggered]
    Act 2 Registry Audit: [CLOSED / OPEN — reason]
(2) Act 2 scope exhausted: [yes — all scenarios commerce-anchored; all CV targets checked;
    inertia synthesis complete]
(3) No RULE-BYPASSED conditions remain unresolved within Act 2: [yes / exception detail]
ACT 2 STATUS: CLOSED / OPEN
```

ANALYSIS COMPLETE (declared only when ACT 1 STATUS: CLOSED AND ACT 2 STATUS: CLOSED)

---

---

## V-02

**Variation axis**: Lifecycle emphasis — each of the three Gap Identification tables (OEG,
DCV, MRF) in Gate 3 is extended with a mandatory **Observable Signal** column. Every named
finding row must carry: (1) a named monitoring signal (specific metric, log pattern, trace
attribute, or alert condition); (2) a rationale sentence explaining why that signal would
surface this gap in production before user impact. A finding row without both components is
a Gate 3 exit violation. When a named gap has no known observability signal, the absence is
emitted as an MRF-OBS-NN finding (missing recovery flow — observability variant): the
inability to detect a known gap in production is itself a recovery-flow deficiency.

**Hypothesis**: C-10 is persistently uncracked because observability is treated as optional
commentary. Co-locating the Observable Signal with the gap finding it monitors creates
mandatory bidirectional linkage by column-contract enforcement: each gap knows its monitor;
each monitor knows its gap. The MRF-OBS-NN mechanism prevents silent observability absence
— a gap with no monitoring is not merely undocumented, it is a new named finding, subject to
the same Status-Quo Carrying Cost and Actionable Recommendation requirements as any other MRF.

---

You are running the **flow-resilience** skill for `{topic}`.

This analysis runs in two sequential acts. Act 1 is the Distributed Systems Expert.
Act 2 is the Commerce Domain Validator. Each act closes with a formal sign-off.
Do not blend the acts.

---

### RULE REGISTRY

| Rule ID | Trigger Condition | Action Required | Bypass Owner |
|---|---|---|---|
| RULE-CR-DCV | Concurrent state modification by multiple actors without a coordination mechanism | Emit DCV-NN in Gate 3; cite rule inline at trigger point | DS Expert (Act 1) |
| RULE-BARRED-CG | Discovery entry confidence basis cannot be resolved from available context | Mark BARRED; emit CG-NN in coverage log | DS Expert (Act 1) |
| RULE-NIL-SUPERSEDE | Downstream finding introduced in a category that held a typed nil | Annotate nil SUPERSEDED citing new finding ID | DS Expert (Act 1) |
| RULE-COMMERCE-ANCHOR | Include scenario references a generic operation with no named commerce flow | Amend to name specific operation; record amendment | Commerce Validator (Act 2) |

**Bypass Owner column**: Commerce Validator cannot reopen Act 1 gates; DS Expert cannot
reopen Act 2 gates.

---

### BYPASS GATE-REOPENING PROTOCOL

**Authority**: DS Expert owns this protocol for Act 1 rules; Commerce Validator for Act 2
rules. Cross-act invocation is not permitted.

When any rule shows RULE-BYPASSED in the Post-Analysis Rule Registry Audit:

1. Bypass Owner emits: `GATE N-bypass: REOPENED — [rule ID] — bypass at [gate, entry ID]`
2. Bypass Owner applies the rule.
3. Bypass Owner emits: `GATE N-bypass: AMENDED — CLOSED — [rule now applied]`
4. Bypass Owner updates the audit row: Status → INVOKED; BYPASS-TRIGGER →
   "RESOLVED — [sub-gate reference]"; Citations += sub-gate reference.

**COMPLETE may not be declared** while any RULE-BYPASSED entry remains unresolved in any act.

---

### ANTI-OMISSION ARCHITECTURE

| Level | Anti-Omission Mechanism | Omission Risk Targeted | Mechanism Location |
|---|---|---|---|
| Table | Unified row index (`#`) + anti-split instruction | Row fragmentation across ownership transitions | `#` column; anti-split in Gate 2 |
| Section | Phase gate — all rows complete before Gap Identification | Premature section advance | Section gate in Gate 2 |
| Slot | In-row bold imperative: **"Write this row now."** / **"Do not advance to Row N+1 until..."** | Row omission under token pressure | Row Descriptors |
| Column-Group | Intra-row phase gate: C-phase columns complete before D-phase begins within the same row | Mid-row D-phase omission on ownership shift | Row Descriptors: Column-Group Gate |
| Column | Column ownership per header in Column Contract | Individual column omission | Column Contract |

**Anti-split instruction**: Do not split Commerce Expert and DS Expert columns into separate
sub-tables. Do not insert breaks between rows when ownership shifts within a row.

---

### COLUMN CONTRACT

| Column Name | Owner | Phase | Fill Requirement |
|---|---|---|---|
| `#` | Shared | — | Sequential integer; no gaps |
| `ID` | Shared | — | FS-NN format; unique per scenario |
| `Trigger Condition` | DS Expert | C-phase | **Two required components**: (1) threshold expression — quantified activation condition; (2) detection signal — named observable confirming threshold crossing. Qualitative descriptions without threshold expression fail. |
| `State` | Commerce Expert | C-phase | Specific system configuration; name components and states |
| `Capability` | Commerce Expert | C-phase | Named commerce operations still completable |
| `Data at Risk` | DS Expert | D-phase | Named data type + consistency failure mode |
| `Recovery Path` | DS Expert | D-phase | Four stages each with three components: mechanism (named actor) \| SLA target \| VS (named observable artifact confirming stage completion). Format: Detect (mech \| actor \| TTD \| VS: [named]); Contain (mech \| actor \| TTC \| VS: [named]); Recover (mech \| actor \| TTR \| VS: [named]); Validate (mech \| actor \| TTV \| VS: [named]). VS must be named, observable, and distinct from the mechanism. |
| `Severity` | DS Expert | D-phase | `degraded` / `impaired` / `down` |
| `Blast Radius` | DS Expert | D-phase | Fraction or named segment |
| `Rule Applied` | DS Expert | D-phase | Rule ID or `—` |

---

### Pre-Analysis: Commerce Operation Scope Declaration

```
SCOPE DECLARATION
Operations in scope: [minimum four from: checkout / inventory reservation / payment
processing / order fulfillment / cart state / loyalty redemption / return-refund]
Operations explicitly excluded (with reason): [list or "none"]
SCOPE DECLARATION COMPLETE
```

### Pre-Analysis: Coverage Accountability Roster

| Degradation Class | Committed Minimum | DS Primitive for Impossibility |
|---|---|---|
| Network partition / offline | 2 | [required if slot unfillable] |
| Partial service failure | 2 | |
| Eventual consistency | 2 | |

---

```
ACT 1 OPEN — Distributed Systems Expert
Scope: Gates 1–4 + Act 1 Registry Audit + Nil Supersession Log + Scope Verification +
       ACT 1 CLOSE
```

### GATE 1: Discovery and Triage

```
GATE 1 OPEN
Preconditions:
  [ ] SCOPE DECLARATION COMPLETE present
  [ ] Coverage Accountability Roster committed
Entry confirmed: [yes / no]
```

| # | ID | Failure Class | Confidence Basis | Disposition | Rule Applied | Notes |
|---|---|---|---|---|---|---|
| 1 | FS-01 | | | Include / BARRED / Argued-Impossible | RULE-BARRED-CG or — | |

BARRED: cite RULE-BARRED-CG; emit CG-NN.
Argued-Impossible: name DS Primitive. "Topic does not mention X" is not a DS Primitive.

**Gate 1b — BARRED Resolution**

| BARRED ID | Confidence Basis | Resolved? | Resolution Mechanism | New Disposition |
|---|---|---|---|---|

No BARRED entries: `Gate 1b: none.`

```
GATE 1 CLOSE
Exit postconditions:
  [ ] Every candidate has one named disposition
  [ ] Every BARRED entry has CG-NN emitted
  [ ] Every Argued-Impossible cites DS Primitive by name
  [ ] Roster counts updated
Gate 1 STATUS: CLOSED / OPEN — [reason if open]
```

---

### GATE 2: Four-Field Scenario Analysis

```
GATE 2 OPEN
Preconditions:
  [ ] Gate 1 STATUS: CLOSED
Entry confirmed: [yes / no]
```

**Anti-split**: Single scenario table. No sub-tables by ownership. No breaks between rows
when ownership shifts.

**Section gate**: All scenario rows before Gap Identification.

**Column-group gate**: Within each row, C-phase columns (Trigger Condition, State,
Capability) must be non-placeholder before any D-phase column begins. Confirm inline in
each row descriptor.

#### Row Descriptors

**Row 1 — FS-01: [Scenario Name]**

Consequence context: [acute consequences per resolution branch]. Chronic if never addressed:
[rate] / [horizon] / [metric accumulates].

**Write this row now.**
Fill Trigger Condition: threshold expression + detection signal.
C-phase (Commerce Expert): fill State (exact system configuration, named components) and
Capability (named operations still completable).
**C-phase complete check: do not begin D-phase until Trigger Condition, State, Capability
are non-placeholder.**
D-phase (DS Expert): fill Data at Risk, Recovery Path (all four stages: mechanism | actor |
SLA target | VS — VS must be named observable distinct from mechanism), Severity, Blast
Radius, Rule Applied.
**Do not advance to Row 2 until all columns including all four VS entries are
non-placeholder.**

---

**Row 2 — FS-02: [Scenario Name]**

Consequence context: [payment idempotency miss / loyalty double-redemption / order
divergence]. Chronic: reconciliation backlog / without ceiling / dispute-count accumulates.

**Write this row now.**
Fill all columns per Column Contract including Trigger Condition (threshold + detection),
Recovery Path (all four stages with mechanism | actor | SLA | VS).
**C-phase complete check before D-phase. Do not advance to Row 3 until all columns
non-placeholder including VS entries.**

---

Continue this pattern for all remaining Include scenarios.

Scenario table:

| # | ID | Trigger Condition | State | Capability | Data at Risk | Recovery Path | Severity | Blast Radius | Rule Applied |
|---|---|---|---|---|---|---|---|---|---|
| 1 | FS-01 | [threshold] / [detection signal] | | | | Detect: [mech\|actor\|TTD\|VS]; Contain: [mech\|actor\|TTC\|VS]; Recover: [mech\|actor\|TTR\|VS]; Validate: [mech\|actor\|TTV\|VS] | | | |

```
GATE 2 CLOSE
Exit postconditions:
  [ ] Every Include scenario has all four fields non-trivial
  [ ] Every Trigger Condition has threshold expression + detection signal
  [ ] Every recovery path has four stages each with mechanism, SLA target, named VS
  [ ] All RULE-CR-DCV triggers recorded
  [ ] Column-group gate checkpoint confirmed for every row
Gate 2 STATUS: CLOSED / OPEN — [reason if open]
```

---

### GATE 3: Gap Identification

```
GATE 3 OPEN
Preconditions:
  [ ] Gate 2 STATUS: CLOSED
Entry confirmed: [yes / no]
```

**Observable Signal column requirement**: Every named finding in OEG, DCV, and MRF tables
must carry an Observable Signal entry with two components: (1) named signal — a specific
metric name, log pattern, trace attribute, or alert condition (e.g.,
"cart-session-divergence-count > 0 per session", "payment-duplicate-charge-audit-log entry
present"); (2) rationale sentence — why this signal would surface the gap in production
before user impact (e.g., "counter increments on every stale-overwrite event; alert threshold
of 1 per hour fires before user-visible data loss accumulates"). A generic signal ("add
monitoring") without a named observable fails. A named observable without a rationale
sentence fails.

**MRF-OBS-NN rule**: When a named gap finding has no known observability signal — no signal
exists that would surface this gap in production — emit an MRF-OBS-NN finding in the MRF
table: Absent Mechanism = "no production observability for [gap ID]"; Why No Current Path
Exists = reason the gap is undetectable with current signals. This is treated as a missing
recovery flow — the system cannot recover from what it cannot detect.

**OEG — Offline Experience Gaps**

| ID | Scenario Ref | Gap Description | Status-Quo Carrying Cost | Observable Signal | Actionable Recommendation |
|---|---|---|---|---|---|
| OEG-01 | FS-NN | | [rate \| horizon \| user-visible failure] | [named signal] — [rationale sentence] | |

No OEG: `OEG-NIL-1: [scope rationale]`

**DCV — Data Consistency Violations**

| ID | Source | Data Type | Failure Mode | Conflict Resolution | Adequacy | Status-Quo Carrying Cost | Observable Signal | Rule Applied |
|---|---|---|---|---|---|---|---|---|
| DCV-01 | FS-NN | | | LWW / merge / manual / reject-stale / undefined | adequate / inadequate / undefined | [rate \| horizon \| metric] | [named signal] — [rationale] | |

No DCV: `DCV-NIL-1: [scope rationale]`

**MRF — Missing Recovery Flows**

| ID | Scenario Ref | Absent Mechanism | Status-Quo Carrying Cost | Observable Signal | Why No Current Path Exists |
|---|---|---|---|---|---|
| MRF-01 | FS-NN | | [rate \| horizon \| failure mode] | [named signal] — [rationale] | |

No MRF: `MRF-NIL-1: [scope rationale]`

If a named finding has no known observability signal: emit `MRF-OBS-NN` in the MRF table
with Absent Mechanism = "no production observability for [gap ID]".

```
GATE 3 CLOSE
Exit postconditions:
  [ ] All three gap categories present (OEG, DCV, MRF)
  [ ] Every named finding has Observable Signal with named signal + rationale sentence
  [ ] Findings with no observable signal have MRF-OBS-NN emitted
  [ ] Every typed nil has a unique identifier with scope rationale
  [ ] All RULE-CR-DCV entries assigned DCV-NN
  [ ] Status-Quo Carrying Cost populated for every named finding
Gate 3 STATUS: CLOSED / OPEN — [reason if open]
```

---

### GATE 4: Amendment Pass

```
GATE 4 OPEN
Preconditions:
  [ ] Gate 3 STATUS: CLOSED
Entry confirmed: [yes / no]
```

| AMD ID | Entry ID | Original (summary) | Amended (summary) | Rule Invoked | Gate Re-Opened? |
|---|---|---|---|---|---|

No amendments: `Gate 4: no amendments required. No gate re-opens triggered.`

```
GATE 4 CLOSE
Exit postconditions:
  [ ] All recovery paths have minimum two actor-labeled steps
  [ ] Every superseded nil has SUPERSEDED annotation with finding ID
Gate 4 STATUS: CLOSED / OPEN — [reason if open]
```

---

### Act 1 Terminal: Post-Analysis Rule Registry Audit

| Rule ID | Invocations | Citations (gate, entry) | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-CR-DCV | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | [empty or trigger citation] |
| RULE-BARRED-CG | | | | |
| RULE-NIL-SUPERSEDE | | | | |

BYPASS-TRIGGER non-empty → invoke bypass gate-reopening protocol before ACT 1 CLOSE.

POST-ANALYSIS REGISTRY AUDIT (ACT 1) COMPLETE: [confirm no RULE-BYPASSED entries remain]

---

### Act 1 Terminal: Nil Supersession Log

| Nil ID | Gap Type | State | Superseded By | Gate |
|---|---|---|---|---|

No supersessions: `No supersessions in this run.`

---

### Act 1 Terminal: Scope Verification

| Declared Operation | Covered | Gap Finding |
|---|---|---|
| [operation] | Yes / No | SV-GAP-NN / — |

SCOPE VERIFICATION COMPLETE

---

```
ACT 1 CLOSE (sign-off)
(1) All gates within Act 1 CLOSED:
    Gate 1: [CLOSED / OPEN — reason]; Gate 1b: [CLOSED / N/A]
    Gate 2: [CLOSED / OPEN — reason]; Gate 3: [CLOSED / OPEN — reason]
    Gate 4: [CLOSED / OPEN — reason]
    GATE N-bypass blocks: [CLOSED / none triggered]
    Act 1 Registry Audit: [CLOSED / OPEN — reason]
(2) Act 1 scope exhausted: [yes / list unresolved items]
(3) No RULE-BYPASSED conditions remain unresolved within Act 1: [yes / exception detail]
ACT 1 STATUS: CLOSED / OPEN
```

---

```
ACT 2 OPEN — Commerce Domain Validator
Entry condition: ACT 1 STATUS: CLOSED
Scope: Gate 5 + Act 2 Registry Audit + Inertia Synthesis + ACT 2 CLOSE
```

### GATE 5: Commerce Domain Validation

```
GATE 5 OPEN
Preconditions:
  [ ] ACT 1 STATUS: CLOSED
Entry confirmed: [yes / no]
```

| Scenario ID | Commerce Operation Named? | Amended Operation | CV Finding Issued |
|---|---|---|---|
| FS-01 | Yes / No | | — / CV-DCV-01 / CV-OEG-01 / CV-MRF-01 |

Commerce-domain targets: inventory oversell / payment idempotency / loyalty
double-redemption / order state divergence — each: [present / absent — rationale].

```
GATE 5 CLOSE
Exit postconditions:
  [ ] Every scenario anchored to named commerce operation
  [ ] All four commerce-domain targets checked
Gate 5 STATUS: CLOSED / OPEN — [reason if open]
```

---

### Act 2 Terminal: Post-Analysis Rule Registry Audit

| Rule ID | Invocations | Citations | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-COMMERCE-ANCHOR | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | [empty or bypass trigger] |

POST-ANALYSIS REGISTRY AUDIT (ACT 2) COMPLETE

---

### Inertia Synthesis

**Per-finding carrying cost**: For each named gap — failure mode, rate, horizon, metric.

**Overall synthesis**:
Urgency: HIGH / MEDIUM / LOW
Highest-risk finding: [gap ID] — [carrying cost from Gate 3]
Status-quo option: [specific to `{topic}`]
Intervention recommendation: [owner + threshold + consequence]

```
ACT 2 CLOSE (sign-off)
(1) All gates within Act 2 CLOSED: Gate 5 / bypass blocks / Registry Audit
(2) Act 2 scope exhausted: [yes]
(3) No RULE-BYPASSED conditions remain unresolved: [yes / exception]
ACT 2 STATUS: CLOSED / OPEN
```

ANALYSIS COMPLETE (declared only when ACT 1 STATUS: CLOSED AND ACT 2 STATUS: CLOSED)

---

---

## V-03

**Variation axis**: Phrasing register — direct conversational imperative throughout. Gate
declarations are replaced with numbered step headers ("**Step 3: Write the scenario table**")
and direct "Write this now / Here is the format" instruction blocks. The same structural
completeness requirements are preserved — coverage roster, column-group gate, typed nil
identifiers, rule registry, bypass chain, VS per recovery stage, Trigger Condition column,
Gate 2b chaos table, Gate 3 Observable Signal column — but the phrasing is directive rather
than bureaucratic. Gate status is tracked with a compact inline checkbox block rather than a
formal GATE N OPEN / GATE N CLOSE wrapper.

**Hypothesis**: The formal gate wrapper (GATE N OPEN / GATE N CLOSE / Exit postconditions
table) consumes significant token budget with structural boilerplate. A conversational
imperative register delivers the same structural enforcement with less overhead — "Write a
chaos test row for each scenario; include these three things:" is equivalent to "GATE 2b
OPEN / Preconditions / Exit postconditions" but shorter. The question is whether reduced
formalism degrades structural compliance (gate-state tracking, bypass invocation, sign-off
completeness) or improves it by reducing parse cost.

---

You are running the **flow-resilience** skill for `{topic}`.

Two roles run in sequence: first the Distributed Systems Expert (DS Expert), then the
Commerce Domain Validator. Finish the DS Expert's scope completely before the Commerce
Validator begins. Each role closes with a sign-off confirming all work in its scope is done.

---

**Rules that fire during this analysis** (consult this table before each step):

| Rule ID | When it fires | What to do | Who owns it |
|---|---|---|---|
| RULE-CR-DCV | Concurrent state modification by multiple actors without coordination | Emit DCV-NN in the Data Consistency table; note rule inline | DS Expert |
| RULE-BARRED-CG | Discovery entry has unresolvable confidence basis | Mark it BARRED; emit CG-NN | DS Expert |
| RULE-NIL-SUPERSEDE | A downstream finding appears in a category that already has a nil entry | Mark that nil SUPERSEDED with the new finding ID | DS Expert |
| RULE-COMMERCE-ANCHOR | A scenario references no named commerce operation | Amend the scenario to name the operation | Commerce Validator |

**Bypass protocol** — if any rule shows RULE-BYPASSED in the final audit:
1. Named owner re-opens the affected step: emit `STEP N-bypass: REOPENED — [rule] — bypass at [step, entry]`
2. Apply the rule (produce the required output).
3. Emit `STEP N-bypass: AMENDED — CLOSED`
4. Update the audit entry: Status → INVOKED; note sub-step reference.

You cannot declare the analysis complete while any RULE-BYPASSED entry is unresolved.

---

**Before you begin** — declare the scope and coverage commitment.

Write a commerce operation scope list (minimum four operations from: checkout, inventory
reservation, payment processing, order fulfillment, cart state, loyalty redemption,
return/refund). Then write a coverage commitment table: at least two scenarios per
degradation class (network partition/offline, partial service failure, eventual consistency).
If a class slot cannot be filled, name the DS Primitive (CAP theorem, topology constraint,
synchrony guarantee) that makes it impossible — description absence is not a DS Primitive.

Mark the scope declaration closed: `SCOPE DECLARATION COMPLETE`

---

**Step 1 — Discover failure modes.**

List every failure mode relevant to `{topic}`. For each, decide:
- **Include** — confidence is high enough to analyze
- **BARRED** — confidence basis unresolvable; invoke RULE-BARRED-CG; emit CG-NN
- **Argued-Impossible** — cite the DS Primitive by name

Table format:

| # | ID | Failure Class | Confidence Basis | Disposition | Rule Applied | Notes |
|---|---|---|---|---|---|---|

For any BARRED entries, immediately try to resolve the confidence basis. Record the
resolution attempt:

| BARRED ID | Confidence Basis | Resolved? | Resolution Mechanism | New Disposition |
|---|---|---|---|---|

If no BARRED entries: `Step 1b: none.`

**Step 1 done when**: every candidate has one named disposition; every BARRED has CG-NN;
every Argued-Impossible cites a DS Primitive; coverage roster counts are updated.
`Step 1 STATUS: done / blocked — [reason]`

---

**Step 2 — Write the scenario table.**

This is one unified table — do not split it by role or class. Write all rows before moving
to Step 3.

For each row, follow this sequence: first write the Trigger Condition and Commerce Expert
columns (Trigger Condition, State, Capability) — do not write any DS Expert column until
those three are non-placeholder. Then write the DS Expert columns (Data at Risk, Recovery
Path, Severity, Blast Radius, Rule Applied).

**Columns you must fill for every row:**

- **Trigger Condition**: two things — (1) threshold expression: the exact quantified
  condition that makes this scenario active ("payment API latency > 500ms p99",
  "inventory count < safety-stock threshold"); (2) detection signal: how the system knows
  the threshold has been crossed ("payment-provider timeout counter exceeds 10/minute",
  "inventory-service health probe returns degraded"). "Service is unavailable" is not a
  threshold expression.

- **State**: the specific system configuration when this failure occurs. Name the components
  and their states. Not "the system is degraded."

- **Capability**: named commerce operations the user can still complete in this state. Not
  "partial functionality."

- **Data at Risk**: named data type + the specific consistency failure mode (lost / stale /
  inconsistent, with mechanism).

- **Recovery Path**: four stages, each with three things:
  - Mechanism + named actor (who does what)
  - SLA target (TTD/TTC/TTR/TTV commitment)
  - Verification Signal (VS) — a named observable artifact that confirms the stage is
    complete, independent of timer expiry. Must be named ("inventory-service heartbeat
    returns 200"), not generic ("stage confirmed"). VS confirms outcome; SLA records
    duration. Do not conflate them.

- **Severity**: `degraded` / `impaired` / `down`
- **Blast Radius**: fraction or named user segment affected
- **Rule Applied**: rule ID or `—`

For each row, use this inline sequence:

> Row N — FS-NN: [Scenario Name]
> **Write this row now.** [consequence context sentence]
> Commerce Expert columns first (Trigger Condition, State, Capability).
> **Check: are Trigger Condition, State, Capability non-placeholder? If not, fill them
> before writing Data at Risk.**
> DS Expert columns now (Data at Risk, Recovery Path with all four VS entries, Severity,
> Blast Radius, Rule Applied).
> **Do not advance to Row N+1 until all columns including all four VS entries are
> non-placeholder.**

Table:

| # | ID | Trigger Condition | State | Capability | Data at Risk | Recovery Path | Severity | Blast Radius | Rule Applied |
|---|---|---|---|---|---|---|---|---|---|
| 1 | FS-01 | [threshold] / [detection signal] | | | | Detect: [mech\|actor\|TTD\|VS]; Contain: [mech\|actor\|TTC\|VS]; Recover: [mech\|actor\|TTR\|VS]; Validate: [mech\|actor\|TTV\|VS] | | | |

**Step 2 done when**: all Include scenarios are in the table; every row has all columns
non-trivial including both Trigger Condition components and all four VS entries;
column-group sequence confirmed for each row.
`Step 2 STATUS: done / blocked — [reason]`

---

**Step 3 — Write a chaos test for each scenario.**

Do not begin Step 3 until Step 2 is done.

For every Include scenario, write one row in the chaos test table. Three things per row:

1. **Trigger Condition Reference**: copy the threshold expression from Step 2 for this
   scenario. The chaos test fires at this boundary — same condition as the monitoring spec.

2. **Inject**: the specific fault to introduce. Name the fault type, mechanism, and
   parameters. "Network partition: block all TCP egress from payment-service — duration:
   60s" is valid. "Make the service fail" is not.

3. **Expected Observable**: what you observe while the fault is active. Name it at the
   level of a specific API response, log entry, or metric reading. Not a recovery
   description — what you see during the fault.

4. **Pass-Fail Signal**: the binary outcome. Name the specific metric, response code, log
   entry, or system state that makes the test pass or fail. "PASS if
   payment-idempotency-key-collision-count == 0 at test end; FAIL if any charge appears
   more than once for the same order ID." Generic outcomes fail.

| # | Scenario ID | Trigger Condition Reference | Inject | Expected Observable | Pass-Fail Signal |
|---|---|---|---|---|---|
| 1 | FS-01 | [threshold from Step 2 FS-01] | | | |

**Step 3 done when**: one row per Include scenario; every row has all four fields at named
granularity; Trigger Condition Reference cites Step 2 threshold; Pass-Fail Signal names a
specific binary artifact.
`Step 3 STATUS: done / blocked — [reason]`

---

**Step 4 — Identify the gaps.**

Do not begin Step 4 until Step 2 is done.

Write three gap sections. Each section needs at least one named finding or a typed nil with
scope rationale. Nil format: `OEG-NIL-1: [why this gap type doesn't apply here — name the
specific deployment constraint, not "not mentioned in the topic"]`.

For every named finding, fill the Observable Signal field: (1) named signal (specific
metric, log, trace, alert); (2) rationale sentence (why this signal surfaces the gap before
user impact). If you cannot identify an observable signal for a finding, emit MRF-OBS-NN:
"no production observability for [gap ID]" — undetectable gaps are missing recovery flows.

**Offline Experience Gaps (OEG)**

| ID | Scenario Ref | Gap Description | Status-Quo Carrying Cost | Observable Signal | Actionable Recommendation |
|---|---|---|---|---|---|
| OEG-01 | FS-NN | | [rate \| horizon \| user failure] | [named signal] — [rationale] | |

**Data Consistency Violations (DCV)**

| ID | Source | Data Type | Failure Mode | Conflict Resolution | Adequacy | Status-Quo Carrying Cost | Observable Signal | Rule Applied |
|---|---|---|---|---|---|---|---|---|
| DCV-01 | FS-NN | | | LWW / merge / manual / reject-stale / undefined | adequate / inadequate / undefined | [rate \| horizon \| metric] | [named signal] — [rationale] | |

Inadequate/undefined resolution → invoke RULE-CR-DCV; emit DCV-CR-NN.

**Missing Recovery Flows (MRF)**

| ID | Scenario Ref | Absent Mechanism | Status-Quo Carrying Cost | Observable Signal | Why No Current Path Exists |
|---|---|---|---|---|---|
| MRF-01 | FS-NN | | [rate \| horizon \| failure] | [named signal] — [rationale] | |

**Step 4 done when**: all three sections present; every finding has Observable Signal with
named signal + rationale; unobservable gaps have MRF-OBS-NN emitted; all RULE-CR-DCV
entries assigned DCV-NN; Status-Quo Carrying Cost present for every finding.
`Step 4 STATUS: done / blocked — [reason]`

---

**Step 5 — Amendment pass.**

Review all recovery paths: minimum two actor-labeled steps each. Check all nil findings —
if any was superseded by a later finding, annotate it SUPERSEDED with the finding ID. Check
all DCV findings — if any arrived late (after the gap section was written), add a sub-step
amendment record.

| AMD ID | Entry ID | Original (summary) | Amended (summary) | Rule Invoked | Step Re-Opened? |
|---|---|---|---|---|---|

No amendments: `Step 5: no amendments. No step re-opens triggered.`

`Step 5 STATUS: done / blocked — [reason]`

---

**DS Expert — Rule Registry Audit.**

Scan every rule. For each: how many times did it fire? At which step and entry ID? If it
didn't fire — was the condition absent (SCENARIO-ABSENT) or did the condition arise but
the rule wasn't applied (RULE-BYPASSED)?

| Rule ID | Invocations | Citations (step, entry) | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-CR-DCV | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | [empty or trigger citation] |
| RULE-BARRED-CG | | | | |
| RULE-NIL-SUPERSEDE | | | | |

BYPASS-TRIGGER non-empty → invoke bypass protocol before DS Expert sign-off.

REGISTRY AUDIT (DS Expert) COMPLETE: [no RULE-BYPASSED entries remain]

---

**DS Expert — Nil Supersession Log.**

| Nil ID | Gap Type | State | Superseded By | Step |
|---|---|---|---|---|

No supersessions: `No supersessions in this run.`

---

**DS Expert — Scope Verification.**

| Declared Operation | Covered | Gap Finding |
|---|---|---|
| [operation] | Yes / No | SV-GAP-NN / — |

SCOPE VERIFICATION COMPLETE

---

```
DS EXPERT SIGN-OFF
Steps completed: 1 / 1b / 2 / 3 / 4 / 5 / Registry Audit / Nil Log / Scope Verification
All steps done: [yes / list unresolved]
No RULE-BYPASSED entries unresolved: [yes / exception]
DS EXPERT STATUS: CLOSED / OPEN
```

---

```
COMMERCE VALIDATOR — begin only when DS EXPERT STATUS: CLOSED
```

**Step 6 — Commerce domain validation.**

For each Include scenario: is it anchored to a named commerce operation? If not, invoke
RULE-COMMERCE-ANCHOR — amend to name the operation, record the amendment.

Check four targets (name each as present or absent with rationale):
- Inventory oversell under partition
- Payment idempotency window expiry
- Loyalty point double-redemption under split-brain
- Order state divergence under partial fulfillment failure

| Scenario ID | Commerce Operation Named? | Amended Operation | CV Finding Issued |
|---|---|---|---|
| FS-01 | Yes / No | | — / CV-DCV-01 / CV-OEG-01 / CV-MRF-01 |

`Step 6 STATUS: done / blocked — [reason]`

---

**Commerce Validator — Rule Registry Audit.**

| Rule ID | Invocations | Citations | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-COMMERCE-ANCHOR | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | [empty or trigger] |

BYPASS-TRIGGER non-empty → invoke bypass protocol before Commerce Validator sign-off.

REGISTRY AUDIT (Commerce Validator) COMPLETE

---

**Step 7 — Inertia synthesis.**

Per-finding carrying cost (from Step 4 Status-Quo Carrying Cost): for each named gap —
failure mode, rate, horizon, metric. One entry per finding.

Overall synthesis:
- Urgency: HIGH / MEDIUM / LOW
- Highest-risk finding: [gap ID] — [carrying cost]
- Status-quo option: [specific to `{topic}` — what "do nothing" looks like]
- Intervention recommendation: [owner + threshold + consequence of missing threshold]

---

```
COMMERCE VALIDATOR SIGN-OFF
Steps completed: 6 / Registry Audit / 7 (Inertia)
All steps done: [yes]
No RULE-BYPASSED entries unresolved: [yes / exception]
COMMERCE VALIDATOR STATUS: CLOSED / OPEN
```

ANALYSIS COMPLETE (DS EXPERT STATUS: CLOSED AND COMMERCE VALIDATOR STATUS: CLOSED)

---

---

## V-04

**Variation axis**: Role sequence + lifecycle emphasis — A third act is added: Act 3, the
SRE Reliability Expert. Acts run in strict sequence: DS Expert (Act 1) → Commerce Domain
Validator (Act 2) → SRE Reliability Expert (Act 3). Act 3 takes the enumerated Include
scenarios from Gate 1 (Act 1 output) and the named gap findings from Gate 3 (Act 1 output)
as its inputs, then produces two gated outputs: Gate 6 (Chaos Engineering Specification —
one row per Include scenario) and Gate 7 (Observability Manifest — one row per named gap
finding). RULE-CHAOS-INJECT and RULE-OBS-GAP are added to the Rule Registry, owned by the
SRE Expert. Both rules are subject to the standard bypass mechanism: a scenario without a
chaos row is RULE-CHAOS-INJECT RULE-BYPASSED; a gap finding without an Observable Signal is
RULE-OBS-GAP RULE-BYPASSED.

**Hypothesis**: Separating operational concerns (chaos testing, observability) into a
dedicated third act prevents them from being elided in the DS Expert's token-budget pressure
during Gates 2–4. When RULE-CHAOS-INJECT and RULE-OBS-GAP are registered rules with named
bypass owners (SRE Expert), their absence triggers the same gate-reopening chain that governs
RULE-CR-DCV and RULE-BARRED-CG — making operational coverage structurally enforced rather
than aspirational. An Act 3 Operational Readiness Declaration (pre-Gate 6) commits to
coverage minimums before scenario and gap enumeration begins in that act, parallel to Act
1's Coverage Accountability Roster.

---

You are running the **flow-resilience** skill for `{topic}`.

This analysis runs in three sequential acts:
- Act 1 — Distributed Systems Expert: failure mode discovery, scenario analysis, gap
  identification
- Act 2 — Commerce Domain Validator: commerce anchoring, domain completeness check
- Act 3 — SRE Reliability Expert: chaos engineering specification, observability manifest

Each act closes with a formal sign-off. Do not begin an act until the prior act is CLOSED.

---

### RULE REGISTRY

| Rule ID | Trigger Condition | Action Required | Bypass Owner |
|---|---|---|---|
| RULE-CR-DCV | Concurrent state modification by multiple actors without a coordination mechanism | Emit DCV-NN in Gate 3; cite rule inline | DS Expert (Act 1) |
| RULE-BARRED-CG | Discovery entry confidence basis cannot be resolved | Mark BARRED; emit CG-NN | DS Expert (Act 1) |
| RULE-NIL-SUPERSEDE | Downstream finding supersedes a typed nil | Annotate nil SUPERSEDED with finding ID | DS Expert (Act 1) |
| RULE-COMMERCE-ANCHOR | Include scenario has no named commerce operation | Amend to name operation | Commerce Validator (Act 2) |
| RULE-CHAOS-INJECT | Include scenario from Gate 1 has no chaos test row in Gate 6 | Emit CE-NN in Gate 6 bypass block; produce Inject / Expected Observable / Pass-Fail Signal | SRE Expert (Act 3) |
| RULE-OBS-GAP | Named gap finding from Gate 3 has no Observable Signal entry in Gate 7 | Emit OS-NN in Gate 7 bypass block; produce named signal + rationale | SRE Expert (Act 3) |

**Bypass Owner column**: Cross-act invocation is not permitted. SRE Expert cannot reopen
Act 1 or Act 2 gates. DS Expert and Commerce Validator cannot reopen Act 3 gates.

---

### BYPASS GATE-REOPENING PROTOCOL

**Authority**: Each rule's Bypass Owner is the sole authorized actor for that rule's
gate-reopening chain. Cross-act invocation not permitted.

When any rule shows RULE-BYPASSED in its act's Post-Analysis Rule Registry Audit:

1. Bypass Owner emits: `GATE N-bypass: REOPENED — [rule ID] — bypass at [gate, entry ID]`
2. Bypass Owner applies the rule and produces required output.
3. Bypass Owner emits: `GATE N-bypass: AMENDED — CLOSED — [rule now applied]`
4. Bypass Owner updates the audit row: Status → INVOKED; BYPASS-TRIGGER →
   "RESOLVED — [sub-gate]"; Citations += sub-gate.

**COMPLETE may not be declared** while any RULE-BYPASSED entry remains unresolved in any act.

---

### ANTI-OMISSION ARCHITECTURE

| Level | Anti-Omission Mechanism | Omission Risk Targeted | Mechanism Location |
|---|---|---|---|
| Table | Unified row index (`#`) + anti-split instruction | Row fragmentation across ownership transitions | `#` column; anti-split in Gate 2 |
| Section | Phase gate — all rows complete before Gap Identification | Premature section advance | Section gate in Gate 2 |
| Slot | In-row bold imperative: **"Write this row now."** / **"Do not advance to Row N+1 until..."** | Row omission under token pressure | Row Descriptors |
| Column-Group | Intra-row phase gate: C-phase columns complete before D-phase begins within the same row | Mid-row D-phase omission on ownership shift | Row Descriptors: Column-Group Gate |
| Column | Column ownership per header in Column Contract | Individual column omission | Column Contract |

**Anti-split instruction**: Single scenario table. No breaks or sub-tables when ownership
shifts within a row.

---

### COLUMN CONTRACT

| Column Name | Owner | Phase | Fill Requirement |
|---|---|---|---|
| `#` | Shared | — | Sequential integer; no gaps |
| `ID` | Shared | — | FS-NN; unique per scenario |
| `Trigger Condition` | DS Expert | C-phase | Threshold expression (quantified activation condition) + detection signal (named observable confirming threshold crossing). Qualitative descriptions without threshold expression fail. |
| `State` | Commerce Expert | C-phase | Specific system configuration; named components and states |
| `Capability` | Commerce Expert | C-phase | Named commerce operations still completable |
| `Data at Risk` | DS Expert | D-phase | Named data type + consistency failure mode |
| `Recovery Path` | DS Expert | D-phase | Four stages each with: mechanism (named actor) \| SLA target \| VS (Verification Signal — named observable confirming stage completion). VS must be named, observable, distinct from mechanism. |
| `Severity` | DS Expert | D-phase | `degraded` / `impaired` / `down` |
| `Blast Radius` | DS Expert | D-phase | Fraction or named segment |
| `Rule Applied` | DS Expert | D-phase | Rule ID or `—` |

---

### Pre-Analysis: Commerce Operation Scope Declaration

```
SCOPE DECLARATION
Operations in scope: [minimum four: checkout / inventory reservation / payment processing /
order fulfillment / cart state / loyalty redemption / return-refund]
Operations excluded (with reason): [list or "none"]
SCOPE DECLARATION COMPLETE
```

### Pre-Analysis: Coverage Accountability Roster

| Degradation Class | Committed Minimum | DS Primitive for Impossibility |
|---|---|---|
| Network partition / offline | 2 | [required if slot unfillable] |
| Partial service failure | 2 | |
| Eventual consistency | 2 | |

---

```
ACT 1 OPEN — Distributed Systems Expert
Scope: Gates 1–4 + Act 1 Registry Audit + Nil Supersession Log + Scope Verification +
       ACT 1 CLOSE
```

### GATE 1: Discovery and Triage

```
GATE 1 OPEN
Preconditions:
  [ ] SCOPE DECLARATION COMPLETE present
  [ ] Coverage Accountability Roster committed
Entry confirmed: [yes / no]
```

| # | ID | Failure Class | Confidence Basis | Disposition | Rule Applied | Notes |
|---|---|---|---|---|---|---|
| 1 | FS-01 | | | Include / BARRED / Argued-Impossible | RULE-BARRED-CG or — | |

BARRED: cite RULE-BARRED-CG; emit CG-NN.
Argued-Impossible: name DS Primitive. Topic-scope arguments are not DS Primitives.

**Gate 1b — BARRED Resolution**

| BARRED ID | Confidence Basis | Resolved? | Resolution Mechanism | New Disposition |
|---|---|---|---|---|

No BARRED entries: `Gate 1b: none.`

```
GATE 1 CLOSE
Exit postconditions:
  [ ] Every candidate has one named disposition
  [ ] Every BARRED has CG-NN; every Argued-Impossible cites DS Primitive
  [ ] Roster counts updated
Gate 1 STATUS: CLOSED / OPEN — [reason if open]
```

---

### GATE 2: Four-Field Scenario Analysis

```
GATE 2 OPEN
Preconditions:
  [ ] Gate 1 STATUS: CLOSED
Entry confirmed: [yes / no]
```

**Anti-split**: Single table. No sub-tables by ownership. No breaks between rows.

**Section gate**: All scenario rows before Gap Identification.

**Column-group gate**: C-phase columns (Trigger Condition, State, Capability) complete
before D-phase columns begin within each row.

#### Row Descriptors

**Row 1 — FS-01: [Scenario Name]**

Consequence context: [acute consequences per resolution branch]. Chronic if never addressed:
[rate] / [horizon] / [metric accumulates].

**Write this row now.**
Fill Trigger Condition (threshold expression + detection signal). C-phase (Commerce Expert):
State and Capability.
**C-phase complete check: do not begin D-phase until Trigger Condition, State, Capability
are non-placeholder.**
D-phase (DS Expert): Data at Risk; Recovery Path (all four stages: mechanism | actor | SLA
target | VS — VS must be named observable distinct from mechanism); Severity; Blast Radius;
Rule Applied.
**Do not advance to Row 2 until all columns including all four VS entries are
non-placeholder.**

---

**Row 2 — FS-02: [Scenario Name]**

Consequence context: [payment idempotency / loyalty double-redemption / order divergence].
Chronic: [backlog / ceiling / metric accumulates].

**Write this row now.**
Fill all columns per Column Contract.
**C-phase complete check before D-phase. Do not advance to Row 3 until all columns
non-placeholder.**

---

Continue for all remaining Include scenarios.

| # | ID | Trigger Condition | State | Capability | Data at Risk | Recovery Path | Severity | Blast Radius | Rule Applied |
|---|---|---|---|---|---|---|---|---|---|
| 1 | FS-01 | [threshold] / [detection] | | | | Detect: [mech\|actor\|TTD\|VS]; Contain: [mech\|actor\|TTC\|VS]; Recover: [mech\|actor\|TTR\|VS]; Validate: [mech\|actor\|TTV\|VS] | | | |

```
GATE 2 CLOSE
Exit postconditions:
  [ ] All Include scenarios in table with all columns non-trivial
  [ ] Every Trigger Condition has threshold expression + detection signal
  [ ] Every recovery path has four stages each with mechanism, SLA target, named VS
  [ ] Column-group gate confirmed for every row
Gate 2 STATUS: CLOSED / OPEN — [reason if open]
```

---

### GATE 3: Gap Identification

```
GATE 3 OPEN
Preconditions:
  [ ] Gate 2 STATUS: CLOSED
Entry confirmed: [yes / no]
```

**OEG — Offline Experience Gaps**

| ID | Scenario Ref | Gap Description | Status-Quo Carrying Cost | Actionable Recommendation |
|---|---|---|---|---|
| OEG-01 | FS-NN | | [rate \| horizon \| user failure] | |

No OEG: `OEG-NIL-1: [scope rationale]`

**DCV — Data Consistency Violations**

| ID | Source | Data Type | Failure Mode | Conflict Resolution | Adequacy | Status-Quo Carrying Cost | Rule Applied |
|---|---|---|---|---|---|---|---|
| DCV-01 | FS-NN | | | LWW / merge / manual / reject-stale / undefined | adequate / inadequate / undefined | [rate \| horizon \| metric] | |

No DCV: `DCV-NIL-1: [scope rationale]`

**MRF — Missing Recovery Flows**

| ID | Scenario Ref | Absent Mechanism | Status-Quo Carrying Cost | Why No Current Path Exists |
|---|---|---|---|---|
| MRF-01 | FS-NN | | [rate \| horizon \| failure] | |

No MRF: `MRF-NIL-1: [scope rationale]`

```
GATE 3 CLOSE
Exit postconditions:
  [ ] All three gap categories present; every finding or typed nil with scope rationale
  [ ] Status-Quo Carrying Cost present for every named finding
  [ ] All RULE-CR-DCV entries assigned DCV-NN
Gate 3 STATUS: CLOSED / OPEN — [reason if open]
```

---

### GATE 4: Amendment Pass

```
GATE 4 OPEN
Preconditions:
  [ ] Gate 3 STATUS: CLOSED
Entry confirmed: [yes / no]
```

| AMD ID | Entry ID | Original | Amended | Rule Invoked | Gate Re-Opened? |
|---|---|---|---|---|---|

No amendments: `Gate 4: no amendments. No gate re-opens triggered.`

```
GATE 4 CLOSE
Exit postconditions:
  [ ] Recovery paths have minimum two actor-labeled steps
  [ ] Superseded nils annotated SUPERSEDED with finding ID
Gate 4 STATUS: CLOSED / OPEN — [reason if open]
```

---

### Act 1 Terminal: Post-Analysis Rule Registry Audit

| Rule ID | Invocations | Citations (gate, entry) | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-CR-DCV | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | [empty or trigger] |
| RULE-BARRED-CG | | | | |
| RULE-NIL-SUPERSEDE | | | | |

BYPASS-TRIGGER non-empty → invoke bypass protocol before ACT 1 CLOSE.

POST-ANALYSIS REGISTRY AUDIT (ACT 1) COMPLETE

---

### Act 1 Terminal: Nil Supersession Log

| Nil ID | Gap Type | State | Superseded By | Gate |
|---|---|---|---|---|

No supersessions: `No supersessions in this run.`

---

### Act 1 Terminal: Scope Verification

| Declared Operation | Covered | Gap Finding |
|---|---|---|
| [operation] | Yes / No | SV-GAP-NN / — |

SCOPE VERIFICATION COMPLETE

---

```
ACT 1 CLOSE (sign-off)
(1) All gates within Act 1 CLOSED:
    Gate 1: [CLOSED / OPEN]; Gate 1b: [CLOSED / N/A]
    Gate 2: [CLOSED / OPEN]; Gate 3: [CLOSED / OPEN]
    Gate 4: [CLOSED / OPEN]; GATE N-bypass blocks: [CLOSED / none]
    Act 1 Registry Audit: [CLOSED / OPEN]
(2) Act 1 scope exhausted: [yes / list unresolved]
(3) No RULE-BYPASSED remain in Act 1: [yes / exception]
ACT 1 STATUS: CLOSED / OPEN
```

---

```
ACT 2 OPEN — Commerce Domain Validator
Entry condition: ACT 1 STATUS: CLOSED
```

### GATE 5: Commerce Domain Validation

```
GATE 5 OPEN
Preconditions:
  [ ] ACT 1 STATUS: CLOSED
Entry confirmed: [yes / no]
```

| Scenario ID | Commerce Operation Named? | Amended Operation | CV Finding Issued |
|---|---|---|---|
| FS-01 | Yes / No | | — / CV-DCV-01 |

Targets: inventory oversell / payment idempotency / loyalty double-redemption / order
divergence — each: [present / absent — rationale].

```
GATE 5 CLOSE
Exit postconditions:
  [ ] Every scenario anchored to commerce operation
  [ ] All four targets checked
Gate 5 STATUS: CLOSED / OPEN — [reason if open]
```

### Act 2 Terminal: Post-Analysis Rule Registry Audit

| Rule ID | Invocations | Citations | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-COMMERCE-ANCHOR | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | [empty or trigger] |

POST-ANALYSIS REGISTRY AUDIT (ACT 2) COMPLETE

---

### Inertia Synthesis

Per-finding carrying cost: for each named gap — failure mode, rate, horizon, metric.

Overall synthesis:
Urgency: HIGH / MEDIUM / LOW
Highest-risk finding: [gap ID] — [carrying cost]
Status-quo option: [specific to `{topic}`]
Intervention recommendation: [owner + threshold + consequence]

```
ACT 2 CLOSE (sign-off)
(1) Gate 5 / bypass blocks / Registry Audit: all CLOSED
(2) Act 2 scope exhausted: [yes]
(3) No RULE-BYPASSED remain in Act 2: [yes / exception]
ACT 2 STATUS: CLOSED / OPEN
```

---

```
ACT 3 OPEN — SRE Reliability Expert
Entry condition: ACT 2 STATUS: CLOSED
Scope: Operational Readiness Declaration + Gates 6–7 + Act 3 Registry Audit + ACT 3 CLOSE
Inputs from Act 1:
  - Include scenario list from Gate 1 (IDs: FS-01, FS-02, ...)
  - Named gap findings from Gate 3 (IDs: OEG-NN, DCV-NN, MRF-NN)
```

### Pre-Act 3: Operational Readiness Declaration

Before writing Gate 6 or Gate 7, declare coverage commitments:

```
OPERATIONAL READINESS DECLARATION
Chaos test coverage commitment: one row per Include scenario from Gate 1
  Scenarios to cover: [list FS-IDs from Gate 1]
  Scenarios where chaos test is architecturally impossible (DS Primitive required):
  [list or "none"]
Observability coverage commitment: one Observable Signal per named gap from Gate 3
  Gaps to cover: [list OEG/DCV/MRF IDs from Gate 3]
  Gaps where observable signal is unknown (emit MRF-OBS-NN required):
  [list or "none — all gaps have known observability signals"]
OPERATIONAL READINESS DECLARATION COMPLETE
```

---

### GATE 6: Chaos Engineering Specification

```
GATE 6 OPEN
Preconditions:
  [ ] ACT 2 STATUS: CLOSED
  [ ] OPERATIONAL READINESS DECLARATION COMPLETE
  [ ] Include scenario list from Gate 1 available
Entry confirmed: [yes / no]
```

For each Include scenario from Gate 1, produce one row. Three required fields:

- **Trigger Condition Reference**: copy the threshold expression from Gate 2 for this
  scenario ID. The chaos test activates at this boundary.
- **Inject**: named fault type + mechanism + parameters. Generic descriptions fail.
- **Expected Observable**: in-fault system behavior at named observation granularity.
- **Pass-Fail Signal**: the binary named artifact (metric, response code, log entry) that
  terminates the test with a definite outcome.

If RULE-CHAOS-INJECT fires (scenario from Gate 1 has no chaos row): emit CE-NN in a bypass
block before declaring Gate 6 CLOSED.

| # | Scenario ID | Trigger Condition Reference | Inject | Expected Observable | Pass-Fail Signal |
|---|---|---|---|---|---|
| 1 | FS-01 | [threshold from Gate 2] | | | |

```
GATE 6 CLOSE
Exit postconditions:
  [ ] One row per Include scenario from Gate 1
  [ ] Every row has Trigger Condition Reference citing Gate 2 threshold
  [ ] Every row has Inject with named fault type, mechanism, parameter
  [ ] Every row has Expected Observable at named granularity
  [ ] Every row has Pass-Fail Signal naming binary artifact
Gate 6 STATUS: CLOSED / OPEN — [reason if open]
```

---

### GATE 7: Observability Manifest

```
GATE 7 OPEN
Preconditions:
  [ ] Gate 6 STATUS: CLOSED
  [ ] Named gap list from Gate 3 available
Entry confirmed: [yes / no]
```

For each named gap finding from Gate 3 (OEG-NN, DCV-NN, MRF-NN), produce one row:

- **Gap ID**: reference to the Gate 3 finding
- **Observable Signal**: named metric, log pattern, trace attribute, or alert condition
  that would surface this gap in production. Must be named to observable granularity
  (e.g., "cart-session-divergence-count > 0 per session monitored via inventory-service
  /metrics endpoint"). Generic signals fail.
- **Detection Horizon**: estimated time from gap onset to signal firing (e.g., "< 30s if
  sampled at 15s interval"; "session-scoped — fires at next cart load").
- **Rationale**: one sentence explaining why this signal surfaces the gap before user
  impact.

If RULE-OBS-GAP fires (gap finding has no known observable signal): emit OS-NN in a bypass
block and emit MRF-OBS-NN in the observability manifest — the gap is undetectable in
production, which is itself a missing recovery flow.

| # | Gap ID | Observable Signal | Detection Horizon | Rationale |
|---|---|---|---|---|
| 1 | OEG-01 | | | |
| 2 | DCV-01 | | | |

```
GATE 7 CLOSE
Exit postconditions:
  [ ] One row per named gap finding from Gate 3
  [ ] Every row has Observable Signal named to observable granularity
  [ ] Every row has Detection Horizon and Rationale
  [ ] Gaps with no known observable have MRF-OBS-NN emitted
Gate 7 STATUS: CLOSED / OPEN — [reason if open]
```

---

### Act 3 Terminal: Post-Analysis Rule Registry Audit

| Rule ID | Invocations | Citations (gate, entry) | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-CHAOS-INJECT | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | [empty or trigger] |
| RULE-OBS-GAP | | | | |

BYPASS-TRIGGER non-empty → invoke bypass protocol before ACT 3 CLOSE.

POST-ANALYSIS REGISTRY AUDIT (ACT 3) COMPLETE

---

```
ACT 3 CLOSE (sign-off)
(1) All gates within Act 3 CLOSED:
    Gate 6: [CLOSED / OPEN — reason]
    Gate 7: [CLOSED / OPEN — reason]
    GATE N-bypass blocks (if triggered): [CLOSED / none]
    Act 3 Registry Audit: [CLOSED / OPEN]
(2) Act 3 scope exhausted: [yes — chaos rows written for all Include scenarios; observable
    signals written for all named gap findings]
(3) No RULE-BYPASSED remain in Act 3: [yes / exception]
ACT 3 STATUS: CLOSED / OPEN
```

ANALYSIS COMPLETE (declared only when ACT 1, ACT 2, and ACT 3 STATUS: CLOSED)

---

---

## V-05

**Variation axis**: Full integration — chaos engineering and observability hooks are
integrated at every structural level. Gate 2b (Chaos Engineering Table, from V-01) is
inserted between Gate 2 and Gate 3. Gate 3 gap tables carry an Observable Signal column
(from V-02). RULE-CHAOS-INJECT and RULE-OBS-GAP are added to the Rule Registry (from V-04),
owned by DS Expert (Act 1) — both rules are subject to the same bypass mechanism that
governs Act 1 rules, not isolated in a separate act. The chaos test activation threshold is
linked to the Trigger Condition from Gate 2 (from V-01). Observability absence generates
MRF-OBS-NN findings (from V-02). The post-analysis registry audit covers all six rules. A
Chaos-Observability Coverage Matrix in Act 1 Terminal cross-references chaos coverage and
observability coverage across all Include scenarios and gap findings.

**Hypothesis**: Full integration via the rule-bypass machinery (rather than a separate act
or optional section) produces the strongest structural enforcement of C-09 and C-10. When
RULE-CHAOS-INJECT and RULE-OBS-GAP are registered in the same registry as RULE-CR-DCV and
RULE-BARRED-CG, their bypass conditions trigger the same gate-reopening chain — making
operational coverage as structurally mandatory as data-consistency and confidence-triage
coverage. The Chaos-Observability Coverage Matrix is a new excellence signal: it creates a
joint falsifiability view where each row shows whether a scenario has both a chaos test and
an observability hook for its gap, enabling a reader to verify operational completeness in
O(1) rather than by cross-referencing Gate 2b against Gate 3.

---

You are running the **flow-resilience** skill for `{topic}`.

This analysis runs in two sequential acts. Act 1 is the Distributed Systems Expert.
Act 2 is the Commerce Domain Validator. Each act closes with a formal sign-off.
Do not blend the acts.

---

### RULE REGISTRY

| Rule ID | Trigger Condition | Action Required | Bypass Owner |
|---|---|---|---|
| RULE-CR-DCV | Concurrent state modification by multiple actors without a coordination mechanism | Emit DCV-NN in Gate 3; cite rule inline at trigger point | DS Expert (Act 1) |
| RULE-BARRED-CG | Discovery entry confidence basis cannot be resolved from available context | Mark BARRED; emit CG-NN in coverage log | DS Expert (Act 1) |
| RULE-NIL-SUPERSEDE | Downstream finding introduced in a category that held a typed nil | Annotate nil SUPERSEDED citing new finding ID | DS Expert (Act 1) |
| RULE-CHAOS-INJECT | Include scenario from Gate 1 has no chaos test row in Gate 2b at Gate 2b CLOSE | Emit CE-NN in Gate 2b bypass block; produce all three required chaos test components for the scenario | DS Expert (Act 1) |
| RULE-OBS-GAP | Named gap finding in Gate 3 has no Observable Signal entry at Gate 3 CLOSE | Emit OS-NN in Gate 3 bypass block; produce named signal + detection horizon + rationale; if no signal exists, emit MRF-OBS-NN | DS Expert (Act 1) |
| RULE-COMMERCE-ANCHOR | Include scenario references a generic operation with no named commerce flow | Amend to name specific operation; record amendment | Commerce Validator (Act 2) |

**Bypass Owner column**: Cross-act invocation is not permitted. Commerce Validator cannot
reopen Act 1 gates. DS Expert cannot reopen Act 2 gates.

---

### BYPASS GATE-REOPENING PROTOCOL

**Authority**: DS Expert owns this protocol for Act 1 rules (including RULE-CHAOS-INJECT
and RULE-OBS-GAP); Commerce Validator for Act 2 rules. Cross-act invocation not permitted.

When any rule shows RULE-BYPASSED in the Post-Analysis Rule Registry Audit:

1. Bypass Owner emits: `GATE N-bypass: REOPENED — [rule ID] — bypass at [gate, entry ID]`
2. Bypass Owner applies the rule: produces CE-NN chaos row, OS-NN observability entry,
   DCV-NN, CG-NN, SUPERSEDED annotation, or commerce anchor amendment as required.
3. Bypass Owner emits: `GATE N-bypass: AMENDED — CLOSED — [rule now applied]`
4. Bypass Owner updates the audit row: Status → INVOKED; BYPASS-TRIGGER →
   "RESOLVED — [sub-gate]"; Citations += sub-gate.

**COMPLETE may not be declared** while any RULE-BYPASSED entry remains unresolved in any act.

---

### ANTI-OMISSION ARCHITECTURE

| Level | Anti-Omission Mechanism | Omission Risk Targeted | Mechanism Location |
|---|---|---|---|
| Table | Unified row index (`#`) + anti-split instruction | Row fragmentation across ownership transitions | `#` column; anti-split in Gate 2 |
| Section | Phase gate — all rows complete before Gap Identification | Premature section advance | Section gate in Gate 2 |
| Slot | In-row bold imperative: **"Write this row now."** / **"Do not advance to Row N+1 until..."** | Row omission under token pressure | Row Descriptors |
| Column-Group | Intra-row phase gate: C-phase columns complete before D-phase begins within the same row | Mid-row D-phase omission on ownership shift | Row Descriptors: Column-Group Gate |
| Column | Column ownership per header in Column Contract | Individual column omission | Column Contract |

**Anti-split instruction**: Single scenario table in Gate 2. No sub-tables or breaks between
rows when ownership shifts.

---

### COLUMN CONTRACT

Place this table before any scenario output. Every column in the Gate 2 scenario table must
have an entry here.

| Column Name | Owner | Phase | Fill Requirement |
|---|---|---|---|
| `#` | Shared | — | Sequential integer; no gaps |
| `ID` | Shared | — | FS-NN format; unique per scenario |
| `Trigger Condition` | DS Expert | C-phase | **Two required components**: (1) threshold expression — quantified activation condition (e.g., "inventory count falls below safety-stock threshold", "payment API p99 latency > 500ms"); (2) detection signal — named observable mechanism confirming threshold crossing (e.g., "inventory-service health probe returns degraded", "payment-provider timeout counter exceeds N/window"). The threshold expression is also used as the activation condition in Gate 2b (chaos test). Qualitative descriptions without threshold expression fail. |
| `State` | Commerce Expert | C-phase | Specific system configuration; named components and states; not "degraded" |
| `Capability` | Commerce Expert | C-phase | Named commerce operations the user can still complete |
| `Data at Risk` | DS Expert | D-phase | Named data type + consistency failure mode |
| `Recovery Path` | DS Expert | D-phase | Four stages each with three required components: mechanism (named actor) \| SLA target \| VS (Verification Signal — named observable artifact confirming stage completion independent of SLA elapse). Format: Detect (mech \| actor \| TTD \| VS: [named observable]); Contain (mech \| actor \| TTC \| VS: [named]); Recover (mech \| actor \| TTR \| VS: [named]); Validate (mech \| actor \| TTV \| VS: [named]). VS must be named, observable (system state / log / metric / response code), and distinct from the mechanism. |
| `Severity` | DS Expert | D-phase | `degraded` / `impaired` / `down` |
| `Blast Radius` | DS Expert | D-phase | Fraction or named segment |
| `Rule Applied` | DS Expert | D-phase | Rule ID or `—` |

---

### Pre-Analysis: Commerce Operation Scope Declaration

Declare before Gate 1. Minimum four operations from: checkout, inventory reservation,
payment processing, order fulfillment, cart state, loyalty redemption, return/refund.

```
SCOPE DECLARATION
Operations in scope: [list each]
Operations explicitly excluded (with reason): [list or "none"]
SCOPE DECLARATION COMPLETE
```

### Pre-Analysis: Coverage Accountability Roster

| Degradation Class | Committed Minimum | DS Primitive for Impossibility |
|---|---|---|
| Network partition / offline | 2 | [required if slot unfillable] |
| Partial service failure | 2 | |
| Eventual consistency | 2 | |

---

```
ACT 1 OPEN — Distributed Systems Expert
Scope: Gates 1–4 + Gate 2b + Act 1 Registry Audit + Nil Supersession Log +
       Chaos-Observability Coverage Matrix + Scope Verification + ACT 1 CLOSE
```

### GATE 1: Discovery and Triage

```
GATE 1 OPEN
Preconditions:
  [ ] SCOPE DECLARATION COMPLETE present
  [ ] Coverage Accountability Roster committed
Entry confirmed: [yes / no]
```

| # | ID | Failure Class | Confidence Basis | Disposition | Rule Applied | Notes |
|---|---|---|---|---|---|---|
| 1 | FS-01 | | | Include / BARRED / Argued-Impossible | RULE-BARRED-CG or — | |

BARRED: cite RULE-BARRED-CG; emit CG-NN.
Argued-Impossible: name DS Primitive. Topic-scope arguments are not DS Primitives.

**Gate 1b — BARRED Resolution**

| BARRED ID | Confidence Basis | Resolved? | Resolution Mechanism | New Disposition |
|---|---|---|---|---|

No BARRED entries: `Gate 1b: none.`

```
GATE 1 CLOSE
Exit postconditions:
  [ ] Every candidate has one named disposition
  [ ] Every BARRED has CG-NN; every Argued-Impossible cites DS Primitive
  [ ] Roster counts updated
Gate 1 STATUS: CLOSED / OPEN — [reason if open]
```

---

### GATE 2: Four-Field Scenario Analysis

```
GATE 2 OPEN
Preconditions:
  [ ] Gate 1 STATUS: CLOSED
Entry confirmed: [yes / no]
```

**Anti-split**: Single scenario table. No sub-tables by ownership. No breaks between rows.

**Section gate**: All scenario rows before Gap Identification.

**Column-group gate**: C-phase columns (Trigger Condition, State, Capability) complete
before D-phase columns begin within each row. Confirmed inline in each row descriptor.

#### Row Descriptors

**Row 1 — FS-01: [Scenario Name]**

Consequence context: [acute consequences per resolution branch — oversell / double-charge /
duplicate fulfillment]. Chronic if never addressed: [rate] / [horizon: unbounded] / [metric
accumulates].

**Write this row now.**
Fill Trigger Condition: (1) threshold expression naming the quantified activation condition;
(2) detection signal naming the observable mechanism confirming the threshold is crossed.
This threshold expression will be referenced in Gate 2b as the chaos test activation
boundary for this scenario.
C-phase (Commerce Expert): fill State (exact system configuration, named components) and
Capability (named operations still completable).
**C-phase complete check: do not begin D-phase columns until Trigger Condition, State,
Capability are non-placeholder.**
D-phase (DS Expert): fill Data at Risk, Recovery Path (all four stages: mechanism | actor |
SLA target | VS — VS is the named observable confirming stage completion, distinct from
mechanism, non-generic), Severity, Blast Radius, Rule Applied.
**Do not advance to Row 2 until all columns including both Trigger Condition components and
all four VS entries are non-placeholder.**
Example VS entries: Detect VS — "inventory-service health probe returns degraded"; Contain
VS — "reserve-lock-count metric increments, confirming lock acquired"; Recover VS —
"inventory-service heartbeat returns 200 for 30s"; Validate VS — "inventory-accuracy metric
returns to baseline ± 0.5%."

---

**Row 2 — FS-02: [Scenario Name]**

Consequence context: [payment idempotency miss → double-charge; loyalty double-redemption
under split-brain; order state divergence under partial fulfillment]. Chronic: reconciliation
backlog / without ceiling / dispute-count accumulates.

**Write this row now.**
Fill Trigger Condition (threshold expression + detection signal — threshold will be
referenced in Gate 2b). Fill all columns per Column Contract.
**C-phase complete check before D-phase. Do not advance to Row 3 until all columns
non-placeholder including all four VS entries.**

---

Continue this pattern for all remaining Include scenarios.

Scenario table:

| # | ID | Trigger Condition | State | Capability | Data at Risk | Recovery Path | Severity | Blast Radius | Rule Applied |
|---|---|---|---|---|---|---|---|---|---|
| 1 | FS-01 | [threshold] / [detection signal] | | | | Detect: [mech\|actor\|TTD\|VS]; Contain: [mech\|actor\|TTC\|VS]; Recover: [mech\|actor\|TTR\|VS]; Validate: [mech\|actor\|TTV\|VS] | | | |

```
GATE 2 CLOSE
Exit postconditions:
  [ ] Every Include scenario has all columns non-trivial
  [ ] Every Trigger Condition has threshold expression + detection signal
  [ ] Every recovery path has four stages each with mechanism, SLA target, named VS
  [ ] All RULE-CR-DCV triggers recorded
  [ ] Column-group gate confirmed for every row
Gate 2 STATUS: CLOSED / OPEN — [reason if open]
```

---

### GATE 2b: Chaos Engineering Specification

```
GATE 2b OPEN
Preconditions:
  [ ] Gate 2 STATUS: CLOSED
  [ ] Include scenario list from Gate 1 available (IDs: FS-01, FS-02, ...)
Entry confirmed: [yes / no]
```

For each Include scenario from Gate 1, write one row. Four required fields:

- **Trigger Condition Reference**: copy the threshold expression from the Gate 2 Trigger
  Condition column for this scenario. The chaos test activates when this threshold is
  crossed — the same boundary as the monitoring spec. Do not invent a separate activation
  condition.

- **Inject**: the specific fault to introduce. Format: `[fault type]: [named mechanism] —
  [parameter]`. Examples: "Network partition: block all TCP egress from payment-service
  pod — duration: 60s"; "Latency spike: inject 2000ms delay at payment-provider ingress —
  rate: 100%"; "Service kill: SIGTERM inventory-service — restart policy: manual". Generic
  descriptions ("make the service fail") are not valid.

- **Expected Observable**: what the system exhibits during the fault, at named observation
  granularity. This is in-fault behavior, not post-recovery state. Example: "Checkout
  endpoint returns HTTP 503 with Retry-After: 30 header; no silent data loss; cart state
  preserved in local storage."

- **Pass-Fail Signal**: the binary artifact that terminates the test with a definite named
  outcome. Must name a specific metric value, API response code, log entry, or system state.
  Example: "PASS if payment-duplicate-charge-count == 0 and no order with status
  'duplicate-created' appears in order-service audit log; FAIL otherwise." Generic
  outcomes ("system handles it correctly") fail.

If any Include scenario lacks a chaos row at Gate 2b CLOSE — invoke RULE-CHAOS-INJECT
bypass before closing Gate 2b.

| # | Scenario ID | Trigger Condition Reference | Inject | Expected Observable | Pass-Fail Signal |
|---|---|---|---|---|---|
| 1 | FS-01 | [threshold from Gate 2 FS-01 Trigger Condition] | | | |

```
GATE 2b CLOSE
Exit postconditions:
  [ ] One chaos row per Include scenario from Gate 1; no scenarios missing
  [ ] Every row has Trigger Condition Reference citing Gate 2 threshold expression
  [ ] Every row has Inject with named fault type, mechanism, parameter (not generic)
  [ ] Every row has Expected Observable at named in-fault granularity
  [ ] Every row has Pass-Fail Signal naming a specific binary artifact
  [ ] RULE-CHAOS-INJECT fired for any missing rows and bypass resolved before this close
Gate 2b STATUS: CLOSED / OPEN — [reason if open]
```

---

### GATE 3: Gap Identification

```
GATE 3 OPEN
Preconditions:
  [ ] Gate 2 STATUS: CLOSED
Entry confirmed: [yes / no]
```

**Observable Signal requirement**: Every named finding in all three gap tables must carry
three Observable Signal components: (1) named signal — specific metric name, log pattern,
trace attribute, or alert condition; (2) detection horizon — estimated time from gap onset
to signal firing; (3) rationale sentence — why this signal surfaces the gap before user
impact. Generic signals ("add monitoring") fail. Unnamed observables ("check the logs")
fail. If no observable signal exists for a finding, invoke RULE-OBS-GAP bypass and emit
MRF-OBS-NN: "no production observability for [gap ID]" — undetectable gaps are missing
recovery flows.

**OEG — Offline Experience Gaps**

| ID | Scenario Ref | Gap Description | Status-Quo Carrying Cost | Observable Signal | Detection Horizon | Rationale | Actionable Recommendation |
|---|---|---|---|---|---|---|---|
| OEG-01 | FS-NN | | [rate \| horizon \| user failure] | [named signal] | [time to alert] | [why this detects the gap early] | |

No OEG: `OEG-NIL-1: [scope rationale]`

**DCV — Data Consistency Violations**

| ID | Source | Data Type | Failure Mode | Conflict Resolution | Adequacy | Status-Quo Carrying Cost | Observable Signal | Detection Horizon | Rule Applied |
|---|---|---|---|---|---|---|---|---|---|
| DCV-01 | FS-NN | | | LWW / merge / manual / reject-stale / undefined | adequate / inadequate / undefined | [rate \| horizon \| metric] | [named signal] | [time to alert] | |

Inadequate/undefined resolution: invoke RULE-CR-DCV; emit DCV-CR-NN.
No DCV: `DCV-NIL-1: [scope rationale]`

**MRF — Missing Recovery Flows**

| ID | Scenario Ref | Absent Mechanism | Status-Quo Carrying Cost | Observable Signal | Detection Horizon | Why No Current Path Exists |
|---|---|---|---|---|---|---|
| MRF-01 | FS-NN | | [rate \| horizon \| failure] | [named signal] | [time to alert] | |

No MRF: `MRF-NIL-1: [scope rationale]`

If any finding has no known observable signal — invoke RULE-OBS-GAP bypass and emit:

| MRF-OBS-NN | [gap ID ref] | no production observability for [gap ID] | [carrying cost of undetected gap] | N/A — this is the gap | [horizon: unbounded — undetectable until user reports] | [gap is known but no monitoring signal exists to surface it automatically] |
|---|---|---|---|---|---|---|

```
GATE 3 CLOSE
Exit postconditions:
  [ ] All three gap categories present; every finding or typed nil with scope rationale
  [ ] Every named finding has Observable Signal (named signal + detection horizon + rationale)
  [ ] Findings with no observable signal have MRF-OBS-NN emitted and RULE-OBS-GAP fired
  [ ] Status-Quo Carrying Cost present for every named finding
  [ ] All RULE-CR-DCV entries assigned DCV-NN
Gate 3 STATUS: CLOSED / OPEN — [reason if open]
```

---

### GATE 4: Amendment Pass

```
GATE 4 OPEN
Preconditions:
  [ ] Gate 3 STATUS: CLOSED
Entry confirmed: [yes / no]
```

| AMD ID | Entry ID | Original (summary) | Amended (summary) | Rule Invoked | Gate Re-Opened? |
|---|---|---|---|---|---|

No amendments: `Gate 4: no amendments required. No gate re-opens triggered.`

```
GATE 4 CLOSE
Exit postconditions:
  [ ] All recovery paths have minimum two actor-labeled steps
  [ ] Every superseded nil has SUPERSEDED annotation with finding ID
Gate 4 STATUS: CLOSED / OPEN — [reason if open]
```

---

### Act 1 Terminal: Post-Analysis Rule Registry Audit

**BYPASS-TRIGGER column**: A RULE-BYPASSED status cell requires a non-empty BYPASS-TRIGGER
entry. An empty BYPASS-TRIGGER cell beside a RULE-BYPASSED status is itself an audit failure.

| Rule ID | Invocations | Citations (gate, entry) | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-CR-DCV | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | [empty or trigger citation] |
| RULE-BARRED-CG | | | | |
| RULE-NIL-SUPERSEDE | | | | |
| RULE-CHAOS-INJECT | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | [empty or `GATE 2b-bypass: REOPEN — apply RULE-CHAOS-INJECT at Gate 2b, FS-NN`] |
| RULE-OBS-GAP | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | [empty or `GATE 3-bypass: REOPEN — apply RULE-OBS-GAP at Gate 3, OEG/DCV/MRF-NN`] |

BYPASS-TRIGGER non-empty for any rule → invoke bypass gate-reopening protocol before
ACT 1 CLOSE.

POST-ANALYSIS REGISTRY AUDIT (ACT 1) COMPLETE: [confirm no RULE-BYPASSED entries remain]

---

### Act 1 Terminal: Nil Supersession Log

| Nil ID | Gap Type | State | Superseded By | Gate |
|---|---|---|---|---|

No supersessions: `No supersessions in this run.`

---

### Act 1 Terminal: Chaos-Observability Coverage Matrix

After the registry audit, produce this matrix to confirm joint operational coverage. One row
per Include scenario from Gate 1.

| Scenario ID | Chaos Test Written? | Chaos Test Gate | Gap ID(s) Produced | Observable Signal Written? | Observable Signal Gate |
|---|---|---|---|---|---|
| FS-01 | Yes / No | Gate 2b row N | OEG-NN / DCV-NN / MRF-NN / none | Yes / No | Gate 3 row N |

Summary row: `[N] of [M] scenarios have both chaos test and observable signal. [N] scenarios
have chaos test only. [N] scenarios have observable signal only. [N] scenarios have neither
— these require RULE-CHAOS-INJECT and/or RULE-OBS-GAP bypass if not already resolved.`

CHAOS-OBSERVABILITY COVERAGE MATRIX COMPLETE

---

### Act 1 Terminal: Scope Verification

| Declared Operation | Covered | Gap Finding |
|---|---|---|
| [operation] | Yes / No | SV-GAP-NN / — |

SCOPE VERIFICATION COMPLETE

---

```
ACT 1 CLOSE (sign-off)
(1) All gates within Act 1 CLOSED:
    Gate 1:     [CLOSED / OPEN — reason]
    Gate 1b:    [CLOSED / N/A — no BARRED entries]
    Gate 2:     [CLOSED / OPEN — reason]
    Gate 2b:    [CLOSED / OPEN — reason]
    Gate 3:     [CLOSED / OPEN — reason]
    Gate 4:     [CLOSED / OPEN — reason]
    GATE N-bypass blocks (if triggered): [CLOSED / none triggered]
    Act 1 Registry Audit: [CLOSED / OPEN — reason]
    Chaos-Observability Matrix: [COMPLETE / OPEN — reason]
(2) Act 1 scope exhausted: [yes / list any unresolved items]
(3) No RULE-BYPASSED conditions remain unresolved within Act 1: [yes / exception detail]
ACT 1 STATUS: CLOSED / OPEN
```

---

```
ACT 2 OPEN — Commerce Domain Validator
Entry condition: ACT 1 STATUS: CLOSED
Scope: Gate 5 + Act 2 Registry Audit + Inertia Synthesis + ACT 2 CLOSE
```

### GATE 5: Commerce Domain Validation

```
GATE 5 OPEN
Preconditions:
  [ ] ACT 1 STATUS: CLOSED
Entry confirmed: [yes / no]
```

| Scenario ID | Commerce Operation Named? | Amended Operation (RULE-COMMERCE-ANCHOR) | CV Finding Issued |
|---|---|---|---|
| FS-01 | Yes / No | | — / CV-DCV-01 / CV-OEG-01 / CV-MRF-01 |

Commerce-domain finding targets (check each):
- Inventory oversell under partition: [present / absent — rationale]
- Payment idempotency window expiry: [present / absent — rationale]
- Loyalty point double-redemption under split-brain: [present / absent — rationale]
- Order state divergence under partial fulfillment failure: [present / absent — rationale]

```
GATE 5 CLOSE
Exit postconditions:
  [ ] Every Include scenario anchored to a named commerce operation
  [ ] All RULE-COMMERCE-ANCHOR invocations recorded
  [ ] All four commerce-domain targets checked (present or rationale)
Gate 5 STATUS: CLOSED / OPEN — [reason if open]
```

---

### Act 2 Terminal: Post-Analysis Rule Registry Audit

| Rule ID | Invocations | Citations | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-COMMERCE-ANCHOR | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | [empty or `GATE 5-bypass: REOPEN now`] |

If BYPASS-TRIGGER non-empty — Commerce Validator resolves before ACT 2 CLOSE.

POST-ANALYSIS REGISTRY AUDIT (ACT 2) COMPLETE

---

### Inertia Synthesis — What Does Doing Nothing Cost?

**Per-finding carrying cost** (from Gate 3 Status-Quo Carrying Cost column):
For each named gap (OEG-NN, DCV-NN, MRF-NN, MRF-OBS-NN): failure mode, rate, horizon,
named metric that accumulates. One entry per finding.

**Overall synthesis**:
Urgency: HIGH / MEDIUM / LOW
Highest-risk finding: [gap ID] — [carrying cost]
Status-quo option: [what "do nothing" looks like for `{topic}` specifically — not generic]
Intervention recommendation: [owner + threshold + consequence of missing threshold]

```
ACT 2 CLOSE (sign-off)
(1) All gates within Act 2 CLOSED:
    Gate 5: [CLOSED / OPEN — reason]
    GATE 5-bypass blocks (if triggered): [CLOSED / none triggered]
    Act 2 Registry Audit: [CLOSED / OPEN — reason]
(2) Act 2 scope exhausted: [yes — all scenarios commerce-anchored; all CV targets checked;
    inertia synthesis complete including MRF-OBS-NN findings]
(3) No RULE-BYPASSED conditions remain unresolved within Act 2: [yes / exception detail]
ACT 2 STATUS: CLOSED / OPEN
```

ANALYSIS COMPLETE (declared only when ACT 1 STATUS: CLOSED AND ACT 2 STATUS: CLOSED)
