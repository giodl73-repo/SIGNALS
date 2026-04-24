Written to `simulations/quest/rubrics/trace-permissions-rubric-v6-2026-03-16.md`

---

**v6 summary:**

**22 criteria, max 125.0** (up from 19 / 117.5)

Three new aspirational criteria from Round 7:

| ID | Name | Source | Failure mode prevented |
|----|------|--------|----------------------|
| **C-20** | Structural enforcement of layer-override explanation | C-09 PARTIAL (all three R7 variants, same gap) | C-09 is satisfied by naming the effective enforcement layer; the model can omit the "why upper layers don't override" reasoning entirely because no required table column demands it -- the reasoning gap is invisible until a downstream finding contradicts it |
| **C-21** | Complete phase dependency graph | V-03 full 5-phase C-11 + C-18 chain | A partial chain (C-11 / C-18 at "at least two consecutive phases") leaves boundary phases as orphans -- Phase 1's output is undeclared (scope inflation undetectable) and the final analysis phase's handoff to aggregation is unenforced (scope truncation undetectable at exactly the transition where gap loss concentrates) |
| **C-22** | Coverage gate before aggregation | V-03 Phase 4 COVERAGE GATE CONFIRMATION | A prompt with routing rules (C-19) and a complete phase chain (C-21) still permits partial analysis to advance to remediation -- without a structural count-check between the final analysis phase and the gap inventory phase, a short analysis looks identical to a complete one |

**Distinction chain for the three new criteria and their structural predecessors:**
- **C-09 + C-20** -- effective layer identification (which layer enforces) + layer-override explanation (why upper layers are overridden). C-20 is the mechanism that makes C-09's "explains why upper layers do not override it" structurally required rather than prose-prompted.
- **C-11 + C-18 + C-21** -- input declaration (consuming phase) + output declaration (producing phase) + complete chain (every phase, no orphans). C-21 is the end-state when C-11 and C-18 are both satisfied at every phase boundary.
- **C-19 + C-22** -- routing rules (discoveries must reach the register) + coverage gate (counts confirm all discoveries were registered before aggregation closes). C-22 is the verification layer that detects when C-19's routing was applied to an incomplete analysis.

