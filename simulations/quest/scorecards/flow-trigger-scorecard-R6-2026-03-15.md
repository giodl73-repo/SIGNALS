## flow-trigger — Round 6 Scorecard (Rubric v3)

---

### Rubric Parameters

| Category | Count | Criteria | Weight |
|----------|-------|----------|--------|
| Essential | 5 | C-01–C-05 | 60 pts |
| Recommended | 3 | C-06–C-08 | 30 pts |
| Aspirational | 8 | C-09–C-16 | 10 pts |

**Golden threshold**: all essential pass AND composite ≥ 80.

---

### V-01 — Execution Position Citation

**Mechanism**: EOR-01–EOR-07 table + `Positioned because: EOR-{NN}` slot mandatory on every firing entry + EOR citation count in closure arithmetic.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Trigger enumeration | PASS | Phase 2b: one entry per C-ID |
| C-02 | Execution order stated | **STRONG PASS** | EOR table declared globally; every firing entry cites the specific EOR rule that places it at its position — ordering is auditable per entry |
| C-03 | Inputs/outputs per trigger | PASS | `Reads:` / `Produces:` / `Writes:` slots in firing entry format |
| C-04 | Three anomaly class verdicts | PASS | Phase 3: exactly three verdict blocks required |
| C-05 | Platform grounding | PASS | Vocabulary contract table; `[NC: {term}]` markers |
| C-06 | Circular trigger analysis | PASS | Directed edge set + back-edge detection in Phase 3 |
| C-07 | Conditional branch paths | PASS | `Condition (EXECUTED)` + `Condition (SKIPPED would be)` slots |
| C-08 | Anomaly remediation proposed | PASS | Remediation field required in every verdict block |
| C-09 | Execution tier and latency flags | PASS | `Execution tier:` + `Latency:` slots |
| C-10 | Cascade completeness | PASS | `Cascades to: Entry #{N}` field triggers child row |
| C-11 | Candidate denominator declared | PASS | `DENOMINATOR: N =` before enumeration |
| C-12 | Gap tokens for non-firers | PASS | `[NOT FIRED — {reason}]` gap entry format |
| C-13 | Anomaly verdict evidence citation | PASS | `Rows inspected:` mandatory in every verdict block |
| C-14 | Scope-closing event gate | PASS | Phase 1 Decomposition Gate with event tuple + `[GATE 1: PASSED]` |
| C-15 | Bilateral counterfactual per entry | PASS | `Flip to NOT FIRE` on firing entries; `Flip to FIRE` on gap entries |
| C-16 | Registration witness | PASS | `Registration witness:` slot + `[UNWITNESSED]` in both entry types |

**Essential pass**: 5/5 | **Recommended pass**: 3/3 | **Aspirational pass**: 8/8

```
composite = (5/5 × 60) + (3/3 × 30) + (8/8 × 10) = 60 + 30 + 10 = 100
```

---

### V-02 — Cascade Depth Register

**Mechanism**: `CASCADE DEPTH BUDGET` declared before enumeration; `[Depth: N/MAX]` counter on every cascade entry; `[DEPTH EXCEEDED]` entry format when chain exceeds budget; storm verdict explicitly checks `DE > 0`.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Trigger enumeration | PASS | Step 3: one entry per C-ID |
| C-02 | Execution order stated | PASS | "Entries ordered by execution tier and sequence" — global statement, no per-entry EOR citation |
| C-03 | Inputs/outputs per trigger | PASS | `Reads:` / `Produces:` / `Writes:` in firing entry format |
| C-04 | Three anomaly class verdicts | PASS | Step 4: three verdict blocks |
| C-05 | Platform grounding | PASS | Vocabulary contract |
| C-06 | Circular trigger analysis | PASS | Directed edge set excluding DEPTH EXCEEDED entries; back-edge detection |
| C-07 | Conditional branch paths | PASS | `Condition (EXECUTED)` + `Condition (SKIPPED would be)` |
| C-08 | Anomaly remediation proposed | PASS | Remediation in verdict format |
| C-09 | Execution tier and latency flags | PASS | `Execution tier:` + `Latency:` slots |
| C-10 | Cascade completeness | **STRONG PASS** | Cascade entry format + `[Depth: N/MAX]` traces chains end-to-end; DEPTH EXCEEDED makes pathological chains structurally visible |
| C-11 | Candidate denominator declared | PASS | `DENOMINATOR: N =` in Step 2 |
| C-12 | Gap tokens for non-firers | PASS | `[NOT FIRED — {reason}]` gap format |
| C-13 | Anomaly verdict evidence citation | PASS | `Rows inspected:` mandatory; storm verdict references depth counters |
| C-14 | Scope-closing event gate | PASS | Step 1a event tuple + `[GATE 1a: PASSED]` |
| C-15 | Bilateral counterfactual per entry | PASS | Both flip directions in entry formats |
| C-16 | Registration witness | PASS | `Registration witness:` slot in all entry types |

