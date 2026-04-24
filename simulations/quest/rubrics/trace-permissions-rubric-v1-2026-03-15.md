---
skill: quest-rubric
skill_target: trace-permissions
date: 2026-03-15
version: 1
---

# Rubric: trace-permissions

Scoring rubric for the `trace-permissions` skill. Evaluates whether the output correctly traces RBAC, security roles, teams, and field-level security -- and identifies privilege escalation paths, missing FLS, team gaps, and sharing rule conflicts.

## Composite Score Formula

```
composite = (essential_pass/N * 60) + (recommended_pass/N * 30) + (aspirational_pass/N * 10)
```

**Golden threshold**: all essential criteria pass AND composite >= 80.

---

## Essential Criteria (60 points -- all must pass)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Operation-role matrix** -- For each operation named in the topic, the output states which roles can perform it. No operation is left unmapped. | correctness | essential | Every operation has at least one role assignment; no operation appears with "unknown" or blank role. |
| C-02 | **Record access scope** -- For each role, the output identifies the record-access level: org-wide, business unit, team, or user-owned. Scope is stated explicitly, not implied. | correctness | essential | Each role entry includes an explicit access scope (e.g., "BU-level read", "org-wide write"). |
| C-03 | **Field-level security coverage** -- For at least the highest-sensitivity fields in the topic, the output identifies which roles can read vs. write vs. are denied access. | coverage | essential | At least 3 distinct fields have explicit FLS assignments per role; denial is stated where it applies. |
| C-04 | **Security gap identification** -- The output names at least one concrete security gap: a privilege escalation path, a missing FLS rule, a team membership gap, or a sharing rule conflict. | correctness | essential | At least one gap is named with: (a) the specific role/field/record involved, (b) the type of gap, and (c) the risk it creates. |

---

## Recommended Criteria (30 points)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-05 | **Escalation path tracing** -- Where a lower-privileged role can reach resources intended for higher-privileged roles (via team membership, sharing rules, or field inheritance), the output traces the exact path: role -> mechanism -> resource reached. | depth | recommended | At least one escalation path is traced end-to-end with the intermediate mechanism named. |
| C-06 | **Sharing rule conflict analysis** -- Where sharing rules broaden access beyond security role intent, the output identifies the conflict and states which records become over-exposed. | depth | recommended | At least one sharing rule conflict is identified with: the rule, the role affected, and the over-exposed record set. |
| C-07 | **Team membership gap analysis** -- For operations that require team membership (e.g., queue access, team-owned records), the output identifies roles that are blocked due to missing team assignments. | coverage | recommended | At least one team membership gap is identified, naming the operation blocked and the role affected. |

---

## Aspirational Criteria (10 points)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-08 | **Remediation guidance** -- For each identified gap, the output provides a specific, actionable fix: the exact FLS rule to add, the sharing rule to restrict, the team to create, or the role privilege to remove. | depth | aspirational | Every gap identified in C-04/C-05/C-06/C-07 has a corresponding remediation step. Generic advice ("review permissions") does not pass. |
| C-09 | **Defense-in-depth assessment** -- The output evaluates whether the security model layers controls correctly: security role + FLS + record ownership each provide an independent enforcement boundary. Identifies any single-point-of-failure in the access control stack. | behavior | aspirational | Output explicitly names whether each enforcement layer (role, FLS, record scope) is independently enforced or whether bypassing one layer bypasses the control. |

---

## Scoring Worksheet

```
Essential pass count  (N=4): ___  ->  ___ / 4 * 60 = ___
Recommended pass count (N=3): ___  ->  ___ / 3 * 30 = ___
Aspirational pass count (N=2): ___  ->  ___ / 2 * 10 = ___

Composite score: ___
Golden (all essential + composite >= 80): YES / NO
```

---

## Failure Modes to Watch

- **Role enumeration without scope** -- listing roles without stating what records they can reach (fails C-02)
- **FLS mentioned but not per-role** -- stating "this field has FLS enabled" without mapping read/write/deny per role (fails C-03)
- **Generic gap warnings** -- "sharing rules may be too broad" without naming the specific rule or record set (fails C-04)
- **Missing stock role coverage** -- Customer Service or Dataverse security expert roles not addressed when the topic involves those domains
