## Scorecard — org-pr Round 5

**Rubric**: v5 | **N_essential**: 5 | **N_recommended**: 5 | **N_aspirational**: 12

---

### Criterion-by-Criterion Grid

#### Essential Criteria (60 pts / 12 pts each)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Multi-role coverage | PASS | PASS | PASS | PASS | PASS |
| C-02 P1/P2/P3 on every finding | PASS | PASS | PASS | PASS | PASS |
| C-03 File-based role selection | PASS | PASS | PASS | PASS | PASS |
| C-04 Explicit go/no-go verdict | PASS | PASS | PASS | PASS | PASS |
| C-05 Per-role structure / no bleeding | PASS | PASS | PASS | PASS | PASS |
| **Essential total** | **60** | **60** | **60** | **60** | **60** |

All essential pass in every variation.

---

#### Recommended Criteria (30 pts / 6 pts each)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-06 Projection-aware consensus | PASS | PASS | PASS | PASS | PASS |
| C-07 Conflict analysis (resolution present) | PASS | **FAIL** | PASS | PASS | PASS |
| C-08 Locator self-correction gate | PASS | PASS | PASS | PASS | PASS |
| C-09 Phase/lifecycle gating | **FAIL** | PASS | PASS | PASS | PASS |
| C-10 Downstream risk field | PASS | PASS | PASS | PASS | PASS |
| **Recommended total** | **24** | **24** | **30** | **30** | **30** |

Evidence notes:
- **C-07 V-02**: No conflict analysis section at all. V-02 is a single-axis isolation (phase gate only); no conflict table → FAIL, not PARTIAL.
- **C-09 V-01**: No phase gate in V-01. Confirmed FAIL — this was the primary remaining gap after R4.
- **C-08 all**: Branch instruction present in every variation — "if invalid → rewrite → include" explicit in V-01 through V-05. Tightened pass condition satisfied.

---

#### Aspirational Criteria (10 pts / 0.833 pts each)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-11 Formula lock | PASS | PASS | PASS | PASS | PASS |
| C-12 Named invalid forms | FAIL | FAIL | FAIL | FAIL | **PASS** |
| C-13 Inertia / if-stays framing | FAIL | FAIL | FAIL | **PASS** | PASS |
| C-14 Verdict escape closure | **PARTIAL** | **PARTIAL** | **PARTIAL** | **PARTIAL** | **PASS** |
| C-15 Projection convergence call | PASS | PASS | PASS | PASS | PASS |
| C-16 Self-correction gate pre-commit | PASS | **FAIL** | PASS | PASS | PASS |
| C-17 Role authority sequence declaration | PASS | **FAIL** | PASS | PASS | PASS |
| C-18 Axis conflict resolution rule | N/A→PASS | N/A→PASS | N/A→PASS | PASS | PASS |
| C-19 Verdict hardening pair | **PARTIAL** | **PARTIAL** | **PARTIAL** | **PARTIAL** | **PASS** |
| C-20 Priority table as composition mechanism | N/A→PASS | N/A→PASS | N/A→PASS | PASS | PASS |
| C-21 Authority-inertia reconciliation rule | N/A→PASS | N/A→PASS | N/A→PASS | PASS | PASS |
| C-22 Conflict resolution column | PASS | N/A→PASS | PASS | PASS | PASS |

Evidence notes:

**C-12**: V-01 through V-04 have no named invalid forms. V-05 names three: untagged (no severity), revision (changing upstream severity), and aggregate (combining two surfaces) — each with correction instruction. First round to achieve PASS.

**C-13**: V-01 through V-03 have no if-stays column or instruction. V-04 and V-05 add the "If-Stays Projection" column with "compounding cost" framing. PASS for V-04 and V-05.

**C-14**: V-01 through V-04 name the escape paths ("Reclassify any P1 or accept No-Go") and state "No third outcome" — but none explicitly close by exclusion. The critical missing phrase is "No other escape path exists." Without it, a novel escape claim is not explicitly foreclosed. PARTIAL all four. V-05 adds: "No other escape path exists. A P1 + Go claim is invalid under this formula." PASS.

**C-16**: V-02 has no pre-commit self-check section. All others include explicit numbered pre-commit verification items.

**C-17**: V-02 has no Authority Chain section and no declared review order. V-01, V-03, V-04, V-05 all declare Security (1) → UX (6) with authority rationale.

**C-18**: V-01, V-02, V-03 each have fewer than 3 competing governance axes (authority chain is the primary axis, with supplemental structures that explicitly defer to it). N/A → PASS. V-04 introduces an explicit 3-axis Axis Composition Table (authority chain / inertia framing / conflict resolution) with tiebreaker — PASS. V-05 extends to 8 axes with the same structure — PASS.

**C-19**: Follows C-14. C-19 requires both C-11 and C-14 PASS simultaneously. C-11 PASS in all variations. C-14 PARTIAL in V-01 through V-04 → C-19 PARTIAL. V-05 is the first to explicitly name the pair as a unit ("Verdict Hardening Pair" section header) and achieve C-14 PASS → C-19 PASS.

**C-20**: V-01, V-02, V-03 all have fewer than 3 composition axes (phase gate excluded as a pre-run guard, not a review-time governance axis). N/A → PASS. V-04 and V-05 both have 3+ explicit axes with priority tables — PASS.

