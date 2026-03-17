Written to `simulations/quest/rubrics/flow-throttle-rubric-v18-2026-03-16.md`.

---

**What changed in v18**

Four new aspirational criteria extracted from R17 excellence patterns:

| ID | Source | Pattern |
|----|--------|---------|
| **C-45** | V-02, V-05 | Signal distinction table with a dedicated "Does NOT confirm" column — each signal's limitation is column-scannable rather than prose-embedded. C-43 allows non-conflation in prose; C-45 requires it as a named column value, making limitation inspection a scan task rather than a parse task |
| **C-46** | V-05 | Prompt-header signal chain declaration — the role activation chain table at the prompt header shows SIG-01 and SIG-02 as separate cells before any role body begins. C-43 requires the chain to be visible in role architecture; C-46 requires it to be visible at the architectural entry point, before any role activates |
| **C-47** | V-02 | Bypass-attempt rejection register — the C-44 bypass defeat is recorded as a typed-row register (Bypass attempt / Attempt type / Structural reason columns) rather than embedded prose. Parallels C-22 above C-09: C-44 allows a named section; C-47 requires a typed, auditable row |
| **C-48** | V-05 | Required-fill bypass rejection field as verification prerequisite — a fill field (BYPASS ATTEMPT IDENTIFIED AND REJECTED / NO BYPASS ATTEMPT DETECTED) that must be completed before the verification table opens, making bypass rejection a structural gate rather than a named section. Parallels C-36/C-41 elevations in the annotation inventory chain |

**Score delta**: 180 pts (36 × 5) → 200 pts (40 × 5), max composite 270 → 290. Golden threshold unchanged.

**Structural progression table** gains a new two-column extension section below the main table showing the C-43/C-44 patterns and their C-45/C-46/C-47/C-48 progressions: left column traces signal-chain visibility (role architecture → column-readable → prompt header); right column traces bypass-rejection enforcement (named section → typed register row → required-fill gate).
