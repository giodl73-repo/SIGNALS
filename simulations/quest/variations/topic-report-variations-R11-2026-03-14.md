Written to `simulations/quest/rubrics/topic-report-rubric-v11-variations-R11-2026-03-15.md`.

---

## Round 11 Variations -- `topic-report`

**Base**: R10 V-04 (31/31 under v11)
**Discriminator targets**: Two asymmetric single-axis extensions targeting the V-01=V-02 tie at 26/31.

| Variation | Axis | Key change | v11 score |
|-----------|------|------------|-----------|
| **V-01** | D only | Adds `SLOT 3 contamination consequence:` line to Branch A recovery directive -- names the structural substitution and criterion IDs (C-04, C-13, C-16) violated if Branch B template is applied at SLOT 3 | 26/31 = 98.4 |
| **V-02** | E only | Adds structural format-type qualifiers to Branch B dual-mapped register entries: `READINESS LINE / BRANCH B (one card row, no markdown)`, `NEXT STEP LINE / BRANCH B (two card rows, no markdown)` | 26/31 = 98.4 |
| **V-03** | D+E | Both axes on R10-V-03 base | 28/31 = 99.0 |
| **V-04** | D+E+F | All three + temporal-role annotation on register header: `=== CONTRACT REGISTER [TEMPORAL ROLE: planning phase -- read before branch dispatch...] ===`; Coordination line updated to reference the temporal-role declaration | 31/31 = 100.0 |
| **V-05** | neutral | R10 V-04 verbatim | 31/31 = 100.0 |

**Candidate composites for v12**:
- **C-43** = C-40 + C-16: same-position double-gate at SLOT 3 / BRANCH A (contamination warning fires at recovery header → scan executes before write)
- **C-44** = C-41 + C-25: format-type-aware Branch B self-containment arc (format types at register + independent Branch B header)
- **C-45** = C-42 + C-36: dual temporal declaration (register header names planning phase; write-point coordination statement names the planning-to-recovery relationship; each endpoint declared explicitly)

**Open question**: Whether C-43's same-position double-gate is a structurally distinct composite class from C-44's temporal-coordination arc will determine if the V-01=V-02 tie breaks under v12. If they score symmetrically, the tie persists and R12 must find a genuinely asymmetric axis. If C-43 scores while C-44 doesn't (or vice versa), the tie breaks and the asymmetry is real.
