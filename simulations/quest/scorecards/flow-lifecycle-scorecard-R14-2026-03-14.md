# flow-lifecycle — Round 14 Scorecard

**Rubric:** v14 | **Formula:** aspirational_pass / 37 × 10 | **Golden threshold:** ≥9.0

---

## Variation Scoring

### V-01 — Role Sequence (Finance-first ordering)

**Axis:** Role ordering only. No structural additions (no C-44, no C-45).

**Hypothesis:** Finance-first role ordering improves dual-cite evidence quality without structural additions.

| Group | Criteria | Result | Notes |
|-------|----------|--------|-------|
| Essential | C-01–C-05 | PASS × 5 | Strong baseline; role ordering does not break any essential criterion |
| Aspirational baseline | C-06–C-43 | PASS × 29 | All prior-round structural criteria satisfied |
| C-44 | Per-block Exception Refs enumeration | **FAIL** | No `Exception Refs:` sub-field in B-NN blocks; only gate check present |
| C-45 | Phase Gate Three-Field Contract Declaration | **FAIL** | No explicit CONTRACT SUMMARY or preamble naming the three fields as a unit |

**Aspirational pass:** 34 / 37
**Score:** 34/37 × 10 = **9.189**
**Golden:** PASS (≥9.0)

**Finding:** Finance-first role ordering produces no additional aspirational gain. Confirms role sequence is orthogonal to structural depth criteria. The hypothesis is falsified — role ordering alone does not improve aspirational score.

---

### V-02 — Output Format (Isolated per-block Exception Refs)

**Axis:** Structural format change only — promotes `Exception Refs:` to a named sub-block with `Required format:` and `Fail condition:` lines.

**Hypothesis:** Isolated per-block sub-block format is more reliable C-44 compliance trigger than embedded preamble instruction.

| Group | Criteria | Result | Notes |
|-------|----------|--------|-------|
| Essential | C-01–C-05 | PASS × 5 | Unaffected |
| Aspirational baseline | C-06–C-43 | PASS × 29 | All prior-round structural criteria satisfied |
| C-44 | Per-block Exception Refs enumeration | **PASS** | Named sub-block with `Required format: Exception Refs: EX-N, EX-M` + `Fail condition:` anchors compliance visually and structurally; preamble gate check remains consistent |
| C-45 | Phase Gate Three-Field Contract Declaration | **FAIL** | No dedicated CONTRACT SUMMARY; three-field relationship remains implicit |

**Aspirational pass:** 35 / 37
**Score:** 35/37 × 10 = **9.459**
**Golden:** PASS

**Finding:** Structural isolation of the `Exception Refs:` field as a self-contained named sub-block (parallel to Evidence block structure) produces reliable C-44 compliance. The `Required format:` + `Fail condition:` pattern gives per-block verification handles. Hypothesis confirmed.

---

### V-03 — Lifecycle Emphasis (Dedicated PHASE GATE CONTRACT SUMMARY)

**Axis:** Lifecycle structure only — explicit `PHASE GATE CONTRACT SUMMARY` section before PHASE 1 naming all three fields as a declared unit.

**Hypothesis:** Dedicated PHASE GATE CONTRACT SUMMARY is a more reliable C-45 trigger than R13's cross-block phrasing.

| Group | Criteria | Result | Notes |
|-------|----------|--------|-------|
| Essential | C-01–C-05 | PASS × 5 | Unaffected |
| Aspirational baseline | C-06–C-43 | PASS × 29 | All prior-round structural criteria satisfied |
| C-44 | Per-block Exception Refs enumeration | **FAIL** | No per-block `Exception Refs:` sub-field; B-NN blocks carry only preamble gate ref |
| C-45 | Phase Gate Three-Field Contract Declaration | **PASS** | Dedicated section explicitly names `Prior phase:`, `Prior phase blocked bottleneck:`, `Next phase:` as a unit; orthogonality declared using string-pattern comparison language; CHAIN STATUS direction mapping explicit |

**Aspirational pass:** 36 / 37
**Score:** 36/37 × 10 = **9.730**
**Golden:** PASS

**Finding:** Dedicated PHASE GATE CONTRACT SUMMARY reliably triggers C-45. The section-level declaration (vs. cross-block inference) is the critical structural move. Hypothesis confirmed. V-03 outscores V-02 because C-45 (36/37) > C-44 (35/37) in isolation — both are single-criterion additions but C-45 passes while C-44 does not appear.

---

### V-04 — Role Sequence + Output Format (Finance-first + per-block refs)

**Axis:** V-01 + V-02 composition. Finance-first roles + isolated per-block `Exception Refs:` format.

**Hypothesis:** The two axes compose without conflict; C-44 passes independently of role ordering.

