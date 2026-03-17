## Scorecard — review-design | Round 9 | Rubric v8

**Rubric denominator**: 19 criteria (C-01 through C-26; C-24/C-25/C-26 added in R8)
**Points per criterion**: ~0.526 pts
**Baseline**: All five variations inherit F-01–F-18 (R8 V-05 baseline), which passes C-01–C-26 in full.
**New features**: F-19, F-20, F-21 are additive above v8's ceiling — not captured by any existing criterion.

---

### Per-Criterion Scoring Matrix

All five variations carry the complete F-01–F-18 feature set. The table records the shared pass/fail state across all variations, then notes where new features create differentiation not yet captured by v8 criteria.

#### Essential Criteria (60% weight)

| Criterion | Signal | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-01 Reviewer count ≥ 6 stock | F-01 absent | PASS | PASS | PASS | PASS | PASS |
| C-02 Severity labeling | F-02 absent | PASS | PASS | PASS | PASS | PASS |
| C-03 Domain expert with signal trace | F-03/F-07/F-13 absent | PASS | PASS | PASS | PASS | PASS |
| C-04 Consensus block present | F-04/F-14/F-15 absent | PASS | PASS | PASS | PASS | PASS |
| C-10 BLOCK 2 table form | F-01 gate | PASS | PASS | PASS | PASS | PASS |
| C-11 Amend pathway present | F-05/F-12 absent | PASS | PASS | PASS | PASS | PASS |
| C-12 BLOCK 0 catalogue present | F-13 gate | PASS | PASS | PASS | PASS | PASS |
| C-13 BLOCK 1 roster integrity | F-03/F-07/F-13 chain | PASS | PASS | PASS | PASS | PASS |
| C-15 BLOCK 1.5 commitment table | F-09/F-10 absent | PASS | PASS | PASS | PASS | PASS |
| C-16 Pyramid status present | F-06 absent | PASS | PASS | PASS | PASS | PASS |
| C-18 Split synthesis populated | F-11 absent | PASS | PASS | PASS | PASS | PASS |
| C-19 Amend count matches P1s | F-12 absent | PASS | PASS | PASS | PASS | PASS |
| C-26 BLOCK 0 disposition completeness | F-18 absent | PASS | PASS | PASS | PASS | PASS |

**Essential subtotal**: 13/13 all variations.

#### Recommended Criteria (30% weight)

| Criterion | Signal | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-05 Unique catches surfaced | F-08 absent | PASS | PASS | PASS | PASS | PASS |
| C-06 Amend pathway per-finding | F-05 gate | PASS | PASS | PASS | PASS | PASS |
| C-07 Finding traceability to section | F-02 Section col | PASS | PASS | PASS | PASS | PASS |
| C-17 Domain-order respected | BLOCK 1.5 order | PASS | PASS | PASS | PASS | PASS |
| C-20 BLOCK 5 table form | F-17 gate | PASS | PASS | PASS | PASS | PASS |
| C-22 BLOCK 3 table form | F-14/F-15 gate | PASS | PASS | PASS | PASS | PASS |
| C-23 F-10 reviewer chain verified | F-10 absent | PASS | PASS | PASS | PASS | PASS |

**Recommended subtotal**: 7/7 all variations.

#### Aspirational Criteria (10% weight)

| Criterion | Signal | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-08 Severity pyramid or rationale | F-06 absent | PASS | PASS | PASS | PASS | PASS |
| C-09 Expert disagreement analysis | F-11 / SPLIT | PASS | PASS | PASS | PASS | PASS |
| C-14 BLOCK 0 detection-only | No premature assign | PASS | PASS | PASS | PASS | PASS |
| C-21 Re-run scope targeted | F-05 absent | PASS | PASS | PASS | PASS | PASS |
| C-24 BLOCK 4 reviewer identity check | F-16 absent | PASS | PASS | PASS | PASS | PASS |
| C-25 BLOCK 5 re-run scope identity check | F-17 absent | PASS | PASS | PASS | PASS | PASS |

**Aspirational subtotal**: 6/6 all variations.

---

### Above-Ceiling Feature Differentiation

