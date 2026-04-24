Rubric written to `simulations/quest/rubrics/crew-review-rubric-v1-2026-03-16.md`.

---

**crew-review rubric v1 — structure:**

**5 Essential** (60 pts, all must pass):
- **C-01** Correctness — roles selected from `.roles/`, none fabricated
- **C-02** Format — review matrix present with all 4 columns (role, findings, severity, recommendation)
- **C-03** Correctness — severity is HIGH/MEDIUM/LOW only, semantics match finding content
- **C-04** Depth — each role reviews from its own lens, findings non-overlapping
- **C-05** Depth — recommendations are concrete and name a specific surface/action

**3 Recommended** (30 pts):
- **C-06** Behavior — depth flag respected (standard 2-4 roles; deep = full registry)
- **C-07** Coverage — at least one convergence or conflict named across roles
- **C-08** Format — AMEND section present with 2+ named options

**2 Aspirational** (10 pts):
- **C-09** Depth — inertia-advocate appears first with null hypothesis statement
- **C-10** Depth — 80%+ findings name a specific artifact surface (not generic)

**Golden**: all 5 essential pass + composite >= 80. Achievable with all essential + 2/3 recommended (exactly 80).

Key design note: this rubric targets the simpler **matrix-first** output form — distinct from org-review's DISPOSITION_CONTRACT v1 structure which has its own 38-criteria rubric series.
