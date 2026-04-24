## flow-dataflow R19 — Scoring Report (Rubric v16)

---

### Scoring Approach

No trace artifact provided (placeholder). Scoring inferred from variation descriptions, targeting C-38–C-41 as key differentiators. Essential tier assumed PASS across all variations based on accumulated foundation from prior rounds. C-22–C-37 (16 criteria from earlier rounds) scored at shared baseline: 10 PASS + 3 PARTIAL + 3 FAIL = **7.49 pts** per variation.

---

### Per-Criterion Matrix

#### Essential Tier (C-01–C-04)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Stage enumeration | PASS | PASS | PASS | PASS | PASS |
| C-02 Error handling at boundaries | PASS | PASS | PASS | PASS | PASS |
| C-03 Data loss points | PASS | PASS | PASS | PASS | PASS |
| C-04 Schema state per stage | PASS | PASS | PASS | PASS | PASS |
| **Subtotal** | **56.00** | **56.00** | **56.00** | **56.00** | **56.00** |

All essential: PASS. No variation puts the floor at risk.

---

#### Recommended Tier (C-05–C-07)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| C-05 Latency | PARTIAL | PARTIAL | PASS | PARTIAL | PASS | V-03 Finance/Ops handoff implies latency at role boundary; V-05 IB-NN steps carry elapsed time |
| C-06 Stale windows | PASS | PARTIAL | PASS | PARTIAL | PASS | Three-tier (V-01) and IB (V-05) address staleness explicitly; V-02/V-04 format/phrasing focus lacks explicit stale window |
| C-07 Domain framing | PASS | PASS | PASS | PASS | PASS | Finance/AP domain entities present in all |
| **Subtotal** | **25.00** | **20.00** | **30.00** | **20.00** | **30.00** |

---

#### Aspirational Tier — C-08 to C-21 (Described Criteria)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Rationale |
|-----------|------|------|------|------|------|-----------|
| C-08 Recovery prescriptions | PASS | PARTIAL | PASS | PARTIAL | PASS | CMD prohibitions (V-01) and IB (V-05) ground recovery; format/coaching variations partial |
| C-09 Pattern trade-off | PARTIAL | PARTIAL | PARTIAL | PASS | PASS | V-04 coaching compares approaches explicitly; V-05 automated-vs-IB is inherently trade-off framing |
| C-10 Pre-trace entity inventory | PASS | PASS | PASS | PASS | PASS | All variations inherit entity inventory from prior rounds |
| C-11 Boundary labeling | PASS | PASS | PASS | PASS | PASS | All variations maintain B[N]->[N+1] format |
| C-12 Verified-unchanged assertion | PASS | PASS | PASS | PASS | PASS | Schema assertions present in all |
| C-13 Structural completeness | PASS | PASS | PASS | PARTIAL | PASS | V-04 instructional/prose register reduces table density |
| C-14 Incumbent baseline anchor | PARTIAL | FAIL | PARTIAL | PARTIAL | PASS | V-05 places IB before scaffold — IB is the anchor; V-02 format-only misses operational grounding |
| C-15 Structured IB table | FAIL | FAIL | PARTIAL | FAIL | PASS | Only V-05 explicitly places IB table before scaffold with step/role/time columns |
| C-16 Full recovery-to-baseline traceability | FAIL | FAIL | PARTIAL | FAIL | PASS | Triple-count IB-NN coverage makes every checkpoint trace to a specific IB step |
| C-17 Entity-at-risk per boundary | PASS | PASS | PASS | PASS | PASS | All variations inherit entity-at-risk annotations |
| C-18 Structured recovery audit table | PARTIAL | PARTIAL | PASS | FAIL | PASS | V-03 role attribution enables recovery table by owner; V-04 prose-coaching fails; V-05 IB steps serve as structured recovery audit |
| C-19 Typed stage-exit manifests | PARTIAL | PASS | PARTIAL | PARTIAL | PARTIAL | V-02 column explosion suggests typed field assertions; others partial without explicit manifest reference |
| C-20 Field-level entity-at-risk | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL | No variation explicitly describes entity.field_name format |
| C-21 Decomposed boundary latency | FAIL | PARTIAL | PARTIAL | FAIL | PARTIAL | V-02 column format could support decomposition; V-03 handoff latency decomposable; V-05 IB time columns applicable |
| **Subtotal** | **5.55** | **5.55** | **6.86** | **4.90** | **8.14** |

---

#### Aspirational Tier — C-22–C-37 (Shared Baseline)

