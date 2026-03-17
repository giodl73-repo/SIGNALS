## Round 13 Scorecard — `topic-roadmap` (v13 Rubric)

---

### Essential Criteria (all must pass)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Delta categories present | PASS | PASS | PASS | PASS | PASS |
| C-02 Proposals after delta | PASS | PASS | PASS | PASS | PASS |
| C-03 Proposals concrete / action-typed | PASS | PASS | PASS | PASS | PASS |
| C-04 Confirmation gate present and blocking | PASS | PASS | PASS | PASS | PASS |
| C-05 All-namespace coverage with null rows | PASS | PASS | PASS | PASS | PASS |

All five variations pass all essential criteria.

---

### Recommended Criteria (≥ 2 of 3 must pass)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-06 Null path stop at defeat phase | PASS | PASS | PASS | PASS | PASS |
| C-07 Confidence tiers defined | PASS | PASS | PASS | PASS | PASS |
| C-08 Consequence-if-unchanged in proposals | FULL | **PARTIAL** Phase 5 col is "Consequence if HOLDS", not "Consequence if unchanged" | FULL | FULL | FULL |

All variations meet the ≥ 2/3 threshold.

---

### Aspirational Criteria (0 / 1 / 2 each; max = 44)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| C-09 Pre-signal defense register | 2 | 2 | **1** | 2 | 2 | V-03: no restart isolation, weaker isolation constraint |
| C-10 SIGNAL READ-LOCK named + bias-labeled | 2 | 2 | 2 | 2 | 2 | All present |
| C-11 INERTIA-GATE explicit blocking | 2 | 2 | 2 | 2 | 2 | All present |
| C-12 Consequence column in defeat assessment | 2 | **1** | 2 | 2 | 2 | V-02: col named "Consequence if HOLDS" — C-12 requires "Consequence if unchanged" by name |
| C-13 DEFEATED/HOLDS verdict semantics | 2 | 2 | 2 | 2 | 2 | All present (V-03: embedded in Phase 5, still fully specified) |
| C-14 NEW/PRIOR with explicit date anchor | 2 | 2 | 2 | 2 | 2 | All present |
| C-15 Confidence levels with evidential criteria | 2 | 2 | 2 | 2 | 2 | All present |
| C-16 Type-labeled nulls for all categories | 2 | 2 | 2 | 2 | 2 | All seven null types present |
| C-17 Bias labels per proposal row and per phase | **1** | 2 | 2 | 2 | 2 | V-01: phase annotations only; no "Bias blocked by guard" column in Phase 6 |
| C-18 WITHDRAW operator defined | 2 | 2 | 2 | 2 | 2 | All present with row-level syntax |
| C-19 Phase entry/exit conditions | 2 | 2 | 2 | 2 | 2 | All present |
| C-20 Bias labels at every structural guard | 2 | 2 | **1** | 2 | 2 | V-03: confirmation gate and write guard unlabeled; Phase 6 INERTIA-GATE has no separate bias annotation |
| C-21 Dual-site INERTIA-GATE | 2 | 2 | 2 | 2 | 2 | V-03 text has both sites; Phase 6 restates HOLDS exclusion independently |
| C-22 Restart isolation clause in Phase 1 | 2 | 2 | **0** | 2 | 2 | V-03: no restart clause anywhere |
| C-23 Standalone verdict vocabulary block | 2 | 2 | **0** | 2 | 2 | V-03: verdict semantics embedded inline in Phase 5 |
| C-24 Structural mechanism spatial separation | 2 | 2 | **0** | 2 | 2 | V-03: no SECTION SCOPE declarations; mechanisms co-located |
| C-25 Phase 5 verdict deferral + anti-duplication | 2 | 2 | **0** | 2 | 2 | V-03: Phase 5 redefines verdict semantics inline; no forward-reference |
| C-26 Consequence field in Phase 5 exit criterion | 2 | 2 | 2 | 2 | 2 | All exit criteria name "Consequence if unchanged" |
| C-27 Column header ≡ exit criterion field name | 2 | **1** | 2 | 2 | 2 | V-02: Phase 5 col = "Consequence if HOLDS" ≠ exit criterion "Consequence if unchanged" |
| C-28 Dual-site consequence blocking | 2 | **1** | **1** | 2 | 2 | V-02: exit criterion only (no preamble CONSEQUENCE GATE); V-03: same |
| C-29 Three-way consequence field name identity | **2** | **1** | **2** | **2** | **2** | V-02: Phase 5 site drifts to "Consequence if HOLDS" (2 of 3 match) |
| C-30 Proposal table bias column at row level | **0** | **2** | **2** | **2** | **2** | V-01: deliberately absent; V-02–V-05: "Bias blocked by guard" column in 6a and 6b schemas |

