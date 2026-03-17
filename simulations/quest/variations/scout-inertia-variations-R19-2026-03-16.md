Written to `simulations/quest/golden/scout-inertia-variate-R19-2026-03-17.md`.

---

## scout-inertia R19 -- Variation Summary

**New criteria under v19**: A-44 (status column label = verification-action register) + A-45 (command directive label or body = verification-action vocabulary). Ceiling: 270 → 280.

**Key design insight**: All R18 forms incidentally satisfied A-44 and A-45 because gate heading verb propagated into the column label and CONFIRM/VALIDATE appeared as the body imperative. R19 isolates and formalizes these as explicit scoring targets.

| Variation | Axis | Gate heading | Column label | Command | Predicted |
|-----------|------|-------------|--------------|---------|-----------|
| V-01 | Reference carry (DEFAULT OPTION, SECTION, BOTH) | BOTH BRIDGE ARTIFACTS VERIFIED? | Verified? | [BRIDGE COMPLETION COMMAND]: **CONFIRM** | 280/280 |
| V-02 | A-45 single-axis: explicit `[BRIDGE VERIFICATION COMMAND]` label (INERTIA THREAT, SECTION, EACH) | EACH BRIDGE ARTIFACT VERIFIED? | Verified? | **[BRIDGE VERIFICATION COMMAND]**: VERIFY | 280/280 |
| V-03 | A-44 single-axis: CHECKED verb variant (INERTIA THREAT, SECTION, EACH) | EACH BRIDGE ARTIFACT **CHECKED?** | **Checked?** | [BRIDGE COMPLETION COMMAND]: CONFIRM | 280/280 |
| V-04 | Combined: STATUS QUO + STAGE + explicit `[BRIDGE VALIDATION COMMAND]` label | ALL BRIDGE ARTIFACTS VALIDATED? | Validated? | **[BRIDGE VALIDATION COMMAND]**: VALIDATE | 280/280 |
| V-05 | Combined: INCUMBENT + STAGE + explicit `[BRIDGE VERIFICATION COMMAND]` + full VERIFY-root coherence | EACH BRIDGE ARTIFACT VERIFIED? | Verified? | **[BRIDGE VERIFICATION COMMAND]**: VERIFY | 280/280 |

**Three single-axis variation axes picked**:
1. **A-45 directive-label** (V-02): implicit body-verb → explicit `[BRIDGE VERIFICATION COMMAND]` label
2. **A-44 column verb** (V-03): CONFIRMED → CHECKED in heading + column; tests CHECKED as new A-43/A-44 verb
3. **Reference carry** (V-01): confirmed R18 form establishing the 280/280 baseline

**Two combined-axis variations** (V-04, V-05): STAGE schema + explicit command label + domain-prefix coherence. V-05 achieves maximum VERIFY-root coherence: heading verb, column label, and command label all derive from the same VERIFY root — the strongest possible three-point register signal under A-43, A-44, A-45 simultaneously.
