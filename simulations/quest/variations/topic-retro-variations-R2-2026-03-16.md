Written to `simulations/quest/golden/topic-retro-variate-R2-2026-03-16.md`.

---

## R2 Variations — topic-retro

All five variations embed C-11 (explicit numeric formula) and C-12 (Echo before accuracy) structurally. Single-axis variations first:

**V-01 — Phrasing Register: Imperative/Technical**
Each phase is a command with an explicit pass/fail output condition. Formula appears as "Required output" in Phase E. Echo is Phase A with a `LOCK PHASE A` gate. Hypothesis: imperative language with checkable artifacts eliminates stylistic shortcuts.

**V-02 — Output Format: Pure Table-Driven**
All output is tables. Table 1 is the Echo table; Table 4 is accuracy. Per-namespace score is a column header — it can't be dropped without breaking table structure. C-12 is enforced purely by document position. Hypothesis: table format makes required fields physically undropable.

**V-03 — Lifecycle Emphasis: Strict Phase Gates**
Five phases with `>> COMMIT` gates and explicit revision prohibitions at each boundary. The Echo-commit gate (after Phase 2, before Phase 3) is the hardest C-12 constraint in the set — it prohibits revision even if Phase 3 would change the finding. Hypothesis: gate language produces higher compliance than structural position alone.

**V-04 — Role Sequence + Lifecycle (Three-Voice Protocol)**
Three named roles with handoff contracts: Archivist (inventory only), Echo Finder (surprise only), Scorer (accuracy + verdict). Scorer cannot revise Echo Record. Formula is Scorer's only permitted accuracy method. Hypothesis: role-as-persona framing sustains the constraints differently than phase-as-step framing.

**V-05 — Inertia Framing + Formula + Echo-First**
Every section anchored to "would this have changed the commit decision?" Echo must be named before the commit frame is assessed (Section 0 before Section 2). Commit-confidence framing motivates formula-based accuracy. Adds Inertia check column to gaps and coverage tiers to inventory. Hypothesis: decision-impact anchor is a sufficient natural generator for C-11 and C-12 without needing explicit gates.

---

**Key design choice across all five:** The formula `(Correct*100 + Partial*50) / (Correct+Partial+Wrong)` is stated inline in the accuracy section of every variation — not in a preamble, not implied. R1 showed that prose verdict sections consistently drop per-namespace differentiation when the formula isn't structurally required at the point of output.
