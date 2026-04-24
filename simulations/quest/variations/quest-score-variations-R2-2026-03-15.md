Written to `simulations/quest/golden/quest-score-variate-R2-2026-03-15.md`.

---

## Summary

**5 variations generated for quest-score Round 2 against rubric v2.**

### Axes selected

| Axis | Target criteria | Mechanism |
|------|-----------------|-----------|
| A — Rubric-derivation-first | C-11 | DERIVE phase gate forces E_count/R_count/A_count derivation before any output file is opened; formula written symbolically, never as resolved literals |
| B — Labeled-field slots | C-09, C-12 | Required `Golden:` field per output block; required `Pattern:/Diagnosis:/Rationale:` template per failure entry; unfilled slots are structurally visible |
| C — Formula anti-pattern | C-11 | Concrete negative example showing the exact R1 failure (hardcoded `/5`, `/2`, `/1`) with a targeted check: "if a numeric literal appears in a denominator position — replace it" |

### Variation map

| Variation | Axes | Primary hypothesis |
|-----------|------|--------------------|
| V-01 | A | One derivation gate at the start is sufficient for C-11 |
| V-02 | B | Slot-fill format closes C-09/C-12 without degrading C-10 rationale depth |
| V-03 | C | Targeted negative anchor produces C-11 compliance vs. shifting which literals are hardcoded |
| V-04 | A+B | Combination closes C-09/C-11/C-12 independently without evidence regression on C-02 |
| V-05 | A+B+C | All three axes at different lifecycle points (before open, Phase 1, Phases 3-4) produce highest-probability full pass on the three new aspirational criteria |

### Key design decisions vs R1

- **No literal denominators anywhere in the skill body.** R1's universal failure was that all variations stated the formula with `/2` and `/1`. R2 variations state only named variables; the anti-pattern explicitly calls out `/5`, `/2`, `/1` as the wrong mechanism.
- **`Golden:` is a required labeled field, not a derivation from the score table.** This closes C-09 structurally.
- **`Pattern/Diagnosis/Rationale:` template is present in all 5 variations** (unlike R1 where V-01/V-02/V-03 used prose). The question is whether the template is enforced by phase gates (V-01), slot prescription (V-02/V-04/V-05), or both.
