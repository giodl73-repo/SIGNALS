Written to `simulations/quest/rubrics/topic-plan-rubric-v6-2026-03-15.md`.

---

**Four new criteria extracted from Round 5 excellence signals:**

| ID | Name | Layer | Source signal |
|----|------|-------|---------------|
| C-24 | Unstated-assumption extraction at strategy read step | depth | V-05 Step 1 "What it assumed without naming" row |
| C-25 | Inertia cost column in proposals: "If unchanged" | depth | V-05 Step 6 "If unchanged" column naming cost of deferral |
| C-26 | Schema-first priming before file reading | enforcement | V-04's complete output schema declared before Step 1 |
| C-27 | Cascade schema-commitment checkpoints at proposals and diff | enforcement | V-02's 3 independent auditable checkpoints vs C-22's single delta checkpoint |

**Updated totals:** 27 criteria, 185 pts max. Formula: `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/19 × 95)`

**The v6 meta-pattern splits in two directions from v5's enforcement foundation:**
- C-24/C-25 are *depth* criteria — a structurally correct output can still fill columns mechanically; these require an additional dimension of causal reasoning (surface what strategy hid, name the cost of inaction).
- C-26/C-27 are *enforcement* criteria — extending C-21's adjacency declarations to upfront priming (before any reading), and extending C-22's single checkpoint to a three-point cascade.