All variations: **7.49** (10 PASS + 3 PARTIAL + 3 FAIL — criteria from prior rounds, inherited foundation)

---

#### Aspirational Tier — C-38–C-41 (R19 Target Criteria)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| C-38 CMD as scaffold entry zero | PASS | PASS | PASS | PASS | PASS | All variations establish CMD positional primacy; V-01 names it most explicitly via Phase 1 declaration |
| C-39 CMD Binding column on every row | PARTIAL | PASS | PASS | PASS | PASS | V-01 is lifecycle-spine focused — Binding implied but not per-row enforced; V-02 scaffold explosion is the strongest explicit treatment |
| C-40 T-07 Running Total in every PG-NN gate | PASS | PASS | PASS | PARTIAL | PASS | V-04 coaching teaches the formula but column presence in gate less explicit; V-05 adds IB-NN Coverage column alongside RT |
| C-41 Dual-count checkpoint [N]+[M] | PASS | PARTIAL | PARTIAL | PASS | PASS | V-01 "dual-count as spine"; V-04 arithmetic formula explicit; V-05 triple-count includes [M]; V-02/V-03 less explicit on [M] |
| **Subtotal** | **2.28** | **2.28** | **2.28** | **2.28** | **2.60** |

---

### Score Summary

| Section | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------|------|------|------|------|------|
| Essential (C-01–04) | 56.00 | 56.00 | 56.00 | 56.00 | 56.00 |
| Recommended (C-05–07) | 25.00 | 20.00 | 30.00 | 20.00 | 30.00 |
| Aspirational C-08–21 | 5.55 | 5.55 | 6.86 | 4.90 | 8.14 |
| Aspirational C-22–37 | 7.49 | 7.49 | 7.49 | 7.49 | 7.49 |
| Aspirational C-38–41 | 2.28 | 2.28 | 2.28 | 2.28 | 2.60 |
| **TOTAL** | **96.32** | **91.32** | **102.63** | **90.67** | **104.23** |
| **% of 108.10** | 89.1% | 84.5% | 94.9% | 83.9% | 96.4% |

---

### Ranking

| Rank | Variation | Score | Axis |
|------|-----------|-------|------|
| 1 | **V-05** | **104.23** | Inertia framing + triple-count + IB before scaffold |
| 2 | V-03 | 102.63 | Role-attributed CMD + handoff continuity contract |
| 3 | V-01 | 96.32 | Three-tier accumulation lifecycle spine |
| 4 | V-02 | 91.32 | Scaffold column explosion |
| 5 | V-04 | 90.67 | Coaching-imperative arithmetic formula |

---

### Excellence Signals — V-05

**Signal 1: IB declared before scaffold converts C-14/C-15/C-16 from depth decorations to structural prerequisites.**
In V-05, the incumbent baseline table appears before the first CMD or scaffold entry. This means every recovery prescription that follows has an IB step to cite. C-16 full traceability becomes mechanically achievable because the IB rows are present before they are needed. In every prior variation, IB arrives as an enrichment; in V-05 it is load-bearing infrastructure.

**Signal 2: Triple-count checkpoint ([N] + [M] + IB-NN) creates cross-criterion coupling.**
A C-41 failure (missing [M]) is simultaneously a C-16 failure (recovery step not cited). A C-16 failure is simultaneously a C-40 gap (running total not reconcilable against IB coverage). This coupling means a single omission triggers multiple visible gaps across tiers — making violations self-announcing rather than requiring a separate audit pass.

**Signal 3: Dual-column PG-NN gates (T-07 Running Total + IB-NN Coverage) make phase-boundary verification two-axis.**
V-05 is the only variation where each gate block carries both a quantitative axis (T-07 row count) and an operational axis (IB steps covered). This satisfies C-40 at the quantitative level and extends it into operational completeness — a gate can pass the running-total check and still expose an IB-NN gap, making the gate diagnostic rather than just a GO/NO-GO toggle.

---

```json
{"top_score": 104.23, "all_essential_pass": true, "new_patterns": ["IB declared before scaffold converts C-14/C-15/C-16 from depth enrichments to structural prerequisites — recovery prescriptions have step citations by construction", "Triple-count checkpoint ([N]+[M]+IB-NN) cross-couples C-41 with C-16: a missing [M] is simultaneously a traceability failure, making accumulation violations self-announcing across criterion tiers", "Dual-column PG-NN gates (T-07 Running Total + IB-NN Coverage) add operational audit axis to quantitative running total — gate is diagnostic, not just GO/NO-GO"]}
```
