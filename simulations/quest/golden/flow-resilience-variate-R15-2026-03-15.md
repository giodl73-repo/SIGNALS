# Flow-Resilience Skill — Round 15 Variations (Rubric v14)

**Skill**: flow-resilience — Simulate degraded conditions: offline, partial failure, eventual
consistency.
**Rubric**: v14 (C-01 through C-44, essential/recommended/aspirational tiers)
**Date**: 2026-03-15

---

## Round 15 Context

**No new criteria entering R15**: v14 is current. v15 criteria will be extracted from R15
excellence signals. R15 goal: close all open gaps from v14 across all variations and
introduce a new structural property in V-05 as a candidate for C-45.

**R13 ceiling under v14**:
- V-05 72/72 (C-42 PASS, C-43 PASS, C-44 PASS)
- V-04 70/72 (C-44 FAIL)
- V-01 68/72 (C-43 FAIL, C-44 FAIL)
- V-02 67/72 (C-42 FAIL, C-44 FAIL)
- V-03 65/72 (C-42 FAIL, C-43 FAIL)

**R15 targets**:
- Crack C-43 PASS for V-01 — Gate 1 CLOSE split into two independent checkboxes
  (required-basis:present + prohibited-basis:absent), one structural split away from 70/72
- Crack C-42 PASS for V-02 — Gate 2b CLOSE split into two independent checkboxes
  (identity confirmed + prohibition confirmed), one structural split away from 69/72
- Crack C-42 + C-43 PASS for V-03 — both Gate CLOSE splits while preserving C-44 formal
  registry, bringing V-03 to 72/72 from 65/72 starting point
- Crack C-44 PASS for V-04 — formal PART A + PART B GAP REGISTRY added while preserving
  C-42 + C-43, bringing V-04 to 72/72 from 70/72 starting point
- V-05: maintain 72/72 + introduce Recovery Stage VS Cross-Reference Registry as a new Act
  1 Terminal artifact — candidate for C-45

**Variation axes selected**:
- V-01: Single axis — Gate 1 CLOSE structural independence: existing combined postcondition
  `[ ] Every Argued-Impossible cites architecture basis, not description absence` is split
  into two independent checkboxes. Targets C-43. C-42 PASS and C-44 FAIL carry from
  R13 V-01 baseline.
- V-02: Single axis — Gate 2b CLOSE structural independence: existing combined postcondition
  `[ ] Every TCR contains verbatim Gate 2 threshold expression (identity assertion satisfied
  — no paraphrase, no independent calibration)` is split into two independent checkboxes.
  Targets C-42. C-43 PASS and C-44 FAIL carry from R13 V-02 baseline.
- V-03: Combination — Gate 2b CLOSE split (C-42) + Gate 1 CLOSE split (C-43), both added
  while preserving the formal PART A + PART B GAP REGISTRY from R13 V-03 (C-44). Tests
  whether all three independence patterns coexist without structural interference.
- V-04: Single axis — Formal PART A + PART B GAP REGISTRY added to the bidirectional
  matrix. Preserves C-42 (two-checkbox Gate 2b CLOSE) + C-43 (two-checkbox Gate 1 CLOSE)
  from R13 V-04. Targets C-44. Expected to reach 72/72.
- V-05: Full integration + new structural property — Recovery Stage VS Cross-Reference
  Registry added as Act 1 Terminal artifact. For every named Verification Signal (VS) across
  all recovery path stages in Gate 2, registers three fields: VS ID / Stage Context /
  Observation Assertion. Orthogonal to C-35 (which requires VS to be present in the row);
  this criterion requires each VS to be independently assertion-ready in a cross-stage
  registry. Candidate for C-45.

**Expected R15 discrimination under v14:**

| Rank | Variation | C-42 | C-43 | C-44 | C-45 (cand.) | Uncapped |
|------|-----------|------|------|------|--------------|---------|
| 1 | V-05 | PASS | PASS | PASS | PASS | 72/72 + C-45 |
| 2 (tie) | V-03 | PASS | PASS | PASS | FAIL | 72/72 |
| 2 (tie) | V-04 | PASS | PASS | PASS | FAIL | 72/72 |
| 4 | V-01 | PASS | PASS | FAIL | FAIL | 70/72 |
| 5 | V-02 | PASS | PASS | FAIL | FAIL | 70/72 |

