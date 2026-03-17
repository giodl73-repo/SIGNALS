`narrate-behavior-rubric-v10-2026-03-17.md` written.

**What changed from v9:**

| Change | Detail |
|--------|--------|
| **C-31 updated** | Pass condition now explicitly requires the 4-term form (`N_finding + N_covered + N_investigation + N_none`). 3-term `N_inertia_rows` form is a named FAIL. Cross-artifact equality (`N_investigation = TRIAGE GATE count`) codified as the strongest C-28 realization. |
| **C-23 updated** | Added note: condensed DEFINITIONS referencing ratio codes `(a)/(b)/(c)` without per-form required statements fails this criterion -- confirmed by V-43. |
| **C-32 added** | Risk Density Matrix -- 3x3 grid (Blast Radius x Severity) with F-IDs per cell. REQUIRE: every F-ID in exactly one cell. Orthogonal to sorted table and DISCOVERY PATHWAY AUDIT. |
| **C-33 added** | Lifecycle Phase Structure in S3 -- INIT/NOMINAL/DEGRADED/TEARDOWN/HANDOFF with per-phase PHASE EXIT CONDITIONs. S3 aggregate EXIT GATE sums phases. REPORT gains S3 phase breakdown table. |
| **C-34 added** | Boundary Risk Density Score -- RDS = sum(blast_weight) per B-ID (WIDE=3/MED=2/NARROW=1). Portfolio-level invariant: sum(all RDS) = total blast-weighted finding count. Orthogonal to C-22 and C-32. |
| **Aspirational threshold** | Any 13 of 27 (was 12 of 24). |
