Written to `simulations/quest/rubrics/trace-migration-rubric-v15-2026-03-15.md`.

---

**v14 → v15 changes:**

| New | Axis | Core distinction |
|-----|------|-----------------|
| **C-44** | D | C-42 creates ALIGNMENT STATE as a record; C-44 tests whether it's wired into the Phase A-to-B EXIT BLOCK as a named gate condition. Passes C-42, fails C-44 = alignment tracked but not enforced at the boundary. |
| **C-45** | D | C-37 manifests boundary-transition gates; C-45 tests whether the manifest is extended to include the C-43 substrate gate and C-44 alignment gate. Fails = a content-category gate failure is invisible to manifest-level verification. |

**Scoring:** 265 → 275 pts · 43 → 45 criteria · 35 → 37 aspirational · Golden 206 → 206 (75%).

The key structural logic: C-44 completes the gate promotion chain — C-41 (constraint) → C-43 (parse-return gate) → C-42 (alignment record) → C-44 (alignment gate wired into boundary). C-45 closes the manifest coverage gap that opens when the gate architecture grows beyond boundary-transition gates: the PROTOCOL COUNT MANIFEST becomes the authoritative single verification surface only when it enumerates all named gates, not just the boundary layer.
