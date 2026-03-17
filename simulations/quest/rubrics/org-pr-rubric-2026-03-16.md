Rubric written to `simulations/quest/rubrics/org-pr-rubric-v1-2026-03-16.md`.

---

**Summary of criteria:**

**Essential (must all pass):**
- **C-01** Coverage — 2+ roles from the defined set produce findings
- **C-02** Severity — every finding tagged P1/P2/P3, none unclassified
- **C-03** File-based selection — each role's inclusion justified by which files changed
- **C-04** Go/no-go — explicit verdict with stated basis, not contradicted by findings
- **C-05** Structure — each reviewer section labeled with role name, clearly separated

**Recommended:**
- **C-06** Consensus analysis — convergence (2+ roles hit same surface) and conflicts named
- **C-07** P1 blocks go — formula consistency: open P1 = No-Go, no exceptions
- **C-08** Actionable findings — 80%+ of findings include a specific locator (file/line/pattern)

**Aspirational:**
- **C-09** Author-blind perspective — at least one finding per section challenges an embedded assumption
- **C-10** Non-obvious issue — at least one cross-cutting or out-of-diff concern the author wouldn't self-identify

The essential criteria are tight because `org-pr`'s entire value proposition is "surface issues the author missed" — if the output lacks role attribution, severity, or a clear verdict, it's not actionable regardless of how much text it produces.
