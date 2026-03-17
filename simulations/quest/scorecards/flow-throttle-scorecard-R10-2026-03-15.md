## flow-throttle Round 10 — Scoring

### Baseline confirmation

R9 V-05 passes C-01 through C-26 under v10. The two open questions for R10:
- **C-27**: R9 V-05 FAILS — Section B names four exempt types but carries no closure declaration; register is open
- **C-28**: R9 V-05 PASSES — TYPE SCAN GATE annotation has a named "Audit test" field with both compliance-path instruction and gate-absent failure signature

---

### V-01 — C-27 FAIL Isolation

**Axis:** Section B open register (no closure declaration). C-28 Audit test carries from R9 V-05 baseline.

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01 | PASS | TABLE A Binding? = Y + `[prose: item 1]` causal reason |
| C-02 | PASS | TABLE B with Hop column, mechanism values constrained |
| C-03 | PASS | TABLE A multi-tier with Component, Scope, Limit |
| C-04 | PASS | TABLE C source: TABLE A, one row per Tier-ID |
| C-05 | PASS | TABLE D with gap reason column |
| C-06 | PASS | TABLE C: Retry-After present/surfaced/ignored-consequence columns |
| C-07 | PASS | TABLE E Cascade type required; TABLE B backpressure trace |
| C-08 | PASS | TABLE A Limit column requires number+unit |
| C-09 | PASS | TABLE F with Tradeoff column |
| C-10 | PASS | TABLE A Failure mode column: hard rejection / queue saturation / silent drop / degraded throughput / timeout |
| C-11 | PASS | Step 1A SOURCE REGISTER locks source-IDs before any tier |
| C-12 | PASS | GLOBAL CRITERION-COVERAGE STEP present, named dedicated step |
| C-13 | PASS | SOURCE REGISTER appears before Step 1B tier inventory |
| C-14 | PASS | `[prose: item 2 — binding constraint exclusivity]` at Phase 1B exit |
| C-15 | PASS | Named phases (Phase 1/Phase 2) with explicit handoff statements |
| C-16 | PASS | PROHIBITED statements in negative-constraint form with failure mode annotations |
| C-17 | PASS | "For each tier in TABLE A (C-17):" enumeration anchor |
| C-18 | PASS | *prevents retroactive source injection*, *prevents scope creep*, *prevents coverage elision* on all prohibitions/anchors |
| C-19 | PASS | GLOBAL CRITERION-COVERAGE STEP maps C-01 through C-05 by name, per-criterion verdicts |
| C-20 | PASS | Section A PROSE-PERMITTED CONTEXTS: three items, closed list |
| C-21 | PASS | `*(Source: TABLE A. One row per...*` co-located at each derived table |
| C-22 | PASS | TABLE E: Type column with Burst/Cascade/RetryAfter taxonomy, per-type minimum stated |
| C-23 | PASS | `[prose: item N — label]` inline tags at all three prose locations |
| C-24 | PASS | TYPE SCAN GATE: named step, per-category Y/N verdicts, PROCEED/BLOCKED decision |
| C-25 | PASS | Section B names four exempt element types; classification by element type declared |
| C-26 | PASS | Gate Purpose: references C-22, names failure mode (category elision after TABLE F), explains construction-time vs. post-hoc gap; escape route demolisher present |
| **C-27** | **FAIL** | Section B has no closure declaration. Four types listed but register is open — executor encountering unlisted type must classify by content inspection |
| C-28 | PASS | "Audit test (C-28):" named field; compliance path: verify PROCEED/BLOCKED between TABLE E and TABLE F with three verdicts; gate-absent: scan TABLE E after TABLE F complete |

**Composite: 185/190** (C-27 = 0, all others = 5)

---

### V-02 — C-27 Minimal Inline Closure

**Axis:** One closing sentence added: "No other element types are added to this register without revising this contract."

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01–C-26 | PASS | Carries from V-01; all criteria satisfied |
| **C-27** | **PASS** | "No other element types are added to this register without revising this contract." — closure declaration present, states exhaustiveness, states revision requirement. Section B header reads `(C-25, C-27)` |
| C-28 | PASS | Audit test carries from V-01 — inline two-clause form with compliance path and gate-absent signature |

**Composite: 190/190**

Q1 answer confirmed: one closing sentence is sufficient. C-27 is a presence check, not a quality check. The delta from V-01 to V-02 is exactly one sentence.

---

### V-03 — C-28 Two-Path Labeled Audit Test

**Axis:** Audit test expanded into labeled sub-fields; C-27 closure carries from V-02.

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01–C-26 | PASS | Carries from V-02 baseline |
| C-27 | PASS | Closure declaration present: "No other element types are added to this register without revising this contract." |
| **C-28** | **PASS** | Gate annotation has three explicitly labeled fields: *Failure mode prevented*, *Gap above C-22*, **Audit test (C-28)** split into: (a) `Gate-present audit method:` — confirm gate step position, three Y/N verdicts, PROCEED/BLOCKED before TABLE F; (b) `Gate-absent signature:` — TABLE F opens immediately after TABLE E, type completeness is post-hoc scan only. Each path independently scannable. |

**Composite: 190/190**

Q2 answer: V-02 and V-03 both pass C-28 (both have named audit test element with compliance path and absence signature). The labeled form in V-03 is more auditable — each path is independently scannable without parsing compound sentences — but the compliance verdict is identical.

