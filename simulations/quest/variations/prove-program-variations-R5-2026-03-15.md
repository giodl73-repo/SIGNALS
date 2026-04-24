Here are the 5 variations for `prove-program` R5, saved to `simulations/quest/golden/prove-program-variate-R5-2026-03-15.md`.

---

## Summary

**Single-axis variations (V-01–V-03)** each target one R5 criterion in isolation:

| Variation | Axis | New criterion |
|-----------|------|---------------|
| **V-01** | Lifecycle emphasis | **C-20** — GATE-1 is a two-row conjunction table (Condition A AND Condition B). Evaluates both, names a PASS only when both are TRUE. The key structural move: one gate, explicit boolean, not a checklist. |
| **V-02** | Lifecycle emphasis | **C-21** — GATE-CAL sits between findings and synthesis. Pass condition is ">=2 distinct confidence values" — presence is explicitly called out as insufficient. The FAIL names the uniform-label pattern specifically. |
| **V-03** | Output format | **C-22** — Each consumer block (E-02 onward) has the anti-pointer prohibition embedded as the opening clause of its own INPUT section, with the label "citation contract (local to this block):". Not in a preamble. |

**Combined variations (V-04–V-05)**:

| Variation | Axes | Coverage |
|-----------|------|----------|
| **V-04** | C-20 + C-21 | Symmetric quality gates at both ends — GATE-1 before planning, GATE-CAL before synthesis. Neither can be bypassed. |
| **V-05** | C-20 + C-21 + C-22 over R4 V-05 floor | Full layering. Role sequence + verbatim blockquotes + named gates + inline FAIL (R4 floor) + atomic gate (C-20) + calibration gate (C-21) + per-block contracts (C-22). Projected 160/160. |

**Key design decisions for R5:**
- C-20 is distinct from C-18+C-09 because the gate must be *one* gate with an *explicit conjunction evaluation* — V-01 uses a table with A/B rows and a single PASS line to make this unambiguous
- C-21 is distinct from C-07 because the gate condition is non-uniformity, not presence — V-02 names "all high" as a specific FAIL case
- C-22 is distinct from C-17 and C-19 because the prohibition must live *inside* each block's INPUT section — V-03 uses a named clause format that repeats per block, not just once at the top of the phase
