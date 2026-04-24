Written to `simulations/quest/golden/mock-review-variate-R6-2026-03-15.md`.

---

## Summary

**R6 produces 5 complete variations targeting C-22, C-23, C-24.**

### Axis map

| V | Single/Combined | Axis | New criterion targeted |
|---|----------------|------|----------------------|
| V-01 | single | inertia-framing | C-22 — DEFAULT DECISION POSITION block, PM-first, single Rationale slot. Isolates inertia framing from role ordering. |
| V-02 | single | output-format | C-23 — Structural position slot label changed to `Structural position (Strategy SQ-1 tier decision):` making SQ-1 a named field requirement. Names SLOT-LABEL VIOLATION as detectable error. |
| V-03 | single | lifecycle-emphasis | C-24 — Replaces the conditional `{if eval-driven}` format with two explicit sub-templates per priority bucket: eval-driven entries require `{Artifact state field}` unconditionally; auto-flagged entries use `trigger: {value}`. Names traceability break as detectable error. |
| V-04 | combined | output-format + lifecycle-emphasis | C-23 + C-24, Strategy-first ordering. No inversion block. Tests whether SQ-1 anchor + explicit sub-templates together close the gaps without inertia framing. |
| V-05 | combined (ceiling) | all three + Strategy-first | C-22 + C-23 + C-24 + all R5 V-05 ceiling criteria. All prior criteria (C-09 through C-21) preserved. |

### Key structural innovations in R6 vs R5

- **C-23**: The slot label `Structural position (Strategy SQ-1 tier decision):` is a mechanical change — the label itself forces the author to produce a decision name + type classification, making a generic statement a *named violation* rather than an under-specified fill.
- **C-24**: Two format sub-templates (eval-driven vs auto-flagged) removes the `if eval-driven` conditional from R5 V-05 — propagation is now unconditional for each entry type.
- **R7 forward pointer**: If V-05 closes all three criteria, the remaining gap is type-specificity in the Structural position slot — whether the type classification ("STRUCTURAL-FORM vs TIER-GATING") produces an architectural property name or just a type label.
