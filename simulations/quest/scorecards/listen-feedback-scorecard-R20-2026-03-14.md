# listen-feedback — Round 20 Scoring (Rubric v17)

## Scoring Framework

| Source | Points |
|--------|--------|
| C-01 to C-05 (essential, 15 pts each) | 75 pts max |
| R-01 (recommended, 15 pts) | 15 pts max |
| A-01 to A-31 (aspirational, 5 pts each) | 155 pts max |
| **Total** | **245 pts max** |

PASS = 5 pts · PARTIAL = 3 pts · FAIL = 0 pts (aspirational)

---

## Per-Variation Scoring

### Essential and Recommended (shared baseline — all variations)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 12 persona cards | PASS | PASS | PASS | PASS | PASS |
| C-02 NPS score + justification | PASS | PASS | PASS | PASS | PASS |
| C-03 Severity-labeled feedback | PASS | PASS | PASS | PASS | PASS |
| C-04 Aggregate NPS + threshold | PASS | PASS | PASS | PASS | PASS |
| C-05 Cross-persona theme matrix | PASS | PASS | PASS | PASS | PASS |
| R-01 Blocking issues escalated | PASS | PASS | PASS | PASS | PASS |
| **Subtotal** | **90** | **90** | **90** | **90** | **90** |

All variations preserve the baseline output contract. No variation degrades structural completeness in service of the axis it targets.

---

### Aspirational Criteria — Foundational (A-01 through A-15, A-18–A-20, A-22–A-23, A-26, A-29)

All variations inherit these from the stable protocol base. Assumed **PASS** across the board.

| Criteria group | Pts each variation |
|---|---|
| A-01 to A-15 (15 criteria × 5 pts) | 75 |
| A-18, A-19, A-20, A-22, A-23 (5 × 5 pts) | 25 |
| A-26 persona influence weighting present | 5 |
| A-29 CI formula in output format | 5 |
| **Foundational subtotal** | **110** |

Combined base (essential + foundational): **200 pts** shared by all variations before differentiating criteria.

---

### Aspirational Criteria — Differentiating (A-16, A-17, A-21, A-24, A-25, A-27, A-28, A-30, A-31)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| **A-16** Structured 4-sub-field Current approach | PASS 5 | FAIL 0 | FAIL 0 | PASS 5 | PASS 5 | V-02 has bilateral fields but Field 1 remains prose |
| **A-17** Bilateral gains/losses coverage enforced | FAIL 0 | PASS 5 | FAIL 0 | PASS 5 | PASS 5 | V-01 has sub-fields but NPS justification is single prose; no bilateral split |
| **A-21** Conjunctive framing (each field names the other) | FAIL 0 | PASS 5 | FAIL 0 | PASS 5 | PASS 5 | Requires explicit mutual reference between Gains and Losses fields |
| **A-24** Field completion requires invoking named A-16 sub-field | FAIL 0 | FAIL 0 | FAIL 0 | PASS 5 | PASS 5 | V-02: bilateral exists but no named sub-fields to cross-reference — A-16 prerequisite unmet |
| **A-25** UX-before-PM rationale co-located with ordering instruction | PARTIAL 3 | PARTIAL 3 | PARTIAL 3 | PARTIAL 3 | PASS 5 | V-05 inherits R19 V-05 base; V-01–V-04 have structural ordering, no in-constraint rationale |
| **A-27** Failure mode annotation co-located with constraint | PARTIAL 3 | PARTIAL 3 | PARTIAL 3 | PARTIAL 3 | PASS 5 | V-05 uniquely states epistemic grounding within the constraint instruction itself |
| **A-28** Directional sensitivity: upward/downward delta reported separately | FAIL 0 | FAIL 0 | PASS 5 | FAIL 0 | PASS 5 | V-01/V-02/V-04 use symmetric ±1 figures; asymmetric band-crossing invisible |
| **A-30** Derivation-phase protocol (formula enforced at generation time) | FAIL 0 | FAIL 0 | FAIL 0 | FAIL 0 | PASS 5 | V-01–V-04: A-29 only (formula required at output inspection, not at computation) |
| **A-31** CI formula failure mode named at point of constraint | FAIL 0 | FAIL 0 | FAIL 0 | FAIL 0 | PASS 5 | Co-location required — not satisfied by failure mode stated separately |

---

### Composite Scores

| Variation | Base | A-16 | A-17 | A-21 | A-24 | A-25 | A-27 | A-28 | A-30 | A-31 | **Total** | **% of 245** |
|-----------|------|------|------|------|------|------|------|------|------|------|-----------|-------------|
| V-01 | 200 | +5 | 0 | 0 | 0 | +3 | +3 | 0 | 0 | 0 | **211** | 86.1% |
| V-02 | 200 | 0 | +5 | +5 | 0 | +3 | +3 | 0 | 0 | 0 | **216** | 88.2% |
| V-03 | 200 | 0 | 0 | 0 | 0 | +3 | +3 | +5 | 0 | 0 | **211** | 86.1% |
| V-04 | 200 | +5 | +5 | +5 | +5 | +3 | +3 | 0 | 0 | 0 | **226** | 92.2% |
| **V-05** | 200 | +5 | +5 | +5 | +5 | +5 | +5 | +5 | +5 | +5 | **245** | **100%** |

**Rank:** V-05 (245) > V-04 (226) > V-02 (216) > V-01 = V-03 (211)

---

## Criterion-Level Notes

