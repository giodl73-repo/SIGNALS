Written to `simulations/quest/golden/org-review-variate-R12-2026-03-17.md`.

---

# org-review -- Variate R12

5 complete prompt body variations. Single-axis first, then combinations.

**R12 design target**: R11 V-05 predicted 225/225 but scored 210/225 — C-33/C-34/C-35 all absent at execution time despite protocol text being present. R12 identifies the residual failure mode per criterion and applies a stronger binding mechanism:

| Criterion | R11 failure mode | R12 fix |
|-----------|-----------------|---------|
| **C-35** Null Hypothesis Dimension Table | LOCKED sentinel emitted but NH TESTIMONY prose can still introduce off-table assessments — no mechanism rejects uncited claims | **§0 PHASE 2a DIMENSION COUNT BINDING**: bind `dimension_count = N` as filled integer after lock. g_null derivation formula references `dimension_count` by name. NH TESTIMONY must open with "Based on dimension_count=[N]...". Off-table assessments cannot alter the bound count; reference verifiable by inspection. |
| **C-33** Lens Applicability Rating | §17a Basis column present but CITATION VALIDITY RULE is prose instruction — model writes generic archetype text and row is structurally valid | **§17a TYPED ASSERTION BLOCK** replaces Basis column with 3-field typed structure `{surface_anchor, rating_basis, rating}`. `surface_anchor` must contain verbatim §1 text. Verbatim-match is inspectable; generic archetype text fails the test by construction. |
| **C-34** ADVISORY-GAP Domain Coverage | §18 gap-check narratively describes certification — model may conflate domains or skip rows without triggering a detectable error | **§18 FORMAL PREDICATE** `K(d) = |R(d)|`; `K(d) = 0 → ADVISORY-GAP`. **COUNT ASSERTION** `§5.8 certified N domains, M gaps` where N must equal `|S|` declared in §1a. Count mismatch is a detectable protocol error. |

**R12 variation axes:**

- **V-01** — Lifecycle emphasis (C-35): `dimension_count` binding + named reference in derivation formula and NH TESTIMONY opening sentence
- **V-02** — Output format (C-33 → C-34): typed assertion block with verbatim `surface_anchor`; §5.8 uses §17a rating fields as source
- **V-03** — Phrasing register (C-34): formal predicate `K(d) = |R(d)|` + count assertion `certified N domains, M gaps`
- **V-04** — Lifecycle + Output format (C-35 + C-33 → C-34): V-01 + V-02
- **V-05** — Lifecycle + Output format + Phrasing register (C-35 + C-33 + C-34 independent): V-01 + V-02 + V-03; three independent enforcement chains, no single-mechanism cascading failure

**Predicted R12 scores under v11:**

| | C-33 | C-34 | C-35 | Score |
|--|------|------|------|-------|
| V-01 | FAIL | vacuous | PASS | 215/225 |
| V-02 | PASS | PASS (via §17a) | FAIL | 220/225 |
| V-03 | FAIL | PASS (formal predicate) | FAIL | 215/225 |
| V-04 | PASS | PASS | PASS | 225/225 |
| V-05 | PASS | PASS (independent) | PASS | 225/225 |

**V-05 distinguishing property**: C-34 is enforced by two independent mechanisms (§17a source data from V-02 AND formal predicate + count assertion from V-03). No single-mechanism failure cascades to all three criteria.
