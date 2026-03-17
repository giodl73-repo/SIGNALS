Written to `simulations/quest/rubrics/quest-score-rubric-v14-2026-03-15.md`.

---

**v14 changes from v13:**

4 new aspirational criteria extracted from R13 V-01 excellence:

| ID | Criterion | What it captures |
|----|-----------|-----------------|
| C-37 | Cascade-triggered C-33 activation includes explicit NOT-auto-PASS declaration | V-01's "C-31 is NOT auto-PASS" — a distinct third element beyond trigger + evaluation-consequence; without it, "active (C-07 fires; grouping must be evaluated)" satisfies C-33 but leaves scoping ambiguous |
| C-38 | Count-threshold C-33 activation names observed count alongside threshold | V-01's "N_variations = 5 ≥ 2" — names both the session value and the boundary, making activation independently auditable; "multiple variations" satisfies C-33 but is not falsifiable |
| C-39 | C-37 three-scale enumeration in diagnostic question | Closes the three-scale gap for C-37's PARTIAL boundary (evaluation consequence present but NOT-auto-PASS flag absent) |
| C-40 | C-38 three-scale enumeration in diagnostic question | Closes the three-scale gap for C-38's PARTIAL boundary (threshold only, or count only, but not both) |

**Cascade updates:**
- N_aspirational: 29 → 33 (each criterion: 10/33 ≈ 0.303 pt)
- C-03 design note: N_aspirational=33
- C-16 declaration list: 12 → 14 (add C-37, C-38; both cascade from C-33 per C-29)
- C-14 roster: 36-row → 40-row
- C-25 "Applied in this rubric": 11 → 13 entries (add C-39 for C-37, C-40 for C-38)
- C-36 example delta updated to reflect new weight: `−0.303 pt (FAIL × 10/33)`

**Cascade chain note:** C-37 and C-38 both auto-PASS when C-33 auto-PASS fires (which itself fires when C-07 does not fire). The C-16/C-29 declarations name C-33 as the triggering criterion, not the underlying data condition — this keeps the cascade graph visible at the declaration layer.