**Essential pass**: 5/5 | **Recommended pass**: 3/3 | **Aspirational pass**: 8/8

```
composite = 100
```

---

### V-03 — Scope Exclusion Log

**Mechanism**: Dedicated Role B sweeps all automation layers and produces a named EXCLUSION LOG before the candidate scan; Role D verdict blocks carry an `Exclusion log reference:` field; three-part accounting: (a) excluded layers, (b) in-scope non-firers, (c) firers.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Trigger enumeration | PASS | Role C: one entry per C-ID |
| C-02 | Execution order stated | PASS | "Entries ordered by execution tier and sequence within tier" |
| C-03 | Inputs/outputs per trigger | PASS | `Reads:` / `Produces:` / `Writes:` slots |
| C-04 | Three anomaly class verdicts | PASS | Role D: three verdict blocks |
| C-05 | Platform grounding | PASS | Vocabulary contract |
| C-06 | Circular trigger analysis | PASS | Directed edge set + back-edge detection in Role D |
| C-07 | Conditional branch paths | PASS | `Condition (EXECUTED)` + `Condition (SKIPPED would be)` |
| C-08 | Anomaly remediation proposed | PASS | Remediation in verdict block format |
| C-09 | Execution tier and latency flags | PASS | `Execution tier:` + `Latency:` slots |
| C-10 | Cascade completeness | PASS | `Cascades to: Entry #{N}` field |
| C-11 | Candidate denominator declared | PASS | `DENOMINATOR: N =` in Role C |
| C-12 | Gap tokens for non-firers | PASS | `[NOT FIRED — {reason}]` gap format |
| C-13 | Anomaly verdict evidence citation | **STRONG PASS** | `Rows inspected:` + `Exclusion log reference:` field — verdicts cite both enumeration rows and exclusion log |
| C-14 | Scope-closing event gate | PASS | Role A event tuple + `[GATE A: PASSED]` |
| C-15 | Bilateral counterfactual per entry | PASS | Both flip directions in both entry types |
| C-16 | Registration witness | PASS | `Registration witness:` slot in all entry types |

**Essential pass**: 5/5 | **Recommended pass**: 3/3 | **Aspirational pass**: 8/8

```
composite = 100
```

---

### V-04 — Formal Prescriptive Register Throughout

