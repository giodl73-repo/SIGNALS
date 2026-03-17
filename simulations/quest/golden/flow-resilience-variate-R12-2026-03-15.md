# Flow-Resilience Skill — Round 12 Variations (Rubric v12)

**Skill**: flow-resilience — Simulate degraded conditions: offline, partial failure, eventual
consistency.
**Rubric**: v12 (C-01 through C-38, essential/recommended/aspirational tiers)
**Date**: 2026-03-15

---

## Round 12 Context

**New criteria entering R12**: none — all three criteria added in v12 (C-36, C-37, C-38)
were extracted from R11 excellence signals.

**Persistent uncracked**: C-15 PASS (inline VALID/INVALID examples absent in all rounds).

**R11 ceiling under v12**: V-05 at 59/60 uncapped aspirational. C-36 PASS and C-38 PASS
are V-05 only. C-37 PASS cracked by V-04 and V-05. C-15 remains uncracked by all.

**R12 targets**:
- Crack C-15 — DS-Primitive-Grounded Impossibility Arguments with inline VALID/INVALID
  annotated examples in the Argued-Impossible template
- Spread C-36 PASS to more than V-05 only — explicit identity assertion in Gate 2b column
  contract (identity claim, not reference link)
- Spread C-38 PASS to more than V-05 only — bidirectional matrix with gap findings emitted
  for both directions

**Variation axes selected**:
- V-01: Single axis — Lifecycle emphasis: Gate 1 Argued-Impossible template extended with
  named "DS Primitive cited:" field and inline VALID/INVALID annotated examples (targets C-15)
- V-02: Single axis — Output format: Gate 2b Column Contract added with explicit identity
  assertion for Trigger Condition Reference (targets C-36 PASS form)
- V-03: Single axis — Output format: Chaos-Observability Coverage Matrix restructured as
  explicit bidirectional artifact with CHAOS-OBS-GAP-NN and OBS-CHAOS-GAP-NN gap findings
  (targets C-38 PASS form)
- V-04: Combination — Gate 2b Column Contract identity assertion + bidirectional matrix
  (C-36 + C-38 combined from V-02 + V-03)
- V-05: Full integration — DS Primitive VALID/INVALID (V-01) + Gate 2b identity assertion
  (V-02) + bidirectional matrix (V-03), targeting C-15 + C-36 + C-38 simultaneously

---

## V-01

**Variation axis**: Lifecycle emphasis — Gate 1's Argued-Impossible disposition is extended
with a structured template. The template contains three named fields: (1) **DS Primitive
cited** — the specific CAP theorem guarantee, synchrony guarantee, or topology constraint
that architecturally forecloses the failure class; (2) inline VALID annotated example
showing an architecture-basis argument; (3) inline INVALID annotated example showing a
topic-scope argument that fails. The template is placed immediately after the
Argued-Impossible row in the Gate 1 discovery table. The Coverage Accountability Roster DS
Primitive column is extended from a placeholder to a required reference to the DS Primitive
cited in the corresponding Argued-Impossible template.

**Hypothesis**: C-15 is persistently uncracked because the current Gate 1 structure
discourages topic-scope arguments in prose ("Topic does not mention X is not a DS
Primitive") but does not supply a template that forces architecture-basis arguments by
structure. Naming `DS Primitive cited:` as a required field — with inline VALID/INVALID
examples inside the template — converts the distinction from advisory to structural: a
row that names "the topic doesn't mention this" in the DS Primitive field is a template
violation visible at the field level. The VALID/INVALID examples also serve as an
inline scoring key so the model can self-evaluate each Argued-Impossible instance against
the criterion before Gate 1 CLOSE.

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
| `Trigger Condition` | DS Expert | C-phase | **Two required components**: (1) threshold expression — quantified activation condition (e.g., "inventory count falls below safety-stock threshold", "payment API p99 latency > 500ms"); (2) detection signal — named observable mechanism confirming threshold crossing (e.g., "inventory-service health probe returns degraded", "payment-provider timeout counter exceeds N/window"). The threshold expression is also used verbatim as the activation condition in Gate 2b. Qualitative descriptions without threshold expression fail. |
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
  [ ] Every BARRED has CG-NN; every Argued-Impossible cites DS Primitive by name
  [ ] Every Argued-Impossible has DS Primitive cited: field completed (architecture basis,
      not description absence)
  [ ] Roster counts updated; DS Primitive column populated for any impossibility slot
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
SLA target | VS — VS is named observable confirming stage completion, distinct from
mechanism), Severity, Blast Radius, Rule Applied.
**Do not advance to Row 2 until all columns including both Trigger Condition components and
all four VS entries are non-placeholder.**

---

**Row 2 — FS-02: [Scenario Name]**

Consequence context: [payment idempotency miss → double-charge; loyalty double-redemption
under split-brain; order state divergence under partial fulfillment]. Chronic: reconciliation
backlog / without ceiling / dispute-count accumulates.

