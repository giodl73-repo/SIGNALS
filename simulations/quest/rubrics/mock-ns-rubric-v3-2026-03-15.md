Written to `simulations/quest/rubrics/quest-rubric-mock-ns-v3-2026-03-15.md`.

**What changed in v3:**

Two new aspirational criteria from Round 2 excellence signals:

- **C-14** — FLAG immutability declared at *both* the compute site and the consumption site. C-11 only requires the compute step precedes assembly; C-14 requires explicit "do not rederive" prohibition at both sites. V-01, V-03, and V-04 all carry this pattern; V-02 (which fails C-11 entirely) fails C-14 automatically. This closes the residual risk that a model re-derives the flag at header time despite a compute step being present.

- **C-15** — Default skill table uses a dedicated structural column for exclusion constraints, not inline annotation. C-12 requires the exclusion language to exist; C-15 requires it be elevated to a named table column (e.g., three-column table: namespace | default skill | exclusion note). V-03's "Exclusion column contains hard constraints" and V-04's S-2 column structure both exhibit this. Bracket annotations and appended prose pass C-12 but fail C-15 — they're visible to a careful reader but not structurally enforced.

**Scoring update:** Aspirational denominator changes from 5 to 7 (`pass/7 * 10`). Round 2 retro-scores: V-04 = 100, V-03 ≈ 98.6, V-01 ≈ 97.1, V-02 ≈ 94.3.