V-01 and V-02 tie on C-42/C-43/C-44; they differ in construction path (Gate 1 axis vs Gate
2b axis) and will be separated by v15 criteria if a new Gate-level structural independence
axis is extracted. Open for R16: C-44 PASS for V-01/V-02 (inline gap findings in both);
C-45 PASS for V-03/V-04 (no VS Registry in either). No fully uncracked criteria remain
under v14 after R15 if V-03 and V-04 achieve 72/72.

---

## V-01

**Variation axis**: Lifecycle emphasis — Gate 1 CLOSE's combined impossibility-argument
postcondition is split into two independent, separately-checkboxed items. The R13 V-01
form: `[ ] Every Argued-Impossible has DS Primitive cited: field completed (architecture
basis, not description absence)` — one checkbox verifying two independent conditions
(required basis present AND prohibited basis absent). V-01 makes them two checkboxes:
(1) required-basis check: every Argued-Impossible cites an architecture basis; (2)
prohibited-basis check: no Argued-Impossible uses description absence as its basis. The
Gate 2b CLOSE two-checkbox structure (C-42 PASS baseline from R13 V-01) is retained
unchanged. No formal gap registry (C-44 FAIL maintained to isolate the C-43 axis).

**Hypothesis**: C-43 FAIL in R13 V-01 because the combined Gate 1 CLOSE postcondition
`(architecture basis, not description absence)` places both conditions in a parenthetical
within a single checkbox. When a model confirms "DS Primitive cited: field completed," the
parenthetical is treated as an elaboration of the same confirmation, not as a second
independent check. The structural ambiguity means a Gate 1 CLOSE with a valid architecture
basis will pass the combined check even if description-absence language is also present,
because the positive confirmation dominates. Splitting into two checkboxes makes the
prohibition independently load-bearing: a Gate 1 CLOSE can fail the prohibition check while
passing the required-basis check, which the combined form cannot express.

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

