Written to `simulations/quest/rubrics/quest-score-rubric-v13-variations-R13-2026-03-15.md`.

---

## R13 Variations — V-01 through V-05

**Design notes summary:**

N_aspirational updated 25 → 29. Roster 32 → 36 rows. Four new structural additions for R13 that all five variations must get right or ablate cleanly:

| New | What it is |
|-----|-----------|
| C-33 | SETUP activation declaration for conditionally-scoped criteria when C-07 fires |
| C-34 | Step 1.4 variation axis summary with formula-derived predicted delta |
| C-35 | C-33 diagnostic question must enumerate FAIL/PARTIAL/PASS with examples |
| C-36 | C-34 diagnostic question must enumerate FAIL/PARTIAL/PASS with examples |

**Variation axes and predictions:**

| Variation | Axis | Predicted verdict | Mechanism |
|-----------|------|-------------------|-----------|
| V-01 | Baseline — R13 full stack | All R13 criteria PASS | All new structures intact |
| V-02 | Lifecycle emphasis | C-33 PARTIAL | "C-31 -- active" written without trigger rationale |
| V-03 | Output format | C-34 PARTIAL | Delta column present but "minor penalty" not "−0.172 pt (PARTIAL × 10/29)" |
| V-04 | Phrasing register | C-35 PARTIAL + C-36 PARTIAL | C-33/C-34 diagnostics enumerate only FAIL and PASS, PARTIAL boundary omitted |
| V-05 | Combination (V-02 + V-03) | C-33 PARTIAL + C-34 PARTIAL | Additive degradation ≈ −0.344 pt from V-01 ceiling |

**Key structural differences across variations:**

- `Step 1.1` C-07 cascade block: V-01/V-03/V-04 include trigger rationale in activation declarations; V-02/V-05 write status-only ("C-31 -- active")
- `Step 1.4` delta column instruction: V-01/V-02/V-04 specify formula-derived values; V-03/V-05 specify qualitative descriptors
- `Step 1.4` C-33 diagnostic: V-01/V-02/V-03/V-05 enumerate three cases; V-04 enumerates two
- `Step 1.4` C-34 diagnostic: V-01/V-02/V-03/V-05 enumerate three cases; V-04 enumerates two
