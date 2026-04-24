Continuing V-05 from the Row 1 descriptor cut point.

---

D-phase (DS Expert): Data at Risk, Recovery Path (four stages -- mechanism, actor, SLA, VS; each VS will be registered in VS Cross-Reference Registry; any VS with no Gate 3 Observable Signal Ref will produce a VSOG-NN in the VS Observability Gap Report), Severity, Blast Radius, Rule Applied.
**Do not advance to Row 2 until all columns non-placeholder and all four VS entries named.**

---

**Row 2 -- FS-02: [Scenario Name]**

**Write this row now.** All columns per Column Contract. **C-phase complete check before D-phase. Do not advance to Row 3 until non-placeholder.**

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
| `Trigger Condition Reference` | DS Expert | Identity assertion: chaos activation boundary = Gate 2 threshold expression verbatim -- identical, not a derivative. Transcribe exact threshold expression string. Do not paraphrase, abbreviate, or add conditions not in Gate 2. |
| `Inject` | DS Expert | `[fault type]: [named mechanism] -- [parameter]`. Generic descriptions fail. |
| `Expected Observable` | DS Expert | In-fault system behavior at named observation granularity; not post-recovery state |
| `Pass-Fail Signal` | DS Expert | Binary artifact naming specific metric, response code, log entry, or system state |

```
GATE 2b OPEN
Preconditions:
  [ ] Gate 2 STATUS: CLOSED
  [ ] Include scenario list from Gate 1 available
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

**Observable Signal requirement**: Every named finding must carry: (1) named signal; (2) detection horizon (concrete time window, not "promptly"); (3) rationale sentence. Generic signals fail. No signal: invoke RULE-OBS-GAP; emit MRF-OBS-NN.

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

| Rule ID | Invocations | Citations (gate, entry) | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-CR-DCV | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | |
| RULE-BARRED-CG | | | | |
| RULE-NIL-SUPERSEDE | | | | |
| RULE-CHAOS-INJECT | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | |
| RULE-OBS-GAP | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | |

`POST-ANALYSIS REGISTRY AUDIT (ACT 1) COMPLETE: [confirm no RULE-BYPASSED entries remain]`

---

### Act 1 Terminal: Nil Supersession Log

No supersessions: `No supersessions in this run.`

---

### Act 1 Terminal: VS Cross-Reference Registry

This registry is a required Act 1 Terminal artifact. For every named VS in the Recovery Path column across all Gate 2 scenario rows, register one entry. A missing entry for any Gate 2 VS is an ACT 1 CLOSE blocker.

| VS ID | Scenario ID | Stage | VS Text | Observable Signal Ref |
|---|---|---|---|---|
| VS-01 | FS-NN | Detect / Contain / Recover / Validate | [VS text from Recovery Path -- transcribe verbatim] | [OEG-NN / DCV-NN / MRF-NN from Gate 3 that monitors this observable; or N/A -- no Gate 3 finding corresponds. N/A entries will produce VSOG-NN in VS Observability Gap Report.] |

**VS ID assignment**: VS-NN sequential across all scenarios and stages. Shared VS across scenarios: distinct IDs, note "Same signal as VS-MM; independently registered for FS-NN."

**Observable Signal Ref**: Gate 3 finding ID or explicit N/A nil marker. Blank not permitted. At least one concrete ID required.

**N/A escalation**: Every entry carrying N/A in Observable Signal Ref will be elevated to a structured VSOG-NN finding in the VS Observability Gap Report immediately following this registry.

**Completion gate**: COMPLETE may not be declared while any scenario x stage slot has a blank VS or blank Observable Signal Ref. Zero-scenario: `VS REGISTRY: none.`

`VS REGISTRY COMPLETE: [VS-01 through VS-NN]`

---

### Act 1 Terminal: VS Observability Gap Report

This report is a required Act 1 Terminal artifact produced immediately after the VS Cross-Reference Registry. For every VS registry entry carrying Observable Signal Ref = N/A, produce one structured VSOG-NN finding. A VS registry with no N/A entries produces a nil confirmation. Absence of this report is an ACT 1 CLOSE blocker.

**Purpose**: VS registry N/A entries indicate recovery stages whose completion is confirmable only by SLA elapse or by reading mechanism output, not by any production observable. These are monitoring-dark recovery stages: the recovery path can succeed in a test environment while being unobservable in production. VSOG-NN findings surface these gaps as independently actionable items.

For each N/A entry in the VS Cross-Reference Registry, write one structured finding:

```
VSOG-NN
VS ID: [VS-NN from VS Cross-Reference Registry]
Stage Context: [Scenario ID] -- [Stage Name]
VS Text: [VS text from registry]
Dark condition: [why no production observable fires to confirm this recovery stage
  completion -- name the specific absence: no metric emitted by [actor] at [stage]
  completion; no log entry written by [mechanism] confirming [state transition];
  no API response code confirming [condition]. Must name the specific missing signal
  class, not just assert absence.]
