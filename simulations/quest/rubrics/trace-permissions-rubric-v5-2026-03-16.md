Reading the R5 scorecard carefully to extract the new excellence patterns before writing.

The three new patterns from R5 not captured in v4:

1. **V-02 strong on C-17** — COUNT MANDATE annotation: the C-17 row includes an explicit `Row count: [N]` label that must appear before PASS; the correct count alone is insufficient. Absent label = auto-fail. Having exactly N rows (C-17) and labeling the count (C-19) are two separate structural properties.

2. **V-03 M5 mechanism** — M5: Enforcement Layers column declared in Step 0.2; any aspirational criterion with single-layer enforcement is flagged; each flag carries a SHALL-J or SHALL-K resolution; CA-1.12 verifies no unresolved flags. This is a meta-enforcement audit not captured by any existing criterion.

3. **V-05 self-referential loop** — 14-row aspirational table covering C-08..C-21, including rows for the new mechanism criteria themselves (C-19/C-20/C-21); C-17 row states N=14; each new-mechanism row has a Self-Assessment cell forcing inline verification that the mechanism is active.

→ **C-19**: Count-Mandate Row Label (from V-02 strong)
→ **C-20**: M5 Enforcement-Density Column (from V-03 mechanism)
→ **C-21**: Self-Referential Aspirational Loop (from V-05)

N grows from 11 to 14. Full aspirational tier = 10 pts = 14/14 pass.

---

```markdown
# trace-permissions — Quest Rubric v5

**Skill**: `trace-permissions` | **Version**: v5 | **Date**: 2026-03-16
**Criteria**: C-01..C-21 (4 essential / 3 recommended / 14 aspirational)

---

## Changelog

### v4 → v5

Three new aspirational criteria extracted from the R5 scorecard excellence signals (not captured in v4):

| ID | Criterion | Source Signal |
|----|-----------|---------------|
| C-19 | **Count-Mandate Row Label** | V-02 strong: COUNT MANDATE annotation in the C-17 row; `Row count: [N]` must appear before PASS is awarded; absent label = auto-fail — having the correct row count (C-17) is necessary but not sufficient; the explicit label is a separate structural property |
| C-20 | **M5 Enforcement-Density Column** | V-03 mechanism: Step 0.2 declares M5: Enforcement Layers column; any aspirational criterion with single-layer enforcement is flagged with SHALL-J or SHALL-K resolution; CA-1.12 verifies all flags resolved — enforcement-density audit is a meta-layer not captured by any existing criterion |
| C-21 | **Self-Referential Aspirational Loop** | V-05 mechanism: 14-row aspirational table covering C-08..C-21, including rows for C-19, C-20, and C-21 themselves; C-17 row states N=14; each new-mechanism row has a Self-Assessment cell forcing inline verification that the mechanism is active in this output |

**Scoring impact:** N grows from 11 to 14. A v4-golden output (11/11 aspirational pass) now scores
11/14 × 10 = **7.86 pts** on the aspirational tier. Full 10 pts requires all 14 criteria.
Essential and recommended tiers unchanged.

**Dependency notes added:**
- C-19 auto-fails if C-17 fails.
- C-21 auto-fails if C-15 fails (requires 3-column structure).
- C-21 auto-fails if C-17 fails (requires correct row count).

**C-17 pass condition updated:** row range extends from C-08..C-18 (11 rows) to C-08..C-21 (14 rows).
A v4-golden output with exactly 11 rows now fails C-17 under v5.

**Structural failure pattern noted from R5 (diagnostic, not new criterion):**
V-02 and V-03 both fail C-09 for the same reason: the Closing Summary is described in prose at SE-5
rather than registered as Schema ID TABLE_6 in Step 0.1. C-09 already encodes this via the
Step 0.1 registration requirement — the R5 failures confirm that prose-only description of a closing
section is the most common C-09 miss pattern.

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

Score = `(aspirational_pass / 14) * 10`. N = 14.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-08 | **Cross-Entity Cascade** | coverage | At least one cross-entity cascade effect traced; a self-audit row forces self-assessment and triggers revision on failure. |
| C-09 | **TABLE_6 Schema Registered** | structure | Closing Summary registered as Schema ID TABLE_6 in Step 0.1; SHALL-I obligation declared; CA-1.11 double-anchor present; GCR-7 references TABLE_6. Prose-only description of the closing section fails. |
| C-10 | **\[CLOSES:\] Annotations** | structure | Every gap row in TABLE_4/TABLE_5 carries a `[CLOSES: C-NN]` annotation linking it to the criterion it satisfies; self-audit row enforces compliance. |
| C-11 | **Null-Case Rows** | structure | PPF-1..PPF-6 prohibit prose null-cases; every table site has a null-case row (or explicit N/A with justification); no null case expressed as prose. |
| C-12 | **Escalation Risk \[GCR-7\]** | structure | GCR-7 explicitly declared for the TABLE_6 / Closing Summary site; inline justification required; absent declaration fails. |
| C-13 | **GCR Block (a)+(b)+(c) Co-Located** | structure | Every GCR-N block (GCR-1..GCR-7) contains scale, auto-fail condition, and post-table verification instruction in one contiguous block. Cross-section splits fail; inline annotations that defer (c) to a separate section fail. |
| C-14 | **Prohibited Prose Form** | structure | PPF-1..PPF-6 each present with verbatim wrong-form example and the criterion ID it violates; one PPF entry per named table site (TABLE_1..TABLE_5 + Escalation Risk column). One example total fails. |
| C-15 | **3-Column Aspirational Audit Table** | structure | Aspirational audit table has three columns: Pass Condition, Fail Signal, Self-Assessment. A flat checklist — even with the correct row count — fails; the column structure is load-bearing. |
| C-16 | **GCR-N Citation in All Headers** | structure | Every graded-column header cites the corresponding GCR-N identifier; CA-1.9 (or equivalent) double-anchor verifies all headers; any uncited header fails. |
| C-17 | **Exactly 14 Rows C-08..C-21** | structure | Aspirational audit table contains exactly 14 rows covering C-08..C-21; no criterion omitted, no extra rows. A v4-format 11-row table fails this criterion under v5. |
| C-18 | **PPF-1..PPF-6 per Table Site** | structure | Each PPF entry is keyed to a specific named table or schema site (TABLE_1..TABLE_5, TABLE_6); PPF-6 explicitly keyed to TABLE_6. Generic or site-unkeyed entries fail. |
| C-19 | **Count-Mandate Row Label** | meta | The C-17 row in the aspirational audit table contains an explicit `Row count: [N]` annotation where N matches the actual row count; the annotation must appear before the PASS verdict in the Self-Assessment cell. Absent annotation = auto-fail. Auto-fails if C-17 fails. |
| C-20 | **M5 Enforcement-Density Column** | meta | Step 0.2 declares an M5: Enforcement Layers column; any aspirational criterion with single-layer enforcement is flagged; each flag carries a SHALL-J or SHALL-K resolution; CA-1.12 (or equivalent) verifies all M5 flags resolved before the output closes. |
| C-21 | **Self-Referential Aspirational Loop** | meta | The aspirational audit table covers C-08..C-21 (all 14 rows), including rows for C-19, C-20, and C-21 themselves; the C-17 Self-Assessment cell states `Row count: 14`; C-19, C-20, and C-21 rows each contain a filled Self-Assessment cell verifying the corresponding mechanism is active. Auto-fails if C-15 fails or C-17 fails. |
```
