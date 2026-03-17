# Flow-Resilience Skill — Round 13 Variations (Rubric v13)

**Skill**: flow-resilience — Simulate degraded conditions: offline, partial failure, eventual
consistency.
**Rubric**: v13 (C-01 through C-41, essential/recommended/aspirational tiers)
**Date**: 2026-03-15

---

## Round 13 Context

**New criteria entering R13**: C-39, C-40, C-41 (extracted from R12 excellence signals).

**R12 ceiling under v13**: V-05 at 65/66 uncapped. C-40 PARTIAL (prohibition clause embedded
inline with positive confirmation, not standalone). C-38 PASS only V-05; PARTIAL for V-01–V-04.
C-41 FAIL for V-02/V-03/V-04 (Gate 1 CLOSE names presence check but not prohibited basis).

**R13 targets**:
- Crack C-40 PASS — Gate 2b CLOSE prohibition clause as standalone independent postcondition
  (not merged with positive confirmation in one parenthetical)
- Crack C-41 PASS for V-02/V-03/V-04 — Gate 1 CLOSE names both required basis
  ("architecture basis") AND prohibited basis ("not description absence") as independent items
- Spread C-38 PASS — bidirectional matrix adds formal GAP REGISTRY blocks with structured
  finding entries (ID + source + consequence), not inline ad hoc emit instructions

**Variation axes selected**:
- V-01: Single axis — Lifecycle emphasis: Gate 2b CLOSE prohibition clause extracted from
  merged parenthetical into standalone named postcondition checkbox (targets C-40)
- V-02: Single axis — Output format: Gate 1 CLOSE extended with dual-named quality
  postcondition naming required basis (architecture: confirmed) and prohibited basis
  (description absence: absent) as independent items (targets C-41)
- V-03: Single axis — Output format: Bidirectional Coverage Matrix adds formal GAP REGISTRY
  blocks after each direction table, requiring structured ID+consequence entries for each
  gap finding (targets C-38)
- V-04: Combination — standalone prohibition clause (V-01) + Gate 1 quality postcondition
  (V-02) without bidirectional gap registry (C-40 + C-41)
- V-05: Full integration — standalone prohibition clause (V-01) + Gate 1 quality postcondition
  (V-02) + formal gap registry (V-03), targeting C-40 + C-41 + C-38 simultaneously

---

## V-01

**Variation axis**: Lifecycle emphasis — Gate 2b CLOSE's merged identity assertion line is
split into two independent, separately-checkboxed postcondition items. Currently the CLOSE
reads: `[ ] Every Trigger Condition Reference contains verbatim Gate 2 threshold expression
(identity assertion satisfied — no paraphrase, no independent calibration)` — one checkbox
verifying two independent claims. V-01 makes them two checkboxes: (1) identity assertion
confirmed: every TCR contains the verbatim Gate 2 threshold expression; (2) prohibition
clause confirmed: no TCR contains a paraphrase or independently calibrated expression
(no paraphrase, no independent calibration). The rest of the prompt is identical to R12 V-05.

**Hypothesis**: C-40 scores PARTIAL in R12 V-05 because embedding the prohibition clause
inside a parenthetical appended to the positive confirmation line makes them visually and
structurally coupled — a model confirming "identity assertion satisfied" implicitly treats
the parenthetical as satisfied too. The rubric's C-40 PASS requirement is that the prohibition
clause is independently load-bearing: "the positive confirmation and the prohibition clause are
independently load-bearing." Two separate checkbox items are independently verifiable — one can
be checked without the other, making the independence explicit at the structural level. A model
that passes the positive confirmation but omits the prohibited form will fail the second
checkbox rather than having it silently pass under the first.

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
2. Bypass Owner applies the rule: produces CE-NN, OS-NN, DCV-NN, CG-NN, SUPERSEDED
   annotation, or commerce anchor amendment as required.
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
| `Trigger Condition` | DS Expert | C-phase | **Two required components**: (1) threshold expression — quantified activation condition (e.g., "inventory count falls below safety-stock threshold", "payment API p99 latency > 500ms"); (2) detection signal — named observable mechanism confirming threshold crossing (e.g., "inventory-service health probe returns degraded", "payment-provider timeout counter exceeds N/window"). The threshold expression is also used verbatim as the activation condition in Gate 2b (chaos test). Qualitative descriptions without threshold expression fail. |
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
| Network partition / offline | 2 | [required if slot unfillable — cite DS Primitive by name here] |
| Partial service failure | 2 | |
| Eventual consistency | 2 | |

---

```
ACT 1 OPEN — Distributed Systems Expert
Scope: Gates 1–4 + Gate 2b + Act 1 Registry Audit + Nil Supersession Log +
       Bidirectional Chaos-Observability Coverage Matrix + Scope Verification + ACT 1 CLOSE
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

**Argued-Impossible template** — complete this block for every Argued-Impossible row:

```
FS-NN Argued-Impossible:
DS Primitive cited: [name the specific CAP theorem guarantee / synchrony guarantee /
  deployment topology constraint that architecturally forecloses this failure class.
  Must address the architecture of {topic}, not the description of the prompt.]

VALID argument example:
  "DS Primitive cited: Single-datacenter synchronous replication with no async follower —
   forecloses multi-master split-brain because all writes commit synchronously to one
   primary; no partition scenario produces divergent acknowledged writes under this
   topology."

INVALID argument example:
  "DS Primitive cited: The topic does not describe a distributed cache, so cache
   invalidation race conditions are not applicable."
  [Fails: this is a description-absence argument, not an architecture constraint. The
   absence of a feature from the prompt description does not prove the system lacks it
   architecturally. A valid argument must cite what the architecture guarantees, not what
   the description omits.]
```

Apply this template for every Argued-Impossible row. A DS Primitive field containing a
topic-scope argument ("the topic doesn't mention X", "the system description is too simple
for this") is a Gate 1 violation. Identify the architecture constraint; do not read the
absence of a description as an architecture guarantee.

**Gate 1b — BARRED Resolution**

| BARRED ID | Confidence Basis | Resolved? | Resolution Mechanism | New Disposition |
|---|---|---|---|---|

No BARRED entries: `Gate 1b: none.`

```
GATE 1 CLOSE
Exit postconditions:
  [ ] Every candidate has one named disposition
  [ ] Every BARRED has CG-NN emitted
  [ ] Every Argued-Impossible has DS Primitive cited: field completed (architecture basis,
      not description absence)
  [ ] DS Primitive column in Coverage Accountability Roster populated for any
      impossibility slot
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
This threshold expression will be transcribed verbatim into Gate 2b as the chaos activation
boundary for this scenario — identical to the production monitoring boundary.
C-phase (Commerce Expert): fill State (exact system configuration, named components) and
Capability (named operations still completable).
**C-phase complete check: do not begin D-phase columns until Trigger Condition, State,
Capability are non-placeholder.**
D-phase (DS Expert): fill Data at Risk, Recovery Path (all four stages: mechanism | actor |
SLA target | VS — VS is named observable confirming stage completion, distinct from
mechanism), Severity, Blast Radius, Rule Applied.
**Do not advance to Row 2 until all columns including both Trigger Condition components and
all four VS entries are non-placeholder.**

---

**Row 2 — FS-02: [Scenario Name]**

Consequence context: [payment idempotency miss → double-charge; loyalty double-redemption
under split-brain; order state divergence]. Chronic: reconciliation backlog / without
ceiling / dispute-count accumulates.

**Write this row now.**
Fill Trigger Condition (threshold + detection signal — threshold verbatim in Gate 2b). Fill
all columns per Column Contract including all four Recovery Path stages with mechanism, SLA,
named VS.
**C-phase complete check before D-phase. Do not advance to Row 3 until non-placeholder.**

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

#### Gate 2b Column Contract

| Column Name | Owner | Fill Requirement |
|---|---|---|
| `#` | Shared | Sequential integer; no gaps |
| `Scenario ID` | Shared | FS-NN from Gate 1 Include list; one row per Include scenario |
| `Trigger Condition Reference` | DS Expert | **Identity assertion**: the chaos activation boundary expression IS the Trigger Condition threshold expression from Gate 2 for this scenario — identical, not a derivative or approximation. Transcribe the exact threshold expression string verbatim from the Gate 2 Trigger Condition column. Do not paraphrase, abbreviate, or add conditions not present in Gate 2. Any modification between Gate 2 and Gate 2b produces an uncalibrated chaos test whose results are not directly predictive of production trigger behavior. |
| `Inject` | DS Expert | `[fault type]: [named mechanism] — [parameter]`. Generic descriptions ("make service unavailable") are not valid. |
| `Expected Observable` | DS Expert | In-fault system behavior at named observation granularity; not post-recovery state |
| `Pass-Fail Signal` | DS Expert | Binary artifact naming a specific metric value, API response code, log entry, or system state; generic outcomes fail |

```
GATE 2b OPEN
Preconditions:
  [ ] Gate 2 STATUS: CLOSED
  [ ] Include scenario list from Gate 1 available (IDs: FS-01, FS-02, ...)
  [ ] Identity assertion acknowledged: chaos activation boundary = Gate 2 threshold
      expression for each scenario, verbatim — not a derivative
Entry confirmed: [yes / no]
```

For each Include scenario from Gate 1, write one row using the Gate 2b Column Contract.
The Trigger Condition Reference must contain the verbatim threshold expression from Gate 2
for that scenario ID.

If any Include scenario lacks a chaos row at Gate 2b CLOSE — invoke RULE-CHAOS-INJECT
bypass before closing Gate 2b.

| # | Scenario ID | Trigger Condition Reference | Inject | Expected Observable | Pass-Fail Signal |
|---|---|---|---|---|---|
| 1 | FS-01 | [verbatim threshold expression from Gate 2 FS-01 — identical to Gate 2 value] | | | |

