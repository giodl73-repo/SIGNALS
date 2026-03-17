Written to `simulations/quest/golden/flow-resilience-variate-R7-2026-03-15.md`.

---

## Round 7 Variations — Summary

**Three new criteria entering R7**: C-25, C-26, C-27.

**Axes selected:**

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| **V-01** | Nil-Finding Supersession Protocol (C-25) | A typed nil ID without a lifecycle state is half-implemented. V-01 adds ACTIVE/SUPERSEDED states, supersession annotation citing the replacing finding ID, and a mandatory Nil Supersession Log. |
| **V-02** | Confidence Triage Resolution Sub-Gate (C-26) | R6 V-03 handled permanently-BARRED entries cleanly (CG registry). C-26 formalizes the inverse: when a BARRED entry's basis is resolved, `GATE 1b: RESOLVED` records the entry ID, satisfied basis, resolution mechanism, and new disposition. Without it, a promoted entry has no auditable path. |
| **V-03** | Named Rule Block Registry (C-27) | R6 V-03 rules satisfied C-24 (named conditionals) but scattered trigger restates across gate prose. C-27 requires a discrete `RULE REGISTRY` where all rules are declared once with unique IDs, gate sections cite `RULE-CR-DCV` by ID rather than restating conditions, and a Post-Analysis Registry Audit closes the rule lifecycle. |
| **V-04** | C-25 + C-26 combination | Nil lifecycle and BARRED promotion lifecycle are both "what happened to this artifact between declaration and now?" — V-04 tests they coexist without structural conflict. Adds a Gate 1b Promotion Audit after Gate 4. |
| **V-05** | C-25 + C-26 + C-27 + full R6 formalization | All three lifecycle closure mechanisms combined with scope brackets, typed nil identifiers, phased gate formalism, DS-primitive impossibility arguments, and coverage accountability roster. `RULE-NIL-SUPERSEDE` is added as a third registry rule to make nil lifecycle transitions as explicit as cross-section linkages. |

**Key structural novelties in R7 vs R6:**

- `RULE-NIL-SUPERSEDE` as a first-class registry rule (V-05) — nil transitions are now rule-governed, not ad-hoc protocol instructions
- `GATE 1b: RESOLVED` sub-gate (V-02, V-04, V-05) — BARRED-to-Include promotions have an auditable labeled record symmetric with the BARRED-to-CG path
- Nil Supersession Log (all variations) — explicit terminal record of nil lifecycle events; "no supersessions" is a required confirmation, not silence
- Post-Analysis Registry Audit (V-03, V-05) — the rule registry is closed at the end of analysis, confirming all linkages were declared before they were applied
