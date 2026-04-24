Written to `simulations/quest/golden/corps-scan-variate-R3-2026-03-17.md`.

---

## R3 Variate — corps-scan

**5 variations targeting the 3 new v3 criteria** (C-14, C-15, C-16). All variations carry forward the full R2 baseline (C-01 through C-13 all covered), including: Signal ID typed table (C-11), named Signal ID in pivot rationale (C-12), and hard ordering gate (C-13).

### Variation Axes

| Variation | Axis | Primary Mechanism |
|-----------|------|-------------------|
| **V-01** | Output format | `NOT COMPLETE UNTIL` headers (C-15) + gate-row as terminal table row (C-14) + one-sentence repair instruction in constraints (C-16) |
| **V-02** | Lifecycle emphasis | Phase Completion Test blocks as required output per phase (C-15); `Gate row present: YES/NO` field (C-14); `Traceability failures > 0 → return to Phase 1` (C-16) |
| **V-03** | Phrasing register | `INVARIANT / VIOLATION / REPAIR` triples per phase; Phase 1 invariant requires gate-row (C-14); Phase 3 REPAIR block names return-to-phase (C-16) |
| **V-04** | Output format + Lifecycle | Dual gate: `NOT COMPLETE UNTIL` header pre-phase + Completion Test post-phase (C-15 × 2); gate-row in table (C-14); repair in completion test (C-16) |
| **V-05** | Role sequence + Phrasing | Invariant-gated SCANNER/ANALYST/DRAFTER; SCANNER exit invariant requires gate-row (C-14); per-role entry conditions (C-15); DRAFTER VIOLATION/REPAIR block (C-16) |

### Key R3 Design Decisions

- **C-14 is uniform across all 5**: every variation uses the gate row as the terminal row of the typed inventory table. The structural inseparability from R2 V-04 is preserved.
- **C-15 varies by placement**: pre-phase (V-01/V-04), post-phase (V-02/V-04), INVARIANT block (V-03/V-05), role entry condition (V-05).
- **C-16 varies by form**: inline sentence (V-01/V-04), completion test field (V-02), REPAIR block (V-03/V-05) — all valid under the rubric.
- **C-10 PASS**: all five explicitly instruct the model to output the draft boundary statement before structural content.
