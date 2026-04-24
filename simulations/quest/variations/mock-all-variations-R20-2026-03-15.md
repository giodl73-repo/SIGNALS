Written to `simulations/quest/golden/mock-all-variate-R20-2026-03-16.md`.

---

## mock-all Variate — Round 20

**Rubric:** v20 | **Denominator:** 32 | **New criteria:** C-39, C-40

### What changed from R19

| Criterion | What it tests |
|-----------|---------------|
| **C-39** | Preamble declarations are architecturally *separate* — Declaration A governs only REAL-REQUIRED identifier; Declaration B governs only per-stage firing. Neither subsumes the other's scope. |
| **C-40** | Each stage body's inertia instance phrase names a *stage-specific* artifact domain (HIGH-STRUCTURE / EVIDENCE-HEAVY / MIXED vocabulary), not a generic placeholder valid in any stage. |

**R19 V-05 retroactive:** C-39 PASS (declarations were already clean), C-40 FAIL (generic placeholder identical across all three stages) → **31/32 = 99.688**.

### Axis assignment

| Variation | C-39 | C-40 | Asp | Composite | Primary axis |
|-----------|------|------|-----|-----------|--------------|
| V-01 | FAIL | FAIL | 30/32 | **99.375** | Cross-contaminating declarations (each covers both dims) + generic instance |
| V-02 | PASS | FAIL | 31/32 | **99.688** | Single axis: C-39 fix only (R19 V-05 structure, retro-annotated) |
| V-03 | FAIL | PASS | 31/32 | **99.688** | Single axis: C-40 fix only (stage-typed placeholders, still merged declarations) |
| V-04 | PASS | PASS | 32/32 | **100.0** | Both fixed; C-40 via instruction (model must follow) |
| V-05 | PASS | PASS | 32/32 | **100.0** | Both fixed; C-40 via pre-seeded example per stage (strongest guarantee) |

### Key findings embedded in design

**C-39 diagnostic:** Read Declaration A alone — does it contain per-stage firing language ("fires independently," "Stage 1, Stage 2, Stage 3," "inertia extension")? If yes, C-39 FAIL. Read Declaration B alone — does it mention "canonical identifier," "REAL-REQUIRED," or "copies verbatim"? If yes, C-39 FAIL.

**C-40 diagnostic:** Read Stage 1 instance placeholder — does it name a HIGH-STRUCTURE artifact domain (state transition / boundary contract / trigger condition / configuration key)? If not, C-40 FAIL. Same check for Stage 2 (EVIDENCE-HEAVY) and Stage 3 (MIXED). A placeholder valid across multiple stage categories fails C-40.

**V-04 vs V-05 structural risk:** Both score 100.0. V-04's C-40 depends on model compliance with a domain-constraint instruction; V-05 eliminates that risk by pre-seeding example instance phrases the model copies. Same rubric score, different runtime reliability — same pattern as the V-02/V-03 structural guarantee gap in the scout-feasibility R3 series.
