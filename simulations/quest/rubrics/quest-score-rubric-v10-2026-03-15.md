Written to `simulations/quest/rubrics/quest-score-rubric-v10-2026-03-16.md`.

---

**Summary of v9 → v10 changes:**

**Two new aspirational criteria from R9 excellence signals:**

| ID | Name | Source | Strengthens |
|----|------|---------|-------------|
| C-30 | SYNTHESIS — intra-phase timing order in injection-point map | V-04/V-05, R9 | C-28 |
| C-31 | SYNTHESIS — per-axis correspondence enumeration in two-path equivalence signal | V-04/V-05, R9 | C-29 |

**C-30** tightens C-28: when two axes share the same phase (C-25 and C-27 both in VERIFIER), asserting "different timing positions" is not enough — the signal must name which position each occupies (C-25 fires post-write before audit table; C-27 fires post-correction-loop before gate token) and confirm non-overlap explicitly.

**C-31** tightens C-29: asserting "equivalent coverage" is not enough — the signal must enumerate per-axis adversarial↔template correspondences by criterion ID (AUDIT C = CHECK F for C-22/C-23/C-24) and confirm that SYNTHESIS-phase criteria (C-26, C-27) are path-agnostic (architecturally identical on both paths regardless of which Verifier architecture was used).

**Additional tightening applied to C-16:** Pass condition now requires *quoted* examples (literal text extracts), not described examples. PARTIAL added for declared-but-unquoted case, matching the R9 finding that V-02/V-03 declared equivalence without exemplifying it. C-03 updated to /23 denominator. N_aspirational: 21 → 23. Roster: 29 → 31 rows.

**Score benchmarks:**
- Both C-30/C-31 missing: 99.13
- One missing: 99.57
- Full combination: 100.00