```
GATE 2b CLOSE
Exit postconditions:
  [ ] One chaos row per Include scenario; no scenarios missing
  [ ] Identity assertion confirmed: every Trigger Condition Reference contains the
      verbatim Gate 2 threshold expression — identical string, not a paraphrase
  [ ] Prohibition clause confirmed: no Trigger Condition Reference contains a paraphrased
      or independently calibrated expression — no paraphrase, no independent calibration
  [ ] Every row has Inject with named fault type, mechanism, and parameter (not generic)
  [ ] Every row has Expected Observable at named in-fault observation granularity
  [ ] Every row has Pass-Fail Signal naming a specific binary artifact
  [ ] RULE-CHAOS-INJECT fired for any missing rows; bypass resolved before this close
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
trace attribute, or alert condition; (2) detection horizon — concrete time window from gap
onset to signal firing (generic language "promptly" fails); (3) rationale sentence — why
this signal surfaces the gap before user impact. Generic signals ("add monitoring") fail.
If no observable signal exists for a finding, invoke RULE-OBS-GAP bypass and emit
MRF-OBS-NN.

**OEG — Offline Experience Gaps**

| ID | Scenario Ref | Gap Description | Status-Quo Carrying Cost | Observable Signal | Detection Horizon | Rationale | Actionable Recommendation |
|---|---|---|---|---|---|---|---|
| OEG-01 | FS-NN | | [rate \| horizon \| user failure] | [named signal] | [time to alert] | [why this detects early] | |

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

`MRF-OBS-NN | [gap ID ref] | no production observability for [gap ID] | [carrying cost of undetected gap] | N/A | [horizon: unbounded — undetectable until user reports] | [gap is known but no monitoring signal exists]`

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

### Act 1 Terminal: Bidirectional Chaos-Observability Coverage Matrix

This matrix is a required Act 1 Terminal artifact. It verifies that every chaos scenario is
linked to at least one Observable Signal (forward direction) and every Observable Signal is
linked to at least one chaos scenario (reverse direction). Absence is an Act 1 CLOSE blocker.

**Part A — Forward Direction: Chaos Scenario → Observable Signal**

For each chaos row in Gate 2b, identify the Observable Signal ID(s) from Gate 3 that will
confirm detection of that chaos scenario's fault in production.

| Gate 2b Row | Scenario ID | Observable Signal ID(s) Linked | Coverage Gap? |
|---|---|---|---|
| Row 1 | FS-01 | [OEG-NN / DCV-NN / MRF-NN — the Gate 3 finding whose Observable Signal monitors this fault] | No / CHAOS-OBS-GAP-NN |

**Dark chaos finding**: A chaos row with no Observable Signal linkage = "dark chaos" —
the fault fires but cannot be confirmed as detected in production. Emit:
`CHAOS-OBS-GAP-NN | Chaos row [N] / [Scenario ID] | no Observable Signal linked | consequence: pass/fail result unverifiable in production without monitoring confirmation`

**Part B — Reverse Direction: Observable Signal → Chaos Scenario**

For each Observable Signal entry in Gate 3 (across OEG, DCV, MRF tables), identify the
Gate 2b chaos row(s) that exercise the fault conditions monitored by that signal.

| Gate 3 Finding ID | Signal Name | Chaos Scenario ID(s) Linked | Coverage Gap? |
|---|---|---|---|
| OEG-01 | [named signal from Gate 3] | [FS-NN — the Gate 2b scenario that injects the fault this signal monitors] | No / OBS-CHAOS-GAP-NN |

**Unvalidated signal finding**: An Observable Signal with no chaos scenario linkage = the
signal exists but its production behavior under fault conditions is untested. Emit:
`OBS-CHAOS-GAP-NN | [Gate 3 finding ID] | [signal name] | no chaos scenario linked | consequence: signal behavior under fault untested; cannot confirm it fires as specified`

```
Matrix summary:
Forward coverage: [N] of [M] chaos rows have linked Observable Signals.
Reverse coverage: [N] of [M] Observable Signals have linked chaos scenarios.
Dark chaos gaps: [CHAOS-OBS-GAP-NN list / none]
Unvalidated signal gaps: [OBS-CHAOS-GAP-NN list / none]
```

BIDIRECTIONAL CHAOS-OBSERVABILITY COVERAGE MATRIX COMPLETE

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
    Bidirectional Chaos-Observability Matrix: [COMPLETE / OPEN — reason]
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
| RULE-COMMERCE-ANCHOR | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | [empty or bypass trigger] |

POST-ANALYSIS REGISTRY AUDIT (ACT 2) COMPLETE

---

### Inertia Synthesis — What Does Doing Nothing Cost?

**Per-finding carrying cost** (from Gate 3 Status-Quo Carrying Cost column):
For each named gap (OEG-NN, DCV-NN, MRF-NN): state the failure mode, rate, horizon, metric.

**Overall synthesis**:
Urgency: HIGH / MEDIUM / LOW
Highest-risk finding: [gap ID] — [carrying cost from Gate 3]
Status-quo option: [what "do nothing" looks like for `{topic}` specifically]
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

**Variation axis**: Output format — Gate 1 CLOSE is extended with a dual-named quality
postcondition. The existing postcondition `[ ] Every Argued-Impossible cites DS Primitive
by name` (presence check only) is replaced with two independent named checks: (1) required
basis check — `[ ] Impossibility argument basis confirmed: every Argued-Impossible cites an
architecture basis (required)` and (2) prohibited basis check — `[ ] Impossibility argument
prohibition confirmed: no Argued-Impossible cites description absence as the basis
(prohibited)`. These are structurally separate checkbox items — one verifying presence of
the required form, one verifying absence of the prohibited form. The Gate 2b Column Contract
identity assertion and OPEN precondition acknowledgment are carried from R12 V-02 (C-39/C-40
PASS baseline). The bidirectional matrix is the standard form from R12 V-05. No DS Primitive
VALID/INVALID template change from V-01.

**Hypothesis**: C-41 FAIL in R12 V-02/V-04 because their Gate 1 CLOSE postcondition reads
`[ ] Every Argued-Impossible has DS Primitive cited: field with architecture basis — not
description absence` — one combined statement. The C-41 signal requires "both required basis
('architecture basis') AND prohibited basis ('not description absence') in one statement" but
as independent verifiable items, not merged prose. Separating them into two independent
checkboxes makes each independently enforceable at gate-close time: a Gate 1 CLOSE that
confirms presence but omits the prohibition check is a visible failure rather than a silent
pass. The dual-checkbox structure converts C-41 from a prose quality statement into two
binary gate-close requirements.

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

**Bypass Owner column**: Cross-act invocation is not permitted.

---

### BYPASS GATE-REOPENING PROTOCOL

**Authority**: DS Expert owns this protocol for Act 1 rules; Commerce Validator for Act 2
rules. Cross-act invocation not permitted.

When any rule shows RULE-BYPASSED in the Post-Analysis Rule Registry Audit:

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
| `Trigger Condition` | DS Expert | C-phase | **Two required components**: (1) threshold expression — quantified activation condition (e.g., "inventory count falls below safety-stock threshold", "payment API p99 latency > 500ms"); (2) detection signal — named observable mechanism confirming threshold crossing. The threshold expression is also used verbatim in Gate 2b. Qualitative descriptions without threshold expression fail. |
| `State` | Commerce Expert | C-phase | Specific system configuration; named components and states; not "degraded" |
| `Capability` | Commerce Expert | C-phase | Named commerce operations the user can still complete |
| `Data at Risk` | DS Expert | D-phase | Named data type + consistency failure mode |
| `Recovery Path` | DS Expert | D-phase | Four stages each with: mechanism (named actor) \| SLA target \| VS (named observable confirming stage completion, distinct from mechanism). Format: Detect / Contain / Recover / Validate each with mech \| actor \| SLA \| VS. |
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
Scope: Gates 1–4 + Gate 2b + Act 1 Registry Audit + Nil Supersession Log +
       Bidirectional Chaos-Observability Coverage Matrix + Scope Verification + ACT 1 CLOSE
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
Argued-Impossible: name DS Primitive (CAP theorem guarantee, synchrony guarantee, topology
constraint). "The topic does not mention X" is not a DS Primitive — description absence does
not establish an architecture guarantee.

**Gate 1b — BARRED Resolution**

No BARRED entries: `Gate 1b: none.`

```
GATE 1 CLOSE
Exit postconditions:
  [ ] Every candidate has one named disposition
  [ ] Every BARRED has CG-NN emitted
  [ ] Impossibility argument basis confirmed: every Argued-Impossible cites an
      architecture basis (CAP theorem guarantee, synchrony guarantee, or topology
      constraint that forecloses the failure class) — required basis: present
  [ ] Impossibility argument prohibition confirmed: no Argued-Impossible argument
      is based on description absence ("the topic does not mention X", "the description
      is too simple for this") — prohibited basis: absent
  [ ] DS Primitive column in Coverage Accountability Roster populated for any
      impossibility slot
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

**Column-group gate**: C-phase (Trigger Condition, State, Capability) complete before
D-phase within each row.

#### Row Descriptors

**Row 1 — FS-01: [Scenario Name]**

Consequence context: [acute consequences per resolution branch]. Chronic: [rate] / [horizon]
/ [metric].

**Write this row now.**
Fill Trigger Condition: threshold expression + detection signal (threshold used verbatim in
Gate 2b).
C-phase (Commerce Expert): fill State and Capability.
**C-phase complete check before D-phase.**
D-phase (DS Expert): fill Data at Risk, Recovery Path (four stages, mechanism | actor | SLA
| VS), Severity, Blast Radius, Rule Applied.
**Do not advance to Row 2 until all columns non-placeholder including all four VS entries.**

---

**Row 2 — FS-02: [Scenario Name]**

Consequence context: [payment idempotency / loyalty double-redemption / order divergence].
Chronic: reconciliation backlog / without ceiling / dispute-count accumulates.

**Write this row now.** Fill all columns per Column Contract.
**C-phase complete check before D-phase. Do not advance to Row 3 until non-placeholder.**

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
  [ ] All RULE-CR-DCV triggers recorded; column-group gate confirmed every row
Gate 2 STATUS: CLOSED / OPEN — [reason if open]
```

---

### GATE 2b: Chaos Engineering Specification

#### Gate 2b Column Contract

| Column Name | Owner | Fill Requirement |
|---|---|---|
| `#` | Shared | Sequential integer; no gaps |
| `Scenario ID` | Shared | FS-NN from Gate 1 Include list; one row per Include scenario |
| `Trigger Condition Reference` | DS Expert | **Identity assertion**: the chaos activation boundary expression IS the Trigger Condition threshold expression from Gate 2 for this scenario — identical, not a derivative or approximation. Transcribe the exact threshold expression string verbatim from the Gate 2 Trigger Condition column for this scenario ID. Do not paraphrase, abbreviate, or add conditions not present in Gate 2. Any modification to the expression between Gate 2 and Gate 2b produces an uncalibrated chaos test whose results are not directly predictive of production trigger behavior. The same logical expression that activates production monitoring activates this chaos test — they share the same boundary by assertion. |
| `Inject` | DS Expert | `[fault type]: [named mechanism] — [parameter]`. Generic descriptions ("make service unavailable") are not valid. |
| `Expected Observable` | DS Expert | In-fault system behavior at named observation granularity; not post-recovery state |
| `Pass-Fail Signal` | DS Expert | Binary artifact naming a specific metric value, API response code, log entry, or system state; generic outcomes fail |

```
GATE 2b OPEN
Preconditions:
  [ ] Gate 2 STATUS: CLOSED
  [ ] Include scenario list from Gate 1 available (IDs: FS-01, FS-02, ...)
  [ ] Identity assertion acknowledged: chaos activation boundary = Gate 2 threshold
      expression for each scenario, verbatim — not a derivative
Entry confirmed: [yes / no]
```

For each Include scenario from Gate 1, write one row using the Gate 2b Column Contract.
The Trigger Condition Reference must contain the verbatim threshold expression from Gate 2.

If any Include scenario lacks a chaos row at Gate 2b CLOSE — invoke RULE-CHAOS-INJECT
bypass before closing Gate 2b.

| # | Scenario ID | Trigger Condition Reference | Inject | Expected Observable | Pass-Fail Signal |
|---|---|---|---|---|---|
| 1 | FS-01 | [verbatim threshold expression from Gate 2 FS-01 — identical to Gate 2 value] | | | |

```
GATE 2b CLOSE
Exit postconditions:
  [ ] One chaos row per Include scenario; no scenarios missing
  [ ] Every Trigger Condition Reference contains verbatim Gate 2 threshold expression
      (identity assertion satisfied — no paraphrase, no independent calibration)
  [ ] Every row has Inject (named fault type, mechanism, parameter — not generic)
  [ ] Every row has Expected Observable at named in-fault observation granularity
  [ ] Every row has Pass-Fail Signal naming a specific binary artifact
  [ ] RULE-CHAOS-INJECT fired for any missing rows; bypass resolved before this close
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

**Observable Signal requirement**: Every named finding must carry three components:
(1) named signal (specific metric, log pattern, trace attribute, or alert condition);
(2) detection horizon (concrete time window — generic "promptly" fails);
(3) rationale sentence (why this signal surfaces the gap before user impact).
Generic signals fail. No observable signal → RULE-OBS-GAP + MRF-OBS-NN.

**OEG — Offline Experience Gaps**

| ID | Scenario Ref | Gap Description | Status-Quo Carrying Cost | Observable Signal | Detection Horizon | Rationale | Actionable Recommendation |
|---|---|---|---|---|---|---|---|
| OEG-01 | FS-NN | | [rate \| horizon \| user failure] | [named signal] | [time to alert] | [why this detects early] | |

No OEG: `OEG-NIL-1: [scope rationale]`

**DCV — Data Consistency Violations**

| ID | Source | Data Type | Failure Mode | Conflict Resolution | Adequacy | Status-Quo Carrying Cost | Observable Signal | Detection Horizon | Rule Applied |
|---|---|---|---|---|---|---|---|---|---|
| DCV-01 | FS-NN | | | LWW / merge / manual / reject-stale / undefined | adequate / inadequate / undefined | [rate \| horizon \| metric] | [named signal] | [time to alert] | |

No DCV: `DCV-NIL-1: [scope rationale]`

**MRF — Missing Recovery Flows**

| ID | Scenario Ref | Absent Mechanism | Status-Quo Carrying Cost | Observable Signal | Detection Horizon | Why No Current Path Exists |
|---|---|---|---|---|---|---|
| MRF-01 | FS-NN | | [rate \| horizon \| failure] | [named signal] | [time to alert] | |

No MRF: `MRF-NIL-1: [scope rationale]`

```
GATE 3 CLOSE
Exit postconditions:
  [ ] All three gap categories present; every finding or typed nil with scope rationale
  [ ] Every named finding has Observable Signal (named signal + detection horizon + rationale)
  [ ] Findings with no observable signal have MRF-OBS-NN and RULE-OBS-GAP fired
  [ ] Status-Quo Carrying Cost present for every named finding
  [ ] All RULE-CR-DCV entries assigned DCV-NN
Gate 3 STATUS: CLOSED / OPEN — [reason if open]
```

---

### GATE 4: Amendment Pass

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
| RULE-CR-DCV | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | |
| RULE-BARRED-CG | | | | |
| RULE-NIL-SUPERSEDE | | | | |
| RULE-CHAOS-INJECT | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | |
| RULE-OBS-GAP | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | |

POST-ANALYSIS REGISTRY AUDIT (ACT 1) COMPLETE: [confirm no RULE-BYPASSED entries remain]

---

### Act 1 Terminal: Nil Supersession Log

No supersessions: `No supersessions in this run.`

---

### Act 1 Terminal: Bidirectional Chaos-Observability Coverage Matrix

This matrix verifies coverage in both directions. It is a required Act 1 Terminal artifact.

**Part A — Forward Direction: Chaos Scenario → Observable Signal**

| Gate 2b Row | Scenario ID | Observable Signal ID(s) Linked | Coverage Gap? |
|---|---|---|---|
| Row 1 | FS-01 | [OEG-NN / DCV-NN / MRF-NN] | No / CHAOS-OBS-GAP-NN |

Dark chaos: `CHAOS-OBS-GAP-NN | Chaos row [N] / [Scenario ID] | no Observable Signal linked | consequence: pass/fail unverifiable in production`

**Part B — Reverse Direction: Observable Signal → Chaos Scenario**

| Gate 3 Finding ID | Signal Name | Chaos Scenario ID(s) Linked | Coverage Gap? |
|---|---|---|---|
| OEG-01 | [named signal] | [FS-NN] | No / OBS-CHAOS-GAP-NN |

Unvalidated signal: `OBS-CHAOS-GAP-NN | [Gate 3 finding ID] | [signal name] | no chaos scenario linked | consequence: signal behavior under fault untested`

```
Matrix summary:
Forward coverage: [N] of [M] chaos rows have linked Observable Signals.
Reverse coverage: [N] of [M] Observable Signals have linked chaos scenarios.
Dark chaos gaps: [list / none]
Unvalidated signal gaps: [list / none]
```

BIDIRECTIONAL CHAOS-OBSERVABILITY COVERAGE MATRIX COMPLETE

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
    Gate 1 / 1b / 2 / 2b / 3 / 4: [CLOSED / OPEN — reason]
    GATE N-bypass blocks: [CLOSED / none]
    Act 1 Registry Audit: [CLOSED / OPEN]
    Bidirectional Chaos-Observability Matrix: [COMPLETE / OPEN — reason]
(2) Act 1 scope exhausted: [yes / list unresolved]
(3) No RULE-BYPASSED conditions remain: [yes / exception]
ACT 1 STATUS: CLOSED / OPEN
```

---

```
ACT 2 OPEN — Commerce Domain Validator
Entry condition: ACT 1 STATUS: CLOSED
Scope: Gate 5 + Act 2 Registry Audit + Inertia Synthesis + ACT 2 CLOSE
```

### GATE 5: Commerce Domain Validation

| Scenario ID | Commerce Operation Named? | Amended Operation (RULE-COMMERCE-ANCHOR) | CV Finding Issued |
|---|---|---|---|
| FS-01 | Yes / No | | |

Commerce targets: inventory oversell / payment idempotency / loyalty double-redemption /
order state divergence — each [present / absent — rationale].

```
GATE 5 CLOSE
Exit postconditions: Every scenario anchored; all four targets checked.
Gate 5 STATUS: CLOSED / OPEN
```

### Act 2 Terminal: Post-Analysis Rule Registry Audit

| Rule ID | Invocations | Citations | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-COMMERCE-ANCHOR | | | | |

POST-ANALYSIS REGISTRY AUDIT (ACT 2) COMPLETE

### Inertia Synthesis

Per-finding: failure mode, rate, horizon, metric.
Urgency: HIGH / MEDIUM / LOW. Highest-risk: [gap ID]. Status-quo: [{topic} specific].
Intervention: [owner + threshold + consequence].

```
ACT 2 CLOSE
(1) Gate 5 / bypass / Registry Audit: CLOSED
(2) Scope exhausted; inertia synthesis complete
(3) No RULE-BYPASSED remain
ACT 2 STATUS: CLOSED / OPEN
```

ANALYSIS COMPLETE (declared only when ACT 1 STATUS: CLOSED AND ACT 2 STATUS: CLOSED)

---

---

## V-03

**Variation axis**: Output format — The Bidirectional Chaos-Observability Coverage Matrix
is extended with formal GAP REGISTRY blocks after each direction table. Currently gap
findings are emitted as inline ad hoc lines. V-03 adds a named GAP REGISTRY section after
Part A and Part B, requiring each gap entry as a structured three-field block: (1) Gap ID
(CHAOS-OBS-GAP-NN or OBS-CHAOS-GAP-NN); (2) linkage statement naming the specific chaos
row or signal ID and the specific missing link; (3) consequence sentence explaining what
cannot be verified. The matrix closure block becomes a formal non-placeholder requirement
with four named fields before COMPLETE can be declared. The rest is identical to R12 V-04
(has C-39/C-40 PASS and standard bidirectional matrix; no DS Primitive VALID/INVALID
template change).

**Hypothesis**: C-38 PARTIAL in R12 V-03/V-04 because gap findings are described as inline
emit instructions rather than entries in a named, structured registry. Formalizing them as
GAP REGISTRY blocks with required fields (ID, source, missing-link statement, consequence)
makes each gap finding an independently identifiable artifact rather than a prose annotation.
The closure block as a non-placeholder requirement enforces that both direction tables and
both gap registries are complete before the matrix can be marked COMPLETE.

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

**Bypass Owner column**: Cross-act invocation is not permitted.

---

### BYPASS GATE-REOPENING PROTOCOL

**Authority**: DS Expert owns this protocol for Act 1 rules; Commerce Validator for Act 2
rules. Cross-act invocation not permitted.

When any rule shows RULE-BYPASSED in the Post-Analysis Rule Registry Audit:

1. Bypass Owner emits: `GATE N-bypass: REOPENED — [rule ID] — bypass at [gate, entry ID]`
2. Bypass Owner applies the rule and produces required output.
3. Bypass Owner emits: `GATE N-bypass: AMENDED — CLOSED — [rule now applied]`
4. Bypass Owner updates the audit row: Status → INVOKED; BYPASS-TRIGGER → "RESOLVED — [sub-gate]"; Citations += sub-gate.

**COMPLETE may not be declared** while any RULE-BYPASSED entry remains unresolved in any act.

---

### ANTI-OMISSION ARCHITECTURE

| Level | Anti-Omission Mechanism | Omission Risk Targeted | Mechanism Location |
|---|---|---|---|
| Table | Unified row index (`#`) + anti-split instruction | Row fragmentation | `#` column; Gate 2 |
| Section | Phase gate — all rows before Gap Identification | Premature advance | Gate 2 |
| Slot | **"Write this row now."** / **"Do not advance until..."** | Row omission | Row Descriptors |
| Column-Group | C-phase before D-phase within each row | Mid-row omission | Row Descriptors |
| Column | Column ownership in Column Contract | Column omission | Column Contract |

**Anti-split**: Single scenario table. No sub-tables or breaks between rows.

---

### COLUMN CONTRACT

| Column Name | Owner | Phase | Fill Requirement |
|---|---|---|---|
| `#` | Shared | — | Sequential integer; no gaps |
| `ID` | Shared | — | FS-NN; unique per scenario |
| `Trigger Condition` | DS Expert | C-phase | Threshold expression + detection signal. Threshold used verbatim in Gate 2b. |
| `State` | Commerce Expert | C-phase | Specific system configuration; named components |
| `Capability` | Commerce Expert | C-phase | Named commerce operations still completable |
| `Data at Risk` | DS Expert | D-phase | Named data type + consistency failure mode |
| `Recovery Path` | DS Expert | D-phase | Four stages: Detect / Contain / Recover / Validate each with mechanism \| actor \| SLA \| VS (named observable, distinct from mechanism) |
| `Severity` | DS Expert | D-phase | `degraded` / `impaired` / `down` |
| `Blast Radius` | DS Expert | D-phase | Fraction or named segment |
| `Rule Applied` | DS Expert | D-phase | Rule ID or `—` |

---

### Pre-Analysis: Commerce Operation Scope Declaration

```
SCOPE DECLARATION
Operations in scope: [minimum four]
Operations excluded (with reason): [or "none"]
SCOPE DECLARATION COMPLETE
```

### Pre-Analysis: Coverage Accountability Roster

| Degradation Class | Committed Minimum | DS Primitive for Impossibility |
|---|---|---|
| Network partition / offline | 2 | |
| Partial service failure | 2 | |
| Eventual consistency | 2 | |

---

```
ACT 1 OPEN — Distributed Systems Expert
Scope: Gates 1–4 + Gate 2b + Act 1 Registry Audit + Nil Supersession Log +
       Bidirectional Chaos-Observability Coverage Matrix + Scope Verification + ACT 1 CLOSE
```

### GATE 1: Discovery and Triage

```
GATE 1 OPEN
Preconditions:
  [ ] SCOPE DECLARATION COMPLETE; Coverage Roster committed
Entry confirmed: [yes / no]
```

| # | ID | Failure Class | Confidence Basis | Disposition | Rule Applied | Notes |
|---|---|---|---|---|---|---|
| 1 | FS-01 | | | Include / BARRED / Argued-Impossible | RULE-BARRED-CG or — | |

BARRED: cite RULE-BARRED-CG; emit CG-NN.
Argued-Impossible: name DS Primitive (CAP theorem, synchrony guarantee, topology bound).
"Topic does not mention X" is not a DS Primitive.

**Gate 1b — BARRED Resolution**

No BARRED entries: `Gate 1b: none.`

```
GATE 1 CLOSE
Exit postconditions:
  [ ] Every candidate has one named disposition
  [ ] Every BARRED has CG-NN; every Argued-Impossible cites DS Primitive by name
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

**Anti-split**: Single table. **Section gate**: All rows before Gap Identification.
**Column-group gate**: C-phase before D-phase within each row.

#### Row Descriptors

**Row 1 — FS-01:** **Write this row now.** Fill Trigger Condition (threshold + detection signal). C-phase then D-phase. **Do not advance to Row 2 until non-placeholder in all columns including all four VS entries.**

**Row 2 — FS-02:** **Write this row now.** Fill all columns per Column Contract. **C-phase check before D-phase. Do not advance to Row 3 until non-placeholder.**

Continue for all remaining Include scenarios.

| # | ID | Trigger Condition | State | Capability | Data at Risk | Recovery Path | Severity | Blast Radius | Rule Applied |
|---|---|---|---|---|---|---|---|---|---|
| 1 | FS-01 | [threshold] / [detection signal] | | | | Detect / Contain / Recover / Validate each with mech\|actor\|SLA\|VS | | | |

```
GATE 2 CLOSE
Exit postconditions:
  [ ] All columns non-trivial; threshold + detection signal per row; four VS per recovery path
Gate 2 STATUS: CLOSED / OPEN
```

---

### GATE 2b: Chaos Engineering Specification

#### Gate 2b Column Contract

| Column Name | Owner | Fill Requirement |
|---|---|---|
| `#` | Shared | Sequential integer; no gaps |
| `Scenario ID` | Shared | FS-NN; one row per Include scenario |
| `Trigger Condition Reference` | DS Expert | **Identity assertion**: the chaos activation boundary IS the Gate 2 Trigger Condition threshold expression — identical, not a derivative. Transcribe verbatim. Do not paraphrase or independently calibrate. |
| `Inject` | DS Expert | `[fault type]: [named mechanism] — [parameter]`. Not generic. |
| `Expected Observable` | DS Expert | In-fault behavior at named observation granularity |
| `Pass-Fail Signal` | DS Expert | Binary artifact naming specific metric/code/log/state |

```
GATE 2b OPEN
Preconditions:
  [ ] Gate 2 STATUS: CLOSED; Include scenario IDs available
  [ ] Identity assertion acknowledged: Trigger Condition Reference = verbatim Gate 2
      threshold expression — identical, not a derivative
Entry confirmed: [yes / no]
```

| # | Scenario ID | Trigger Condition Reference | Inject | Expected Observable | Pass-Fail Signal |
|---|---|---|---|---|---|
| 1 | FS-01 | [verbatim threshold expression from Gate 2 FS-01] | | | |

```
GATE 2b CLOSE
Exit postconditions:
  [ ] One row per Include scenario; all fields non-generic
  [ ] Every Trigger Condition Reference contains verbatim Gate 2 threshold expression
      (identity assertion satisfied — no paraphrase, no independent calibration)
  [ ] RULE-CHAOS-INJECT fired for any missing rows; bypass resolved
Gate 2b STATUS: CLOSED / OPEN
```

---

### GATE 3: Gap Identification

```
GATE 3 OPEN
Preconditions:
  [ ] Gate 2 STATUS: CLOSED
Entry confirmed: [yes / no]
```

Observable Signal requirement: named signal + concrete detection horizon + rationale.
Generic signals fail. No observable signal → RULE-OBS-GAP + MRF-OBS-NN.

**OEG — Offline Experience Gaps**

| ID | Scenario Ref | Gap Description | Status-Quo Carrying Cost | Observable Signal | Detection Horizon | Rationale | Actionable Recommendation |
|---|---|---|---|---|---|---|---|

No OEG: `OEG-NIL-1: [scope rationale]`

**DCV — Data Consistency Violations**

| ID | Source | Data Type | Failure Mode | Conflict Resolution | Adequacy | Status-Quo Carrying Cost | Observable Signal | Detection Horizon | Rule Applied |
|---|---|---|---|---|---|---|---|---|---|

No DCV: `DCV-NIL-1: [scope rationale]`

**MRF — Missing Recovery Flows**

| ID | Scenario Ref | Absent Mechanism | Status-Quo Carrying Cost | Observable Signal | Detection Horizon | Why No Current Path Exists |
|---|---|---|---|---|---|---|

No MRF: `MRF-NIL-1: [scope rationale]`

```
GATE 3 CLOSE
Exit postconditions:
  [ ] All three categories present; named signal + horizon + rationale per finding
  [ ] Findings without signal have MRF-OBS-NN and RULE-OBS-GAP fired
Gate 3 STATUS: CLOSED / OPEN
```

---

### GATE 4: Amendment Pass

No amendments: `Gate 4: no amendments required.`

```
GATE 4 CLOSE
Exit postconditions:
  [ ] Recovery paths have minimum two actor-labeled steps; superseded nils annotated
Gate 4 STATUS: CLOSED / OPEN
```

---

### Act 1 Terminal: Post-Analysis Rule Registry Audit

| Rule ID | Invocations | Citations | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-CR-DCV | | | | |
| RULE-BARRED-CG | | | | |
| RULE-NIL-SUPERSEDE | | | | |
| RULE-CHAOS-INJECT | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | |
| RULE-OBS-GAP | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | |

POST-ANALYSIS REGISTRY AUDIT (ACT 1) COMPLETE: [no RULE-BYPASSED entries remain]

---

### Act 1 Terminal: Nil Supersession Log

No supersessions: `No supersessions in this run.`

---

### Act 1 Terminal: Bidirectional Chaos-Observability Coverage Matrix

This matrix is a required Act 1 Terminal artifact. Both direction tables and both GAP
REGISTRY blocks must be complete before COMPLETE can be declared. Absence is an Act 1
CLOSE blocker.

**Part A — Forward Direction: Chaos Scenario → Observable Signal**

For each chaos row in Gate 2b, list the Observable Signal ID(s) from Gate 3. If no signal
is linked, mark the row DARK.

| Gate 2b Row | Scenario ID | Observable Signal ID(s) Linked | Link Status |
|---|---|---|---|
| Row 1 | FS-01 | [OEG-NN / DCV-NN / MRF-NN] | Linked / DARK |

**PART A GAP REGISTRY — Dark Chaos Findings**

For each DARK row, write one structured finding block:

```
CHAOS-OBS-GAP-NN:
  Source: Gate 2b Row [N] / Scenario ID: [FS-NN]
  Missing link: no Observable Signal in Gate 3 monitors the fault injected by this scenario
  Consequence: [specific — pass/fail result is unconfirmable in production without a
    monitoring signal for this fault class; test outcome cannot be validated operationally]
```

No dark chaos gaps: `PART A GAP REGISTRY: none.`

---

**Part B — Reverse Direction: Observable Signal → Chaos Scenario**

For each Observable Signal entry in Gate 3, list the Gate 2b chaos row(s). If none, mark
UNVALIDATED.

| Gate 3 Finding ID | Signal Name | Chaos Scenario ID(s) Linked | Link Status |
|---|---|---|---|
| OEG-01 | [named signal] | [FS-NN] | Linked / UNVALIDATED |

**PART B GAP REGISTRY — Unvalidated Signal Findings**

For each UNVALIDATED row, write one structured finding block:

```
OBS-CHAOS-GAP-NN:
  Source: Gate 3 Finding ID: [OEG/DCV/MRF-NN] / Signal: [named signal]
  Missing link: no Gate 2b chaos scenario exercises the fault conditions this signal monitors
  Consequence: [specific — the signal's behavior under fault is untested; cannot confirm it
    fires as specified under fault conditions]
```

No unvalidated signal gaps: `PART B GAP REGISTRY: none.`

---

```
Matrix closure — all four fields required before declaring COMPLETE:
Forward coverage: [N] of [M] chaos rows linked to Observable Signals.
Reverse coverage: [N] of [M] Observable Signals linked to chaos scenarios.
PART A GAP REGISTRY: [CHAOS-OBS-GAP-NN list / none]
PART B GAP REGISTRY: [OBS-CHAOS-GAP-NN list / none]
```

BIDIRECTIONAL CHAOS-OBSERVABILITY COVERAGE MATRIX COMPLETE

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
    Gate 1 / 1b / 2 / 2b / 3 / 4: [CLOSED / OPEN — reason]
    GATE N-bypass blocks: [CLOSED / none]
    Act 1 Registry Audit: [CLOSED / OPEN]
    Bidirectional Chaos-Observability Matrix: [COMPLETE / OPEN — reason]
(2) Act 1 scope exhausted: [yes / list unresolved]
(3) No RULE-BYPASSED conditions remain: [yes / exception]
ACT 1 STATUS: CLOSED / OPEN
```

---

```
ACT 2 OPEN — Commerce Domain Validator
Entry condition: ACT 1 STATUS: CLOSED
Scope: Gate 5 + Act 2 Registry Audit + Inertia Synthesis + ACT 2 CLOSE
```

### GATE 5: Commerce Domain Validation

| Scenario ID | Commerce Operation Named? | Amended Operation | CV Finding Issued |
|---|---|---|---|
| FS-01 | Yes / No | | |

Commerce targets: inventory oversell / payment idempotency / loyalty double-redemption /
order state divergence — each [present / absent — rationale].

```
GATE 5 CLOSE
Exit postconditions: Every scenario anchored; all four targets checked.
Gate 5 STATUS: CLOSED / OPEN
```

### Act 2 Terminal: Post-Analysis Rule Registry Audit

| Rule ID | Invocations | Citations | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-COMMERCE-ANCHOR | | | | |

POST-ANALYSIS REGISTRY AUDIT (ACT 2) COMPLETE

### Inertia Synthesis

Per-finding: failure mode, rate, horizon, metric.
Urgency: HIGH / MEDIUM / LOW. Highest-risk: [gap ID]. Status-quo: [{topic} specific].
Intervention: [owner + threshold + consequence].

```
ACT 2 CLOSE
(1) Gate 5 / bypass / Registry Audit: CLOSED; scope exhausted; no RULE-BYPASSED.
ACT 2 STATUS: CLOSED / OPEN
```

ANALYSIS COMPLETE (declared only when ACT 1 STATUS: CLOSED AND ACT 2 STATUS: CLOSED)

---

---

## V-04

**Variation axis**: Combination — standalone prohibition clause postcondition in Gate 2b
CLOSE (from V-01) + dual-named Gate 1 CLOSE quality postcondition (from V-02). No formal
GAP REGISTRY blocks. DS Primitive VALID/INVALID template retained (C-15). Gate 2b Column
Contract identity assertion and OPEN precondition acknowledgment retained (C-39/C-40).
Gate 1 CLOSE extended with two independent quality postconditions (C-41).

**Hypothesis**: C-40 and C-41 are orthogonal: C-40 governs Gate 2b CLOSE (standalone
prohibition checkbox), C-41 governs Gate 1 CLOSE (dual-named required/prohibited basis).
Combining them without V-03's gap registry tests whether C-40+C-41 alone lift the score
above R12 V-05 (65/66). If V-04 reaches 65/66 or higher, the C-41 fix is independently
sufficient for its criterion. If V-04 scores C-38 higher than R12 V-02 (which has C-40 PASS
but no C-41), that confirms C-41 indirectly supports C-38 via Gate 1 quality.

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
| RULE-CHAOS-INJECT | Include scenario from Gate 1 has no chaos test row in Gate 2b at Gate 2b CLOSE | Emit CE-NN in Gate 2b bypass block; produce all three required chaos test components | DS Expert (Act 1) |
| RULE-OBS-GAP | Named gap finding in Gate 3 has no Observable Signal entry at Gate 3 CLOSE | Emit OS-NN in Gate 3 bypass block; produce named signal + detection horizon + rationale; if no signal exists, emit MRF-OBS-NN | DS Expert (Act 1) |
| RULE-COMMERCE-ANCHOR | Include scenario references a generic operation with no named commerce flow | Amend to name specific operation; record amendment | Commerce Validator (Act 2) |

**Bypass Owner column**: Cross-act invocation is not permitted.

---

### BYPASS GATE-REOPENING PROTOCOL

When any rule shows RULE-BYPASSED in the Post-Analysis Rule Registry Audit:

1. Bypass Owner emits: `GATE N-bypass: REOPENED — [rule ID] — bypass at [gate, entry ID]`
2. Bypass Owner applies the rule and produces required output.
3. Bypass Owner emits: `GATE N-bypass: AMENDED — CLOSED — [rule now applied]`
4. Bypass Owner updates the audit row: Status → INVOKED; BYPASS-TRIGGER → "RESOLVED — [sub-gate]"; Citations += sub-gate.

**COMPLETE may not be declared** while any RULE-BYPASSED entry remains unresolved in any act.

---

### ANTI-OMISSION ARCHITECTURE

| Level | Anti-Omission Mechanism | Omission Risk Targeted | Mechanism Location |
|---|---|---|---|
| Table | Unified row index (`#`) + anti-split instruction | Row fragmentation | `#` column; Gate 2 |
| Section | Phase gate — all rows before Gap Identification | Premature advance | Gate 2 |
| Slot | **"Write this row now."** / **"Do not advance until..."** | Row omission | Row Descriptors |
| Column-Group | C-phase before D-phase within each row | Mid-row omission | Row Descriptors |
| Column | Column ownership in Column Contract | Column omission | Column Contract |

**Anti-split**: Single scenario table. No sub-tables or breaks between rows.

---

### COLUMN CONTRACT

| Column Name | Owner | Phase | Fill Requirement |
|---|---|---|---|
| `#` | Shared | — | Sequential integer; no gaps |
| `ID` | Shared | — | FS-NN format; unique per scenario |
| `Trigger Condition` | DS Expert | C-phase | **Two required components**: (1) threshold expression — quantified activation condition; (2) detection signal — named observable confirming threshold crossing. Threshold used verbatim in Gate 2b. |
| `State` | Commerce Expert | C-phase | Specific system configuration; named components; not "degraded" |
| `Capability` | Commerce Expert | C-phase | Named commerce operations still completable |
| `Data at Risk` | DS Expert | D-phase | Named data type + consistency failure mode |
| `Recovery Path` | DS Expert | D-phase | Four stages each with mechanism \| actor \| SLA \| VS (named observable, distinct from mechanism). Format: Detect / Contain / Recover / Validate. |
| `Severity` | DS Expert | D-phase | `degraded` / `impaired` / `down` |
| `Blast Radius` | DS Expert | D-phase | Fraction or named segment |
| `Rule Applied` | DS Expert | D-phase | Rule ID or `—` |

---

### Pre-Analysis: Commerce Operation Scope Declaration

```
SCOPE DECLARATION
Operations in scope: [minimum four]
Operations excluded (with reason): [or "none"]
SCOPE DECLARATION COMPLETE
```

### Pre-Analysis: Coverage Accountability Roster

| Degradation Class | Committed Minimum | DS Primitive for Impossibility |
|---|---|---|
| Network partition / offline | 2 | [required if slot unfillable — cite DS Primitive by name] |
| Partial service failure | 2 | |
| Eventual consistency | 2 | |

---

```
ACT 1 OPEN — Distributed Systems Expert
Scope: Gates 1–4 + Gate 2b + Act 1 Registry Audit + Nil Supersession Log +
       Bidirectional Chaos-Observability Coverage Matrix + Scope Verification + ACT 1 CLOSE
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

**Argued-Impossible template** — complete this block for every Argued-Impossible row:

```
FS-NN Argued-Impossible:
DS Primitive cited: [name the specific CAP theorem guarantee / synchrony guarantee /
  deployment topology constraint that architecturally forecloses this failure class.
  Must address the architecture of {topic}, not the description of the prompt.]

VALID argument example:
  "DS Primitive cited: Single-datacenter synchronous replication with no async follower —
   forecloses multi-master split-brain because all writes commit synchronously to one
   primary."

INVALID argument example:
  "DS Primitive cited: The topic does not describe a distributed cache, so cache
   invalidation race conditions are not applicable."
  [Fails: description-absence argument. A valid argument must cite the architecture
   guarantee, not what the description omits.]
```

**Gate 1b — BARRED Resolution**

No BARRED entries: `Gate 1b: none.`

```
GATE 1 CLOSE
Exit postconditions:
  [ ] Every candidate has one named disposition
  [ ] Every BARRED has CG-NN emitted
  [ ] Impossibility argument basis confirmed: every Argued-Impossible cites an
      architecture basis (CAP theorem guarantee, synchrony guarantee, or topology
      constraint) — required basis: present
  [ ] Impossibility argument prohibition confirmed: no Argued-Impossible argument is
      based on description absence ("the topic does not mention X") — prohibited basis: absent
  [ ] DS Primitive column in Coverage Accountability Roster populated for any
      impossibility slot
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

**Anti-split**: Single scenario table. **Section gate**: All rows before Gap Identification.
**Column-group gate**: C-phase before D-phase within each row.

#### Row Descriptors

**Row 1 — FS-01: [Scenario Name]**

Consequence context: [acute consequences]. Chronic: [rate] / [horizon] / [metric].

**Write this row now.** Fill Trigger Condition (threshold + detection signal, threshold
verbatim in Gate 2b). C-phase (Commerce Expert) then D-phase (DS Expert).
**Do not advance to Row 2 until all columns non-placeholder including all four VS entries.**

---

**Row 2 — FS-02: [Scenario Name]**

**Write this row now.** Fill all columns per Column Contract.
**C-phase check before D-phase. Do not advance until non-placeholder.**

---

Continue for all remaining Include scenarios.

| # | ID | Trigger Condition | State | Capability | Data at Risk | Recovery Path | Severity | Blast Radius | Rule Applied |
|---|---|---|---|---|---|---|---|---|---|
| 1 | FS-01 | [threshold] / [detection signal] | | | | Detect: [mech\|actor\|TTD\|VS]; Contain: [mech\|actor\|TTC\|VS]; Recover: [mech\|actor\|TTR\|VS]; Validate: [mech\|actor\|TTV\|VS] | | | |

```
GATE 2 CLOSE
Exit postconditions:
  [ ] Every Include scenario has all columns non-trivial
  [ ] Every Trigger Condition has threshold expression + detection signal
  [ ] Every recovery path has four stages each with mechanism, SLA target, named VS
  [ ] All RULE-CR-DCV triggers recorded; column-group gate confirmed every row
Gate 2 STATUS: CLOSED / OPEN — [reason if open]
```

---

### GATE 2b: Chaos Engineering Specification

#### Gate 2b Column Contract

| Column Name | Owner | Fill Requirement |
|---|---|---|
| `#` | Shared | Sequential integer; no gaps |
| `Scenario ID` | Shared | FS-NN; one row per Include scenario |
| `Trigger Condition Reference` | DS Expert | **Identity assertion**: the chaos activation boundary IS the Trigger Condition threshold expression from Gate 2 — identical, not a derivative. Transcribe verbatim. Do not paraphrase, abbreviate, or independently calibrate. |
| `Inject` | DS Expert | `[fault type]: [named mechanism] — [parameter]`. Generic descriptions are not valid. |
| `Expected Observable` | DS Expert | In-fault behavior at named observation granularity; not post-recovery state |
| `Pass-Fail Signal` | DS Expert | Binary artifact naming specific metric value, API response code, log entry, or system state |

```
GATE 2b OPEN
Preconditions:
  [ ] Gate 2 STATUS: CLOSED; Include scenario IDs available
  [ ] Identity assertion acknowledged: chaos activation boundary = Gate 2 threshold
      expression for each scenario, verbatim — not a derivative
Entry confirmed: [yes / no]
```

| # | Scenario ID | Trigger Condition Reference | Inject | Expected Observable | Pass-Fail Signal |
|---|---|---|---|---|---|
| 1 | FS-01 | [verbatim threshold expression from Gate 2 FS-01 — identical to Gate 2 value] | | | |

```
GATE 2b CLOSE
Exit postconditions:
  [ ] One chaos row per Include scenario; no scenarios missing
  [ ] Identity assertion confirmed: every Trigger Condition Reference contains the
      verbatim Gate 2 threshold expression — identical string, not a paraphrase
  [ ] Prohibition clause confirmed: no Trigger Condition Reference contains a paraphrased
      or independently calibrated expression — no paraphrase, no independent calibration
  [ ] Every row has Inject (named fault type, mechanism, parameter — not generic)
  [ ] Every row has Expected Observable at named in-fault observation granularity
  [ ] Every row has Pass-Fail Signal naming a specific binary artifact
  [ ] RULE-CHAOS-INJECT fired for any missing rows; bypass resolved
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

Observable Signal requirement: named signal + concrete detection horizon + rationale.
Generic signals fail. No signal → RULE-OBS-GAP + MRF-OBS-NN.

**OEG — Offline Experience Gaps**

| ID | Scenario Ref | Gap Description | Status-Quo Carrying Cost | Observable Signal | Detection Horizon | Rationale | Actionable Recommendation |
|---|---|---|---|---|---|---|---|
| OEG-01 | FS-NN | | [rate \| horizon \| failure] | [named signal] | [time to alert] | [why early] | |

No OEG: `OEG-NIL-1: [scope rationale]`

**DCV — Data Consistency Violations**

| ID | Source | Data Type | Failure Mode | Conflict Resolution | Adequacy | Status-Quo Carrying Cost | Observable Signal | Detection Horizon | Rule Applied |
|---|---|---|---|---|---|---|---|---|---|
| DCV-01 | FS-NN | | | LWW / merge / manual / reject-stale / undefined | adequate / inadequate / undefined | | | | |

No DCV: `DCV-NIL-1: [scope rationale]`

**MRF — Missing Recovery Flows**

| ID | Scenario Ref | Absent Mechanism | Status-Quo Carrying Cost | Observable Signal | Detection Horizon | Why No Current Path Exists |
|---|---|---|---|---|---|---|
| MRF-01 | FS-NN | | | | | |

No MRF: `MRF-NIL-1: [scope rationale]`

```
GATE 3 CLOSE
Exit postconditions:
  [ ] All three categories present; named signal + horizon + rationale per finding
  [ ] Findings without signal have MRF-OBS-NN and RULE-OBS-GAP fired
  [ ] Status-Quo Carrying Cost present for every named finding
Gate 3 STATUS: CLOSED / OPEN — [reason if open]
```

---

### GATE 4: Amendment Pass

No amendments: `Gate 4: no amendments required.`

```
GATE 4 CLOSE
Exit postconditions:
  [ ] Recovery paths have minimum two actor-labeled steps; superseded nils annotated
Gate 4 STATUS: CLOSED / OPEN
```

---

### Act 1 Terminal: Post-Analysis Rule Registry Audit

| Rule ID | Invocations | Citations | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-CR-DCV | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | |
| RULE-BARRED-CG | | | | |
| RULE-NIL-SUPERSEDE | | | | |
| RULE-CHAOS-INJECT | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | |
| RULE-OBS-GAP | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | |

POST-ANALYSIS REGISTRY AUDIT (ACT 1) COMPLETE: [no RULE-BYPASSED entries remain]

---

### Act 1 Terminal: Nil Supersession Log

No supersessions: `No supersessions in this run.`

---

### Act 1 Terminal: Bidirectional Chaos-Observability Coverage Matrix

**Part A — Forward Direction: Chaos Scenario → Observable Signal**

| Gate 2b Row | Scenario ID | Observable Signal ID(s) Linked | Coverage Gap? |
|---|---|---|---|
| Row 1 | FS-01 | [OEG-NN / DCV-NN / MRF-NN] | No / CHAOS-OBS-GAP-NN |

Dark chaos: `CHAOS-OBS-GAP-NN | Chaos row [N] / [Scenario ID] | no Observable Signal linked | consequence: pass/fail unverifiable in production`

**Part B — Reverse Direction: Observable Signal → Chaos Scenario**

| Gate 3 Finding ID | Signal Name | Chaos Scenario ID(s) Linked | Coverage Gap? |
|---|---|---|---|
| OEG-01 | [named signal] | [FS-NN] | No / OBS-CHAOS-GAP-NN |

Unvalidated signal: `OBS-CHAOS-GAP-NN | [Gate 3 ID] | [signal name] | no chaos scenario linked | consequence: signal behavior under fault untested`

```
Matrix summary:
Forward coverage: [N] of [M] chaos rows have linked Observable Signals.
Reverse coverage: [N] of [M] Observable Signals have linked chaos scenarios.
Dark chaos gaps: [list / none]
Unvalidated signal gaps: [list / none]
```

BIDIRECTIONAL CHAOS-OBSERVABILITY COVERAGE MATRIX COMPLETE

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
    Gate 1 / 1b / 2 / 2b / 3 / 4: [CLOSED / OPEN — reason]
    GATE N-bypass blocks: [CLOSED / none]
    Act 1 Registry Audit: [CLOSED / OPEN]
    Bidirectional Chaos-Observability Matrix: [COMPLETE / OPEN — reason]
(2) Act 1 scope exhausted: [yes / list unresolved]
(3) No RULE-BYPASSED conditions remain: [yes / exception]
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

Commerce targets: inventory oversell / payment idempotency / loyalty double-redemption /
order state divergence — each [present / absent — rationale].

```
GATE 5 CLOSE
Exit postconditions:
  [ ] Every Include scenario anchored; all four targets checked
Gate 5 STATUS: CLOSED / OPEN
```

### Act 2 Terminal: Post-Analysis Rule Registry Audit

| Rule ID | Invocations | Citations | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-COMMERCE-ANCHOR | | | | |

POST-ANALYSIS REGISTRY AUDIT (ACT 2) COMPLETE

### Inertia Synthesis

Per-finding: failure mode, rate, horizon, metric.
Urgency: HIGH / MEDIUM / LOW. Highest-risk: [gap ID]. Status-quo: [{topic} specific].
Intervention: [owner + threshold + consequence].

```
ACT 2 CLOSE
(1) Gate 5 / bypass / Registry Audit: CLOSED; scope exhausted; no RULE-BYPASSED.
ACT 2 STATUS: CLOSED / OPEN
```

ANALYSIS COMPLETE (declared only when ACT 1 STATUS: CLOSED AND ACT 2 STATUS: CLOSED)

---

---

## V-05

**Variation axis**: Full integration — All three R13 interventions combined: (1) standalone
prohibition clause postcondition in Gate 2b CLOSE (V-01, targeting C-40); (2) dual-named
Gate 1 CLOSE quality postcondition (V-02, targeting C-41); (3) formal GAP REGISTRY blocks
in the Bidirectional Coverage Matrix (V-03, targeting C-38). Retains R12 V-05's DS Primitive
VALID/INVALID template (C-15) and Gate 2b Column Contract identity assertion with OPEN
precondition acknowledgment (C-39). This is the candidate for 66/66 uncapped.

**Hypothesis**: C-40, C-41, and C-38 are orthogonal and their interventions do not interact.
Full integration should achieve PASS on all three simultaneously. The discriminating question
for R13: if V-05 achieves 66/66, the standalone prohibition clause checkbox is the form C-40
requires. If V-05 scores C-40 PARTIAL still, then C-40 requires a structural form not yet
identified — the prohibition clause may need to appear as a named section header rather than
a checkbox item, or be syntactically separated at the section level rather than the checkbox
level.

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
| RULE-CHAOS-INJECT | Include scenario from Gate 1 has no chaos test row in Gate 2b at Gate 2b CLOSE | Emit CE-NN in Gate 2b bypass block; produce all three required chaos test components | DS Expert (Act 1) |
| RULE-OBS-GAP | Named gap finding in Gate 3 has no Observable Signal entry at Gate 3 CLOSE | Emit OS-NN in Gate 3 bypass block; produce named signal + detection horizon + rationale; if no signal exists, emit MRF-OBS-NN | DS Expert (Act 1) |
| RULE-COMMERCE-ANCHOR | Include scenario references a generic operation with no named commerce flow | Amend to name specific operation; record amendment | Commerce Validator (Act 2) |

**Bypass Owner column**: Cross-act invocation is not permitted. Commerce Validator cannot
reopen Act 1 gates. DS Expert cannot reopen Act 2 gates.

---

### BYPASS GATE-REOPENING PROTOCOL

**Authority**: DS Expert owns this protocol for Act 1 rules; Commerce Validator for Act 2
rules. Cross-act invocation not permitted.

When any rule shows RULE-BYPASSED in the Post-Analysis Rule Registry Audit:

1. Bypass Owner emits: `GATE N-bypass: REOPENED — [rule ID] — bypass at [gate, entry ID]`
2. Bypass Owner applies the rule and produces required output.
3. Bypass Owner emits: `GATE N-bypass: AMENDED — CLOSED — [rule now applied]`
4. Bypass Owner updates the audit row: Status → INVOKED; BYPASS-TRIGGER → "RESOLVED — [sub-gate]"; Citations += sub-gate.

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

**Anti-split instruction**: Single scenario table in Gate 2. No sub-tables or breaks between rows when ownership shifts.

---

### COLUMN CONTRACT

Place this table before any scenario output.

| Column Name | Owner | Phase | Fill Requirement |
|---|---|---|---|
| `#` | Shared | — | Sequential integer; no gaps |
| `ID` | Shared | — | FS-NN format; unique per scenario |
| `Trigger Condition` | DS Expert | C-phase | **Two required components**: (1) threshold expression — quantified activation condition (e.g., "inventory count falls below safety-stock threshold", "payment API p99 latency > 500ms"); (2) detection signal — named observable confirming threshold crossing. Threshold used verbatim in Gate 2b. |
| `State` | Commerce Expert | C-phase | Specific system configuration; named components and states; not "degraded" |
| `Capability` | Commerce Expert | C-phase | Named commerce operations the user can still complete |
| `Data at Risk` | DS Expert | D-phase | Named data type + consistency failure mode |
| `Recovery Path` | DS Expert | D-phase | Four stages each with three required components: mechanism (named actor) \| SLA target \| VS (named observable confirming stage completion, distinct from mechanism). Format: Detect / Contain / Recover / Validate each with mech \| actor \| SLA \| VS. |
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
| Network partition / offline | 2 | [required if slot unfillable — cite DS Primitive by name] |
| Partial service failure | 2 | |
| Eventual consistency | 2 | |

---

```
ACT 1 OPEN — Distributed Systems Expert
Scope: Gates 1–4 + Gate 2b + Act 1 Registry Audit + Nil Supersession Log +
       Bidirectional Chaos-Observability Coverage Matrix + Scope Verification + ACT 1 CLOSE
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

**Argued-Impossible template** — complete this block for every Argued-Impossible row:

```
FS-NN Argued-Impossible:
DS Primitive cited: [name the specific CAP theorem guarantee / synchrony guarantee /
  deployment topology constraint that architecturally forecloses this failure class.
  Must address the architecture of {topic}, not the description of the prompt.]

VALID argument example:
  "DS Primitive cited: Single-datacenter synchronous replication with no async follower —
   forecloses multi-master split-brain because all writes commit synchronously to one
   primary; no partition scenario produces divergent acknowledged writes under this
   topology."

INVALID argument example:
  "DS Primitive cited: The topic does not describe a distributed cache, so cache
   invalidation race conditions are not applicable."
  [Fails: description-absence argument, not an architecture constraint. The absence of a
   feature from the prompt description does not prove the system lacks it architecturally.
   A valid argument must cite what the architecture guarantees, not what the description
   omits.]
```

Apply this template for every Argued-Impossible row. A DS Primitive field containing a
topic-scope argument is a Gate 1 violation.

**Gate 1b — BARRED Resolution**

No BARRED entries: `Gate 1b: none.`

```
GATE 1 CLOSE
Exit postconditions:
  [ ] Every candidate has one named disposition
  [ ] Every BARRED has CG-NN emitted
  [ ] Impossibility argument basis confirmed: every Argued-Impossible cites an
      architecture basis (CAP theorem guarantee, synchrony guarantee, or topology
      constraint that architecturally forecloses the failure class) — required basis: present
  [ ] Impossibility argument prohibition confirmed: no Argued-Impossible argument is
      based on description absence ("the topic does not mention X", "the description is
      too simple for this") — prohibited basis: absent
  [ ] DS Primitive column in Coverage Accountability Roster populated for any
      impossibility slot
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
**Column-group gate**: C-phase before D-phase within each row.

#### Row Descriptors

**Row 1 — FS-01: [Scenario Name]**

Consequence context: [acute consequences — oversell / double-charge / duplicate fulfillment]. Chronic: [rate] / [horizon] / [metric].

**Write this row now.**
Fill Trigger Condition: threshold expression + detection signal (threshold verbatim in Gate 2b).
C-phase (Commerce Expert): fill State and Capability.
**C-phase complete check before D-phase.**
D-phase (DS Expert): fill Data at Risk, Recovery Path (four stages, mech | actor | SLA | VS), Severity, Blast Radius, Rule Applied.
**Do not advance to Row 2 until all columns non-placeholder including all four VS entries.**

---

**Row 2 — FS-02: [Scenario Name]**

Consequence context: [payment idempotency / loyalty double-redemption / order divergence]. Chronic: reconciliation backlog / without ceiling.

**Write this row now.** Fill all columns per Column Contract.
**C-phase check before D-phase. Do not advance until non-placeholder.**

---

Continue for all remaining Include scenarios.

| # | ID | Trigger Condition | State | Capability | Data at Risk | Recovery Path | Severity | Blast Radius | Rule Applied |
|---|---|---|---|---|---|---|---|---|---|
| 1 | FS-01 | [threshold] / [detection signal] | | | | Detect: [mech\|actor\|TTD\|VS]; Contain: [mech\|actor\|TTC\|VS]; Recover: [mech\|actor\|TTR\|VS]; Validate: [mech\|actor\|TTV\|VS] | | | |

```
GATE 2 CLOSE
Exit postconditions:
  [ ] Every Include scenario has all columns non-trivial
  [ ] Every Trigger Condition has threshold expression + detection signal
  [ ] Every recovery path has four stages each with mechanism, SLA target, named VS
  [ ] All RULE-CR-DCV triggers recorded; column-group gate confirmed every row
Gate 2 STATUS: CLOSED / OPEN — [reason if open]
```

---

### GATE 2b: Chaos Engineering Specification

#### Gate 2b Column Contract

| Column Name | Owner | Fill Requirement |
|---|---|---|
| `#` | Shared | Sequential integer; no gaps |
| `Scenario ID` | Shared | FS-NN; one row per Include scenario |
| `Trigger Condition Reference` | DS Expert | **Identity assertion**: the chaos activation boundary IS the Gate 2 Trigger Condition threshold expression — identical, not a derivative. Transcribe verbatim. Do not paraphrase, abbreviate, or add conditions not in Gate 2. Any modification produces an uncalibrated test. |
| `Inject` | DS Expert | `[fault type]: [named mechanism] — [parameter]`. Generic descriptions not valid. |
| `Expected Observable` | DS Expert | In-fault behavior at named observation granularity; not post-recovery state |
| `Pass-Fail Signal` | DS Expert | Binary artifact naming specific metric value, API response code, log entry, or system state |

```
GATE 2b OPEN
Preconditions:
  [ ] Gate 2 STATUS: CLOSED; Include scenario IDs available
  [ ] Identity assertion acknowledged: chaos activation boundary = Gate 2 threshold
      expression for each scenario, verbatim — not a derivative
Entry confirmed: [yes / no]
```

| # | Scenario ID | Trigger Condition Reference | Inject | Expected Observable | Pass-Fail Signal |
|---|---|---|---|---|---|
| 1 | FS-01 | [verbatim threshold expression from Gate 2 FS-01 — identical to Gate 2 value] | | | |

```
GATE 2b CLOSE
Exit postconditions:
  [ ] One chaos row per Include scenario; no scenarios missing
  [ ] Identity assertion confirmed: every Trigger Condition Reference contains the
      verbatim Gate 2 threshold expression — identical string, not a paraphrase
  [ ] Prohibition clause confirmed: no Trigger Condition Reference contains a paraphrased
      or independently calibrated expression — no paraphrase, no independent calibration
  [ ] Every row has Inject (named fault type, mechanism, parameter — not generic)
  [ ] Every row has Expected Observable at named in-fault observation granularity
  [ ] Every row has Pass-Fail Signal naming a specific binary artifact
  [ ] RULE-CHAOS-INJECT fired for any missing rows; bypass resolved before this close
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

Observable Signal requirement: (1) named signal; (2) concrete detection horizon; (3) rationale.
Generic signals fail. No signal → RULE-OBS-GAP + MRF-OBS-NN.

**OEG — Offline Experience Gaps**

| ID | Scenario Ref | Gap Description | Status-Quo Carrying Cost | Observable Signal | Detection Horizon | Rationale | Actionable Recommendation |
|---|---|---|---|---|---|---|---|
| OEG-01 | FS-NN | | [rate \| horizon \| failure] | [named signal] | [time to alert] | [why early] | |

No OEG: `OEG-NIL-1: [scope rationale]`

**DCV — Data Consistency Violations**

| ID | Source | Data Type | Failure Mode | Conflict Resolution | Adequacy | Status-Quo Carrying Cost | Observable Signal | Detection Horizon | Rule Applied |
|---|---|---|---|---|---|---|---|---|---|
| DCV-01 | FS-NN | | | LWW / merge / manual / reject-stale / undefined | adequate / inadequate / undefined | [rate \| horizon \| metric] | [named signal] | [time to alert] | |

No DCV: `DCV-NIL-1: [scope rationale]`

**MRF — Missing Recovery Flows**

| ID | Scenario Ref | Absent Mechanism | Status-Quo Carrying Cost | Observable Signal | Detection Horizon | Why No Current Path Exists |
|---|---|---|---|---|---|---|
| MRF-01 | FS-NN | | [rate \| horizon \| failure] | [named signal] | [time to alert] | |

No MRF: `MRF-NIL-1: [scope rationale]`

```
GATE 3 CLOSE
Exit postconditions:
  [ ] All three categories present; named signal + horizon + rationale per finding
  [ ] Findings without signal have MRF-OBS-NN and RULE-OBS-GAP fired
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

No amendments: `Gate 4: no amendments required. No gate re-opens triggered.`

```
GATE 4 CLOSE
Exit postconditions:
  [ ] Recovery paths have minimum two actor-labeled steps; superseded nils annotated
Gate 4 STATUS: CLOSED / OPEN
```

---

### Act 1 Terminal: Post-Analysis Rule Registry Audit

**BYPASS-TRIGGER column**: A RULE-BYPASSED status requires a non-empty BYPASS-TRIGGER entry.

| Rule ID | Invocations | Citations (gate, entry) | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-CR-DCV | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | |
| RULE-BARRED-CG | | | | |
| RULE-NIL-SUPERSEDE | | | | |
| RULE-CHAOS-INJECT | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | |
| RULE-OBS-GAP | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | |

POST-ANALYSIS REGISTRY AUDIT (ACT 1) COMPLETE: [confirm no RULE-BYPASSED entries remain]

---

### Act 1 Terminal: Nil Supersession Log

No supersessions: `No supersessions in this run.`

---

### Act 1 Terminal: Bidirectional Chaos-Observability Coverage Matrix

This matrix is a required Act 1 Terminal artifact. Both direction tables and both GAP
REGISTRY blocks must be complete before COMPLETE can be declared. Absence is an Act 1
CLOSE blocker.

**Part A — Forward Direction: Chaos Scenario → Observable Signal**

For each chaos row in Gate 2b, identify the Observable Signal ID(s) from Gate 3. If no
signal is linked, mark DARK.

| Gate 2b Row | Scenario ID | Observable Signal ID(s) Linked | Link Status |
|---|---|---|---|
| Row 1 | FS-01 | [OEG-NN / DCV-NN / MRF-NN] | Linked / DARK |

**PART A GAP REGISTRY — Dark Chaos Findings**

For each DARK row, write one structured finding block:

```
CHAOS-OBS-GAP-NN:
  Source: Gate 2b Row [N] / Scenario ID: [FS-NN]
  Missing link: no Observable Signal in Gate 3 monitors the fault injected by this scenario
  Consequence: [specific — pass/fail result unconfirmable in production without a
    monitoring signal; test outcome cannot be operationally validated]
```

No dark chaos gaps: `PART A GAP REGISTRY: none.`

---

**Part B — Reverse Direction: Observable Signal → Chaos Scenario**

For each Observable Signal entry in Gate 3, identify the Gate 2b chaos row(s). If none,
mark UNVALIDATED.

| Gate 3 Finding ID | Signal Name | Chaos Scenario ID(s) Linked | Link Status |
|---|---|---|---|
| OEG-01 | [named signal] | [FS-NN] | Linked / UNVALIDATED |

**PART B GAP REGISTRY — Unvalidated Signal Findings**

For each UNVALIDATED row, write one structured finding block:

```
OBS-CHAOS-GAP-NN:
  Source: Gate 3 Finding ID: [OEG/DCV/MRF-NN] / Signal: [named signal]
  Missing link: no Gate 2b chaos scenario exercises the fault conditions this signal monitors
  Consequence: [specific — signal behavior under fault untested; cannot confirm it fires
    as specified; production behavior under this failure class unconfirmed]
```

No unvalidated signal gaps: `PART B GAP REGISTRY: none.`

---

```
Matrix closure — all four fields required before declaring COMPLETE:
Forward coverage: [N] of [M] chaos rows linked to Observable Signals.
Reverse coverage: [N] of [M] Observable Signals linked to chaos scenarios.
PART A GAP REGISTRY: [CHAOS-OBS-GAP-NN list / none]
PART B GAP REGISTRY: [OBS-CHAOS-GAP-NN list / none]
```

BIDIRECTIONAL CHAOS-OBSERVABILITY COVERAGE MATRIX COMPLETE

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
    Bidirectional Chaos-Observability Matrix: [COMPLETE / OPEN — reason]
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
| RULE-COMMERCE-ANCHOR | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | |

POST-ANALYSIS REGISTRY AUDIT (ACT 2) COMPLETE

---

### Inertia Synthesis — What Does Doing Nothing Cost?

Per-finding: failure mode, rate, horizon, metric (from Gate 3 Status-Quo Carrying Cost).

Urgency: HIGH / MEDIUM / LOW
Highest-risk finding: [gap ID] — [carrying cost from Gate 3]
Status-quo option: [what "do nothing" looks like for `{topic}` specifically]
Intervention recommendation: [owner + threshold + consequence of missing threshold]

```
ACT 2 CLOSE (sign-off)
(1) All gates within Act 2 CLOSED:
    Gate 5: [CLOSED / OPEN — reason]
    GATE 5-bypass blocks (if triggered): [CLOSED / none triggered]
    Act 2 Registry Audit: [CLOSED / OPEN — reason]
(2) Act 2 scope exhausted: [yes — all scenarios anchored; CV targets checked; inertia complete]
(3) No RULE-BYPASSED remain: [yes / exception]
ACT 2 STATUS: CLOSED / OPEN
```

ANALYSIS COMPLETE (declared only when ACT 1 STATUS: CLOSED AND ACT 2 STATUS: CLOSED)
