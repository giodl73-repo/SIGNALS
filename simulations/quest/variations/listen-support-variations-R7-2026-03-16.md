Written to `simulations/quest/golden/listen-support-variate-R7-2026-03-16.md`.

---

## listen-support — R7 Variations Summary

**Rubric target:** v7 (C-01 through C-25, max 175 pts)
**Baseline:** R6 V-05 (predicted 160/175 — C-23, C-24, C-25 open)

### Variation axes

| Variation | Axis | Target | Mechanism |
|-----------|------|--------|-----------|
| **V-01** | Lifecycle emphasis | C-25 | Adds STEP 10 CRITERION VERIFICATION SPINE — one row per C-ID (C-01 through C-25), replacing VERIFICATION MANIFEST |
| **V-02** | Output format | C-24 | Adds VOCABULARY MATERIALIZATION section after STEP 3B — maps VM Row ID → STEP 3B → ## headline, with orphan-gap check (type A + type B) |
| **V-03** | Phrasing register | C-23 | Adds `[C-NN: BELT]` labels at all generation steps; `[C-NN: SUSPENDERS]` labels in VERIFICATION MANIFEST rows — redundant enforcement visible and named |
| **V-04** | Combined | C-23 + C-25 | Belt labels at generation + STEP 10 spine as consolidated suspenders layer; no materialization |
| **V-05** | Full synthesis | C-23 + C-24 + C-25 | All three mechanisms stacked on R6 V-05 base; STEP 10 spine declares its own `[C-25: BELT confirmed]`; first composite 175 candidate under v7 |

### Key structural decisions

- **C-25 spine design (V-01, V-04, V-05):** STEP 10 as a named output step rather than an appended table. Forces the spine to be a first-class section the model commits to completing. Scorer reads only the spine table to determine all 25 criterion states.

- **C-24 orphan model (V-02, V-05):** Two orphan types explicitly named — type A (manifest rows with no commitment) checked at planning time; type B (commitment rows with no body) checked post-STEP 6. The two-pass structure closes the gap that a single pre-generation check misses.

- **C-23 label convention (V-03, V-04, V-05):** `[C-NN: BELT]` inline in instruction text; `[C-NN: SUSPENDERS]` inline in the spine table's C-ID column. The labels are grep-checkable. A scorer can verify "C-14 has a belt label at STEP 2 and STEP 4, and a suspenders row in STEP 10" in two searches.

- **V-05 self-reference:** The COMPLIANCE CONTRACT in V-05 includes belt labels for C-23, C-24, and C-25 themselves — the new criteria are enforced by the same mechanism they define.
