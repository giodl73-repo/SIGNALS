Written to `simulations/quest/golden/scout-size-variate-R12-2026-03-17.md`.

---

# Scout-Size Prompt Variations — R12

**Rubric**: v12 (25 aspirational criteria) | **New in v12**: C-32 + C-33

---

## Variation Axes

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| **V-01** | Output format (pre-slot examples throughout + C-32 standalone gap + C-33 failure-class label) | Mechanical upgrade of R11 V-01: remove gap from compilation table (C-32), add "you have written a basis-negation" to self-test (C-33). Achieves C-19 + C-32 + C-33 simultaneously in single-phase without structural overhead. |
| **V-02** | Lifecycle emphasis (DIAGNOSIS: block elevates failure-class label to structural event) | R11 V-02's "basis-negation" was an inline clause. V-02 promotes it to a dedicated `DIAGNOSIS:` sub-block — a document-structure-level event the model encounters before producing the gap field. Hypothesis: labeled DIAGNOSIS primes the failure class more reliably than an inline conditional. |
| **V-03** | Phrasing register (second-person imperative; C-33 failure class in direct-address register: "you are in a basis-negation pattern") | Shifts from first-person self-assessment ("I have written a basis-negation") to second-person detection ("you are in a basis-negation pattern"). Tests whether addressed-voice register changes how the model engages with the constraint at generation time. |
| **V-04** | Role sequence + lifecycle emphasis (two-phase; Phase 2 owns standalone gap section as its primary output; C-33 in Phase 2 charter as named charter violation) | Gains C-20/C-23/C-24/C-25/C-26/C-27/C-29 through role separation. Phase 2's primary production IS the standalone gap section (C-32). Charter self-test labels basis-negation as a "Phase 2 charter violation" (C-33). Role-tagged compilation table achieves C-26. |
| **V-05** | Inertia framing + output format + role sequence (three-phase; Phase 0 inertia gate with explicit CLOSED/OPEN status; C-32 + C-33 in Phase 2; role-tagged column headers throughout) | Inertia becomes a mandatory gate — Phase 1 cannot begin until Phase 0 CLOSED. Three-phase ownership: Phase 0 = Inertia Assessor, Phase 1 = Sizing Analyst, Phase 2 = Risk Assessor. Role-tagged column headers achieve C-26 structurally. C-32 and C-33 embedded in Phase 2. Tests whether phase-gate semantics amplify enforcement guarantees or introduce overhead. |

---

## C-32 Compliance (all five variations)

All five variations satisfy C-32 by design:
- The confidence gap appears in a named standalone section `── CONFIDENCE GAP CHECKPOINT ──`
- It is **not** a row or cell in the output compilation table (compilation table footnotes reference the section)
- It is positioned **after** the confidence basis section and **before** the sensitivity section in all variations

## C-33 Compliance per variation

| Variation | Self-test affirmative branch |
|-----------|------------------------------|
| V-01 | "If yes: **you have written a basis-negation.**" |
| V-02 | "If yes → **DIAGNOSIS: basis-negation detected.**" |
| V-03 | "If yes: **you are in a basis-negation pattern.**" |
| V-04 | "If yes: **you have written a basis-negation — a Phase 2 charter violation.**" |
| V-05 | "If yes: **you have written a basis-negation.** You are in a basis-negation pattern." |

The key structural difference from R11: V-01–V-03 are single-phase designs that formally satisfy both new criteria without role-separation cost. V-04–V-05 trade single-phase simplicity for the full role-separation cluster, with C-32 + C-33 embedded in Phase 2's charter and standalone output.
