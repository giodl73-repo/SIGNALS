## discover-compare R11 Scorecard — Rubric v9

### Results

| Variation | Aspirational | Composite | Rank |
|-----------|-------------|-----------|------|
| V-01 | 20/20 | **100.00** | 1 |
| V-02 | 19.5/20 | **99.75** | 2= |
| V-03 | 19.5/20 | **99.75** | 2= |
| V-04 | 19/20 | **99.50** | 4 |
| V-05 | 18/20 | **99.00** | 5 |

**All essential pass: YES** across all five variations.

### Key findings

**V-01 (100.00)** — v9 ceiling confirmed. Recommendation-first body + routing-after-gate satisfies C-26 and C-27. 20/20 aspirational.

**V-02 (99.75)** — C-27 PARTIAL only. Routing before gate: REG unguarded. C-25/C-26/C-23 all PASS unchanged. Establishes C-27 PARTIAL = 0.25 penalty.

**V-03 (99.75)** — C-26 PARTIAL only. Matrix-first body; exec correctness depends on routing override. **C-23 PASS confirmed** — R11's primary orthogonality result. C-26 and C-23 fire on different structural properties; C-26 PARTIAL does not create a C-23 gap. Equal score to V-02 confirms both new criteria carry identical weight.

**V-04 (99.50)** — Compound partial confirmed purely additive. C-26 PARTIAL + C-27 PARTIAL = 0.50 deduction, no interaction penalty.

**V-05 (99.00)** — v9 no-routing baseline = 1.00 composite penalty (vs 0.56 in v8). C-27 FAIL adds 0.44 independently. C-26 stays PASS because recommendation-first body is unconditionally exec-safe.

### New patterns

