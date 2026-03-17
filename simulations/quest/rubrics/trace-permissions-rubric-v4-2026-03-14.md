Reading the scorecard carefully to extract the new excellence patterns before writing the rubric.

From the Round 3 results, the key patterns are:

1. **JSON pattern** — "Dual-layer structural enforcement: H-flag columns enforce hypothesis tracing at table-cell granularity while phase completion gates enforce sequencing at section-transition granularity — two independent mechanisms operating at different levels create a ceiling that neither mechanism achieves alone"
2. **V-04 specific evidence** — Table 7: "Do not introduce gaps in Phase 4 that do not appear in this table" — gap provenance enforcement; distinct from C-08 (risk-ranked summary) and C-09 (remediation per gap), which govern *what* appears in the summary, not *where it must have originated*

C-13 and C-14 already exist. The new extractable criterion is **Gap Provenance Enforcement** (Table 7 pattern) — a structural constraint that the summary is a consolidation of evidence-table rows, not a new analysis layer.

---

# Rubric: trace-permissions (v4)

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

## Aspirational Criteria (40 points total)

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

---

## Scoring Table

| Tier | Criteria | Max Points | Points Per Criterion |
|------|----------|------------|----------------------|
| Essential | C-01 -- C-04 | 60 | 15 each |
| Recommended | C-05 -- C-07 | 30 | 10 each |
| Aspirational | C-08 -- C-15 | 40 | 5 each |
| **Total** | | **130** | |

---

**What changed from v3:**

| Change | Source |
|--------|--------|
| C-15 Gap Provenance Enforcement | V-04 Table 7 constraint: "Do not introduce gaps in Phase 4 that do not appear in this table" — enforces that the final summary is a consolidation of evidence-table rows, not a new analysis layer; structurally distinct from C-08/C-09 which govern content of the summary, not its origin |
| Aspirational ceiling raised from 35 to 40 pts | One new criterion at 5 pts |
| Total ceiling raised from 125 to 130 | |

**Why C-15:** R3 confirmed that C-13 and C-14 are genuinely independent mechanisms operating at different granularity levels (cell vs. section-transition). V-04's gap provenance constraint reveals a third enforcement target: the boundary between analysis phases and the summary. Without C-15, an output can pass C-08 and C-09 by introducing well-formed gaps directly in Phase 4 that were never traced through evidence tables. C-15 closes that path and enforces that the summary is structurally downstream of the evidence, not a parallel track.

**Why not a "dual-mechanism pairing" criterion:** C-13 and C-14 are already separate scoreable criteria. Formalizing their combination as a third criterion would make 10 points contingent on the same two mechanisms — adding noise without discriminating power. C-15 targets a structurally distinct enforcement point.

---

## Notes

- The rubric is platform-agnostic. Whether the system is Dataverse, Salesforce, custom RBAC, or
  another model, the criteria apply by analogy.
- Stock reviewer persona (Dataverse security expert) surfaces FLS gaps and sharing rule
  conflicts; Customer Service perspective surfaces team membership and record visibility gaps.
- C-10 through C-12 target the gap between 88/100 and 96-98/100 outputs: systematic framing
  vs. ad-hoc gap enumeration.
- C-13 and C-14 target the gap between 115 and 120: table-cell hypothesis tracing vs. prose
  tracing; explicit phase-gate assertion vs. structural dividers.
- C-15 targets the gap between 125 and 130: summary-as-consolidation vs.
  summary-as-new-analysis. An output can pass C-08 and C-09 with high-quality summary content
  while still failing C-15 by introducing gaps that bypassed the evidence tables.