The R7 C-09 PARTIAL evidence is the diagnostic: all three variants produce the 4-layer table with Effective Enforcement Layer column (satisfying C-09's pass condition) but the "why upper layers do not override" explanation is present only as a prose instruction, never as a required column in the table. Every model that passes C-09 without C-20 is technically compliant while leaving the causal reasoning untested. The precedent is exact: C-10 identifies the cross-role differential (content requirement); C-16 adds SHALL language (structural enforcement). C-09 identifies the defense-in-depth layering (content requirement); C-20 adds a required explanation column (structural enforcement).

**Scoring change:** Aspirational tier N=11->14, tier total 27.5->35 pts, overall max 117.5->**125.0**.

---

## What changed from v4 to v5

| ID | Name | Source signal | What it captures |
|----|------|---------------|-----------------|
| **C-18** | Named phase exit gate artifacts | V-01 C-11 PASS; V-03 exit gates | The output side of the C-11 contract -- the producing phase declares its artifact with a labeled schema before the consuming phase can reference it by name |
| **C-19** | Aggregation routing rules | V-02 cross-table routing ("Any FLS Gap = YES row MUST appear in Table 4") | Explicit routing rules close the loop between discovery mechanism and aggregation destination; without them C-12 sentinels accumulate at discovery but are not structurally guaranteed to reach the gap inventory |

**Scoring change:** Aspirational tier N=9->11, tier total 22.5->27.5 pts, overall max 112.5->117.5.

---

## Essential Criteria (60 points total, N=5)

All five must pass. Failing any essential criterion disqualifies the output regardless of other scores.

| ID | Text | Category | Weight | Pass Condition |
|----|------|----------|--------|----------------|
| C-01 | **Role enumeration with BU scope** -- The output identifies every role in scope, including the BU scope level (user / BU / child BUs / org-wide), operations each role can perform on the target table, and any team assignments or column security profiles attached. | coverage | essential | Role name, BU scope level, at least one operation, and any column security profile present for each in-scope role. Missing BU scope or operations for any role is a FAIL. |
| C-02 | **Field visibility per role** -- For each in-scope role and each operation that role can perform, the output states which fields are visible (readable or writable) given the combination of security role privileges and any column security profiles in effect. | coverage | essential | Field visibility stated per role per operation for at least the sensitive fields in scope. A role-operation combination not evaluated is a FAIL unless the operation is inapplicable (and the inapplicability is stated). |
| C-03 | **Record scope assessment** -- The output evaluates whether each role's BU scope is appropriate for the role's stated purpose, or whether the assigned scope is over-permissioned relative to that purpose. | correctness | essential | For at least one role, the output evaluates whether the assigned scope is appropriate or over-permissioned relative to the stated purpose. |
| C-04 | **Escalation path detection** -- The output identifies at least one privilege escalation path (e.g., team membership granting broader role, sharing rule bypassing FLS, environment-level admin override) or explicitly concludes none were found after checking the known vectors. | correctness | essential | Section or finding dedicated to escalation paths. A conclusion of none found is acceptable only if each known vector (team inheritance, sharing rules, impersonation, admin roles) was checked and ruled out individually. |
| C-05 | **Security gap inventory** -- The output produces a named list of gaps: missing FLS on sensitive fields, team membership holes, sharing rule conflicts, or over-permissioned roles. | coverage | essential | At least one gap named with a specific field, role, or rule. If no gaps exist, explicit evidence provided (e.g., all sensitive fields have FLS configured) rather than a bare assertion. |

---

## Recommended Criteria (30 points total, N=3)

Output is better with these. Failing one degrades usefulness but does not disqualify.

| ID | Text | Category | Weight | Pass Condition |
|----|------|----------|--------|----------------|
| C-06 | **Dataverse-native terminology** -- The output uses correct Dataverse security constructs: business units, security roles, team types (owner vs. access), table permissions, column security profiles, sharing records, environment roles. No generic RBAC language substituted where Dataverse terms apply. | correctness | recommended | At least 4 Dataverse-specific terms appear and are used accurately. Generic terms like group or permission level used without Dataverse mapping are treated as imprecision. |
| C-07 | **Sharing rule conflict analysis** -- The output checks whether sharing rules (manual, team-based, or via Power Automate) conflict with role-level access -- granting access that roles deny, or denying access that FLS permits. | depth | recommended | At least one sharing scenario evaluated for conflict. A conclusion of no conflicts requires checking at least the intersection of one sharing rule with one FLS column profile. |
| C-08 | **Remediation specificity** -- For each identified gap, the output provides a specific, actionable remediation: which column security profile to create, which role privilege to tighten, which team assignment to add or remove. | behavior | recommended | At least 50% of named gaps have a specific remediation step (not just "add FLS" but "create column security profile on creditlimit, restrict to Sales Manager role"). Generic advice without naming the exact configuration object fails. |

---

## Aspirational Criteria (35.0 points total, N=14)

These raise the bar once essential and recommended are stable.

| ID | Text | Category | Weight | Pass Condition |
|----|------|----------|--------|----------------|
| C-09 | **Defense-in-depth layering** -- The output evaluates security at all four Dataverse layers in sequence: (1) environment/admin role, (2) security role + BU scope, (3) team membership, (4) field-level security/column profiles. It identifies which layer is the effective enforcement point for each operation. | depth | aspirational | All four layers named and assessed. For at least one operation, the output identifies the specific layer where access is granted or denied and explains why upper layers do not override it. |
| C-10 | **Cross-role differential analysis** -- The output compares access across two or more roles for the same operation and field set, surfacing where roles diverge and whether that divergence is intentional (principle of least privilege satisfied) or anomalous. | depth | aspirational | At least two roles compared side-by-side on at least one operation. The analysis states whether the access differential is expected given the roles' described purposes, or flags it as a candidate over-permission. |
| C-11 | **Phase dependency chaining** -- Each analytical phase or pass explicitly declares what it requires from prior phases as named inputs. Phase N+1 cannot proceed without the named outputs of Phase N. The prompt structurally enforces sequence rather than relying on the model to volunteer it. | structure | aspirational | At least two consecutive phases name their dependency relationship explicitly. Dependency names must match actual output labels from the prior phase (e.g., "the role list from Pass 1", "Role A escalation verdict") -- generic references like "the above" do not qualify. |
| C-12 | **Inline violation sentinels** -- When the analysis discovers a violation, ambiguity, or unchecked state during the trace, the output places a named sentinel token at that point -- e.g., [GAP-FLS-fieldname], [SCOPE AMBIGUOUS], [UNCHECKED]. Sentinels accumulate into the gap inventory rather than being invented at summary time. | structure | aspirational | At least two distinct sentinel types used. Each sentinel placed at the point of discovery, not retroactively inserted into the gap section. The gap inventory (C-05) references or aggregates sentinels from the trace body rather than re-stating findings independently. |
| C-13 | **Security state persistence (inertia framing)** -- Security verdicts assigned to a role in one phase carry forward as the persistent default into subsequent phases. A role that is CLEARED in Phase 2 remains CLEARED in Phase 3 unless Phase 3 produces a finding that explicitly overrides it. Phases do not reset role state to unknown; they inherit and either confirm or amend prior verdicts. | structure | aspirational | At least one role verdict carries forward across two consecutive phases with explicit continuity language -- e.g., "CLEARED from Phase 2, no change" or "Phase 3 finding overrides Phase 2 CLEARED verdict". A phase that re-issues a verdict without referencing prior-phase state fails, even if the new verdict happens to be correct. |
| C-14 | **Failure mode enumeration** -- The prompt names the specific failure mode that each structural element (phase, pass, sentinel type, or aggregation rule) defends against. Example: "Phase 4 is structured as an aggregator because Failure Mode 4 is gap loss during model transition from traversal to summary." The structural choice is legible and testable. | structure | aspirational | At least two structural elements carry an associated named failure mode. Each failure mode names the specific analytical error prevented -- not a generic quality concern but a concrete failure path (e.g., "prevents model from skipping Phase 2 when role list is short"). |
| C-15 | **Pre-phase failure mode catalog** -- Before Phase 1 begins, the prompt includes a named structural element (e.g., FAILURE MODE MAP, structural threat model) that lists every failure mode the subsequent phases defend against. Distinct from C-14 (inline annotation at each phase) -- C-15 requires the complete catalog upfront, making structural omission detectable before analysis begins rather than discoverable phase-by-phase. | structure | aspirational | A named pre-phase structural element (appearing before Phase 1 instructions) lists at least 3 named failure modes. Each entry maps to at least one subsequent phase, gate, or structural construct. A phase-by-phase annotation pattern does not satisfy this criterion -- the catalog must precede Phase 1. |
| C-16 | **SHALL-level enforcement for cross-role differential** -- The prompt uses SHALL/SHALL NOT language to structurally require cross-role differential analysis. Not "compare roles where relevant" but an explicit SHALL instruction naming the comparison, the conclusion required (expected differential vs. candidate over-permission), and the disposition for each case. This is the mechanism that elevates C-10 from emergent-PARTIAL to enforced-PASS. | structure | aspirational | At least one SHALL-level instruction explicitly requires cross-role differential comparison by name. The instruction must require both (a) performing the comparison across named roles and (b) stating an explicit conclusion for each pair -- expected differential or candidate over-permission. A guideline or descriptive instruction without SHALL language does not satisfy this criterion. |
| C-17 | **Skill-level threat model in CONTEXT** -- The CONTEXT or preamble section names failure modes for the skill as a whole -- not per-phase failure modes but systemic gaps that permissions-tracing analysis is prone to miss as a type of work. Examples: "FLS post-incident discovery", "cumulative scope blindness", "verdict drift". This skill-level threat model motivates the entire trace causally rather than motivating individual phases. | structure | aspirational | The CONTEXT section (or equivalent preamble before Phase 1) names at least 2 skill-level failure modes -- failure modes for permissions tracing as a category of analysis, not failure modes for individual phases. Each named failure mode describes a concrete analytical error specific to this skill. The presence of a FAILURE MODE MAP satisfying C-15 does not automatically satisfy C-17. |
| C-18 | **Named phase exit gate artifacts** -- Each analytical phase declares its output as a named artifact with a labeled schema before that artifact is referenced by downstream phases. Example: "This phase produces: ROLE CATALOG (role name | BU scope | owner teams | access teams | admin role flag)." The declared artifact name becomes the canonical token for downstream C-11 input declarations. Without declared output schemas, C-11 input references are accidental name matches rather than enforced contracts. | structure | aspirational | At least two phases declare a named output artifact with a labeled schema (field names, column headers, or equivalent). The declared artifact name must match the reference token used in at least one downstream phase's input declaration (C-11). An implicit naming convention (e.g., "the output from Phase 1" or an unnamed table) does not satisfy this criterion. |
| C-19 | **Aggregation routing rules** -- The prompt includes at least one explicit routing rule that guarantees discoveries from traversal phases reach the aggregation or gap inventory destination, preventing gap loss at the phase transition boundary. Example: "Any row with FLS Gap = YES MUST appear in Table 4 with no omission" or "Any [GAP-FLS-*] sentinel placed during Phase 2 MUST be referenced in the Phase 4 gap inventory." Distinct from C-12 (sentinels placed at discovery) -- C-19 closes the loop between discovery mechanism and aggregation target. | structure | aspirational | At least one named routing rule present. The rule must reference both (a) the discovery mechanism (sentinel token, row flag, phase output type) and (b) the aggregation destination (gap register, inventory table, or equivalent) by name. A general completeness instruction like "produce a complete gap list" does not satisfy this criterion. |
| C-20 | **Structural enforcement of layer-override explanation** -- The defense-in-depth table (C-09) includes a dedicated column or required labeled field for the explanation of why upper layers do not override the effective enforcement layer -- not a prose instruction to explain, but a table cell that is required for every operation or role-operation combination evaluated. This is the mechanism that elevates C-09 from prose-prompted to structurally enforced: the same role C-16 plays for C-10. | structure | aspirational | The defense-in-depth table includes a named column or labeled field (e.g., "Why Not Overridden", "Layer Override Reasoning", "Upper-Layer Disposition") requiring an explanation for at least every operation where the effective layer is not the outermost layer. A prose instruction to explain (e.g., "explain why upper layers do not override") without a corresponding required table field does not satisfy this criterion. For at least one operation, the explanation field contains a non-generic justification naming the specific override mechanism (e.g., "Environment Admin not assigned; BU scope is the outermost active constraint"). |
| C-21 | **Complete phase dependency graph** -- Every phase in the analysis has both (a) a named exit gate artifact declaration with labeled schema satisfying C-18 and (b) input declarations naming the exact artifacts from all prior phases it depends on satisfying C-11. No phase is an analytical orphan. The first phase declares its output; every intermediate phase declares its inputs and its output; the final phase declares its inputs. The full chain is traceable end-to-end without gaps at any phase boundary. | structure | aspirational | Every phase (all phases, not just two consecutive) declares at least one named output artifact with a labeled schema, and every phase except the first declares its named input dependencies matching prior-phase exit gate labels. A chain with any orphan phase -- a phase that receives no declared inputs or produces no declared output -- does not satisfy this criterion. A complete 3-phase chain (Phase 1 output declared; Phase 2 input + output declared; Phase 3 input declared) is the minimum. |
| C-22 | **Coverage gate before aggregation** -- A dedicated coverage gate phase or structural element appears between the final analysis phase and the gap aggregation or remediation phase. The gate verifies completeness by comparing discovered findings to registered gap identifiers: the count of issues discovered during traversal must equal the count of identifiers assigned in the gap register before aggregation is allowed to proceed. The gate's output is a named artifact (e.g., COVERAGE GATE CONFIRMATION, COMPLETENESS CHECK) that the aggregation phase explicitly requires as a C-11-compliant input. Without this gate, a partial analysis is structurally indistinguishable from a complete one at the point of aggregation. | structure | aspirational | A named coverage gate element appears before the gap aggregation or remediation phase. The gate must: (a) compare a count from traversal (total findings discovered or entities processed) against a count from the gap register (total gap identifiers assigned); (b) produce a named pass/fail or count-match output; and (c) have that output declared as an input dependency by the aggregation or remediation phase. A routing rule (C-19) without an explicit count-comparison step does not satisfy this criterion. |

---

## v6 Change Log

Three new aspirational criteria extracted from Round 7 scorecard excellence signals (V-01, V-02, V-03):

- **C-20** (structural enforcement of layer-override explanation): The R7 diagnostic is C-09 PARTIAL across all three variants with identical evidence -- the defense-in-depth table has 4 layers plus an Effective Enforcement Layer column (satisfying C-09) but the "why upper layers do not override" reasoning is present only as a prose instruction, never as a required table field. All three prompts instruct the model to explain; none require it structurally. A model that identifies the correct effective layer passes C-09 without ever justifying the layer assignment. C-20 is the structural mechanism that closes this gap: a dedicated table column whose presence demands a per-row justification. The precedent is exact: C-10 identifies the cross-role differential (content requirement); C-16 adds SHALL language (structural enforcement). C-09 identifies the defense-in-depth layering (content requirement); C-20 adds a required explanation column (structural enforcement). Failure mode C-20 prevents: the model selects the effective enforcement layer correctly but omits the reasoning that would catch a wrong selection -- an incorrect assignment passes C-09 silently unless the explanation is structurally required.

- **C-21** (complete phase dependency graph): V-01 achieves two named dependency pairs (Pass 1 output -> Pass 2 input; Pass 2 output -> Pass 3 input), satisfying C-11 and C-18 at "at least two consecutive phases." V-03 achieves five consecutive phase pairs, every phase boundary closed. The R7 scorecard reveals that a partial chain leaves specific failure modes unaddressed: Phase 1 with no declared output (scope inflation undetectable -- the phase can silently over-collect or under-collect before handing off) and the final analysis phase with no declared output (scope truncation undetectable -- the phase can silently drop findings before aggregation). These are the boundaries where the most consequential errors concentrate. C-21 is not a stronger version of C-11 or C-18; it is the end-state when both are applied uniformly. The three criteria form a progression: C-11 (at least two inputs declared), C-18 (at least two outputs declared), C-21 (all inputs and all outputs declared, no orphan phases). Failure mode C-21 prevents: the partial chain that satisfies C-11 and C-18 while leaving boundary phases structurally unconnected, making scope errors at entry and exit unverifiable.

- **C-22** (coverage gate before aggregation): V-03 introduces a Phase 4 COVERAGE GATE CONFIRMATION between the analysis phases (2 and 3) and the gap aggregation phase (5). The gate counts findings-discovered against identifiers-assigned and requires a match before Phase 5 may proceed. This is structurally distinct from C-19's routing rules and C-21's complete phase chain: a prompt can have named routing rules and a complete phase chain while still allowing Phase 5 to aggregate from an analysis that processed only three of six entities -- because neither routing rules nor phase chaining check completeness, they only check that what was found was routed correctly. The coverage gate is the only structural element that catches the case where the analysis itself was partial. Failure mode C-22 prevents: a prompt that correctly routes all discovered gaps (C-19) and correctly declares all phase handoffs (C-21) but allows the model to complete Phase 3 having evaluated 3 of 6 entities -- the gap register is internally consistent, all routing rules were followed, but the analysis missed half the scope.

**Why these three and not others:** The R7 scorecards are primarily testing C-18 (V-01), C-19 (V-02), and C-18+C-19 together (V-03). The new signals come from (1) the consistent C-09 PARTIAL pattern revealing a gap in C-09's structural depth, (2) V-03's complete chain exceeding what C-11 and C-18 individually require, and (3) V-03's coverage gate phase introducing a completeness verification step not captured by routing rules alone. C-12, C-13, C-14, C-15, C-16, and C-17 all FAIL across all three variants with no new structural signals -- they remain targets for future rounds.

**Scoring change:** Aspirational tier grows from N=11 to N=14. Tier total grows from 27.5 to 35.0 points; overall maximum grows from 117.5 to 125.0.

---

## v5 Change Log (preserved)

- **C-18** (named phase exit gate artifacts): The output side of the C-11 contract -- the producing phase declares its artifact with a labeled schema that makes naming possible. Without C-18, a C-11 PASS is structurally fragile: an accidental name match rather than an enforced contract.

- **C-19** (aggregation routing rules): V-02 included cross-table routing rules correctly scored as C-11 PARTIAL but identified as a real structural mechanism not addressed by C-11 or C-12. C-12 requires sentinels at discovery; C-19 requires the prompt to explicitly route those discoveries to the aggregation destination.

**Scoring change:** Aspirational tier N=9->11, tier total 22.5->27.5 pts, overall max 112.5->117.5.

---

## v4 Change Log (preserved)

- **C-15** (pre-phase failure mode catalog): V-05 placed a FAILURE MODE MAP before Phase 1. Failure mode prevented: structural omissions undetectable until the phase that should have caught them is already complete.
- **C-16** (SHALL-level enforcement for cross-role differential): SHALL language makes cross-role comparison structurally required. V-04 produces it emergently; V-05 enforces it.
- **C-17** (skill-level threat model in CONTEXT): V-05 named three failure modes for the skill as a whole -- FLS post-incident discovery, cumulative scope blindness, verdict drift.

**Scoring change:** Aspirational tier N=6->9, tier total 15->22.5 pts, overall max 105->112.5.

---

## v3 Change Log (preserved)

- **C-13** (security state persistence / inertia framing): Verdicts carry forward as persistent state.
- **C-14** (failure mode enumeration): Each structural element carries a named failure mode.

**Scoring change:** Aspirational tier N=4->6, tier total 10->15 pts, overall max 100->105.

---

## v2 Change Log (preserved)

- **C-11** (phase dependency chaining): Prior-phase outputs required as named inputs.
- **C-12** (inline violation sentinels): Tokens placed at discovery, not invented at summary.

Aspirational tier grew from N=2 to N=4. Point allocation decreased from 5 to 2.5, preserving the 10-point tier total.

---

## Scoring Reference

| Criteria tier | N | Points each | Max pts |
|---------------|---|-------------|---------|
| Essential | 5 | 12.0 | 60.0 |
| Recommended | 3 | 10.0 | 30.0 |
| Aspirational | 14 | 2.5 | 35.0 |
| **Total** | **22** | | **125.0** |

**Example scores:**

| Pass pattern | Composite | Golden? |
|-------------|-----------|---------|
| 5E + 3R + 14A | 125.0 | Yes |
| 5E + 3R + 11A | 117.5 | Yes |
| 5E + 3R + 9A | 112.5 | Yes |
| 5E + 3R + 6A | 105.0 | Yes |
| 5E + 3R + 4A | 100.0 | Yes |
| 5E + 3R + 2A | 95.0 | Yes |
| 5E + 3R + 0A | 90.0 | Yes |
| 5E + 2R + 14A | 115.0 | Yes |
| 5E + 2R + 4A | 90.0 | Yes |
| 5E + 2R + 0A | 80.0 | Yes (boundary) |
| 5E + 1R + 14A | 105.0 | Yes |
| 5E + 1R + 0A | 70.0 | No (composite < 80) |
| 4E + 3R + 14A | 113.0 | No (not all essential) |
| 3E + 3R + 14A | 101.0 | No (not all essential) |