**A-16 vs A-09 (V-01 split confirmed):** V-01 earns A-16 because it specifies four named sub-fields (What it delivers / Where it falls short / Floor-level switching cost / Persona-specific workflow disruption) — this is more than a bare label. V-02 fails A-16 because its Field 1 is unstructured prose despite having bilateral output fields, confirming A-16 is not satisfied by structural adjacency to the bilateral split.

**A-17 vs A-21 (V-02 split preserved):** V-02 earns both because Field 2 explicitly prohibits completion without Field 3 (A-17 prohibition) and names Field 3 by label (A-21 conjunctive). V-01 fails both because the NPS justification remains a single prose sentence with no bilateral division.

**A-24 gating on A-16 (V-02 failure confirmed):** V-02 has bilateral fields and mutual naming (A-17+A-21), but neither field references a named sub-field from Field 1 — because Field 1 has no named sub-fields. A-24 requires cross-reference to a specific named component of A-16's structure; without A-16, A-24 is structurally unreachable. This confirms A-16 is a prerequisite for A-24.

**A-28 asymmetry (V-03 clean differentiation):** V-03 and V-05 pass; all others fail. The critical evidence: V-01/V-02/V-04 report ±1 as a single symmetric figure. V-03/V-05 emit `Upward delta (+1)` and `Downward delta (−1)` as distinct lines with per-direction band-crossing detection. When a persona sits at the 6/7 threshold, a +1 move crosses to above-threshold while −1 stays sub-threshold — qualitatively different narrative implications that the symmetric figure silently suppresses.

**A-25 and A-27 partial spread:** V-01–V-04 all get PARTIAL on both because structural enforcement is present but the rationale (A-25) or failure mode (A-27) is stated in a separate section, not co-located with the instruction. V-05 passes both because it inherits the R19 V-05 design pattern where the constraint and its epistemic grounding occupy the same step.

**A-30 vs A-29:** The distinction is generation-time vs inspection-time. V-01–V-04 all have A-29 (formula required in output) but not A-30 (formula required as input to derivation). A-30 means an evaluator running D.1→D.2→D.3→D.4 cannot reach D.2 without the formula already stated in D.1 — omission is detectable before output exists. V-01–V-04 can satisfy A-29 by adding the parenthetical retroactively; V-05 cannot because the formula is consumed during computation.

**A-31 co-location:** V-05 only. The failure mode ("without the formula parenthetical, a reader cannot confirm whether the interval was computed via the correct method") appears within the formula constraint instruction. V-01–V-04 that have any failure mode discussion at all place it in a rationale section, not inline with the constraint.

---

## Excellence Signals from V-05

**Signal 1 — Full structural enforcement stack eliminates independent failure categories**
Each major constraint in V-05 is enforced at multiple independent layers: derivation-phase (A-30), output-format (A-29), bilateral prohibition (A-17), conjunctive naming (A-21), sub-field cross-reference gating (A-24), and co-located failure mode annotation (A-31). The key property is independence: satisfying any single layer does not satisfy the others. This means a protocol deviation cannot pass all layers simultaneously — silent compliance failure requires violating at least one detectable structural check.

**Signal 2 — Prerequisite gating creates directed structural dependency chains**
A-24 (gated on A-16) establishes that field completion requires invoking a named component of a structurally prior field. This differs from bilateral prohibition (A-17) and conjunctive naming (A-21): those enforce *mutual presence*, while A-24 enforces *directed reference*. The completing field cannot stand alone — it must cite a specific named sub-field. Omission of the prior field (A-16) makes the downstream reference impossible, not just instructionally prohibited. The dependency chain is now detectable without running the scoring protocol.

**Signal 3 — Directional delta separation reveals asymmetric boundary effects**
The A-28 pattern (upward delta vs downward delta reported as distinct findings) generalizes beyond NPS scoring: any metric with non-symmetric threshold semantics benefits from directional sensitivity reporting. A persona at 6/7 or 8/9 faces qualitatively different narrative implications for a +1 vs −1 move, and symmetric ±figures destroy this signal. The pattern is: whenever score thresholds have different above/below implications, directional deltas are not equivalent and must not be collapsed.

---

## Round 20 Summary

V-05 achieves maximum score (245/245) by being the first variation to hold all four enforcement properties simultaneously across all major constraints: process-level enforcement (derivation phase), bilateral structural coverage, directed dependency gating, and co-located failure mode annotation. V-04 is the strong second (226) — it closes the inertia chain but does not add directional sensitivity or process-level CI enforcement. The V-01/V-03 tie (211) reveals that targeting a single axis (structured sub-fields or directional sensitivity) without building the bilateral enforcement chain leaves half the structural gap open.

---

```json
{"top_score": 245, "all_essential_pass": true, "new_patterns": ["Full structural enforcement stack: applying derivation-phase, output-format, bilateral prohibition, conjunctive naming, sub-field cross-reference gating, and co-located failure mode annotation simultaneously makes silent compliance failure detectable at independent layers — no single layer's violation can be hidden by satisfying another", "Prerequisite field gating (A-24 on A-16): requiring gain/loss field completion to explicitly invoke a named sub-field from a structurally prior baseline creates a directed dependency chain where omission of the prior field makes downstream compliance structurally impossible, not merely instructionally prohibited", "Directional delta separation (A-28): any metric with non-symmetric threshold semantics requires upward and downward deltas reported as distinct findings — symmetric ±figures suppress asymmetric band-crossing effects at score boundaries where the same absolute change produces qualitatively different narrative implications by direction"]}
```