```
SCOPE DECLARATION
Operations in scope: [list each — minimum four from: checkout, inventory reservation,
payment processing, order fulfillment, cart state, loyalty redemption, return/refund]
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
Scope: Gates 1-4 + Gate 2b + Act 1 Registry Audit + Nil Supersession Log +
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
  [ ] Impossibility argument basis confirmed: every Argued-Impossible cites an
      architecture basis (CAP theorem guarantee, synchrony constraint, or topology
      bound that architecturally forecloses the failure class) — required basis: present
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

**Section gate**: All scenario rows complete before Gap Identification.

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

Consequence context: [payment idempotency miss / loyalty double-redemption under split-brain
/ order state divergence]. Chronic: reconciliation backlog / without ceiling / dispute-count
accumulates.

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
| `Trigger Condition Reference` | DS Expert | **Identity assertion**: the chaos activation boundary expression IS the Trigger Condition threshold expression from Gate 2 for this scenario — identical, not a derivative or approximation. Transcribe the exact threshold expression string verbatim from the Gate 2 Trigger Condition column. Do not paraphrase, abbreviate, or add conditions not present in Gate 2. Any modification between Gate 2 and Gate 2b produces an uncalibrated chaos test. |
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

BYPASS-TRIGGER non-empty for any rule -> invoke bypass gate-reopening protocol before
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

**Part A — Forward Direction: Chaos Scenario -> Observable Signal**

For each chaos row in Gate 2b, identify the Observable Signal ID(s) from Gate 3 that will
confirm detection of that chaos scenario's fault in production.

| Gate 2b Row | Scenario ID | Observable Signal ID(s) Linked | Coverage Gap? |
|---|---|---|---|
| Row 1 | FS-01 | [OEG-NN / DCV-NN / MRF-NN] | No / CHAOS-OBS-GAP-NN |

**Dark chaos finding**: A chaos row with no Observable Signal linkage = "dark chaos" —
the fault fires but cannot be confirmed as detected in production. Emit:
`CHAOS-OBS-GAP-NN | Chaos row [N] / [Scenario ID] | no Observable Signal linked | consequence: pass/fail result unverifiable in production without monitoring confirmation`

**Part B — Reverse Direction: Observable Signal -> Chaos Scenario**

For each Observable Signal entry in Gate 3 (across OEG, DCV, MRF tables), identify the
Gate 2b chaos row(s) that exercise the fault conditions monitored by that signal.

| Gate 3 Finding ID | Signal Name | Chaos Scenario ID(s) Linked | Coverage Gap? |
|---|---|---|---|
| OEG-01 | [named signal from Gate 3] | [FS-NN] | No / OBS-CHAOS-GAP-NN |

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

**Variation axis**: Output format — Gate 2b CLOSE's combined identity assertion is split
into two independent, separately-checkboxed items. The R13 V-02 form: one combined checkbox
`[ ] Every Trigger Condition Reference contains verbatim Gate 2 threshold expression
(identity assertion satisfied — no paraphrase, no independent calibration)` verifies two
independent conditions together. V-02 makes them two checkboxes: (1) identity assertion
confirmed: every TCR contains the verbatim Gate 2 threshold expression — identical string,
not a paraphrase; (2) prohibition clause confirmed: no TCR contains a paraphrased or
independently calibrated expression — no paraphrase, no independent calibration. The Gate 1
CLOSE two-checkbox structure (C-43 PASS baseline from R13 V-02) is retained unchanged.
No formal gap registry (C-44 FAIL maintained to isolate the C-42 axis).

**Hypothesis**: C-42 FAIL in R13 V-02 because the combined postcondition places both
conditions in a parenthetical appended to the positive confirmation. A model confirming
"verbatim threshold expression present" treats the no-paraphrase condition as co-satisfied.
Splitting into two checkboxes makes the prohibition independently load-bearing: a Gate 2b
CLOSE can fail the prohibition check while passing the identity confirmation, which the
combined form cannot express. This mirrors the structural independence that Gate 1 CLOSE
(C-43) already applies to impossibility arguments — C-42 applies the same pattern to the
chaos test calibration gate.

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

1. Bypass Owner emits: `GATE N-bypass: REOPENED -- [rule ID] -- bypass at [gate, entry ID]`
2. Bypass Owner applies the rule and produces required output.
3. Bypass Owner emits: `GATE N-bypass: AMENDED -- CLOSED -- [rule now applied]`
4. Bypass Owner updates the audit row: Status -> INVOKED; BYPASS-TRIGGER ->
   "RESOLVED -- [sub-gate]"; Citations += sub-gate.

**COMPLETE may not be declared** while any RULE-BYPASSED entry remains unresolved in any act.

---

### ANTI-OMISSION ARCHITECTURE

| Level | Anti-Omission Mechanism | Omission Risk Targeted | Mechanism Location |
|---|---|---|---|
| Table | Unified row index (`#`) + anti-split instruction | Row fragmentation across ownership transitions | `#` column; anti-split in Gate 2 |
| Section | Phase gate -- all rows complete before Gap Identification | Premature section advance | Section gate in Gate 2 |
| Slot | In-row bold imperative: **"Write this row now."** | Row omission under token pressure | Row Descriptors |
| Column-Group | Intra-row phase gate: C-phase complete before D-phase begins | Mid-row D-phase omission on ownership shift | Row Descriptors: Column-Group Gate |
| Column | Column ownership per header in Column Contract | Individual column omission | Column Contract |

**Anti-split instruction**: Single scenario table in Gate 2. No sub-tables or breaks between
rows when ownership shifts.

---

### COLUMN CONTRACT

Place this table before any scenario output.

