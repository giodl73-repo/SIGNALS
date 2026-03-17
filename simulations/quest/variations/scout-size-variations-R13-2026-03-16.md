**R13 variations written** to `simulations/quest/golden/scout-size-variate-R13-2026-03-17.md`.

---

## What R13 Addresses

v13 adds C-34 and C-35. Here's how each variation covers them:

| Variation | Axis | C-34 | C-35 | Architecture |
|-----------|------|------|------|--------------|
| **V-01** | Output format | `DIAGNOSIS: basis-negation.` inline in WRONG block | — | Single-phase |
| **V-02** | Lifecycle emphasis | Full 3-field sub-block: FAILURE CLASS / DETECTION PATTERN / WHY IT FAILS | — | Single-phase |
| **V-03** | Inertia framing | `You have produced a basis-negation.` (second-person) | Phase 0 binary CLOSED/OPEN gate on inertia | Single-phase after gate |
| **V-04** | Role sequence + inertia framing | `DIAGNOSIS: basis-negation.` in Phase 2 WRONG block | Phase 0 gate before Phase 1 | Two-phase + Phase 0 |
| **V-05** | All three combined | 3-field structured DIAGNOSIS block in Phase 2 | Phase 0 extended to gate on **both** inertia AND C-05 signal boundary | Three-phase |

**Key structural decisions by variation:**

- **V-01** is the minimal C-34 test — one added line in the WRONG block, everything else from R12 V-01 unchanged
- **V-02** tests whether three labeled diagnostic sub-fields produce stronger priming than a single annotation (at the cost of more prompt text)
- **V-03** introduces C-35 in the simplest possible form — a Phase 0 gate before an otherwise single-phase design, with second-person C-34 register
- **V-04** recombines Phase 0 + two-phase to verify the full C-20 cluster can coexist with both new criteria
- **V-05** extends Phase 0 to a two-precondition gate (inertia + signal boundary), making C-05 a structural production dependency rather than a closing prose instruction — the most aggressive enforcement design in this series