**Write this row now.**
Fill Trigger Condition (threshold expression + detection signal). Fill all columns per
Column Contract including all four Recovery Path stages with mechanism, SLA target, named VS.
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
  granularity. In-fault behavior, not post-recovery state.

- **Pass-Fail Signal**: the binary artifact that terminates the test with a named outcome.
  Must name a specific metric value, API response code, log entry, or system state.

If any Include scenario lacks a chaos row at Gate 2b CLOSE — invoke RULE-CHAOS-INJECT
bypass before closing Gate 2b.

| # | Scenario ID | Trigger Condition Reference | Inject | Expected Observable | Pass-Fail Signal |
|---|---|---|---|---|---|
| 1 | FS-01 | [threshold from Gate 2 FS-01 Trigger Condition] | | | |

```
GATE 2b CLOSE
Exit postconditions:
  [ ] One chaos row per Include scenario; no scenarios missing
  [ ] Every row has Trigger Condition Reference citing Gate 2 threshold expression
  [ ] Every row has Inject with named fault type, mechanism, parameter (not generic)
  [ ] Every row has Expected Observable at named in-fault granularity
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
trace attribute, or alert condition; (2) detection horizon — estimated time from gap onset
to signal firing (concrete time window required; "promptly" fails); (3) rationale sentence —
why this signal surfaces the gap before user impact. Generic signals ("add monitoring") fail.
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

**Variation axis**: Output format — A dedicated Gate 2b Column Contract is added immediately
before the Gate 2b instruction block. The column contract defines fill requirements for all
five Gate 2b columns. The `Trigger Condition Reference` column carries an explicit **identity
assertion** in its fill requirement: the chaos activation boundary expression IS the same
threshold expression as the Gate 2 Trigger Condition column value — identical by definition,
not linked by reference. The identity claim uses the word "identical" and forecloses
paraphrase, approximation, or independent calibration. The precondition block for Gate 2b
is extended with a new check: `[ ] Identity assertion acknowledged: chaos activation
boundary = Gate 2 threshold expression, not a derivative`. Everything else (rule registry,
bypass chain, Gate 3 observable signal with detection horizon, coverage matrix) is identical
to V-01's baseline.

**Hypothesis**: C-36 remains PARTIAL in V-01 through V-04 of R11 because none of them
contain an identity assertion in a named structural location — they reference the Trigger
Condition threshold but do not assert that the chaos boundary IS that expression. The
rubric PASS condition requires the identity claim to appear "in the template structure, not
only in a row-level example." Adding a formal Gate 2b Column Contract with `Fill
Requirement: Identity assertion — the chaos activation boundary expression IS the Trigger
Condition threshold expression from Gate 2` places the claim at the template level. The
precondition acknowledgement forces the model to confirm it before writing chaos rows,
converting the identity claim from prose guidance into a gate entry condition.

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
| `Trigger Condition` | DS Expert | C-phase | **Two required components**: (1) threshold expression — quantified activation condition; (2) detection signal — named observable confirming threshold crossing. The threshold expression is also used verbatim in Gate 2b as the chaos activation boundary. Qualitative descriptions without threshold expression fail. |
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
| `#` | Shared | Sequential integer; matches chaos row number; no gaps |
| `Scenario ID` | Shared | FS-NN from Gate 1 Include list; one row per Include scenario |
| `Trigger Condition Reference` | DS Expert | **Identity assertion**: the chaos activation boundary expression IS the Trigger Condition threshold expression from Gate 2 for this scenario — identical, not a derivative or approximation. Transcribe the exact threshold expression string verbatim from the Gate 2 Trigger Condition column for this scenario ID. Do not paraphrase, abbreviate, or add conditions not present in Gate 2. Any modification to the expression between Gate 2 and Gate 2b produces an uncalibrated chaos test whose results are not directly predictive of production trigger behavior. The same logical expression that activates production monitoring activates this chaos test — they share the same boundary by assertion. |
| `Inject` | DS Expert | Named fault type + mechanism + parameter. Format: `[fault type]: [named mechanism] — [parameter]`. Generic descriptions ("make service unavailable") are not valid. |
| `Expected Observable` | DS Expert | In-fault system behavior at named observation granularity; not post-recovery state |
| `Pass-Fail Signal` | DS Expert | Binary artifact terminating the test with a named outcome; must name a specific metric value, API response code, log entry, or system state; generic outcomes ("system handles it") fail |

```
GATE 2b OPEN
Preconditions:
  [ ] Gate 2 STATUS: CLOSED
  [ ] Include scenario list from Gate 1 available (IDs: FS-01, FS-02, ...)
  [ ] Identity assertion acknowledged: chaos activation boundary = Gate 2 threshold
      expression for each scenario, verbatim — not a derivative
Entry confirmed: [yes / no]
```

For each Include scenario from Gate 1, write one row using the Gate 2b Column Contract
above. The Trigger Condition Reference must contain the verbatim threshold expression from
Gate 2 — the identity assertion in the column contract is the governing constraint.

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
  [ ] Every row has Inject (named type, mechanism, parameter)
  [ ] Every row has Expected Observable at named in-fault granularity
  [ ] Every row has Pass-Fail Signal naming specific binary artifact
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

