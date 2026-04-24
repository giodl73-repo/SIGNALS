Written to `simulations/quest/golden/corps-rob-variate-R12-2026-03-17.md`.

---

**R12 summary: 5 variations targeting the two universal v12 gaps**

| Variation | Axis | New v12 criteria | Expected score |
|-----------|------|-----------------|----------------|
| V-01 | C-40 Glossary Exclusivity Declaration (single axis) | C-40 PASS | 245/250 |
| V-02 | C-35 RULE AUDIT-TABLE Additive Constraint (single axis) | C-35 PASS | 245/250 |
| V-03 | RULE IB-URGENCY-CASCADE as named glossary rule (single axis) | C-39 hardened | ~225 |
| V-04 | V-01 + V-02 combined, base = R11 V-05 | C-35 + C-40 PASS | **250/250** |
| V-05 | V-01 + V-02 + V-03, base = R11 V-05 | C-35 + C-40 + C-39 named | **250/250** |

**Key structural additions vs R11 best (V-05 at 240):**

- **C-40** (V-01, V-04, V-05): Glossary preamble gets one explicit sentence -- the glossary is the exclusive named-rule locus; inline declarations don't satisfy named-rule criteria.
- **C-35** (V-02, V-04, V-05): RULE AUDIT-TABLE gets the additive constraint -- table inserted above AUDIT RESULT block, not replacing it; C-29 per-condition enumeration mandatory beneath.
- **C-39 hardening** (V-03, V-05): RULE IB-URGENCY-CASCADE added as a first-class glossary rule with explicit trigger (Urgency Gradient = HIGH) and three mandatory cascade targets (Go/No-Go citation, Risk Register delay-compounding entry, Inertia Pressure Summary compounding path).

V-04 and V-05 are both 250/250 candidates via different C-39 mechanisms -- V-04 via inline instruction (R11 V-05 path), V-05 via named rule. This makes R12 a diagnostic for whether C-39 requires the named-rule path or whether the inline path suffices.
