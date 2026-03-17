# corps-build Round 12 Scorecard — v10 Rubric

## Scoring Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-01** Role file completeness | PASS | PASS | PASS | PASS | PASS |
| **C-02** org-chart.md ASCII hierarchy | PASS | PASS | PASS | PASS | PASS |
| **C-03** IA in every team | PASS | PASS | PASS | PASS | PASS |
| **C-04** org.yaml structural fidelity | PASS | PASS | PASS | PASS | PASS |
| **C-05** Typed fields present | PASS | PASS | PASS | PASS | PASS |
| **C-06** Headcount table + levels | PASS | PASS | PASS | PASS | PASS |
| **C-07** Standard vs specialized distinction | PASS | PASS | PASS | PASS | PASS |
| **C-08** AMEND with three options | PASS | PASS | PASS | PASS | PASS |
| **C-09** IA team-contextualized | PASS | PASS | PASS | PASS | PASS |
| **C-10** *(aspirational baseline)* | PASS | PASS | PASS | PASS | PASS |
| **C-11** Named INVARIANTS block | **PASS** | PARTIAL | PARTIAL | **PASS** | **PASS** |
| **C-12** Auditable check-output | PASS | PASS | PASS | PASS | PASS |
| **C-13** Named failure modes per criterion | PASS | PASS | PASS | PASS | PASS |
| **C-14** Pre-step FAILURE MODES block | PASS | PASS | PASS | PASS | PASS |
| **C-15** CHECK-OUTPUT PROTOCOL COP-NN | PARTIAL | **PASS** | PARTIAL | **PASS** | **PASS** |
| **C-16** Phase-exit guard tokens | PASS | PASS | PASS | PASS | PASS |
| **C-17** Per-artifact TRANSCRIPTION-RECEIPT | PASS | PASS | PASS | PASS | PASS |
| **C-18** BUILD-VERIFY single-purpose phase | PASS | PASS | PASS | PASS | PASS |
| **C-19** TRANSCRIPTION-RECEIPT remediation | PASS | PASS | PASS | PASS | PASS |
| **C-20** BUILD-VERIFY exclusion manifest | PASS | PASS | PASS | PASS | PASS |
| **C-21** TRANSCRIPTION-CLEAR re-audit | PASS | PASS | PASS | PASS | PASS |
| **C-22** IA failure mode contrast pair | PASS | PASS | PASS | PASS | PASS |
| **C-23** Typed STRUCTURAL-ERROR taxonomy | PASS | PASS | PASS | PASS | PASS |
| **C-24** Premature-exit as STRUCTURAL-ERROR | PASS | PASS | PASS | PASS | PASS |
| **C-25** ENTRY-GATE bidirectional enforcement | PASS | PASS | PASS | PASS | PASS |
| **C-26** Pre-execution STRUCTURAL-ERROR-CATALOG | PASS | PASS | PASS | PASS | PASS |
| **C-27** PROFILE-phase typed violation taxonomy | PASS | PASS | PASS | PASS | PASS |
| **C-28** ROLES-WRITTEN per-team receipt | PASS | PASS | PASS | PASS | PASS |
| **C-29** AMEND --area PROFILE-REDERIVE gate | PASS | PASS | PASS | PASS | PASS |
| **C-30** CATALOG-CLOSURE terminal attestation | PASS | PASS | PASS | PASS | PASS |
| **C-31** ROLES-WRITTEN NO-halt cycle | PASS | PASS | PASS | PASS | PASS |
| **C-32** AMEND-CHAIN-COMPLETE terminal token | PASS | PASS | PASS | PASS | PASS |
| **C-33** STRUCTURAL-ERROR-CATALOG as INVARIANTS | **PASS** | PARTIAL | PARTIAL | **PASS** | **PASS** |
| **C-34** SPECIALIZATION-GATE per-team block | PASS | PASS | PASS | PASS | PASS |
| **C-35** ROLES-COMPLETE specialization attestation | PASS | PASS | PASS | PASS | PASS |
| **C-36** AMEND --area SPECIALIZATION-GATE re-run | PARTIAL | PARTIAL | **PASS** | PARTIAL | **PASS** |

---

## Per-Variation Evidence Notes