**Observable Signal requirement**: Every named finding must carry three components:
(1) named signal (specific metric, log pattern, trace attribute, or alert condition);
(2) detection horizon (concrete time window — "within 30s of fault injection"; generic
language "promptly" fails);
(3) rationale sentence (why this signal surfaces the gap before user impact).
Generic signals ("add monitoring") fail. If no observable signal exists, invoke RULE-OBS-GAP
and emit MRF-OBS-NN.

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

```
GATE 4 OPEN / CLOSE
Exit postconditions:
  [ ] All recovery paths have minimum two actor-labeled steps
  [ ] Every superseded nil has SUPERSEDED annotation with finding ID
Gate 4 STATUS: CLOSED / OPEN — [reason if open]
```

| AMD ID | Entry ID | Original (summary) | Amended (summary) | Rule Invoked | Gate Re-Opened? |
|---|---|---|---|---|---|

No amendments: `Gate 4: no amendments required.`

---

### Act 1 Terminal: Post-Analysis Rule Registry Audit

| Rule ID | Invocations | Citations (gate, entry) | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-CR-DCV | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | |
| RULE-BARRED-CG | | | | |
| RULE-NIL-SUPERSEDE | | | | |
| RULE-CHAOS-INJECT | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | [empty or `GATE 2b-bypass: REOPEN`] |
| RULE-OBS-GAP | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | [empty or `GATE 3-bypass: REOPEN`] |

POST-ANALYSIS REGISTRY AUDIT (ACT 1) COMPLETE: [confirm no RULE-BYPASSED entries remain]

---

### Act 1 Terminal: Nil Supersession Log

No supersessions: `No supersessions in this run.`

---

### Act 1 Terminal: Chaos-Observability Coverage Matrix

| Scenario ID | Chaos Test Written? | Chaos Test Gate | Gap ID(s) Produced | Observable Signal Written? | Observable Signal Gate |
|---|---|---|---|---|---|
| FS-01 | Yes / No | Gate 2b row N | OEG-NN / DCV-NN / MRF-NN / none | Yes / No | Gate 3 row N |

Summary: `[N] of [M] scenarios have both chaos test and observable signal.`

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
    Gate 1: [CLOSED / OPEN]; Gate 1b: [CLOSED / N/A]
    Gate 2: [CLOSED / OPEN]; Gate 2b: [CLOSED / OPEN]
    Gate 3: [CLOSED / OPEN]; Gate 4: [CLOSED / OPEN]
    GATE N-bypass blocks: [CLOSED / none triggered]
    Act 1 Registry Audit: [CLOSED / OPEN]
    Chaos-Observability Matrix: [COMPLETE / OPEN]
(2) Act 1 scope exhausted: [yes / list unresolved]
(3) No RULE-BYPASSED conditions remain unresolved: [yes / exception]
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
| FS-01 | Yes / No | | — / CV-DCV-01 / CV-OEG-01 / CV-MRF-01 |

Commerce-domain targets: inventory oversell / payment idempotency / loyalty
double-redemption / order state divergence — each: [present / absent — rationale].

```
GATE 5 CLOSE
Exit postconditions:
  [ ] Every scenario anchored; all RULE-COMMERCE-ANCHOR invocations recorded
  [ ] All four commerce-domain targets checked
Gate 5 STATUS: CLOSED / OPEN
```

### Act 2 Terminal: Post-Analysis Rule Registry Audit

| Rule ID | Invocations | Citations | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-COMMERCE-ANCHOR | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | |

POST-ANALYSIS REGISTRY AUDIT (ACT 2) COMPLETE

### Inertia Synthesis

**Per-finding**: failure mode, rate, horizon, metric — one entry per named gap.
Urgency: HIGH / MEDIUM / LOW
Highest-risk: [gap ID] — [carrying cost]
Status-quo: [specific to `{topic}`]
Intervention: [owner + threshold + consequence]

```
ACT 2 CLOSE (sign-off)
(1) Gate 5 / bypass blocks / Registry Audit: all CLOSED
(2) Act 2 scope exhausted: yes
(3) No RULE-BYPASSED conditions remain: yes / exception
ACT 2 STATUS: CLOSED / OPEN
```

ANALYSIS COMPLETE (declared only when ACT 1 STATUS: CLOSED AND ACT 2 STATUS: CLOSED)

---

---

## V-03

