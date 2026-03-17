Written to `simulations/quest/rubrics/trace-permissions-rubric-2026-03-14.md`.

**Rubric summary — trace-permissions v1:**

**Essential (4 criteria, 60 pts):**
- C-01 Role-Operation Matrix — every op (CRUD+) mapped to permitted roles
- C-02 Field-Level Security Per Role — specific fields, specific roles, specific deny/allow
- C-03 Record Access Scope — Own / BU / Parent BU / Org stated per role
- C-04 At Least One Gap Identified — must name a real problem, not describe the model

**Recommended (3 criteria, 30 pts):**
- C-05 Privilege Escalation Path — named path, not just assertion
- C-06 Sharing Rule Conflict — widening or contradictory grants called out
- C-07 Team Membership Gap — missing assignment or over-combined permissions

**Aspirational (2 criteria, 10 pts):**
- C-08 Risk-Ranked Gap Summary — H/M/L with justification
- C-09 Remediation Per Gap — concrete action, not vague guidance

The key design decision: C-04 (gap identification) is essential, not recommended. A permissions trace that only describes access without surfacing problems isn't useful — the whole point of the skill is to find what's wrong.
plies") do not pass. |
| C-03 | **Record Access Scope** | correctness | essential | For each role, output states the access scope: Own / Business Unit / Parent BU / Organization (or equivalent RBAC scope). Must not conflate role privileges with record ownership. |
| C-04 | **At Least One Security Gap Identified** | coverage | essential | Output explicitly names at least one missing or misconfigured security control -- a missing FLS restriction, an over-permissive role, a sharing rule conflict, or a team membership gap. |

---

## Recommended Criteria (30 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-05 | **Privilege Escalation Path Analysis** | depth | recommended | Output identifies at least one plausible privilege escalation path -- e.g., a user in Role A who can reassign records to gain Role B scope, or a team membership that grants unintended org-wide access. Must name the path, not just assert it exists. |
| C-06 | **Sharing Rule Conflict Detection** | depth | recommended | Output examines sharing rules (manual, criteria-based, or owner-based) and identifies at least one case where a sharing rule widens access beyond the security role baseline, or a case where sharing rules create contradictory access grants. |
| C-07 | **Team Membership Gap** | coverage | recommended | Output identifies at least one scenario where team membership creates a gap -- either a user not on the expected team who loses access, or a user on multiple teams whose combined permissions exceed intent. |

---

## Aspirational Criteria (10 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-08 | **Risk-Ranked Gap Summary** | depth | aspirational | Output concludes with a ranked list of identified gaps ordered by risk severity (High / Medium / Low), with a one-line justification per gap. Ranking must be defensible relative to the operation and data sensitivity described. |
| C-09 | **Remediation Recommendation Per Gap** | behavior | aspirational | For each gap identified, output provides a concrete remediation action (e.g., "add FLS read-deny on AccountNumber for Customer Service role", "remove team-level sharing rule that grants org-wide read"). Vague guidance ("tighten security") does not pass. |

---

## Scoring Table

| Tier | Criteria | Max Points | Points Per Criterion |
|------|----------|------------|----------------------|
| Essential | C-01, C-02, C-03, C-04 | 60 | 15 each |
| Recommended | C-05, C-06, C-07 | 30 | 10 each |
| Aspirational | C-08, C-09 | 10 | 5 each |
| **Total** | | **100** | |

---

## Failure Modes (auto-fail essential)

- Output lists roles without tying them to operations (C-01 fails)
- Output says "field-level security should be configured" without specifying which fields or which roles (C-02 fails)
- Output uses only "user can access their own records" with no mention of scope hierarchy (C-03 fails)
- Output describes the RBAC model without surfacing any problem, gap, or risk (C-04 fails)

---

## Notes

- The rubric is platform-agnostic. Whether the system is Dataverse, Salesforce, custom RBAC, or another model, the criteria apply by analogy.
- Stock reviewer persona (Dataverse security expert) surfaces FLS gaps and sharing rule conflicts; Customer Service perspective surfaces team membership and record visibility gaps.
- Version 1 -- iterate rubric if golden outputs reveal systematic blind spots not covered here.
