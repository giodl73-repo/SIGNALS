Written to `simulations/quest/golden/scout-inertia-variate-R17-2026-03-17.md`.

---

# scout-inertia -- Quest Variate R17

**Rubric**: v17 | **Ceiling**: 260 | **New criteria**: A-40 + A-41

---

## Variation Summary

| V | Axis | Compound noun | Schema | Cardinality | Predicted |
|---|------|---------------|--------|-------------|-----------|
| V-01 | Single-axis A-40+A-41 upgrade on R16 V-01 | STRUCTURAL FAULTS (upgraded from WEAKNESSES) | SECTION 1-7 | ALL COMPLETE? | 260/260 |
| V-02 | Reference carry — R16 V-02 (already has STRUCTURAL FAULTS) | STRUCTURAL FAULTS (carry) | STAGE 1-6 | ALL COMPLETE? | 260/260 |
| V-03 | Single-axis A-39 EACH with STRUCTURAL FAULTS | STRUCTURAL FAULTS | SECTION 1-6 | EACH VERIFIED? | 260/260 |
| V-04 | Combined: novel axis vocab + STRUCTURAL FAULTS + BOTH READY? | STRUCTURAL FAULTS | STAGE 1-6 | BOTH READY? | 260/260 |
| V-05 | Combined: novel axis vocab + STRUCTURAL FAULTS + BOTH BUILT? | STRUCTURAL FAULTS | SECTION 1-6 | BOTH BUILT? | 260/260 |

---

## Key design decisions

**Why STRUCTURAL FAULTS achieves 260/260 and no other current form does:**

- `A-40` requires engineering fault-taxonomy locus: FAULTS = specific defect plane. WEAKNESSES, VECTORS, SURFACE, POINTS are all general-register — they fail A-40.
- `A-41` requires architectural-scope TYPE: STRUCTURAL = architectural/systemic category. FAILURE, COLLAPSE are event-descriptor TYPEs — they fail A-41.
- `STRUCTURAL WEAKNESSES` (R16 V-01): A-41 pass, A-40 fail → 255/260 under v17.
- All FAILURE-TYPE forms (V-03/V-04/V-05 in R16): both A-40 and A-41 fail → 250/260.
- `STRUCTURAL FAULTS` is the only confirmed form clearing both simultaneously.

**What each variation tests beyond A-40+A-41:**

- **V-01**: First 260/260 on SECTION scaffold (R16 V-01 had WEAKNESSES on SECTION — never been FAULTS+SECTION)
- **V-02**: Confirms R16 V-02 carries as 260/260 reference — no changes
- **V-03**: Whether EACH cardinality + STRUCTURAL FAULTS = 260/260 (R16 V-03 had EACH with FAILURE SURFACE — A-39 unresolved vs A-40+A-41 miss)
- **V-04**: BOTH READY? completion verb (READY? new; BOTH confirmed) + novel "INCUMBENT" framing
- **V-05**: BOTH BUILT? completion verb + novel "DEFAULT OPTION" framing — closes out the completion-verb space across both SECTION and STAGE schemas