**Variation axis**: Output format — The Chaos-Observability Coverage Matrix in Act 1
Terminal is replaced with a **Bidirectional Chaos-Observability Coverage Matrix** that
explicitly verifies coverage in both directions: (A) Forward — each chaos scenario (by
Gate 2b row ID) links to one or more Observable Signal IDs from Gate 3; (B) Reverse —
each Observable Signal (by Gate 3 finding ID) links back to one or more chaos scenario IDs
from Gate 2b. Gap findings are emitted by the matrix itself: a chaos row with no Observable
Signal linkage emits CHAOS-OBS-GAP-NN ("dark chaos" — fires but cannot be confirmed); an
Observable Signal with no chaos scenario linkage emits OBS-CHAOS-GAP-NN ("unvalidated
signal" — never exercised by chaos harness). The matrix is named as a required Act 1
Terminal artifact in the ACT 1 OPEN scope declaration and in the ACT 1 CLOSE sign-off.
Everything else (rule registry, Gate 2b column structure, Gate 3 observable signal with
detection horizon) is identical to V-02's baseline.

**Hypothesis**: R11 V-05's coverage matrix verified scenario-level coverage (each scenario
→ chaos test + observable signal) but did not verify bidirectional ID linkage between
specific chaos rows and specific Observable Signal entries. The rubric's C-38 PASS condition
requires that "each chaos scenario [is listed] by ID alongside its linked Observable
Signal(s) by ID, and each Observable Signal [is listed] by ID alongside its linked chaos
scenario(s) by ID." The R11 V-05 matrix covered the scenario → gap category direction but
not the explicit chaos-row → signal-ID and signal-ID → chaos-row cross-reference. Making
the two directions explicit in separate table sections, with gap findings emitted when a
cell is empty in either direction, produces the bidirectional linkage that C-38 requires
and also identifies the two distinct failure modes: dark chaos (chaos without observability
confirmation) and unvalidated signals (observability without chaos exercise).

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

**Bypass Owner column**: Cross-act invocation not permitted.

---

### BYPASS GATE-REOPENING PROTOCOL

When any rule shows RULE-BYPASSED in the Post-Analysis Rule Registry Audit:

1. Bypass Owner emits: `GATE N-bypass: REOPENED — [rule ID] — bypass at [gate, entry ID]`
2. Bypass Owner applies the rule and produces required output.
3. Bypass Owner emits: `GATE N-bypass: AMENDED — CLOSED — [rule now applied]`
4. Bypass Owner updates the audit row: Status → INVOKED; BYPASS-TRIGGER → "RESOLVED".

**COMPLETE may not be declared** while any RULE-BYPASSED entry remains unresolved.

---

### ANTI-OMISSION ARCHITECTURE

| Level | Anti-Omission Mechanism | Omission Risk Targeted | Mechanism Location |
|---|---|---|---|
| Table | Unified row index + anti-split instruction | Row fragmentation | `#` column; Gate 2 |
| Section | Phase gate — all rows complete before Gap Identification | Premature advance | Gate 2 |
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
| `Recovery Path` | DS Expert | D-phase | Four stages: Detect / Contain / Recover / Validate — each with mechanism \| actor \| SLA \| VS (named observable, distinct from mechanism) |
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

**Row 1 — FS-01:** Consequence context. **Write this row now.** Fill Trigger Condition
(threshold + detection signal). C-phase then D-phase. **Do not advance to Row 2 until
non-placeholder in all columns including all four VS entries.**

**Row 2 — FS-02:** **Write this row now.** Fill all columns per Column Contract.
**C-phase check before D-phase. Do not advance to Row 3 until non-placeholder.**

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

```
GATE 2b OPEN
Preconditions:
  [ ] Gate 2 STATUS: CLOSED; Include scenario IDs available
Entry confirmed: [yes / no]
```

For each Include scenario, write one row. Required fields:
- **Trigger Condition Reference**: copy threshold expression from Gate 2 (same boundary as
  monitoring spec; do not invent separate activation condition)
- **Inject**: `[fault type]: [mechanism] — [parameter]` (not generic)
- **Expected Observable**: in-fault behavior at named observation granularity
- **Pass-Fail Signal**: binary artifact naming specific metric/code/log/state

| # | Scenario ID | Trigger Condition Reference | Inject | Expected Observable | Pass-Fail Signal |
|---|---|---|---|---|---|
| 1 | FS-01 | [threshold from Gate 2 FS-01] | | | |

