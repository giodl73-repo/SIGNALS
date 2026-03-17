---
name: signal-flow-resilience
description: Degraded-condition simulation covering offline, partial failure, and eventual consistency.
allowed-tools: [Read, Write, Glob]
param_set: lean
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

1. Bypass Owner emits: GATE N-bypass: REOPENED -- [rule ID] -- bypass at [gate, entry ID]
2. Bypass Owner applies the rule and produces required output.
3. Bypass Owner emits: GATE N-bypass: AMENDED -- CLOSED -- [rule now applied]
4. Bypass Owner updates the audit row: Status -> INVOKED; BYPASS-TRIGGER ->
   "RESOLVED -- [sub-gate]"; Citations += sub-gate.

**COMPLETE may not be declared** while any RULE-BYPASSED entry remains unresolved in any act.

---

### ANTI-OMISSION ARCHITECTURE

| Level | Anti-Omission Mechanism | Omission Risk Targeted | Mechanism Location |
|---|---|---|---|
| Table | Unified row index + anti-split instruction | Row fragmentation | # column; anti-split in Gate 2 |
| Section | Phase gate -- all rows complete before Gap Identification | Premature section advance | Section gate in Gate 2 |
| Slot | In-row bold imperative: Write this row now. | Row omission under token pressure | Row Descriptors |
| Column-Group | Intra-row phase gate: C-phase complete before D-phase begins | Mid-row D-phase omission | Row Descriptors |
| Column | Column ownership per header in Column Contract | Individual column omission | Column Contract |
| VS | Recovery Stage VS Registry -- all row VS entries registered before ACT 1 CLOSE | VS omission invisible at row level | Act 1 Terminal: VS Registry |

**Anti-split instruction**: Single scenario table in Gate 2. No sub-tables or breaks.

---

### COLUMN CONTRACT

| Column Name | Owner | Phase | Fill Requirement |
|---|---|---|---|
| # | Shared | -- | Sequential integer; no gaps |
| ID | Shared | -- | FS-NN format; unique per scenario |
| Trigger Condition | DS Expert | C-phase | Two required components: (1) threshold expression -- quantified activation condition (e.g., "inventory count falls below safety-stock threshold", "payment API p99 latency > 500ms"); (2) detection signal -- named observable confirming threshold crossing. Threshold expression used verbatim in Gate 2b. |
| State | Commerce Expert | C-phase | Specific system configuration; named components and states |
| Capability | Commerce Expert | C-phase | Named commerce operations still completable |
| Data at Risk | DS Expert | D-phase | Named data type + consistency failure mode |
| Recovery Path | DS Expert | D-phase | Four stages each with mechanism (named actor), SLA target, VS (named observable confirming stage completion, distinct from mechanism). Each VS will be registered in the Act 1 Terminal VS Registry. Format: Detect / Contain / Recover / Validate each with mech, actor, SLA, VS. |
| Severity | DS Expert | D-phase | degraded / impaired / down |
| Blast Radius | DS Expert | D-phase | Fraction or named segment |
| Rule Applied | DS Expert | D-phase | Rule ID or -- |

---

### Pre-Analysis: Commerce Operation Scope Declaration

SCOPE DECLARATION
Operations in scope: [minimum four from: checkout / inventory reservation / payment
processing / order fulfillment / cart state / loyalty redemption / return-refund]
Operations explicitly excluded (with reason): [list or "none"]
SCOPE DECLARATION COMPLETE

### Pre-Analysis: Coverage Accountability Roster

| Degradation Class | Committed Minimum | DS Primitive for Impossibility |
|---|---|---|
| Network partition / offline | 2 | [required if slot unfillable -- cite DS Primitive by name] |
| Partial service failure | 2 | |
| Eventual consistency | 2 | |

---

ACT 1 OPEN -- Distributed Systems Expert
Scope: Gates 1-4 + Gate 2b + Act 1 Registry Audit + Nil Supersession Log +
       Recovery Stage VS Cross-Reference Registry +
       Bidirectional Chaos-Observability Coverage Matrix + Scope Verification + ACT 1 CLOSE

### GATE 1: Discovery and Triage

GATE 1 OPEN
Preconditions:
  [ ] SCOPE DECLARATION COMPLETE present
  [ ] Coverage Accountability Roster committed
Entry confirmed: [yes / no]

| # | ID | Failure Class | Confidence Basis | Disposition | Rule Applied | Notes |
|---|---|---|---|---|---|---|
| 1 | FS-01 | | | Include / BARRED / Argued-Impossible | RULE-BARRED-CG or -- | |