| Column Name | Owner | Phase | Fill Requirement |
|---|---|---|---|
| `#` | Shared | -- | Sequential integer; no gaps |
| `ID` | Shared | -- | FS-NN format; unique per scenario |
| `Trigger Condition` | DS Expert | C-phase | Two required components: (1) threshold expression -- quantified activation condition; (2) detection signal -- named observable confirming threshold crossing. Threshold expression used verbatim in Gate 2b. |
| `State` | Commerce Expert | C-phase | Specific system configuration; named components and states |
| `Capability` | Commerce Expert | C-phase | Named commerce operations the user can still complete |
| `Data at Risk` | DS Expert | D-phase | Named data type + consistency failure mode |
| `Recovery Path` | DS Expert | D-phase | Four stages each with mechanism (named actor), SLA target, VS (named observable confirming stage completion, distinct from mechanism). Format: Detect / Contain / Recover / Validate each with mech, actor, SLA, VS. |
| `Severity` | DS Expert | D-phase | `degraded` / `impaired` / `down` |
| `Blast Radius` | DS Expert | D-phase | Fraction or named segment |
| `Rule Applied` | DS Expert | D-phase | Rule ID or `--` |

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
| Network partition / offline | 2 | [required if slot unfillable] |
| Partial service failure | 2 | |
| Eventual consistency | 2 | |

---

ACT 1 OPEN -- Distributed Systems Expert
Scope: Gates 1-4 + Gate 2b + Act 1 Registry Audit + Nil Supersession Log +
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

**Argued-Impossible template** -- complete this block for every Argued-Impossible row:

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
  [Fails: description-absence argument. Absence from description does not prove absence
   architecturally. Cite what the architecture guarantees, not what the description omits.]

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
      bound) -- required basis: present
  [ ] Impossibility argument prohibition confirmed: no Argued-Impossible argument is
      based on description absence ("the topic does not mention X") -- prohibited
      basis: absent
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

Consequence context: [acute consequences per resolution branch]. Chronic if never addressed:
[rate] / [horizon] / [metric accumulates].

**Write this row now.**
Fill Trigger Condition: (1) threshold expression; (2) detection signal. Threshold verbatim
in Gate 2b.
C-phase (Commerce Expert): State + Capability.
**C-phase complete check before D-phase.**
D-phase (DS Expert): Data at Risk, Recovery Path (four stages with mechanism, SLA, named
VS), Severity, Blast Radius, Rule Applied.
**Do not advance to Row 2 until all columns non-placeholder.**

---

**Row 2 -- FS-02: [Scenario Name]**

**Write this row now.** Fill all columns per Column Contract.
**C-phase complete check before D-phase. Do not advance to Row 3 until non-placeholder.**

---

Continue this pattern for all remaining Include scenarios.

Scenario table:

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
| `#` | Shared | Sequential integer; no gaps |
| `Scenario ID` | Shared | FS-NN; one row per Include scenario |
| `Trigger Condition Reference` | DS Expert | Identity assertion: chaos activation boundary = Gate 2 threshold expression verbatim -- identical, not a derivative. Transcribe exact threshold expression. Do not paraphrase. |
| `Inject` | DS Expert | [fault type]: [named mechanism] -- [parameter]. Generic descriptions fail. |
| `Expected Observable` | DS Expert | In-fault system behavior at named observation granularity |
| `Pass-Fail Signal` | DS Expert | Binary artifact naming specific metric, response code, log entry, or system state |

GATE 2b OPEN
Preconditions:
  [ ] Gate 2 STATUS: CLOSED
  [ ] Include scenario list from Gate 1 available
  [ ] Identity assertion acknowledged: chaos activation boundary = Gate 2 threshold
      expression for each scenario, verbatim -- not a derivative
Entry confirmed: [yes / no]

| # | Scenario ID | Trigger Condition Reference | Inject | Expected Observable | Pass-Fail Signal |
|---|---|---|---|---|---|
| 1 | FS-01 | [verbatim threshold expression from Gate 2 FS-01] | | | |

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
(2) detection horizon (concrete time window, not "promptly"); (3) rationale sentence.

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

### Act 1 Terminal: Bidirectional Chaos-Observability Coverage Matrix

**Part A -- Forward Direction: Chaos Scenario -> Observable Signal**

