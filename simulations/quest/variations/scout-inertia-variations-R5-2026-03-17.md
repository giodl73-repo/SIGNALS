Written to `simulations/quest/golden/scout-inertia-variate-R5-2026-03-17.md`.

---

# scout-inertia — Prompt Variations R5

## Context

All R4 variations scored 100/100 on rubric v4. Rubric v5 adds one new criterion:

**C-18 — Per-Table Column Manifest**: immediately before each tabular section, an explicit `Required columns for this table: X | Y | Z` declaration appears. Column omission is detectable at the declaration line, not only at the table header row. This is the column-level analog of C-17 applied locally per table.

The rubric notes that R4 V-01 through V-04 all pass C-16 and C-17 but fail C-18 — "one insertion per table brings any of them into compliance."

## Variation Map

| ID | Axis | Hypothesis |
|----|------|------------|
| V-01 | Phrasing register | Minimal inline `Required columns for this table:` before each table on the Competitor Zero prose base |
| V-02 | Output format | C-18 as explicit `> Schema: X \| Y \| Z` block — visually separated from the table header |
| V-03 | Role sequence | C-18 embedded as analyst-role procedural step: "Before writing each table, write this line" |
| V-04 | Lifecycle + output format (combined) | Column manifests at the top of each table-producing phase, alongside the document-level section manifest (C-17) |
| V-05 | All axes (combined) | Full R4 V-05 scaffold + column manifests before Section C (failure modes) and Section D (inertia-loss conditions) |

---

## V-01 — Axis: Phrasing Register (Minimal Inline C-18)

Single-axis: only change from R4 V-01 is the two inline declarations before the failure mode and inertia-loss tables. Tests whether inline text achieves C-18's pre-commitment property.

The key additions (all else unchanged from R4 V-01):
- Before the Why Inertia Loses table: `Required columns for this table: # | Condition | Observable Threshold | Verification Command`
- Before the Failure Modes table: `Required columns for this table: # | Failure Mode | Trigger | Impact | Severity`

---

## V-02 — Axis: Output Format (Schema Block)

Single-axis: changes the C-18 expression from inline text to a `> Schema:` block on its own line. Visual separation creates stronger enforcement — a missing block produces a visible gap in the output structure rather than a missing inline phrase.

---

## V-03 — Axis: Role Sequence (Procedural Column Declaration)

Single-axis: embeds C-18 inside the ANALYST role as an explicit procedural step. The analyst is instructed: "Before writing each table, write this line: Required columns for this table: [columns]." Tests whether procedural generation produces the same pre-commitment property as template insertion.

---

## V-04 — Combined: Lifecycle + Output Format

Column manifests appear at the top of Phase 3 (Failure Modes) and Phase 4A (Why Inertia Loses). Combined with the document-level section manifest at the top (C-17), this creates a two-level structural contract: section omission is visible at the phase manifest; column omission is visible at the per-phase column declaration.

---

## V-05 — Combined: All Axes

Full scaffold. Every mechanism from R4 V-05 is preserved; the only additions are:
- `Required columns for this table: # | Failure Mode | Trigger | Impact | Severity` immediately before Section C
- `Required columns for this table: # | Condition | Observable Threshold | Verification Command` immediately before Section D

---

## Predicted Scores

| Variation | C-18 | C-16/C-17 (carried) | Predicted |
|-----------|------|---------------------|-----------|
| V-01 | PASS (inline) | PASS | 100 |
| V-02 | PASS (Schema block) | PASS | 100 |
| V-03 | PASS (procedural) | PASS | 100 |
| V-04 | PASS (phase-level) | PASS | 100 |
| V-05 | PASS (all positions) | PASS | 100 |

## Reliability Gradient

V-01 < V-02 < V-03 < V-04 < V-05 on adversarial robustness. V-05 requires three independent omissions to violate C-18 (phase declaration, inline declaration, and template structure all must fail simultaneously).