### V-01 — INVARIANTS block (C-11 focus)
- **C-11 PASS**: `INVARIANT-SPECIALIZATION-DISTINCTNESS` named, paired to `STRUCTURAL-ERROR:SPECIALIZATION-COPY-VIOLATION`, CO-EXTENSIVE DECLARATION present. Closes R11 gap where INVARIANTS existed without specialization entry.
- **C-15 PARTIAL**: Has check-output mechanism from baseline but COP-NN section lacks COP-07 / COP-09 specialization entries — those were the R12 target of V-02, not V-01.
- **C-33 PASS**: INVARIANTS block declared as contract; SPECIALIZATION-COPY-VIOLATION maps to named invariant.
- **C-36 PARTIAL**: AMEND names SPECIALIZATION-GATE parenthetically; `AMEND-CHAIN-COMPLETE` has no `specialization-gate-rerun:` field.

### V-02 — CHECK-OUTPUT PROTOCOL (C-15 focus)
- **C-15 PASS**: COP-01 through COP-13 fully enumerated; COP-07 = SPECIALIZATION-GATE gate-verdict per team; COP-09 = ROLES-COMPLETE `all-specialization-gates-passed` check. Closes R11 gap where COP existed without specialization items.
- **C-11 PARTIAL**: Has baseline INVARIANTS but `INVARIANT-SPECIALIZATION-DISTINCTNESS` not named — V-02's axis is COP, not INVARIANTS.
- **C-33 PARTIAL**: INVARIANTS present but not explicitly declared as contract; STRUCTURAL-ERROR-CATALOG linkage incomplete.
- **C-36 PARTIAL**: COP-09 documents the check but AMEND chain still lacks explicit `specialization-gate-rerun:` field.

### V-03 — AMEND-chain precision (C-36 focus)
- **C-36 PASS**: `--area` flag explicitly discards prior gate verdicts rather than inheriting them; `AMEND-CHAIN-COMPLETE` gains required `specialization-gate-rerun: { per-team: [...] }` field. This is the structural fix absent from R11.
- **C-11 PARTIAL**: No `INVARIANT-SPECIALIZATION-DISTINCTNESS` — not in scope for this axis.
- **C-15 PARTIAL**: No specialization-aware COP-NN — not in scope for this axis.
- **C-33 PARTIAL**: INVARIANTS block present but not extended to cover specialization-gate invariant.

### V-04 — INVARIANTS + COP (C-11 + C-15 focus)
- **C-11 PASS**: INVARIANTS block with `INVARIANT-SPECIALIZATION-DISTINCTNESS` + `cop:` pointer linking to COP-07 and COP-09. CO-EXTENSIVE DECLARATION holds across both layers.
- **C-15 PASS**: COP-07 and COP-09 annotated with `INVARIANT-SPECIALIZATION-DISTINCTNESS` by name — protocol items are traceable to their invariant source.
- **C-33 PASS**: INVARIANTS block functions as contract; COP-NN annotations make the linkage explicit.
- **C-36 PARTIAL**: AMEND still lacks `specialization-gate-rerun:` field in `AMEND-CHAIN-COMPLETE` — V-04 stops at INVARIANTS/COP, does not extend into AMEND chain.

### V-05 — Full synthesis (C-11 + C-15 + C-36)
- **C-11 PASS**: INVARIANTS block with `cop:` pointers to COP-07/COP-09; CO-EXTENSIVE DECLARATION explicitly extends to COP-NN layer as a third verification mechanism alongside INVARIANTS and CATALOG.
- **C-15 PASS**: COP-NN items confirm invariants by name; COP-07 = specialization-gate verdict; COP-09 = ROLES-COMPLETE terminal field. Protocol and invariant layers are mutually verifiable.
- **C-33 PASS**: Three-layer co-extensive contract: STRUCTURAL-ERROR-CATALOG (CATALOG layer), INVARIANTS block (invariant layer), COP-NN (protocol layer) all independently attest the same structural properties.
- **C-36 PASS**: `AMEND-CHAIN-COMPLETE` enumerates `specialization-gate-rerun: { per-team: [...] }` as a required field; AMEND --area explicitly discards prior gate verdicts; specialization re-audit is a named member of the AMEND chain alongside PROFILE-REDERIVE and ROLES-WRITTEN.

---

## Score Computation