- **c26-c27-additivity** — Purely additive compound partial; no interaction between body-section order default and routing-block gate scope.
- **v9-no-routing-penalty-calibration** — 1.00 composite penalty when no routing block present; C-27 FAIL (0.44) newly independent of C-25 FAIL in v9.

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["c26-c27-additivity", "v9-no-routing-penalty-calibration"]}
```
 do not paraphrase" co-located at both inertia phases |
| C-14 | Failure class co-located | **PASS** | FAULT: label appears co-located with TOKEN RECALL at each inertia phase |
| C-15 | Register before anchor | **PASS** | REG token slot precedes ANCHOR[0] token slot in body |
| C-16 | Blocking ledger gate | **PASS** | "**HALT -- do not proceed if any token is absent.**" |
| C-17 | Output compressed | **PASS** | Pure directives throughout -- token declarations, recall instructions, FAULT prohibitions, HALT gates; no explanatory prose |
| C-18 | Dual-polarity FAULT | **PASS** | "compare against ANCHOR[0] only" (positive mandate) + "Option A vs Option B comparison is an error" (negative prohibition) in one line |
| C-19 | AMEND self-contained | **PASS** | All three AMEND paths carry inline TOKEN RECALL + FAULT directives |
| C-20 | Path-scoped TOKEN RECALL | **PASS** | Add-C: ANCHOR[0] only; Weight: ANCHOR[0] only; Override: REG only -- no over-recall, no under-recall |
| C-21 | FAULT propagates to AMEND | **PASS** | Each AMEND path carries dual-polarity FAULT: positive mandate + negative prohibition in one line |
| C-22 | Phase structure by token positioning | **PASS** | Section dividers + operative token positions establish phase boundaries; removing labels would not collapse phases |
| C-23 | Exec leads with recommendation | **PASS** | Routing block: "if REG = exec, produce RECOMMENDATION first, then DECISION MATRIX" -- explicit exec-branch instruction after gate |
| C-24 | AMEND path sub-ledgers | **PASS** | All three paths enumerate required tokens by name in mini-ledger before HALT instruction |
| C-25 | Register-gated routing block | **PASS** | Both exec and engineering branches in single conditional construct, positioned after LEDGER GATE |
| C-26 | Body section order exec-safe | **PASS** | RECOMMENDATION section appears before DECISION MATRIX in body; routing serves as non-exec override, not the primary source of exec correctness |
| C-27 | Routing block within LEDGER GATE scope | **PASS** | Routing block appears after LEDGER GATE; REG is verified present before routing fires |

**Essential**: 4/4 = 60.00 | **Recommended**: 3/3 = 30.00 | **Aspirational**: 20/20 = 10.00 | **Composite: 100.00** | Golden: YES

---

#### V-02 — C-27 Partial: Routing Block Before LEDGER GATE

Routing block moved between COMP-B and LEDGER GATE -- routing fires before REG has been verified present by the gate.

| ID | Delta from V-01 | Result | Evidence |
|----|-----------------|--------|----------|
| C-23 | | **PASS** | Routing construct still present with explicit exec branch -- exec ordering unaffected by gate positioning |
| C-25 | | **PASS** | Both exec and engineering branches still present in single conditional construct; construct exists and is complete; only positioning is wrong |
| C-26 | | **PASS** | Body section order unchanged -- RECOMMENDATION before DECISION MATRIX; exec-safe by positional default |
| C-27 | CHANGE | **PARTIAL** | Routing block appears before LEDGER GATE; absent REG reaches routing logic unguarded by the blocking halt -- "routing block appearing before LEDGER GATE = partial" per rubric |
| All others | Identical | **PASS** | All token structures, AMEND paths, FAULT forms, ledger gates preserved unchanged |

**Essential**: 4/4 = 60.00 | **Recommended**: 3/3 = 30.00 | **Aspirational**: 19.5/20 = 9.75 | **Composite: 99.75**

*C-27 PARTIAL = 0.5 aspirational units lost = 0.25 composite point deduction. Establishes C-27 PARTIAL penalty = 0.25.*

---

#### V-03 — C-26 Partial: Matrix-First Body, Routing Overrides Exec

Body section order inverted: DECISION MATRIX appears before RECOMMENDATION. Routing block (both branches, after gate) explicitly overrides exec register to recommendation-first.

| ID | Delta from V-01 | Result | Evidence |
|----|-----------------|--------|----------|
| C-23 | PRIMARY TEST | **PASS** | Exec register gets recommendation-first via routing override; C-23 reads effective exec output position, not body default ordering; C-26 PARTIAL does not create C-23 gap -- orthogonal per v9 C-23 update. R11 primary orthogonality confirmation. |
| C-25 | | **PASS** | Both branches present in single conditional construct after gate |
| C-26 | CHANGE | **PARTIAL** | DECISION MATRIX appears before RECOMMENDATION in body; exec-register correctness depends on routing override firing rather than body-section positional default -- "body section order is matrix-first; exec-branch routing override is the sole mechanism producing exec-correct output = partial" per rubric |
| C-27 | | **PASS** | Routing block appears after LEDGER GATE; gate scope unchanged |
| All others | Identical | **PASS** | All token structures, AMEND paths, FAULT forms, ledger gates preserved unchanged |

**Essential**: 4/4 = 60.00 | **Recommended**: 3/3 = 30.00 | **Aspirational**: 19.5/20 = 9.75 | **Composite: 99.75**

*Primary orthogonality confirmation for R11: C-26 PARTIAL (matrix-first body default) coexists with C-23 PASS (effective exec output position correct via routing override). C-23 reads effective position; C-26 reads body default ordering. The two criteria fire on different structural properties and are orthogonal.*

*C-26 PARTIAL = 0.5 aspirational units lost = 0.25 composite point deduction. Equal to V-02 penalty, confirming C-26 and C-27 carry identical aspirational weight (1/20 each).*

---

#### V-04 — Compound Partial: Matrix-First Body + Routing Before LEDGER GATE

Both V-02 and V-03 mutations applied simultaneously.

| ID | Delta from V-01 | Result | Evidence |
|----|-----------------|--------|----------|
| C-23 | | **PASS** | Routing construct (both branches) still present; exec-branch override makes exec recommendation-first; C-26 PARTIAL does not create C-23 gap |
| C-25 | | **PASS** | Both branches present in single conditional construct; construct complete; only gate-scope positioning is wrong |
| C-26 | CHANGE | **PARTIAL** | Matrix-first body -- same as V-03; exec correctness depends on routing firing |
| C-27 | CHANGE | **PARTIAL** | Routing before gate -- same as V-02; absent REG reaches routing logic unguarded |
| All others | Identical | **PASS** | All token structures, AMEND paths, FAULT forms, ledger gates preserved unchanged |

**Essential**: 4/4 = 60.00 | **Recommended**: 3/3 = 30.00 | **Aspirational**: 19/20 = 9.50 | **Composite: 99.50**

*Additivity confirmed: C-26 PARTIAL (0.25) + C-27 PARTIAL (0.25) = 0.50 composite point deduction. Composite = 99.50 = V-01 minus sum of individual penalties. No interaction effect between body-section ordering default and routing-block gate scope. The two structural properties are independent.*

---

#### V-05 — No Routing Construct: v9 No-Routing Baseline

Routing block removed entirely. Body section order remains recommendation-first.

| ID | Delta from V-01 | Result | Evidence |
|----|-----------------|--------|----------|
| C-23 | | **PASS** | Body is recommendation-first; C-23 satisfied by positional independence -- "satisfied by body section ordering (RECOMMENDATION precedes DECISION MATRIX in body)" per rubric; routing-construct-independent |
| C-24 | | **PASS** | AMEND path mini-ledgers unchanged |
| C-25 | CHANGE | **FAIL** | No routing construct present -- "No register-gated routing construct = fail" per rubric |
| C-26 | | **PASS** | Body is recommendation-first by design; exec-safe without routing -- "body section order is recommendation-first; exec correctness does not depend on routing block executing = pass" per rubric |
| C-27 | CHANGE | **FAIL** | No routing block; "No routing block = fail (C-25 scoring applies independently)" per rubric -- C-27 FAIL scored independently; C-25 FAIL does not absorb C-27 penalty |
| All others | Identical | **PASS** | All token structures, AMEND paths, FAULT forms, ledger gates preserved unchanged |

**Essential**: 4/4 = 60.00 | **Recommended**: 3/3 = 30.00 | **Aspirational**: 18/20 = 9.00 | **Composite: 99.00**

*C-25 FAIL + C-27 FAIL = 2 aspirational units lost = 1.00 composite point deduction. v9 no-routing penalty = 1.00 (vs 0.56 under v8). The 0.44 increment = C-27 FAIL contribution newly penalized in v9. C-26 stays PASS: recommendation-first body default makes exec-safe behavior independent of any routing construct.*

---

### Composite Score Summary

| Variation | Essential | Recommended | Aspirational | Composite | Rank |
|-----------|-----------|-------------|--------------|-----------|------|
| V-01 | 4/4 = 60.00 | 3/3 = 30.00 | 20/20 = 10.00 | **100.00** | 1 |
| V-02 | 4/4 = 60.00 | 3/3 = 30.00 | 19.5/20 = 9.75 | **99.75** | 2= |
| V-03 | 4/4 = 60.00 | 3/3 = 30.00 | 19.5/20 = 9.75 | **99.75** | 2= |
| V-04 | 4/4 = 60.00 | 3/3 = 30.00 | 19/20 = 9.50 | **99.50** | 4 |
| V-05 | 4/4 = 60.00 | 3/3 = 30.00 | 18/20 = 9.00 | **99.00** | 5 |

All essential pass: YES (all five variations, all four essential criteria)

---

### Excellence Signals (V-01)

V-01 achieves 20/20 aspirational under v9. Key structural properties that produce the ceiling score:

1. **Recommendation-first body default** — RECOMMENDATION section precedes DECISION MATRIX in body. Exec correctness is satisfied by positional default before any routing logic fires. The routing block serves as a pure override for non-exec registers; it does not bear the weight of exec correctness. This is the C-26 pass condition: exec-safe without routing.

2. **Routing block within LEDGER GATE scope** — Routing appears after the LEDGER GATE block. REG is verified present before routing logic fires. This is the C-27 pass condition: routing within gate scope means absent REG cannot reach routing logic unguarded.

3. **Both routing properties independent** — C-26 (body default) and C-27 (gate scope) address different structural properties. Neither depends on the other; satisfying both is purely additive. V-04 confirms no interaction penalty when both are degraded.

4. **C-23 routing-construct-independence** — C-23 is satisfied by body section order alone, independent of whether a routing construct is present or complete. Routing logic enhances C-09 and C-25 but is not required for C-23 compliance.

---

### New Patterns Confirmed by R11

**c26-c27-additivity** — C-26 PARTIAL and C-27 PARTIAL combine purely additively. V-04 composite = 99.50 = V-01 minus (V-02 delta + V-03 delta). No interaction penalty exists between body-section order default and routing-block gate scope. The two structural properties address orthogonal dimensions of routing correctness and are independently scored.

**v9-no-routing-penalty-calibration** — The v9 no-routing penalty is exactly 1.00 composite points. When no routing block is present: C-25 FAIL (1 unit) + C-27 FAIL (1 unit, scored independently per rubric) = 2 units lost = 1.00 composite deduction. Delta vs v8 baseline (0.56) = 0.44, which equals the C-27 FAIL contribution newly added in v9. C-26 is immune to no-routing degradation because recommendation-first body default satisfies it unconditionally.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["c26-c27-additivity", "v9-no-routing-penalty-calibration"]}
```