---

### V-04 — Role Sequence + C-27 Inertia Framing

**Axes:** Format Analyst role produces OUTPUT FORMAT CONTRACT (including Section B closure + inertia annotation). Domain Expert bound by contract. Labeled two-path C-28 carries from V-03.

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01–C-26 | PASS | Carries from baseline; Role 2 (Domain Expert) produces all analysis artifacts |
| **C-27** | **PASS** | Closure declaration present. Additionally: inertia annotation "why the register must be closed" demolishes the implicit-complement reasoning: "anything not in prose list is implicitly structured output" → this requires content inspection → reintroduces C-25 problem → closure forecloses content inspection by making unlisted type explicitly unclassified |
| C-28 | PASS | Three-field annotation: labeled `Gate-present audit method:` and `Gate-absent signature:` |

**Note on C-15:** V-04's two-role pipeline (Format Analyst → Domain Expert) satisfies C-15's phase-locked sequencing with stronger structural enforcement than a single-role phase boundary. Format Contract is a precondition, not an instruction.

**Composite: 190/190**

---

### V-05 — Three Roles + Comprehensive C-27 Inertia + C-28 Full Dual-Path

**Axes:** Three-role pipeline (Format Analyst → Domain Expert → Consequence Analyst). C-27 inertia annotation names specific unregistered element examples and the exact problem that reintroduces. C-28 adds named observables in both paths; includes escape route demolisher for C-26.

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01–C-26 | PASS | All carry from baseline; three-role pipeline enforces C-15 architecturally |
| **C-27** | **PASS** | Closure declaration present + comprehensive inertia annotation: names three concrete unregistered element examples (compound gate variant, load-shape verdict label, phase-entry condition banner), explains how each requires content inspection, states that closure converts unlisted type to explicitly unclassified with detectable gap status requiring contract revision auditable by history |
| **C-28** | **PASS** | `Gate-present audit method:` — scan for named gate step between TABLE E/F, confirm three per-category Y/N verdicts, confirm PROCEED/BLOCKED stated before TABLE F. `Gate-absent signature:` — TABLE F opens immediately after TABLE E, distinction stated: "gate present means a missing category blocks TABLE F from opening; gate absent means a missing category is a gap discovered after TABLE F is complete." Plus escape route demolisher for C-26. |

**Composite: 190/190**

---

### Scoring Summary

| Variation | Essential | Recommended | Aspirational | Composite | Rank |
|-----------|-----------|-------------|--------------|-----------|------|
| V-05 | 60 | 30 | 100 | **190/190** | 1 |
| V-04 | 60 | 30 | 100 | **190/190** | 2 |
| V-03 | 60 | 30 | 100 | **190/190** | 3 |
| V-02 | 60 | 30 | 100 | **190/190** | 4 |
| V-01 | 60 | 30 | 95 | **185/190** | 5 |

Rank tie-break (V-02 through V-05 all 190): structural quality gradient. V-05 > V-04 > V-03 > V-02 on C-27 annotation richness, C-28 path specificity, and phase-enforcement architecture.

---

### Excellence Signals from V-05

**Signal 1 — Closed-register inertia demolishes the escape route in place.** The C-27 annotation names the specific wrong-path reasoning ("anything not in the prose-permitted list is implicitly structured output") and explains the causal chain from that reasoning back to content inspection. The executor who would leave the register open is addressed at the exact decision point. Contrast V-02: one sentence states the rule without explaining why an executor would be tempted to violate it.

**Signal 2 — Three-role architecture makes phase ordering a structural precondition, not an instruction.** Format Analyst exit condition (`ROLE 1 COMPLETE`) gates Domain Expert activation. Domain Expert exit condition (`ROLE 2 COMPLETE. The Consequence Analyst activates after the TYPE SCAN GATE below is cleared`) gates Role 3. Out-of-order execution is not discouraged — it is architecturally impossible within the prompt structure.

**Signal 3 — C-28 dual-path with named observables converts annotation into scan task.** V-02's audit test is a compound sentence requiring parsing. V-05's `Gate-present audit method:` and `Gate-absent signature:` are independently scannable labeled fields. The gate-absent path names the specific detectable difference: "gate present means a missing category *blocks* TABLE F from opening; gate absent means a missing category is a *gap discovered after TABLE F is complete*" — a distinction an auditor can verify without knowing the rubric.

**Signal 4 — Escape route demolishment at multiple levels.** V-05 carries escape routes for both C-26 ("the gate Purpose annotation is redundant because C-22 already explains why type coverage matters") and C-27 ("non-prose is the complement of the prose list"). Each demolisher is co-located with the element it defends, making the reasoning auditable without cross-referencing the rubric. The pattern: anticipate the most likely wrong-path inference and demolish it at the decision point.

---

```json
{"top_score": 190, "all_essential_pass": true, "new_patterns": ["closed-register declaration converts open exemption enumeration into formally bounded set — unlisted types are explicitly unclassified rather than implicitly exempt, making additions require auditable contract revision", "inertia annotation for register closure names the specific escape-route reasoning (implicit complement of prose list = structured output) and demolishes it in place, converting closure from a rule to a self-defending constraint", "dual-path labeled audit test with named observables splits gate verification into independently scannable compliance-path and gate-absent-signature fields, converting annotation from rationale statement into two-step scan task"]}
```