BARRED: cite RULE-BARRED-CG; emit CG-NN.

**Argued-Impossible template** -- complete for every Argued-Impossible row:

FS-NN Argued-Impossible:
DS Primitive cited: [name the specific CAP theorem guarantee / synchrony guarantee /
  deployment topology constraint that architecturally forecloses this failure class.
  Must address the architecture of {topic}, not the description of the prompt.]

VALID argument example:
  "DS Primitive cited: Single-datacenter synchronous replication with no async follower --
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

Apply this template for every Argued-Impossible row.

**Gate 1b -- BARRED Resolution**

| BARRED ID | Confidence Basis | Resolved? | Resolution Mechanism | New Disposition |
|---|---|---|---|---|

No BARRED entries: Gate 1b: none.

GATE 1 CLOSE
Exit postconditions:
  [ ] Every candidate has one named disposition
  [ ] Every BARRED has CG-NN emitted
  [ ] Impossibility argument basis confirmed: every Argued-Impossible cites an
      architecture basis (CAP theorem guarantee, synchrony constraint, or topology
      bound that architecturally forecloses the failure class) -- required basis: present
  [ ] Impossibility argument prohibition confirmed: no Argued-Impossible argument is
      based on description absence ("the topic does not mention X", "the description is
      too simple for this") -- prohibited basis: absent
  [ ] DS Primitive column in Coverage Accountability Roster populated for any
      impossibility slot
  [ ] Roster counts updated
Gate 1 STATUS: CLOSED / OPEN -- [reason if open]

---

### GATE 2: Four-Field Scenario Analysis

GATE 2 OPEN
Preconditions:
  [ ] Gate 1 STATUS: CLOSED
Entry confirmed: [yes / no]

**Anti-split**: Single scenario table. No sub-tables by ownership. No breaks between rows.
**Section gate**: All scenario rows complete before Gap Identification.
**Column-group gate**: C-phase before D-phase within each row.

#### Row Descriptors

**Row 1 -- FS-01: [Scenario Name]**

Consequence context: [acute consequences per resolution branch -- oversell / double-charge /
duplicate fulfillment]. Chronic if never addressed: [rate] / [horizon] / [metric].

**Write this row now.**
Fill Trigger Condition: (1) threshold expression naming quantified activation condition;
(2) detection signal naming observable confirming threshold crossing. Threshold verbatim
in Gate 2b.
C-phase (Commerce Expert): State + Capability.
**C-phase complete check: do not begin D-phase until Trigger Condition, State, Capability
are non-placeholder.**
D-phase (DS Expert): Data at Risk, Recovery Path (four stages: mechanism, actor, SLA, VS --
each VS will be registered in the Act 1 Terminal VS Registry), Severity, Blast Radius,
Rule Applied.
**Do not advance to Row 2 until all columns non-placeholder and all four VS entries named.**

---

**Row 2 -- FS-02: [Scenario Name]**

**Write this row now.** Fill all columns per Column Contract.
**C-phase complete check before D-phase. Do not advance to Row 3 until non-placeholder.**

---

Continue this pattern for all remaining Include scenarios.

| # | ID | Trigger Condition | State | Capability | Data at Risk | Recovery Path | Severity | Blast Radius | Rule Applied |
|---|---|---|---|---|---|---|---|---|---|
| 1 | FS-01 | [threshold] / [detection signal] | | | | Detect: [mech,actor,TTD,VS]; Contain: [mech,actor,TTC,VS]; Recover: [mech,actor,TTR,VS]; Validate: [mech,actor,TTV,VS] | | | |

GATE 2 CLOSE
Exit postconditions:
  [ ] Every Include scenario has all columns non-trivial
  [ ] Every Trigger Condition has threshold expression + detection signal
  [ ] Every recovery path has four stages each with mechanism, SLA target, named VS
  [ ] All RULE-CR-DCV triggers recorded
  [ ] Column-group gate confirmed for every row
Gate 2 STATUS: CLOSED / OPEN -- [reason if open]

---

### GATE 2b: Chaos Engineering Specification

#### Gate 2b Column Contract

| Column Name | Owner | Fill Requirement |
|---|---|---|
| # | Shared | Sequential integer; no gaps |
| Scenario ID | Shared | FS-NN; one row per Include scenario |
| Trigger Condition Reference | DS Expert | Identity assertion: chaos activation boundary = Gate 2 threshold expression verbatim -- identical, not a derivative or approximation. Transcribe exact threshold expression string. Do not paraphrase, abbreviate, or add conditions. |
| Inject | DS Expert | [fault type]: [named mechanism] -- [parameter]. Generic descriptions fail. |
| Expected Observable | DS Expert | In-fault system behavior at named observation granularity; not post-recovery state |
| Pass-Fail Signal | DS Expert | Binary artifact naming specific metric, response code, log entry, or system state |

GATE 2b OPEN
Preconditions:
  [ ] Gate 2 STATUS: CLOSED
  [ ] Include scenario list from Gate 1 available
  [ ] Identity assertion acknowledged: chaos activation boundary = Gate 2 threshold
      expression for each scenario, verbatim -- not a derivative
Entry confirmed: [yes / no]

| # | Scenario ID | Trigger Condition Reference | Inject | Expected Observable | Pass-Fail Signal |
|---|---|---|---|---|---|
| 1 | FS-01 | [verbatim threshold expression from Gate 2 FS-01 -- identical to Gate 2 value] | | | |

GATE 2b CLOSE
Exit postconditions:
  [ ] One chaos row per Include scenario; no scenarios missing
  [ ] Identity assertion confirmed: every Trigger Condition Reference contains the
      verbatim Gate 2 threshold expression -- identical string, not a paraphrase
  [ ] Prohibition clause confirmed: no Trigger Condition Reference contains a paraphrased
      or independently calibrated expression -- no paraphrase, no independent calibration
  [ ] Every row has Inject with named fault type, mechanism, and parameter (not generic)
  [ ] Every row has Expected Observable at named in-fault observation granularity
  [ ] Every row has Pass-Fail Signal naming a specific binary artifact
  [ ] RULE-CHAOS-INJECT fired for any missing rows; bypass resolved before this close
Gate 2b STATUS: CLOSED / OPEN -- [reason if open]

---

### GATE 3: Gap Identification

GATE 3 OPEN
Preconditions:
  [ ] Gate 2 STATUS: CLOSED
Entry confirmed: [yes / no]

**Observable Signal requirement**: Every named finding must carry: (1) named signal;
(2) detection horizon (concrete time window); (3) rationale sentence. Generic signals fail.
If no observable signal exists, invoke RULE-OBS-GAP and emit MRF-OBS-NN.

**OEG -- Offline Experience Gaps**

| ID | Scenario Ref | Gap Description | Status-Quo Carrying Cost | Observable Signal | Detection Horizon | Rationale | Actionable Recommendation |
|---|---|---|---|---|---|---|---|
| OEG-01 | FS-NN | | [rate, horizon, user failure] | [named signal] | [time to alert] | [why early] | |

No OEG: OEG-NIL-1: [scope rationale]

**DCV -- Data Consistency Violations**

| ID | Source | Data Type | Failure Mode | Conflict Resolution | Adequacy | Status-Quo Carrying Cost | Observable Signal | Detection Horizon | Rule Applied |
|---|---|---|---|---|---|---|---|---|---|
| DCV-01 | FS-NN | | | LWW / merge / manual / reject-stale / undefined | adequate / inadequate / undefined | [rate, horizon, metric] | [named signal] | [time to alert] | |

No DCV: DCV-NIL-1: [scope rationale]

**MRF -- Missing Recovery Flows**

| ID | Scenario Ref | Absent Mechanism | Status-Quo Carrying Cost | Observable Signal | Detection Horizon | Why No Current Path Exists |
|---|---|---|---|---|---|---|
| MRF-01 | FS-NN | | [rate, horizon, failure] | [named signal] | [time to alert] | |

No MRF: MRF-NIL-1: [scope rationale]

GATE 3 CLOSE
Exit postconditions:
  [ ] All three gap categories present; every finding or typed nil with scope rationale
  [ ] Every named finding has Observable Signal (named signal + detection horizon + rationale)
  [ ] Findings with no observable signal have MRF-OBS-NN emitted and RULE-OBS-GAP fired
  [ ] Status-Quo Carrying Cost present for every named finding
  [ ] All RULE-CR-DCV entries assigned DCV-NN
Gate 3 STATUS: CLOSED / OPEN -- [reason if open]

---

### GATE 4: Amendment Pass

GATE 4 OPEN
Preconditions:
  [ ] Gate 3 STATUS: CLOSED
Entry confirmed: [yes / no]

| AMD ID | Entry ID | Original (summary) | Amended (summary) | Rule Invoked | Gate Re-Opened? |
|---|---|---|---|---|---|

No amendments: Gate 4: no amendments required.

GATE 4 CLOSE
Exit postconditions:
  [ ] All recovery paths have minimum two actor-labeled steps
  [ ] Every superseded nil has SUPERSEDED annotation with finding ID
Gate 4 STATUS: CLOSED / OPEN -- [reason if open]

---

### Act 1 Terminal: Post-Analysis Rule Registry Audit

| Rule ID | Invocations | Citations (gate, entry) | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-CR-DCV | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | [empty or trigger citation] |
| RULE-BARRED-CG | | | | |
| RULE-NIL-SUPERSEDE | | | | |
| RULE-CHAOS-INJECT | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | |
| RULE-OBS-GAP | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | |

POST-ANALYSIS REGISTRY AUDIT (ACT 1) COMPLETE: [confirm no RULE-BYPASSED entries remain]

---

### Act 1 Terminal: Nil Supersession Log

No supersessions: No supersessions in this run.

---

### Act 1 Terminal: Recovery Stage VS Cross-Reference Registry

This registry is a required Act 1 Terminal artifact. For every named Verification Signal
(VS) written in the Recovery Path column across all Gate 2 scenario rows, register one
entry here. A missing registry entry for any VS named in Gate 2 is an ACT 1 CLOSE blocker.

**VS Registry format**:

| VS ID | Stage Context | Observation Assertion |
|---|---|---|
| VS-01 | FS-NN -- [stage name: Detect / Contain / Recover / Validate] | [what specific observable artifact confirms this stage is complete -- name the metric, log entry, response code, or system state; state the condition under which it fires; must be independently confirmable without reading the Recovery Path column] |

**VS ID assignment**: VS-NN sequential across all scenarios and all stages. One entry per
named VS. When two scenarios share an identical VS specification, assign distinct IDs and
note: "Same signal as VS-MM; independently registered for scenario FS-NN."

**Observation Assertion requirement**: Must name the specific observable (not the
mechanism) and state the binary condition under which it confirms stage completion.
Generic assertions ("monitoring confirms completion", "system returns to normal") fail.
An assertion that cannot be independently evaluated as true or false without reading the
scenario row fails this criterion.

**Completion gate**: COMPLETE may not be declared if any Recovery Path VS in Gate 2 has
no registry entry. When Gate 2 has zero Include scenarios, emit: VS REGISTRY: none.

VS REGISTRY COMPLETE: [list VS IDs, e.g., VS-01 through VS-NN / none if zero scenarios]

---

### Act 1 Terminal: Bidirectional Chaos-Observability Coverage Matrix

This matrix is a required Act 1 Terminal artifact. It verifies that every chaos scenario is
linked to at least one Observable Signal (forward direction) and every Observable Signal is
linked to at least one chaos scenario (reverse direction). Absence is an Act 1 CLOSE blocker.

**Part A -- Forward Direction: Chaos Scenario -> Observable Signal**

| Gate 2b Row | Scenario ID | Observable Signal ID(s) Linked | Coverage Status |
|---|---|---|---|
| Row 1 | FS-01 | [OEG-NN / DCV-NN / MRF-NN] | Linked / DARK |

**PART A GAP REGISTRY -- Dark Chaos Findings**

For each DARK row, write one structured finding block:

  CHAOS-OBS-GAP-NN
  Source: [Gate 2b Row N / Scenario ID FS-NN -- the chaos scenario with no signal linkage]
  Missing link: [no Observable Signal in Gate 3 monitors the fault injected by this row;
    name the specific fault class and why no Gate 3 signal covers it]
  Consequence: [the chaos test result cannot be operationally confirmed; production fault
    detection for this fault class is unverified; test outcome is not predictive of
    production monitoring behavior without a linked Observable Signal]

No dark chaos gaps: PART A GAP REGISTRY: none.

---

**Part B -- Reverse Direction: Observable Signal -> Chaos Scenario**

| Gate 3 Finding ID | Signal Name | Chaos Scenario ID(s) Linked | Coverage Status |
|---|---|---|---|
| OEG-01 | [named signal] | [FS-NN] | Linked / UNVALIDATED |

**PART B GAP REGISTRY -- Unvalidated Signal Findings**

For each UNVALIDATED row, write one structured finding block:

  OBS-CHAOS-GAP-NN
  Source: [Gate 3 Finding ID / Signal Name -- the Observable Signal with no chaos linkage]
  Missing link: [no Gate 2b row injects the fault condition monitored by this signal]
  Consequence: [the Observable Signal has not been validated under controlled fault
    injection; production behavior of this signal under its target fault class is untested;
    cannot confirm the signal fires as specified]

No unvalidated signal gaps: PART B GAP REGISTRY: none.

---

Matrix closure -- all four fields required before declaring COMPLETE:
Forward coverage: [N] of [M] chaos rows linked to Observable Signals.
Reverse coverage: [N] of [M] Observable Signals linked to chaos scenarios.
PART A GAP REGISTRY: [CHAOS-OBS-GAP-NN list / none]
PART B GAP REGISTRY: [OBS-CHAOS-GAP-NN list / none]

BIDIRECTIONAL CHAOS-OBSERVABILITY COVERAGE MATRIX COMPLETE

---

### Act 1 Terminal: Scope Verification

| Declared Operation | Covered | Gap Finding |
|---|---|---|
| [operation] | Yes / No | SV-GAP-NN / -- |

SCOPE VERIFICATION COMPLETE

---

ACT 1 CLOSE (sign-off)
(1) All gates within Act 1 CLOSED:
    Gate 1:     [CLOSED / OPEN -- reason]
    Gate 1b:    [CLOSED / N/A]
    Gate 2:     [CLOSED / OPEN -- reason]
    Gate 2b:    [CLOSED / OPEN -- reason]
    Gate 3:     [CLOSED / OPEN -- reason]
    Gate 4:     [CLOSED / OPEN -- reason]
    GATE N-bypass blocks (if triggered): [CLOSED / none triggered]
    Act 1 Registry Audit: [CLOSED / OPEN -- reason]
    VS Cross-Reference Registry: [COMPLETE / OPEN -- reason]
    Bidirectional Chaos-Observability Matrix: [COMPLETE / OPEN -- reason]
(2) Act 1 scope exhausted: [yes / list any unresolved items]
(3) No RULE-BYPASSED conditions remain unresolved within Act 1: [yes / exception detail]
ACT 1 STATUS: CLOSED / OPEN

---

ACT 2 OPEN -- Commerce Domain Validator
Entry condition: ACT 1 STATUS: CLOSED
Scope: Gate 5 + Act 2 Registry Audit + Inertia Synthesis + ACT 2 CLOSE

### GATE 5: Commerce Domain Validation

GATE 5 OPEN
Preconditions:
  [ ] ACT 1 STATUS: CLOSED
Entry confirmed: [yes / no]

| Scenario ID | Commerce Operation Named? | Amended Operation (RULE-COMMERCE-ANCHOR) | CV Finding Issued |
|---|---|---|---|
| FS-01 | Yes / No | | -- / CV-DCV-01 / CV-OEG-01 / CV-MRF-01 |

Commerce-domain finding targets:
- Inventory oversell under partition: [present / absent -- rationale]
- Payment idempotency window expiry: [present / absent -- rationale]
- Loyalty point double-redemption under split-brain: [present / absent -- rationale]
- Order state divergence under partial fulfillment failure: [present / absent -- rationale]

GATE 5 CLOSE
Exit postconditions:
  [ ] Every Include scenario anchored to a named commerce operation
  [ ] All RULE-COMMERCE-ANCHOR invocations recorded
  [ ] All four commerce-domain targets checked
Gate 5 STATUS: CLOSED / OPEN -- [reason if open]

---

### Act 2 Terminal: Post-Analysis Rule Registry Audit

| Rule ID | Invocations | Citations | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-COMMERCE-ANCHOR | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | |

POST-ANALYSIS REGISTRY AUDIT (ACT 2) COMPLETE

---

### Inertia Synthesis -- What Does Doing Nothing Cost?

Per-finding carrying cost: For each named gap: failure mode, rate, horizon, metric.

Overall synthesis:
Urgency: HIGH / MEDIUM / LOW
Highest-risk finding: [gap ID] -- [carrying cost from Gate 3]
Status-quo option: [what "do nothing" looks like for {topic} specifically]
Intervention recommendation: [owner + threshold + consequence of missing threshold]

ACT 2 CLOSE (sign-off)
(1) All gates within Act 2 CLOSED:
    Gate 5: [CLOSED / OPEN -- reason]
    GATE 5-bypass blocks: [CLOSED / none triggered]
    Act 2 Registry Audit: [CLOSED / OPEN -- reason]
(2) Act 2 scope exhausted: [yes]
(3) No RULE-BYPASSED conditions remain: [yes / exception detail]
ACT 2 STATUS: CLOSED / OPEN

ANALYSIS COMPLETE (declared only when ACT 1 STATUS: CLOSED AND ACT 2 STATUS: CLOSED)