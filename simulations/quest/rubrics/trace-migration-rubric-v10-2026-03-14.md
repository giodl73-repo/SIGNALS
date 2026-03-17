Written to `simulations/quest/rubrics/trace-migration-rubric-v10-2026-03-15.md`.

---

**What changed v9 → v10**

One new aspirational criterion extracted from R10 V-03's excellence signal:

| New | Source | Distinction |
|-----|--------|-------------|
| **C-34** Phase Boundary Dual-Anchor Gate Block | V-03 axis — every phase boundary carries EXIT BLOCK (bottom of preceding phase) + ENTRY REFERENCE (top of succeeding phase), both with "(BINARY FIELD)" annotation | C-21 tests whether all transitions are gated. C-17 tests whether gate fields carry compound annotation at their definition site. C-34 tests whether the gate appears at **both** positions per boundary. PASS C-21/C-17, FAIL C-34 if each gate is anchored at only one side. |

**Scoring:** 215 → 220 total max (26 aspirational, 130 pts). Golden threshold 176 pts (80%).

---

**Why only one new criterion**

V-01 and V-02 were the C-19 and C-30 axes respectively — both already C-33 criteria. V-04 established that C-19 + C-30 compound orthogonally without conflict, which is a design observation, not a new structural requirement. V-03 is the only variant that introduced a genuinely new structural mechanism: bilateral gate annotation at phase boundaries.
