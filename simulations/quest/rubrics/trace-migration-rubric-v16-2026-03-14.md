Written to `simulations/quest/rubrics/trace-migration-rubric-v16-2026-03-15.md`.

---

**v15 -> v16 changes:**

| New | Axis | Core distinction |
|-----|------|-----------------|
| **C-46** | D | C-17 tests `(BINARY FIELD)` annotation at definition sites (EXIT BLOCK); C-34 tests bilateral structural presence (EXIT BLOCK + ENTRY REFERENCE). C-46 tests whether the annotation is symmetric — ENTRY REFERENCE positions carry the compound type annotation independently, not just "GATE = STATE required." Passes C-17 + C-34, fails C-46 = bilateral structure complete, annotation asymmetric. |
| **C-47** | D | C-45 tests that all named gates appear in the manifest. C-47 tests whether the manifest declares its own completeness condition as a named assertion ("A gate named in any block but absent from this manifest = incomplete registry"). Passes C-45, fails C-47 = manifest is complete by enumeration but states no rule by which a future omission is detectable. |

**Scoring:** 275 -> 285 pts · 45 -> 47 criteria · 37 -> 39 aspirational · Golden 206 -> 206 (72%).

**The gate promotion chain is now fully annotated at both anchors:** C-21 (gate exists) → C-17 (EXIT BLOCK annotated) → C-34 (both positions structurally present) → C-46 (both positions annotated). And the manifest coverage chain is complete: C-37 (manifest exists) → C-45 (all gate types enumerated) → C-47 (completeness condition self-stated).
