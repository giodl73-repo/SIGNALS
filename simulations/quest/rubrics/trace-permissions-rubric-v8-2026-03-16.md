```markdown
# trace-permissions — Quest Rubric v8

**Skill**: `trace-permissions` | **Version**: v8 | **Date**: 2026-03-16
**Criteria**: C-01..C-27 (4 essential / 3 recommended / 20 aspirational)

---

## Changelog

### v7 → v8

Two new aspirational criteria extracted from the R8 scorecard excellence signals (V-05 axis
confirmed absent from V-03/V-04):

| ID | Criterion | Source Signal |
|----|-----------|---------------|
| C-26 | **FM-SKILL Naming for Self-Defense Mechanisms** | V-05 strength on CONTEXT causal motivation: V-05 names FM-SKILL-7 "Self-Assessment Loop Staleness" in CONTEXT before Phase 1 and adds a corresponding FAILURE MODE MAP row — V-03/V-04 achieve 18/18 structurally (pre-printed cells and runtime phrase respectively) but neither names the failure mode causing the staleness nor maps it to a structural defense; without a numbered FM-SKILL in CONTEXT, the structural rules are unexplained obligations rather than causally-grounded mechanisms; when criteria defend the self-assessment structure itself (loop range currency, SHALL-L mandate extension), a named FM-SKILL entry is required and the FAILURE MODE MAP must maintain 1:1 coverage of all numbered FM-SKILLs |
| C-27 | **Phase-level Structural Purpose Annotation Completeness** | V-05 strength on defense chain completeness: V-05 adds FM-SKILL-7 to Phase 8's structural purpose blockquote — V-03/V-04 enforce the mechanism at the structural level without annotating why at the phase level; a complete defense chain requires CONTEXT motivation → FAILURE MODE MAP mapping → phase-level enforcement annotation at the point of application; any phase that enforces a new FM-SKILL must name it in that phase's structural purpose blockquote |

**Scoring impact:** N grows from 18 to 20. A v7-golden output (18/18 aspirational pass) now scores
18/20 × 10 = **9.000 pts** on the aspirational tier. Full 10 pts requires all 20 criteria.
Essential and recommended tiers unchanged.

**Dependency notes added:**
- C-26 auto-fails if no structural self-defense criteria exist to name (requires C-24 or C-25 as the mechanism being motivated).
- C-27 auto-fails if C-26 fails (phase annotation cannot reference an FM-SKILL that was never declared in CONTEXT).

**C-17 pass condition updated:** integer must equal 20 and row range must be declared as C-08..C-27.
A v7-golden output with integer=18 now fails C-17 under v8.

**C-21 pass condition updated:** self-referential loop must cover C-08..C-27 (20 rows); each
new-mechanism row (C-19, C-20, C-21, C-22, C-23, C-24, C-25, C-26, C-27) must include a
Self-Assessment cell. A v7-golden output whose loop ends at C-25 (18 rows) fails C-21 under v8.

**C-24 pass condition updated:** literal range string `C-08..C-27` must appear in the C-21 mechanism
phrase text. Stale strings (`C-08..C-25`, `C-08..C-23`, `C-08..C-21`) fail even when all rows
are structurally present.

**C-25 pass condition updated:** SHALL-L must explicitly name C-22, C-23, C-24, C-25, C-26, C-27.
Cells that contain mechanism phrases by inheritance without a SHALL-L naming mandate fail.

**Slot displacement note:**
v7 flagged the [CLOSES:] annotation gap as "candidate for C-26." The C-26 slot is occupied by
the FM-SKILL naming signal extracted from R8. The [CLOSES:] gap remains FAIL across all R8
variations (no passing example produced) and is re-flagged as candidate for C-28 in a future round.

---

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
| C-05 | **Role Hierarchy Representation** | structure | Role hierarchy or inheritance chain explicitly represented. Flat role lists without hierarchy context fail. |
| C-06 | **Multi-Operation Cross-Role Comparison** | coverage | At least two operations compared across at least two roles showing differential access. Single-role or single-operation traces fail. |
| C-07 | **Enforcement Mechanism Identification** | depth | At least one named enforcement mechanism (field rule, record filter, role check) identified per gap. Gaps without enforcement context fail. |

---

## Aspirational Criteria (10 pts total)

N = 20 criteria (C-08..C-27). Each pass worth 10/20 = **0.500 pts**. Full tier = all 20 pass.

### Phase 1 — Context and Failure Mode Catalog

| ID | Criterion | Pass Condition |
|----|-----------|----------------|
| C-08 | **Phase Structure Completeness** | Output organized into at least 6 distinct phases or sections. Unstructured prose fails. |
| C-09 | **Failure Mode Catalog Presence** | At least one FM-SKILL entry in CONTEXT naming a failure mode specific to permission tracing. CONTEXT section must appear before Phase 1. |

### Phase 2 — Role-Operation Coverage

| ID | Criterion | Pass Condition |
|----|-----------|----------------|
| C-10 | **Cross-Role Differential Table** | EXPECTED DIFFERENTIAL / CANDIDATE OVER-PERMISSION table present (Phase 7 SHALL differential). At least one differential row with explicit expected-vs-actual access delta. |
| C-11 | **FLS Mechanism Tracing** | At least one field-level security rule traced to its enforcement point (policy, filter, or attribute rule). Rule identification alone without tracing to enforcement fails. |

### Phase 3 — Record and Scope

| ID | Criterion | Pass Condition |
|----|-----------|----------------|
| C-12 | **Record Scope Inheritance Chain** | Scope inheritance explicitly traced (e.g., owner → team → BU → org). Flat scope lists without inheritance context fail. |
| C-13 | **Audit Trail Coverage** | Audit or logging coverage identified for at least one operation-role pair. Outputs without audit context fail. |

### Phase 4 — Gap Analysis Depth

| ID | Criterion | Pass Condition |
|----|-----------|----------------|
| C-14 | **Delegation and Escalation Path Tracing** | At least one delegation or escalation path traced from base role to elevated role. Missing escalation context fails. |
| C-15 | **FM-SKILL Minimum Coverage** | CONTEXT names FM-SKILL-1 through FM-SKILL-6 at minimum (6 named failure modes). Outputs with fewer than 6 FM-SKILLs fail. Outputs exceeding the minimum (e.g., FM-SKILL-7 via V-05) pass. |

### Phase 5 — Structural Integrity

| ID | Criterion | Pass Condition |
|----|-----------|----------------|
| C-16 | **Criterion-Count Structural Integrity** | Self-assessment table row count matches declared N integer. A table whose row count disagrees with the N declaration fails even if the integer alone is correct. |
| C-17 | **N Integer and Range Declaration** | Self-assessment declares integer N=20 and row range C-08..C-27. Any stale integer (18, 16, etc.) or stale range string fails. |

### Phase 6 — SHALL Mandate Completeness

| ID | Criterion | Pass Condition |
|----|-----------|----------------|
| C-18 | **SHALL-A Record Scope Mandate** | SHALL-A mandate present requiring record-scope identification for every operation-role pair. Missing mandate fails even if scope rows are structurally present. |
| C-19 | **SHALL-L Observable Mechanism Mandate** | SHALL-L mandate present requiring observable mechanism phrases in Self-Assessment cells. Missing SHALL-L fails. C-25 auto-fails if C-19 fails. |
| C-20 | **SHALL-M Cross-Role Differential Mandate** | SHALL-M mandate present requiring cross-role differential analysis. Missing mandate fails even if the differential table is structurally present. |

### Phase 7 — Self-Assessment Loop

| ID | Criterion | Pass Condition |
|----|-----------|----------------|
| C-21 | **Self-Assessment Loop Completeness** | Self-referential loop mechanism declared, covering C-08..C-27 (20 rows). Loop must name every criterion in range. Stale terminal rows (C-25, C-23, etc.) fail. Each new-mechanism row (C-19..C-27) must include a Self-Assessment cell. C-24 auto-fails if C-21 fails. |
| C-22 | **C-22 Self-Assessment Mechanism Phrase** | C-22 Self-Assessment cell contains an observable mechanism phrase (not bare PASS/FAIL). Inherited cells without an explicit mechanism description fail. |
| C-23 | **C-23 Self-Assessment Mechanism Phrase** | C-23 Self-Assessment cell contains an observable mechanism phrase (not bare PASS/FAIL). Inherited cells without an explicit mechanism description fail. |

### Phase 8 — Loop Currency and Mandate Extension

| ID | Criterion | Pass Condition |
|----|-----------|----------------|
| C-24 | **C-21 Loop Range Phrase Currency** | Literal string `C-08..C-27` present in the C-21 mechanism phrase text. Structural loop coverage alone does not satisfy this criterion. Stale strings (`C-08..C-25`, `C-08..C-23`, `C-08..C-21`) fail even when all rows are structurally present. Auto-fails if C-21 fails. |
| C-25 | **SHALL-L Mandate Extension for New Criteria** | SHALL-L explicitly names C-22, C-23, C-24, C-25, C-26, C-27. Cells that contain mechanism phrases by inheritance without a SHALL-L naming mandate fail. Auto-fails if C-19 fails. |

### Phase 9 — Causal Defense Chain

| ID | Criterion | Pass Condition |
|----|-----------|----------------|
| C-26 | **FM-SKILL Naming for Self-Defense Mechanisms** | When criteria defend the self-assessment structure itself (loop range currency, SHALL-L mandate extension), CONTEXT names a numbered FM-SKILL motivating the mechanism before Phase 1, and the FAILURE MODE MAP contains a corresponding row naming the structural defense. FAILURE MODE MAP must maintain 1:1 coverage with all numbered FM-SKILLs. Structural enforcement without causal naming fails. Auto-fails if both C-24 and C-25 fail (no self-defense mechanism exists to name). |
| C-27 | **Phase-level Structural Purpose Annotation Completeness** | Every phase that enforces a FM-SKILL names it in that phase's structural purpose blockquote. Complete defense chain: CONTEXT motivation → FAILURE MODE MAP mapping → phase-level enforcement annotation at point of application. A phase enforcing the C-24/C-25/C-26 mechanisms that omits FM-SKILL-7 from its structural purpose blockquote fails. Auto-fails if C-26 fails. |

---

## Scoring Summary

| Tier | Criteria | Points | Pass Condition |
|------|----------|--------|----------------|
| Essential | C-01..C-04 | 60 pts (15 each) | All four must pass |
| Recommended | C-05..C-07 | 30 pts (10 each) | Each criterion independent |
| Aspirational | C-08..C-27 | 10 pts (0.500 each) | (N pass / 20) × 10 |
| **Total** | | **100 pts** | |

**Full score**: 100.000 pts requires all 4 essential + all 3 recommended + all 20 aspirational.

**Version regression table** (aspirational tier only):

| Output vintage | Aspirational pass | Score |
|----------------|:-----------------:|------:|
| v8-golden (all 20) | 20/20 | 10.000 |
| v7-golden (18/20 under v8) | 18/20 | 9.000 |
| v6-golden (16/20 under v8) | 16/20 | 8.000 |
```
