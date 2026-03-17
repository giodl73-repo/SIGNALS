Saved to `simulations/quest/rubrics/review-design-variate-R12-2026-03-14.md`.

---

## Round 12 Variations — `review-design`

**Rubric**: v11 (C-01 through C-35, denominator 28)
**Baseline**: R11 V-05 (F-01 through F-27 all carried)

---

### V-01 | Axis: Role Sequence — Domain-First Ordering

**Hypothesis**: Domain experts generate findings before stock disciplines in BLOCK 2. BLOCK 1.5 and BLOCK 2 list Domain reviewers first, Stock disciplines second. Tests whether generation order changes consensus convergence pattern and whether a new "ordering commitment" enforcement gap emerges (the committed order in BLOCK 1.5 should be checkable against actual BLOCK 2 generation order).

**Key structural difference**: BLOCK 1.5 explicitly sequences Domain before Stock. BLOCK 2 header says "Domain reviewers generate first." All 27 F-IDs carried unchanged.

**New feature candidate**: A cross-block ordering-fidelity halt — if BLOCK 2 generation order does not match BLOCK 1.5 committed sequence, a named halt fires. This is a new enforcement class: sequence integrity (distinct from count parity, identity integrity, content completeness).

---

### V-02 | Axis: Output Format — Section-Anchored Column Order

**Hypothesis**: BLOCK 2 tables reorder columns to `Section / Sev / Finding` (section is leftmost). BLOCK 2.5 uses a per-tier matrix (row per tier) instead of a single summary row. Tests whether section-first column order makes F-27 enforcement more salient — a blank leftmost cell on a P1 row is visually impossible to miss — and whether the matrix form for BLOCK 2.5 surfaces a per-tier Status enforcement gap.

**Key structural difference**: BLOCK 2 columns are `Section | Sev | Finding`. BLOCK 2.5 has columns `Tier | Count | Status | Rationale` (one row per tier). All 27 F-IDs carried.

**New feature candidate**: Per-tier Status enforcement in BLOCK 2.5 — a named halt that fires when a per-tier Status cell is absent or has an invalid value, complementing F-19 (inversion rationale) with a per-row structural integrity check.

---

### V-03 | Axis: Lifecycle Emphasis — Amend-Primary

**Hypothesis**: BLOCK 5 is declared the primary deliverable; BLOCKS 0-4 are labeled `[Evidence]`. BLOCK 5 gains a fifth column: **Priority Rank** (integer 1 to P1_count, no duplicates). Tests whether action-primary framing changes output quality and whether Priority Rank surfaces two new enforcement gaps: rank completeness (every row has a rank) and rank uniqueness (no two rows share the same rank).

**Key structural difference**: Opening sentence frames BLOCK 5 as the output. BLOCK 5 table: `Priority Rank | P1 Finding | Section | Action | Re-run Scope`. All 27 F-IDs carried.

**New feature candidate (C-36)**: Priority Rank completeness halt — fires when any BLOCK 5 row has an empty Priority Rank cell.
**New feature candidate (C-37)**: Priority Rank uniqueness halt — fires when two or more BLOCK 5 rows share the same Priority Rank value.

---

### V-04 | Axis: Phrasing Register — Second-Person Imperative

**Hypothesis**: All block headers and F-ID trigger clauses use second-person imperative: `You SHALL`, `STOP: do not continue until`, `REQUIRE: populate before proceeding`. Register isolation (C-23) is preserved because imperative register is formal, not calibrating. Tests whether `STOP:` prefix is more reliably instruction-following than `fires when... halt` third-person form, and whether a new register-boundary criterion emerges: the boundary between imperative headers and descriptive body prose may itself need an enforcement declaration.

**Key structural difference**: All F-ID lines read `STOP: if [condition], halt and [remedy]` instead of `fires when [condition]. Halt.` Block headers read `You SHALL [action]`. All 27 F-IDs carried in the new register.

**New feature candidate**: Remediation-action completeness — STOP clauses in V-04 specify not just the halt condition but the corrective action ("halt and populate it", "halt and correct the mismatch"). This is structurally richer than bare `fires... halt`. If other variations without explicit remediation actions score 100, a new criterion requiring STOP clauses to name a specific corrective action becomes a C-36 candidate.

---

### V-05 | Axes: Role Sequence + Lifecycle Emphasis + Inertia Framing

**Hypothesis**: Three axes combined. Design is framed as committed and in-flight (inertia framing). BLOCK 0 gains a fourth column: **Amendment Cost** (High/Medium/Low). Domain experts run first. BLOCK 5 is primary with Priority Rank ordered by amendment cost from BLOCK 0. This creates a cross-block continuity contract: BLOCK 0 Amendment Cost feeds BLOCK 5 Priority Rank ordering, which may surface a new enforcement class — cross-block cost-continuity integrity.

**Key structural difference**:
- BLOCK 0: `Signal Phrase | Location | Amendment Cost | Disposition`
- BLOCK 1.5: Domain-first ordering
- BLOCK 5: `Priority Rank | P1 Finding | Section | Action | Re-run Scope` with rank ordered by BLOCK 0 cost tags
- All 27 F-IDs carried

**New feature candidate (C-36 or C-37)**: BLOCK 0 Amendment Cost completeness halt — fires when any BLOCK 0 catalogue row has an empty or invalid Amendment Cost cell (same enforcement class as F-21, F-23, F-25, etc. — content-completeness-within-structural-presence, fifth column variant).
**Second candidate**: BLOCK 0↔BLOCK 5 cost-continuity verification — fires when the Priority Rank ordering in BLOCK 5 does not reflect the Amendment Cost tags from BLOCK 0 for the corresponding signals. A new cross-block ordering integrity class.

---

### Variation Summary

| Var | Axis | Key Change | Above-Ceiling Candidate |
|-----|------|-----------|------------------------|
| V-01 | Role sequence | Domain-first in BLOCK 1.5 + BLOCK 2 | Sequence-integrity halt (BLOCK 1.5 order = BLOCK 2 generation order) |
| V-02 | Output format | Section-first column order; BLOCK 2.5 matrix form | Per-tier Status cell enforcement in BLOCK 2.5 |
| V-03 | Lifecycle emphasis | BLOCK 5 primary; Priority Rank 5th column | C-36: rank completeness; C-37: rank uniqueness |
| V-04 | Phrasing register | `STOP: halt and [remedy]` throughout | Remediation-action completeness in halt clauses |
| V-05 | Combination | Domain-first + amend-primary + inertia framing + BLOCK 0 Amendment Cost | BLOCK 0 cost completeness halt; BLOCK 0↔BLOCK 5 cost-continuity integrity |
