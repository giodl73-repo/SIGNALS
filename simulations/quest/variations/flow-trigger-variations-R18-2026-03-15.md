Written to `simulations/quest/golden/flow-trigger-variate-R18-2026-03-16.md`.

---

## flow-trigger R18 — V-01 through V-05 (Rubric v15, C-42 + C-43)

### New criteria targeted

| ID | What it requires | Key signal |
|----|-----------------|------------|
| **C-42** | Every NOTE assertion uses `[must be VALUE — inline rationale]` — rationale syntax-bound inside the bracket, not a separate line | Extending both brackets in the NOTE block |
| **C-43** | At least one NOTE assertion asserts a combined-system property (REMEDIATION SELF-SUFFICIENCY), not just element presence | Adding a third NOTE line that names the systemic guarantee explicitly |

### R17 gap analysis (retroactive against v15)

| Variation | C-42 | C-43 |
|-----------|------|------|
| V-01 R17 | FAIL — plain `[must be present]`, no inline rationale | FAIL — two element assertions, no systemic assertion |
| V-02 R17 | vacuous FAIL (C-40 not a full pass) | FAIL |
| V-03 R17 | FAIL — prose register NOTE, no brackets | FAIL |
| V-04 R17 | PARTIAL — two assertion lines, brackets plain | FAIL |
| V-05 R17 | **PASS** — both assertions extended | **PASS** — REMEDIATION SELF-SUFFICIENCY present |

### R18 ladder

| Variation | Axis | C-41 | C-42 | C-43 |
|-----------|------|------|------|------|
| V-01 | Role sequence | PASS | **FAIL** — plain brackets | **FAIL** — no systemic assertion |
| V-02 | Output format | FAIL vacuous | vacuous FAIL | FAIL |
| V-03 | Lifecycle emphasis | PASS | **PARTIAL** — first bracket extended, second plain | FAIL |
| V-04 | Inertia framing + phrasing register | PASS | **PASS** — all brackets extended | **FAIL** — systemic guarantee inferable but not asserted |
| V-05 | Phrasing register + extended bracket + systemic assertion | PASS | **PASS** | **PASS** |

### Key structural moves per variation

**V-01** NOTE block (C-42 FAIL path): two assertions with plain `[must be present]` — register is correct (C-41 PASS) but bracket ends at the constraint value with no `— rationale` clause.

**V-02** (vacuous path): CLOSURE CHECK is prose, no fence → C-40 not satisfied → C-41/C-42/C-43 all vacuous FAIL.

**V-03** NOTE block (C-42 PARTIAL): first line uses `[must be present — ARTIFACT MANIFEST names...]`, second line uses plain `[must be present]` — inconsistent extension, not a structural property.

**V-04** NOTE block (C-42 PASS, C-43 FAIL): both assertions use extended bracket form with inline rationale, but only two element-presence assertions — the systemic guarantee (removing either layer breaks self-sufficiency) is derivable but never stated as a named `REMEDIATION SELF-SUFFICIENCY: maintained [must be maintained — ...]` assertion.

**V-05** NOTE block (full pass): three assertions — DECLARATION TIME and DETECTION TIME with extended brackets, plus `REMEDIATION SELF-SUFFICIENCY: maintained [must be maintained — removing either attribution layer breaks self-sufficiency; removal is not a coverage reduction]` as the explicit systemic-property assertion.
