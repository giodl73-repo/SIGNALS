Written to `simulations/quest/rubrics/quest-variate-rubric-v14-2026-03-15.md`.

---

**Changes from v13 → v14:**

**One new criterion — C-38: Type-stratified checkpoint failure routing**

The R14/V-01 checkpoint failure section has two distinct labeled routing blocks keyed on failure type:
1. Variation-level failures → `"STOP AND REWRITE THIS VARIATION BODY. Do not note the failure and continue."`
2. Set-level predicate failures → `"DO NOT attempt to resolve this failure by rewriting the variation body."`

Plus the resolution-path blockade pre-installed in the preamble as a role-constitutive duty: `"When a set-level predicate fails... body rewrite is not a valid resolution path."` V-02 cleanly ablated this by unifying to a single branch (satisfying C-23 but not C-38), confirming independence.

**Design decision chain:** C-21 (what to check) → C-23 (failure branch uses hard-stop imperative) → **C-38** (failure branch is type-stratified with a dedicated resolution-path blockade for set-level failures, with preamble pre-installation).

**Denominator: 30 → 31.**

**R14 tier structure under v14:**

| Rank | Variation | Score | Failures |
|------|-----------|-------|----------|
| 1 | V-01 full stack | 100.00 | — |
| 2 | V-02 (C-38 ablation) | 99.68 | C-38 |
| 2 | V-03 (C-37 ablation) | 99.68 | C-37 |
| 2 | V-04 (C-36 ablation) | 99.68 | C-36 |
| 5 | V-05 (C-38+C-37 combo) | 99.35 | C-38, C-37 |

Three-way symmetry at Rank 2 — all three of C-38 (checkpoint routing), C-37 (Phase 2 STOP destination), C-36 (Phase 3 STOP artifact-name) are confirmed, independent, and equidistant from perfect. No R14→R15 candidate identified.
