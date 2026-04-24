Written to `simulations/quest/golden/topic-plan-variate-R4-2026-03-15.md`.

---

## Round 4 Variations — topic:plan

**Rubric target**: C-17 (two-tier sentinel vocabulary), C-18 (pre-signal defense register), C-19 (integer-enforcement gate language), C-20 (sequential phase-linked stop gates)

---

### V-01 — Formal Vocabulary Contract (C-17)

**Axis**: Output format — single axis

**Key mechanism**: A standalone `VOCABULARY CONTRACT` block placed *before* any schema. Defines `??` (OPEN OBLIGATION) and `--` (CLOSED DECISION) as a formal two-column specification with named violations: TOKEN LEFT OPEN, PREMATURE CLOSURE, SILENT OMISSION.

**Delta from R3**: R3 V-01 embedded the `??`/`--` rule inside a "Pre-committed schema" section header. R4 separates it into a first-class contract block that the model processes before encountering any cell to fill.

---

### V-02 — Pre-Signal Defense Register as Phase 0 (C-18)

**Axis**: Role sequence — single axis

**Key mechanism**: Defense register is Phase 0. Strategy.md is read only for its dimension list, then *closed* before any artifact search begins. Proposals in Phase 4 must cite the Phase 0 defense register by row number — generic rationale ("new evidence found") is named as a removal-before-applying violation.

**Delta from R3**: R3 V-04 placed the register at Step 2 with strategy.md still in working memory. R4 Phase 0 closes the file before any artifact opens.

---

### V-03 — Sequential Phase-Linked Gates + Integer-Enforcement Gate Language (C-19 + C-20)

**Axis**: Lifecycle emphasis — single axis (two criteria share the same axis: both make failure detectable by name)

**Key mechanism**: Every stop gate says "Do not advance to Phase N+1" with the explicit next-phase number. The delta phase adds an `INTEGER ENFORCEMENT RULE`: writing "a few", "several", "some", "multiple", "many" is a *gate failure*, not a quality concern. Non-integer = named, detectable failure condition.

**Delta from R3**: R3 V-03 gate numbering was inconsistent. No prior round used "gate failure" language for fuzzy counts.

---

### V-04 — Vocabulary Contract + Defense Register (C-17 + C-18)

**Axis**: Output format + Role sequence — combined

**Key mechanism**: VOCABULARY CONTRACT block governs all cell-level representation; Phase 0 defense register governs all proposal-level justification. The two mechanisms reinforce: `??` cells in Schema B force explicit filling before artifact search, and `--` in "Override threshold" is the correct CLOSED DECISION token when a threshold is genuinely unspecifiable.

---

### V-05 — Full Combination (C-17 + C-18 + C-19 + C-20)

**Axis**: Full combination

**Key mechanism**: All four criteria as dedicated named structural components:
- `VOCABULARY CONTRACT` block before all content (C-17)
- Schema B as pre-committed Phase 0 output, strategy.md closed before artifact search (C-18)
- `INTEGER ENFORCEMENT RULE` at Phase 2 naming banned forms as "gate failure" (C-19)
- Every gate says "Do not advance to Phase N+1" — no exceptions (C-20)
- TOKEN LEFT OPEN scan at every phase gate

**Structural risk ranking** (lowest risk): V-05 > V-04 > V-02 > V-03 > V-01. V-05 gives each criterion its own mechanism inside a numbered phase with an exit gate.
