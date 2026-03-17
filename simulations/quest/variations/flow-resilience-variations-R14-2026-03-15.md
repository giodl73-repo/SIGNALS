      each scenario, verbatim — not a derivative
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

**Observable Signal requirement**: Every named finding must carry three components:
(1) named signal — specific metric name, log pattern, trace attribute, or alert condition;
(2) detection horizon — concrete time window from gap onset to signal firing;
(3) rationale sentence — why this signal surfaces the gap before user impact.
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

Inadequate/undefined resolution: invoke RULE-CR-DCV; emit DCV-CR-NN.
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
| RULE-CHAOS-INJECT | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | [empty or bypass trigger] |
| RULE-OBS-GAP | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | [empty or bypass trigger] |
| RULE-ROSTER-MISMATCH | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | [empty or trigger citation] |

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

This matrix is a required Act 1 Terminal artifact. Both direction tables and both GAP
REGISTRY blocks must be complete before COMPLETE can be declared. Absence is an Act 1
CLOSE blocker.

**Part A — Forward Direction: Chaos Scenario → Observable Signal**

For each chaos row in Gate 2b, identify the Observable Signal ID(s) from Gate 3. If no
signal is linked, mark the row DARK.

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

## R14 Discrimination Summary

**Predicted scores under v14** (36 criteria, uncapped max 72, cap 10):

| Rank | Variation | C-42 | C-43 | C-44 | E-31 (v15 candidate) | Uncapped |
|------|-----------|------|------|------|----------------------|---------|
| 1 | **V-04** | PASS | PASS | PASS | FAIL | **72/72** |
| 1 | **V-05** | PASS | PASS | PASS | PASS | **72/72** |
| 3 | **V-01** | PASS | PASS | FAIL | FAIL | **70/72** |
| 4 | **V-02** | PASS | PASS | FAIL | FAIL | **69/72** |
| 5 | **V-03** | PASS | FAIL | PASS | FAIL | **67/72** |

**V-04 vs V-05 tie at 72/72** under v14. Discrimination axis for v15: E-31 (Roster Impossibility
Forward-Pass). V-05 carries ROSTER-IMP-NN assignment in Coverage Accountability Roster,
`Roster Reference:` field in Argued-Impossible template, `RULE-ROSTER-MISMATCH` in Rule
Registry, and the third Gate 1 CLOSE postcondition (`Roster reference confirmed`). None of
these appear in V-04.

**V-01 vs V-02** (70 vs 69): differ by one non-C-42/43/44 criterion — V-01 R13 base scores
higher on C-15/C-36/C-38 cluster than V-02 R13 base. The two-point gap survives R14 structural
additions because neither V-01 nor V-02 R14 alters those upstream criteria.

**V-03** (67/72): C-43 still FAIL — Gate 1 CLOSE retains the abbreviated combined form from
V-03 R13. C-42 now PASS; C-44 carried from V-03 R13. Tests whether the C-42 split is equally
detectable in a context where C-43 is absent vs. present (comparison with V-01/V-02).

**Open for R15**: E-31 PASS for V-01/V-02/V-03/V-04 (Roster Forward-Pass absent in all);
C-43 PASS for V-03 (combined Gate 1 CLOSE form); any structural novelty introduced when
V-05's E-31 pattern is formalized as a rubric criterion.

---

*Written to `simulations/quest/golden/flow-resilience-variate-R14-2026-03-15.md`*
