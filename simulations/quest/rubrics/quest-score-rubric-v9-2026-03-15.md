Written to `simulations/quest/rubrics/quest-score-rubric-v9-2026-03-16.md`.

---

**Round 8 excellence signals extracted → C-28 and C-29:**

**C-28 — Combination injection-point map in SYNTHESIS** (V-04 signal)
V-04's signal named the phase-timing position for each R8 axis individually — Y (AUDIT C) post-write in Verifier after AUDIT B; Z (PLATEAU-CLASSIFICATION NOTE) in SYNTHESIS; A2 (FLAG CLOSURE) as the final Verifier gate — and explicitly confirmed structural disjointness. Without C-28, a combination variation's SYNTHESIS signal can describe the aggregate effect without mapping individual injection points, leaving orthogonality unconfirmed.

**C-29 — Two-path equivalence signal in SYNTHESIS** (V-05 signal)
V-05 confirmed that the template enforcement path (CHECK A through CHECK F) carries the R8 evaluator-behavior axes equivalently to the adversarial path (AUDIT A/B/C). Without C-29, the SYNTHESIS can describe the template-path extension mechanically without confirming coverage equivalence — a reader cannot verify the two architectures satisfy the same set of new criteria.

**N_aspirational: 19 → 21.** Formula denominator updated throughout. Roster count updated to 29-row. Per-criterion aspirational weight: 10/21 ≈ 0.476 pt. Single-axis R9 variations (one of C-28/C-29 missing): 60 + 30 + (19/21 × 10) = 99.05.