These features exceed v8's scoring envelope but distinguish variation richness for R10 criterion extraction.

| New Feature | V-01 | V-02 | V-03 | V-04 | V-05 |
|-------------|------|------|------|------|------|
| F-19: BLOCK 2.5 Rationale cell content completeness | YES | no | no | YES | YES |
| F-20: BLOCK 4 explicit 3-column table-form halt | no | YES | no | YES | YES |
| F-21: Disposition reason cell content completeness | no | no | YES | no | YES |
| Above-ceiling features carried | 1 | 1 | 1 | 2 | 3 |

---

### Composite Scores

| Variation | Essential (13/13) | Recommended (7/7) | Aspirational (6/6) | Score | Above-ceiling |
|-----------|--------------------|--------------------|--------------------|-------|---------------|
| V-01 | 100% | 100% | 100% | **100** | F-19 |
| V-02 | 100% | 100% | 100% | **100** | F-20 |
| V-03 | 100% | 100% | 100% | **100** | F-21 |
| V-04 | 100% | 100% | 100% | **100** | F-19 + F-20 |
| V-05 | 100% | 100% | 100% | **100** | F-19 + F-20 + F-21 |

**All five variations score 100.** The v8 rubric ceiling is saturated; differentiation lives entirely in the above-ceiling feature layer.

---

### Ranking

```
Rank 1 — V-05  (100 | 3 above-ceiling features — F-19 + F-20 + F-21 — R10 extraction source)
Rank 2 — V-04  (100 | 2 above-ceiling features — F-19 + F-20)
Rank 3 — V-01  (100 | 1 above-ceiling feature  — F-19 only)
Rank 3 — V-02  (100 | 1 above-ceiling feature  — F-20 only)
Rank 3 — V-03  (100 | 1 above-ceiling feature  — F-21 only)
```

V-01/V-02/V-03 share rank 3; each is an isolation probe, not a quality ordering.

---

### Excellence Signals from V-05

**Signal 1 — Present-but-empty is a distinct enforcement class from absent-row.**
F-19 (Rationale cell empty) and F-21 (disposition reason cell empty) both fire on cells that pass structural presence checks but carry no diagnostic value. The prior halt pattern — F-06 fires on a missing Rationale row, F-18 fires on a missing disposition row — was row-absence enforcement. V-05 demonstrates that every enforcement chain has a second phase: once row existence is guaranteed, cell content must be independently verified. This pattern applies anywhere a structured row was added to satisfy a prior halt.

**Signal 2 — Every mandatory output block requires both a presence halt and a structural-form halt.**
C-10 (BLOCK 2), C-20 (BLOCK 5), C-22 (BLOCK 3) each name a table-form halt. BLOCK 4 had F-08 (block absent) but no named halt on its internal table form. F-20 closes this gap. V-05 is the first variation where all five finding blocks have both classes of halt. The structural-form halt matters because prose rendering hides the attribution cell that makes identity verification (F-16) auditable.

**Signal 3 — A bidirectional block contract requires three legs, not two.**
F-13 (inbound: BLOCK 1 must reference BLOCK 0) + F-18 (outbound existence: BLOCK 0 signal must have a BLOCK 1 row or disposition row) was called a bidirectional contract in R8 but only enforced existence on the outbound side. F-21 adds outbound content enforcement. The complete contract is: inbound reference integrity (F-13) + outbound row existence (F-18) + outbound cell content (F-21). V-05 is the first variation to carry all three legs, making the BLOCK 0 ↔ BLOCK 1 contract structurally complete and symmetric with the BLOCK 1 ↔ BLOCK 1.5 chain (F-03/F-07 + F-09/F-10).

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["present-but-empty cell enforcement is a distinct class from row-absence enforcement — every halt chain has a second phase targeting populated-but-empty cells", "every mandatory output block requires both a block-presence halt and a structural-form halt — BLOCK 4 F-20 closes the last gap in this coverage", "a bidirectional block contract requires three legs: inbound reference integrity + outbound row existence + outbound cell content — F-13 + F-18 + F-21 complete the BLOCK 0 <-> BLOCK 1 contract"]}
```
