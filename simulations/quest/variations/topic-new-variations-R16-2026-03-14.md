Round 16 variations written to `simulations/quest/rubrics/topic-new-rubric-v14-variate-R16-2026-03-15.md`.

---

## R16 Summary

**Problem going in**: No R15 variation satisfied both C-45 (zero inline prose in phases) AND C-46 (Stakeholder Most Harmed column with role names at every citation) simultaneously. R15 V-01 had C-45 but failed C-42/C-43/C-44. R15 V-02 had C-46 but phases still had inline prose.

**Variation Map**

| ID | Axis | What's New |
|----|------|-----------|
| V-01 | Combined registry baseline | Synthesizes R15 V-01 + R15 V-02 into one coherent prompt — pre-pipeline schemas as sole constraint source, INERTIA REGISTER with Stakeholder Most Harmed column, zero inline prose in all phases |
| V-02 | + PIPELINE CONSEQUENCE REGISTER | Adds PCR-01–PCR-04 pre-pipeline registry (stable IDs for skip costs); pipeline "If Skipped" column becomes PCR-NN citations not prose; phases cite PCR-NN at risk points |
| V-03 | + PRIORITY SCHEMA isolation | Extracts priority vocabulary from F-01 cell into its own P-01/P-02/P-03 block; F-01 becomes a pointer to PRIORITY SCHEMA; eliminates the dual-source drift risk between cell text and citations |
| V-04 | + COMMITMENT BLOCK gates | Replaces checkbox exit gates with structured fill-in templates; model authors `Observed:` and `Status: PASS / FAIL` for each condition; C-28/C-30 independence satisfied by template structure not prose instruction |
| V-05 | Maximum integration | All three new axes combined — six pre-pipeline blocks, COMMITMENT BLOCK gates throughout, F-01 points to PRIORITY SCHEMA, PCR-NN in every entry/exit gate |

**Predicted criterion gains from R15 V-02 baseline (100/36 → targeting 38/38)**:
- C-45: All five variations satisfy it — phases carry zero inline prose
- C-46: All five variations satisfy it — INERTIA REGISTER has Stakeholder Most Harmed, role names travel to every IR-NN citation
- V-05 likely generates an excellence signal on the PCR-NN pattern (future C-47 candidate)