| Group | Criteria | Result | Notes |
|-------|----------|--------|-------|
| Essential | C-01–C-05 | PASS × 5 | Unaffected |
| Aspirational baseline | C-06–C-43 | PASS × 29 | Role ordering does not break any existing criterion |
| C-44 | Per-block Exception Refs enumeration | **PASS** | Per-block named sub-block format (from V-02) preserved; role ordering is orthogonal |
| C-45 | Phase Gate Three-Field Contract Declaration | **FAIL** | No CONTRACT SUMMARY; three-field relationship implicit |

**Aspirational pass:** 35 / 37
**Score:** 35/37 × 10 = **9.459**
**Golden:** PASS

**Finding:** V-04 = V-02 in score (35/37). Finance-first role ordering contributes zero additional aspirational passes, confirming V-01's finding. The composition is clean but adds no incremental gain beyond V-02 alone. C-44 passes, C-45 does not.

---

### V-05 — Output Format + Lifecycle Emphasis (V-02 + V-03 combined)

**Axis:** Maximum density — per-block `Exception Refs:` (C-44) + dedicated PHASE GATE CONTRACT SUMMARY (C-45) + per-phase incumbent IM-reference callouts.

**Hypothesis:** V-02 + V-03 compose to 37/37; IM-reference callouts additionally anchor SECTION A dual-cite evidence.

| Group | Criteria | Result | Notes |
|-------|----------|--------|-------|
| Essential | C-01–C-05 | PASS × 5 | Unaffected |
| Aspirational baseline | C-06–C-43 | PASS × 29 | All prior-round criteria fully satisfied |
| C-44 | Per-block Exception Refs enumeration | **PASS** | Isolated sub-block with `Required format:` + `Fail condition:` in every B-NN block; consistent with preamble gate check by string comparison |
| C-45 | Phase Gate Three-Field Contract Declaration | **PASS** | Dedicated PHASE GATE CONTRACT SUMMARY section; three fields named as a unit; orthogonality declaration explicit; CHAIN STATUS coverage declared |

**Aspirational pass:** 37 / 37
**Score:** 37/37 × 10 = **10.000**
**Golden:** PASS (perfect)

**Finding:** V-02 and V-03 compose additively with no interference. The per-phase incumbent IM-reference callouts anchor dual-cite evidence quality without disrupting any existing criterion. Perfect aspirational coverage achieved. Hypothesis confirmed.

---

## Ranking

| Rank | Variation | C-44 | C-45 | Score |
|------|-----------|:----:|:----:|-------|
| 1 | **V-05** | PASS | PASS | **10.000** |
| 2 | **V-03** | FAIL | PASS | **9.730** |
| 3 | **V-02** | PASS | FAIL | **9.459** |
| 3 | **V-04** | PASS | FAIL | **9.459** |
| 5 | **V-01** | FAIL | FAIL | **9.189** |

All 5 variations cross the golden threshold (≥9.0). All essential criteria PASS in all variations.

---

## Excellence Signals (from V-05)

**1. Named sub-block with verification handles outperforms embedded instruction.**
The `Exception Refs:` field isolated into its own named sub-block — structurally parallel to Evidence/Impact fields — with explicit `Required format: Exception Refs: EX-N, EX-M` and `Fail condition: missing or NONE when EX blocks point here` lines produces C-44 compliance more reliably than embedding the instruction in preamble prose. The visual isolation makes the field mandatory, not optional.

**2. Dedicated CONTRACT SUMMARY section beats cross-block declaration for C-45.**
A standalone `PHASE GATE CONTRACT SUMMARY` section placed before PHASE 1, with one row per field and explicit orthogonality language using string-pattern comparison, binds the three-field contract as a named unit. Cross-block phrasing that implies the relationship does not trigger C-45; only an explicit section that declares it does.

**3. The two structural axes are non-interfering and fully additive.**
V-02's per-block format change and V-03's lifecycle summary section operate in independent structural zones (B-NN blocks vs. preamble/lifecycle section). They compose to 37/37 without degrading any existing criterion — confirmed by V-05 matching the theoretical maximum.

**4. Role ordering is a neutral axis.**
V-01 and V-04 confirm that domain-specific role sequencing (Finance-first) has no effect on aspirational score. Role ordering changes surface presentation, not structural depth. This isolates the aspirational criteria as structural, not organizational.

---

## R14 → R15 Guidance

V-05 achieves 37/37. The remaining R15 question is whether instruction isolation generalizes: can the `Required format:` + `Fail condition:` sub-block pattern be applied to other aspirational criteria to improve their reliability, or is it specific to the enumeration case?

---

```json
{"top_score": 10.0, "all_essential_pass": true, "new_patterns": ["Named sub-block with Required format and Fail condition fields produces more reliable criterion compliance than embedded instruction text — isolation makes fields mandatory not optional", "Dedicated CONTRACT SUMMARY section with explicit row-per-field and orthogonality declaration is more reliable C-45 trigger than cross-block phrasing that implies the relationship", "V-02 and V-03 structural axes are non-interfering and compose additively to 37/37 — per-block refs and lifecycle summary operate in independent structural zones", "Role ordering is a neutral axis — domain-specific sequencing affects surface presentation not structural depth criteria"]}
```
