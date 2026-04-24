Written to `simulations/quest/golden/crew-roles-variate-R2-2026-03-17.md`.

---

## crew-roles Variate R2 — Summary

**5 variations targeting the 3 new v2 aspirational criteria.**

### Single-axis (V-01, V-02, V-03)

| Variation | Axis | Primary target | Hypothesis |
|-----------|------|----------------|------------|
| **V-01** | Vocabulary-Forced-Field | C-11 | Phase 1 vocabulary extraction, each `expertise.relevance` must reference at least one term from it — prevents generic infill structurally |
| **V-02** | Inertia Pre-Characterization | C-12 | Explicit 3-question block (current system / migration cost / user habits) before writing inertia-advocate; verify questions must reference at least 2 of 3 dimensions |
| **V-03** | Registry Summary Table | C-13 | Mandatory post-write table (Role / Orientation / Scope / Collaborates With) with orphan check and scope gradient check at execution time |

### Two-axis combinations (V-04, V-05)

| Variation | Axes | Hypothesis |
|-----------|------|------------|
| **V-04** | C-11 + C-12 | Vocabulary feeds inertia characterization — the current system named in vocabulary is what the inertia questions must challenge; neither can drift to generic language because each is anchored to the other |
| **V-05** | C-11 + C-12 + C-13 (full) | Phase-gated: vocabulary → inertia characterization → role files → summary table self-verification; all three aspirational criteria satisfied structurally, each phase feeding the next |

### Design choices worth noting

- V-01 allows inferred vocabulary terms (labeled `[inferred]`) to handle sparse input without blocking
- V-02's inertia constraint requires proper nouns, not "existing approach" — closes the generic drift path
- V-03's table includes a **two-check pass**: orphan references and scope gradient, both auto-corrected before delivery
- V-05 adds an inertia-advocate `orientation.frame` constraint that requires the current system name to appear **verbatim** — the strictest binding of C-12's intent
