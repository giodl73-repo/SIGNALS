Written to `simulations/quest/golden/mock-all-variate-R13-2026-03-15.md`.

---

## Round 13 — Five Variations

**What R13 is testing:** Two new criteria added in v13 — C-28 (gate self-annotation declaring its field list as required verbatim column names) and C-29 (inertia gap skeleton seed content pre-authored in template body, not model-generated). Denominator rises from 19 to 21.

### Axis-Assignment Summary

| Variation | Axis | C-26 | C-27 | C-28 | C-29 | Predicted |
|-----------|------|------|------|------|------|-----------|
| V-01 | Role-sequence: seed phrases in template, paraphrase gate | PASS | FAIL | FAIL | **PASS** | 19/21 |
| V-02 | Output-format: verbatim gate + annotation, no seeds | uncertain | PASS | **PASS** | FAIL | 20/21 |
| V-03 | Output-format: verbatim gate, annotation omitted | uncertain/FAIL | PASS | **FAIL** | FAIL | 18–19/21 |
| V-04 | Combination: model-specific instruction + verbatim gate + annotation | **PASS** | PASS | PASS | **FAIL** | 20/21 |
| V-05 | Combination ceiling: seeds + verbatim gate + annotation | **PASS** | PASS | PASS | **PASS** | 21/21 |

### What Each Variation Tests

**V-01** — Isolates C-29. Template pre-authors all 9 seed phrases; model copies them verbatim. Gate uses paraphrase descriptions, so C-27/C-28 stay dark. Confirms C-29 PASS is achievable without the gate-structure chain.

**V-02** — Isolates C-28. Gate names verbatim column headers and adds the self-annotation ("The column names listed here are the required verbatim field names"). No seed phrases provided — C-29 must FAIL. Confirms C-28 PASS without C-29.

**V-03** — Tests C-28 independence from C-27. Same verbatim-gate structure as V-02 but annotation deliberately omitted. Expected C-27 PASS + C-28 FAIL. The generic skeleton fill instruction also sets up the C-26 FAIL + C-29 FAIL third case of the 3-way separation matrix.

**V-04** — Middle case of C-26/C-29 3-way separation. Template instructs the model to generate namespace-specific content (description-of-phrase, not the phrase itself) — C-26 likely PASS because the instruction drives specificity, but C-29 FAIL because no seed phrases exist in the template. Gate-structure chain at ceiling (C-27 + C-28) to isolate the effect.

**V-05** — Full 12-criterion table-coupling cluster ceiling. Seed phrases cascade through C-29 → C-26 → C-21 → C-10 + C-17. Annotated verbatim gate cascades through C-28 → C-27 → C-16 → C-11 + C-14. All 21 aspirational criteria targeted simultaneously.