| Gate 2b Row | Scenario ID | Observable Signal ID(s) Linked | Coverage Gap? |
|---|---|---|---|
| Row 1 | FS-01 | [OEG-NN / DCV-NN / MRF-NN] | No / CHAOS-OBS-GAP-NN |

Dark chaos finding: emit CHAOS-OBS-GAP-NN for each chaos row with no Observable Signal
linkage. Format: CHAOS-OBS-GAP-NN | Chaos row [N] / [Scenario ID] | no Observable Signal
linked | consequence: pass/fail result unverifiable in production

**Part B -- Reverse Direction: Observable Signal -> Chaos Scenario**

| Gate 3 Finding ID | Signal Name | Chaos Scenario ID(s) Linked | Coverage Gap? |
|---|---|---|---|
| OEG-01 | [named signal] | [FS-NN] | No / OBS-CHAOS-GAP-NN |

Unvalidated signal finding: emit OBS-CHAOS-GAP-NN for each Observable Signal with no chaos
scenario linkage. Format: OBS-CHAOS-GAP-NN | [Gate 3 finding ID] | [signal name] | no
chaos scenario linked | consequence: signal behavior under fault untested

Matrix summary:
Forward coverage: [N] of [M] chaos rows have linked Observable Signals.
Reverse coverage: [N] of [M] Observable Signals have linked chaos scenarios.
Dark chaos gaps: [CHAOS-OBS-GAP-NN list / none]
Unvalidated signal gaps: [OBS-CHAOS-GAP-NN list / none]

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

Per-finding carrying cost: For each named gap (OEG-NN, DCV-NN, MRF-NN): failure mode,
rate, horizon, metric.

Overall synthesis:
Urgency: HIGH / MEDIUM / LOW
Highest-risk finding: [gap ID] -- [carrying cost]
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

---

---

## V-03

**Variation axis**: Combination -- Gate 2b CLOSE structural independence (C-42) + Gate 1
CLOSE structural independence (C-43), both added while preserving the formal PART A + PART
B GAP REGISTRY from R13 V-03 (C-44). R13 V-03 had C-44 PASS but C-42 FAIL and C-43 FAIL.
V-03 applies the two-checkbox split to both gates simultaneously, testing whether C-42 and
C-43 coexist with C-44 without structural interference.

**Hypothesis**: C-42 and C-43 are orthogonal to C-44 -- the two-checkbox independence
pattern in Gate CLOSE blocks does not interact with the formal registry structure in the
bidirectional matrix. If V-03 achieves 72/72, all three structural independence patterns
(C-42, C-43, C-44) are independently composable. If V-03 scores lower than expected, the
interference hypothesis indicates one of the independence patterns constrains another --
e.g., the formal registry may require the bidirectional matrix precondition structure to
change, which might conflict with a Gate CLOSE form.

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
| Table | Unified row index + anti-split instruction | Row fragmentation across ownership transitions | # column; anti-split in Gate 2 |
| Section | Phase gate -- all rows complete before Gap Identification | Premature section advance | Section gate in Gate 2 |
| Slot | In-row bold imperative: Write this row now. | Row omission under token pressure | Row Descriptors |
| Column-Group | Intra-row phase gate: C-phase complete before D-phase begins | Mid-row D-phase omission on ownership shift | Row Descriptors |
| Column | Column ownership per header in Column Contract | Individual column omission | Column Contract |

**Anti-split instruction**: Single scenario table in Gate 2. No sub-tables or breaks.

---

### COLUMN CONTRACT

| Column Name | Owner | Phase | Fill Requirement |
|---|---|---|---|
| # | Shared | -- | Sequential integer; no gaps |
| ID | Shared | -- | FS-NN format; unique per scenario |
| Trigger Condition | DS Expert | C-phase | Two required components: (1) threshold expression -- quantified activation condition; (2) detection signal -- named observable confirming threshold crossing. Threshold used verbatim in Gate 2b. |
| State | Commerce Expert | C-phase | Specific system configuration; named components and states |
| Capability | Commerce Expert | C-phase | Named commerce operations still completable |
| Data at Risk | DS Expert | D-phase | Named data type + consistency failure mode |
| Recovery Path | DS Expert | D-phase | Four stages each with mechanism (named actor), SLA target, VS (named observable confirming stage completion, distinct from mechanism). Format: Detect / Contain / Recover / Validate each with mech, actor, SLA, VS. |
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
| Network partition / offline | 2 | [required if slot unfillable] |
| Partial service failure | 2 | |
| Eventual consistency | 2 | |

