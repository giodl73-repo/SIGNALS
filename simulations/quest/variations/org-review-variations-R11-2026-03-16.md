Written to `simulations/quest/golden/org-review-variate-R11-2026-03-17.md`.

---

## org-review -- Variate R11 (v11 rubric)

**Gap analysis from R10 V-05:**

| Criterion | R10 failure mode |
|-----------|-----------------|
| C-33 | §17 says "not from role definition" but has no enforcement. Model writes generic archetype citations. |
| C-34 | §18 infers domains from §1 surfaces at §5.8 time -- late-binding, inconsistent domain decomposition. |
| C-35 | §0 table exists but NH TESTIMONY prose may introduce assessments not traceable to any table row. |

**Five variations:**

| Variation | Axis | New mechanism | Predicted score |
|-----------|------|---------------|----------------|
| V-01 | Inertia framing | `DIMENSION TABLE LOCKED` sentinel in §0 PHASE 2 -- NH TESTIMONY is structurally subordinate, no admissible assessments outside table rows | 215/225 (C-35 only) |
| V-02 | Output format | §17a SURFACE CITATION REQUIREMENT -- each §5.7 row gains a `Basis (§1 citation)` column; archetype-only basis is explicitly INVALID and triggers ADVISORY-OPEN-LENS | 220/225 (C-33+C-34) |
| V-03 | Lifecycle emphasis | §1a ARTIFACT DOMAIN INVENTORY -- atomic domains locked from §1 surfaces before any reviewer runs; §18 operates on this inventory, not late-inferred labels | 215/225 (C-34 only) |
| V-04 | V-01 + V-02 | Lock gate + surface citation | 225/225 (C-33+C-34+C-35) |
| V-05 | V-01 + V-02 + V-03 | Lock gate + surface citation + pre-locked domain inventory (strongest enforcement chain; §1a feeds §18; §17a validates §17; §0 PHASE 2 locks g_null source) | 225/225 (all three, strongest) |

V-04 and V-05 are both 225/225 candidates. V-05 is the preferred golden path because it also hardens C-34 against the late-binding domain inference problem that would re-surface in deeper scoring runs.