```
GATE 2b CLOSE
Exit postconditions:
  [ ] One row per Include scenario; all four fields non-generic
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

Observable Signal requirement: named signal + detection horizon (concrete time window) +
rationale. Generic signals fail. No observable signal → RULE-OBS-GAP + MRF-OBS-NN.

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

This matrix verifies coverage in both directions between Gate 2b chaos rows and Gate 3
Observable Signal entries. It is a required output — absence is an Act 1 CLOSE blocker.

**Part A — Forward Direction: Chaos Scenario → Observable Signal**

For each chaos row in Gate 2b, list the Observable Signal ID(s) from Gate 3 that will
confirm detection of that chaos scenario's fault in production.

| Gate 2b Row | Scenario ID | Observable Signal ID(s) Linked | Coverage Gap? |
|---|---|---|---|
| Row 1 | FS-01 | [OEG-NN / DCV-NN / MRF-NN — the Gate 3 finding whose Observable Signal monitors this scenario's fault] | No / CHAOS-OBS-GAP-NN |

**Dark chaos finding**: If a chaos row has no Observable Signal linkage — the fault fires
but cannot be confirmed as detected in production. Emit:
`CHAOS-OBS-GAP-NN | Chaos row [N] / [Scenario ID] | no Observable Signal linked | [consequence: pass/fail result unverifiable in production without monitoring confirmation]`

**Part B — Reverse Direction: Observable Signal → Chaos Scenario**

For each Observable Signal entry in Gate 3 (across OEG, DCV, MRF tables), list the Gate
2b chaos row(s) that exercise the fault conditions monitored by that signal.

| Gate 3 Finding ID | Signal Name | Chaos Scenario ID(s) Linked | Coverage Gap? |
|---|---|---|---|
| OEG-01 | [named signal from Gate 3] | [FS-NN — the Gate 2b scenario that injects the fault this signal monitors] | No / OBS-CHAOS-GAP-NN |

**Unvalidated signal finding**: If an Observable Signal has no chaos scenario linkage —
the signal exists in the observability manifest but its production behavior under fault
conditions has never been exercised by the chaos harness. Emit:
`OBS-CHAOS-GAP-NN | [Gate 3 finding ID] | [signal name] | no chaos scenario linked | [consequence: signal behavior under fault is untested; cannot confirm it fires as specified]`

**Matrix summary**:
```
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
Exit postconditions: Every scenario anchored; all targets checked.
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
ACT 2 CLOSE (sign-off): Gate 5 / bypass / Registry Audit CLOSED; scope exhausted; no RULE-BYPASSED.
ACT 2 STATUS: CLOSED / OPEN
```

ANALYSIS COMPLETE (declared only when ACT 1 STATUS: CLOSED AND ACT 2 STATUS: CLOSED)

---

---

## V-04

**Variation axis**: Combination — Gate 2b Column Contract with identity assertion (from
V-02) + Bidirectional Chaos-Observability Coverage Matrix (from V-03). V-01's DS Primitive
VALID/INVALID template is not included. The Gate 2b Column Contract explicitly asserts
identity between the chaos activation boundary and the Trigger Condition threshold
expression. The Act 1 Terminal Coverage Matrix is the full bidirectional form with forward
and reverse tables, CHAOS-OBS-GAP-NN and OBS-CHAOS-GAP-NN gap findings, and a matrix
summary. Gate 1 uses the standard Argued-Impossible instruction without inline VALID/INVALID
examples.

**Hypothesis**: C-36 and C-38 together constitute the operational precision ceiling — they
ensure chaos tests are calibrated to the exact production boundary (C-36) and that chaos
and observability coverage are jointly verified (C-38). Combining them without adding C-15's
VALID/INVALID examples tests whether the two identity+bidirectional interventions alone
reach ceiling, isolating the contribution of the DS Primitive template change. If V-04
achieves C-36 PASS + C-38 PASS but misses C-15 (as expected), it establishes the C-15
gap as the remaining differentiator between V-04 and V-05.

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
| RULE-OBS-GAP | Named gap finding in Gate 3 has no Observable Signal entry at Gate 3 CLOSE | Emit OS-NN; produce named signal + detection horizon + rationale; if no signal exists, emit MRF-OBS-NN | DS Expert (Act 1) |
| RULE-COMMERCE-ANCHOR | Include scenario references a generic operation with no named commerce flow | Amend to name specific operation; record amendment | Commerce Validator (Act 2) |

**Bypass Owner**: Cross-act invocation not permitted.

---

### BYPASS GATE-REOPENING PROTOCOL

When any rule shows RULE-BYPASSED in the Post-Analysis Rule Registry Audit:
1. Bypass Owner emits: `GATE N-bypass: REOPENED — [rule ID] — bypass at [gate, entry ID]`
2. Bypass Owner applies the rule.
3. Bypass Owner emits: `GATE N-bypass: AMENDED — CLOSED — [rule now applied]`
4. Bypass Owner updates audit row.

**COMPLETE may not be declared** while any RULE-BYPASSED entry remains unresolved.

---

### ANTI-OMISSION ARCHITECTURE

| Level | Mechanism | Risk Targeted | Location |
|---|---|---|---|
| Table | Unified row index + anti-split | Row fragmentation | `#` column; Gate 2 |
| Section | Phase gate — all rows before Gap Identification | Premature advance | Gate 2 |
| Slot | **"Write this row now."** / **"Do not advance until..."** | Row omission | Row Descriptors |
| Column-Group | C-phase before D-phase within each row | Mid-row omission | Row Descriptors |
| Column | Column ownership in Column Contract | Column omission | Column Contract |

---

### COLUMN CONTRACT

| Column Name | Owner | Phase | Fill Requirement |
|---|---|---|---|
| `#` | Shared | — | Sequential integer; no gaps |
| `ID` | Shared | — | FS-NN; unique per scenario |
| `Trigger Condition` | DS Expert | C-phase | **Two required components**: (1) threshold expression — quantified activation condition; (2) detection signal — named observable confirming threshold crossing. Threshold expression used verbatim as Gate 2b chaos activation boundary. Qualitative descriptions without threshold expression fail. |
| `State` | Commerce Expert | C-phase | Specific system configuration; named components |
| `Capability` | Commerce Expert | C-phase | Named commerce operations still completable |
| `Data at Risk` | DS Expert | D-phase | Named data type + consistency failure mode |
| `Recovery Path` | DS Expert | D-phase | Four stages (Detect / Contain / Recover / Validate) each with mechanism \| actor \| SLA \| VS (named observable, distinct from mechanism) |
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
  [ ] SCOPE DECLARATION COMPLETE; Roster committed
