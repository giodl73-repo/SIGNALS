## flow-throttle Round 13 — Scorecard

### Rubric Summary
- **Essential** (C-01–C-05): 12 pts each = 60
- **Recommended** (C-06–C-08): 10 pts each = 30
- **Aspirational** (C-09–C-36): 5 pts each = 140
- **Max**: 230 | **Threshold**: all essential PASS + composite ≥ 80

---

## Per-Variation Scoring

### V-01 — Single-Role Baseline Carry

| Band | Criteria | Status | Pts |
|------|----------|--------|-----|
| Essential | C-01–C-05 | All PASS — tables present, binding tier identified, backpressure traced, UX rows, burst path | 60 |
| Recommended | C-06–C-08 | All PASS — retry-after, cascade, numeric thresholds carried from baseline | 30 |
| Aspirational C-09–C-17 | C-09–C-17 | All PASS | 45 |
| C-18 | Constraint-purpose annotation | PASS — enumeration anchor at Phase 2 entry carries "— *prevents coverage elision; a tier absent from a derived table produces a detectable T-NN count gap*" | 5 |
| C-19–C-34 | All aspirational | All PASS — global coverage step, prose declaration, register, gate annotation, escape-route demolisher, field-count header, observable count declarations | 80 |
| **C-35** | Format-contract phase lock | **FAIL** — single-role form; format contract is an inline section headed "OUTPUT FORMAT CONTRACT," not a role deliverable; no FORMAT CONTRACT COMPLETE at any handoff boundary; a downstream instruction change could silently override the field-count header without producing a detectable structural violation | 0 |
| **C-36** | Role-boundary observable-count declaration | **FAIL** — count labels ("Gate-present audit method — 5 observables:" and "Gate-absent signature — 1 observable:") appear as path identifiers inside the TYPE SCAN GATE body; no consequence-phase role exists; no role-activation boundary carries these counts as entry conditions; their absence would be a rubric-scan finding, not a role-activation failure | 0 |

**V-01 composite: 220 / 230**

---

### V-02 — FORMAT CONTRACT COMPLETE at Phase Boundary (C-35 axis only)

| Band | Criteria | Status | Pts |
|------|----------|--------|-----|
| Essential | C-01–C-05 | All PASS | 60 |
| Recommended | C-06–C-08 | All PASS | 30 |
| C-09–C-17 | All PASS | All PASS | 45 |
| C-18 | Constraint-purpose annotation | PASS — Phase 2 enumeration anchor carries "— *prevents coverage elision*"; all prohibitions carry annotations | 5 |
| C-19–C-34 | All PASS | Carried intact from V-01/baseline | 80 |
| **C-35** | Format-contract phase lock | **PASS** — Phase 0 is a named FORMAT CONTRACT phase producing Section A and Section B; it terminates with "FORMAT CONTRACT COMPLETE" before Phase 1 opens; the contract is a phase deliverable sealed at the boundary; omitting FORMAT CONTRACT COMPLETE is a phase-handoff violation detectable by structural analysis, not a rubric scan | 5 |
| **C-36** | Role-boundary observable-count declaration | **FAIL** — count labels remain inside the TYPE SCAN GATE body as path-identifier text ("Gate-present audit method — 5 observables:"); the merged Phase 1+Phase 2+Gate execution context has no separate Consequence Analyst role; no activation boundary carries the counts as entry conditions | 0 |

**V-02 composite: 225 / 230**

---

### V-03 — Consequence-Role Activation Conditions (C-36 axis only)

| Band | Criteria | Status | Pts |
|------|----------|--------|-----|
| Essential | C-01–C-05 | All PASS | 60 |
| Recommended | C-06–C-08 | All PASS | 30 |
| C-09–C-17 | All PASS | All PASS | 45 |
| **C-18** | Constraint-purpose annotation | **FAIL** — Role 1's Phase 2 enumeration anchor reads "**For each tier in TABLE A (C-17):** every downstream derived table must include a row for every T-NN. Coverage verifiable by T-NN count match against TABLE A." The annotation is absent; "coverage verifiable by T-NN count match" states the verification method, not the failure mode prevented (coverage elision). Compare V-01/V-02 which both carry "— *prevents coverage elision*" on the same anchor. C-18 requires every enumeration anchor to carry a co-located annotation naming the failure mode it prevents. | 0 |
| C-19–C-34 | All PASS | Carried intact | 80 |
| **C-35** | Format-contract phase lock | **FAIL** — no Format Analyst role; the OUTPUT FORMAT CONTRACT is an inline section at the top of Role 1 body; no FORMAT CONTRACT COMPLETE statement at any role-handoff boundary; the contract is instructionally present but architecturally unmutated | 0 |
| **C-36** | Role-boundary observable-count declaration | **PASS** — Role 2 ACTIVATION CONDITIONS block at lines 919–937 declares: "gate-present path — 5 observables required before Role 2 opens: (1)–(5)" and "gate-absent path — 1 observable confirms non-activation"; these count declarations are role entry conditions; a missing count is a role-activation failure (Role 2 cannot open without confirming the declared count), not a gate-body formatting gap | 5 |

