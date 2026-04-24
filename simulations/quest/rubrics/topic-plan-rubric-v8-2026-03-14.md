Written to `simulations/quest/rubrics/topic-plan-rubric-v8-2026-03-15.md`.

---

**What changed from v7:**

**C-32 — Reversibility taxonomy column** (`depth`)
Extends C-25 + C-31. The "If unchanged" column names what degrades; C-31 makes it a decision gate. C-32 adds the missing temporal dimension: three enumerated values — *Reversible at same cost / Gets harder / Becomes impossible* — that classify how fast the deferral window closes, not just what closes. Prose like "it will be harder later" satisfies neither value 2 nor value 3 without committing to whether the window is a ratchet or a hard stop.

**C-33 — Full assumption table schema in the upfront output schema block** (`enforcement`)
Extends C-26 + C-30. C-26 puts the proposal/diff schemas upfront before Step 1; C-30 requires all five assumption table columns at the assumption step. C-33 closes the gap: the complete five-column assumption table schema must appear in the same pre-reading schema block as the other tables. A C-30 pass that declares the assumption schema only adjacent to the assumption step (mid-execution, under context pressure) fails C-33.

**Updated totals:** 33 criteria, 215 pts. Formula: `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/25 × 125)`. Golden threshold bumped to 125.

**Phase 6 added to the arc:** *temporal precision and pre-reading contract coverage* — the same structural mechanisms applied to consequence reasoning (temporal classification) and schema coverage (assumption table joins the upfront contract).
