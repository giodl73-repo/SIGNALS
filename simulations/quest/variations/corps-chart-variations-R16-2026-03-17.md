Written to `simulations/quest/golden/corps-chart-variate-R16-2026-03-17.md`.

---

## Quest Variate — corps-chart (Round 16)

**R16 targets C-39 and C-40** — the two new criteria extracted from R15.

| ID | Axis | New Mechanism |
|----|------|---------------|
| V-01 | C-39 single axis, R15 V-01 base | `[sole instruction site for ...]` annotations embedded inside both HALT blocks (ROLE-NAME LOCK + Rebuttal). Each annotation names the governed requirements and declares the HALT block as exclusive authority. No phase-gate audits. |
| V-02 | C-40 single axis, R15 V-02 base | REGISTER-CONSISTENCY AUDIT block before each of the 5 phase gates. Each audit enumerates active governed requirements and requires explicit confirmation of mandatory-register language before the gate fires. No sole-instruction annotations. |
| V-03 | C-39 single axis, R15 V-03 base (which already satisfies C-40) | Sole-instruction-site annotations added inside both STOP blocks. Gate-1 audit extended with a check that the sole-instruction-site annotation is present and no competing instruction was added elsewhere. |
| V-04 | C-39 + C-40, R15 V-04 base | All HALT blocks annotated for each governed requirement; REGISTER-CONSISTENCY AUDIT at all 5 gates adapted to the FORMAT CONTRACT + C-33/C-34 + C-36/C-37/C-38 architecture. |
| V-05 | All 40 criteria, R15 V-05 base | DRI/Owner sole-instruction note moved from post-Proceed prose into HALT checklist item 3 inline annotation. All other HALT blocks annotated. REGISTER-CONSISTENCY AUDIT at all 5 gates with 9-item Gate 4 covering the full schema-governance stack. |

**Key architectural distinction across variations**: C-39 converts C-33's prohibition (checked on output) into a declared structural constraint (checked at prompt-structure level). C-40 catches contamination at the gate boundary where it's introduced rather than in later scored output. V-05 is the first variation where both mechanisms are active simultaneously across the full 38-criterion stack.