**V-03 composite: 220 / 230**

> **Scoring deviation from prediction:** Predicted 225/230; scored 220/230. The C-36 gain (+5) is offset by an undetected C-18 regression (–5). The two-role construction relocated the enumeration anchor into Role 1's Phase 2 without carrying the inertia annotation forward from the baseline prompt.

---

### V-04 — Three-Role Pipeline (C-35 + C-36 combined)

| Band | Criteria | Status | Pts |
|------|----------|--------|-----|
| Essential | C-01–C-05 | All PASS | 60 |
| Recommended | C-06–C-08 | All PASS | 30 |
| C-09–C-17 | All PASS | All PASS | 45 |
| C-18 | Constraint-purpose annotation | PASS — Role 2's Phase 2 enumeration anchor reads "**Enumeration anchor — for each tier in TABLE A (C-17):** ... — *prevents coverage elision; a tier absent from a derived table produces a detectable T-NN count gap*"; all prohibitions carry inertia annotations | 5 |
| C-19–C-34 | All PASS | Formal register preserves all annotation content; field-count header, observable count declarations, escape-route demolisher, concrete example all intact | 80 |
| **C-35** | Format-contract phase lock | **PASS** — Role 1 (Format Analyst) produces the complete OUTPUT FORMAT CONTRACT and states "FORMAT CONTRACT COMPLETE" before Role 2 activates; the contract is a formally-declared role deliverable; omitting FORMAT CONTRACT COMPLETE is a role-handoff violation identifiable by structural analysis without reading the contract content | 5 |
| **C-36** | Role-boundary observable-count declaration | **PASS** — Role 3 ACTIVATION CONDITIONS (lines 1295–1314) declare: "Gate-present path — 5 observables required: (1)–(5). A missing observable is a Role 3 activation failure" and "Gate-absent path — 1 observable confirms non-activation"; the count declarations are role entry gates; their absence structurally prevents Role 3 from opening | 5 |

**V-04 composite: 230 / 230**

---

### V-05 — Three-Role Pipeline + Imperative/Terse Register

| Band | Criteria | Status | Pts |
|------|----------|--------|-----|
| Essential | C-01–C-05 | All PASS | 60 |
| Recommended | C-06–C-08 | All PASS | 30 |
| C-09–C-17 | All PASS | All PASS | 45 |
| **C-18** | Constraint-purpose annotation | **FAIL** — Phase 2 enumeration anchor reads: "One row per T-NN in every derived table. Verify T-NN count matches TABLE A before proceeding to each table." No annotation naming the failure mode prevented. The compression dropped the "— *prevents coverage elision*" annotation that V-04 carries. "Verify T-NN count matches TABLE A" states the verification action, not the failure mode (coverage elision) the anchor prevents. C-18 pass condition requires explicit co-located annotation naming the failure mode. | 0 |
| C-19–C-34 | All PASS | C-29/C-30: inertia annotation "3 fields: Failure mode prevented | Gap above C-25 | Concrete example (C-29, C-30)" header and three compressed but complete fields present; C-32: escape-route demolisher present ("Escape route for C-32 — ...Incorrect. C-22 explains the type taxonomy. The Purpose annotation explains why..."); C-33: field-count header present; C-34: "5 observables" and "1 observable" count declarations present in gate body | 80 |
| **C-35** | Format-contract phase lock | **PASS** — Role 1 header: "Produce the OUTPUT FORMAT CONTRACT below. Roles 2 and 3 are bound by it and cannot modify it. State FORMAT CONTRACT COMPLETE when done. Role 2 does not open until FORMAT CONTRACT COMPLETE is stated." FORMAT CONTRACT COMPLETE appears at Role 1 exit. Structural position is identical to V-04; phrasing register change does not affect the handoff-boundary mechanism | 5 |
| **C-36** | Role-boundary observable-count declaration | **PASS** — Role 3 ACTIVATION CONDITIONS: "Gate-present — 5 observables required before Role 3 opens: 1–5. VIOLATION: Role 3 opens without all 5 confirmed = activation failure." "Gate-absent — 1 observable blocks activation." Count declarations at role-activation boundary; same structural mechanism as V-04; terse phrasing does not change the architectural position | 5 |

