Written to `simulations/quest/rubrics/trace-contract-rubric-v1-2026-03-15.md`.

---

**Rubric summary — trace-contract**

**5 essential** (C-01 through C-05):
- **C-01 Contract-first order** — expected written from spec before execution, not reverse-engineered
- **C-02 Explicit diff** — each deviation shown as a concrete before/after pair
- **C-03 Severity per finding** — every mismatch labeled breaking / degraded / cosmetic
- **C-04 Root cause per finding** — why, not just that, it deviated
- **C-05 Spec reference per finding** — ties each finding to the contract clause it violates

**3 recommended** (C-06 through C-08):
- **C-06 Automate / Connectors lens** — integration-level impact called out per finding
- **C-07 Summary verdict** — counts by severity + PASS/FAIL conclusion
- **C-08 Clean no-finding confirmation** — explicit "contract honored" rather than silence

**2 aspirational** (C-09, C-10):
- **C-09 Amendment suggestion** — breaking findings propose spec-side vs. implementation-side resolution
- **C-10 Pattern recognition** — related findings grouped when root cause is shared

Golden = all essential pass + composite >= 80. Passing essential + all recommended gives 90 — comfortably golden without needing aspirational.