| Variation | Essential (60 max) | Recommended (30 max) | Aspirational (140 max) | **Total (230 max)** |
|-----------|--------------------|----------------------|------------------------|---------------------|
| V-01 | 60 | 30 | 135 (C-15 PARTIAL=2.5, C-36 PARTIAL=2.5) | **225.0** |
| V-02 | 60 | 30 | 132.5 (C-11 PARTIAL=2.5, C-33 PARTIAL=2.5, C-36 PARTIAL=2.5) | **222.5** |
| V-03 | 60 | 30 | 132.5 (C-11 PARTIAL=2.5, C-15 PARTIAL=2.5, C-33 PARTIAL=2.5) | **222.5** |
| V-04 | 60 | 30 | 137.5 (C-36 PARTIAL=2.5) | **227.5** |
| V-05 | 60 | 30 | 140 | **230.0** |

**All variations**: all 5 essentials PASS, composite >= 191 → all meet golden threshold.

---

## Rankings

| Rank | Variation | Score | Key differentiator |
|------|-----------|-------|--------------------|
| 1 | **V-05** | 230.0 | Full synthesis — three-layer co-extensive contract |
| 2 | **V-04** | 227.5 | INVARIANTS + COP linked; only C-36 PARTIAL |
| 3 | **V-01** | 225.0 | C-11 PASS + C-33 PASS; C-15/C-36 still PARTIAL |
| 4 | **V-02** | 222.5 | C-15 PASS; C-11/C-33/C-36 PARTIAL |
| 4 | **V-03** | 222.5 | C-36 PASS; C-11/C-15/C-33 PARTIAL |

---

## Excellence Signals — V-05

### Three-layer co-extensive contract (genuinely new pattern)

V-05 extends CO-EXTENSIVE DECLARATION beyond its prior two-layer form (INVARIANTS ↔ STRUCTURAL-ERROR-CATALOG) to include a third independent layer: **COP-NN**. Each layer independently attests the same structural properties:

- **INVARIANTS layer**: declares `INVARIANT-SPECIALIZATION-DISTINCTNESS` with named identifier and `cop:` pointer to COP-07 and COP-09
- **CATALOG layer**: STRUCTURAL-ERROR-CATALOG names `SPECIALIZATION-COPY-VIOLATION` as an enforcement code linked to the invariant
- **COP-NN layer**: COP-07 checks gate-verdict per team; COP-09 checks `all-specialization-gates-passed` in ROLES-COMPLETE — both reference `INVARIANT-SPECIALIZATION-DISTINCTNESS` by name

This creates a **closed audit loop**: any silent failure in the specialization gate is detectable from any of the three layers independently. A gap in COP-07 contradicts the invariant; a gap in the invariant leaves COP-07 unmoored; a gap in the CATALOG leaves the STRUCTURAL-ERROR code without a declared source. All three must agree.

This pattern was predicted as the discriminator in the R12 setup but was not previously formalized as a criterion — it goes beyond C-11 (names the invariant), C-15 (names the COP item), and C-33 (links catalog to invariants). The new structural property is **mutual verifiability across three independent mechanism layers**.

### COP-to-INVARIANT bi-directional cross-reference (refinement pattern)

V-04 established that COP-NN items can reference INVARIANT identifiers by name. V-05 extends this to bidirectional: INVARIANTS also carry `cop:` pointers back to COP-NN items. Prior art (V-04) was unidirectional (COP → INVARIANT). V-05 makes both directions explicit, enabling forward-tracing (invariant → protocol check) and backward-tracing (protocol check → invariant declaration) without needing to search either section.

---

## New Criteria for v11

| ID | Pattern | Source |
|----|---------|--------|
| C-37 | **Three-layer CO-EXTENSIVE DECLARATION** — INVARIANTS, STRUCTURAL-ERROR-CATALOG, and COP-NN each independently attest the same structural properties; all three must agree; gap in any layer is detectable from the others | V-05 R12 |
| C-38 | **Bidirectional INVARIANT–COP cross-reference** — INVARIANTS carry `cop:` pointers to their COP-NN items; COP-NN items carry `invariant:` back-references; enables forward + backward traceability without section search | V-05 R12 |

---

```json
{"top_score": 230, "all_essential_pass": true, "new_patterns": ["Three-layer CO-EXTENSIVE DECLARATION: INVARIANTS, STRUCTURAL-ERROR-CATALOG, and COP-NN each independently attest the same structural properties creating a closed audit loop where any silent failure is detectable from any layer", "Bidirectional INVARIANT-COP cross-reference: INVARIANTS carry cop: pointers to COP-NN items and COP-NN items carry invariant: back-references enabling forward and backward traceability without section search"]}
```
