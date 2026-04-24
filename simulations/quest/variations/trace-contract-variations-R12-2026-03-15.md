Written to `simulations/quest/golden/trace-contract-variate-R12-census-2026-03-15.md`.

---

## Round 12 Variation Map

| V | Axis | Target | Mechanism |
|---|------|--------|-----------|
| V-01 | **phrasing-register** | C-33 | Named `VERBATIM-COPY from [S5.5 Sub-task A · mechanism-distribution]` directive at the S7 instruction site |
| V-02 | **output-format** | C-34 | Required `source: group-candidate-N` field in Singleton and Multi-pattern branch templates |
| V-03 | **lifecycle-emphasis** | C-33 | Hard Gate S6.5 that requires quoting the S5.5 Sub-task A line as a gate token before S7 unlocks |
| V-04 | **phrasing-register + output-format** | C-33 + C-34 | V-01 copy directive + V-02 `source:` field combined; closes both derivation sites |
| V-05 | **role-sequence + lifecycle-emphasis + output-format** | C-29–C-34 | Expert produces named bounded artifacts `[CENSUS-ARTIFACT-A]` / `[CENSUS-ARTIFACT-B]`; S6 and S7 consume by artifact name |

**Key design decisions:**

- **V-01 vs V-03** are the diagnostic pair for C-33: directive vs. gate. If V-01 passes, V-03's gate is overhead. If V-01 fails and V-03 passes, the gate is the necessary mechanism.
- **V-04** is the priority evaluation — two orthogonal sites, no interference. Run it first to determine whether the combination is sufficient before analyzing single-axis contribution.
- **V-05** adds bounded artifact tags (`[CENSUS-ARTIFACT-A]...[/CENSUS-ARTIFACT-A]`) as the ceiling test — if V-05 exceeds V-04, role ownership adds value beyond directive + field.
