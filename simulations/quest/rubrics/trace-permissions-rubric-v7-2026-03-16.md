Reading the R7 scorecard carefully for new patterns before writing.

**Three new patterns from R7 not captured in v6:**

1. **V-03 axis absent from V-04 (C-21 range phrase currency)** — V-03 updates the mechanism phrase in the C-21 self-referential loop from `C-08..C-21` to `C-08..C-23`. V-01, V-02, and V-04 all pass C-21 *structurally* (rows present, loop terminates) but retain the stale phrase. The V-04 description explicitly calls out "C-21 mechanism phrase update not included (V-03 axis absent)," confirming this is a separable enforcement axis. Pattern: the literal range string in the C-21 mechanism must name the current terminal criterion, not just cover it structurally.

2. **V-03 axis absent from V-04 (SHALL-L mandate extension)** — V-03 extends SHALL-L to formally mandate observable mechanism phrases in C-22 and C-23 Self-Assessment cells. V-01/V-02/V-04 contain mechanism phrases in those cells via inheritance or structural compliance, but SHALL-L does not name C-22/C-23 as covered — presence without mandate is unenforceable obligation. Pattern: when new criteria are introduced, SHALL-L must be explicitly extended to name them.

3. **C-10 [CLOSES:] slot displacement** — v6 flagged C-10 as "candidate for C-24." R7 still confirms FAIL across all variations but produces no passing example. The C-24 slot is now occupied by the V-03 range-phrase signal. C-10 gap re-flagged as candidate for C-26.

→ **C-24**: C-21 Loop Range Phrase Currency (from V-03 axis, absent V-04)
→ **C-25**: SHALL-L Mandate Extension for New Criteria (from V-03 axis, absent V-04)

N grows from 16 to 18. Full aspirational tier = 10 pts = 18/18 pass.

---