Entry confirmed: [yes / no]
```

| # | ID | Failure Class | Confidence Basis | Disposition | Rule Applied | Notes |
|---|---|---|---|---|---|---|
| 1 | FS-01 | | | Include / BARRED / Argued-Impossible | RULE-BARRED-CG or — | |

BARRED: cite RULE-BARRED-CG; emit CG-NN.
Argued-Impossible: name DS Primitive (CAP theorem, synchrony guarantee, topology bound).
"Topic does not mention X" is not a DS Primitive.

**Gate 1b — BARRED Resolution**: No BARRED entries: `Gate 1b: none.`

```
GATE 1 CLOSE
Exit postconditions:
  [ ] Every candidate has one named disposition
  [ ] Every Argued-Impossible cites DS Primitive by name; Roster updated
Gate 1 STATUS: CLOSED / OPEN
```

---

### GATE 2: Four-Field Scenario Analysis

```
GATE 2 OPEN
Preconditions: [ ] Gate 1 STATUS: CLOSED
Entry confirmed: [yes / no]
```

**Anti-split**. **Section gate**. **Column-group gate** (C-phase before D-phase per row).

#### Row Descriptors

**Row 1 — FS-01:** Consequence context. **Write this row now.** Trigger Condition (threshold
+ detection signal — threshold verbatim in Gate 2b). C-phase then D-phase (VS per stage).
**Do not advance to Row 2 until non-placeholder in all columns.**

**Row 2 — FS-02:** **Write this row now.** All columns per Column Contract. **C-phase check.
Do not advance to Row 3 until non-placeholder.**

Continue for all remaining Include scenarios.

| # | ID | Trigger Condition | State | Capability | Data at Risk | Recovery Path | Severity | Blast Radius | Rule Applied |
|---|---|---|---|---|---|---|---|---|---|
| 1 | FS-01 | [threshold] / [detection signal] | | | | Detect / Contain / Recover / Validate each with mech\|actor\|SLA\|VS | | | |

```
GATE 2 CLOSE
Exit postconditions:
  [ ] All columns non-trivial; threshold + detection signal; four VS per recovery path
Gate 2 STATUS: CLOSED / OPEN
```

---

### GATE 2b: Chaos Engineering Specification

#### Gate 2b Column Contract

| Column Name | Owner | Fill Requirement |
|---|---|---|
| `#` | Shared | Sequential integer; no gaps |
| `Scenario ID` | Shared | FS-NN from Gate 1 Include list; one row per scenario |
| `Trigger Condition Reference` | DS Expert | **Identity assertion**: the chaos activation boundary expression IS the Trigger Condition threshold expression from Gate 2 for this scenario — identical, not a derivative or approximation. Transcribe the exact threshold expression string verbatim from the Gate 2 Trigger Condition column. Any modification between Gate 2 and Gate 2b produces an uncalibrated chaos test not predictive of production trigger behavior. The same expression that gates production monitoring gates this chaos test — identical by definition. |
| `Inject` | DS Expert | `[fault type]: [named mechanism] — [parameter]`. Generic descriptions fail. |
| `Expected Observable` | DS Expert | In-fault system behavior at named observation granularity |
| `Pass-Fail Signal` | DS Expert | Binary artifact naming specific metric/code/log/state |

```
GATE 2b OPEN
Preconditions:
  [ ] Gate 2 STATUS: CLOSED
  [ ] Include scenario IDs available from Gate 1
  [ ] Identity assertion acknowledged: Trigger Condition Reference = verbatim Gate 2
      threshold expression — identical, not a derivative
Entry confirmed: [yes / no]
```

For each Include scenario, write one row per Gate 2b Column Contract. Invoke
RULE-CHAOS-INJECT bypass for any scenario without a row before Gate 2b CLOSE.

| # | Scenario ID | Trigger Condition Reference | Inject | Expected Observable | Pass-Fail Signal |
|---|---|---|---|---|---|
| 1 | FS-01 | [verbatim threshold expression from Gate 2 FS-01 — identical to Gate 2 value] | | | |

```
GATE 2b CLOSE
Exit postconditions:
  [ ] One row per Include scenario
  [ ] Every Trigger Condition Reference = verbatim Gate 2 threshold expression (identity
      assertion satisfied — no paraphrase, no independent calibration)
  [ ] All four fields non-generic
  [ ] RULE-CHAOS-INJECT resolved for any missing rows
Gate 2b STATUS: CLOSED / OPEN
```

---

### GATE 3: Gap Identification

```
GATE 3 OPEN
Preconditions: [ ] Gate 2 STATUS: CLOSED
Entry confirmed: [yes / no]
```

