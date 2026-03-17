Written to `simulations/quest/rubrics/prove-topic-rubric-v11-2026-03-17.md`.

---

**v11 adds 3 new criteria (C-39/C-40/C-41). Aspirational pool: 30 -> 33 pts. Total: 104 -> 107.**

## New Criteria

| ID | What it codifies | Source |
|----|-----------------|--------|
| C-39 | SESSION INVARIANTS block declares all five invariants (A/B/C/D/E) as a **unified complete system** — each entry with canonical failure label + stage-scope annotation. C-12 (A-D floor) + C-36 (Invariant E separately) are necessary but not sufficient. | All R10 variations |
| C-40 | ROLE A initialization **reads Stage 0 forward-commitment fields by name** (synthesis_closure_form + synthesis_mandate_label), creating the middle anchor of the Stage 0 -> ROLE A -> Stage 5 three-anchor chain — parallel to how C-31 cross-wires Stage 5 back to the ROLE A contract. | R10 V-02/V-04/V-05 |
| C-41 | Stage 0 EXIT SIGNAL **explicitly asserts synthesis_closure_form matches the pre-registered CAMPAIGN CLOSURE CANONICAL FORM** by naming both — closes the registration-to-commitment loop at Stage 0, not deferred to Stage 5. | R10 V-03/V-05 |

## R10 Scores Under v11

| Variation | Total | New pts |
|-----------|-------|---------|
| V-01 | 104/107 | +C-39 |
| V-02 | 104/107 | +C-40 |
| V-03 | 104/107 | +C-41 |
| V-04 | 105/107 | +C-39, C-40 |
| V-05 | 106/107 | +C-39, C-40, C-41 |

The structural pattern C-39/C-40/C-41 codify is a **three-anchor pre-commitment verification spine**: the SESSION INVARIANTS unified governance declaration (C-39) + Stage 0 commitment verified at ROLE A (C-40) + registration-to-commitment loop closed at Stage 0 (C-41). C-10 remains the universal fail floor: `s4_displacement_verdict` as a distinct labeled field in `evidence_summary` is the remaining open gap.
