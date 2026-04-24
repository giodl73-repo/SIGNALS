Written to `simulations/quest/golden/file-issue-variate-R7-2026-03-17.md`.

---

## file-issue -- Round 7 Variations

**Rubric**: v6 | **Scoring target**: 12/12 = 100.00

**R6 context**: Three implementations confirmed at 100.00 (V-03 "determines both" + C-18 + C-19, V-04 inertia framing, V-05 minimal patch). All three R6 open questions answered. No new criteria.

---

### Round 7 open questions and variation axes

| Variation | Axis | Key question |
|-----------|------|--------------|
| **V-01** | C-19 only accumulation (C-18 intentionally absent) | Is C-19 alone (no C-18) sufficient for C-17 with "determines both"? Or do C-18 + C-19 jointly constitute the accumulation path? |
| **V-02** | Alternative blocking imperative: "PHASE B IS LOCKED. Begin only after..." | Does C-15 require the exact "DO NOT BEGIN PHASE B" form, or is any strong blocking directive sufficient? |
| **V-03** | Dispatch manifest table in A1 (4-row table: severity → schema + template) | Can table-based dispatch satisfy C-17, C-18, and C-19 through structured notation? |
| **V-04** | Completion condition as verification table (4-row gate table with Check/Required State/Gate columns) | Does table-form completion condition satisfy C-16 and C-18, or is prose form load-bearing? |
| **V-05** | Maximum compression (shortest prompt that preserves 12/12) | What is the minimum token expression for 100.00? Which prose elements are structural anchors vs. expendable elaboration? |

### Predicted scores

| | Aspirational | Composite | Critical test |
|---|---|---|---|
| V-01 | 10/12 (C-17 FAIL, C-18 FAIL) | **98.33** | C-17 symmetry: C-19 alone fails C-17 just as C-18 alone did (R6 V-02) |
| V-02 | 12/12 | **100.00** | "PHASE B IS LOCKED" satisfies C-15 -- imperative form is not load-bearing |
| V-03 | 11-12/12 | **99.17 or 100.00** | Whether "manifest row" provenance satisfies C-19's origin-in-heading requirement |
| V-04 | 12/12 | **100.00** | Table form for completion condition is valid for C-16 and C-18 |
| V-05 | 12/12 | **100.00** | Structural anchors (blocking, completion condition, provenance headings, dispatch declaration) survive prose compression |

The most information-dense test is **V-01**: if C-17 fails (predicted), it confirms that C-18 and C-19 are jointly required for the structural accumulation path -- neither site alone is sufficient when A1 uses "determines both." This closes the symmetry question left open after R6.
