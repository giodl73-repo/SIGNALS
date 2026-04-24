`crew-check-variate-R8-2026-03-17.md` written. Here is the summary:

---

## crew-check — R8 Variate Summary

**5 variations targeting v7 rubric criteria C-24 through C-27.**

| Variation | Axis | New criteria | Key structural addition |
|-----------|------|--------------|------------------------|
| V-01 | C-24 single | Dual-axis calibration | Confidence scale pre-committed with named tiers + operational meanings. Confidence in matrix schema, secondary sort key, CONFIRMED (MEDIUM+HIGH confidence) = HIGH-effective in Gate 7. G4f BLOCKING + G4g DEFERRED. |
| V-02 | C-25 single | Named convergence tier register | Presupposes C-24. CORROBORATED = same surface 2+ roles (any confidence). CONFIRMED = same surface + matching confidence tier (all non-LOW). CONFIRMED-LOW = same surface + all LOW. Gate 9 enumerates Confidence=LOW findings separately. |
| V-03 | C-26+C-27 combined | Stage pre-condition + 4-value scope column | G0.5 in HALT REGISTRY before G1. DEPRECATED as 4th STAGE-APPROPRIATE value (automatic READY). Scope-grouped matrix (YES → ADVISORY → NO → DEPRECATED). Gate 7 reads YES only. `--amend stage:{value}` in AMEND. |
| V-04 | C-24 + C-25 | Full confidence + convergence chain | Confidence feeds convergence tier derivation. CONFIRMED-LOW distinguished from CONFIRMED non-LOW. Clean 4-tier convergence register. |
| V-05 | All four + IC-CHALLENGED | Full integration | All four new criteria plus R7 inertia framing. G0.5→G1 ordering. 8-column finding rows. Convergence register over YES-scope only. CONFIRMED findings can make ICs OVERCOME-CONFIRMED. 4 independent mechanical signals (scope, severity, confidence, inertia). |

**Key R8 structural advances over R7:**

1. **C-26 formalization** — G0.5 is now explicitly ordered *before* G1 in the HALT REGISTRY table (R7 V-03 had G0.5 but its HALT REGISTRY table placed G1 first)
2. **C-27 DEPRECATED value** — R7 V-03 had YES/ADVISORY/NO; R8 adds DEPRECATED as a formal fourth value with automatic READY rule, preventing retired artifacts from being accidentally blocked
3. **C-25 tier distinction** — R7 V-02 defined CONFIRMED as "3+ roles"; R8 redefines CONFIRMED as "same surface + matching confidence tier" — the distinguishing criterion is confidence alignment, not role count
4. **C-25 Confidence=LOW enumeration** — R7 V-02 mentioned LOW in Gate 9 prose; R8 V-02/V-04/V-05 emit a formal table of all Confidence=LOW findings as a mandatory Gate 9 section
