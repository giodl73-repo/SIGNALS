## Scout-Size Round 15 Scorecard

### Evaluation Framework

**Scoring formula** (v15, 31 aspirational):
- Essential: C-01–C-05 (60 pts, 5 criteria)
- Recommended: C-06–C-08 (30 pts, 3 criteria)
- Aspirational: C-09–C-39 (10 pts, 31 criteria: PASS=1, PARTIAL=0.5, FAIL=0)

---

### Essential Criteria (C-01–C-05) — All Variations

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| C-01 Surface area enumerated | PASS | PASS | PASS | PASS | PASS | Named integration point tables with total count present in all |
| C-02 Complexity tier on-scale | PASS | PASS | PASS | PASS | PASS | WRONG examples for MODERATE/3/5; enforced vocabulary in column header |
| C-03 Inertia check present | PASS | PASS | PASS | PASS | PASS | Phase 0 Precondition A workaround + cost direction in all |
| C-04 Confidence level + basis | PASS | PASS | PASS | PASS | PASS | Named confidence basis column in all |
| C-05 Signal boundary respected | PASS | PASS | PASS | PASS | PASS | Precondition B Phase 0 gate structurally enforces this |

**Essential: 5/5 PASS → 60 pts** for all variations.

---

### Recommended Criteria (C-06–C-08) — All Variations

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| C-06 Team-size names specialist types | PASS | PASS | PASS | PASS | PASS | "name the role — 'engineer' alone fails" in column header |
| C-07 Timeline as sprint range | PASS | PASS | PASS | PASS | PASS | N–M format enforced; WRONG shows "4 sprints" fails |
| C-08 Primary complexity driver | PASS | PASS | PASS | PASS | PASS | Named causal factor column |

**Recommended: 3/3 PASS → 30 pts** for all variations.

---

### Aspirational Criteria (C-09–C-39) — Variation-by-Variation

#### V-01 and V-02 (Single-phase; C-38 + C-39 in minimal architecture)

V-01 and V-02 are structurally identical — V-02 rewrites all instructions in second-person ("your gap," "you have written a basis-negation") but introduces no structural differences. Evaluated together.

| Criterion | V-01 | V-02 | Evidence |
|-----------|------|------|----------|
| C-09 Tier sensitivity (up + down) | PASS | PASS | Step 7 table with both directions |
| C-10 Confidence calibration | PASS | PASS | Step 6 table present |
| C-11 Confidence gap named | PASS | PASS | `── CONFIDENCE GAP CHECKPOINT ──` standalone section |
| C-12 Single named sensitivity conditions | PASS | PASS | "Single Named Falsifiable Condition [one scenario]" in column |
| C-13 Explicit tier destination | PASS | PASS | "Tier rises to [ ]" / "Tier drops to [ ]" column slots |
| C-14 Falsifiable conditions | PASS | PASS | "name what investigation settles it" in column |
| C-15 Basis/gap non-overlapping | PASS | PASS | Self-test + DIAGNOSTIC PATTERN enforce different-dimension constraint |
| C-16 Destination tier differs from current | PASS | PASS | Column header: "must differ from current tier" |
| C-17 High-risk constraints carry inline failure examples | PASS | PASS | WRONG/CORRECT adjacent to each constrained field |
| C-18 Constraints encoded as structural features | PASS | PASS | Tier vocabulary in header; "must differ" in column label |
| C-19 Inline examples precede governed field | PASS | PASS | WRONG/CORRECT before table in each step; DIAGNOSTIC PATTERN before gap field |
| C-20 Role-separated production for basis/gap | FAIL | FAIL | Single-phase — no role separation |
| C-21 Both WRONG and CORRECT instances | PASS | PASS | Both present in DIAGNOSTIC PATTERN block |
| C-22 Relational constraint co-encoded in dependent field label | PASS | PASS | Gap field: "not a negation of it"; tier destination: "must differ" in column |
| C-23 Role charters own all output fields | FAIL | FAIL | Single-phase — no role charters |
| C-24 Phase 2 non-access names prohibited category | FAIL | FAIL | Single-phase — no Phase 2 |
| C-25 Phase 2 self-test query | FAIL | FAIL | Single-phase — no Phase 2 |
| C-26 Role ownership co-encoded in field labels | FAIL | FAIL | Single-phase — no role tags |
| C-27 Cross-phase relational constraint in compilation table | FAIL | FAIL | Single-phase — no cross-phase |
| C-28 Single-phase self-test in gap field body | PASS | PASS | "Ask: if I reversed something from my Step 5 basis…" present before gap field |
| C-29 Phase 1 explicit field exclusion list | FAIL | FAIL | Single-phase — no Phase 1 |
| C-30 Defense cluster on gap field | PASS | PASS | All three mechanisms in `── CONFIDENCE GAP CHECKPOINT ──`: column label, self-test query, WRONG/CORRECT |
| C-31 Named pre-commit gate block (in-table gap) | PASS | PASS | Vacuous — C-19 achieved for sensitivity; C-32 removes gap from table |
| C-32 Gap in named standalone section | PASS | PASS | `── CONFIDENCE GAP CHECKPOINT ──` with visual delimiter |
| C-33 Self-test names failure class | PASS | PASS | "If yes: you have written a basis-negation." |
| C-34 Failure-class label in WRONG block | PASS | PASS | `FAILURE CLASS: basis-negation` in WRONG instance |
| C-35 Pre-analysis gate with binary entry signal | PASS | PASS | Phase 0 OPEN/CLOSED |
| C-36 C-05 as independent precondition with per-precondition CLOSED | PASS | PASS | Preconditions A and B; CLOSED-LABEL identifies which failed |
| C-37 Three-field WRONG sub-block (FAILURE CLASS + DETECTION PATTERN + WHY IT FAILS) | PASS | PASS | All three as separately labeled entries in DIAGNOSTIC PATTERN |
| C-38 Phase 0 gate as formal STATUS + CLOSED-LABEL table | PASS | PASS | Two-row table with `Status [CLEAR / BLOCKED]` and `CLOSED-LABEL [fill only if BLOCKED…]` columns |
| C-39 Three-field block in named `── DIAGNOSTIC PATTERN ──` section | PASS | PASS | `### ── DIAGNOSTIC PATTERN ──` section wraps FAILURE CLASS / DETECTION PATTERN / WHY IT FAILS |