```markdown
# trace-permissions — Quest Rubric v7

**Skill**: `trace-permissions` | **Version**: v7 | **Date**: 2026-03-16
**Criteria**: C-01..C-25 (4 essential / 3 recommended / 18 aspirational)

---

## Changelog

### v6 → v7

Two new aspirational criteria extracted from the R7 scorecard excellence signals (V-03 axis
confirmed absent from V-04):

| ID | Criterion | Source Signal |
|----|-----------|---------------|
| C-24 | **C-21 Loop Range Phrase Currency** | V-03 strength on C-21 evidence quality: V-03 updates the range string in the C-21 self-referential loop mechanism phrase from `C-08..C-21` to `C-08..C-23`; V-01, V-02, and V-04 pass C-21 structurally (all rows present, Self-Assessment cells present) but retain the stale phrase — the binary pass result is the same under v6 but the explicit range string does not reflect the current N; V-04 description explicitly calls out "C-21 mechanism phrase update not included (V-03 axis absent)," confirming this is a distinct enforcement axis; any output that introduces new criteria must update the range phrase to name the new terminal row |
| C-25 | **SHALL-L Mandate Extension for New Criteria** | V-03 strength on SHALL-L scope: V-03 extends SHALL-L to formally mandate observable mechanism phrases in C-22 and C-23 Self-Assessment cells; V-01, V-02, and V-04 contain mechanism phrases in those cells (via inheritance or structural compliance) but SHALL-L does not explicitly name C-22/C-23 as covered — without the SHALL-L mandate, mechanism phrase presence in new-criterion cells is structural coincidence, not enforced obligation; V-04 lacks this axis despite combining V-01 and V-02 |

**Scoring impact:** N grows from 16 to 18. A v6-golden output (16/16 aspirational pass) now scores
16/18 × 10 = **8.89 pts** on the aspirational tier. Full 10 pts requires all 18 criteria.
Essential and recommended tiers unchanged.

**Dependency notes added:**
- C-24 auto-fails if C-21 fails (requires the self-referential loop mechanism to exist).
- C-25 auto-fails if C-19 fails (requires the SHALL-L mechanism to exist).

**C-17 pass condition updated:** integer must equal 18 and row range must be declared as C-08..C-25.
A v6-golden output with integer=16 now fails C-17 under v7.

**C-21 pass condition updated:** self-referential loop must cover C-08..C-25 (18 rows); each
new-mechanism row (C-19, C-20, C-21, C-22, C-23, C-24, C-25) must include a Self-Assessment cell.
A v6-golden output whose loop ends at C-23 (16 rows) fails C-21 under v7.

**C-24 pass condition note:** Pass requires the literal range string `C-08..C-25` to appear in the
C-21 mechanism phrase text. Structural loop coverage alone does not satisfy C-24. Stale strings
(`C-08..C-21`, `C-08..C-23`) fail even when all rows are structurally present.

**C-25 pass condition note:** Pass requires SHALL-L to explicitly name the new criteria by ID
(minimum: C-22, C-23, C-24, C-25 under v7). Cells that contain mechanism phrases by inheritance
without a SHALL-L naming mandate fail.

**Slot displacement note:**
v6 flagged C-10 (`[CLOSES:]` annotation) as "candidate for C-24." The C-24 slot is occupied by
the V-03 range-phrase signal extracted from R7. The [CLOSES:] gap remains FAIL across all R7
variations (no passing example produced) and is re-flagged as candidate for C-26 in a future round.

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
| C-06 | **Scale Declaration** | depth | At least one operation or role scope carries a GCR-7-level or equivalent scale qualifier (e.g., record-count range, BU scope boundary). Scope claims without a qualifier fail. |
| C-07 | **Prohibition Documentation** | completeness | At least one access prohibition (PPF-6 or equivalent) documented with the specific operation, role, and reason it is disallowed. Gaps identified but not prohibited fail. |

---

## Aspirational Criteria (10 pts total)

Score = (passing criteria / N) × 10. **N = 18** (C-08..C-25). Full 10 pts requires 18/18 pass.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-08 | **Multi-Table Output Structure** | format | Output contains at least three distinct structured tables covering operation-role pairs, field-level restrictions, and record accessibility scope. Single-table outputs fail. |
| C-09 | **Cross-Table Label Consistency** | correctness | Role identifiers, operation names, and scope labels are consistent across all tables — no label appearing in one table absent or renamed in another without explicit explanation. |
| C-10 | **[CLOSES:] Section Header Annotation** | traceability | Each section header that closes a named gap includes a literal `[CLOSES: <label>]` inline annotation in the header text. Substantive gap closure via MANUAL GAP labels or STRUCTURED CLOSE blocks is insufficient; the inline notation in the section header is required. |
| C-11 | **Null-Case Prohibitions** | completeness | Prohibitions table (PPF-1..PPF-6 or equivalent) includes at least one null-case entry — an operation/role combination with no access, explicitly documented rather than omitted. |
| C-12 | **Escalation Risk Inline Justification** | depth | Escalation risk entries (GCR-7 or equivalent) each include an inline justification string explaining why the escalation is a risk, not just a label or severity marker. |
| C-13 | **Scope Boundary Conditions** | correctness | At least one boundary condition for record or field access scope is identified (e.g., what changes at BU boundary, what changes at org boundary). Scope declarations without boundaries fail. |
| C-14 | **Gap Severity Labeling** | depth | Each identified gap carries a severity or risk-level label (HIGH/MED/LOW or equivalent). Unlabeled gaps fail this criterion regardless of description quality. |
| C-15 | **Operation Coverage Completeness** | coverage | All operations declared in the Operation-Role Matrix also appear in the FLS table and Record Scope table. Missing cross-table operation coverage fails. |
| C-16 | **GCR-N Header Citation Rule** | format | Every table column that references a GCR dimension includes the GCR-N citation by ID. Freeform column names without GCR-N labels fail. |
| C-17 | **COUNT MANDATE** | meta | Self-Assessment table includes an explicit integer row count equal to **18** and declares the row range as **C-08..C-25**. Integer ≠ 18 fails. Declared range ≠ C-08..C-25 fails. |
| C-18 | **Dependency Chain Declaration** | depth | At least one auto-fail dependency chain is declared (criterion X auto-fails if criterion Y fails), with both criteria identified by ID. Dependency claims without ID references fail. |
| C-19 | **COUNT MANDATE Label Mechanism (SHALL-L)** | meta | Self-Assessment table contains a SHALL-L label entry with an observable mechanism phrase mandating the row count. Presence of the integer alone without a SHALL-L label fails. |
| C-20 | **M5 Enforcement-Density Matrix Entry** | meta | Step 0.2 M5 enforcement-density matrix contains entries for each self-referential criterion (C-19, C-20, C-21 at minimum) with explicit SHALL resolutions. Absence of M5 entries for these criteria fails. |
| C-21 | **Self-Referential Loop Coverage** | meta | Self-Assessment table loop covers **C-08..C-25** (18 rows). Each new-mechanism row (C-19, C-20, C-21, C-22, C-23, C-24, C-25) must include a Self-Assessment cell. Loop terminating before C-25 fails. |
| C-22 | **New-Criteria M5 Closure** | meta | Every criterion introduced by this output is registered in the Step 0.2 M5 enforcement-density matrix with an explicit SHALL resolution. Criteria present only in the self-audit table (single-layer enforcement) fail. C-22 must itself appear in the M5 matrix (recursive self-registration). Auto-fails if C-20 fails. |
| C-23 | **SHALL-L Cross-Cell Anchor Phrase** | meta | The C-19 Self-Assessment cell contains the verbatim phrase `Row count: [integer] confirmed in C-17 Self-Assessment cell.` The integer must match the C-17 declared count. Absence of the anchor phrase fails. Auto-fails if C-17 fails. Auto-fails if C-19 fails. |
| C-24 | **C-21 Loop Range Phrase Currency** | meta | The mechanism phrase in the C-21 self-referential loop explicitly names the current terminal criterion as `C-08..C-25`. Stale range strings (`C-08..C-21`, `C-08..C-23`, etc.) fail even when the loop structurally covers all 18 rows. Pass requires the literal string `C-08..C-25` to appear in the mechanism text. Auto-fails if C-21 fails. |
| C-25 | **SHALL-L Mandate Extension for New Criteria** | meta | The SHALL-L declaration is explicitly extended to mandate observable mechanism phrases in each new criterion's Self-Assessment cell (minimum: C-22, C-23, C-24, C-25 under v7). New criteria whose Self-Assessment cells contain mechanism phrases by inheritance or structural coincidence — without a SHALL-L naming mandate — fail this criterion. Auto-fails if C-19 fails. |

---

## Scoring Summary

| Tier | Points | Criteria | Rule |
|------|--------|----------|------|
| Essential | 60 | C-01..C-04 | 15 pts each; all four must pass |
| Recommended | 30 | C-05..C-07 | 10 pts each |
| Aspirational | 10 | C-08..C-25 | (passing / 18) × 10 |
| **Total** | **100** | | |

### Aspirational Score Reference (v7)

| Pass Count | Score | Context |
|------------|-------|---------|
| 18/18 | 10.00 | Full v7 golden |
| 17/18 | 9.44 | One structural gap |
| 16/18 | 8.89 | v6-golden baseline under v7 |
| 15/18 | 8.33 | |
| 14/18 | 7.78 | v5-golden baseline under v7 |
```