Consequence: recovery stage completion for [Scenario ID] [Stage Name] is not confirmed
  by production monitoring; [mechanism]'s [stage] completion is only verifiable by
  SLA elapse ([SLA target]); if [stage] silently fails or stalls, no alert fires until
  [downstream consequence or user-visible failure].
```

No monitoring-dark stages:

```
VSOG-NIL
VS ID: N/A -- all VS registry entries carry concrete Observable Signal Refs
Stage Context: N/A -- no N/A entries in VS registry
Dark condition: nil -- all recovery stage completion signals are covered by Gate 3
  Observable Signals
Consequence: nil -- VS Observability Gap Report coverage complete
```

Registry coverage summary:

```
Total VS registry entries: [N]
Linked to Observable Signal (concrete ID): [N]
Monitoring-dark (N/A -> VSOG-NN): [N]
VSOG findings emitted: [VSOG-NN list / none]
```

`VS OBSERVABILITY GAP REPORT COMPLETE`

---

### Act 1 Terminal: Bidirectional Chaos-Observability Coverage Matrix

This matrix is a required Act 1 Terminal artifact. Absence is an Act 1 CLOSE blocker.

**Part A -- Forward Direction: Chaos Scenario -> Observable Signal**

| Gate 2b Row | Scenario ID | Observable Signal ID(s) Linked | Coverage Status |
|---|---|---|---|
| Row 1 | FS-01 | [OEG-NN / DCV-NN / MRF-NN] | Linked / DARK |

**PART A GAP REGISTRY**

For each DARK row:

```
CHAOS-OBS-GAP-NN
Source: [Gate 2b Row N / Scenario ID FS-NN]
Missing link: [fault class and reason no Gate 3 signal covers it]
Consequence: [chaos test result unverifiable in production; fault detection unconfirmed]
```

No dark chaos gaps:

```
CHAOS-OBS-GAP-NIL
Source: N/A -- all chaos scenarios fully linked to >= 1 Observable Signal
Missing link: N/A -- no dark chaos scenarios in this direction
Consequence: nil -- PART A bidirectional coverage complete
```

---

**Part B -- Reverse Direction: Observable Signal -> Chaos Scenario**

| Gate 3 Finding ID | Signal Name | Chaos Scenario ID(s) Linked | Coverage Status |
|---|---|---|---|
| OEG-01 | [named signal] | [FS-NN] | Linked / UNVALIDATED |

**PART B GAP REGISTRY**

For each UNVALIDATED row:

```
OBS-CHAOS-GAP-NN
Source: [Gate 3 Finding ID / Signal Name]
Missing link: [no Gate 2b row injects the fault condition this signal monitors]
Consequence: [signal behavior under fault untested; cannot confirm it fires as specified]
```

No unvalidated signal gaps:

```
OBS-CHAOS-GAP-NIL
Source: N/A -- all Observable Signals fully linked to >= 1 chaos scenario
Missing link: N/A -- no unvalidated signals in this direction
Consequence: nil -- PART B bidirectional coverage complete
```

---

```
Matrix closure:
Forward coverage: [N] of [M] chaos rows linked to Observable Signals.
Reverse coverage: [N] of [M] Observable Signals linked to chaos scenarios.
PART A GAP REGISTRY: [CHAOS-OBS-GAP-NN list / CHAOS-OBS-GAP-NIL]
PART B GAP REGISTRY: [OBS-CHAOS-GAP-NN list / OBS-CHAOS-GAP-NIL]
```

`BIDIRECTIONAL CHAOS-OBSERVABILITY COVERAGE MATRIX COMPLETE`

---

### Act 1 Terminal: Scope Verification

| Declared Operation | Covered | Gap Finding |
|---|---|---|
| [operation] | Yes / No | SV-GAP-NN / -- |

`SCOPE VERIFICATION COMPLETE`

---

```
ACT 1 CLOSE (sign-off)
(1) All gates within Act 1 CLOSED:
    Gate 1:                         [CLOSED / OPEN -- reason]
    Gate 1b:                        [CLOSED / N/A]
    Gate 2:                         [CLOSED / OPEN -- reason]
    Gate 2b:                        [CLOSED / OPEN -- reason]
    Gate 3:                         [CLOSED / OPEN -- reason]
    Gate 4:                         [CLOSED / OPEN -- reason]
    GATE N-bypass blocks:           [CLOSED / none triggered]
    Act 1 Registry Audit:           [CLOSED / OPEN -- reason]
    VS Cross-Reference Registry:    [COMPLETE / OPEN -- reason]
    VS Observability Gap Report:    [COMPLETE / OPEN -- reason]
    Bidirectional Chaos-Observability Matrix: [COMPLETE / OPEN -- reason]
(2) Act 1 scope exhausted: [yes / list any unresolved items]
(3) No RULE-BYPASSED conditions remain unresolved within Act 1: [yes / exception detail]
ACT 1 STATUS: CLOSED / OPEN

