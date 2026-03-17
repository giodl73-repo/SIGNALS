Written to `simulations/quest/rubrics/topic-plan-rubric-v10-2026-03-15.md`.

---

**Two new criteria extracted from Round 10:**

**C-36 — Named pre-schema rule block with rule-reference linkage at commitment checkpoints** (`enforcement`)

The discriminating signal: V-01 passes C-34 by embedding closed-enum constraints per-column inside the upfront schema — one annotation per column, encountered under context pressure. V-03 passes C-34 and adds a COLUMN CONTRACT block *before* the schema, numbering each rule; commitment checkpoints reference the rule by ID ("per Rule 1") rather than re-inlining the constraint. The gap: C-34 requires the constraint at both declaration sites, but does not specify that those constraints must be architecturally consolidated above the schema. A pre-schema rule block is encountered once before any schema column; per-column annotation is encountered under context pressure column-by-column. Rule-by-reference is auditable in one lookup; per-column re-embedding requires a full schema re-read to verify consistency.

**C-37 — Operationalized independence test procedure embedded in column definition with explicit pass/fail examples** (`depth`)

The discriminating signal: V-02 passes C-35 by naming the "row-key aliasing" anti-pattern with three fail examples and one pass example — a recognition scaffold applied post-hoc. V-03 passes C-35 and adds a decision-question test ("Can I fill this cell without reading the source document?") embedded in the column annotation as a named cell-level procedure with pass/fail examples. The gap: C-35 requires independent content; it is satisfied by recognition-based failure-mode naming. C-37 requires the independence requirement to be expressed as a prospective generation procedure the model applies before populating each cell — intercepting novel shortcuts that satisfy the anti-pattern label while violating its intent, rather than only repeating known failure modes.

**Updated totals:** 37 criteria, 235 pts. Formula: `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/29 × 145)`. Golden threshold bumped to 140.

**Phase 8 added to the arc:** *constraint architecture and test operationalization* — constraints promoted from per-column in-schema annotations into a named pre-schema rule block with numbered rules and rule-reference linkage; independence requirements expressed as cell-level decision-question procedures applied at generation time rather than recognition scaffolds applied at review time.
