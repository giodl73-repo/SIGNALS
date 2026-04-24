Here is the complete updated rubric:

---

# Rubric: trace-permissions (v3)

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

## Aspirational Criteria (35 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-08 | **Risk-Ranked Gap Summary** | depth | aspirational | Output concludes with a ranked list of identified gaps ordered by risk severity (High / Medium / Low), with a one-line justification per gap. Ranking must be defensible relative to the operation and data sensitivity described. |
| C-09 | **Remediation Recommendation Per Gap** | behavior | aspirational | For each gap identified, output provides a concrete remediation action (e.g., "add FLS read-deny on AccountNumber for Customer Service role", "remove team-level sharing rule that grants org-wide read"). Vague guidance ("tighten security") does not pass. |
| C-10 | **Hypothesis Pre-commitment** | depth | aspirational | Before tracing, output states at least two expected security gaps as explicit hypotheses. Findings section addresses each hypothesis by name -- confirmed, refuted, or modified with evidence. Outputs that surface gaps without pre-committed hypotheses do not pass, even if the gaps are correct. |
| C-11 | **Null-Finding Accountability** | behavior | aspirational | For any recommended section where no gap is found, output names the specific controls examined and provides a one-sentence justification for the null result. "None identified" alone does not pass. |
| C-12 | **Four-Vector Escalation Sweep** | depth | aspirational | Privilege escalation analysis covers all four standard vectors: (1) record reassignment, (2) team promotion or membership elevation, (3) sharing rule bypass, and (4) impersonation or delegation. Each is either named or explicitly cleared. Identifying one path without checking the remaining vectors does not pass. |
| C-13 | **Hypothesis-Anchored Evidence Tables** | depth | aspirational | Evidence tables (role-operation matrix, FLS table, record scope table) include an H-flag column that ties each row to a specific pre-committed hypothesis by identifier (H1, H2, etc.) or marks it N/A. Findings section resolves each hypothesis by referencing the specific table rows that confirmed, refuted, or modified it. A hypothesis section connected to findings only by prose, with no table-level tracing, does not pass. |
| C-14 | **Explicit Phase Completion Gate** | behavior | aspirational | Output includes at least one explicit phase completion marker (e.g., "PHASE 1 COMPLETE") asserted after each major section -- hypothesis, evidence, findings, summary -- before the next section begins. The marker is a visible state transition the output must take, not a section header. Outputs that execute all sections without asserting any completion marker, or that place a marker before the section content is complete, do not pass. |

---

## Scoring Table

| Tier | Criteria | Max Points | Points Per Criterion |
|------|----------|------------|----------------------|
| Essential | C-01 -- C-04 | 60 | 15 each |
| Recommended | C-05 -- C-07 | 30 | 10 each |
| Aspirational | C-08 -- C-14 | 35 | 5 each |
| **Total** | | **125** | |

---

**What changed from v2:**

| New | Source |
|-----|--------|
| C-13 Hypothesis-Anchored Evidence Tables | H-flag column pattern in V-04/V-05 — mechanical traceability from table cells to hypotheses without relying on model recall |
| C-14 Explicit Phase Completion Gate | Phase gate checkbox pattern in V-04/V-05 — "PHASE 1 COMPLETE" is a required state transition action, not a header; absence is structurally visible |
| Aspirational ceiling raised from 25 to 35 pts | Two new criteria at 5 pts each |
| Total ceiling raised from 115 to 125 | |

**Why these two:** R2 showed all variations can reach 115/115 when rubric criteria are built into prompt design. C-13/C-14 restore discriminating power by targeting structural guarantee strength — whether hypothesis tracing is mechanically enforced at the table level (C-13) and whether phase sequencing is enforced by an explicit checkpoint action (C-14) — rather than content completeness alone.
archy (C-03 fails)
- Output describes the RBAC model without surfacing any problem, gap, or risk (C-04 fails)

---

## Notes

- The rubric is platform-agnostic. Whether the system is Dataverse, Salesforce, custom RBAC, or
  another model, the criteria apply by analogy.
- Stock reviewer persona (Dataverse security expert) surfaces FLS gaps and sharing rule
  conflicts; Customer Service perspective surfaces team membership and record visibility gaps.
- C-10 through C-12 target the gap between 88/100 and 96-98/100 outputs: systematic framing
  (C-10), explicit null accountability (C-11), and exhaustive escalation coverage (C-12).
- C-13 and C-14 target the gap between 115/115 (pass/fail parity) and structural bypass
  resistance. V-04/V-05 from R2 both scored 115/115 but differ in robustness: H-flag columns
  (C-13) create mechanical traceability from each table cell to its hypothesis without relying
  on model recall; phase gates (C-14) create visible required state transitions that prevent
  section skipping more robustly than instruction-ordering alone.
- R2 showed all variations can reach 115/115 when rubric criteria are built into the design.
  C-13/C-14 restore discriminating power by targeting structural guarantee strength, not just
  content completeness.
- Version 3 -- iterate if R3+ scorecards reveal new systematic blind spots.
