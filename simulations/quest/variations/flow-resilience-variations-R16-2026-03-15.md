[Scenario Name]**

Consequence context: [acute consequences per resolution branch -- oversell / double-charge / duplicate fulfillment]. Chronic if never addressed: [rate] / [horizon] / [metric accumulates].

**Write this row now.**
Fill Trigger Condition: (1) threshold expression; (2) detection signal. Threshold verbatim in Gate 2b. C-phase (Commerce Expert): State + Capability. **C-phase complete check before D-phase.** D-phase (DS Expert): Data at Risk, Recovery Path (four stages with mechanism, SLA, named VS -- each VS will be registered in the Act 1 Terminal VS Cross-Reference Registry), Severity, Blast Radius, Rule Applied. **Do not advance to Row 2 until all columns non-placeholder.**

---

**Row 2 -- FS-02: [Scenario Name]**

**Write this row now.** Fill all columns per Column Contract. **C-phase complete check before D-phase. Do not advance to Row 3 until non-placeholder.**

---

Continue this pattern for all remaining Include scenarios.

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
Gate 2 STATUS: CLOSED / OPEN -- [reason if open]
```

---

### GATE 2b: Chaos Engineering Specification

#### Gate 2b Column Contract

| Column Name | Owner | Fill Requirement |
|---|---|---|
| `#` | Shared | Sequential integer; no gaps |
| `Scenario ID` | Shared | FS-NN; one row per Include scenario |
| `Trigger Condition Reference` | DS Expert | **Identity assertion**: chaos activation boundary = Gate 2 threshold expression, verbatim. Transcribe exact string. Do not paraphrase. |
| `Inject` | DS Expert | `[fault type]: [named mechanism] -- [parameter]`. Generic descriptions fail. |
| `Expected Observable` | DS Expert | In-fault behavior at named observation granularity |
| `Pass-Fail Signal` | DS Expert | Binary artifact naming specific metric, code, log, or state |

```
GATE 2b OPEN
Preconditions:
  [ ] Gate 2 STATUS: CLOSED
  [ ] Include scenario list from Gate 1 available (IDs: FS-01, FS-02, ...)
  [ ] Identity assertion acknowledged: chaos activation boundary = Gate 2 threshold
      expression for each scenario, verbatim -- not a derivative
Entry confirmed: [yes / no]
```

| # | Scenario ID | Trigger Condition Reference | Inject | Expected Observable | Pass-Fail Signal |
|---|---|---|---|---|---|
| 1 | FS-01 | [verbatim threshold expression from Gate 2 FS-01] | | | |

```
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
```

---

### GATE 3: Gap Identification

```
GATE 3 OPEN
Preconditions:
  [ ] Gate 2 STATUS: CLOSED
Entry confirmed: [yes / no]
```

**Observable Signal requirement**: Every named finding must carry: (1) named signal; (2) detection horizon (concrete time window); (3) rationale sentence. No signal -> invoke RULE-OBS-GAP; emit MRF-OBS-NN.

**OEG -- Offline Experience Gaps**

| ID | Scenario Ref | Gap Description | Status-Quo Carrying Cost | Observable Signal | Detection Horizon | Rationale | Actionable Recommendation |
|---|---|---|---|---|---|---|---|
| OEG-01 | FS-NN | | [rate \| horizon \| user failure] | [named signal] | [time to alert] | [why early] | |

No OEG: `OEG-NIL-1: [scope rationale]`

**DCV -- Data Consistency Violations**

| ID | Source | Data Type | Failure Mode | Conflict Resolution | Adequacy | Status-Quo Carrying Cost | Observable Signal | Detection Horizon | Rule Applied |
|---|---|---|---|---|---|---|---|---|---|
| DCV-01 | FS-NN | | | LWW / merge / manual / reject-stale / undefined | adequate / inadequate / undefined | [rate \| horizon \| metric] | [named signal] | [time to alert] | |

No DCV: `DCV-NIL-1: [scope rationale]`

**MRF -- Missing Recovery Flows**

| ID | Scenario Ref | Absent Mechanism | Status-Quo Carrying Cost | Observable Signal | Detection Horizon | Why No Current Path Exists |
|---|---|---|---|---|---|---|
| MRF-01 | FS-NN | | [rate \| horizon \| failure] | [named signal] | [time to alert] | |

No MRF: `MRF-NIL-1: [scope rationale]`