**C-21**: V-01, V-02, V-03 have no inertia/if-stays axis — N/A → PASS. V-04 and V-05 both include the explicit reconciliation declaration: "describes the compounding cost of the upstream finding going unresolved — not a reclassification." PASS.

**C-22**: V-01, V-03, V-04, V-05 all have the Resolution column wired to authority-position logic. V-02 has no conflict section → N/A → PASS.

**C-07 closure via C-22**: V-01, V-03, V-04, V-05 — all four seal C-07 PASS by providing a Resolution column with explicit authority-position rule. V-05 adds the mechanical derivation statement: "derived mechanically from the authority chain — no judgment required."

---

#### Aspirational Score Summary

| Variation | Pass count (PARTIAL=0.5) | Aspirational pts |
|-----------|--------------------------|-----------------|
| V-01 | 8×1.0 + 2×0.5 + 2×0 = **9.0** | **7.50** |
| V-02 | 7×1.0 + 2×0.5 + 3×0 = **8.0** | **6.67** |
| V-03 | 8×1.0 + 2×0.5 + 2×0 = **9.0** | **7.50** |
| V-04 | 9×1.0 + 2×0.5 + 1×0 = **10.0** | **8.33** |
| V-05 | 12×1.0 + 0×0.5 + 0×0 = **12.0** | **10.00** |

---

### Composite Score Summary

| Variation | Essential | Recommended | Aspirational | **Composite** |
|-----------|-----------|-------------|--------------|---------------|
| V-01 | 60.00 | 24.00 | 7.50 | **91.50** |
| V-02 | 60.00 | 24.00 | 6.67 | **90.67** |
| V-03 | 60.00 | 30.00 | 7.50 | **97.50** |
| V-04 | 60.00 | 30.00 | 8.33 | **98.33** |
| V-05 | 60.00 | 30.00 | 10.00 | **100.00** |

**Ranking**: V-05 > V-04 > V-03 > V-01 > V-02

---

### Gap Analysis vs. Variation Plan Expected Scores

The actual composite scores exceed the variation plan projections across the board. The systematic gap (actual ~91–100 vs. expected ~84–96+) is primarily driven by two factors:

1. **N/A→PASS credits**: C-18, C-20, C-21, C-22 all carry N/A→PASS provisions. Minimal variations (V-01, V-02, V-03) that don't invoke those axes receive full credit, which the variation plan likely underestimated.

2. **C-15 and C-17 consistently pass**: These criteria were implicitly satisfied in all non-V-02 variations; the variation plan may have expected partial compliance.

The ranking order is identical to the plan's projection.

---

### Excellence Signals — V-05

V-05 is the first variation in four rounds to achieve a perfect score. Three patterns distinguish it from V-04 (the next-closest at 98.33):

#### 1. Escape-by-exclusion closes C-14 and C-19

Every prior variation listed the escape paths without explicitly closing them. V-05 adds:

> "No other escape path exists. A P1 + Go claim is invalid under this formula."

"No other escape path exists" closes by exclusion — it is not enough to name the valid paths; the prompt must state that all others are invalid. This is the pattern that finally unseals C-14, which in turn unseals C-19 (which requires both C-11 and C-14 in the same prompt).

#### 2. Invalid-form enumeration as named anti-patterns

C-12 requires naming invalid forms with examples — not just prohibition. V-05 provides three named anti-patterns with concise correction instructions:

- Untagged findings → "rewrite with P1/P2/P3 before including"
- Findings that revise upstream severity → "record as if-stays projection instead"
- Aggregate findings combining two surfaces → "split into separate rows"

Each anti-pattern is named, described, and corrected. Prohibition-only ("do not include untagged findings") fails C-12 because it doesn't give the model a repair path, only a block.

#### 3. Mechanical derivation declaration seals the conflict resolution column

V-05 adds one sentence to the Resolution column instruction:

> "This is derived mechanically from the authority chain — no judgment required."

This removes the last ambiguity in C-22/C-07. Saying "lower position governs" is a rule; saying "no judgment required" removes the implied discretion that allowed a model to treat the conflict as open. Four rounds of C-07 PARTIAL were caused by the absence of a resolution mechanism. The mechanical derivation declaration is what fully closes it.

---

### Unsealed Gaps Entering R6

None. All criteria reach PASS in at least one variation (V-05). The rubric is fully satisfied at 100/100 for V-05.

For R6, if the rubric remains v5:
- V-04 at 98.33 — only gaps are C-12 FAIL and C-14/C-19 PARTIAL. Both sealable by adding V-05's escape-by-exclusion and named anti-pattern sections to V-04's axis structure.
- The priority table + C-21 combination (V-04 and V-05) should be carried forward as the minimum structure for any multi-axis org-pr prompt.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["escape-by-exclusion: stating 'no other escape path exists' explicitly closes C-14; listing escape paths without exclusion scores PARTIAL in every round", "invalid-form enumeration: naming three anti-patterns (untagged, revision, aggregate) with per-form correction instructions achieves C-12 PASS; prohibition-only fails because it blocks without repairing", "mechanical derivation declaration: 'derived mechanically from the authority chain — no judgment required' removes implied discretion from the resolution column, sealing C-07 after four rounds of PARTIAL"]}
```
