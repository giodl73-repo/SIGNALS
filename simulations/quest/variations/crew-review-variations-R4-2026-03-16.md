Written to `simulations/quest/golden/crew-review-variate-R4-2026-03-16.md`.

---

## crew-review Variate R4 -- Summary

**Design target**: Three new aspirational criteria (C-17, C-18, C-19) introduced in rubric v4. Each was sourced from a different R3 variation but no single R3 variation held all three. R4 isolates each as a primary axis, then combines.

---

### Variation axes and hypotheses

| Var | Primary axis | Aspirational target | Key mechanism |
|-----|-------------|---------------------|---------------|
| V-01 | Inertia framing | **C-17** | Named gate G1 with explicit open/closed state and 5-point closure condition. Domain review references G1 by name: "does not begin until G1 closes." Gate is a named variable, not an instruction. |
| V-02 | Output format | **C-18** | Slot-to-row escalation rule: each unfilled slot produces a full 4-column matrix row, placed in the matrix after the challenger primary row. Rule states explicitly: not a sentence inside Findings, not an appended note, each unfilled slot = its own row. |
| V-03 | Output format | **C-19** | 5-column schema where every column definition includes a "NOT:" anti-pattern exclusion inside the column's type definition -- not a separate general instruction. Schema is self-documenting about its own violation patterns. |
| V-04 | Inertia framing + Output format | **C-17 + C-18** | Gate G1 exit condition is defined in terms of row production: gate cannot close unless every unfilled slot has a dedicated separate matrix row. C-18 is enforced by the gate mechanism -- satisfying C-17 requires satisfying C-18. |
| V-05 | Output format + Inertia framing + Role sequence | **C-17 + C-18 + C-19** | All three mechanisms together: typed schema with anti-pattern exclusions per column (C-13+C-19), gate exit condition requiring separate slot rows (C-15+C-17+C-16+C-18), Lens column (C-12). Three mechanisms mutually reinforcing. |

---

### C-17 pattern to watch

The gate pattern (V-01, V-04, V-05) uses named gate state rather than sequence instruction:

> `G1 exit condition: ... Domain review does not begin until G1 exits.`

Contrast with R3 V-04: `Domain review does not begin until PHASE 2 exits` -- close, but the gate here is a named variable with an explicit enumerated closure condition, not a phase-boundary statement.

### C-18 pattern to watch

The separate-row escalation (V-02, V-04, V-05) specifies:
- Full 4 (or 5) column row
- Placed in the matrix (same structure as domain findings)
- Explicitly NOT a sentence inside the challenger row's Findings cell
- Explicitly NOT an appended note
- Two unfilled slots = two rows

### C-19 pattern to watch

The anti-pattern column table (V-03, V-05) uses "Type -- valid | Anti-pattern excluded (NOT valid)" for every column, e.g., Findings column: `NOT: abstract observations without a named surface ("needs more detail", "unclear", "incomplete")`. The exclusion is inside the column definition, not a separate instruction.
