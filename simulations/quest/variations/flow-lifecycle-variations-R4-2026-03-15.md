Written to `simulations/quest/golden/flow-lifecycle-variate-R4-2026-03-15.md`.

---

## Round 4 Variations — Summary

**Single-axis:**

| Variation | Axis | C-18 Mechanism | C-19 Mechanism |
|-----------|------|---------------|---------------|
| **V-01** | Output format | Anti-pattern rules in table column headers (Role Name, Entry/Exit Trigger, Decision Condition, Fallback, SLA Impact columns each carry inline negation) | Scan Table A + Scan Table B + CLOSED gate |
| **V-02** | Role sequence | Generic-label rule inline in Role Name column header — the most common C-18 miss, caught at first authoring step | Single path-per-row terminal scan + CLOSED gate |
| **V-03** | Phrasing register | Imperative field definitions with inline "is a fail" at each constrained field — Step 2 role table, Step 4 trigger columns, Step 5 decision condition | Directive output gate ("Do not write until CLOSED") |

**Combined:**

| Variation | Axes | Design Logic |
|-----------|------|-------------|
| **V-04** | Role sequence + output format | C-18 at two schema locations: role registry header + state table trigger columns. Scan tables achieve C-19. Role-first ordering means generic-label failure is caught before any state is authored. |
| **V-05** | Role sequence + output format + Phase Delta + Scan Tables + Artifact Gate | Three C-18 locations (role registry, state trace triggers, decision condition). Phase Delta blocks (entry contract + exit gate per phase) achieve C-16. Scan Table A + Scan Table B + the exact "artifact may not be written until Scan Summary shows status CLOSED" phrasing achieves C-19 at the artifact boundary, distinct from C-13's criterion ordering. |

**Key design distinctions from prior rounds:**
- V-01–V-04 all achieve C-18 with ≥2 inline schema negations — but vary in which tables carry them and in what register
- V-05's C-18 placement mirrors the R3 V-05 pattern that introduced C-18: negations inside schema block headers and cell definitions at three locations, not collected in any preamble
- C-19's CLOSED gate language is kept consistent across all five ("artifact may not be written until Scan Summary shows status CLOSED") so scoring variance between variations is attributable to other axes, not to C-19 phrasing drift
