`draft-proposal-rubric-v10-2026-03-15.md` is written.

---

**What changed from v9:**

**Two new aspirational criteria extracted from R9 excellence signals:**

| ID | Criterion | Source Axis | Independence from Parent |
|----|-----------|-------------|--------------------------|
| C-34 | **Phase 0 option anatomy contract declaration** | V-01 "Phase 0 contract + T-25" | C-32 requires `PM FRAMING:` and `ARCHITECT VALIDATION:` as typed slots in every option entry. C-34 requires those slots to be declared as a typed Phase 0 initialization contract before any option is authored, with a named T-NN trigger for role-slot violations. Mirrors C-33's upgrade over C-31: C-33 declares the computation chain at Phase 0; C-34 declares the option anatomy field structure at Phase 0. Two orthogonal Phase 0 contracts. |
| C-35 | **PREREQUISITE GATE extension for Phase 0 causal chain contract verification** | V-02 "gate item #9" | C-20 requires PREREQUISITE GATE binaries for register ordering. C-33 requires the Phase 0 causal chain contract. C-35 requires the gate to include a binary item confirming Phase 0 contract presence and completeness. Makes C-33 compliance single-block auditable at Phase 11 without Phase 0 scroll. Extends the established gate-extension pattern: C-27 for inertia axis, C-31 for lead-time axis, C-35 for Phase 0 contract axis. |

**Denominator:** `/26` → `/28`. Each aspirational criterion is worth `0.357` points (10/28).

**Ceiling under v10:** A V-06 combining all six v8/v9 axes (C-28 through C-33) scores `99.29`. The motivated R10 variation combining all eight axes (C-28 through C-35) reaches `100.0`.
