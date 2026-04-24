Written to `simulations/quest/rubrics/trace-permissions-rubric-v2-2026-03-16.md`.

---

**What changed from v1 to v2:**

Three new aspirational criteria extracted from the V-05 (95 pt) excellence signals:

| ID | Criterion | Source Signal |
|----|-----------|---------------|
| C-10 | **Blind-Spot-Labeled Tables** | "naming what each table closes converts gap-hunting from generic obligation to motivated closure against named failure modes" |
| C-11 | **Data-Row Null-Case Mandate** | "requiring the null case as a data row (not prose preamble) makes silent omission structurally impossible" |
| C-12 | **Escalation Risk Column in Closing Summary** | "adding HIGH/MEDIUM/LOW/NONE escalation risk to the summary table serves C-05 and C-09 simultaneously from a single column" |

**Scoring impact:** Aspirational tier grows from 2 to 5 criteria. The formula `(aspirational_pass/N * 10)` is ratio-based so no weight adjustment was needed. A v1-golden output (C-08, C-09 both fail) still scores identically on the essential and recommended tiers; the aspirational delta is now spread across 5 criteria instead of 2, making the ceiling slightly harder to reach but the floor unchanged.

**Dependency note added:** C-12 auto-fails if C-09 fails (no summary table = no column to evaluate).
 output identifies which fields are visible/editable and which are restricted per role. | essential | coverage | At least one field-level restriction is traced for at least one operation. Generic statements like "all fields available" are acceptable only if explicitly justified. |
| C-03 | **Record Accessibility Scope** -- The output identifies which records each role can access (e.g., owned, team, business-unit, org-wide) for the traced operations. | essential | correctness | At least one record-access scope level (owner / team / BU / org) is identified per operation or per role. Missing scope is flagged as a gap, not silently omitted. |
| C-04 | **Gap or Risk Identification** -- The output names at least one security gap: a missing FLS restriction, a privilege escalation path, a team membership gap, or a sharing rule conflict. | essential | depth | At least one named gap appears in the output with a description of why it is a risk. Outputs that only confirm permissions without identifying any gap do not pass. |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-05 | **Privilege Escalation Path Traced** -- The output explicitly traces at least one privilege escalation path: a sequence of role assignments, team memberships, or sharing rules that allows a lower-privilege identity to reach a higher-privilege resource. | recommended | depth | A concrete escalation path is described with the starting role/user, the intermediate step (team membership, sharing rule, etc.), and the elevated access reached. |
| C-06 | **Role Hierarchy Respected** -- Findings acknowledge the role hierarchy (parent/child BU structure or role inheritance) and note where inheritance amplifies or limits access. | recommended | correctness | At least one inheritance or hierarchy effect is called out -- either "role X inherits from Y and therefore can..." or "role X is scoped to BU-only and cannot see...". |
| C-07 | **Remediation Suggestions** -- For each identified gap, the output proposes a specific remediation: a role change, FLS rule to add, team membership to revoke, or sharing rule to restrict. | recommended | behavior | At least one gap in C-04 has a corresponding actionable remediation (not just a restatement of the problem). |

---

## Aspirational Criteria (10 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-08 | **Cross-Entity Cascade** -- The output traces permissions across related entities (e.g., a user with Write on Account also gains implied access to child Contacts via relationship-based sharing), surfacing cascade risks. | aspirational | depth | At least one cross-entity cascade effect is identified with the parent entity, child entity, and the mechanism (cascade sharing, lookup field, related record access). |
| C-09 | **Structured Summary Table** -- The output closes with a summary table: each operation row contains role, FLS verdict (pass/fail/partial), record scope, and gap flag. | aspirational | format | A table with at minimum three columns (operation or role, FLS status, record scope) is present and consistently populated for all traced operations. |
| C-10 | **Blind-Spot-Labeled Tables** -- Each table or section names the specific failure mode it closes (e.g., "closes: silent FLS omission"), converting gap-hunting from a generic obligation into motivated closure against named failure modes. | aspirational | format | At least one table header, section title, or opening sentence names the specific blind spot or failure mode the section addresses -- not a generic label like "FLS Analysis" but a named risk like "closes: cumulative privilege via team membership". |
| C-11 | **Data-Row Null-Case Mandate** -- The null case (e.g., "no FLS profile configured") appears as an explicit data row in the relevant table, not as a prose disclaimer before the table. | aspirational | correctness | At least one null or empty case appears as a data row -- e.g., a table row where FLS Profile = "Not Configured" or Gap Type = "CLEARED" -- rather than as prose commentary outside the table. Silent omission is structurally impossible when the null case is a required row. |
| C-12 | **Escalation Risk Column in Closing Summary** -- The closing summary table includes an Escalation Risk column (HIGH / MEDIUM / LOW / NONE) populated for all traced operations or roles. | aspirational | format | The closing summary table contains an Escalation Risk column with an explicit scale (at minimum two levels) and every row populated. This column satisfies C-05 evidence and C-09 format simultaneously from a single column. |

---

## Design Rationale

- **C-04 is essential** -- an output that only confirms what is allowed without surfacing any risk has zero value for a permissions tracer.
- **C-05 is recommended, not essential** -- the skill may legitimately be called in a context where no escalation path exists; forcing a gap there would make valid clean outputs fail.
- **C-08 is aspirational** -- requires cross-entity schema knowledge that not every invocation context will have.
- **C-10 is aspirational** -- naming blind spots is a quality amplifier, not a correctness requirement; an output without labeled tables can still pass all essential and recommended bars.
- **C-11 is aspirational** -- the data-row null-case is a structural enforcement technique; prose null-case disclaimers satisfy the underlying C-02/C-04 intent even if they are easier to silently omit.
- **C-12 is aspirational** -- the escalation risk column is a bonus efficiency signal; an output can pass C-05 and C-09 separately without combining them into a single column.

---

## Scoring Guide

| Result | Meaning |
|--------|---------|
| All C-01 through C-04 pass | Essential bar cleared |
| Composite >= 80 | Golden threshold met |
| Composite 60-79 | Useful but incomplete -- missing recommended depth |
| Composite < 60 | Not useful -- essential gaps present |

---

## Notes for Evaluators

- **Partial credit is binary per criterion** -- each criterion either passes or fails; no half-points.
- A criterion passes if the pass condition is met for at least the primary operation or role being traced; it does not require exhaustive coverage of every operation/role unless the criterion explicitly says so.
- Outputs that list roles without any field-level or record-scope analysis fail C-02 and C-03 even if C-01 passes.
- "Placeholder" or stub outputs with no actual permission data fail all essential criteria.
- C-10, C-11, C-12 are scored independently -- an output can earn any combination of the three.
- C-12 requires a closing summary table to exist (C-09 pass condition) before it can be evaluated; if no summary table is present, C-12 fails automatically.