**Mechanism**: All obligation positions use SHALL/MUST; all prohibition positions use SHALL NOT/PROHIBITED; gate conditions use "SHALL be declared complete when"; descriptive drift produces `[REG FAIL: {clause}]` inline; missing slots produce `[SLOT ABSENT: {slot}]`; missing citations produce `[CITATION ABSENT: ...]`.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Trigger enumeration | PASS | Phase 3: one entry per C-ID mandated by SHALL |
| C-02 | Execution order stated | PASS | "Entries SHALL be ordered by execution tier and sequence within tier" |
| C-03 | Inputs/outputs per trigger | PASS | `Reads:` / `Produces:` / `Writes:` slots; SLOT ABSENT tag enforces presence |
| C-04 | Three anomaly class verdicts | PASS | Phase 4: all three verdict blocks; anomaly register closure table |
| C-05 | Platform grounding | PASS | Vocabulary contract using SHALL language; `[NC: {term}]` markers |
| C-06 | Circular trigger analysis | PASS | "The analyst SHALL construct the directed edge set... SHALL apply back-edge detection" |
| C-07 | Conditional branch paths | PASS | `Condition (EXECUTED)` + `Condition (SKIPPED would be)` slots |
| C-08 | Anomaly remediation proposed | **STRONG PASS** | Detected anomalies require remediation; `[REMEDIATION ABSENT: ...]` tag enforces compliance — structurally cannot omit fix |
| C-09 | Execution tier and latency flags | PASS | `Execution tier:` + `Latency:` slots |
| C-10 | Cascade completeness | PASS | `Cascades to: Entry #{N}` field |
| C-11 | Candidate denominator declared | PASS | `DENOMINATOR: N =` in Phase 2 |
| C-12 | Gap tokens for non-firers | PASS | `[NOT FIRED — {reason}]` gap format |
| C-13 | Anomaly verdict evidence citation | **STRONG PASS** | `Rows inspected:` mandatory; `[CITATION ABSENT: ...]` tag structurally enforces compliance |
| C-14 | Scope-closing event gate | PASS | Phase 1 scope declaration with SHALL-register gate |
| C-15 | Bilateral counterfactual per entry | PASS | `Flip to NOT FIRE` (SHALL NOT be "remove the trigger") + `Flip to FIRE` |
| C-16 | Registration witness | PASS | `Registration witness:` slot; artifact source SHALL be from scenario |

**Essential pass**: 5/5 | **Recommended pass**: 3/3 | **Aspirational pass**: 8/8

```
composite = 100
```

---

### V-05 — Combined: EOR Citation + Cascade Depth + Exclusion Log + R5 Foundations

**Mechanism**: Role A (event tuple + cascade depth budget) → Role B (EXCLUSION LOG) → Role C (manifest + denominator + anomaly register) → Role D (execution with EOR citations + bilateral counterfactuals + depth counters) → Role E (verdicts with exclusion log cross-reference). Five independent structural barriers: (1) scope gate, (2) authority contracts, (3) per-entry EOR citation, (4) cascade depth budget, (5) exclusion log.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Trigger enumeration | PASS | Role D: one entry per C-ID from Role C manifest |
| C-02 | Execution order stated | **STRONG PASS** | EOR table; every firing entry cites `Positioned because: EOR-{NN}`; closure counts EOR citations absent |
| C-03 | Inputs/outputs per trigger | PASS | `Reads:` / `Produces:` / `Writes:` slots in Role D firing format |
| C-04 | Three anomaly class verdicts | PASS | Role E: three verdict blocks + anomaly register closure |
| C-05 | Platform grounding | PASS | Vocabulary contract; `[NC: {term}]` markers |
| C-06 | Circular trigger analysis | PASS | Directed edge set from Role D Cascades-to fields; excludes DEPTH EXCEEDED entries; back-edge detection |
| C-07 | Conditional branch paths | PASS | `Condition (EXECUTED)` + `Condition (SKIPPED would be)` in firing entry format |
| C-08 | Anomaly remediation proposed | PASS | Remediation in verdict block format |
| C-09 | Execution tier and latency flags | PASS | `Execution tier:` + `Latency:` slots |
| C-10 | Cascade completeness | **STRONG PASS** | Cascade depth budget + `[Depth: N/MAX]` counter + `[DEPTH EXCEEDED]` entries — chains traced with numeric gate |
| C-11 | Candidate denominator declared | PASS | `DENOMINATOR: N =` in Role C |
| C-12 | Gap tokens for non-firers | PASS | `[NOT FIRED — {reason}]` gap format; bilateral counterfactual required |
| C-13 | Anomaly verdict evidence citation | **STRONG PASS** | `Rows inspected:` + `Exclusion log note:` in every verdict; two-layer citation (enumeration rows + Role B layers) |
| C-14 | Scope-closing event gate | PASS | Role A Step A1 event tuple + `[GATE A1: PASSED]` |
| C-15 | Bilateral counterfactual per entry | **STRONG PASS** | Both flip directions on every entry type; "remove the automation" explicitly prohibited as counterfactual |
| C-16 | Registration witness | PASS | `Registration witness:` slot in all entry types; `[UNWITNESSED]` flag required |

**Essential pass**: 5/5 | **Recommended pass**: 3/3 | **Aspirational pass**: 8/8

```
composite = 100
```

---

