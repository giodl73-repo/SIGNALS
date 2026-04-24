Written to `simulations/quest/golden/mock-review-variate-R8-2026-03-15.md`.

---

**Summary of R8 variations:**

| Var | Axis | New criteria targeted | Role order | C-26 | C-27 |
|-----|------|-----------------------|------------|------|------|
| V-01 | role-sequence | C-26 | Architect → Strategy → PM | PASS predicted | FAIL |
| V-02 | output-format | C-27 | Strategy → PM → Architect | FAIL | PASS predicted |
| V-03 | phrasing-register | C-27 (alt mechanism) | Strategy → PM → Architect | FAIL | PASS predicted (distributed fields) |
| V-04 | role-sequence + lifecycle-emphasis | C-26 + C-18 deepened | Architect → Strategy → PM | PASS predicted | FAIL |
| V-05 | role-sequence + output-format + lifecycle-emphasis | C-26 + C-27 + all prior | Architect → Strategy → PM | PASS predicted | PASS predicted |

**Key design decisions:**

**C-26** requires Architect before PM. V-01/V-04/V-05 use **Architect → Strategy → PM** ordering. This preserves C-23 (Strategy SQ-1 available before STEP 6 decisions) while enabling the cross-step guard that fires on `architect-verdict = CONTRADICTS-ARCHITECTURE` and suppresses PM for those namespaces.

**C-27** is tested via two different mechanisms: V-02 uses a co-located **FORBIDDEN OUTPUTS TRIAD** block (one-scan completeness), V-03 uses **per-rule `forbidden-output:` field notation** (distributed but labeled, mirroring the `trigger =` convention). The comparison will show whether co-location or field-label structure is the load-bearing property for C-27.

**V-05 ceiling** combines both: per-rule `forbidden-output:` fields (C-11 + C-27 field axis) + co-located TRIAD (C-27 enumerable set) + Architect-first with cross-step guard (C-26) + all R7 V-05 criteria.
