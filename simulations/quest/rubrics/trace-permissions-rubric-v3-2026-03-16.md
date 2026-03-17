---

**v3 written** to `simulations/quest/rubrics/trace-permissions-rubric-v3-2026-03-16.md`.

Here is the complete updated rubric:

---

# trace-permissions -- Quest Rubric v3

**Skill**: `trace-permissions` | **Version**: v3 | **Date**: 2026-03-16
**Criteria**: C-01..C-15 (4 essential / 3 recommended / 8 aspirational)

---

## Changelog

### v2 -> v3

Three new aspirational criteria extracted from the R2 scorecard patterns (not captured in R1):

| ID | Criterion | Source Signal |
|----|-----------|---------------|
| C-13 | **Pre-Declared Scale with Auto-Fail Condition** | "pre-declared 4-level scale + auto-fail condition before the closing table converts aspirational column to structural gate -- the contract, the consequence, and the verification must all be present" |
| C-14 | **Prose-Substitution Failure Mode Named by Example** | "naming a prose substitution by example makes the failure mode recognizable before selection" |
| C-15 | **Self-Verification Checklist for Aspirational Criteria** | "three-item final verification checklist for aspirational criteria makes omission self-diagnosing at output time -- the model must inspect its own output against named criteria before submission" |

**Scoring impact:** N grows from 5 to 8. A v2-golden output (5/5 aspirational pass) now scores 5/8 x 10 = **6.25 pts** on the aspirational tier. Full 10 pts requires all 8 criteria. Essential and recommended tiers unchanged.

**Dependency notes added:**
- C-13 auto-fails if no graded column is present.
- C-15 auto-fails if no aspirational content is attempted.

---

## Essential Criteria (60 pts total)

Each criterion worth 15 pts. All four must pass.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Operation-Role Matrix** | coverage | At least one operation and role explicitly paired in a table or structured format. |
| C-02 | **FLS Coverage** | coverage | At least one field-level restriction traced. Generic "all fields available" acceptable only if justified. |
| C-03 | **Record Accessibility Scope** | correctness | At least one record-access scope level (owner/team/BU/org) identified per operation or role. Missing scope flagged as gap. |
| C-04 | **Gap or Risk Identification** | depth | At least one named gap with a description of why it is a risk. Confirm-only outputs fail. |

---

## Recommended Criteria (30 pts total)

Each criterion worth 10 pts.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-05 | **Privilege Escalation Path Traced** | depth | Concrete escalation path: starting role, intermediate step, elevated access reached. |
| C-06 | **Role Hierarchy Respected** | correctness | At least one inheritance or hierarchy effect called out explicitly. |
| C-07 | **Remediation Suggestions** | behavior | At least one gap in C-04 has an actionable remediation (not a restatement). |

---

## Aspirational Criteria (10 pts total)

Score = `(aspirational_pass / 8) * 10`. N = 8.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-08 | **Cross-Entity Cascade** | depth | At least one cross-entity cascade: parent entity, child entity, mechanism. |
| C-09 | **Structured Summary Table** | format | Closing table with >= 3 columns (role, FLS status, record scope), consistently populated. |
| C-10 | **Blind-Spot-Labeled Tables** | format | At least one table/section names the specific failure mode it closes (named risk, not generic label). |
| C-11 | **Data-Row Null-Case Mandate** | correctness | At least one null/empty case as a data row, not prose commentary outside the table. |
| C-12 | **Escalation Risk Column in Closing Summary** | format | Closing summary table has Escalation Risk column, explicit scale, every row populated. **Auto-fails if C-09 fails.** |
| C-13 | **Pre-Declared Scale with Auto-Fail Condition** | format | At least one graded column has a preamble with all three elements: (a) scale definition with every level named, (b) explicit auto-fail condition for blank cells, (c) post-table verification instruction. Inline annotations don't pass. **Auto-fails if no graded column present.** |
| C-14 | **Prose-Substitution Failure Mode Named by Example** | correctness | At least one structural requirement shows the wrong prose form verbatim or near-verbatim AND names which criterion it violates. Generic warnings ("avoid prose") fail. |
| C-15 | **Self-Verification Checklist for Aspirational Criteria** | format | Checklist of >= 3 aspirational criteria after the main output body, each named by ID or label with explicit pass/fail self-assessment. Generic completeness signals fail. **Auto-fails if no aspirational content attempted.** |

---

## Aspirational tier at N = 8

| Aspirational pass | Pts | v2 equivalent |
|---|---|---|
| 8/8 | 10.0 | -- (new ceiling) |
| 5/8 | 6.25 | 10.0 (v2 perfect) |
| 3/8 | 3.75 | 6.0 (v2 three-way tie at 96) |
| 2/8 | 2.5 | 4.0 (v2 V-03) |

---

The three R2 patterns map to distinct structural guarantees:

