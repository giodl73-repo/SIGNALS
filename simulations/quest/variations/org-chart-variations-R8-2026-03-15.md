Written to `simulations/quest/golden/org-chart-variate-R8-2026-03-16.md`.

---

## Round 8 — org-chart Variations (V-01 through V-05)

**R7 ceiling recap:** V-03/R7 was the synthesis breakthrough — first design to hold all four structural features (4-part inertia + count guard + ORG-ELEMENT REGISTER + typed APW citations) in a single variation, scoring 99.4 (16/17). It fails C-25 because every compliance directive is descriptively framed ("by convention," "the purpose is to serve as"). R8's sole target: add imperative-mode language and reach 17/17.

---

### Variation Map

| V | Axis | Hypothesis | Predicted |
|---|------|------------|-----------|
| **V-01** | Phrasing register — targeted imperative injection | Append imperative directives (`DO NOT EMIT`, `MUST produce`, `REQUIRED: MUST open each cell`) to the three compliance points in V-03/R7; leave all other prose conversational. Minimal diff, passes C-25 by construction. | 17/17 |
| **V-02** | Phrasing register — full imperative conversion | Replace all conversational/descriptive framing in V-03/R7 with DO/DO-NOT/MUST style throughout. Eliminates descriptive framing completely; matches V-01/R6 register style. Risk: slight output compression, but all structural criteria hold. | 17/17 |
| **V-03** | Phrasing register — enforcement block injection | V-03/R7 conversational prose preserved verbatim; isolated `[ENFORCEMENT: ...]` blocks injected as labeled sections at the three compliance points. Tests whether block-adjacent imperative framing satisfies C-25 vs. inline integration. If evaluators require inline imperative, this scores 16/17. | 17/17 (or 16/17) |
| **V-04** | Phrasing register + inertia framing | V-01/R8 targeted injection plus V-01/R7's two-step count-verification protocol (count reasons, verify >= 2, then emit separator). Adds a second reliability layer for C-23 without restructuring V-03/R7. | 17/17, higher C-23 confidence |
| **V-05** | Phrasing register + output format | V-02/R8 full imperative plus a `MUST PRECEDE` gate on the register section: explicit assertion that Org Evolution Roadmap is gated on register completion, and that inline notes do not substitute. Reinforces C-21 physical-distinctness requirement. | 17/17 |

---

### Key design decisions

**Why three single-axis before combining?** C-25 is a framing criterion, not a structural one. The question is which *form* of imperative injection is sufficient and most maintainable: targeted (V-01), full (V-02), or block-isolated (V-03). Understanding which form satisfies the evaluator before combining avoids over-engineering V-04/V-05.

**V-03's falsifiable prediction.** The rubric says "evaluators check C-25 by locating the skill's guard enforcement, register construction, and citation format directives." If "locating" means finding imperative language *anywhere* in the directive region (including labeled blocks), V-03 passes. If it requires inline integration in the running directive prose, V-03 fails. This is the diagnostic question V-03 answers.

**V-04 vs V-01.** V-01 predicts 17/17; V-04 adds the two-step count protocol specifically to harden C-23. If V-01 already produces reliable C-23 scores, V-04 is redundant but not harmful. If V-01 shows occasional count-mismatch failures in further runs, V-04 is the preferred production form.
