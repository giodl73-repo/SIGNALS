Written to `simulations/quest/golden/quest-score-variate-R9-2026-03-16.md`.

---

## Round 9 Variations -- Summary

**Context**: R8 champion was V-05 (P+Q+R+U+V) at 99.6875, `"new_patterns": []`. R9 is the convergence confirmation round.

**Three variation axes:**

| Code | Axis | Target | Mechanism |
|------|------|--------|-----------|
| X | Prior-Round Input Gate | C-09 | Phase 0 added before Phase 1: conditionally builds PRIOR-ROUND REGISTER when prior-round scorecard provided; explicitly applies N/A rule when not. Enables C-09 PASS when data available. |
| Y | Composite Pre-Derivation Block | C-04, C-10 stability | Section 1e added: pre-derives formula range (max composite, Golden threshold math) from v8 parameters before any verdict row is written. Forces /16 engagement before scoring. |
| Z | Phrasing Register | stability | PHASE/SECTION labels -> numbered checklist steps. All Inertia labels, table schemas, and enforcement rules preserved verbatim. Tests whether any rubric criterion has latent PHASE-label format dependency. |

**Predicted scores** (no prior-round data in scoring run):

| Variation | Axes | Predicted composite |
|-----------|------|---------------------|
| V-01 | X only | 96.875 |
| V-02 | Y only | 96.875 |
| V-03 | Z only | 96.875 (stability: any deviation is a finding) |
| V-04 | P+Q+R+U+V+X | 99.6875 (X non-additive without prior data) |
| V-05 | P+Q+R+U+V | 99.6875 (R8 champion, convergence confirmation) |

**Key diagnostic**: If V-01/V-02/V-03 all score identically and V-04 ties V-05, R9 finds no new patterns -- dual convergence achieved. V-04's advance over V-05 is capability (can achieve C-09 PASS when called with prior data), not composite in this run.
