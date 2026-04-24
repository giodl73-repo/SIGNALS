Written to `simulations/quest/rubrics/trace-permissions-rubric-v2-2026-03-14.md`.

---

**Rubric summary — trace-permissions v2:**

**Essential (4 criteria, 60 pts):** unchanged from v1

**Recommended (3 criteria, 30 pts):** unchanged from v1

**Aspirational (5 criteria, 25 pts):** C-08 and C-09 unchanged; three new criteria:

| ID | Criterion | Source Signal |
|----|-----------|---------------|
| C-10 | **Hypothesis Pre-commitment** | V-03 strength / V-04 weakness — commit to expected gaps before tracing; findings must address each hypothesis by name (confirmed, refuted, or modified). Outputs that find real gaps without pre-commitment don't pass. |
| C-11 | **Null-Finding Accountability** | V-01 structural detail / V-02 implicit gap — "None identified" requires naming what was examined plus a one-sentence justification. Prevents empty sections from slipping through unquestioned. |
| C-12 | **Four-Vector Escalation Sweep** | V-01 vs V-02 delta on C-05 — escalation checked across all four vectors (reassignment, team promotion, sharing bypass, impersonation), each either named or explicitly cleared. One path found is not enough. |

**Scoring ceiling raised from 100 to 115.** Essential + recommended baseline is 90. Aspirational is above-and-beyond. The V-01/V-03 outputs (98/96) would score ~110-115; V-02 (88) maps to ~88/115 — the separation is now numerically visible.

The key delta captured: V-02 merged C-05/C-06/C-07 into a generic gap table and scored 88. C-10/C-11/C-12 make the three structural weaknesses of that approach explicit pass/fail criteria.
 should be configured" or "FLS applies" without naming specific fields and specific roles does not pass. |
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

## Aspirational Criteria (25 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-08 | **Risk-Ranked Gap Summary** | depth | aspirational | Output concludes with a ranked list of identified gaps ordered by risk severity (High / Medium / Low), with a one-line justification per gap. Ranking must be defensible relative to the operation and data sensitivity described. |
| C-09 | **Remediation Recommendation Per Gap** | behavior | aspirational | For each gap identified, output provides a concrete remediation action (e.g., "add FLS read-deny on AccountNumber for Customer Service role", "remove team-level sharing rule that grants org-wide read"). Vague guidance ("tighten security") does not pass. |
| C-10 | **Hypothesis Pre-commitment** | depth | aspirational | Before tracing, output states at least two expected security gaps as explicit hypotheses (e.g., "H1: Customer Service role likely has read access to fields that should be restricted by FLS"). Findings section addresses each hypothesis by name -- confirmed, refuted, or modified with evidence. Outputs that surface gaps without pre-committed hypotheses do not pass, even if the gaps are correct. |
| C-11 | **Null-Finding Accountability** | behavior | aspirational | For any recommended section (escalation, sharing rules, team membership) where no gap is found, output names the specific controls or configurations examined and provides a one-sentence justification for the null result. "None identified" alone does not pass. Acceptable form: "No escalation path found -- record reassignment restricted to System Administrator; no team promotion path exists; sharing rules examined: three criteria-based rules, all scope-narrowing." |
| C-12 | **Four-Vector Escalation Sweep** | depth | aspirational | Privilege escalation analysis covers all four standard vectors: (1) record reassignment, (2) team promotion or membership elevation, (3) sharing rule bypass, and (4) impersonation or delegation. Output either names a plausible path per vector or explicitly clears it with a one-line justification. Identifying one path without checking the remaining vectors does not pass. |

---

## Scoring Table

| Tier | Criteria | Max Points | Points Per Criterion |
|------|----------|------------|----------------------|
| Essential | C-01, C-02, C-03, C-04 | 60 | 15 each |
| Recommended | C-05, C-06, C-07 | 30 | 10 each |
| Aspirational | C-08, C-09, C-10, C-11, C-12 | 25 | 5 each |
| **Total** | | **115** | |

Aspirational points are above the essential + recommended ceiling of 90. A score of 90/115 means
all essential and recommended criteria passed with no aspirational. A score of 115/115 means
every criterion passed.

---

## Failure Modes (auto-fail essential)

- Output lists roles without tying them to operations (C-01 fails)
- Output says "field-level security should be configured" without specifying which fields or which roles (C-02 fails)
- Output uses only "user can access their own records" with no mention of scope hierarchy (C-03 fails)
- Output describes the RBAC model without surfacing any problem, gap, or risk (C-04 fails)

---

## Notes

- The rubric is platform-agnostic. Whether the system is Dataverse, Salesforce, custom RBAC, or
  another model, the criteria apply by analogy.
- Stock reviewer persona (Dataverse security expert) surfaces FLS gaps and sharing rule
  conflicts; Customer Service perspective surfaces team membership and record visibility gaps.
- C-10 through C-12 target the gap between 88/100 and 96-98/100 outputs: systematic framing
  (C-10), explicit null accountability (C-11), and exhaustive escalation coverage (C-12).
- V-02 (88/100) failed C-10/C-11/C-12 by merging C-05/C-06/C-07 into a generic gap table
  with no dedicated sections, no hypothesis pre-commitment, and no null accountability
  requirements. The new aspirational criteria make this structural gap explicit.
- Version 2 -- iterate if R2+ scorecards reveal new systematic blind spots.
