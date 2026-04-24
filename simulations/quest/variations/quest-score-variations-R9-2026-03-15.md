Written to `simulations/quest/golden/quest-score-variate-R9-2026-03-16.md`.

---

## Round 9 — V-01 through V-05

**New axes:**

| Axis | Label | Mechanism | Phase |
|------|-------|-----------|-------|
| B3 | Combination injection-point map | COMBINATION INJECTION-POINT MAP block in SYNTHESIS EXCELLENCE SIGNALS; fires when scored set contains a variation satisfying C-25+C-26+C-27; requires per-axis phase+timing enumeration and explicit disjointness confirmation | SYNTHESIS |
| D3 | Two-path equivalence signal | TWO-PATH EQUIVALENCE PROTOCOL block in SYNTHESIS EXCELLENCE SIGNALS; fires when scored set contains both adversarial-path (AUDIT A/B/C) and template-path (CHECK A-F) combinations; requires both paths named, coverage equivalence confirmed, extension mechanism stated | SYNTHESIS |
| B3p | Injection-point prose (register variant) | Same C-28 semantic content as B3 but delivered as a descriptive paragraph without labeled fields or explicit "Structural disjointness confirmed:" assertion | SYNTHESIS |

**Single-axis variations:**

- **V-01 (B3 — lifecycle emphasis)**: Adds COMBINATION INJECTION-POINT MAP structured protocol to SYNTHESIS. Predicts C-28 PASS, C-29 FAIL. Score **99.52**.
- **V-02 (D3 — output format)**: Adds TWO-PATH EQUIVALENCE PROTOCOL to SYNTHESIS. Predicts C-28 FAIL, C-29 PASS. Score **99.52**.
- **V-03 (B3p — phrasing register)**: Adds prose injection-point paragraph to SYNTHESIS. Predicts C-28 PARTIAL (injection points named but disjointness not in structured confirmation form), C-29 FAIL. Score **99.29** if PARTIAL fires; 99.52 if rubric is format-agnostic.

**Combination variations:**

- **V-04 (B3+D3, adversarial base)**: COMBINATION INJECTION-POINT MAP + TWO-PATH EQUIVALENCE PROTOCOL on R8 V-04 (AUDIT A/B/C). Predicts all 29 PASS. Score **100.00**.
- **V-05 (B3+D3, template base)**: Same SYNTHESIS blocks on R8 V-05 (CHECK A-F). Predicts all 29 PASS. Score **100.00**.

**Key design decision — B3 and D3 as per-set vs. per-variation triggers**: B3 fires per scored variation (any single output satisfying C-25+C-26+C-27 triggers it); D3 fires per scored set (only when both adversarial and template combination variations are simultaneously present). The PARTIAL prediction for V-03 is the diagnostic signal of the round — if C-28 PARTIAL fires it confirms the rubric requires structured explicit confirmation, not narrative description.