INDEPENDENCE AUDIT
Gate 2b CLOSE -- two-checkbox independent form (C-42: confirmed).
Gate 1 CLOSE -- two-checkbox independent form (C-43: confirmed).
No further gate CLOSE blocks in this template carry both a positive confirmation clause
and a prohibition clause. Independence scope: COMPLETE.
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
  [ ] All four commerce-domain targets checked (present or rationale)
Gate 5 STATUS: CLOSED / OPEN -- [reason if open]
```

---

### Act 2 Terminal: Post-Analysis Rule Registry Audit

| Rule ID | Invocations | Citations | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-COMMERCE-ANCHOR | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | |

`POST-ANALYSIS REGISTRY AUDIT (ACT 2) COMPLETE`

---

### Inertia Synthesis -- What Does Doing Nothing Cost?

Per-finding carrying cost (from Gate 3): for each named gap, state failure mode, rate, horizon, metric. Include VSOG-NN findings where applicable: monitoring-dark recovery stages represent silent failure risk where the recovery SLA can elapse undetected.

Urgency: HIGH / MEDIUM / LOW
Highest-risk finding: [gap ID] -- [carrying cost]
Status-quo option: [what "do nothing" looks like for `{topic}` specifically]
Intervention recommendation: [owner + threshold + consequence of missing threshold]

```
ACT 2 CLOSE (sign-off)
(1) All gates within Act 2 CLOSED:
    Gate 5:                [CLOSED / OPEN -- reason]
    GATE 5-bypass blocks:  [CLOSED / none triggered]
    Act 2 Registry Audit:  [CLOSED / OPEN -- reason]
(2) Act 2 scope exhausted: [yes -- all scenarios commerce-anchored; all CV targets
    checked; inertia synthesis complete including VSOG-NN monitoring-dark findings]
(3) No RULE-BYPASSED conditions remain unresolved: [yes / exception detail]
ACT 2 STATUS: CLOSED / OPEN
```

`ANALYSIS COMPLETE` (declared only when ACT 1 STATUS: CLOSED AND ACT 2 STATUS: CLOSED)

---

---

## Expected R17 Discrimination Under v16

| Rank | Variation | C-45 | C-46 | C-47 | Uncapped |
|------|-----------|------|------|------|---------|
| 1 (tie) | **V-02** | PASS | PASS | PASS | 78/78 |
| 1 (tie) | **V-03** | PASS | PASS | PASS | 78/78 |
| 1 (tie) | **V-04** | PASS | PASS | PASS | 78/78 |
| 4 | **V-01** | FAIL | PASS | PASS | 76/78 |
| — | **V-05** | PASS | PASS | PASS | 78/78 + C-48 cand. |

**V-05 position**: Maintains 78/78 under v16. C-48 candidate (VS Observability Gap Report) is not scoreable under v16 -- it would require extraction into a new criterion in v17 if the signal is confirmed novel and orthogonal.

**Three-way tie at 78/78 (V-02/V-03/V-04)**: All crack C-47 via different construction paths. Under v16 they are indistinguishable at uncapped ceiling. If V-05's VSOG-NN pattern is extracted as C-48 in v17, V-05 alone would hold 80/80; all others would remain at 78/80 (C-48 FAIL).

**Open for R18**: C-47 already universal PASS (under this model); C-48 PASS for V-01 through V-04 if V-05's VS Observability Gap Report is confirmed as C-48; three-way tie at 78/78 among V-02/V-03/V-04 unbroken under v16 (V-02 and V-04 are near-identical at criterion level, differing only in VS registry column layout; if rubric v17 adds a criterion distinguishing split vs. combined Stage Context format, the tie would break). V-01 C-45 FAIL persists -- the Gate Independence Completeness Block has not been added; this remains the next single-axis target for V-01 in R18.

**Orthogonality argument for C-48 (VS Observability Gap Report)**:
- Orthogonal to C-47: C-47 requires the VS registry to contain all VS entries with Observable Signal Refs (can be N/A); C-48 requires N/A entries to be elevated to structured VSOG-NN findings with named dark condition and consequence. C-47 FAIL subsumes C-48.
- Orthogonal to C-44 (bidirectional chaos-observability matrix): C-44 addresses gap findings between chaos scenarios and Observable Signals from Gate 3; C-48 addresses gap findings between recovery stage VS entries and Observable Signals from Gate 3. The former covers chaos test observability; the latter covers recovery completion observability. Both reference Gate 3 signals but from different directions: C-44 asks "does this chaos scenario have a production signal that confirms the fault was detected?"; C-48 asks "does this recovery stage have a production signal that confirms the stage completed?"
- Orthogonal to C-35: C-35 requires named VS to be present in each recovery stage row; C-48 requires the monitoring coverage status of those VS to be reported as structured findings when the VS has no corresponding Gate 3 observable. VS presence (C-35) and VS monitoring coverage (C-48) are independently satisfiable.
