---

# program:plan — Round 11 Score Report

**Rubric**: v11 · 30 aspirational · max 240 pts · golden >= 80

---

## Per-variation scores

| Variation | Essential | Recommended | Aspirational | Composite | Golden |
|-----------|-----------|-------------|--------------|-----------|--------|
| **V-01** (C-36 axis) | 60/60 | 30/30 | 130/150 | **220/240** | YES |
| **V-02** (C-37 axis) | 60/60 | 30/30 | 130/150 | **220/240** | YES |
| **V-03** (C-37 variant, est.) | 60/60 | 30/30 | ~130/150 | **~220/240** | YES |
| **V-04** (C-36+C-37 combo) | 60/60 | 30/30 | 140/150 | **230/240** | YES |
| **V-05** (golden synthesis) | 60/60 | 30/30 | 140/150 | **230/240** | YES |

---

## Key criterion outcomes

**V-01 vs V-04 delta (−10):** V-01 uses essential-only correction table → C-29 FAIL → C-35 FAIL. V-04 adds recommended-tier rows to the correction table alongside C-34, closing both.

**V-02 vs V-04 delta (−10):** V-02 has no `Why:` at gate_fail: → C-25 FAIL → C-34 FAIL. V-04 preserves C-34 from R10 V-05 alongside C-35, closing both.

**Ceiling (230/240):** Three persistent deductions apply to all variates:
- C-08 FAIL (−5): no quantified gate thresholds
- C-13 PARTIAL (−2.5): arc in YAML zone comments, not document-level section headers
- C-14 PARTIAL (−2.5): echo has a position label but no explicit `# REQUIRED: DO NOT REMOVE` annotation

**C-36 and C-37 status:** Both new v11 criteria were already latent in R10 V-05 (accurate header + name: field annotations present). R11 makes them explicit and ensures they survive variate construction. Neither criterion conflicts with any prior mechanism.

---

## Excellence signals from V-04 / V-05

1. **C-34 and C-29 are structurally orthogonal** — compound `gate_fail:` annotation lives in the YAML template; recommended-tier correction table rows live in the correction table. Adding both creates no structural conflict.
2. **C-35 is the conjunction criterion** — it passes automatically when C-31 and C-29 both pass; no extra design work needed beyond those two.
3. **C-36 is a free addition to any C-31-passing prompt** — changing one header label earns it without restructuring anything.
4. **C-37 was already implicit in R10 V-05** — the pattern (# WRONG C-06 at name: fields) was already present; v11 makes it an explicit requirement with a displacement anti-pattern teaching block.

---

```json
{"top_score": 230, "all_essential_pass": true, "new_patterns": ["C-34 compound gate_fail: annotation and C-29 recommended-tier correction table rows are structurally orthogonal — combining both earns C-35 without any mechanism conflict", "C-36 header label accuracy is a free addition to any C-31-passing prompt — changing the BAD PLAN header from essential-only scope to full-coverage scope earns C-36 without restructuring", "C-37 field-level C-06 annotation was already latent in R10 V-05 — the v11 discipline makes explicit what was implicit: the co-location rule from C-26 (criterion tag at structural gate_fail:) applies equally to name: field violations in the BAD PLAN"]}
```
