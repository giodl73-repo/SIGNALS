Done. `draft-proposal-rubric-v9-2026-03-15.md` is written.

---

**What changed from v8:**

**Two new aspirational criteria extracted from R8 excellence signals:**

| ID | Criterion | Source Axis | Independence from Parent |
|----|-----------|-------------|--------------------------|
| C-32 | **Field-level role enforcement in option anatomy** | V-04 "field-level role" | C-06 requires dual-role content; C-28 requires PM-first sign-off. C-32 requires `PM FRAMING:` and `ARCHITECT VALIDATION:` as typed slots in every option anatomy entry — role sequence enforced at option level, not only at phase level. Three enforcement points: template structure, option authoring, sign-off. |
| C-33 | **Phase 0 causal contract declaration** | V-05 "cross-phase causal contract" | C-13 names the deadline; C-27 names the crossover sprint; C-31 computes DECISION LEAD TIME. C-33 requires `TEMPORAL ANCHOR − INERTIA OFFSET = DECISION LEAD TIME` declared as a typed Phase 0 initialization contract with source phase attribution and T-GUARD routing, before any term-contributing phase executes. |

**Denominator:** `/24` → `/26`. Each aspirational criterion is worth `0.385` points (10/26).

**Key structural testability additions:**
- C-32: reviewer reads the option anatomy template and confirms `PM FRAMING:` and `ARCHITECT VALIDATION:` are typed slots in every option entry — no phase scan required
- C-33: reviewer reads the Phase 0 block and confirms a typed computation formula appears with source phase attribution and T-GUARD routing rule

**Ceiling under v9:** A V-06 combining all four v8 axes scores 99.23 (not 100.0). A motivated R9 variation combining all six axes (C-28 through C-33) would reach 100.0.