---

ACT 1 OPEN -- Distributed Systems Expert
Scope: Gates 1-4 + Gate 2b + Act 1 Registry Audit + Nil Supersession Log +
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
  [Fails: description-absence argument, not an architecture constraint. Absence from
   description does not prove absence architecturally. Cite what the architecture
   guarantees, not what the description omits.]

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
      bound) -- required basis: present
  [ ] Impossibility argument prohibition confirmed: no Argued-Impossible argument is
      based on description absence ("the topic does not mention X") -- prohibited
      basis: absent
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

Consequence context: [acute consequences]. Chronic: [rate] / [horizon] / [metric].

**Write this row now.**
Fill Trigger Condition: (1) threshold expression; (2) detection signal. Threshold verbatim
in Gate 2b.
C-phase (Commerce Expert): State + Capability.
**C-phase complete check before D-phase.**
D-phase (DS Expert): Data at Risk, Recovery Path (four stages with mechanism, SLA, named
VS), Severity, Blast Radius, Rule Applied.
**Do not advance to Row 2 until all columns non-placeholder.**

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
| Trigger Condition Reference | DS Expert | Identity assertion: chaos activation boundary = Gate 2 threshold expression verbatim. Transcribe exact threshold expression. Do not paraphrase. |
| Inject | DS Expert | [fault type]: [named mechanism] -- [parameter]. Generic descriptions fail. |
| Expected Observable | DS Expert | In-fault system behavior at named observation granularity |
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
| 1 | FS-01 | [verbatim threshold expression from Gate 2 FS-01] | | | |

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
(2) detection horizon; (3) rationale sentence. Generic signals fail.

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

### Act 1 Terminal: Bidirectional Chaos-Observability Coverage Matrix

This matrix is a required Act 1 Terminal artifact. Absence is an Act 1 CLOSE blocker.

**Part A -- Forward Direction: Chaos Scenario -> Observable Signal**

| Gate 2b Row | Scenario ID | Observable Signal ID(s) Linked | Coverage Status |
|---|---|---|---|
| Row 1 | FS-01 | [OEG-NN / DCV-NN / MRF-NN] | Linked / DARK |

**PART A GAP REGISTRY -- Dark Chaos Findings**

For each DARK row, write one structured finding block:

GAP ENTRY FORMAT:
  CHAOS-OBS-GAP-NN
  Source: [Gate 2b Row N / Scenario ID FS-NN -- the chaos scenario with no signal linkage]
  Missing link: [no Observable Signal in Gate 3 monitors the fault injected by this scenario]
  Consequence: [the chaos test passes or fails with no production confirmation that the
    fault is detectable; dark chaos leaves unverified whether the monitoring signal for this
    fault class fires; test outcome cannot be operationally validated]

No dark chaos gaps: PART A GAP REGISTRY: none.

---

**Part B -- Reverse Direction: Observable Signal -> Chaos Scenario**

| Gate 3 Finding ID | Signal Name | Chaos Scenario ID(s) Linked | Coverage Status |
|---|---|---|---|
| OEG-01 | [named signal] | [FS-NN] | Linked / UNVALIDATED |

**PART B GAP REGISTRY -- Unvalidated Signal Findings**

For each UNVALIDATED row, write one structured finding block:

GAP ENTRY FORMAT:
  OBS-CHAOS-GAP-NN
  Source: [Gate 3 Finding ID / Signal Name -- the Observable Signal with no chaos scenario]
  Missing link: [no Gate 2b row injects the fault condition monitored by this signal]
  Consequence: [the signal specification has not been validated under controlled fault
    conditions; cannot confirm the signal fires as specified; production behavior under
    this failure class unconfirmed]

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

