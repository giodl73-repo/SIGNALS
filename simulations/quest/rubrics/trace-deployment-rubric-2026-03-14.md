Rubric written to `simulations/quest/rubrics/trace-deployment-rubric-2026-03-14.md`.

**10 criteria across 3 tiers:**

**Essential (C-01–C-05, 60 pts — all must pass)**
- C-01: Pre-deploy checks enumerated (>=3 concrete checks)
- C-02: Deployment sequence is step-by-step (>=4 ordered steps)
- C-03: Post-deploy validation specified (>=2 specific actions)
- C-04: Rollback path defined (trigger + steps + verification)
- C-05: At least one gap per phase (4 gaps minimum — no pure happy-path)

**Recommended (C-06–C-08, 30 pts)**
- C-06: Ordering dependencies made explicit (not just implied by list order)
- C-07: Domain framing applied (Commerce/Operations vocabulary)
- C-08: Gaps are actionable, not just named

**Aspirational (C-09–C-10, 10 pts)**
- C-09: Gaps prioritized by deployment risk/severity
- C-10: Automation hooks identified

The hard requirement on C-05 (one gap per phase) is the key discriminator — it forces the skill to do gap analysis across all four phases, not just trace the happy path.
nment" does not pass. |
| C-02 | **Deployment sequence is step-by-step** | correctness | essential | Output presents an ordered, numbered sequence of deployment steps. Steps are discrete and ordered — not a summary paragraph. At least 4 steps present. |
| C-03 | **Post-deploy validation specified** | coverage | essential | Output identifies at least 2 specific post-deploy validation actions (e.g., smoke tests, health checks, data integrity probes). "Test that it works" does not pass. |
| C-04 | **Rollback path is defined** | correctness | essential | Output describes a concrete rollback path: what triggers rollback, what steps undo the deployment, and how to verify rollback succeeded. Absence of any rollback content fails. |
| C-05 | **At least one gap identified per phase** | behavior | essential | Output calls out at least one missing or weak element in pre-deploy, sequence, post-deploy, and rollback — four gaps minimum, one per phase. Pure happy-path trace with no gap analysis fails. |

---

## Recommended Criteria (30 pts — better with these)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Deployment order dependencies made explicit** | depth | recommended | Output calls out at least one ordering dependency — steps that must complete before others can start (e.g., "database migration must precede service restart"). Implicit ordering in a list does not satisfy this. |
| C-07 | **Domain framing applied** | depth | recommended | Output uses Commerce or Operations deployment vocabulary appropriate to the solution context (e.g., catalog sync, order pipeline, inventory lock, tenant provisioning). Generic cloud-deploy framing without domain anchoring does not pass. |
| C-08 | **Gaps are actionable, not just named** | correctness | recommended | For each identified gap, the output states what should be added or changed — not just that something is missing. "No rollback trigger defined — add a health-check threshold that fires the revert script" passes; "missing rollback trigger" alone does not. |

---

## Aspirational Criteria (10 pts — raise the bar)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Gaps prioritized by deployment risk** | depth | aspirational | Output ranks or labels identified gaps by severity or blast radius (e.g., critical / moderate / low, or "blocks rollback" vs "cosmetic"). Unranked gap lists do not satisfy this. |
| C-10 | **Automation hooks identified** | behavior | aspirational | Output identifies at least one place in the deployment lifecycle where automation could enforce a check that is currently manual or absent (e.g., CI gate, pre-deploy script, post-deploy canary assertion). |

---

## Scoring Summary

| Tier | Criteria | Points Available |
|------|----------|-----------------|
| Essential | C-01 through C-05 (all must pass) | 60 |
| Recommended | C-06 through C-08 | 30 |
| Aspirational | C-09 through C-10 | 10 |
| **Total** | | **100** |

**Golden**: All of C-01–C-05 pass AND composite >= 80.
