content = """\
---
skill: quest-rubric
skill_target: trace-permissions
date: 2026-03-15
version: 3
prev_version: 2
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
| C-10 | **Real-time gap accumulation** -- Gaps are logged progressively as discovered during entity and field traversal, not collected in a single end-of-trace sweep. The running gap log grows inline as each entity and field is analyzed. | discipline | aspirational | At least two gap entries appear during the body of the trace (not only in a consolidated summary section), demonstrating progressive accumulation rather than post-hoc consolidation. |
| C-11 | **Explicit non-escalation documentation** -- For every role checked for privilege escalation, the output states the negative case explicitly: what access was checked and why no escalation path exists. Positive findings alone are insufficient -- every checked role gets a verdict. | discipline | aspirational | At least one role receives an explicit rule-out statement naming: the access level examined and the specific reason the escalation path is closed (e.g., "Checked Service Rep: write on Case at BU scope only -- no sharing rule grants cross-BU; no team membership to higher-privilege team. No escalation."). |
| C-12 | **Phase-gate completeness checkpoint** -- The output includes at least one explicit self-audit checkpoint that confirms inventory coverage before advancing to gap analysis. The checkpoint names what was covered, not just that "all entities were reviewed." | discipline | aspirational | A distinct completeness assertion appears at a phase boundary naming the entities covered, the sensitive fields confirmed, and any scope decisions made (e.g., entities out-of-scope and why). Implicit transitions do not pass. |
| C-13 | **Entity-level closure marker** -- Each entity section closes with an explicit completeness marker before the trace advances to the next entity. This is finer-grained than C-12 (phase boundary) and distinct from C-10 (gap timing) -- it names what was covered for that entity, not just what gaps were found. | discipline | aspirational | At least one entity section includes a named closure assertion identifying: the operations reviewed for that entity, the fields confirmed, and the gaps tallied -- before the output advances to the next entity. An implicit transition with no closure statement does not pass, even if gaps were logged inline during the section. |
| C-14 | **Per-role sharing rule explicit verdict** -- For every role in the trace, the output states the sharing rule verdict explicitly -- whether expansion was found or not. Sharing rule analysis that documents only conflicts (positive findings) is incomplete; roles with no sharing rule expansion require an explicit confirmation to that effect. | discipline | aspirational | At least one role receives an explicit negative sharing rule confirmation naming the role and the basis for the finding (e.g., "Confirmed: no sharing rules expand [Role] access beyond OWD + security role -- no criteria-based or manual sharing applies"). Positive-only sharing rule coverage fails this criterion. |
| C-15 | **Numbered gap identifiers enabling cross-reference** -- Gap entries carry sequential identifiers (e.g., G-01, G-02) assigned at discovery time. Downstream sections -- remediation steps, phase gates, defense-in-depth tables -- reference gaps by identifier rather than re-describing them. A gap log without identifiers cannot be reliably cross-referenced; downstream references that repeat full gap descriptions instead of citing an ID indicate this criterion is not met. | discipline | aspirational | Gap entries use a consistent numbered scheme. At least one downstream section (remediation, gate table, or defense-in-depth) references a gap by its identifier rather than repeating the description. |

---

## v3 Change Log

Three new aspirational criteria added from Round 2 excellence signals (V-01 through V-04):

- **C-13** (entity-level closure marker): V-01 ENTITY GAP TALLY block, required at the close of every entity section before advancing, is a distinct closure pattern between C-10 (inline gap timing) and C-12 (phase boundary gate). It operates at entity granularity and requires naming operations reviewed and fields confirmed -- not just gaps found. The failure mode it prevents: entity-level coverage gaps masked by smooth narrative flow between entity sections.
- **C-14** (per-role sharing rule explicit verdict): V-02 required "Confirmed: no sharing rules expand [Role] access" for every role checked, whether or not a conflict was found. C-06 requires identifying conflicts that exist; C-14 requires a verdict for every role -- the sharing rule analog of C-11 non-escalation documentation. The failure mode it prevents: sharing rule analysis that appears complete because all conflicts are documented, while unchecked roles are implicitly assumed clean.
- **C-15** (numbered gap identifiers): V-04 Inline Gap Stream introduced [G-##] sequential identifiers assigned at discovery. Without identifiers, remediation steps must re-describe gaps rather than citing them, phase gates cannot reference specific gaps by name, and the gap log degrades from a cross-referenceable artifact to a flat list. The failure mode it prevents: gap entries that cannot be traced forward to their remediation or backward from a phase gate without manual text matching.

The aspirational tier grows from N=5 to N=8. Point allocation per criterion decreases from 2 to 1.25, preserving the 10-point tier total.

---

## Scoring Worksheet

```
Essential pass count  (N=4): ___  ->  ___ / 4 * 60 = ___
Recommended pass count (N=3): ___  ->  ___ / 3 * 30 = ___
Aspirational pass count (N=8): ___  ->  ___ / 8 * 10 = ___

Composite score: ___
Golden (all essential + composite >= 80): YES / NO
```

---

## Failure Modes to Watch

- **Role enumeration without scope** -- listing roles without stating what records they can reach (fails C-02)
- **FLS mentioned but not per-role** -- stating "this field has FLS enabled" without mapping read/write/deny per role (fails C-03)
- **Generic gap warnings** -- "sharing rules may be too broad" without naming the specific rule or record set (fails C-04)
- **Missing stock role coverage** -- Customer Service or Dataverse security expert roles not addressed when the topic involves those domains
- **Gap collapse** -- inline security signals mentioned in passing but absent from any consolidated gap structure (fails C-10)
- **Escalation by silence** -- only positive escalation paths documented; roles with no escalation path receive no verdict (fails C-11)
- **Implicit phase transitions** -- trace moves from inventory to analysis without any coverage confirmation; missed entities propagate undetected (fails C-12)
- **Entity drift** -- trace advances from one entity to the next without naming what was covered in the entity just closed; operations reviewed and fields confirmed are implicit (fails C-13)
- **Sharing rule silence** -- only roles with sharing rule conflicts receive sharing rule commentary; clean roles receive no verdict, leaving the sharing rule picture incomplete (fails C-14)
- **Unanchored gap references** -- remediation steps re-describe gaps in full rather than citing a gap identifier; cross-tracing from fix back to finding requires manual text matching (fails C-15)
"""

with open(r"C:\\src\\sim\\simulations\\quest\\rubrics\\trace-permissions-rubric-v3-2026-03-15.md", "w", encoding="utf-8") as f:
    f.write(content)
print("written", len(content), "chars")
