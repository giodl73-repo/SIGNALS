Now I have everything needed to score R18. Let me produce the full scorecard.

---

## Round 18 Scorecard — corps-committee

### Rubric version: v18 | Denominator: 42 | Weight per criterion: 100 ÷ 42 ≈ 2.381 pts

---

### Per-Criterion Assessment

**Baseline inheritance:** All five R18 variations are built on the R17 V-05 baseline (40/40 = 100.0). C-01 through C-48 are inherited intact across all variations. The R18 rubric introduces two new discriminator criteria: C-49 (pre-flight citation precision) and C-50 (FAILS template recursive currency through the C-46/C-47/C-48 triplet).

| Criterion | Basis | All Variations |
|-----------|-------|----------------|
| C-01–C-45 | Inherited from R17 V-05 (all passing) | **PASS** |
| C-46 | FAILS template carries C-44/C-45 CORRECT entries — present in all R18 variations | **PASS** |
| C-47 | BEFORE YOU START carries a pre-flight halt for FAILS template currency (mechanism fires) — present in all R18 variations | **PASS** |
| C-48 | BEFORE YOU START carries pre-flight halt for CO-DEPENDENCY PREAMBLE completeness — present in all R18 variations | **PASS** |

**Prior 48 criteria: all PASS across all five variations.**

---

### R18 Discriminator Criteria (C-49, C-50)

#### V-01 — C-49 Only (pre-flight citation precision; no C-50)

| Criterion | Evidence | Result |
|-----------|----------|--------|
| **C-49** | BYS pre-flight reads: `"C-42, C-43, C-44, C-45, or any later pair: template not current; C-46 miss."` Citation names `C-46 miss` (the current governing criterion) and explicitly enumerates `C-44, C-45` in the pair list. Both sub-requirements satisfied: citation accurate; enumeration complete. | **PASS** |
| **C-50** | FAILS template ends at C-45. No CORRECT entries exist for C-46, C-47, or C-48. A reviewer encountering a stale pre-flight citation (C-47 violation) or missing preamble pre-flight (C-48 violation) has no canonical FAILS entry to cite from the template. | **FAIL** |

**V-01 score: 41/42 = 97.6**

---

#### V-02 — C-50 Only (template extension through C-48; no C-49)

| Criterion | Evidence | Result |
|-----------|----------|--------|
| **C-49** | BYS pre-flight retains: `"C-42, C-43, or any later pair: template not current; C-44 miss."` Citation names `C-44 miss` — the criterion that governed template currency when C-47 was first authored, not the current governing criterion (C-46). Pair list omits C-44 and C-45. Both sub-requirements fail: citation stale; enumeration incomplete. | **FAIL** |
| **C-50** | FAILS template carries CORRECT entries for C-46, C-47, and C-48. A C-46, C-47, or C-48 violation has a canonical FAILS citation in the template. Recursive currency extended to the full R17 aspirational triplet. | **PASS** |

**V-02 score: 41/42 = 97.6**

---

#### V-03 — Prose Format Variation (neither C-49 nor C-50)

| Criterion | Evidence | Result |
|-----------|----------|--------|
| **C-49** | BYS pre-flight retains `C-44 miss` citation with stale pair list `"C-42, C-43, or any later pair."` Neither citation nor enumeration meets C-49 standard. | **FAIL** |
| **C-50** | FAILS template ends at C-45 — no C-46/C-47/C-48 entries. | **FAIL** |
| **C-01–C-48** | Phase 3 rendered as prose blocks with STANCE/CITE/RESPONDS-TO preserved as named fields within each block. All content-based criteria satisfied; table format is confirmed non-load-bearing for criteria satisfaction. | **PASS** |

**V-03 score: 40/42 = 95.2**

**Note on V-03 content finding:** The prose format experiment confirms that criteria C-01 through C-48 are content-dependent, not format-dependent. The table structure in Phase 3 is a readability affordance, not a criterion-bearing element. This is a bounded finding — it does not affect C-49 or C-50, which are structural/pre-flight requirements.

---

#### V-04 — C-50 Full + C-49 Partial (correct criterion, stale pair list)

| Criterion | Evidence | Result |
|-----------|----------|--------|
| **C-49** | BYS pre-flight reads: `"C-42, C-43, or any later pair: template not current; C-46 miss."` Citation names `C-46 miss` — correct governing criterion (sub-requirement 1 satisfied). Pair list reads `"C-42, C-43, or any later pair"` — C-44 and C-45 not explicitly enumerated, requiring reviewer inference (sub-requirement 2 not satisfied). C-49 requires both: accurate citation AND complete enumeration. V-04 satisfies the citation half but not the enumeration half. | **PARTIAL** |
| **C-50** | FAILS template carries CORRECT entries for C-46, C-47, and C-48. Full recursive currency through the R17 triplet. | **PASS** |

