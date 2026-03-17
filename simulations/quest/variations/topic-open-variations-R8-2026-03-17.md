Written to `simulations/quest/golden/topic-open-variate-R8-2026-03-17.md`.

---

**R8 variation summary:**

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | AMEND completeness | Named AMEND blocks for all 5 Phase 5 items (not just C-04); uniform label format creates scannable repair surface |
| V-02 | Gate failure routing | GATE FAILURE line after Phase 2 exit gate routes to return phase; detection without routing is incomplete |
| V-03 | Recovery column | 6th column in DEFAULTS THIS SKILL OVERRIDES; repair at constraint-level before reaching Phase 5 |
| V-04 | V-01 + V-02 | Gate routing → Phase 2 → named AMEND per item; full correction chain |
| V-05 | V-01 + V-02 + V-03 | Three-layer repair cascade: matrix-level (V-03) → gate-level (V-02) → item-level (V-01) |

**Predicted scoring:**
- V-01: passes C-31 (AMEND completeness), fails C-32/C-33
- V-02: passes C-32 (gate failure routing), fails C-31/C-33
- V-03: passes C-33 (recovery column), fails C-31/C-32
- V-04: passes C-31 + C-32, fails C-33
- V-05: passes all three — candidate golden

The scorecard will determine whether these three axes constitute distinct criteria or whether any two collapse into the same criterion.
