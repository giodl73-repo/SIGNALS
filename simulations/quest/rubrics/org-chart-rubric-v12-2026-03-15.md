Written to `simulations/quest/rubrics/org-chart-rubric-v12-2026-03-16.md`.

---

**What changed in v12:**

**Two new aspirational criteria extracted from R11:**

| ID | Source | Behavior |
|----|--------|----------|
| C-31 | V-02/R11 | Phase transition gates use positional emit-then-block directives: `=== [PHASE GATE: ...] ===` markers at macro document boundaries (role loading → inertia → org diagram → headcount → rhythm), each with "DO emit / DO NOT proceed" form and purely positional text. Parallels C-22/C-23 at document scope vs. inertia-sub-section scope. Dep: C-28. |
| C-32 | V-03/R11 | Format specifications are directive-embedded; no code-fenced template scaffolding. All format requirements (separator syntax, annotation format, table column names, vocabulary lists) expressed as inline backtick format strings within imperative directive sentences. V-03/R11 proved template scaffolding is non-load-bearing for all 22 prior criteria. Dep: C-25. |

**Denominator:** `/22` → `/24` (≈ 0.417 pts per criterion)

**Prior round rescaling (denominator only):**
- R9 leading variations (20/22): → **98.3** (20/24)
- R10 best (21/22): → **98.8** (21/24)
- R8 V-02 ceiling (19/22): → **97.9** (19/24)

**R11 scores:** V-01 earns neither C-31 nor C-32 → **99.2** (22/24). V-02 earns C-31, fails C-32 → **99.6** (23/24). V-03 earns C-32, fails C-31 → **99.6** (23/24). R11 ceiling: 99.6. First 24/24 requires combining both.