Observable Signal: named signal + detection horizon (concrete time window) + rationale.
Generic signal ("add monitoring") fails. No signal → RULE-OBS-GAP + MRF-OBS-NN.

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
  [ ] All three categories; named signal + horizon + rationale per finding
  [ ] Findings without signal: MRF-OBS-NN + RULE-OBS-GAP
Gate 3 STATUS: CLOSED / OPEN
```

---

### GATE 4: Amendment Pass

No amendments: `Gate 4: no amendments required.`

```
GATE 4 CLOSE
Exit postconditions: Recovery paths min two actor steps; superseded nils annotated.
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

POST-ANALYSIS REGISTRY AUDIT (ACT 1) COMPLETE

---

### Act 1 Terminal: Nil Supersession Log

No supersessions: `No supersessions in this run.`

---

### Act 1 Terminal: Bidirectional Chaos-Observability Coverage Matrix

**Part A — Forward Direction: Chaos Scenario → Observable Signal**

| Gate 2b Row | Scenario ID | Observable Signal ID(s) Linked | Coverage Gap? |
|---|---|---|---|
| Row 1 | FS-01 | [OEG-NN / DCV-NN / MRF-NN whose Observable Signal monitors this scenario] | No / CHAOS-OBS-GAP-NN |

Dark chaos finding (chaos row with no linked Observable Signal):
`CHAOS-OBS-GAP-NN | Chaos row [N] / [Scenario ID] | no Observable Signal linked | fault fires but result unverifiable in production without monitoring confirmation`

**Part B — Reverse Direction: Observable Signal → Chaos Scenario**

| Gate 3 Finding ID | Signal Name | Chaos Scenario ID(s) Linked | Coverage Gap? |
|---|---|---|---|
| OEG-01 | [named signal] | [FS-NN exercising this signal's fault condition] | No / OBS-CHAOS-GAP-NN |

Unvalidated signal finding (Observable Signal with no linked chaos scenario):
`OBS-CHAOS-GAP-NN | [Gate 3 finding ID] | [signal name] | no chaos scenario linked | signal behavior under fault is untested`

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
    Gate 1 / 1b / 2 / 2b / 3 / 4: [CLOSED / OPEN — reason each]
    GATE N-bypass blocks: [CLOSED / none triggered]
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
GATE 5 CLOSE: Every scenario anchored; all targets checked.
Gate 5 STATUS: CLOSED / OPEN
```

### Act 2 Terminal: Post-Analysis Rule Registry Audit

| Rule ID | Invocations | Citations | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-COMMERCE-ANCHOR | | | | |

POST-ANALYSIS REGISTRY AUDIT (ACT 2) COMPLETE

### Inertia Synthesis

Per finding: failure mode, rate, horizon, metric.
Urgency: HIGH / MEDIUM / LOW. Highest-risk: [gap ID]. Status-quo: [{topic} specific].
Intervention: [owner + threshold + consequence].

```
ACT 2 CLOSE: Gate 5 / bypass / Registry Audit CLOSED; scope exhausted; no RULE-BYPASSED.
ACT 2 STATUS: CLOSED / OPEN
```

ANALYSIS COMPLETE (declared only when ACT 1 STATUS: CLOSED AND ACT 2 STATUS: CLOSED)

---

---

## V-05

**Variation axis**: Full integration — All three R12 interventions combined: (1) DS Primitive
VALID/INVALID template in Gate 1 Argued-Impossible (from V-01, targeting C-15); (2) Gate 2b
Column Contract with explicit identity assertion for Trigger Condition Reference (from V-02,
targeting C-36); (3) Bidirectional Chaos-Observability Coverage Matrix with CHAOS-OBS-GAP-NN
and OBS-CHAOS-GAP-NN gap findings (from V-03, targeting C-38). Gate 2b precondition block
includes the identity assertion acknowledgement. Gate 1 CLOSE exit postconditions include
confirmation that all Argued-Impossible entries use the DS Primitive cited field with
architecture basis. ACT 1 CLOSE references the bidirectional matrix explicitly. No other
structural changes from R11 V-05.

**Hypothesis**: All three uncracked/V-05-only criteria (C-15, C-36, C-38) require structural
template changes at different gates — C-15 at Gate 1, C-36 at Gate 2b, C-38 at the Act 1
Terminal. They are orthogonal interventions with no conflict: the DS Primitive template
does not interact with the identity assertion, which does not interact with the bidirectional
matrix. Full integration should achieve PASS on all three simultaneously and establish the
new uncapped ceiling. The discriminating question for R12 is whether single-axis variations
(V-01, V-02, V-03) successfully isolate each criterion — confirming the interventions are
independent and individually sufficient — or whether ceiling requires all three together.

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

**Bypass Owner column**: Cross-act invocation not permitted. Commerce Validator cannot
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

**Argued-Impossible template** — complete this block for every Argued-Impossible entry:

```
FS-NN Argued-Impossible:
DS Primitive cited: [name the specific CAP theorem guarantee / deployment topology
  constraint / synchrony guarantee that architecturally forecloses this failure class —
  must address the architecture of {topic}, not the text of the prompt description]

VALID argument example:
  "DS Primitive cited: Strong consistency guarantee — single-primary RDBMS with synchronous
   replication and no async replica forecloses split-brain because no partition can produce
   two acknowledged writes to divergent primaries under this topology."

INVALID argument example:
  "DS Primitive cited: The topic description does not mention a message queue, so queue
   ordering violations are not in scope."
  [Fails: this argument addresses description absence, not architecture. The system may have
   a message queue not described in the prompt. A valid argument must cite what the
   architecture guarantees — a constraint that forecloses the failure class regardless of
   how the prompt is worded.]
```

Apply this template for every Argued-Impossible row. A DS Primitive field that contains a
topic-scope argument ("the topic doesn't mention X", "the description is too simple for
this") is a Gate 1 violation. Identify the architectural guarantee; do not read prompt
omission as an architecture constraint.

**Gate 1b — BARRED Resolution**

| BARRED ID | Confidence Basis | Resolved? | Resolution Mechanism | New Disposition |
|---|---|---|---|---|

No BARRED entries: `Gate 1b: none.`

```
GATE 1 CLOSE
Exit postconditions:
  [ ] Every candidate has one named disposition
  [ ] Every BARRED has CG-NN emitted
  [ ] Every Argued-Impossible has DS Primitive cited: field with architecture basis —
      not description absence (topic-scope argument is a gate violation)
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
mechanism, non-generic), Severity, Blast Radius, Rule Applied.
**Do not advance to Row 2 until all columns including both Trigger Condition components and
all four VS entries are non-placeholder.**
Example VS entries: Detect VS — "inventory-service health probe returns degraded"; Contain
VS — "reserve-lock-count metric increments"; Recover VS — "inventory-service heartbeat
returns 200 for 30s"; Validate VS — "inventory-accuracy metric returns to baseline ± 0.5%."

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
| `Trigger Condition Reference` | DS Expert | **Identity assertion**: the chaos activation boundary expression IS the Trigger Condition threshold expression from Gate 2 for this scenario — identical, not a derivative or approximation. Transcribe the exact threshold expression string verbatim from the Gate 2 Trigger Condition column. Do not paraphrase, abbreviate, or add conditions not present in Gate 2. Any modification between Gate 2 and Gate 2b produces an uncalibrated chaos test whose results are not directly predictive of production trigger behavior. The same logical expression that activates production monitoring activates this chaos test — they share the same boundary by assertion, not by convention. |
| `Inject` | DS Expert | `[fault type]: [named mechanism] — [parameter]`. Generic descriptions ("make service unavailable") are not valid. |
| `Expected Observable` | DS Expert | In-fault system behavior at named observation granularity; not post-recovery state |
| `Pass-Fail Signal` | DS Expert | Binary artifact naming a specific metric value, API response code, log entry, or system state; generic outcomes ("system handles it correctly") fail |

