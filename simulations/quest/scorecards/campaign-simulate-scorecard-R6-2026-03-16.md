# Quest Score — campaign-simulate (Round 6, v6 Rubric)

## Scoring Baseline

R5 V-05 scores **106/110** under v6 (96.4 normalized) — all criteria except C-22 and C-23 pass by construction. Each new criterion is worth 2 pts (aspirational); both needed for 100.

---

## Criterion-by-Criterion Evaluation

### Essential (C-01–C-05) — All Variations

All five variations inherit the R5 V-05 base, which passes all essential criteria by construction.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Structural Axis Declaration | PASS | PASS | PASS | PASS | PASS |
| C-02 Sub-Skill Execution Order | PASS | PASS | PASS | PASS | PASS |
| C-03 Findings Report Produced | PASS | PASS | PASS | PASS | PASS |
| C-04 Blast Radius Ranking | PASS | PASS | PASS | PASS | PASS |
| C-05 (5th essential) | PASS | PASS | PASS | PASS | PASS |

**Essential subtotal: 50/50 for all variations.**

---

### Recommended (C-06–C-08) — All Variations

Inherited from R5 V-05 base.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-06 | PASS | PASS | PASS | PASS | PASS |
| C-07 | PASS | PASS | PASS | PASS | PASS |
| C-08 | PASS | PASS | PASS | PASS | PASS |

**Recommended subtotal: 30/30 for all variations.**

---

### Aspirational (C-09–C-21) — All Variations

All 13 criteria pass by construction from the R5 V-05 base.

**Aspirational subtotal (C-09–C-21): 26/26 for all variations.**

---

### New Aspirational Criteria (C-22, C-23)

#### C-22 — Observational Discipline as Co-Equal Structural Axis

Row 5 of the axis declaration table must carry the same `Observable Output` column depth as rows 1–4: 3+ distinct named sub-observables, not just a summary phrase.

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| **V-01** | **PASS** | Explicitly adds depth requirement to axis declaration; row 5 names three sub-observables (genre section, T-1 filter log, per-scope gates). Evaluator can verify C-22 from the declaration table alone. |
| **V-02** | **PARTIAL** | Built on R5 V-05 base which has observational discipline as a structural axis, but the variation's focus is the T-1 ANNEX — it does not explicitly enforce 3+ named sub-observables in the axis row. Depth is implied, not declared. |
| **V-03** | **PARTIAL** | Same reasoning as V-02: T-1 evidence is distributed to per-scope gate tables, which satisfies T-1 falsification but does not directly address axis-row depth. Sub-observables can be inferred from the Disposition column but are not co-located in the declaration table. |
| **V-04** | **PASS** | Combines V-01's axis-depth requirement with V-02's T-1 ANNEX. Row 5 carries explicit 3+ sub-observables by design. |
| **V-05** | **PASS** | Same as V-04 plus hardened partial compliance. Row 5 depth is unchanged from V-04 — PASS identical. |

#### C-23 — T-1 Must Be Falsified (Rejection Citation Required)

The filter log or its resolution must cite a named observation that was evaluated, failed T-1, and was withheld. Declaration alone is insufficient.

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| **V-01** | **FAIL** | Row 5 adds three named sub-observables, but no mechanism is introduced to record a T-1 rejection. The filter log remains a declaration instrument, not a falsification instrument. No named withheld observation present. |
| **V-02** | **PASS** | Introduces `T-1 ANNEX` as a mandatory named block post-Template A/B. The ANNEX must name a withheld-T1 observation or invoke T-1 RECALIBRATION. Report cannot close without it — T-1 is structurally falsifiable by design. |
| **V-03** | **PASS** | Distributes T-1 evidence across per-scope gate tables via a `Disposition` column (elevated / withheld-T1 / withheld-rule). `T-1 EVALUATION SUMMARY` aggregates across all five scopes. Evidence is co-located with execution; any scope showing `withheld-T1` constitutes a named rejection. |
| **V-04** | **PASS** | Carries V-02's mandatory T-1 ANNEX on the R5 V-05 base. Compliance checklist row 6 cites the named T-1 rejection explicitly. |
| **V-05** | **PASS** | Same as V-04 plus compliance checklist row 6 uses `fired/partial/not fired` with three independently-verifiable sub-claims. The partial verdict names which sub-claim failed. Architecture bonus is excluded from scoring per rubric preamble — but T-1 falsification is unambiguous PASS. |

---

### Score Summary

| Variation | Essential | Recommended | C-09–C-21 | C-22 | C-23 | Raw | Normalized |
|-----------|-----------|-------------|-----------|------|------|-----|------------|
| **V-01** | 50 | 30 | 26 | 2 | 0 | 108 | **98.2** |
| **V-02** | 50 | 30 | 26 | 1 | 2 | 109 | **99.1** |
| **V-03** | 50 | 30 | 26 | 1 | 2 | 109 | **99.1** |
| **V-04** | 50 | 30 | 26 | 2 | 2 | 110 | **100.0** |
| **V-05** | 50 | 30 | 26 | 2 | 2 | 110 | **100.0** |

*Divisor: 1.10. PARTIAL = 1 pt.*

---

## Ranking

| Rank | Variation | Score | Distinguishing Feature |
|------|-----------|-------|------------------------|
| 1 | **V-04** | 100.0 | Cleanest integration of C-22 + C-23 with minimal structural overhead |
| 1 | **V-05** | 100.0 | Same as V-04 + hardened partial compliance (not scored, but auditably superior) |
| 3 | **V-02** | 99.1 | C-23 via mandatory T-1 ANNEX; C-22 implied but not declared |
| 3 | **V-03** | 99.1 | C-23 via per-scope Disposition column; C-22 same gap as V-02 |
| 5 | **V-01** | 98.2 | C-22 fully resolved; C-23 entirely absent — no rejection mechanism |

---

## Excellence Signals — V-04 / V-05

**What made V-04/V-05 strictly better than V-01, V-02, V-03:**

1. **Conjunctive compliance requires conjunctive design.** V-01 solved C-22 alone; V-02/V-03 solved C-23 alone. Neither variation is sufficient — C-22 and C-23 are structurally interdependent (an axis cannot be co-equal if it is unfalsifiable; a T-1 rejection is unverifiable without named sub-observables to reject against). V-04 earns both by designing the axis row and the rejection mechanism as a single integrated unit.

2. **Depth in the declaration enables falsification downstream.** V-01 showed that naming 3+ sub-observables in the axis row is necessary. V-02 showed that a mandatory ANNEX is necessary. V-04 shows that the sub-observable names in the axis row are what give the T-1 ANNEX referents to cite — the declaration table and the rejection log point to the same named entities.

3. **V-05 extension (architecture bonus, excluded from scoring):** The `fired/partial/not-fired` sub-claim decomposition in compliance checklist row 6 makes partial verdicts auditable at sub-claim granularity. While excluded from v6 scoring per rubric preamble, this pattern represents a structural advance in compliance verifiability that prior rounds have not captured.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Sub-claim granularity in partial compliance verdicts — V-05 names which sub-claim of a multi-part criterion failed, making partial verdicts independently verifiable without re-running the full skill; this pattern may warrant a future criterion when compliance checklists carry 3+ sub-claims per row"]}
```