### Composite Score Summary

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | Composite | All Essential |
|-----------|---------------|-----------------|-------------------|-----------|---------------|
| V-01 | 60 | 30 | 10 | **100** | YES |
| V-02 | 60 | 30 | 10 | **100** | YES |
| V-03 | 60 | 30 | 10 | **100** | YES |
| V-04 | 60 | 30 | 10 | **100** | YES |
| V-05 | 60 | 30 | 10 | **100** | YES |

**Observation**: Rubric v3 is saturated. Every R6 variation that carries R5 foundations scores 100. The rubric cannot differentiate R6 variations because the new mechanisms (C-17, C-18, C-19, C-20) are not yet in the scoring formula. The rubric must grow.

---

### Ranking

Since all composite scores are tied at 100, rank by structural completeness and audit depth:

| Rank | Variation | Structural Superiority |
|------|-----------|----------------------|
| 1 | **V-05** | All three R6 mechanisms combined + authority contracts. Five independent structural barriers. Strong passes on C-02, C-10, C-13, C-15. |
| 2 | **V-01** | EOR per-entry citation makes C-02 strongly auditable; strongest answer to ordering verification |
| 3 | **V-03** | Exclusion log gives C-13 the deepest citation (two-layer: rows + excluded layers). Strongest missing-trigger detection |
| 4 | **V-02** | Depth counter makes C-10 numeric. Storm detection improved but no role separation |
| 5 | **V-04** | Strong on C-08 and C-13 enforcement via violation tags. Formal register improves robustness but adds no structural accounting layer |

---

### Excellence Signals from V-05

1. **Five independent structural barriers** — each addresses a distinct failure mode with no overlap: scope gate (false positives), authority contracts (role creep), EOR citations (ordering drift), depth budget (unbounded cascades), exclusion log (unexamined space). The combination is more than additive.

2. **Two-layer anomaly citation** — Role E verdicts cite both Role D entry rows AND Role B exclusion log rows. Missing trigger verdicts can now name "fixable exclusion in Role B" as a finding, not just an absent firing row. C-13 is satisfied at greater depth.

3. **Closure arithmetic covers four entry types** — FR (root firers) + FC (cascade firers) + NF (non-firers) + DE (depth exceeded) + EOR citation counts. The arithmetic is a multi-dimensional health check on the output, not just an F + NF = N check.

4. **Cascade depth converts storm detection from judgment to arithmetic** — `DE > 0` is an objective numeric gate. Prior rounds required the scorer to decide whether a cascade count was "too many." V-05 makes the threshold explicit before enumeration begins.

5. **Authority contracts prevent boundary erosion across rounds** — Role B (exclusion witness) is PROHIBITED from evaluating which candidates fire; Role D is PROHIBITED from adding verdicts; Role E is PROHIBITED from adding candidates. This means structural violations are named and locatable, not invisible.

---

### New Patterns Discovered This Round

All three R6 mechanisms survived single-axis testing and integration:

| Pattern | Variation | Predicted Criterion |
|---------|-----------|---------------------|
| Per-entry execution order citation (`Positioned because: EOR-{NN}`) — sequence position independently verifiable at row level without cross-referencing global rule table | V-01, V-05 | C-17 |
| Pre-declared cascade depth budget + per-entry `[Depth: N/MAX]` counter + `[DEPTH EXCEEDED]` flag — converts unbounded cascade detection from subjective count threshold to numeric gate | V-02, V-05 | C-18 |
| Formal EXCLUSION LOG naming every out-of-scope layer with explicit exclusion reason before candidate scan — completes three-part accounting: (a) excluded layers, (b) in-scope non-firers, (c) firers | V-03, V-05 | C-19 |

V-04's formal register (C-20) is a behavioral enforcer rather than a structural accounting mechanism. It strengthens C-08 and C-13 compliance assurance via violation tagging but does not close an accounting gap. Weaker C-20 candidacy than C-17–C-19.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["per-entry EOR citation slot grounds sequence position in a named platform rule making ordering independently verifiable at row level", "pre-declared cascade depth budget with per-entry depth counter converts storm detection from subjective count threshold to numeric gate", "formal exclusion log completes three-part accounting: excluded layers plus in-scope non-firers plus firers"]}
```
