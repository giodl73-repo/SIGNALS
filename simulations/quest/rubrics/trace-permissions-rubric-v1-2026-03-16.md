---
skill: quest-rubric
skill_target: trace-permissions
date: 2026-03-16
version: 1
---

# Rubric: trace-permissions

Evaluates output from `/trace-permissions` -- tracing who can do what through RBAC, security roles, teams, and field-level security.

---

## Scoring Formula

```
Composite = (essential_pass/N * 60) + (recommended_pass/N * 30) + (aspirational_pass/N * 10)
```

**Golden threshold**: all essential criteria pass AND composite >= 80.

---

## Essential Criteria (60 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-01 | **Operation-Role Matrix** -- Output enumerates the target operations and maps each operation to the set of security roles that can perform it. | essential | correctness | At least one operation is explicitly listed with at least one role that can or cannot perform it. Matrix or equivalent table/list is present. |
| C-02 | **Field-Level Security Coverage** -- For each operation, the output identifies which fields are visible/editable and which are restricted per role. | essential | coverage | At least one field-level restriction is traced for at least one operation. Generic statements like "all fields available" are acceptable only if explicitly justified. |
| C-03 | **Record Accessibility Scope** -- The output identifies which records each role can access (e.g., owned, team, business-unit, org-wide) for the traced operations. | essential | correctness | At least one record-access scope level (owner / team / BU / org) is identified per operation or per role. Missing scope is flagged as a gap, not silently omitted. |
| C-04 | **Gap or Risk Identification** -- The output names at least one security gap: a missing FLS restriction, a privilege escalation path, a team membership gap, or a sharing rule conflict. | essential | depth | At least one named gap appears in the output with a description of why it is a risk. Outputs that only confirm permissions without identifying any gap do not pass. |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-05 | **Privilege Escalation Path Traced** -- The output explicitly traces at least one privilege escalation path: a sequence of role assignments, team memberships, or sharing rules that allows a lower-privilege identity to reach a higher-privilege resource. | recommended | depth | A concrete escalation path is described with the starting role/user, the intermediate step (team membership, sharing rule, etc.), and the elevated access reached. |
| C-06 | **Role Hierarchy Respected** -- Findings acknowledge the role hierarchy (parent/child BU structure or role inheritance) and note where inheritance amplifies or limits access. | recommended | correctness | At least one inheritance or hierarchy effect is called out -- either "role X inherits from Y and therefore can..." or "role X is scoped to BU-only and cannot see...". |
| C-07 | **Remediation Suggestions** -- For each identified gap, the output proposes a specific remediation: a role change, FLS rule to add, team membership to revoke, or sharing rule to restrict. | recommended | behavior | At least one gap in C-04 has a corresponding actionable remediation (not just a restatement of the problem). |

---

## Aspirational Criteria (10 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-08 | **Cross-Entity Cascade** -- The output traces permissions across related entities (e.g., a user with Write on Account also gains implied access to child Contacts via relationship-based sharing), surfacing cascade risks. | aspirational | depth | At least one cross-entity cascade effect is identified with the parent entity, child entity, and the mechanism (cascade sharing, lookup field, related record access). |
| C-09 | **Structured Summary Table** -- The output closes with a summary table: each operation row contains role, FLS verdict (pass/fail/partial), record scope, and gap flag. | aspirational | format | A table with at minimum three columns (operation or role, FLS status, record scope) is present and consistently populated for all traced operations. |

---

## Scoring Guide

| Result | Meaning |
|--------|---------|
| All C-01 through C-04 pass | Essential bar cleared |
| Composite >= 80 | Golden threshold met |
| Composite 60-79 | Useful but incomplete -- missing recommended depth |
| Composite < 60 | Not useful -- essential gaps present |

---

## Notes for Evaluators

- **Partial credit is binary per criterion** -- each criterion either passes or fails; no half-points.
- A criterion passes if the pass condition is met for at least the primary operation or role being traced; it does not require exhaustive coverage of every operation/role unless the criterion explicitly says so.
- Outputs that list roles without any field-level or record-scope analysis fail C-02 and C-03 even if C-01 passes.
- "Placeholder" or stub outputs with no actual permission data fail all essential criteria.
