Written to `simulations/quest/rubrics/org-chart-rubric-v7-2026-03-16.md`.

---

**Two new criteria extracted from R6:**

**C-23 — Sequencing guard embeds a mechanism-reason count** (V-01/R6 source)
C-22 requires an observable guard. C-23 requires the guard to additionally print the count of mechanism-typed reasons it is sealing — e.g., `{N} mechanism reasons recorded` — making the guard self-verifying. A guard without a count passes C-22, fails C-23. Dep: C-22.

**C-24 — Anti-Pattern Watch citations use typed register reference syntax** (V-02/R6 source)
C-21 requires a register artifact to exist before APW. C-24 requires APW cells to cite from it using `[element name] (cat-N)` syntax with explicit category codes. Prose references to correct elements pass C-21, fail C-24. Dep: C-21.

**Denominator:** `/14` → `/16` (0.625 pts per criterion)

**R6 scores:** Both V-01 and V-02 reach **98.8** (14/16). V-01 earns C-22+C-23 (4-part with count guard), fails C-21/C-24. V-02 earns C-21+C-24 (register + typed citations), fails C-22/C-23. No variation in R5 or R6 reaches 16/16 — a first perfect run requires combining both designs.