**V-04 score: 41.5/42 = 98.8**

**Note on V-04 C-49 partial:** V-04's pre-flight would direct a reviewer to check for a `C-46` violation (correct) but would not tell the reviewer which specific pairs require template entries — those must be inferred from "any later pair." The gap is not mechanical (the halt fires) but informational: a reviewer cannot reconstruct the exact staleness condition from the halt text alone. C-49 PARTIAL awards half-criterion credit (0.5/1.0).

---

#### V-05 — Full Integration: C-49 Precise + C-50 Full

| Criterion | Evidence | Result |
|-----------|----------|--------|
| **C-49** | BYS pre-flight reads: `"C-42, C-43, C-44, C-45, or any later pair: template not current; C-46 miss."` Citation names `C-46 miss` (current governing criterion — sub-requirement 1). Pair list explicitly enumerates `C-44, C-45` alongside `C-42, C-43` (complete enumeration — sub-requirement 2). Both halves satisfied: a reviewer reading this halt knows exactly which criterion governs AND which pairs require template entries without consulting rubric history. | **PASS** |
| **C-50** | FAILS template carries CORRECT entries for C-46, C-47, and C-48. Full recursive currency through the R17 aspirational triplet. Combined with C-49, every mechanism required by C-47 is both present (the halt fires), correctly labelled (cites C-46), and self-documenting (enumerates the pairs). | **PASS** |

**V-05 score: 42/42 = 100.0**

---

### Composite Scores + Ranking

| Rank | Variation | C-01–C-48 | C-49 | C-50 | Score | Golden? |
|------|-----------|-----------|------|------|-------|---------|
| 1 | **V-05** Full integration | 48/48 | PASS | PASS | **100.0** | YES |
| 2 | **V-04** C-50 + C-49 partial | 48/48 | PARTIAL | PASS | **98.8** | YES |
| 3 | **V-01** C-49 only | 48/48 | PASS | FAIL | **97.6** | — |
| 3 | **V-02** C-50 only | 48/48 | FAIL | PASS | **97.6** | — |
| 5 | **V-03** Prose format | 48/48 | FAIL | FAIL | **95.2** | — |

---

### Excellence Signals — V-05

**1. Pre-flight precision is a two-component requirement: citation accuracy and enumeration completeness.** V-04 demonstrates that naming the correct governing criterion (C-46 miss) is not sufficient if the pair list remains implicit. V-05 shows that both components are independently necessary: a halt that names the right criterion but leaves the affected pairs implicit fails the same way a stale citation does — a reviewer cannot reconstruct the staleness condition from the halt text alone. The two components are orthogonal and must both be maintained as the rubric evolves.

**2. Catch-all inference ("any later pair") is a maintenance gap, not a completeness guarantee.** V-04's pair list includes `"or any later pair"` as a catch-all, which appears to cover forward cases. But it offloads enumeration to the reviewer: they must consult rubric history to determine which pairs are "later." V-05 eliminates this inference dependency by explicitly listing `C-44, C-45` in the pair list. The pattern: when a maintenance instruction says "or any later X," that is a signal that the instruction itself will need to be updated each time a new X is added — the catch-all is temporary, not permanent.

**3. Simultaneous closure is not automatic from independent mechanism presence.** V-01 satisfies C-49 alone; V-02 satisfies C-50 alone; V-04 satisfies C-50 fully and C-49 partially. Only V-05 closes both gaps simultaneously at full precision. The excellence signal is not that both mechanisms exist — V-04 has both mechanisms — but that both mechanisms are maintained to the same precision standard. A system with defense in depth is only as precise as its least-precise layer.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["pre-flight halt precision is a two-component requirement — citation accuracy (which criterion governs) and enumeration completeness (which pairs are affected) are orthogonal and must both be maintained independently as the rubric evolves", "catch-all inference clauses like 'any later pair' are maintenance gaps not completeness guarantees — they must be replaced with explicit enumeration each time a new criterion pair is added, for the same reason the template entries must be updated"], "rubric_version_produced": "v19", "new_criteria": ["C-51: C-47 pre-flight pair-list currency — citation advances to C-50 miss; pair list explicitly enumerates C-46/C-47/C-48", "C-52: FAILS template carries C-49/C-50 self-referential entries"], "denominator": "42 → 44"}
```
