Written to `simulations/quest/rubrics/flow-throttle-rubric-v17-2026-03-16.md`.

---

**What changed in v17**

Three new aspirational criteria extracted from R16 excellence patterns:

| ID | Source | Pattern |
|----|--------|---------|
| **C-42** | All 5 R16 variations | Audit block extended with a named Field 5 that explicitly verifies the C-41 gate reached CLEARED before Step 1A — gate compliance is a first-class audit target, not inferred from body quality |
| **C-43** | V-03, V-05 | Two-signal handoff chain: FORMAT CONTRACT COMPLETE (Role 1 → verifier) and INVENTORY VERIFIED (verifier → Role 2) — the two signals are distinct and cannot be conflated; "sections present" vs. "count verified" is structurally visible |
| **C-44** | V-05 | Inertia-frame rejection: the "looks complete" bypass is named and defeated with a structural proof that FORMAT CONTRACT COMPLETE confirms section presence but not count completeness — parallel to C-26 at Step 1B |

**Score delta**: 165 pts (33 × 5) → 180 pts (36 × 5), max composite 255 → 270. Golden threshold unchanged.

**Structural progression table** gains a seventh column (Audit-covered layer) with C-42 on the annotation row. C-43 and C-44 extend the C-41 gate design architecture rather than adding a new layer column, noted below the table.
