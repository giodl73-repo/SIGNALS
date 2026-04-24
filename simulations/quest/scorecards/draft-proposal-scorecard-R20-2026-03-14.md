## Round 20 — draft-proposal Scoring

### Scoring Framework
Formula: `(E/4×60) + (R/3×30) + (A/42×10)`
All variations share the same golden scaffold for E-01..E-04, R-01..R-03, C-01..C-44. Differentiation is purely in C-45..C-49.

---

## V-01 — C-48 FAIL (independent)

**Axis**: Phrasing register · T-46 CONDITION abstract, T-47 golden

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| E-01..E-04 | PASS | Role sequence declared, options anatomy complete, comparison matrix present, recommendation with qualifying conditions |
| R-01..R-03 | PASS | Risk register with P/I/P×I, prerequisites verified, finalization complete |
| C-01..C-07 | PASS | All structural mandatory criteria met |
| C-08..C-44 | PASS | All aspirational criteria through T-40 chain met — T-40 carries full Part 1 + explanation + Part 2 |
| C-45 | PASS | T-42 CONDITION carries Part 1 exemplar (deficient T-40 form quoted with explanation-of-abstractness) |
| C-46 | PASS | T-42 CONDITION carries Part 2 correct-format prescription |
| C-47 | PASS | T-42 Part 1 includes explanation-of-abstractness language |
| **C-48** | **FAIL** | T-46 CONDITION reads "fires if T-42 CONDITION lacks correct-format prescription showing what a passing T-40 CONDITION entry looks like — Part 2: a quoted or paraphrased exemplar..." — category-only; no inline exemplar quoting a T-42 CONDITION with Part 1 labeled/present and Part 2 absent |
| C-49 | PASS | T-47 CONDITION carries golden inline exemplar: quotes the exemplar-without-explanation T-42 state with "(C-45 PASS)" pass-state annotation and explicit explanation of why the quoted form is abstract |
| C-24 | PASS | Spec declares T-01..T-49, exactly 49 rows |

**Fails: 1 (C-48)** · A = 41/42
**Score: (4/4×60) + (3/3×30) + (41/42×10) = 60 + 30 + 9.762 = 99.76**

---

## V-02 — C-49 FAIL (independent)

**Axis**: Output format · T-47 CONDITION abstract, T-46 golden

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| E-01..E-04 | PASS | Identical golden scaffold |
| R-01..R-03 | PASS | |
| C-01..C-44 | PASS | T-40 and T-42 both fully specified with Part 1 + explanation + Part 2 |
| C-45 | PASS | T-42 Part 1 exemplar present |
| C-46 | PASS | T-42 Part 2 prescription present |
| C-47 | PASS | T-42 Part 1 includes explanation-of-abstractness |
| C-48 | PASS | T-46 CONDITION carries golden inline exemplar: 'Part 1 — Failure exemplar with explanation: A deficient T-40 CONDITION entry reads: "fires if Phase 9b Domain 2 per-column enumeration lacks Risk row: anchor prefix" — abstract because...' `[END — no Part 2 label and no Part 2 content present]` — explicit terminal marker delineating Part-1-present-Part-2-absent state |
| **C-49** | **FAIL** | T-47 CONDITION reads "fires if T-42 CONDITION exemplar lacks explanation of why the quoted deficient T-40 CONDITION form is abstract — Part 1 must include both the quoted T-40 form AND an explanation..." — category-only; no inline exemplar quoting a T-42 CONDITION that has exemplar present but explanation absent |
| C-24 | PASS | 49 rows declared |

**Fails: 1 (C-49)** · A = 41/42
**Score: 60 + 30 + 9.762 = 99.76**

---

## V-03 — C-48 + C-49 FAIL (both independent)