**V-01/V-02 aspirational**: 24 PASS, 0 PARTIAL, 7 FAIL (C-20, C-23, C-24, C-25, C-26, C-27, C-29)
**Aspirational score**: 24/31 × 10 = **7.74 pts**

---

#### V-03 (Two-phase role separation; C-38 + C-39 additions)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-20 Role-separated production for basis/gap | PASS | Phase 1 Sizing Analyst / Phase 2 Risk Assessor split |
| C-23 Role charters own all output fields | PASS | "Fields owned by Phase 1" + "Fields reserved for Phase 2" enumeration; "Fields excluded from Phase 2" list |
| C-24 Phase 2 non-access names prohibited category | PASS | "Prohibited content category: any item in the P1-5 confirmed set — e.g., 'API contract is stable,'" |
| C-25 Phase 2 self-test query | PASS | "Ask: if I reversed a statement from P1-5 ('X is confirmed' → 'X is not confirmed'), would I produce my gap? If yes: you have written a basis-negation — a Phase 2 charter violation." |
| C-26 Role ownership in field labels | PASS | Column headers throughout carry "[Phase 1 Sizing Analyst]" / "[Phase 2 Risk Assessor]" tags; "Produced By" column in compilation table |
| C-27 Cross-phase constraint in compilation table | FAIL | Gap field excluded from compilation table (pointer reference); no column to encode constraint in |
| C-28 Single-phase self-test in gap field | FAIL | Multi-phase design; C-25 satisfies the self-test requirement instead |
| C-29 Phase 1 explicit field exclusion list | PASS | "Fields reserved for Phase 2 [do not produce here]: Confidence Gap · Confidence Calibration · Tier Sensitivity" |
| C-38 Phase 0 formal STATUS + CLOSED-LABEL table | PASS | Two-row precondition table with STATUS [CLEAR / BLOCKED] and CLOSED-LABEL columns |
| C-39 `── DIAGNOSTIC PATTERN ──` named section | PASS | `### ── DIAGNOSTIC PATTERN ──` section wraps three-field block in Phase 2 gap checkpoint |

All other aspirational criteria (C-09–C-19, C-21, C-22, C-30–C-37): **PASS** (same as V-01/V-02, confirmed in two-phase context).

**V-03 aspirational**: 29 PASS, 0 PARTIAL, 2 FAIL (C-27, C-28)
**Aspirational score**: 29/31 × 10 = **9.35 pts**

---

#### V-04 (Three-phase lifecycle emphasis; Phase 0 expanded sections + gate-decision table upgraded to C-38)

V-04 retains R14 V-04's expanded per-precondition narrative sections. The gate-decision summary table at the end of Phase 0 is upgraded to STATUS + CLOSED-LABEL columns (C-38 compliance). V-04 wraps Phase 0 in `## ── PHASE 0: ENTRY GATE ──` visual delimiter but this is a section header rather than a standalone delimiter signal.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-38 Phase 0 formal STATUS + CLOSED-LABEL table | PASS | Gate-decision summary table splits RESULT into STATUS [CLEAR / BLOCKED] + CLOSED-LABEL columns; per-row CLOSED reason readable from table |
| C-39 `── DIAGNOSTIC PATTERN ──` named section | PASS | `### ── DIAGNOSTIC PATTERN ──` section in Phase 2 gap checkpoint |
| C-27 Cross-phase constraint in compilation table | FAIL | Gap excluded from compilation table (pointer reference) — same architectural gap as V-03 |
| C-28 Single-phase self-test | FAIL | Multi-phase design |
| C-20, C-23, C-24, C-25, C-26, C-29 | PASS | Two-phase role separation with full charter cluster — same as V-03 |
| All other C-09–C-37 | PASS | Confirmed |

