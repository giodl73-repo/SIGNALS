Written to `simulations/quest/golden/corps-build-variate-R2-2026-03-16.md`.

---

## Quest Variate R2 — corps-build

5 variations generated. Summary:

| Variation | Axis | Key Hypothesis | New Criteria Targeted |
|-----------|------|----------------|-----------------------|
| **V-01** | Lifecycle: VALIDATE as hard pre-write gate | VALIDATE-PASS gate makes C-11 impossible to elide; IA-first inside WRITE catches C-12 | C-11, C-12 |
| **V-02** | Output format: table-as-contract + mandatory prose | Table as literal first artifact = C-13 by construction; required prose after each table = C-14 | C-13, C-14 |
| **V-03** | Phrasing register: output-forward / reviewer perspective | Showing expected output (with good/weak examples) guides C-14 prose quality and C-09 depth | C-14, C-09 |
| **V-04** | Resistance profiles + table contract + IA-first (combination) | Table locks file count, profiles lock IA content plan, IA-phase locks ordering — three criteria, one linear sequence | C-09, C-12, C-13, C-14 |
| **V-05** | Full integration — all four new criteria (combination) | Minimal mechanism per criterion: VALIDATE(C-11) + table-first(C-13) + prose(C-14) + IA-phase(C-12) | C-11, C-12, C-13, C-14 |

**Single-axis axes**: lifecycle emphasis (V-01), output format (V-02), phrasing register (V-03).

**R1 gap addressed**: No R1 variation satisfied all four new criteria. V-05 is the first variation targeting C-11+C-12+C-13+C-14 simultaneously.

**Predicted sensitivity**:
- V-01 and V-05 are strongest bets for C-11 (VALIDATE is the structural centerpiece in both)
- V-02 and V-04 are strongest for C-13 (table-first is axis in both)
- V-03 is the only variation that demonstrates expected prose quality through example, which may produce the best C-14 output
- V-05 has the highest ceiling (all 6 aspirational addressable) and highest verbosity risk
