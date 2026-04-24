Here is the complete updated rubric — **v18**, written to `simulations/quest/rubrics/discover-literature-rubric-v18-2026-03-20.md`.

---

**What changed:**

**C-36 — Structural Analogy Named in C-34 Sub-Section** (V-05 R17 excellence signal 2)

The C-34 labeled sub-section must contain an explicit statement of the structural analogy — "C-34 is to C-33 what C-25 is to C-23" — making the recursive design logic self-evident from within the labeled sub-section. This follows the same embedding pattern used throughout the chain: N-of-4 counter in C-25, remove-either-pair test in C-26, grep instructions in C-29/C-32 — in each case a design principle that would otherwise be implicit in the criterion text becomes visible directly in the output element it governs. C-35 PASS required; both pairs (C-34/C-33 and C-25/C-23) must be named; statement in surrounding prose outside the sub-section boundary fails.

**New Key Decisions from R17:**
- **C-34 scattered-prose failure (V-01 R17):** Elements named inline without a labeled heading satisfies C-33 but not C-34 — "scattered" is the failure mode
- **C-35 wrong-terminal failure (V-03 R17):** Chain stopping at `C-32 complete` instead of `C-33 complete` — the chain was not extended to include the current ceiling
- **C-35 interior-gap failure (V-04 R17):** Correct terminal (C-33) but C-30 absent — wrong-terminal and interior-gap are symmetric, independent failure modes

**Scoring delta:**

| | v17 | v18 |
|--|-----|-----|
| Aspirational criteria | 27 | 28 |
| Aspirational ceiling | 135 | 140 |
| Total ceiling | 225 | **230** |