**Axis**: Lifecycle emphasis · Both T-46 and T-47 CONDITION abstract

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| E-01..E-04 | PASS | |
| R-01..R-03 | PASS | |
| C-01..C-44 | PASS | T-40 golden; T-42 full Part 1 + explanation + Part 2 |
| C-45 | PASS | T-42 Part 1 exemplar present |
| C-46 | PASS | T-42 Part 2 prescription present |
| C-47 | PASS | T-42 Part 1 carries explanation-of-abstractness |
| **C-48** | **FAIL** | T-46 CONDITION abstract — "fires if T-42 CONDITION lacks correct-format prescription showing what a passing T-40 CONDITION entry looks like — Part 2: a quoted or paraphrased exemplar..."; no inline exemplar of Part-1-only T-42 state |
| **C-49** | **FAIL** | T-47 CONDITION abstract — "fires if T-42 CONDITION exemplar lacks explanation of why the quoted deficient T-40 CONDITION form is abstract — Part 1 must include both the quoted T-40 form AND an explanation..."; no inline exemplar of exemplar-without-explanation T-42 state |
| C-24 | PASS | 49 rows declared |

**Note**: C-48 and C-49 co-fail with no cascade between them. C-45 PASS, C-46 PASS, C-47 PASS confirm cascade root is clean. T-48 and T-49 rows are present in the 49-row table, correctly describing the C-48/C-49 conditions, but their CONDITION cells (T-46 and T-47 respectively) are abstract.

**Fails: 2 (C-48, C-49)** · A = 40/42
**Score: 60 + 30 + 9.524 = 99.52**

---

## V-04 — C-24 + C-49 FAIL (independent, different root)

**Axis**: Role sequence + inertia framing · Stale 47-row count + T-47 CONDITION abstract

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| E-01..E-04 | PASS | |
| R-01..R-03 | PASS | |
| C-01..C-23 | PASS | |
| **C-24** | **FAIL** | Spec declares "T-01..T-47 — exactly 47 rows"; T-24 checks `!= 47`; LLM generates 47-row table. Rubric v20 requires exactly 49 rows (one per C-01..C-49). T-48 and T-49 rows are absent from the generated table |
| C-25..C-44 | PASS | T-40 golden; T-42 full Part 1 + explanation + Part 2 |
| C-45 | PASS | T-42 Part 1 exemplar present |
| C-46 | PASS | T-42 Part 2 prescription present |
| C-47 | PASS | T-42 Part 1 carries explanation-of-abstractness |
| C-48 | PASS | T-46 CONDITION (within the 47-row table) carries golden inline exemplar of Part-1-only T-42 state, including `[END — no Part 2 label and no Part 2 content present]` terminal marker. T-46 exists in the 47-row table and is golden — C-48 evaluates against T-46's CONDITION content independent of row count |
| **C-49** | **FAIL** | T-47 CONDITION abstract — category-only, no inline exemplar of exemplar-without-explanation T-42 state |

**Note**: C-24 FAIL and C-49 FAIL are independent. The stale count prevents T-48/T-49 trigger rows from existing, but C-49 fires for T-47's CONDITION content. C-48 passes because T-46 exists in the 47-row table with golden content — the row-count failure is orthogonal to T-46's CONDITION cell quality.

**Fails: 2 (C-24, C-49)** · A = 40/42
**Score: 60 + 30 + 9.524 = 99.52**

---

## V-05 — C-45 cascade root → C-46 + C-47 + C-48 + C-49

**Axis**: Phrasing register + lifecycle emphasis · T-42 CONDITION fully abstract

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| E-01..E-04 | PASS | |
| R-01..R-03 | PASS | |
| C-01..C-44 | PASS | T-40 fully specified with Part 1 + explanation + Part 2; C-42, C-43, C-44 all PASS — cascade root isolated at T-42 |
| **C-45** | **FAIL** | T-42 CONDITION reads "fires if T-40 CONDITION lacks inline failure exemplar showing what an abstract-only T-38 CONDITION entry looks like" — category-only, no Part 1 exemplar, no explanation, no Part 2 |
| **C-46** | **FAIL** | Cascade from C-45: no exemplar in T-42 CONDITION means no prescription target can exist |
| **C-47** | **FAIL** | Cascade from C-45: no exemplar means no explanation-of-abstractness can exist |
| **C-48** | **FAIL** | Cascade from C-45: fully abstract T-42 CONDITION (no Part 1 at all) makes the Part-1-present-Part-2-absent state that T-46's exemplar must show structurally unreachable |
| **C-49** | **FAIL** | Cascade from C-45: fully abstract T-42 CONDITION (no exemplar at all) makes the exemplar-present-explanation-absent state that T-47's exemplar must show structurally unreachable |
| C-24 | PASS | Spec declares T-01..T-49, 49 rows |

