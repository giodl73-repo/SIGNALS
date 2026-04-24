Saved to `simulations/quest/golden/draft-proposal-variate-R20-2026-03-15.md`.

---

## Round 20 — draft-proposal Variates V-01..V-05

**Rubric**: v20 · Denominator: /42 · New criteria: C-48 (T-46 CONDITION carries inline exemplar of Part-1-only T-42 state) and C-49 (T-47 CONDITION carries inline exemplar of T-42-exemplar-without-explanation state)

### Variation summary

| Variation | Axis | T-42 | T-46 | T-47 | T-24 | Designed fails | Score |
|-----------|------|------|------|------|------|----------------|-------|
| **V-01** | Phrasing register | golden (Part 1+2) | **abstract** | golden (exemplar) | 49 | C-48 | **99.76** |
| **V-02** | Output format | golden (Part 1+2) | golden (exemplar) | **abstract** | 49 | C-49 | **99.76** |
| **V-03** | Lifecycle emphasis | golden (Part 1+2) | **abstract** | **abstract** | 49 | C-48 + C-49 | **99.52** |
| **V-04** | Role sequence + inertia framing | golden (Part 1+2) | golden (exemplar) | **abstract** | **47 (stale)** | C-24 + C-49 | **99.52** |
| **V-05** | Phrasing register + lifecycle | **abstract** | abstract (cascade) | abstract (cascade) | 49 | C-45→C-46+C-47+C-48+C-49 | **98.81** |

### Key design decisions

**V-01 vs V-02**: Symmetric single-axis probes. V-01 tests whether T-46's phrasing register drives C-48 independently of T-47. V-02 mirrors it for T-47/C-49. Both predict 41/42 — live demonstrations that C-48 and C-49 are mutually independent.

**V-03**: Both T-46 and T-47 abstract simultaneously. Proves C-48 and C-49 can co-fail without cascading from each other. 40/42 with no cascade root.

**V-04**: Stale 47-row count (v19 spec carried forward without adding T-48/T-49). C-24 fires because rubric requires 49 rows. T-47 abstract adds C-49 as a second independent fail. T-46 golden → C-48 PASS, demonstrating that T-46's CONDITION cell is evaluable even within a stale-count table.

**V-05**: Maximum cascade test. T-42 abstract → C-45 FAIL → all downstream criteria (C-46, C-47, C-48, C-49) cascade deterministically. T-40 is fully specified (C-42+C-43+C-44 PASS) to isolate the cascade root at T-42 exactly. 5 fails, 37/42.

### Cascade invariants confirmed by R20 design

- C-48 independent fail: T-46 CONDITION can be abstract (C-48 FAIL) when C-45 PASS, C-46 PASS, C-47 PASS — V-01 is the live demonstration
- C-49 independent fail: T-47 CONDITION can be abstract (C-49 FAIL) when C-45 PASS, C-47 PASS — V-02 is the live demonstration  
- C-48 ⊥ C-49: V-03 shows co-fail with no cascade relation between them
- C-45 FAIL → C-48 + C-49 cascade: V-05 demonstrates both cascade deterministically when T-42 is fully abstract
