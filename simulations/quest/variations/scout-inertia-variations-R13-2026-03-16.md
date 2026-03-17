File written to `simulations/quest/golden/scout-inertia-variate-R13-2026-03-17.md`.

---

## scout-inertia -- Quest Variate R13

**Rubric**: v13 (ceiling 210) | **Target**: First 210/210

---

### Variation Summary

| Variation | Axis | Key Hypothesis |
|-----------|------|---------------|
| **V-01** | Inertia framing | Blockquote-wrapped `> [C-0N COMMAND]:` satisfies A-29+A-30; A-31 via minimal `[FAIL-FIRST RULE]` without criterion ID |
| **V-02** | Lifecycle emphasis | Stage-based; A-31 via `FAIL-FIRST CONSTRAINT [A-31]` (bracket-suffix with criterion ID) — extends A-23 to FAIL-FIRST layer |
| **V-03** | Phrasing register (reference) | R12 V-03 scaffold carried forward unchanged; 210/210 baseline |
| **V-04** | Output format (consolidated bridge) | A-31 via `[A-31 FAIL-FIRST ORDERING RULE]` (bracket-prefix with criterion ID) — extends A-23 via bracket-prefix |
| **V-05** | All axes combined | A-31 via `DEFAULT COMPETITOR FAIL-FIRST RULE [A-31]` — domain-prefix pattern extends to FAIL-FIRST rule layer |

---

### R13 Design Logic

**Three new criteria, three distinct structural layers:**

**A-29** (criterion ID in authoring prompt label): All R12 V-01/V-02/V-04 used `> **C-0N question**:` — criterion ID present but register is "question". R13 upgrades all five to `[C-0N COMMAND]:` form, completing the traceability chain at the authoring-prompt layer.

**A-30** (COMMAND keyword in prompt label): Requires "COMMAND" as a structural element in the bracket-label. V-01 is the stress test: does blockquote-wrapping (`> [C-0N COMMAND]:`) preserve A-30, or does the criterion require bare inline form? V-02–V-05 use inline form.

**A-31** (named structural rule in FAIL-FIRST body): R12 V-03 already had `[FAIL-FIRST RULE]` (minimal, no criterion ID). R13 explores four label forms:
- **Minimal** (V-01, V-03): `[FAIL-FIRST RULE]` — satisfies A-31 alone
- **Bracket-suffix** (V-02): `FAIL-FIRST CONSTRAINT [A-31]` — also extends A-23
- **Bracket-prefix** (V-04): `[A-31 FAIL-FIRST ORDERING RULE]` — also extends A-23
- **Domain-prefix** (V-05): `DEFAULT COMPETITOR FAIL-FIRST RULE [A-31]` — extends the domain-prefix A-23 pattern to the FAIL-FIRST layer

The key A-31 + A-23 question: when the FAIL-FIRST rule label carries the A-31 criterion ID, does A-23's criterion-ID-in-label requirement extend to cover it? V-02, V-04, and V-05 test this simultaneously across all three A-23 label form families.
