Reading the scorecard tiebreaker block — that's where Round 7's new excellence signals live, beyond what C-21/22/23 already captured.

Three patterns:

1. **V-05** — H-connection as fourth inventory field: gap inventory entries carry `(H1/H2)` binding, making C-13 and C-20 jointly verifiable from the inventory block alone.
2. **V-01** — Forward compliance assembly: origin tagging at discovery makes Phase 4 classification a read, not a write — eliminates the V-02 error class structurally.
3. **V-03** — ~40% compression with zero criterion loss: proves structural elements were load-bearing, not decorative framing for prose.

These become C-24, C-25, C-26.

---

```markdown
# Rubric: trace-permissions (v8)

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

## Aspirational Criteria (95 points total)

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
| C-24 | **Hypothesis-Bound Gap Inventory** | behavior | aspirational | Each entry in the Phase 3 gap inventory (C-16) includes a hypothesis binding field indicating which pre-committed hypothesis the gap belongs to or was discovered against, in the form "[G-ID] -- [description] -- first seen: [TABLE X, row Y] -- (H-NN)" or "(H-NN/H-MM)" for gaps that bear on multiple hypotheses. The binding is part of the inventory record itself, not recoverable only by cross-referencing the findings section. An inventory that lists gap identifiers, descriptions, and source tables (C-22) without hypothesis bindings satisfies C-22 but does not satisfy C-24. Hypothesis binding at inventory commit time makes C-13 (hypothesis-anchored tables) and C-20 (full-chain provenance) jointly verifiable from the inventory block alone -- a Phase 4 reviewer can confirm both the structural origin and the hypothesis connection without re-scanning Phase 2 and Phase 3 evidence tables. An inventory entry that omits hypothesis binding, or binds only to a phase without a specific hypothesis identifier, does not pass. |
| C-25 | **Forward Origin Classification** | behavior | aspirational | Origin classification (C-23) is applied at first occurrence: each Phase 2 gap is tagged as Phase 2-origin at the point it is recorded in the Phase 2 evidence table, not retroactively assigned in Phase 4. Phase 3 tables that carry a Phase 2 gap forward preserve the origin tag. The Phase 4 summary table reads origin classification from the upstream record; it does not compute it. An output that satisfies C-23 by deriving origin in Phase 4 from the gap inventory or by back-inferring from table positions satisfies C-23 but does not satisfy C-25. Forward classification eliminates the retrospective error class structurally: a Phase 2 gap that is re-classified in Phase 4 cannot produce a spurious Phase 3 origin claim if origin is locked at the point of discovery. An output that assigns origin classification retroactively -- even correctly -- does not pass. |
| C-26 | **Structural Self-Sufficiency** | depth | aspirational | Each criterion with a designated structural home (table, checklist, inventory block, gate) is satisfied by that structural element without requiring surrounding prose to restate its content. A table row satisfies a criterion; prose that re-narrates what the table row already shows does not increase criterion satisfaction and is not necessary for any criterion to pass. Outputs where any prose block could be removed without reducing criterion satisfaction across all criteria are candidates for passing; outputs where a prose block is the only location satisfying a criterion that also has a structural home do not pass. This criterion is assessed by attempting removal of each prose block in turn: if criterion satisfaction is unchanged after removal, the structural element is self-sufficient. Structural self-sufficiency demonstrates that the output's evidence load is carried by inspectable elements rather than by prose interpretation, making automated or tabular review sufficient for verification. |

---

## Scoring Table

| Tier | Criteria | Max Points | Points Per Criterion |
|------|----------|------------|----------------------|
| Essential | C-01 -- C-04 | 60 | 15 each |
| Recommended | C-05 -- C-07 | 30 | 10 each |
| Aspirational | C-08 -- C-26 | 95 | 5 each |
| **Total** | | **185** | |

---

**What changed from v7:**

Three new aspirational criteria from Round 7 tiebreaker analysis:

- **C-24 (Hypothesis-Bound Gap Inventory):** V-05's fourth inventory field — each gap inventory entry carries a hypothesis binding `(H-NN)`, making C-13 and C-20 jointly verifiable from the inventory block alone without re-scanning evidence tables.
- **C-25 (Forward Origin Classification):** V-01's forward compliance assembly — origin tagging applied at first occurrence in Phase 2, making Phase 4 classification a read operation rather than a retrospective write. Eliminates the V-02 error class structurally.
- **C-26 (Structural Self-Sufficiency):** V-03's ~40% compression with zero criterion loss — proves structural elements were load-bearing rather than decorative framing; each criterion with a structural home is satisfied by that element without prose restatement.

Point ceiling raised from 170 to 185.
```
