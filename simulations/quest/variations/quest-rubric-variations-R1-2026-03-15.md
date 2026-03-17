Written to `simulations/quest/golden/quest-rubric-variate-R1-2026-03-15.md`.

---

## Round 1 Variation Map

| V | Axis | C-03 probe | C-07 probe | Notes |
|---|------|-----------|-----------|-------|
| V-01 | Role sequence | Strong — AUDITOR gate rejects vague pass conditions before DEFINER emits | Moderate — ANALYST names behaviors but no foil contrast | Three-role sequence: ANALYST → AUDITOR (two-scorer test) → DEFINER |
| V-02 | Output format | Moderate — prose blocks give pass conditions unlimited space | Weak — format does not constrain specificity | Per-criterion blocks; no hard specificity gate |
| V-03 | Lifecycle emphasis | Moderate — failure-mode anchors pass conditions | Strong — Phase 1 forces named failures before criteria | Failure-first phases; criteria derived from failures |
| V-04 | Phrasing register | Strong — DO NOT prohibitions on hedging words are binary | Moderate — specificity rule present but not derived | Fully imperative; two-scorer test as an explicit hard gate |
| V-05 | Inertia framing + lifecycle emphasis | Strong — foil failure 2 (vague pass conditions) forces contrast | Strong — foil failure 1 (generic presence checks) forces naming specific values/counts | 5-item STATUS QUO RUBRIC foil + Phase 1 contrast analysis |

---

**Key design choices:**

- **V-01** is the pure mechanism test: does a formal AUDITOR review step produce measurably sharper pass conditions than single-pass writing? If C-03 improves but C-07 does not, role sequence is a C-03 tool only.
- **V-02** isolates whether table-cell compression is causal for C-03 failures. If prose blocks don't improve pass condition quality, the cause is upstream (not knowing what to specify).
- **V-03** and **V-05** both target C-07. V-03 uses failure-first phases alone; V-05 adds the named competitor. If V-05 outperforms V-03 on C-07, the foil's named failure modes are doing the work, not just the lifecycle structure.
- **V-04** is the ablation test for prohibitive language. If it produces C-03 passes that V-01 misses, the mechanism is the prohibition form, not the review role.
- **V-05** is the combined ceiling attempt. If it outperforms all single-axis variations jointly on C-03 + C-07, it becomes the base for R2.