Per-finding carrying cost: For each named gap (OEG-NN, DCV-NN, MRF-NN): failure mode,
rate, horizon, metric.

Overall synthesis:
Urgency: HIGH / MEDIUM / LOW
Highest-risk finding: [gap ID] -- [carrying cost]
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

---

---

## V-04

**Variation axis**: Lifecycle emphasis -- Formal PART A + PART B GAP REGISTRY added to the
Bidirectional Chaos-Observability Coverage Matrix. R13 V-04 had C-42 PASS (two-checkbox
Gate 2b CLOSE) + C-43 PASS (two-checkbox Gate 1 CLOSE) but C-44 FAIL (inline gap
findings). V-04 retains both Gate CLOSE two-checkbox structures from R13 V-04 and adds the
formal three-field registry (Source / Missing link / Consequence) for both dark chaos
findings (Part A) and unvalidated signal findings (Part B). Tests whether C-44 composes
cleanly with C-42 + C-43 from the opposite construction path from V-03 (V-03 starts from
C-44 and adds C-42+C-43; V-04 starts from C-42+C-43 and adds C-44).

**Hypothesis**: C-44 FAIL in R13 V-04 because inline gap findings name the problem but not
the consequence. "CHAOS-OBS-GAP-NN: CS-03 has no linked Observable Signal -> dark chaos
scenario" identifies the gap but a reviewer scanning for risk priority must read surrounding
prose to understand the consequence. The formal registry adds a Consequence field that is
independently readable per entry, enabling registry-level queries. The construction path
distinction from V-03 (starting from C-42+C-43 vs starting from C-44) tests whether the
formal registry language integrates naturally into V-04's existing prompt structure or
introduces awkward redundancy.

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

**Anti-split instruction**: Single scenario table in Gate 2. No sub-tables or breaks.

---

### COLUMN CONTRACT

| Column Name | Owner | Phase | Fill Requirement |
|---|---|---|---|
| # | Shared | -- | Sequential integer; no gaps |
| ID | Shared | -- | FS-NN format; unique per scenario |
| Trigger Condition | DS Expert | C-phase | Two required components: (1) threshold expression -- quantified activation condition; (2) detection signal -- named observable confirming threshold crossing. Threshold expression used verbatim in Gate 2b (identity assertion). |
| State | Commerce Expert | C-phase | Specific system configuration; named components and states |
| Capability | Commerce Expert | C-phase | Named commerce operations still completable |
| Data at Risk | DS Expert | D-phase | Named data type + consistency failure mode |
| Recovery Path | DS Expert | D-phase | Four stages each with mechanism (named actor), SLA target, VS (named observable confirming stage completion, distinct from mechanism). Format: Detect / Contain / Recover / Validate each with mech, actor, SLA, VS. |
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
  [Fails: description-absence argument. Absence from description does not prove absence
   architecturally. Cite the architecture guarantee, not the description gap.]

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
Fill Trigger Condition: (1) threshold expression naming the quantified activation condition;
(2) detection signal naming the observable mechanism confirming threshold crossing.
Threshold expression will be transcribed verbatim into Gate 2b.
C-phase (Commerce Expert): State + Capability.
**C-phase complete check: do not begin D-phase until Trigger Condition, State, Capability
are non-placeholder.**
D-phase (DS Expert): Data at Risk, Recovery Path (four stages: mechanism, actor, SLA, VS),
Severity, Blast Radius, Rule Applied.
**Do not advance to Row 2 until all columns non-placeholder.**

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
| Trigger Condition Reference | DS Expert | Identity assertion: the chaos activation boundary expression IS the Trigger Condition threshold expression from Gate 2 -- identical, not a derivative. Transcribe verbatim. Do not paraphrase or add conditions. |
| Inject | DS Expert | [fault type]: [named mechanism] -- [parameter]. Generic descriptions fail. |
| Expected Observable | DS Expert | In-fault system behavior at named observation granularity |
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