```
GATE 3 CLOSE
Exit postconditions:
  [ ] All three gap categories present; every finding or typed nil with scope rationale
  [ ] Every named finding has Observable Signal (named signal + detection horizon + rationale)
  [ ] Findings with no observable signal have MRF-OBS-NN emitted and RULE-OBS-GAP fired
  [ ] Status-Quo Carrying Cost present for every named finding
  [ ] All RULE-CR-DCV entries assigned DCV-NN
Gate 3 STATUS: CLOSED / OPEN -- [reason if open]
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

No amendments: `Gate 4: no amendments required.`

```
GATE 4 CLOSE
Exit postconditions:
  [ ] All recovery paths have minimum two actor-labeled steps
  [ ] Every superseded nil has SUPERSEDED annotation with finding ID
Gate 4 STATUS: CLOSED / OPEN -- [reason if open]
```

---

### Act 1 Terminal: Post-Analysis Rule Registry Audit

**BYPASS-TRIGGER column**: A RULE-BYPASSED status requires a non-empty BYPASS-TRIGGER entry.

| Rule ID | Invocations | Citations (gate, entry) | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-CR-DCV | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | [empty or trigger citation] |
| RULE-BARRED-CG | | | | |
| RULE-NIL-SUPERSEDE | | | | |
| RULE-CHAOS-INJECT | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | [empty or `GATE 2b-bypass: REOPEN -- apply RULE-CHAOS-INJECT at Gate 2b, FS-NN`] |
| RULE-OBS-GAP | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | [empty or `GATE 3-bypass: REOPEN -- apply RULE-OBS-GAP at Gate 3, OEG/DCV/MRF-NN`] |
| RULE-VS-MISSING | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | [empty or `VS-REG-bypass: REOPEN -- apply RULE-VS-MISSING at VS Registry, FS-NN stage`] |

POST-ANALYSIS REGISTRY AUDIT (ACT 1) COMPLETE: [confirm no RULE-BYPASSED entries remain]

---

### Act 1 Terminal: Nil Supersession Log

| Nil ID | Gap Type | State | Superseded By | Gate |
|---|---|---|---|---|

No supersessions: `No supersessions in this run.`

---

### Act 1 Terminal: VS Cross-Reference Registry

This registry is a required Act 1 Terminal artifact. For every named Verification Signal (VS) in every recovery path stage across all Gate 2 Include scenarios, emit one four-field registry entry. A VS present in a Gate 2 row but absent from this registry is a RULE-VS-MISSING violation; invoke the bypass protocol and emit VS-REG-NN before declaring this terminal complete.

**VS registry entry format**:
```
VS ID:               VS-NN
Gate-2 Row Ref:      FS-NN (scenario ID from Gate 1)
Stage:               Detect | Contain | Recover | Validate
Observation Assertion: [named observable artifact that confirms this stage is complete,
                       stated as a specific condition: e.g., "inventory-service /health
                       returns HTTP 200 with status:healthy after stock-sync completes" --
                       not a restatement of the mechanism. Must name the observable and
                       the condition under which it fires. Generic language ("system
                       returns to normal") fails.]
```

Each scenario contributes up to four VS entries (one per stage). If a stage's VS is shared with another scenario's stage, it still requires its own registry entry with its own Gate-2 Row Ref -- name collision is expected and flagged only if the Observation Assertion is also identical (indicating a copy rather than a scenario-specific assertion).

| VS ID | Gate-2 Row Ref | Stage | Observation Assertion |
|---|---|---|---|
| VS-01 | FS-01 | Detect | [named observable + condition] |
| VS-02 | FS-01 | Contain | [named observable + condition] |
| VS-03 | FS-01 | Recover | [named observable + condition] |
| VS-04 | FS-01 | Validate | [named observable + condition] |

Continue for all Include scenarios. Rows are ordered by Gate-2 Row Ref then Stage sequence (Detect -> Contain -> Recover -> Validate).

If any Gate 2 stage carries a generic VS (e.g., "system healthy") rather than a named observable -- invoke RULE-VS-MISSING; emit VS-REG-NN with a placeholder Observation Assertion of `[UNRESOLVABLE -- no named observable in Gate 2 stage; MRF-OBS-NN recommended]` and fire RULE-OBS-GAP if the gap is not already registered in Gate 3.

VS CROSS-REFERENCE REGISTRY COMPLETE: [N] VS entries registered across [M] scenarios.

---

### Act 1 Terminal: Bidirectional Chaos-Observability Coverage Matrix

**Part A -- Forward Direction: Chaos Scenario -> Observable Signal**

| Gate 2b Row | Scenario ID | Observable Signal ID(s) Linked | Coverage Gap? |
|---|---|---|---|
| Row 1 | FS-01 | [OEG-NN / DCV-NN / MRF-NN] | No / CHAOS-OBS-GAP-NN |

**Part B -- Reverse Direction: Observable Signal -> Chaos Scenario**

| Gate 3 Finding ID | Signal Name | Chaos Scenario ID(s) Linked | Coverage Gap? |
|---|---|---|---|
| OEG-01 | [named signal] | [FS-NN] | No / OBS-CHAOS-GAP-NN |

```
Matrix summary:
Forward coverage: [N] of [M] chaos rows have linked Observable Signals.
Reverse coverage: [N] of [M] Observable Signals have linked chaos scenarios.
Dark chaos gaps: [CHAOS-OBS-GAP-NN list / none]
Unvalidated signal gaps: [OBS-CHAOS-GAP-NN list / none]
```

**GAP REGISTRY**

*Part A Gaps (Chaos Scenario -> Observable Signal):*

For each CHAOS-OBS-GAP-NN finding:
```
Source: [CHAOS-OBS-GAP-NN -- Gate 2b row N / Scenario ID]
Missing link: [named Observable Signal absent -- no Gate 3 finding monitors this fault class]
Consequence: [pass/fail result unverifiable in production; fault fires silently]
```

No Part A gaps:
```
Source: N/A -- all chaos scenarios are fully linked to >= 1 Observable Signal
Missing link: N/A -- no dark chaos scenarios in this direction
Consequence: nil -- PART A bidirectional coverage complete
```

*Part B Gaps (Observable Signal -> Chaos Scenario):*

For each OBS-CHAOS-GAP-NN finding:
```
Source: [OBS-CHAOS-GAP-NN -- Gate 3 finding ID / Signal Name]
Missing link: [no chaos scenario exercises the fault conditions monitored by this signal]
Consequence: [signal behavior under fault conditions untested; cannot confirm it fires as specified]
```

No Part B gaps:
```
Source: N/A -- all Observable Signals are fully linked to >= 1 chaos scenario
Missing link: N/A -- no unvalidated signals in this direction
Consequence: nil -- PART B bidirectional coverage complete
```

BIDIRECTIONAL CHAOS-OBSERVABILITY COVERAGE MATRIX COMPLETE

---

### Act 1 Terminal: Scope Verification

| Declared Operation | Covered | Gap Finding |
|---|---|---|
| [operation] | Yes / No | SV-GAP-NN / -- |

SCOPE VERIFICATION COMPLETE

---

```
ACT 1 CLOSE (sign-off)
(1) All gates within Act 1 CLOSED:
    Gate 1:                  [CLOSED / OPEN -- reason]
    Gate 1b:                 [CLOSED / N/A]
    Gate 2:                  [CLOSED / OPEN -- reason]
    Gate 2b:                 [CLOSED / OPEN -- reason]
    Gate 3:                  [CLOSED / OPEN -- reason]
    Gate 4:                  [CLOSED / OPEN -- reason]
    GATE N-bypass blocks:    [CLOSED / none triggered]
    Act 1 Registry Audit:    [CLOSED / OPEN -- reason]
    VS Cross-Reference Registry: [COMPLETE / OPEN -- reason]
    Bidirectional Chaos-Observability Matrix: [COMPLETE / OPEN -- reason]
(2) Act 1 scope exhausted: [yes / list any unresolved items]
(3) No RULE-BYPASSED conditions remain unresolved within Act 1: [yes / exception detail]
ACT 1 STATUS: CLOSED / OPEN
```

---

```
ACT 2 OPEN -- Commerce Domain Validator
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
| FS-01 | Yes / No | | -- / CV-DCV-01 / CV-OEG-01 / CV-MRF-01 |

Commerce-domain finding targets:
- Inventory oversell under partition: [present / absent -- rationale]
- Payment idempotency window expiry: [present / absent -- rationale]
- Loyalty point double-redemption under split-brain: [present / absent -- rationale]
- Order state divergence under partial fulfillment failure: [present / absent -- rationale]

```
GATE 5 CLOSE
Exit postconditions:
  [ ] Every Include scenario anchored to a named commerce operation
  [ ] All RULE-COMMERCE-ANCHOR invocations recorded
  [ ] All four commerce-domain targets checked
Gate 5 STATUS: CLOSED / OPEN -- [reason if open]
```

---

### Act 2 Terminal: Post-Analysis Rule Registry Audit

| Rule ID | Invocations | Citations | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-COMMERCE-ANCHOR | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | |

POST-ANALYSIS REGISTRY AUDIT (ACT 2) COMPLETE

---

### Inertia Synthesis -- What Does Doing Nothing Cost?

**Per-finding carrying cost**: For each named gap (OEG-NN, DCV-NN, MRF-NN): failure mode, rate, horizon, metric.

**Overall synthesis**:
Urgency: HIGH / MEDIUM / LOW
Highest-risk finding: [gap ID] -- [carrying cost]
Status-quo option: [what "do nothing" looks like for `{topic}` specifically, including which VS entries in the registry represent the earliest recovery-stage signals that will never fire if the gap persists]
Intervention recommendation: [owner + threshold + consequence of missing threshold]

```
ACT 2 CLOSE (sign-off)
(1) All gates within Act 2 CLOSED:
    Gate 5: [CLOSED / OPEN -- reason]
    GATE 5-bypass blocks: [CLOSED / none triggered]
    Act 2 Registry Audit: [CLOSED / OPEN -- reason]
(2) Act 2 scope exhausted: [yes]
(3) No RULE-BYPASSED conditions remain: [yes / exception detail]
ACT 2 STATUS: CLOSED / OPEN
```

```
INDEPENDENCE AUDIT:
Gate 2b CLOSE -- two-checkbox independent form (C-42: confirmed).
  Checkbox 1: Identity assertion confirmed -- every TCR contains verbatim Gate 2 threshold
              expression.
  Checkbox 2: Prohibition clause confirmed -- no TCR contains a paraphrased or
              independently calibrated expression.
Gate 1 CLOSE -- two-checkbox independent form (C-43: confirmed).
  Checkbox 1: Basis confirmed -- every Argued-Impossible cites an architecture basis.
  Checkbox 2: Prohibition confirmed -- no Argued-Impossible uses description absence as
              its basis.
Gate 2 CLOSE -- single-condition postconditions only; not eligible for independence pattern.
Gate 3 CLOSE -- single-condition postconditions only; not eligible.
Gate 4 CLOSE -- single-condition postconditions only; not eligible.
Gate 5 CLOSE -- single-condition postconditions only; not eligible.
No further gate CLOSE blocks in this template carry both a positive confirmation clause
and a prohibition clause.
Independence scope: COMPLETE.
```

ANALYSIS COMPLETE (declared only when ACT 1 STATUS: CLOSED AND ACT 2 STATUS: CLOSED)

---

---

## Scorecard Prediction (under v15)

| Rank | Variation | C-44 | C-45 | C-46 | C-47 (cand.) | Uncapped |
|------|-----------|------|------|------|--------------|---------|
| 1 | **V-05** | PASS | PASS | PASS | PASS | **76/76** + C-47 |
| 2 (tie) | **V-04** | PASS | PASS | PASS | FAIL | **76/76** |
| 3 (tie) | **V-02** | PASS | PASS | PASS | FAIL | **74/76** |
| 3 (tie) | **V-03** | PASS | FAIL | PASS | FAIL | **74/76** |
| 5 | **V-01** | PASS | FAIL | FAIL | FAIL | **72/76** |

**Separation logic:**
- V-01 vs V-03: both from R15-V01 baseline, V-03 adds C-46 (+2) → 2-point gap confirms C-46 is independently load-bearing from C-44.
- V-03 vs V-04: identical registry structure, V-04 adds independence completeness block (+2) → 2-point gap confirms C-45 is independently load-bearing from C-44+C-46.
- V-02 vs V-04: both at 76/76 construction paths differ (V-02 from R15-V04, V-04 from R15-V01); tie expected under v15 since both pass same criteria — v16 will need a new axis to separate if needed.
- V-05 vs V-04: both 76/76 under v15; V-05 carries the VS Cross-Reference Registry which is not captured by any existing criterion. If V-05's VS Registry structure is extractable as C-47 (orthogonal to C-35 and C-44), v16 will discriminate V-05 above V-04.

**Open for R17:** C-47 PASS for V-01/V-02/V-03/V-04 (no VS registry terminal in any); any structural property emerging exclusively from V-05's VS registry orthogonality argument.
