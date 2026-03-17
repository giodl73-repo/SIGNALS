Reading the scorecard carefully to extract the new excellence patterns before writing the rubric.

From the Round 4 results, the key patterns are:

1. **F-02 / C-16** — Gate-level provenance inventory: V-02's inventory gate mechanism is structurally distinct from C-15 (cell-level citation). F-02 explicitly flags it as a candidate criterion ("a gate-level provenance criterion (C-16?) would be satisfied by V-02 mechanism"). It closes the section-transition layer that C-15's Source column cannot close alone.

2. **Signal 4 / C-17** — Gap ID threading: V-03/V-04 persistent identifiers thread from evidence table row through findings through summary. "Not captured in the rubric but matters for production." Makes spurious Table 7 rows mechanically detectable by inspection.

3. **Signal 3 / C-18** — Inertia column framing: V-05 inertia columns ("What breaks if this access is removed?", "What change would open this path?", "What triggers this conflict?") are additive — they improve analytical depth on C-05/C-06/C-07 without structural cost. Signal 3 confirms no compliance friction. Not captured anywhere in the current rubric.

---

```markdown
# Rubric: trace-permissions (v5)

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

## Aspirational Criteria (55 points total)

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

---

## Scoring Table

| Tier | Criteria | Max Points | Points Per Criterion |
|------|----------|------------|----------------------|
| Essential | C-01 -- C-04 | 60 | 15 each |
| Recommended | C-05 -- C-07 | 30 | 10 each |
| Aspirational | C-08 -- C-18 | 55 | 5 each |
| **Total** | | **145** | |

---

**What changed from v4:**

| Change | Source |
|--------|--------|
| C-16 Gate-Level Gap Inventory | F-02 explicit proposal: V-02 inventory gate mechanism satisfies a gate-level provenance criterion; distinct from C-15 (cell-level citation) and C-14 (section-transition completion) -- it closes the section boundary by committing an enumerated inventory block before Phase 3 COMPLETE |
| C-17 Gap ID Threading | Signal 4 / V-03 + V-04: persistent gap identifiers threading from evidence table through findings through summary are "not captured in the rubric but matter for production"; they make spurious Phase 4 gaps mechanically detectable by identifier absence |
| C-18 Inertia Column Framing | Signal 3 / V-05: inertia columns ("What breaks if this access is removed?", "What change would open this path?", "What triggers this conflict?") are additive to analytical depth on C-05/C-06/C-07 with no compliance friction to C-13/C-14/C-15 structural criteria |
| Aspirational ceiling raised from 40 to 55 pts | Three new criteria at 5 pts each |
| Total ceiling raised from 130 to 145 | |

**Why C-16:** R4 F-02 explicitly identified V-02's inventory gate as satisfying a gate-level provenance criterion not yet in the rubric. C-15 operates at cell granularity (per-gap source citation); C-16 operates at section-transition granularity (committed inventory before phase boundary). The two mechanisms are structurally independent: an output can pass C-15 (Source column present) while failing C-16 (no inventory block before Phase 3 gate), or vice versa. Gate-level enforcement catches whole-gap injection; cell-level enforcement catches citation gaps. Neither subsumes the other.

**Why C-17:** Signal 4 named Gap ID threading as a production-reliability mechanism not captured in the rubric. The threading property is independently scoreable: an output either assigns persistent identifiers that appear across all three phases or it does not. The criterion also strengthens C-16 -- when Gap IDs are threaded, the Phase 3 inventory block becomes a verifiable enumeration rather than a prose commitment.

**Why C-18:** Signal 3 confirmed that inertia framing is additive with no structural cost. V-05 achieved 130/130 despite adding four inertia columns. The inertia question type is a distinct analytical move -- it tests access controls by asking what would change if the control were absent, surfacing counterfactual pressure that pure enumeration misses. This is not captured in C-05/C-06/C-07 (which require finding a gap) or C-11 (which requires accounting for null findings). C-18 rewards a specific evidence-table technique.
```
