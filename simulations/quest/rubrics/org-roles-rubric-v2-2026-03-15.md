Done. Here is the complete updated rubric:

---

```markdown
---
skill: quest-rubric
skill_target: org-roles
date: 2026-03-16
version: 2
supersedes: org-roles-rubric-v1-2026-03-15.md
---

# Scoring Rubric: org-roles (v2)
```

**What changed from v1:**

| Delta | Detail |
|-------|--------|
| +C-11 | **Context-first derivation ordering** (from E-1) — step sequence must derive domain experts before stock roles are loaded; FAIL if stock roles appear before domain expert derivation |
| +C-12 | **Failure-mode-named field constraints** (from E-2) — schema field instructions must name the exact failure mode to avoid, not just the positive requirement; FAIL if all instructions are phrased purely positively |
| +C-13 | **Explicit step output format** (from E-3) — every step that names an output must define its format fields and required content; heading-only stubs are a structural omission, not a documentation gap |
| C-10 | Tightened pass condition — now requires all five fields explicitly (area, count, stock names, domain expert names + derivation source, gaps); strengthened FAIL language to distinguish heading-stub failure (C-13 cause) from missing content (C-10 effect) |
| Formula | Aspirational denominator updated `/ 2` → `/ 5` to account for five aspirational criteria |
| Notes | Added evaluator guidance for C-01/C-07 naming risk, C-10 vs C-13 relationship, C-11 ordering evaluation method, C-12 negative-construction test |

**Scoring formula impact on Round 1 score:**

```
v1: (5/5 * 60) + (2.5/3 * 30) + (0.5/2 * 10)  = 87.5
v2: (5/5 * 60) + (2.5/3 * 30) + (0.5/5 * 10)  = 86.0
```

V-01 drops slightly (86.0 vs 87.5) because the aspirational pool is larger — same partial credit, lower denominator weight. Still GOLDEN.