- **C-13** closes the "graded column without contract" gap — V-04 had the Escalation Risk column but no scale definition and no auto-fail, so a blank cell was no different from a populated one.
- **C-14** closes the "prose selected over row" gap — V-01 had blind-spot labels but the FLS null case was still prose; naming the wrong form by example removes the ambiguity before the model chooses.
- **C-15** closes the "aspirational omission invisible at output time" gap — without a checklist, a model can finish without noticing it skipped C-10 or C-13; the checklist makes omission self-diagnosing.
les** -- Each table or section names the specific failure mode it closes (e.g., "closes: silent FLS omission"), converting gap-hunting from a generic obligation into motivated closure against named failure modes. | format | At least one table header, section title, or opening sentence names the specific blind spot or failure mode the section addresses -- not a generic label like "FLS Analysis" but a named risk like "closes: cumulative privilege via team membership". |
| C-11 | **Data-Row Null-Case Mandate** -- The null case (e.g., "no FLS profile configured") appears as an explicit data row in the relevant table, not as a prose disclaimer before the table. | correctness | At least one null or empty case appears as a data row -- e.g., a table row where FLS Profile = "Not Configured" or Gap Type = "CLEARED" -- rather than as prose commentary outside the table. Silent omission is structurally impossible when the null case is a required row. |
| C-12 | **Escalation Risk Column in Closing Summary** -- The closing summary table includes an Escalation Risk column (HIGH / MEDIUM / LOW / NONE) populated for all traced operations or roles. **Auto-fails if C-09 fails.** | format | The closing summary table contains an Escalation Risk column with an explicit scale (at minimum two levels) and every row populated. This column satisfies C-05 evidence and C-09 format simultaneously from a single column. |
| C-13 | **Pre-Declared Scale with Auto-Fail Condition** -- Before any graded column in a table (e.g., Escalation Risk), the output declares (a) the complete scale with level definitions, (b) an explicit auto-fail condition for blank cells, and (c) a post-table verification instruction. All three elements appear before the table, not as inline column commentary. **Auto-fails if no graded column is present.** | format | At least one graded column has a preamble containing all three elements: scale definition with every level named, an explicit statement that blank cells constitute a structural failure, and a verification instruction the reader must execute after the table. Inline column annotations do not pass even if they contain scale values. |
| C-14 | **Prose-Substitution Failure Mode Named by Example** -- For each structural table-row requirement (e.g., the null-case row mandated by C-11), the output names the prose-substitution anti-pattern by showing the wrong form verbatim and identifying which criterion it violates. Example: "Writing 'No FLS configured. See note above.' instead of this row fails C-11." | correctness | At least one structural requirement includes a named prose-substitution example that (a) reproduces the wrong prose form verbatim or near-verbatim and (b) names the criterion it violates by ID or label. Generic warnings ("avoid using prose") do not pass. |
| C-15 | **Self-Verification Checklist for Aspirational Criteria** -- The output closes with a self-verification checklist naming each aspirational criterion the model must confirm before submission. Each checklist item names the criterion by ID or verbatim label and records a pass/fail self-assessment result. **Auto-fails if no aspirational content is attempted.** | format | A checklist of at least three aspirational criteria appears after the main output body. Each item names the criterion (by ID or verbatim label) and records an explicit pass/fail self-assessment. Generic completeness signals ("I verified the output is thorough") do not pass. |

---

## Design Rationale

- **C-04 is essential** -- an output that only confirms what is allowed without surfacing any risk has zero value for a permissions tracer.
- **C-05 is recommended, not essential** -- the skill may legitimately be called in a context where no escalation path exists; forcing a gap there would make valid clean outputs fail.
- **C-08 is aspirational** -- requires cross-entity schema knowledge that not every invocation context will have.
- **C-10 is aspirational** -- naming blind spots is a quality amplifier, not a correctness requirement; an output without labeled tables can still pass all essential and recommended bars.
- **C-11 is aspirational** -- the data-row null-case is a structural enforcement technique; prose null-case disclaimers satisfy the underlying C-02/C-04 intent even if they are easier to silently omit.
- **C-12 is aspirational** -- the escalation risk column is a bonus efficiency signal; an output can pass C-05 and C-09 separately without combining them into a single column.
- **C-13 is aspirational** -- pre-declaring a scale with auto-fail converts an annotation into a structural gate; outputs that include a graded column without the preamble contract are still useful but leave the structural omission risk open.
- **C-14 is aspirational** -- naming the prose-substitution failure mode by example is a prevention technique; an output that defines the null-case row without naming the anti-pattern satisfies C-11 but leaves the failure path unilluminated.
- **C-15 is aspirational** -- a self-verification checklist makes omission self-diagnosing at output time; it is a quality amplifier that cannot substitute for actually passing the underlying criteria.

---

## Scoring Guide

| Result | Meaning |
|--------|---------|
| All C-01 through C-04 pass | Essential bar cleared |
| Composite >= 80 | Golden threshold met |
| Composite 60-79 | Useful but incomplete -- missing recommended depth |
| Composite < 60 | Not useful -- essential gaps present |

**Aspirational tier at N = 8:**

| Aspirational pass | Pts (x/8 * 10) | v2 equivalent |
|-------------------|----------------|---------------|
| 8/8 | 10.0 | -- (new ceiling) |
| 5/8 | 6.25 | 10.0 (v2 perfect) |
| 3/8 | 3.75 | 6.0 (v2 three-way tie at 96) |
| 2/8 | 2.5 | 4.0 (v2 V-03) |

---

## Notes for Evaluators

- **Partial credit is binary per criterion** -- each criterion either passes or fails; no half-points.
- A criterion passes if the pass condition is met for at least the primary operation or role being traced; it does not require exhaustive coverage of every operation/role unless the criterion explicitly says so.
- Outputs that list roles without any field-level or record-scope analysis fail C-02 and C-03 even if C-01 passes.
- "Placeholder" or stub outputs with no actual permission data fail all essential criteria.
- C-10 through C-15 are scored independently -- an output can earn any combination.
- **C-12 auto-fails if C-09 fails** (no summary table = no column to evaluate).
- **C-13 auto-fails if no graded column is present** (nothing to apply the preamble contract to).
- **C-15 auto-fails if no aspirational content is attempted** (no checklist possible without prior aspirational attempt).
- C-14 pass condition requires the wrong form shown verbatim or near-verbatim alongside the criterion name -- a generic anti-pattern description without either element fails.
