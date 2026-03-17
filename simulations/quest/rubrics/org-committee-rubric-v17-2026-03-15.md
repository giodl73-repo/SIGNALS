Written to `simulations/quest/rubrics/org-committee-rubric-v17-2026-03-16.md`.

---

**What changed v16 → v17**

**C-42 — INVARIANT seal fill rules carry bilateral VALIDATE examples** *(new)*

Signal: V-01's C-40 evidence shows `fill rule: PRINT: INERTIA INVARIANT... with bilateral VALIDATE`. C-40 requires the seal declaration to exist; C-30 requires its fill rule to be imperative. Neither requires bilateral VALIDATE coverage for that fill rule. C-36 covers manifest entry format, `CITE:`, `RESPONDS-TO:`, and stance form; C-39 extends to the committee-type declaration checkpoint. The INVARIANT seal slot is the one remaining output-producing skeleton slot with an imperative fill rule but no correctness test. C-42 closes that gap: without it, the seal declaration can be filled with a phase-commit reference omitted or a modification prohibition missing without violating any written rule.

**C-43 — Bidirectionality constraint clauses are pre-declared as skeleton placeholders and enforced by dedicated fill rules** *(new)*

Signal: V-01's C-41 evidence shows `both pre-declared in skeleton and enforced in fill rules`. C-41 requires the clause to appear in each commit block; C-28 requires the commit block to be pre-declared. Neither requires the clause *within* the commit block to be its own labeled placeholder with a dedicated fill rule. The bidirectionality clause is the most recently added required commit-block element (v16), making it the element most likely to be omitted under output pressure. C-43 applies C-28's architectural guarantee to the clause itself: pre-declared placeholder cannot be forgotten; fill-time discipline can.

**Scoring**: aspirational pool 33 → 35; aspirational max 66 → 70; composite max **156 → 160**.
