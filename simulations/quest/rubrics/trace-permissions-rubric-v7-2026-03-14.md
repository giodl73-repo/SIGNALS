Reading the scorecard to extract the excellence patterns before writing the rubric.

The scorecard commentary on V-03 surfaces three structural patterns that exceed existing criteria:

1. **Multi-condition gate checklists** — V-03's gates use per-criterion □ checklists with "assert only when ALL conditions satisfied." Described as "strongest C-14 implementation." C-14 requires a visible marker; this embeds criterion-level verification into the gate itself.

2. **Source-locked gap inventory** — V-03's inventory format includes `"first seen: [TABLE X, row Y]"` at commit time. C-16 requires the inventory to exist; this binds source provenance into the inventory record so Phase 4 can verify without back-tracing.

3. **Origin-classified TABLE 7** — V-03 adds a dedicated "Phase 2 Origin?" column to TABLE 7. C-20 requires the four-location chain to exist; this makes origin classification a first-class column, mechanically separable from prose Justification. Described as the third of three independent C-20 checkpoints.

Three new criteria: **C-21** (multi-condition gate checklists), **C-22** (source-locked gap inventory), **C-23** (origin-classified summary table).

---

```markdown
# Rubric: trace-permissions (v7)

Evaluates the quality of a permissions trace output — a structured analysis of which roles can
perform which operations, what field- and record-level access controls apply, and where gaps or
misconfigurations exist.

---

## Essential Criteria (60 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Role-Operation Matrix** | correctness | essential | For each security role, output maps to each relevant operation (Create, Read, Update, Delete, and any domain-specific operations such as Assign or Share). Output shows which role can perform which operation. Listing roles without tying them to operations does not pass. |
| C-02 | **Field-Level Security Named Per Role** | correctness | essential | For any role whose field access differs from default, output names specific fields and specific allow/deny configurations for that role. Statements such as "FLS should be configured" or "FLS applies" without naming specific fields and specific roles does not pass. |
| C-03 | **Record Access Scope** | correctness | essential | For each role, output states the access scope: Own / Business Unit / Parent BU / Organization (or equivalent RBAC scope). Must not conflate role privileges with record ownership. |
| C-04 | **At Least One Security Gap Identified** | coverage | essential | Output explicitly names at least one missing or misconfigured security control -- a missing FLS restriction, an over-permissive role, a sharing rule conflict, or a team membership gap. Describing the model without surfacing a problem does not pass. |

---

## Recommended Criteria (30 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-05 | **Privilege Escalation Path Analysis** | depth | recommended | Output identifies at least one plausible privilege escalation path -- e.g., a user in Role A who can reassign records to gain Role B scope, or a team membership that grants unintended org-wide access. Must name the path, not just assert it exists. |
| C-06 | **Sharing Rule Conflict Detection** | depth | recommended | Output examines sharing rules (manual, criteria-based, or owner-based) and identifies at least one case where a sharing rule widens access beyond the security role baseline, or a case where sharing rules create contradictory access grants. |
| C-07 | **Team Membership Gap** | coverage | recommended | Output identifies at least one scenario where team membership creates a gap -- either a user not on the expected team who loses access, or a user on multiple teams whose combined permissions exceed intent. |

---

## Aspirational Criteria (80 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-08 | **Risk-Ranked Gap Summary** | depth | aspirational | Output concludes with a ranked list of identified gaps ordered by risk severity (High / Medium / Low), with a one-line justification per gap. Ranking must be defensible relative to the operation and data sensitivity described. |
| C-09 | **Remediation Recommendation Per Gap** | behavior | aspirational | For each gap identified, output provides a concrete remediation action (e.g., "add FLS read-deny on AccountNumber for Customer Service role", "remove team-level sharing rule that grants org-wide read"). Vague guidance ("tighten security") does not pass. |
| C-10 | **Hypothesis Pre-commitment** | depth | aspirational | Before tracing, output states at least two expected security gaps as explicit hypotheses. Findings section addresses each hypothesis by name -- confirmed, refuted, or modified with evidence. Outputs that surface gaps without pre-committed hypotheses do not pass, even if the gaps are correct. |
| C-11 | **Null-Finding Accountability** | behavior | aspirational | For any recommended section where no gap is found, output names the specific controls examined and provides a one-sentence justification for the null result. "None identified" alone does not pass. |
| C-12 | **Four-Vector Escalation Sweep** | depth | aspirational | Privilege escalation analysis covers all four standard vectors: (1) record reassignment, (2) team promotion or membership elevation, (3) sharing rule bypass, and (4) impersonation or delegation. Each is either named or explicitly cleared. Identifying one path without checking the remaining vectors does not pass. |
| C-13 | **Hypothesis-Anchored Evidence Tables** | depth | aspirational | Evidence tables (role-operation matrix, FLS table, record scope table) include an H-flag column that ties each row to a specific pre-committed hypothesis by identifier (H1, H2, etc.) or marks it N/A. Findings section resolves each hypothesis by referencing the specific table rows that confirmed, refuted, or modified it. A hypothesis section connected to findings only by prose, with no table-level tracing, does not pass. |
| C-14 | **Explicit Phase Completion Gate** | behavior | aspirational | Output includes at least one explicit phase completion marker (e.g., "PHASE 1 COMPLETE") asserted after each major section -- hypothesis, evidence, findings, summary -- before the next section begins. The marker is a visible state transition the output must take, not a section header. Outputs that execute all sections without asserting any completion marker, or that place a marker before the section content is complete, do not pass. |
| C-15 | **Gap Provenance Enforcement** | behavior | aspirational | Every gap appearing in the final risk-ranked summary must trace to a specific evidence table and row from the analysis phases. No gap may be introduced in the summary or findings section that was not first recorded in a Phase 2 or Phase 3 evidence table. An output that surfaces additional gaps only in Phase 4 -- even correct and well-justified ones -- does not pass. The summary is a consolidation operation, not a new analysis layer. |
| C-16 | **Gate-Level Gap Inventory** | behavior | aspirational | Before the Phase 3 COMPLETE marker, output commits an explicit inventory of all gap identifiers discovered in Phase 2 and Phase 3 evidence tables. Phase 4 may not introduce a gap identifier absent from this inventory. The gate operates at section-transition granularity, complementary to C-15's cell-level source citation. An output that prohibits new Phase 4 gaps by rule alone -- without a committed inventory block before Phase 3 closes -- does not pass. Prohibition without inventory is not gate-level provenance. |
| C-17 | **Gap ID Threading** | depth | aspirational | Each gap identified in Phase 2 or Phase 3 evidence tables is assigned a persistent identifier (e.g., G-01, G-02) at first occurrence. The identifier appears unchanged in the findings section and in the risk-ranked summary, linking all three phases by the same key. A summary that references gaps by description alone, requiring prose matching to determine provenance, does not pass. Gap ID threading makes any spurious gap introduced in Phase 4 mechanically detectable by inspection -- the identifier will be absent from the Phase 3 inventory. |
| C-18 | **Inertia Column Framing** | depth | aspirational | At least two of the analytical evidence tables (privilege escalation table, sharing rule table, team membership table, or FLS table) include at least one inertia column that asks a counterfactual question per row: what would break if this access were removed, what change would open this escalation path, or what condition triggers this conflict. The inertia column must be populated for at least one row in each qualifying table -- a header with no values does not pass. Outputs that enumerate access controls without surfacing counterfactual pressure on at least two tables do not pass. |
| C-19 | **Phase 2 Inertia Extension** | depth | aspirational | At least one Phase 2 analytical table (FLS table or record scope table) includes an inertia column asking a counterfactual question per row: what would break if this field restriction were removed, what change would widen this access scope, or what condition would expose this field to an unauthorized role. The inertia column must be populated for at least one row. This criterion is satisfied independently of C-18 -- an output that satisfies C-18 using only Phase 3 tables does not satisfy C-19. Phase 2 inertia surfaces counterfactual pressure on field-level and scope decisions before the escalation analysis begins, making structural vulnerabilities visible at the point of discovery rather than only at the remediation layer. |
| C-20 | **Full-Chain Gap ID Provenance** | depth | aspirational | For any gap first identified in a Phase 2 evidence table (FLS table or record scope table), the same persistent identifier must appear in all four locations: (1) Phase 2 table row at first occurrence, (2) Phase 3 analytical table referencing or carrying the gap forward, (3) Phase 3 inventory block committed before the Phase 3 COMPLETE marker (C-16), and (4) Phase 4 risk-ranked summary (Table 7). An output that assigns Gap IDs only at Phase 3 satisfies C-17 but does not satisfy C-20. Full-chain provenance makes Phase 2-origin gaps -- FLS anomalies, scope violations -- mechanically traceable by identifier from discovery through summary. A Phase 2 gap that is re-introduced by description in Phase 4 without its original identifier does not pass, even if the description matches. |
| C-21 | **Multi-Condition Gate Checklists** | behavior | aspirational | Each phase completion gate (C-14) is structured as an explicit multi-condition checklist with one □-prefixed condition per verifiable output requirement -- e.g., inertia columns populated, gap IDs assigned, hypothesis resolutions present. The gate assertion appears only after all checklist conditions are listed and satisfiable by inspection. An output that uses a single-line "PHASE X COMPLETE" marker satisfies C-14 but does not satisfy C-21. Multi-condition gates embed criterion-level verification at phase boundaries, making structural gaps detectable before the next phase begins rather than only in retrospective review. A gate with only one condition, or a checklist whose conditions do not map to specific verifiable output properties, does not pass. |
| C-22 | **Source-Locked Gap Inventory** | behavior | aspirational | Each entry in the Phase 3 gap inventory (C-16) includes the source table name and row identifier at inventory commit time, in the form "[G-ID] -- [description] -- first seen: [TABLE X, row Y]". The source binding is part of the inventory record itself, not recoverable only by back-tracing through Phase 2 and Phase 3 tables after the fact. An inventory that lists gap identifiers and descriptions without source-locking satisfies C-16 but does not satisfy C-22. Source locking at commit time means Phase 4 can verify provenance from the inventory alone; a Phase 4 reviewer does not need to re-scan all evidence tables to confirm where a gap originated. An inventory entry that omits the source table or names only a phase without a specific table and row does not pass. |
| C-23 | **Origin-Classified Summary Table** | depth | aspirational | The Phase 4 risk-ranked summary table (C-08) includes a dedicated Phase Origin column that classifies each gap as Phase 2-origin or Phase 3-origin. For each gap classified as Phase 2-origin, the column value confirms the four-location chain inline -- not in the prose Justification column. An output that satisfies C-20 by confirming the chain only in the Justification column, without a dedicated Origin column, does not satisfy C-23. Origin classification as a first-class column makes Phase 2-origin gaps structurally distinguishable from Phase 3-origin gaps by table inspection, without reading prose. A summary table that omits the column, or that places origin information in Justification only, does not pass regardless of C-20 compliance. |

---

## Scoring Table

| Tier | Criteria | Max Points | Points Per Criterion |
|------|----------|------------|----------------------|
| Essential | C-01 -- C-04 | 60 | 15 each |
| Recommended | C-05 -- C-07 | 30 | 10 each |
| Aspirational | C-08 -- C-23 | 80 | 5 each |
| **Total** | | **170** | |

---

**What changed from v6:**

| Change | Source |
|--------|--------|
| C-21 Multi-Condition Gate Checklists | V-03 strongest C-14 implementation: phase gates structured as per-criterion □ checklists with assertion conditional on ALL conditions satisfied; single-line "PHASE X COMPLETE" satisfies C-14 but not C-21; embeds criterion-level verification at phase boundaries |
| C-22 Source-Locked Gap Inventory | V-03 strongest C-20 implementation (checkpoint 1 of 3): gap inventory format includes "first seen: [TABLE X, row Y]" at commit time, binding source provenance into the inventory record; C-16 requires the inventory to exist but does not specify format; source locking allows Phase 4 provenance verification from the inventory alone |
| C-23 Origin-Classified Summary Table | V-03 strongest C-20 implementation (checkpoint 3 of 3): TABLE 7 dedicated Phase 2 Origin column classifies each gap by origin phase and confirms four-location chain inline as a column value; C-20 requires the chain to exist but can be satisfied via Justification prose; a dedicated column makes origin classification structurally first-class and inspectable without reading prose |
| Aspirational ceiling raised from 65 to 80 pts | Three new criteria at 5 pts each |
| Total ceiling raised from 155 to 170 | |
```
