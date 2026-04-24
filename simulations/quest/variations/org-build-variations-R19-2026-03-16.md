Written to `simulations/quest/golden/org-build-variate-R19-2026-03-16.md`.

---

## R19 — org-build Variate Summary

**R18 gaps targeted**: C-37 (intra-phase sub-step ordering guards) and C-38 (composite typed tokens).

### Variation axes

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| **V-01** | Inertia framing | IA as primary design signal — FLAT-CASE-PRESSURE banner in header, every phase names the IA variable it consumes — improves C-11/C-17/C-35 coherence |
| **V-02** | Lifecycle emphasis | Triple-direction guards (outbound gate FORBIDDEN + inbound phase FORBIDDEN + intra-phase sub-step FORBIDDEN) + extended RECORD blocks reduce gate-crossing failures across C-23/C-25/C-37 |
| **V-03** | Role sequence | Phase 0 labeling for inertia assessment makes the prerequisite structurally unambiguous — you cannot skip Phase 0 to get to Phase 1 without renumbering the sequence |
| **V-04** | Lifecycle + Register | Zero advisory language throughout (every instruction is MUST or FORBIDDEN) + maximum phase formalism closes C-19/C-29 advisory-drift failures simultaneously |
| **V-05** | Inertia framing + Output format | Pre-print skeleton (CONST-3) with named `{{SLOT}}` tokens keyed to gate variables satisfies C-22; composite token table in Phase 2 gate section satisfies C-38; CONST-2 side-by-side columns satisfy C-34 |

### Key structural decisions consistent across all 5 variations

- **CONST-1 / CONST-2 before Phase 1** (C-36) — lookup tables declared once, referenced by name only inside phases
- **Phase 1 = Inertia Assessment before role enumeration** (C-35) — inertia verdict locked as typed gate output before any COUNT sub-step runs
- **Sub-step FORBIDDENs in Phase 2** (C-37) — `COUNT → AREA → FILE` with explicit `FORBIDDEN: beginning sub-step AREA before completing sub-step COUNT`
- **T3-ROLE-OUTCOME composite token** (C-38) — single closed-set value encoding mode × compliance (`STANDARD-FLOOR-MET | DEEP-FLOOR-MET | FLOOR-MISS`)
- **PHASE-ORDERING-GUARD as first field in every RECORD block** (C-28)
- **Input Contract section distinct from Constraints section** (C-32) in every consuming phase
