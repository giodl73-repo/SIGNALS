rubric = """\
# trace-permissions Rubric -- v4 (2026-03-16)

**Skill:** trace-permissions
**Version:** 4
**Structure:** 5 essential + 3 recommended + 9 aspirational = 17 criteria
**Max score:** 112.5 (Essential 60 + Recommended 30 + Aspirational 22.5)

---

## Essential Criteria (60 points total, N=5)

All five must pass for the output to qualify as a golden. A single essential failure disqualifies regardless of other scores.

| ID | Text | Category | Weight | Pass Condition |
|----|------|----------|--------|----------------|
| C-01 | **Role x operation matrix** -- The output produces a complete matrix mapping each named role to each operation (read, create, update, delete, share, assign) across relevant tables. No role/operation pair is omitted without explicit justification. | coverage | essential | Every named role appears as a row. Every applicable operation appears as a column. Cells that cannot be determined are marked UNKNOWN rather than omitted. |
| C-02 | **FLS gap detection** -- The output identifies fields protected by field-level security (column security profiles) and checks whether each sensitive field has an active profile. If no profiles exist, the output states this explicitly rather than omitting FLS analysis. | correctness | essential | At least one field is evaluated for FLS coverage. If no column security profiles are active, the output explicitly states that finding and names the sensitive fields that would require profiles if the data classification changed. |
| C-03 | **BU scope analysis** -- The output identifies the business unit scope for each role (organization-wide, business unit, business unit + child, user-only) and evaluates whether the scope matches the intended access pattern. | correctness | essential | Every named role has an explicit BU scope assignment. For at least one role, the output evaluates whether the assigned scope is appropriate or over-permissioned relative to the stated purpose. |
| C-04 | **Escalation path detection** -- The output identifies at least one privilege escalation path (e.g., team membership granting broader role, sharing rule bypassing FLS, environment-level admin override) or explicitly concludes none were found after checking the known vectors. | correctness | essential | The output contains a section or finding dedicated to escalation paths. A conclusion of none found is acceptable only if the known vectors (team inheritance, sharing rules, impersonation, admin roles) were each checked and ruled out individually. |
| C-05 | **Security gap inventory** -- The output produces a named list of gaps: missing FLS on sensitive fields, team membership holes, sharing rule conflicts, or over-permissioned roles. | coverage | essential | At least one gap is named with a specific field, role, or rule. If no gaps exist, the output provides explicit evidence (e.g., all sensitive fields have FLS configured, no public sharing rules active) rather than a bare assertion. |

---

## Recommended Criteria (30 points total, N=3)

Output is better with these. Failing one degrades usefulness but does not disqualify.

| ID | Text | Category | Weight | Pass Condition |
|----|------|----------|--------|----------------|
| C-06 | **Dataverse-native terminology** -- The output uses correct Dataverse security constructs: business units, security roles, team types (owner vs. access), table permissions, column security profiles, sharing records, environment roles. No generic RBAC language is substituted where Dataverse terms apply. | correctness | recommended | At least 4 Dataverse-specific terms appear and are used accurately. Generic terms like group or permission level used without Dataverse mapping are treated as imprecision. |
| C-07 | **Sharing rule conflict analysis** -- The output checks whether sharing rules (manual, team-based, or via Power Automate) conflict with role-level access -- granting access that roles deny, or denying access that FLS permits. | depth | recommended | At least one sharing scenario is evaluated for conflict. A conclusion of no conflicts requires checking at least the intersection of one sharing rule with one FLS column profile. |
| C-08 | **Remediation specificity** -- For each identified gap, the output provides a specific, actionable remediation: which column security profile to create, which role privilege to tighten, which team assignment to add or remove. | behavior | recommended | At least 50% of named gaps have a specific remediation step (not just "add FLS" but "create column security profile on creditlimit, restrict to Sales Manager role"). Generic remediation advice without naming the exact configuration object fails. |

---

## Aspirational Criteria (22.5 points total, N=9)

These raise the bar once essential and recommended are stable.

| ID | Text | Category | Weight | Pass Condition |
|----|------|----------|--------|----------------|
| C-09 | **Defense-in-depth layering** -- The output evaluates security at all four Dataverse layers in sequence: (1) environment/admin role, (2) security role + BU scope, (3) team membership, (4) field-level security/column profiles. It identifies which layer is the effective enforcement point for each operation. | depth | aspirational | All four layers are named and assessed. For at least one operation, the output identifies the specific layer where access is granted or denied and explains why upper layers do not override it. |
| C-10 | **Cross-role differential analysis** -- The output compares access across two or more roles for the same operation and field set, surfacing where roles diverge and whether that divergence is intentional (principle of least privilege satisfied) or anomalous. | depth | aspirational | At least two roles are compared side-by-side on at least one operation. The analysis states whether the access differential is expected given the roles described purposes, or flags it as a candidate over-permission. |
| C-11 | **Phase dependency chaining** -- Each analytical phase or role explicitly declares what it requires from prior phases as named inputs. Phase N+1 cannot proceed without the named outputs of Phase N. The prompt structurally enforces sequence rather than relying on the model to volunteer it. | structure | aspirational | At least two consecutive phases name their dependency relationship explicitly. Dependency names must match actual output labels from the prior phase (e.g., "the role list from Pass 1", "Role A escalation verdict") -- generic references like "the above" do not qualify. |
| C-12 | **Inline violation sentinels** -- When the analysis discovers a violation, ambiguity, or unchecked state during the trace, the output places a named sentinel token at that point -- e.g., [GAP-FLS-fieldname], [SCOPE AMBIGUOUS], [UNCHECKED]. Sentinels accumulate into the gap inventory rather than being invented at summary time. | structure | aspirational | At least two distinct sentinel types are used. Each sentinel is placed at the point of discovery, not retroactively inserted into the gap section. The gap inventory (C-05) references or aggregates sentinels from the trace body rather than re-stating findings independently. |
| C-13 | **Security state persistence (inertia framing)** -- Security verdicts assigned to a role in one phase carry forward as the persistent default into subsequent phases. A role that is CLEARED in Phase 2 remains CLEARED in Phase 3 unless Phase 3 produces a finding that explicitly overrides it. Phases do not reset role state to unknown; they inherit and either confirm or amend prior verdicts. | structure | aspirational | At least one role verdict carries forward across two consecutive phases with explicit continuity language -- e.g., "CLEARED from Phase 2, no change" or "Phase 3 finding overrides Phase 2 CLEARED verdict". A phase that re-issues a verdict without referencing prior-phase state fails, even if the new verdict happens to be correct. |
| C-14 | **Failure mode enumeration** -- The prompt names the specific failure mode that each structural element (phase, pass, sentinel type, or aggregation rule) defends against. Example: "Phase 4 is structured as an aggregator because Failure Mode 4 is gap loss during model transition from traversal to summary." The structural choice is legible and testable: a reader can verify that the structure actually prevents the named failure. | structure | aspirational | At least two structural elements carry an associated named failure mode. Each failure mode names the specific analytical error prevented -- not a generic quality concern ("to improve accuracy") but a concrete failure path (e.g., "prevents model from skipping Phase 2 when role list is short"). |
| C-15 | **Pre-phase failure mode catalog** -- Before Phase 1 begins, the prompt includes a named structural element (e.g., FAILURE MODE MAP, structural threat model) that lists every failure mode the subsequent phases defend against. This is distinct from C-14 (inline annotation at each phase) -- C-15 requires the complete catalog to be present upfront, making structural omission detectable before analysis begins rather than discoverable phase-by-phase as each annotation is encountered. | structure | aspirational | A named pre-phase structural element (appearing before Phase 1 instructions) lists at least 3 named failure modes. Each entry maps to at least one subsequent phase, gate, or structural construct. A phase-by-phase annotation pattern (V-02 style) does not satisfy this criterion even if every phase carries an annotation -- the catalog must precede Phase 1. |
| C-16 | **SHALL-level enforcement for cross-role differential** -- The prompt uses SHALL/SHALL NOT language to structurally require cross-role differential analysis. Not "compare roles where relevant" but an explicit SHALL instruction naming the comparison, the conclusion required (expected differential vs. candidate over-permission), and the disposition for each case. This is the mechanism that elevates C-10 from emergent-PARTIAL (data present in matrix, comparison derivable) to enforced-PASS (analysis structurally required). | structure | aspirational | At least one SHALL-level instruction explicitly requires cross-role differential comparison by name. The instruction must require both (a) performing the comparison across named roles and (b) stating an explicit conclusion for each pair -- expected differential or candidate over-permission. A guideline or descriptive instruction without SHALL language does not satisfy this criterion even if the resulting output happens to include a differential comparison. |
| C-17 | **Skill-level threat model in CONTEXT** -- The CONTEXT or preamble section names failure modes for the skill as a whole -- not per-phase failure modes but the systemic gaps that permissions-tracing analysis is prone to miss as a type of work. Examples: "FLS post-incident discovery" (permissions appear correct until a specific field read reveals a gap invisible at role level), "cumulative scope blindness" (each role scoped correctly but role combinations create over-permission), "verdict drift" (correct verdicts in early phases silently overridden when Phase 3 opens with a fresh assessment). This skill-level threat model motivates the entire trace causally rather than motivating individual phases. | structure | aspirational | The CONTEXT section (or equivalent preamble before Phase 1) names at least 2 skill-level failure modes -- failure modes for permissions tracing as a category of analysis, not failure modes for individual phases. Each named failure mode describes a concrete analytical error specific to this skill (not a generic quality concern). The presence of a FAILURE MODE MAP satisfying C-15 does not automatically satisfy C-17 -- C-17 requires skill-level failures named in CONTEXT that explain why the skill as a whole is structured the way it is. |

---

## v4 Change Log

Three new aspirational criteria extracted from Round 3 excellence signals (V-05, full combination variant):

- **C-15** (pre-phase failure mode catalog): V-05 placed a FAILURE MODE MAP as a named structural element before Phase 1. This is categorically different from V-02's inline failure mode annotations (C-14). V-02 discovers failure mode motivation as it goes -- each phase annotation is encountered when that phase is reached. V-05's catalog is present before any analysis begins, giving the model the complete structural threat model upfront. The failure mode it prevents: structural omissions that are undetectable until the phase that should have caught them is already complete. A model that skips or collapses Phase 2 in V-02 loses Phase 2's failure mode annotation; in V-05, that omission is visible in the catalog before Phase 2 even begins.

- **C-16** (SHALL-level enforcement for cross-role differential): The entire V-04 to V-05 gap (1.25 pts) is C-10. Both variants satisfy C-13 and C-14; V-05 alone reaches 105.0 on v3. The differentiating mechanism is SHALL language in V-05: "SHALL compare access differentials across all roles in the Role Catalog; SHALL state whether each differential is expected given role purpose or SHALL flag as candidate over-permission." V-04 produces a cross-role comparison as an emergent property of its matrix -- the data is there, the comparison is derivable, but it is not structurally required. The PARTIAL/PASS boundary for C-10 is SHALL vs description. C-16 makes this enforcement mechanism an explicit scoreable criterion rather than a side-effect of other structural choices.

- **C-17** (skill-level threat model in CONTEXT): V-05 named three failure modes for the skill as a whole in its CONTEXT section -- FLS post-incident discovery, cumulative scope blindness, verdict drift -- before introducing any phase structure. These are not phase failure modes (which C-14 and C-15 govern) but failure modes for permissions tracing as a category of analysis. They motivate why the skill is structured with a verdict register, why escalation paths need a dedicated pass, and why the aggregation phase is distinct from the traversal phases. Combined with C-15's FAILURE MODE MAP, the structural choices become causally linked to named failure modes at two levels: skill-wide (CONTEXT) and phase-specific (FAILURE MODE MAP + inline). This makes both harder to collapse independently when the model optimizes for brevity.

**Why these three and not others:** V-05 scored 105.0 on v3 (C-10 PARTIAL). V-04 scored 103.75. V-01 and V-02 scored 101.25. V-03 scored 98.75. C-16 explains the V-04/V-05 gap (1.25 pts, C-10 PARTIAL vs PASS via SHALL enforcement). C-15 and C-17 explain the additional structural investment in V-05 that prevents the failure modes C-16 depends on: a model can know it SHALL compare roles but still not know which failures that comparison prevents, without a skill-level threat model (C-17) and a pre-phase catalog (C-15) to anchor it.

**Scoring change:** The aspirational tier grows from N=6 to N=9. Point allocation per criterion remains 2.5. The aspirational tier total grows from 15 to 22.5 points; the overall maximum score grows from 105 to 112.5.

---

## v3 Change Log (preserved)

Two new aspirational criteria extracted from Round 2 excellence signals (V-05, inertia framing + full integration):

- **C-13** (security state persistence / inertia framing): V-05's inertia framing treats security verdicts as persistent state that carries forward across phases. A role remains CLEARED until a finding changes it -- phases do not re-evaluate from scratch. The failure mode it prevents: the model re-entering a new phase without inherited state, causing prior findings (e.g., a Phase 2 escalation detection) to silently disappear because Phase 3 opens with a fresh assessment. This is distinct from C-11 (which governs required artifact hand-off between phases) -- C-13 governs verdict persistence, not artifact naming.

- **C-14** (failure mode enumeration): V-05 explicitly named Failure Mode 4 (gap loss at summary time) as the motivation for Phase 4's aggregator structure. This pattern -- each structural element carries a named failure mode -- makes structural choices legible and resistant to being optimized away by a model that treats them as redundant. The failure mode it prevents: structural constraints that exist for good reasons but appear optional because the reason is unstated, causing the model to skip or collapse them when output grows long or context switches.

**Why these two and not others:** V-01 scored 93.75. V-02 scored 87.5. V-03 scored 81.25. V-04 scored 100. Round 2 gaps between V-05 and the non-inertia variants are explained by C-13 and C-14.

**Scoring change:** The aspirational tier grows from N=4 to N=6. Point allocation per criterion remains 2.5. The aspirational tier total grows from 10 to 15 points; the overall maximum score grows from 100 to 105.

---

## v2 Change Log (preserved)

Two aspirational criteria extracted from Round 1 excellence signals (V-01, V-04 both scored 100):

- **C-11** (phase dependency chaining): V-01 and V-04 both structurally required prior-phase outputs as named inputs to the next phase. The failure mode it prevents: phases that appear sequential but can be completed independently, allowing the model to skip or summarize earlier phases without producing the outputs later phases depend on.
- **C-12** (inline violation sentinels): V-04 used tokens [GAP-FLS-fieldname], [SCOPE AMBIGUOUS], [UNCHECKED] at the point of discovery. The failure mode it prevents: gaps discovered during traversal that are silently dropped when the model transitions to summary mode.

The aspirational tier grew from N=2 to N=4. Point allocation per criterion decreased from 5 to 2.5, preserving the 10-point tier total.

---

## Scoring Reference

| Criteria tier | N | Points each | Max pts |
|---------------|---|-------------|---------|
| Essential | 5 | 12.0 | 60.0 |
| Recommended | 3 | 10.0 | 30.0 |
| Aspirational | 9 | 2.5 | 22.5 |
| **Total** | **17** | | **112.5** |

**Example scores:**

| Pass pattern | Composite | Golden? |
|-------------|-----------|---------|
| 5E + 3R + 9A | 112.5 | Yes |
| 5E + 3R + 6A | 105.0 | Yes |
| 5E + 3R + 4A | 100.0 | Yes |
| 5E + 3R + 2A | 95.0 | Yes |
| 5E + 3R + 0A | 90.0 | Yes |
| 5E + 2R + 9A | 102.5 | Yes |
| 5E + 2R + 4A | 90.0 | Yes |
| 5E + 2R + 0A | 80.0 | Yes (boundary) |
| 5E + 1R + 9A | 92.5 | Yes |
| 5E + 1R + 0A | 70.0 | No (composite < 80) |
| 4E + 3R + 9A | 100.5 | No (not all essential) |
| 3E + 3R + 9A | 88.5 | No (not all essential) |
"""

with open('C:/src/sim/simulations/quest/rubrics/trace-permissions-rubric-v4-2026-03-16.md', 'w') as f:
    f.write(rubric)
print('written', len(rubric), 'chars')