### Act 1 Terminal: Bidirectional Chaos-Observability Coverage Matrix

This matrix is a required Act 1 Terminal artifact. It verifies that every chaos scenario is
linked to at least one Observable Signal (forward direction) and every Observable Signal is
linked to at least one chaos scenario (reverse direction). Absence is an Act 1 CLOSE blocker.

**Part A -- Forward Direction: Chaos Scenario -> Observable Signal**

For each chaos row in Gate 2b, identify the Observable Signal ID(s) from Gate 3 that will
confirm detection of that chaos scenario's fault in production.

| Gate 2b Row | Scenario ID | Observable Signal ID(s) Linked | Coverage Status |
|---|---|---|---|
| Row 1 | FS-01 | [OEG-NN / DCV-NN / MRF-NN] | Linked / DARK |

**PART A GAP REGISTRY -- Dark Chaos Findings**

For each DARK row, write one structured finding block with all three required fields:

  CHAOS-OBS-GAP-NN
  Source: [Gate 2b Row N / Scenario ID FS-NN -- the chaos scenario with no Observable
    Signal linkage in Gate 3]
  Missing link: [no Observable Signal in Gate 3 monitors the fault class injected by this
    chaos row; name the specific fault class and why no signal covers it]
  Consequence: [the chaos test result -- pass or fail -- cannot be confirmed as
    operationally meaningful; production fault detection for this fault class is unverified;
    test outcome is not predictive of production monitoring behavior]

No dark chaos gaps: PART A GAP REGISTRY: none.

---

**Part B -- Reverse Direction: Observable Signal -> Chaos Scenario**

For each Observable Signal entry in Gate 3, identify the Gate 2b chaos row(s) that exercise
the fault conditions monitored by that signal.

| Gate 3 Finding ID | Signal Name | Chaos Scenario ID(s) Linked | Coverage Status |
|---|---|---|---|
| OEG-01 | [named signal] | [FS-NN] | Linked / UNVALIDATED |

**PART B GAP REGISTRY -- Unvalidated Signal Findings**

For each UNVALIDATED row, write one structured finding block with all three required fields:

  OBS-CHAOS-GAP-NN
  Source: [Gate 3 Finding ID / Signal Name -- the Observable Signal with no Gate 2b linkage]
  Missing link: [no Gate 2b chaos row injects the specific fault condition monitored by this
    signal; name the fault condition and why no chaos row exercises it]
  Consequence: [the Observable Signal has not been validated under controlled fault
    injection; production behavior of this signal under its target fault class is untested;
    cannot confirm the signal fires as specified when the fault occurs]

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

---

---

## V-05

**Variation axis**: Full integration + new structural property -- All C-42/C-43/C-44
patterns maintained from R13 V-05 (72/72 baseline) plus a new Act 1 Terminal artifact:
the **Recovery Stage VS Cross-Reference Registry**. For every named Verification Signal
(VS) across all Recovery Path stages in Gate 2, one registry entry is required with three
fields: (1) VS ID (VS-NN sequential); (2) Stage Context (scenario ID + recovery stage
name); (3) Observation Assertion (the specific observable that confirms stage completion,
stated as a testable binary condition independent of the stage mechanism). This registry
is a candidate for C-45.

**Hypothesis**: C-35 requires each recovery stage to have a named VS that is observable
and distinct from the mechanism -- presence check at row level. The VS Cross-Reference
Registry is orthogonal to C-35: C-35 requires the VS to exist in the scenario row; the
registry requires each VS to be independently assertion-ready without traversing the full
row. A reviewer confirming recovery completeness currently must scan every row and every
stage column to find all VS entries. The registry surfaces all VS entries in a single
auditable artifact with independently confirmable assertion statements. The registry also
enables a new gap class: a VS entry in the registry whose Observation Assertion cannot be
written as a binary testable condition is a VS quality gap independent of the VS being
present in the row. If V-05 introduces this registry and R15 scoring confirms it is not
already covered by C-35, it becomes a candidate for C-45 in the v15 rubric.

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
