# Quest Score — trace-permissions R5

## Rubric v5 Scoring (145-pt ceiling)

---

### V-01 — Inertia on all three Phase 3 analytical tables

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Role-Operation Matrix | **PASS** | Table 1 structure present with all operations |
| C-02 | FLS Named Per Role | **PASS** | Table 2 requires at least one row per role |
| C-03 | Record Access Scope | **PASS** | Table 3 one-row-per-role with explicit scope |
| C-04 | At Least One Gap | **PASS** | Tables 4-6 enforce gap discovery |
| C-05 | Privilege Escalation | **PASS** | Four-vector sweep in Table 4 |
| C-06 | Sharing Rule Conflict | **PASS** | Table 5 with conflict detection |
| C-07 | Team Membership Gap | **PASS** | Table 6 enforces at least one row |
| C-08 | Risk-Ranked Gap Summary | **PASS** | Table 7 has Severity (H/M/L) column |
| C-09 | Remediation Per Gap | **PASS** | Phase 4 pattern carried from R4 V-04 baseline |
| C-10 | Hypothesis Pre-commitment | **PASS** | Phase 1 explicitly required before any table |
| C-11 | Null-Finding Accountability | **PASS** | Tables 4, 5, 6 all require named controls and null justification for No rows |
| C-12 | Four-Vector Escalation Sweep | **PASS** | All four vectors pre-seeded as rows in Table 4 |
| C-13 | Hypothesis-Anchored Evidence Tables | **PASS** | H-flag as rightmost column on all tables; Requirement A enforced |
| C-14 | Phase Completion Gates | **PASS** | Requirement B mandates exact state-transition lines before each phase |
| C-15 | Gap Provenance Enforcement | **PASS** | Level 2: Source column in Table 7; chain enforced |
| C-16 | Gate-Level Gap Inventory | **PASS** | Level 3: inventory block with assertion before PHASE 3 COMPLETE |
| C-17 | Gap ID Threading | **PASS** | Gap IDs assigned at discovery in Tables 4, 5, 6; must match Table 7 |
| C-18 | Inertia Column Framing | **PASS** | Three inertia columns: "What change would open this path?" (T4), "What triggers this conflict?" (T5), "What breaks if membership changes?" (T6) — 3 qualifying tables ≥ 2 required |

**Score: 145/145** | All Essential: YES

---

### V-02 — Minimum viable inertia (FLS table + escalation table)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-17 | All carried criteria | **PASS** | Same structural base as V-01 |
| C-18 | Inertia Column Framing | **PASS** | Table 2 (FLS) + Table 4 (escalation sweep) = 2 qualifying tables; C-18 explicitly lists FLS table as valid — "privilege escalation table, sharing rule table, team membership table, or FLS table"; minimum viable threshold met |

**Score: 145/145** | All Essential: YES

> Key finding: FLS table (Phase 2) qualifies for C-18. Minimum-viable inertia does not require restructuring Phase 3 — one Phase 2 inertia column plus one Phase 3 inertia column satisfies the threshold.

---

### V-03 — Phase 2 Gap ID threading, no inertia (C-18 null by design)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-17 | All carried criteria | **PASS** | Gap IDs extended into Phase 2 tables adds backward traceability; all provenance and structural criteria hold |
| C-18 | Inertia Column Framing | **FAIL** | No inertia columns present by design; counterfactual framing absent from all tables |

**Score: 140/145** | All Essential: YES

---

### V-04 — Phase 2 Gap ID threading + inertia on all Phase 3 tables (combined)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-17 | All carried criteria | **PASS** | Phase 2 Gap IDs extend backward traceability; Phase 3 inertia columns on Tables 4, 5, 6; no interference |
| C-18 | Inertia Column Framing | **PASS** | Tables 4, 5, 6 each carry inertia column — 3 qualifying tables; Phase 2 Gap ID threading coexists cleanly with inertia framing |

**Score: 145/145** | All Essential: YES

> Highest structural completeness: C-17 extended to Phase 2 means any FLS anomaly or scope violation discovered early carries a persistent ID forward, making Phase 2-origin gaps mechanically traceable by identifier through Phase 3 inventory into Phase 4.

---

### V-05 — Conversational register; inertia as prose paragraphs (C-18 null by design)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-17 | All carried criteria | **PASS** | Tables remain present; prose paragraphs appear between tables but do not replace them; all structural criteria hold |
| C-18 | Inertia Column Framing | **FAIL** | C-18 requires "at least one inertia column" — prose paragraphs between tables are not columns; the requirement is structurally table-bound, not a style suggestion; conversational framing cannot satisfy it regardless of analytical richness |

**Score: 140/145** | All Essential: YES

---

## Summary Rankings

| Rank | Variation | Score | Delta |
|------|-----------|-------|-------|
| 1 (tie) | V-01 | 145/145 | +15 vs R4 ceiling |
| 1 (tie) | V-02 | 145/145 | +15 vs R4 ceiling |
| 1 (tie) | V-04 | 145/145 | +15 vs R4 ceiling |
| 4 (tie) | V-03 | 140/145 | C-18 absent by design |
| 4 (tie) | V-05 | 140/145 | C-18 fails by design |

---

## Excellence Signals

**Signal 1 — FLS table is a valid C-18 qualifying table (V-02)**
C-18 explicitly lists the FLS table alongside escalation, sharing, and team tables. V-02 proves minimum viable inertia can be satisfied entirely within Phase 2 structure (Table 2) plus one Phase 3 table. Phase 3 does not need restructuring to meet C-18. This opens a lower-friction path to the ceiling.

**Signal 2 — Phase 2 Gap ID threading is mechanically clean and additive (V-03/V-04)**
Assigning persistent Gap IDs at first discovery in Phase 2 tables (FLS, record scope) extends backward traceability without any conflict with C-16 inventory (which only gates Phase 3 IDs) or C-15 provenance (which operates at the Table 7 cell level). V-04 combines Phase 2 threading with Phase 3 inertia and reaches 145/145 with no friction.

**Signal 3 — Column format is structurally mandatory for C-18, not a style option (V-05)**
Prose paragraphs between tables — even analytically rich ones — do not satisfy C-18. V-05 confirms the criterion is mechanically enforced: inertia must be column-bound to be auditable row-by-row. "What breaks if this access is removed?" written as a paragraph cannot be tied to a specific table row. The column format is the enforcement mechanism.

**Signal 4 — Inertia on all three Phase 3 tables provides headroom (V-01/V-04)**
Two tables satisfy C-18; three provide headroom against partial-credit disputes (e.g., a table with a single-row body where the inertia column has one populated cell). Covering all three Phase 3 analytical tables also creates symmetric depth — every positive and null gap finding carries a counterfactual dimension.

---

```json
{"top_score": 145, "all_essential_pass": true, "new_patterns": ["FLS table (Phase 2) qualifies as a C-18 analytical table — minimum viable inertia needs only two tables total and can include Phase 2 structure", "Phase 2 Gap ID threading extends backward traceability without friction against C-16 inventory or C-15 provenance, and combines cleanly with Phase 3 inertia columns", "Inertia column format is mechanically mandatory — prose paragraphs between tables fail C-18 regardless of analytical richness; the column is the row-level audit mechanism"]}
```