**Note**: T-46 and T-47 CONDITION cells are also abstract in V-05, but this is analytically consistent with cascade — C-48 and C-49 would fail via cascade from C-45 regardless of T-46/T-47 CONDITION quality. The cascade root is clean (T-40 is fully specified, C-42/C-43/C-44 all PASS).

**Fails: 5 (C-45, C-46, C-47, C-48, C-49)** · A = 37/42
**Score: 60 + 30 + 8.810 = 98.81**

---

## Composite Summary

| Variation | Designed Fails | A Passed | Composite | Rank |
|-----------|----------------|----------|-----------|------|
| **V-01** | C-48 | 41/42 | **99.76** | **1 (tied)** |
| **V-02** | C-49 | 41/42 | **99.76** | **1 (tied)** |
| V-03 | C-48, C-49 | 40/42 | 99.52 | 3 (tied) |
| V-04 | C-24, C-49 | 40/42 | 99.52 | 3 (tied) |
| V-05 | C-45→cascade | 37/42 | 98.81 | 5 |

---

## Excellence Signals — V-01 and V-02 (top scorers, 99.76)

**Signal 1: `[END — no Part 2 label and no Part 2 content present]` terminal marker** (V-02's golden T-46 CONDITION)

V-02's T-46 carries: `'Part 1 — Failure exemplar with explanation: A deficient T-40 CONDITION entry reads: "fires if Phase 9b Domain 2 per-column enumeration lacks Risk row: anchor prefix" — abstract because it names the Domain 2 format requirement without quoting a deficient T-38 form.' [END — no Part 2 label and no Part 2 content present]`

The `[END...]` bracket is a new precision device. It explicitly marks where Part 1 terminates and asserts that no Part 2 follows — making the Part-1-present-Part-2-absent boundary unambiguous for an LLM reading the spec. Prior rounds described this state discursively; R20 introduces the terminal marker as a first-class structural signal.

**Signal 2: `(C-45 PASS)` pass-state annotation within exemplar text** (V-01's golden T-47 CONDITION)

V-01's T-47 carries the inline exemplar concluding with: `— this T-42 CONDITION has a quoted deficient T-40 form (C-45 PASS) but no explanation of why that T-40 form is abstract`

The `(C-45 PASS)` parenthetical is a self-documenting cascade annotation: it names the criterion that passes within the exemplar construct itself, making the cascade boundary readable without rubric consultation. The reviewer (or LLM) can see at the exemplar site which prior criterion's pass condition is satisfied and which is absent.

**Design principle confirmed by both top scorers**: The 99.76 ceiling for single-axis variations is reached by keeping the complementary new criterion's trigger golden while degrading only the target. V-01 upgrades T-47 to carry C-49's proof; V-02 upgrades T-46 to carry C-48's proof. The discipline of "upgrade the non-target, degrade only the target" is what separates 99.76 from 99.52.

---

```json
{"top_score": 99.76, "all_essential_pass": true, "new_patterns": ["[END — no Part 2 label and no Part 2 content present] terminal marker in T-46 CONDITION exemplar explicitly delineates the Part-1-present-Part-2-absent boundary as a first-class structural signal", "(C-45 PASS) pass-state annotation within T-47 exemplar text makes cascade precondition self-documenting at the exemplar site without requiring rubric consultation"]}
```
