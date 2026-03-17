Saved to `simulations/quest/golden/topic-achievements-variate-R2-2026-03-17.md`.

---

# Quest Variate — topic-achievements — Round 2

**Rubric**: v2 (2026-03-17) — adds C-11 (state-column isolation), C-12 (synthesis placement boundary), C-13 (hallucination-safe fallback)

**R1 baseline**: V-02 (table-primary grid) scored 100 and was the source of all three new criteria. R2 isolates each mechanism, then combines.

---

## Variation Summary

| Var | Axis | Hypothesis | C-11 | C-12 | C-13 |
|-----|------|------------|------|------|------|
| V-01 | Output Format | Table State column is independently sufficient for C-11; directive synthesis ordering without explicit boundary holds C-12 at baseline | PASS | borderline | FAIL |
| V-02 | Lifecycle Emphasis | Explicit placement boundary with stated failure mode ("placement after fails") passes C-12 independent of table structure | FAIL | PASS | FAIL |
| V-03 | Phrasing Register | Escape hatch framed as positive permission ("cite namespace only") passes C-13 without requiring any structural change | FAIL | borderline | PASS |
| V-04 | Format + Lifecycle | Table + placement boundary achieves C-11+C-12; missing escape hatch (C-13) is the single gap | PASS | PASS | FAIL |
| V-05 | All three | All mechanisms compose safely — no essential degradation from added prompt surface area | PASS | PASS | PASS |

---

## Mechanism Inventory

**C-11 mechanism** (V-01, V-04, V-05): `Category | Achievement | State | Evidence / Progress | Date` table. State column with exactly one value per row. Empty category rows use `LOCKED` in the State cell. Verification is a column scan, not sentence parsing.

**C-12 mechanism** (V-02, V-04, V-05): Explicit placement rule with a stated consequence — "Placement after per-category classification — including as a closing reflection — fails this requirement." Step ordering alone (synthesis step 2, categories step 3) is treated as borderline; the explicit failure-mode statement is the mechanism.

**C-13 mechanism** (V-03, V-05): Evidence citation rule with a positive escape hatch — "When evidence is uncertain, cite the namespace or skill only (e.g., 'namespace: flow'). Do not invent artifact names. Namespace-level evidence is the preferred safe floor." Framed as permission, not just prohibition.

**Single-axis isolation design**: V-01, V-02, V-03 each hold the other two mechanisms at the baseline (absent or borderline) to confirm each mechanism is independently testable. V-04 adds C-11+C-12 to verify their combination. V-05 adds all three to test compositional safety.