**V-05 composite: 225 / 230**

> **Scoring deviation from prediction:** Predicted 230/230; scored 225/230. C-35 and C-36 are indeed register-independent (Q3 confirmed for those two criteria). However, register compression silently dropped the C-18 enumeration anchor annotation — the architectural changes for C-35/C-36 did not cause the regression; the compression pass did. C-18 is the precision criterion the terse register failed.

---

## Ranked Results

| Rank | Variation | Composite | C-35 | C-36 | C-18 | Delta vs Predicted |
|------|-----------|-----------|------|------|------|--------------------|
| 1 | **V-04** | **230/230** | PASS | PASS | PASS | On target |
| 2 | V-02 | 225/230 | PASS | FAIL | PASS | On target |
| 2 | V-05 | 225/230 | PASS | PASS | FAIL | -5 (C-18 regression) |
| 4 | V-01 | 220/230 | FAIL | FAIL | PASS | On target |
| 4 | V-03 | 220/230 | FAIL | PASS | FAIL | -5 (C-18 regression) |

---

## Experiment Questions — Results

**Q1 (V-01 vs V-02 — C-35 independent of C-36):** CONFIRMED. FORMAT CONTRACT COMPLETE at a named phase boundary satisfies C-35 (+5 pts) regardless of C-36 status. V-02 = 225; V-01 = 220; delta = +5 = exactly C-35.

**Q2 (V-01 vs V-03 — C-36 independent of C-35):** PARTIALLY CONFIRMED, WITH CONFOUND. C-36 PASS (+5) is architecturally independent of C-35. However, V-03's two-role construction introduced a C-18 regression (–5), netting zero score delta vs V-01. The C-36 gain is real but masked. Clean Q2 comparison requires a V-03 variant with C-18 annotation preserved.

**Q3 (V-04 vs V-05 — register independence for C-35/C-36):** CONFIRMED for C-35 and C-36. FALSIFIED for overall score: V-05 drops C-18 under compression, producing 225 vs V-04's 230. C-35/C-36 are register-independent; C-18 is register-sensitive.

---

## Excellence Signals from V-04

1. **FORMAT CONTRACT COMPLETE at role-handoff seam**: Format Analyst (Role 1) terminates with the contract-closure statement before any domain role activates. The mechanism is structural — the handoff boundary is the enforcement point, not instruction proximity. Downstream roles cannot modify the contract without violating the handoff.

2. **Count declarations as role-activation prerequisites**: Role 3's activation conditions carry the count values before the role body opens. "A missing observable is a Role 3 activation failure" is the architectural enforcement statement — it converts a rubric finding into a structural precondition. The failure mode is detectable at the boundary, not inside Role 3's output.

3. **Formal register preserves C-18 annotation completeness**: V-04's explanatory style retains the inertia annotation on every enumeration anchor and prohibition. The annotation "— *prevents coverage elision; a tier absent from a derived table produces a detectable T-NN count gap*" survives role decomposition because the formal register doesn't trigger compression. V-03 and V-05 both drop this annotation, showing that C-18 is the annotation most vulnerable to role-restructuring and register changes.

---

```json
{"top_score": 230, "all_essential_pass": true, "new_patterns": ["C-18 enumeration anchor annotation is the highest regression risk under role decomposition and register compression — V-03 (new two-role structure) and V-05 (terse compression) both drop the inertia annotation that V-01, V-02, and V-04 preserve, netting zero score gain for V-03 and masking the C-36 architectural win", "Register compression (V-05) achieves C-35+C-36 parity with V-04 structurally but introduces a C-18 annotation regression, making the net score register-dependent through C-18 rather than through C-35 or C-36 — confirms Q3 for the target criteria while revealing a collateral sensitivity"]}
```
