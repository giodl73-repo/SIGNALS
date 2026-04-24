Written to `simulations/quest/rubrics/trace-migration-variations-R8-2026-03-15.md`.

---

## Round 8 Variations — Summary

Five complete variations targeting C-28, C-29, C-30:

| V | Axis | Primary mechanism | C-28 | C-29 | C-30 |
|---|------|-------------------|------|------|------|
| V-01 | Output format | CONSTRAINT TYPE REGISTRY (4 mandatory rows at parse time) + per-type binary fields in CONSTRAINT TRACE and B1 | VERY LOW risk | LOW risk via 3-lens sub-sections in DOMAIN IMPACT | LOW risk via explicit "different step/table/consequence" requirement in B2 |
| V-02 | Role sequence | PARITY ENFORCEMENT BLOCK printed before Q2 with explicit "DO NOT SCOPE" at zero-downtime and DEFAULT; Q3 calls out "not only financial columns" | LOW via per-role binary fields in Q2/Q3/Q4 | VERY LOW risk — pre-commitment before any role section written | LOW via Q3 Finance Phase A + distinct B2 Operations example |
| V-03 | Inertia framing | PHASE-A-INERTIA-SEED and PHASE-B-INERTIA-SEED as named required artifacts + 3-axis DISTINCTNESS REQUIREMENT as a pre-write check | LOW via per-type sub-sections in TRACE PHASE | LOW via DOMAIN LENS PARITY CHECKLIST in DOMAIN IMPACT | VERY LOW risk — named slots + axis verification before writing |
| V-04 | C-28 + C-29 combined | CONSTRAINT TYPE REGISTRY at parse + PARITY ENFORCEMENT BLOCK before Q2 | VERY LOW | VERY LOW | LOW via Q2+Q3 Phase A + distinct B2 seed |
| V-05 | All three combined | Lifecycle + CONSTRAINT TYPE REGISTRY + DOMAIN LENS PARITY CHECKLIST + named PHASE-A/B-INERTIA-SEED slots with pre-write 3-axis verification | VERY LOW | VERY LOW | VERY LOW |

**Key structural innovations over R7:**
- **C-28**: The CONSTRAINT TYPE REGISTRY (V-01, V-04, V-05) is a stronger C-28 mechanism than per-section prompting — a missing registry row is visible at parse time before any analysis is written.
- **C-29**: The PARITY ENFORCEMENT BLOCK (V-02, V-04) is a pre-commitment mechanism vs. the embedded parity checklist (V-01, V-03, V-05). The pre-commitment fires before the model writes any role section; the embedded checklist depends on per-section recall.
- **C-30**: Named slots as required artifacts (V-03, V-05) add a structural test the model can self-apply before advancing: verify 3 axes of distinctness, then write.
