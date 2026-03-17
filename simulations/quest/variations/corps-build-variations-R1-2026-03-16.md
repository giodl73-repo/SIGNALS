Written to `simulations/quest/golden/corps-build-variate-R1-2026-03-16.md`.

---

## Quest Variate R1 — corps-build

5 variations generated. Summary:

| Variation | Axis | Key Hypothesis | Strongest Criteria |
|-----------|------|----------------|-------------------|
| **V-01** | Role sequence: IA first | Generating IA before any standard role per team eliminates C-03 omission by construction | C-03, C-09 |
| **V-02** | Output format: table-first org-chart | `TABLE-CLOSED` gate before file writing gives a concrete file count target; cross-ref becomes a closing check not a hope | C-06, C-10 |
| **V-03** | Lifecycle emphasis: explicit phase gates | PARSE → VALIDATE → WRITE-CHART → WRITE-ROLES → VERIFY; VALIDATE catches structural failures before any files are written | C-01, C-04 |
| **V-04** | Role sequence + inertia framing | Resistance profiling step before any file writing produces IA files that are genuinely contextualized, not boilerplate | C-03, C-09 (highest) |
| **V-05** | Output format + lifecycle emphasis | Phase gates enforce completeness; prose sections after each table carry level distribution narrative; CROSS-REF is its own dedicated phase | C-01, C-02, C-10 |

**Single-axis axes used**: role sequence (V-01), output format (V-02), lifecycle emphasis (V-03).

**Combination axes**: V-04 combines role sequence + inertia framing; V-05 combines output format + lifecycle emphasis.

**Predicted rubric sensitivity**:
- V-01 and V-04 are the strongest bets for C-03 and C-09
- V-02 is the easiest to audit for C-10 (table total is emitted before file writing begins)
- V-03 is most likely to pass C-01 on an edge-case org.yaml (the VALIDATE phase rejects bad input explicitly)
- V-05 adds the only dedicated CROSS-REF phase, making it the candidate for highest C-10 pass rate
