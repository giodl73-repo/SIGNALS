Written to `simulations/quest/rubrics/flow-throttle-rubric-v16-2026-03-16.md`.

---

**What changed in v16**

One new criterion extracted from Round 15:

| ID | Source | Pattern |
|----|--------|---------|
| **C-41** | V-04 | Annotation-inventory count as Phase 1 role-activation gate — the C-38 count declaration is elevated from an instructional header to a Role 2 / Phase 1 entry condition. A count discrepancy returns to Role 1 before Phase 1 opens (before any body content is generated), not after. Parallel to C-34→C-36 (observable-count at path labels → Role 3 activation condition) applied to the annotation inventory count at the Phase 1 boundary. |

**Score delta**: 160 pts (32 × 5) → 165 pts (33 × 5), max composite 250 → 255. Golden threshold unchanged.

The structural progression table now has a complete sixth column:

| Instructional | Contract-lock | Count-closed | Closure-declared | Prohibition-enforced | Role-gate |
|---|---|---|---|---|---|
| C-33 | C-35 | — | — | — | — |
| C-34 | C-36 | — | — | — | — |
| C-18 | C-37 | C-38 | C-39 | C-40 | **C-41** |

V-03 contributed a clarification to C-40 (not a new criterion): the PROHIBITED clause must be physically co-located inside the annotation inventory, not in a sibling FORMAT CONTRACT block. That co-location requirement is now explicit in C-40's pass condition.
