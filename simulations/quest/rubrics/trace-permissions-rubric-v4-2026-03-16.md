Reading the scorecard carefully to extract the new excellence patterns before writing.

The three new patterns from R3 not captured in v3:

1. **V-01 strong on C-13** — GCR with *numbered entries* (GCR-1..GCR-7) where every graded column is registered and headers cite the GCR-N identifier. C-13 only requires one preamble block; exhaustive column registration is a separate structural property.

2. **V-03 PASS (strong) on C-15** — structured 8-row table with three columns (Pass Condition, Fail Signal, Self-Assessment) covering *all* aspirational criteria, not the minimum 3-item checklist. The column structure is what distinguishes this from the C-15 minimum.

3. **V-02 PASS on C-14** — exhaustive catalog with *one entry per named table site*, not the C-14 minimum of one example. Each entry maps wrong-form verbatim → criterion violated. V-02 shows six entries (TABLE_1..TABLE_5 + Escalation Risk), one per output site.

→ **C-16**: GCR Exhaustive Column Registration (from V-01)
→ **C-17**: Full-Coverage Aspirational Audit Table (from V-03)
→ **C-18**: Prohibited Prose Catalog — One Entry per Table Site (from V-02)

N grows from 8 to 11. Full aspirational tier = 10 pts = 11/11 pass.

---

# trace-permissions — Quest Rubric v4

**Skill**: `trace-permissions` | **Version**: v4 | **Date**: 2026-03-16
**Criteria**: C-01..C-18 (4 essential / 3 recommended / 11 aspirational)

---

## Changelog

### v3 → v4

Three new aspirational criteria extracted from the R3 scorecard excellence signals (not captured in v3):

| ID | Criterion | Source Signal |
|----|-----------|---------------|
| C-16 | **GCR Exhaustive Column Registration** | V-01 strong pass: 7 numbered GCR entries (GCR-1..GCR-7) with every graded column registered and headers citing GCR-N identifiers — C-13 minimum is one block; exhaustive registration is a separate structural property |
| C-17 | **Full-Coverage Aspirational Audit Table** | V-03 PASS (strong): 8-row structured table with three columns (Pass Condition, Fail Signal, Self-Assessment) covering all aspirational criteria — a flat checklist, even with 8 items, does not pass; the column structure is load-bearing |
| C-18 | **Prohibited Prose Catalog — One Entry per Table Site** | V-02 strong pass: 6-entry catalog with one entry per named table or schema, each mapping wrong form verbatim → criterion violated by ID — C-14 minimum is one example; coverage exhaustion across all table sites is a separate structural property |

**Scoring impact:** N grows from 8 to 11. A v3-golden output (8/8 aspirational pass) now scores 8/11 × 10 = **7.27 pts** on the aspirational tier. Full 10 pts requires all 11 criteria. Essential and recommended tiers unchanged.

**Dependency notes added:**
- C-16 auto-fails if C-13 fails.
- C-17 auto-fails if C-15 fails.
- C-18 auto-fails if C-14 fails.

**Structural failure pattern noted from R3 (diagnostic, not new criterion):**
V-02 and V-03 both failed C-13 for the same reason: elements (a) and (b) appeared in the graded column preamble block while element (c) (post-table verification instruction) was deferred to a separate section. C-13 already encodes this via "Inline annotations don't pass" — the R3 failure confirms that cross-section splits are the most common C-13 miss pattern.

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

Score = `(aspirational_pass / 11) * 10`. N = 11.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-08 | **Cross-Entity Cascade** | depth | At least one cross-entity cascade: parent entity, child entity, mechanism. |
| C-09 | **Structured Summary Table** | format | Closing table with >= 3 columns (role, FLS status, record scope), consistently populated. |
| C-10 | **Blind-Spot-Labeled Tables** | format | At least one table/section names the specific failure mode it closes (named risk, not generic label). |
| C-11 | **Data-Row Null-Case Mandate** | correctness | At least one null/empty case as a data row, not prose commentary outside the table. |
| C-12 | **Escalation Risk Column in Closing Summary** | format | Closing summary table has Escalation Risk column, explicit scale, every row populated. **Auto-fails if C-09 fails.** |
| C-13 | **Pre-Declared Scale with Auto-Fail Condition** | format | At least one graded column has a preamble with all three elements co-located in a single block: (a) scale definition with every level named, (b) explicit auto-fail condition for blank cells, (c) post-table verification instruction. Elements split across separate sections fail. Inline annotations fail. **Auto-fails if no graded column present.** |
| C-14 | **Prose-Substitution Failure Mode Named by Example** | correctness | At least one structural requirement shows the wrong prose form verbatim or near-verbatim AND names which criterion it violates by ID. Generic warnings ("avoid prose") fail. |
| C-15 | **Self-Verification Checklist for Aspirational Criteria** | format | Checklist of >= 3 aspirational criteria after the main output body, each named by ID or label with explicit pass/fail self-assessment. Generic completeness signals fail. **Auto-fails if no aspirational content attempted.** |
| C-16 | **GCR Exhaustive Column Registration** | format | Every graded column in the output has a numbered GCR entry (GCR-N identifier). Table and column headers cite the GCR-N identifier. No unregistered graded column permitted — a GCR covering fewer columns than the output contains fails. **Auto-fails if C-13 fails.** |
| C-17 | **Full-Coverage Aspirational Audit Table** | format | Structured table covering all aspirational criteria (C-08..C-15 at minimum, extended to current N) with exactly 3 columns: Pass Condition, Fail Signal, Self-Assessment. Every row populated. A flat checklist — even one listing all criteria — fails: the three-column table structure is required. **Auto-fails if C-15 fails.** |
| C-18 | **Prohibited Prose Catalog — One Entry per Table Site** | correctness | One prohibited prose entry for every named table or schema in the output. Each entry: wrong form verbatim or near-verbatim + criterion violated by ID. Coverage less than the total named table count fails. A catalog with examples drawn from only a subset of tables fails even if each example is otherwise valid. **Auto-fails if C-14 fails.** |

---

## Aspirational Tier at N = 11

| Aspirational pass | Pts | v3 equivalent |
|-------------------|-----|---------------|
| 11/11 | 10.00 | — (new ceiling) |
| 10/11 | 9.09 | — |
| 9/11 | 8.18 | — |
| 8/11 | 7.27 | 10.00 (v3 ceiling) |
| 7/11 | 6.36 | 8.75 (V-01 / V-04 R3 score) |
| 6/11 | 5.45 | 7.50 (V-02 / V-03 R3 score) |
| 5/11 | 4.55 | 6.25 (v2 ceiling) |
| 4/11 | 3.64 | 5.00 |
| 3/11 | 2.73 | 3.75 |
| 0/11 | 0.00 | 0.00 |

---

## Dependency Graph

```
C-13 ──► C-16   (GCR block required before exhaustive registration)
C-14 ──► C-18   (one example required before per-site catalog)
C-15 ──► C-17   (checklist required before full-coverage audit table)
C-09 ──► C-12   (summary table required before escalation column)
```

Auto-fail propagates one level only — C-16 failing does not auto-fail C-17.

---

## Scoring Summary

| Tier | Criteria | Max Pts | Method |
|------|----------|---------|--------|
| Essential | C-01..C-04 | 60 | 15 pts each, all-or-nothing |
| Recommended | C-05..C-07 | 30 | 10 pts each |
| Aspirational | C-08..C-18 | 10 | (pass_count / 11) × 10 |
| **Total** | | **100** | |
