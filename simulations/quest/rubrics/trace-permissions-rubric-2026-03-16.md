Written to `simulations/quest/rubrics/trace-permissions-rubric-v1-2026-03-16.md`.

---

**Rubric summary** (9 criteria, 4+3+2):

| Tier | ID | Criterion | Category |
|------|----|-----------|----------|
| Essential | C-01 | Operation-Role Matrix | correctness |
| Essential | C-02 | Field-Level Security Coverage | coverage |
| Essential | C-03 | Record Accessibility Scope | correctness |
| Essential | C-04 | Gap or Risk Identification | depth |
| Recommended | C-05 | Privilege Escalation Path Traced | depth |
| Recommended | C-06 | Role Hierarchy Respected | correctness |
| Recommended | C-07 | Remediation Suggestions | behavior |
| Aspirational | C-08 | Cross-Entity Cascade | depth |
| Aspirational | C-09 | Structured Summary Table | format |

**Design rationale:**

- C-04 (gap identification) is essential — an output that only confirms what's allowed without surfacing any risk has zero value for a permissions tracer.
- C-05 (privilege escalation) is recommended not essential because the skill may legitimately be called in a context where no escalation path exists; forcing a gap there would make valid "clean" outputs fail.
- C-08 (cross-entity cascade) is aspirational because it requires cross-entity schema knowledge that not every invocation context will have.