**V-04 aspirational**: 29 PASS, 0 PARTIAL, 2 FAIL (C-27, C-28)
**Aspirational score**: 29/31 × 10 = **9.35 pts**

---

#### V-05 (Champion evolution; ENTRY GATE delimiter + EVIDENCE column + four-field DIAGNOSTIC PATTERN)

V-05 extends R14 champion with two new structural patterns beyond current rubric minimums.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-38 Phase 0 formal STATUS + CLOSED-LABEL table | PASS | Two-row table with STATUS + CLOSED-LABEL columns **plus** EVIDENCE column beyond minimum |
| C-39 `── DIAGNOSTIC PATTERN ──` named section | PASS | Section wraps **four** fields: FAILURE CLASS + DETECTION PATTERN + WHY IT FAILS + REMEDIATION — exceeds C-39 minimum |
| C-27 Cross-phase constraint in compilation table | FAIL | Gap excluded from compilation table (same architectural constraint as V-03/V-04 — C-32 standalone section precludes C-27 without duplicating the gap row) |
| C-28 Single-phase self-test | FAIL | Multi-phase design |
| C-20, C-23, C-24, C-25, C-26, C-29 | PASS | Full C-20 cluster retained |
| C-30 Defense cluster | PASS | All three mechanisms in `── CONFIDENCE GAP CHECKPOINT ──`; self-test references REMEDIATION directly: "Apply the REMEDIATION above" |
| All other C-09–C-37 | PASS | Confirmed |

**V-05 aspirational**: 29 PASS, 0 PARTIAL, 2 FAIL (C-27, C-28)
**Aspirational score**: 29/31 × 10 = **9.35 pts**

---

### Composite Scores

| Variation | Essential | Recommended | Aspirational | **Total** |
|-----------|-----------|-------------|--------------|-----------|
| V-01 | 60 | 30 | 7.74 | **97.74** |
| V-02 | 60 | 30 | 7.74 | **97.74** |
| V-03 | 60 | 30 | 9.35 | **99.35** |
| V-04 | 60 | 30 | 9.35 | **99.35** |
| **V-05** | **60** | **30** | **9.35** | **99.35** |

**Ranking**: V-03 = V-04 = V-05 (99.35) > V-01 = V-02 (97.74)

---

### Tiebreaker: V-03 vs V-04 vs V-05

All three top variations score identically under v15. The distinction is architectural:

- **V-03**: Cleanest targeted addition of C-38 + C-39 to the two-phase design. No lifecycle overhead.
- **V-04**: Lifecycle-heavy Phase 0 (narrative per-precondition sections) compatible with C-38 table schema. Demonstrates that the formal table and expanded context coexist without conflict.
- **V-05**: Pushes beyond current rubric. Two new patterns not yet in v15: (1) EVIDENCE column extending CLEAR verdict to schema-verifiable status; (2) REMEDIATION as fourth diagnostic field closing the class→detection→cause→correction loop. Plus `── ENTRY GATE ──` delimiter applies document-level signaling to the gate phase.

**Champion: V-05** — exceeds current rubric, generates two C-40/C-41 candidate patterns.

---

### Structural Flaw Common to V-03/V-04/V-05: C-27 Tension with C-32

All three multi-phase variations FAIL C-27 because C-32 removes the gap from the compilation table. The architecture that satisfies C-32 (standalone section) structurally prevents C-27 (relational constraint in compilation table column header). To satisfy both simultaneously: add a gap row to the compilation table with a field label encoding the relational constraint while retaining the full standalone section treatment. This is an open architectural gap.

---

### Excellence Signals from V-05

**C-40 candidate — EVIDENCE column on CLEAR verdicts**: The C-38 schema encodes why a precondition is BLOCKED (CLOSED-LABEL column). V-05 symmetrically encodes why a precondition is CLEAR (EVIDENCE column). Both verdict paths become schema-verifiable. A CLEAR without evidence is an assertion; a CLEAR with named evidence is a claim that can be checked at the row level without parsing prose.

**C-41 candidate — REMEDIATION as fourth diagnostic field**: The three-field DIAGNOSTIC PATTERN block (C-37/C-39) gives the model class→detection→cause. The REMEDIATION field closes the loop to correction. The self-test can now reference the REMEDIATION directly ("Apply the REMEDIATION above") rather than deriving a correction from the failure analysis. The diagnostic pattern becomes a complete failure-handling unit rather than a diagnostic-only block.

**`── ENTRY GATE ──` delimiter**: Applies the same document-level structural signal as `── CONFIDENCE GAP CHECKPOINT ──` to the gate phase — indicating a mandatory evaluation block, not a preamble.

---

```json
{"top_score": 99, "all_essential_pass": true, "new_patterns": ["EVIDENCE column on gate table extends structural encoding to CLEAR verdicts — both CLEAR and CLOSED paths verifiable at schema level without prose cross-reference (C-40 candidate)", "REMEDIATION as fourth field in DIAGNOSTIC PATTERN closes diagnostic loop: class-detection-cause-correction as a complete unit; self-test references REMEDIATION directly (C-41 candidate)"]}
```
