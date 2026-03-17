Written to `simulations/quest/golden/corps-scan-variate-R11-2026-03-17.md`.

---

## Summary

**5 complete variations** for corps-scan R11, each demonstrating the new C-43–C-48 criteria:

| Variation | Axis | New criteria | MANIFEST TOTAL | Phase test-item split |
|-----------|------|-------------|---------------|----------------------|
| **V-01** | Role architecture block | C-43 | 15 | P1=2, P2=6, P3=6, P4=1 |
| **V-02** | Signal-strength provenance + amend consequence | C-44, C-45 | 16 | P1=2, P2=5, P3=7, P4=2 |
| **V-03** | Typed assertion register | C-46 | 14 | P1=2, P2=5, P3=6, P4=1 |
| **V-04** | 3-part ENTRY + inertia framing | C-47, C-48 | 15 | P1=2, P2=5, P3=7, P4=1 |
| **V-05** | Full combination | C-43–C-48 | 18 | P1=2, P2=6, P3=8, P4=2 |

**Key structural decisions:**

- **C-43 (V-01, V-05)**: ROLE ARCHITECTURE block is a standalone named table before the phases — not inline Phase 2 commentary. The typed handoff emit (`ROLE-HANDOFF: Signal-Surveyor → Org-Architect | type: intra-P2 | ...`) is structurally distinct from the inter-phase gate tokens, preventing conflation.

- **C-44 (V-02, V-05)**: The derivation rule is stated explicitly in the IVR triple body, not implied. A field without a stated derivation rule doesn't pass — the prompt must own the derivation contract.

- **C-45 (V-02, V-05)**: Consequence column entries are phase-specific (e.g., AMEND A re-runs Phase 2; AMEND B updates only the header, no re-run), not generic filler.

- **C-46 (V-03, V-05)**: Register is internally consistent throughout — `Assert:/Execute:/Verify:/Emit:` + `PASS / FAIL` with no YES/NO mixing. The GATE TOKEN PROTOCOL text already uses PASS/FAIL, so C-46 unifies completion tests with gate tokens under one vocabulary.

- **C-47 (V-04, V-05)**: FORBIDDEN-STATES names concrete illegal entry conditions per phase (e.g., "Phase 3 YAML template already written" is forbidden at P2 ENTRY), not generic placeholder text.

- **C-48 (V-04, V-05)**: Both required elements are present simultaneously — the opening names "tribal knowledge" as the concrete failure mode, and `replaces: undocumented tribal org structure` appears in the YAML header. IVR-P3-G (or IVR-P3-H in V-05) explicitly cross-references the opening to make both elements verifiable.