```
GATE 2b OPEN
Preconditions:
  [ ] Gate 2 STATUS: CLOSED
  [ ] Include scenario list from Gate 1 available (IDs: FS-01, FS-02, ...)
  [ ] Identity assertion acknowledged: Trigger Condition Reference for each scenario
      must contain the verbatim threshold expression from Gate 2 — identical, not derived
Entry confirmed: [yes / no]
```

For each Include scenario from Gate 1, write one row using the Gate 2b Column Contract.
The Trigger Condition Reference must contain the verbatim threshold expression from Gate 2
for that scenario ID — the identity assertion in the column contract is the governing
constraint for this field.

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

**Observable Signal requirement**: Every named finding in all three gap tables must carry
three Observable Signal components: (1) named signal — specific metric name, log pattern,
trace attribute, or alert condition; (2) detection horizon — concrete time window from gap
onset to signal firing (e.g., "within 30s of fault injection", "by next heartbeat cycle
<= 60s" — generic language "promptly" or "as soon as possible" fails); (3) rationale
sentence — why this signal surfaces the gap before user impact. Generic signals ("add
monitoring") fail. Unnamed observables ("check the logs") fail. If no observable signal
exists for a finding, invoke RULE-OBS-GAP bypass and emit MRF-OBS-NN: "no production
observability for [gap ID]" — undetectable gaps are missing recovery flows.

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

`MRF-OBS-NN | [gap ID] | no production observability for [gap ID] | [carrying cost of undetected gap] | N/A | [horizon: unbounded — undetectable until user reports] | [gap is known but no automatic monitoring signal exists]`

```
GATE 3 CLOSE
Exit postconditions:
  [ ] All three gap categories present; every finding or typed nil with scope rationale
  [ ] Every named finding has Observable Signal (named signal + detection horizon + rationale)
  [ ] Detection horizons are concrete time windows — not generic language
  [ ] Findings with no observable signal have MRF-OBS-NN and RULE-OBS-GAP fired
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
linked to at least one chaos scenario (reverse direction). Uncovered entries in either
direction generate named gap findings.

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
