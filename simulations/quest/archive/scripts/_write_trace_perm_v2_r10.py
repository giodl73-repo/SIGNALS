content = """\
---
skill: quest-rubric
skill_target: trace-permissions
date: 2026-03-16
version: 2
changelog: >
  v2 adds C-11 (phase dependency chaining) and C-12 (inline violation sentinels)
  as aspirational criteria, extracted from Round 1 excellence signals (V-01, V-04 both 100).
  N_aspirational grows from 2 to 4; each aspirational point is worth 2.5 pts.
---

# Scoring Rubric: trace-permissions

**Skill:** Trace who can do what through RBAC, security roles, teams, and field-level security.
For each operation: which roles can perform it, which fields are visible, which records are accessible.
Identify: privilege escalation paths, missing field-level security, team membership gaps, sharing rule conflicts.
Stock roles: Customer Service / Dataverse security expert.

---

## Composite Score Formula

```
composite = (essential_pass/N_essential * 60)
          + (recommended_pass/N_recommended * 30)
          + (aspirational_pass/N_aspirational * 10)
```

**Golden threshold:** all essential criteria pass AND composite >= 80.

---

## Essential Criteria (60 points total, N=5)

All five must pass. A single essential failure means the output is not useful.

| ID | Text | Category | Weight | Pass Condition |
|----|------|----------|--------|----------------|
| C-01 | **Role-operation matrix** -- The output produces a matrix of roles against Dataverse operations (Create, Read, Write, Delete, Append, AppendTo, Assign, Share at minimum). Every cell must be filled: Granted, Denied, Conditional (with stated condition), or N/A. | correctness | essential | A complete matrix is present. Every cell carries an explicit value. Listing roles without operations, or vice versa, fails. A matrix with blank cells fails. |
| C-02 | **FLS coverage with explicit null case** -- The output checks whether field-level security (column security profiles) is configured for sensitive fields, names which fields are covered and which are not, and explicitly states when no FLS is configured. Absent FLS on sensitive fields is flagged as a gap. | coverage | essential | Every sensitive field in scope has an explicit FLS status (Configured / Not Configured). A system with no FLS is explicitly noted, not silently omitted. Absent FLS on sensitive fields appears in the gap inventory. |
| C-03 | **Record scope per role** -- The output assigns a record access scope to each role: own-records-only, business unit, parent-child BU, org-wide, or team-scoped. | correctness | essential | Every role in the trace has an associated access scope. Ambiguous or unresolved scope is flagged as a gap, not silently omitted. |
| C-04 | **Privilege escalation path detection** -- The output identifies at least one privilege escalation path (e.g., team membership granting broader role, sharing rule bypassing FLS, environment-level admin override) or explicitly concludes none were found after checking the known vectors. | correctness | essential | The output contains a section or finding dedicated to escalation paths. A conclusion of none found is acceptable only if the known vectors (team inheritance, sharing rules, impersonation, admin roles) were each checked and ruled out individually. |
| C-05 | **Security gap inventory** -- The output produces a named list of gaps: missing FLS on sensitive fields, team membership holes, sharing rule conflicts, or over-permissioned roles. | coverage | essential | At least one gap is named with a specific field, role, or rule. If no gaps exist, the output provides explicit evidence (e.g., all sensitive fields have FLS configured, no public sharing rules active) rather than a bare assertion. |

---

## Recommended Criteria (30 points total, N=3)

Output is better with these. Failing one degrades usefulness but does not disqualify.

| ID | Text | Category | Weight | Pass Condition |
|----|------|----------|--------|----------------|
| C-06 | **Dataverse-native terminology** -- The output uses correct Dataverse security constructs: business units, security roles, team types (owner vs. access), table permissions, column security profiles, sharing records, environment roles. No generic RBAC language is substituted where Dataverse terms apply. | correctness | recommended | At least 4 Dataverse-specific terms appear and are used accurately. Generic terms like group or permission level used without Dataverse mapping are treated as imprecision. |
| C-07 | **Sharing rule conflict analysis** -- The output checks whether sharing rules (manual, team-based, or via Power Automate) conflict with role-level access -- granting access that roles deny, or denying access that FLS permits. | depth | recommended | At least one sharing scenario is evaluated for conflict. A conclusion of no conflicts requires checking at least the intersection of one sharing rule with one FLS column profile. |
| C-08 | **Remediation specificity** -- For each identified gap, the output provides a specific, actionable remediation: which column security profile to create, which role privilege to tighten, which team assignment to add or remove. | behavior | recommended | At least 50% of named gaps have a specific remediation step (not just add FLS but create column security profile on creditlimit, restrict to Sales Manager role). Generic remediation advice without naming the exact configuration object fails. |

---

## Aspirational Criteria (10 points total, N=4)

These raise the bar once essential and recommended are stable.

| ID | Text | Category | Weight | Pass Condition |
|----|------|----------|--------|----------------|
| C-09 | **Defense-in-depth layering** -- The output evaluates security at all four Dataverse layers in sequence: (1) environment/admin role, (2) security role + BU scope, (3) team membership, (4) field-level security/column profiles. It identifies which layer is the effective enforcement point for each operation. | depth | aspirational | All four layers are named and assessed. For at least one operation, the output identifies the specific layer where access is granted or denied and explains why upper layers do not override it. |
| C-10 | **Cross-role differential analysis** -- The output compares access across two or more roles for the same operation and field set, surfacing where roles diverge and whether that divergence is intentional (principle of least privilege satisfied) or anomalous. | depth | aspirational | At least two roles are compared side-by-side on at least one operation. The analysis states whether the access differential is expected given the roles described purposes, or flags it as a candidate over-permission. |
| C-11 | **Phase dependency chaining** -- Each analytical phase or role explicitly declares what it requires from prior phases as named inputs. Phase N+1 cannot proceed without the named outputs of Phase N. The prompt structurally enforces sequence rather than relying on the model to volunteer it. | structure | aspirational | At least two consecutive phases name their dependency relationship explicitly. Dependency names must match actual output labels from the prior phase (e.g., the role list from Pass 1, Role A escalation verdict) -- generic references like the above do not qualify. |
| C-12 | **Inline violation sentinels** -- When the analysis discovers a violation, ambiguity, or unchecked state during the trace, the output places a named sentinel token at that point -- e.g., [GAP-FLS-fieldname], [SCOPE AMBIGUOUS], [UNCHECKED]. Sentinels accumulate into the gap inventory rather than being invented at summary time. | structure | aspirational | At least two distinct sentinel types are used. Each sentinel is placed at the point of discovery, not retroactively inserted into the gap section. The gap inventory (C-05) references or aggregates sentinels from the trace body rather than re-stating findings independently. |

---

## v2 Change Log

Two new aspirational criteria extracted from Round 1 excellence signals (V-01, V-04 both scored 100):

- **C-11** (phase dependency chaining): V-01 and V-04 both structurally required prior-phase outputs as named inputs to the next phase -- "Role A output is required input to Role B", "CLEARED only valid with named pass evidence". This enforces analytical sequence through structure, not model goodwill. The failure mode it prevents: phases that appear sequential but can be completed independently, allowing the model to skip or summarize earlier phases without producing the outputs later phases depend on.
- **C-12** (inline violation sentinels): V-04 used tokens [GAP-FLS-fieldname], [SCOPE AMBIGUOUS], [UNCHECKED] at the point of discovery rather than deferring all violations to the final gap section. This makes the trace self-annotating -- violations are structurally visible inline, and the gap inventory aggregates them rather than inventing them. The failure mode it prevents: gaps discovered during traversal that are silently dropped when the model transitions to summary mode.

The aspirational tier grows from N=2 to N=4. Point allocation per criterion decreases from 5 to 2.5, preserving the 10-point tier total.

---

## Scoring Reference

| Criteria tier | N | Points each | Max pts |
|---------------|---|-------------|---------|
| Essential | 5 | 12.0 | 60 |
| Recommended | 3 | 10.0 | 30 |
| Aspirational | 4 | 2.5 | 10 |
| **Total** | **12** | | **100** |

**Example scores:**

| Pass pattern | Composite | Golden? |
|-------------|-----------|---------|
| 5E + 3R + 4A | 100.0 | Yes |
| 5E + 3R + 2A | 95.0 | Yes |
| 5E + 3R + 0A | 90.0 | Yes |
| 5E + 2R + 2A | 85.0 | Yes |
| 5E + 2R + 0A | 80.0 | Yes (boundary) |
| 5E + 1R + 4A | 72.0 | No (composite < 80) |
| 4E + 3R + 4A | 88.0 | No (not all essential) |
| 3E + 3R + 4A | 76.0 | No (not all essential) |
"""

with open(r"C:\\src\\sim\\simulations\\quest\\rubrics\\trace-permissions-rubric-v2-2026-03-16.md", "w", encoding="utf-8") as f:
    f.write(content)
print("written", len(content), "chars")
