Written to `simulations/quest/golden/campaign-behavior-variate-R11-2026-03-17.md`.

---

## Quest Variations — campaign-behavior R11

**Rubric:** v9 (C-01–C-31, denominator 23)
**Base:** R10 V-05 (scored 90/90 under v8; retrograded under v9 because C-30/C-31 lack explicit enforcement)

---

### Axes explored

**Single-axis (3):**

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | **C-30 explicit enforcement** — pre-write T-NN registry verification gate in EXECUTIVE SUMMARY | R10 V-05 uses the right format but has no rejection rule for free-form terminal names. A model may substitute component names without triggering a structural failure. |
| V-02 | **C-31 explicit enforcement** — plain `[CONFIRMED]` token declared INVALID in EXECUTIVE SUMMARY confirmation slots | Q2 already audits field 6 citations. A model may reason that Q2 compliance is sufficient and use a shorter form in the summary without being told it's wrong. |
| V-03 | **Phrasing register shift** — imperative → descriptive/explanatory throughout (DEFINITIONS explain WHY, phase headers explain intent) | WHY framing gives edge-case scaffolding. If register is neutral for scoring, V-03 should score identically to R10 V-05 on structural criteria. |

**Combinations (2):**

| Variation | Axes | Hypothesis |
|-----------|------|------------|
| V-04 | C-30 + C-31 enforcement (V-01 + V-02) | The two validity rules operate on orthogonal bullet fields (chain vs confirmation slot) — no structural interference expected. V-04 is the direct 90/90 candidate under v9. |
| V-05 | V-04 + Q7 EXECUTIVE SUMMARY audit gate + Q2 extended to flag summary slots pre-emptively | Three-layer enforcement: rejection at write time (V-04), Q2 pre-audit flag, Q7 dedicated post-write gate. Makes C-30/C-31 as structurally locked as C-29's four-checkpoint model. |

---

### Predicted scores under v9

| Variation | C-30 | C-31 | Aspirational | Total |
|-----------|------|------|-------------|-------|
| V-01 | PASS | FAIL | 22/23 → 10 | **90** |
| V-02 | FAIL | PASS | 22/23 → 10 | **90** |
| V-03 | PASS (format unchanged) | PASS (format unchanged) | 23/23 → 10 | **90** |
| V-04 | PASS | PASS | 23/23 → 10 | **90** |
| V-05 | PASS | PASS | 23/23 → 10 | **90** |

**Key question for scoring:** Does R10 V-05 (the base) already pass C-30 and C-31 structurally, or does it only PARTIAL? V-03 tests this directly — it keeps the exact EXECUTIVE SUMMARY format from R10 V-05 unchanged and only alters the phrasing register elsewhere. If V-03 scores 90, the C-30/C-31 gap was format-level and R10 V-05 already had it. If V-03 scores below 90, the explicit rejection rules in V-01/V-02 are doing real work.
