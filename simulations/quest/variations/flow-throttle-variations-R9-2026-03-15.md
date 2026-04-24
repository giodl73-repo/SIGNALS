Written to `simulations/quest/golden/flow-throttle-variate-R9-2026-03-16.md`.

---

## flow-throttle Variate — Round 9 (v9 Rubric)

**Baseline:** R8 V-05 passes C-01–C-24. Two new criteria for R9:
- **C-25** — The C-20 prose-restriction declaration must name what is *not* prose (gate decision lines, cross-artifact header lines, prohibition lines, verdict lines) so element classification doesn't require content inspection.
- **C-26** — The TYPE SCAN GATE must carry a Purpose annotation referencing C-22, naming the failure mode prevented (category elision), and explaining why the gate is necessary given that C-22 already requires type coverage.

---

### Variation Map

| | Axes | C-25 | C-26 |
|--|------|------|------|
| **V-01** | Inertia framing (single) | PASS | PASS |
| **V-02** | Phrasing register (single) | PASS | PASS |
| **V-03** | Lifecycle emphasis (single) | PASS | PASS |
| **V-04** | Role sequence + Inertia framing | PASS | PASS |
| **V-05** | Role sequence + Lifecycle emphasis + Inertia framing | PASS | PASS |

---

### V-01 — Inertia Framing
Names the specific escape-route misjudgments: "content inspection treats PROCEED as prose" (C-25) and "C-22 makes the gate redundant" (C-26). Both are named and rebutted at their enforcement points.

### V-02 — Phrasing Register
C-25 and C-26 in explanatory/WHY-first register rather than normative SHALL form. The conceptual gap is framed as a comprehension problem, not a compliance problem. Gate Purpose explains *why* C-22 is insufficient without a construction-time check.

### V-03 — Lifecycle Emphasis
C-25 elevated to a parallel **STRUCTURED OUTPUT REGISTER** sub-section (table with Element type / Canonical form / Prose? / C-23 tag required? columns). C-26 expanded to a **three-field annotation block**: Failure mode prevented / Gap above C-22 / Audit test.

### V-04 — Role Sequence + Inertia Framing
Format Analyst role activates before Domain Expert and produces the entire OUTPUT FORMAT CONTRACT (prose-permitted list + structured-output exemption class) as a role output — making the exemption class a precondition rather than an annotation. C-26 carries the "redundancy" escape-route rebuttal.

### V-05 — All Three Axes
Three-role pipeline (Format Analyst → Domain Expert → Consequence Analyst), STRUCTURED OUTPUT REGISTER as a named table, three-field C-26 annotation block, plus full escape-route framing for both criteria including the structural proof that C-22 and the TYPE SCAN GATE operate at different points in the execution timeline. Strongest candidate for 180/180.
