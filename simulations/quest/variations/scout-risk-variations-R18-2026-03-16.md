`simulations/quest/golden/scout-risk-variate-R18-2026-03-17.md` written. Here's the summary of what changed:

---

## R17 → R18: Three new exploration axes

**Baseline state (R17 V-05 on v17 rubric): 180/180** — first round where baseline already satisfies all criteria. R18 is purely exploratory.

### V-01 — Single axis: C-51 sentence ordering reversal (negative isolation)
Reverses Phase 0c closing from `"This taxonomy is closed. No violation category..."` to `"No violation category... This taxonomy is closed."` Both sentences present and syntactically independent. Tests whether C-51 enforces canonical order (closure-first, prohibition-second). If C-51 requires ordering: V-01 scores 178/180 (PARTIAL) and provides evidence for a v18 C-54 criterion. All other structure identical to R17 V-05.

### V-02 — Single axis: C-52 bi-directional parity
Phase 0 gains a symmetric opening sentence: `"This block is a pre-phase reference block of equal structural weight to Phase 0c — both declare a closed vocabulary before any generation phase executes."` Currently only Phase 0c points to Phase 0; V-02 makes parity verifiable from either block in isolation. Pattern for potential v18 C-55.

### V-03 — Single axis: C-53 count-bounded citation
Phase 0c replaces `"Every prohibition site in this prompt cites this block by its full name"` with `"Five prohibition sites in this prompt cite this block by its full name"`. Converts an unbounded universal assertion to a countable claim — a reviewer can falsify it by finding ≠5 citations. Pattern for potential v18 C-56.

### V-04 — Combination: V-02 + V-03
Bi-directional parity in Phase 0 + count-bounded citation in Phase 0c. Tests whether the two properties reinforce each other structurally.

### V-05 — Full combination: V-02 + V-03 + explicit sentence order rule
Adds a canonical ordering declaration inside Phase 0c: names each sentence by role (`"The state sentence comes first... The use-site constraint sentence comes second... Reversing this order is a schema violation"`), then delivers the two closure sentences in declared order. Makes implicit convention explicit. This is the maximum-auditability form and the likely v18 baseline source.

---

## Score predictions on v17 rubric

| Variation | C-51 | C-52 | C-53 | v17 Score | Delta |
|-----------|------|------|------|-----------|-------|
| Baseline (R17 V-05) | PASS | PASS | PASS | 180/180 | — |
| V-01 | PARTIAL | PASS | PASS | 178/180 | -2 |
| V-02 | PASS | PASS | PASS | 180/180 | 0 |
| V-03 | PASS | PASS | PASS | 180/180 | 0 |
| V-04 | PASS | PASS | PASS | 180/180 | 0 |
| V-05 | PASS | PASS | PASS | 180/180 | 0 |
