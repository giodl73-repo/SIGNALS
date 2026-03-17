Written to `simulations/quest/golden/corps-build-variate-R12-2026-03-17.md`.

---

# Variate R12 — corps-build (2026-03-17)

## What this round targets

R11 certified three new criteria (C-34, C-35, C-36) from the SPECIALIZATION-GATE pattern. Two R11 PARTIALs persist into R12:

| Criterion | Gap | V-01 R11 fixed it — but without SPECIALIZATION-GATE baseline |
|-----------|-----|--------------------------------------------------------------|
| **C-11** | No dedicated `INVARIANTS:` block with named identifiers | V-01 had INVARIANTS but no SPECIALIZATION-GATE; V-03 had SPECIALIZATION-GATE but no INVARIANTS |
| **C-15** | No `CHECK-OUTPUT PROTOCOL:` section with COP-NN items | V-02 had COP but no SPECIALIZATION-GATE |
| **C-36** | AMEND --area names SPECIALIZATION-GATE parenthetically; `AMEND-CHAIN-COMPLETE` has no `specialization-gate-rerun:` field | New target |

## The 5 variations

| Variation | Single axis | Target |
|-----------|-------------|--------|
| **V-01** | INVARIANTS block | C-11 — `INVARIANT-SPECIALIZATION-DISTINCTNESS` named + paired to `STRUCTURAL-ERROR:SPECIALIZATION-COPY-VIOLATION`; CO-EXTENSIVE DECLARATION present |
| **V-02** | CHECK-OUTPUT PROTOCOL | C-15 — COP-01 through COP-13; COP-07 = SPECIALIZATION-GATE gate-verdict per team; COP-09 = ROLES-COMPLETE all-specialization-gates-passed |
| **V-03** | AMEND-chain precision | C-36 — `--area` discards prior gate verdicts explicitly; `AMEND-CHAIN-COMPLETE` gains `specialization-gate-rerun: { per-team: ... }` required field |
| **V-04** | INVARIANTS + COP | C-11 + C-15 — COP-07 and COP-09 annotated with `INVARIANT-SPECIALIZATION-DISTINCTNESS` by name |
| **V-05** | Full synthesis | C-11 + C-15 + C-36 — INVARIANTS `cop:` pointers, COP confirms invariants, AMEND-CHAIN-COMPLETE enumerates gate-rerun; CO-EXTENSIVE DECLARATION extends to COP-NN layer |

**Predicted discriminator**: V-05 is the only variation predicted to achieve full PASS on C-11, C-15, C-34, C-35, and C-36 simultaneously. The structural novelty to watch for new excellence signals: the three-layer co-extensive contract (INVARIANTS — CATALOG — COP-NN each confirm the same properties through independent mechanisms).
