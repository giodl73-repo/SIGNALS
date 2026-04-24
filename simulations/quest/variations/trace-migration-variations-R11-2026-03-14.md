Written to `simulations/quest/rubrics/trace-migration-variations-R11-2026-03-15.md`.

---

# trace-migration — Round 11 Variations (v10 rubric)

**New criterion:** C-34 (Phase Boundary Dual-Anchor Gate Block, 5 pts aspirational). Max now 220, golden threshold 176.

---

## Variation Summary

| V | Axis | C-34 Mechanism | C-19 | C-30 |
|---|------|----------------|------|------|
| V-01 | Lifecycle emphasis | Named BOUNDARY CHECKPOINT sections at both positions | Global citation instruction | Behavioral B2 instruction (→ PARTIAL likely) |
| V-02 | Output format | 2-row boundary gate table: EXIT row at preceding bottom, ENTRY row at succeeding top | Per-section CITATION ANCHORs | Named INERTIA-SEED-B artifact |
| V-03 | Phrasing register | Imperative → PROPAGATE / ← RECEIVED FROM directives | Global citation instruction | Behavioral B2 instruction (→ PARTIAL likely) |
| V-04 | V-01 + V-03 combined | Named BOUNDARY CHECKPOINT sections + imperative cross-references within each slot | Per-section CITATION ANCHORs | Named INERTIA-SEED-B artifact |
| V-05 | All three axes, full backbone | Named sections + 2-row tables + imperative cross-references | Per-section CITATION ANCHORs | Named INERTIA-SEED-B with 3-column checklist |

---

**Key design decisions:**

- **V-01 hypothesis:** C-34 failure = missing named section (easier to detect than missing annotation on present gate field).
- **V-02 hypothesis:** C-34 failure = table row count = 1 when 2 required (mechanical count check, not annotation search). The 2-row table straddles the boundary — each position fills its row; a reader checking either section sees the incomplete half.
- **V-03 hypothesis:** C-34 failure = broken directional reference chain — an unexecuted `→ PROPAGATE` command or a missing `← RECEIVED FROM` source declaration is parse-checkable from either side.
- **V-04:** Two independent detection surfaces for C-34. Missing section OR broken cross-reference — either fires independently.
- **V-05:** Three detection surfaces simultaneously. A C-34 violation must evade named section check, row-count check, AND cross-reference check to survive undetected. Highest structural redundancy of any variation.

**Predicted scores (v10 rubric, 220 max):**
- V-01: ~215 (C-30 likely PARTIAL from behavioral instruction only)
- V-02: ~217.5 (C-34 PASS via table format; strong C-19/C-30 from backbone)
- V-03: ~215 (C-30 likely PARTIAL, same as V-01)
- V-04: 220 (C-34 dual-enforced + full R10 C-19/C-30 machinery)
- V-05: 220 (C-34 triple-enforced + full R10 V-05 backbone)
