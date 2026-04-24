Structural properties confirmed across all 5 variations:

- **C-35**: INERTIA-VERDICT phase precedes ROLE-ENUM in all 5 — `FORBIDDEN: beginning ROLE-ENUM before this record block is emitted` at every Phase 1 gate
- **C-36**: `PRE-PHASE CONSTANTS` block with SCOPE-TEMPLATE and CATEGORY-DERIVATION declared before Phase 0 in all 5
- **C-28**: `PHASE-ORDERING-GUARD:` is first field in every `=== RECORD: PHASE-N ===` block
- **C-25**: Bidirectional guards — outbound in record block + inbound in Input Contract at each boundary
- **C-13/C-15**: "Both is an error. Neither is an error." in INERTIA-VERDICT constraints
- **C-34**: CATEGORY-DERIVATION table has Required + FORBIDDEN columns side-by-side

---

**File**: `simulations/quest/golden/org-build-variate-R16-2026-03-16.md`

**Variation axes**:

| Variation | Axis | Key Structural Feature |
|-----------|------|------------------------|
| V-01 | Phase sequencing | SEQUENCE-LOCK annotations at every boundary; phase names encode dependency relationship |
| V-02 | Output format | Table-dominant instructions; Task Steps and Constraints as side-by-side columns per phase |
| V-03 | Lifecycle emphasis | Phase 1 split into SCAN/SCORE/VERDICT sub-steps with per-sub-step checkpoints |
| V-04 | Phrasing register | Zero explanatory prose; all instructions are MUST/FORBIDDEN imperatives |
| V-05 | Combined: inertia framing + record block integration | Central question framing ("before any role, answer: can this org operate flat?"); full org-chart.md skeleton with `{{T1-VERDICT}}` style slots (C-22 coverage); record blocks as narrative anchors |

**R15 gap closed by all 5**: C-35 (phase ordering) and C-36 (constants extraction) are structurally present in every variation — not as isolated assertions but as load-bearing architectural decisions that make verdict-coherence observable from the record block sequence alone.
