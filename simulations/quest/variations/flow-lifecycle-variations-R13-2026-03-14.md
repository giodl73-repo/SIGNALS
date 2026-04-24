Written to `simulations/quest/rubrics/flow-lifecycle-rubric-v13-variate-R13-2026-03-15.md`.

---

# flow-lifecycle — Round 13 Variations (Rubric v13)

**Open criteria**: C-42 (B-NN→Exception) and C-43 (Phase Exit forward linkage)

**Axis map:**

| Variation | Axes | Bottleneck Analysis change | B-NN block change | Exit Gate change | New CHAIN STATUS directions |
|-----------|------|---------------------------|-------------------|------------------|-----------------------------|
| V-01 | G1 | Gate check: every B-ID must appear in ≥1 EX block | none | none | `B-NN→Exception` |
| V-02 | G1+G2 | Gate check + explicit refs requirement | `Exception Refs:` sub-field per B-NN | none | `B-NN→Exception` (enhanced with consistency check) |
| V-03 | H | none | none | `Next phase:` sub-field; last phase NONE/END | `Phase-exit-sequence` |
| V-04 | G1+H | Gate check | none | `Next phase:` | both |
| V-05 | G1+G2+H | Gate check + explicit refs | `Exception Refs:` | `Next phase:` | both (enhanced) |

**Key structural decisions:**

**C-42 probe design** — mirrors C-40's discriminating pattern exactly: C-40 had (a) EX block `Role Ref:` sub-field and (b) Role Registry Gate fourth check. C-42's analog is (a) EX block `Bottleneck Ref: B-ID` — already established in R11, so the base architecture satisfies the Exception→B direction — and (b) the gate check that every declared B-ID appears in at least one EX block. V-01 isolates the gate check (is it sufficient?). V-02 adds per-B-NN explicit `Exception Refs:` listing (is per-block explicitness required?).

**C-43 probe design** — V-03 tests the `Next phase:` sub-field in isolation. The last-phase NONE/END sentinel is the discriminating boundary marker. Together with C-41's `Prior phase:` (already in base from R12), V-03 presents the complete bidirectional Phase→Phase pair.

**CHAIN STATUS growth:** R12 V-05 had 9 directions. R13 V-05 has 11 — adding `B-NN→Exception` and `Phase-exit-sequence`.
