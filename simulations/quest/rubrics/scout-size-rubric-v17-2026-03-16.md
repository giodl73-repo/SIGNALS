**v17 written** to `simulations/quest/rubrics/scout-size-rubric-v17-2026-03-17.md`.

---

**What changed from v16**

Two new aspirational criteria added. Scoring denominator updated from 33 to 35.

---

**C-42 — CLOSED-LABEL column header encodes the output value format alongside the conditional fill constraint**

Derived from R16: V-02's CLOSED-LABEL column header reads `"fill only if your STATUS = BLOCKED — leave blank if your STATUS = CLEAR — format: …"` — the `format:` slot specifies the expected value structure. C-41 covers *when* to fill and *when* to leave blank; C-42 covers *what to write* when filling. Without it, a model that correctly determines STATUS = BLOCKED may produce a free-form prose closure reason rather than the structured traceable label `"Precondition A: [named condition]"` that C-38's row-level identifiability depends on. The `format:` specification in the column label completes the self-specifying column: fill condition + leave-blank condition + value shape — all resolvable from the header alone.

**C-43 — Self-test affirmative branch names the violated architectural contract alongside the failure class**

Derived from R16: V-01's Phase 2 self-test ends `"If yes: you have written a basis-negation — a Phase 2 charter violation."` C-33 requires the failure-class label (`basis-negation`); C-43 requires the affirmative branch to also name the architectural boundary crossed (`Phase 2 charter violation`). The contract label upgrades the diagnostic from content-level to structural-level: the model understands not just what error it made but which guarantee is now broken — enabling targeted correction ("address a dimension Phase 1 did not confirm") rather than generic revision. It also makes the failure traceable at the output level without cross-referencing the charter definition.
