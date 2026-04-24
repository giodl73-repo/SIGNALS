Scorecard written to `simulations/quest/scorecards/trace-deployment-scorecard-R20-2026-03-15.md`.

---

## Round 20 Results

| Rank | Variation | Score | Predicted | Delta |
|------|-----------|-------|-----------|-------|
| 1 | V-01 Role sequence (Operations-first) | **205/260** | 205 | 0 |
| 2 | V-05 Combined (role + lifecycle + inertia) | **200/260** | ~210 | −10 |
| 3 | V-04 Role sequence + inertia | **195/260** | ~210 | −15 |
| 4 | V-02 Output format (table + formal headers) | **165/260** | ~190 | −25 |
| 5 | V-03 Phrasing register (DIRECTIVE, no skeleton) | **160/260** | ~160 | 0 |

**All five are GOLDEN** (all essential pass, composite ≥ 80).

---

### Key findings

**V-01 hit the R20 target exactly (205/260).** C-41 confirmed: pair notation `(Commerce / PRE-DEPLOY)` on all four Stage 2 sub-questions passes cleanly. C-42 confirmed on V-03: two-stage-only path ceiling is 160/260.

**The ~210 ceiling was not achieved.** Both V-04 and V-05 missed it:

- **V-04 (−15)**: Declarative disqualifier placed in the Stage 1 *general instructions*, not inside the `**what needs to be true...?**` phase section body. C-31 requires both disqualifiers in distinct phase sections — general-instructions placement fails. Fix: move that one sentence into the PRE-DEPLOY section.

- **V-05 (−10)**: Per-phase `*Phase vocabulary*:` lists push each phase past single-paragraph density, killing C-32. V-01 avoids this by keeping vocabulary in the role block.

**V-02 prediction was optimistic by 25 pts**: The ~190 prediction assumed V-02 would inherit C-12/C-15/C-30/C-31/C-32 from the prose structural-adoption base (205 − 15 for formal headers = 190). The prompt doesn't include a current-practice baseline or question-form disqualifier — those five criteria were simply not written in.

---

### New patterns (C-43 candidates)

1. **`stage-2-primary-domain-quality-review`** — V-05's sub-questions 2a–2d direct Stage 2 to audit Stage 1's *own* domain quality (unbounded thresholds, underspecified dependencies, missing numeric triggers, unverified rollback states). Distinct from C-40's cross-domain gap-filling; captures intra-domain quality defects.

2. **`declarative-disqualifier-phase-section-placement`** — The declarative disqualifier must be inside a phase section boundary (not in general instructions) for C-31 to activate. V-04 demonstrates the 10-pt cost of getting this wrong.

```json
{"top_score": 205, "all_essential_pass": true, "new_patterns": ["stage-2-primary-domain-quality-review: Stage 2 sub-questions that critique Stage 1's own domain quality (unbounded thresholds, underspecified ordering dependencies, missing numeric trigger conditions, unverified rollback states) — intra-domain quality review, distinct from C-40 cross-domain gap-filling", "declarative-disqualifier-phase-section-placement: placing the declarative disqualifier explicitly within the PRE-DEPLOY phase section body (not in general instructions before the phase sections) is load-bearing for C-31 and C-32; V-04 demonstrates the 10-point cost of general-instructions placement"]}
```