---

### Composite Scores

| Variation | Raw Points | Score | Rank |
|-----------|-----------|-------|------|
| **V-04** | **44 / 44** | **10.00** | **1 (tie)** |
| **V-05** | **44 / 44** | **10.00** | **1 (tie)** |
| V-01 | 41 / 44 | 9.32 | 3 |
| V-02 | 40 / 44 | 9.09 | 4 |
| V-03 | 33 / 44 | 7.50 | 5 |

V-03's four consecutive zeros (C-22 through C-25) cost 8 points — the minimal base proves C-29 and C-30 are achievable independently, but strips the structural machinery that makes the skill auditable.

---

### Criterion-by-Criterion: V-04 vs V-05

V-04 and V-05 are identical in every per-phase criterion. The distinction is the Output Schema CONTRACT block:

- **V-04**: Single CONTRACT annotation names "Consequence if unchanged" as pre-committed across all three sites (covers C-29)
- **V-05**: Dual CONTRACT annotation adds CONTRACT B naming "Bias blocked by guard" as a required column in Phase 6a/6b (covers C-30 detectability from schema alone)

C-24 spatial separation holds for both: the dual CONTRACT belongs to the Output Schema block's scope, not to Phase 1, Verdict Vocabulary, or INERTIA-GATE sections. No contamination.

---

### Excellence Signals (from V-04 / V-05)

**1. PROPOSAL BIAS AUDIT guard in Phase 6 as a named enforcement point**

V-04/V-05 add this guard at Phase 6 entry with explicit mechanism text distinguishing per-row bias labeling from phase-level annotations. The guard explains _why_ both levels are required — phase annotations address systemic phase structure bias; row-level column addresses motivated reasoning at the individual proposal decision surface. This closes C-30 via a named site that makes the distinction testable independently of C-17.

**2. Phase 6 SECTION SCOPE extended to include row-level bias labeling**

V-04's Phase 6 SECTION SCOPE reads "gate-exclusion text, proposal generation, and row-level bias labeling." This ensures the PROPOSAL BIAS AUDIT guard is scoped within Phase 6's boundary, keeping C-24 spatial separation intact. Without this extension, adding the bias guard to Phase 6 would create a SECTION SCOPE mismatch detectable by a C-24 auditor.

**3. Dual-column OUTPUT SCHEMA CONTRACT pre-committing both C-29 and C-30 (V-05)**

V-05's CONTRACT A + CONTRACT B locks in both "Consequence if unchanged" (four sites) and "Bias blocked by guard" (Phase 6 tables) before any file is read. A reviewer can detect a C-29 failure (naming drift) or a C-30 failure (missing bias column) from the schema block alone, without reading Phase 5 or Phase 6. This makes the top-scoring variation more auditable than V-04 at no cost to any other criterion.

---

### R13 Key Findings

| Finding | Detail |
|---------|--------|
| C-29 + C-30 are orthogonal | V-01 proves C-29 full without C-30; V-02 proves C-30 full without C-29; V-03 proves both from minimal base |
| Full stack is not required for C-29/C-30 | V-03 achieves both at 7.50 — the deficit is C-22–C-25 zeros, not the new criteria |
| V-02's deliberate naming drift costs C-12 and C-27 | "Consequence if HOLDS" in Phase 5 creates a 3-point loss (C-12=1, C-27=1, C-29=1) vs C-30's 2-point gain — net -1 vs V-01 |
| Perfect score is achievable | V-04/V-05 hit 44/44; all 22 aspirational criteria at full pass |

---

```json
{"top_score": 44, "all_essential_pass": true, "new_patterns": ["PROPOSAL BIAS AUDIT guard at Phase 6 entry names the row-level motivated-reasoning failure mode explicitly, distinguishing it from phase-level bias annotations and making C-30 enforcement independently verifiable at a named guard site", "Dual-column OUTPUT SCHEMA CONTRACT pre-commits both consequence-field naming identity across all three sites and bias-column presence in Phase 6 tables before any file is read, making C-29 and C-30 violations detectable from the schema block alone without reading any phase"]}
```
