`sim\simulations\quest\golden\trace-inspect-variate-R14-2026-03-17.md`

---

## trace-inspect -- Variations R14 v10 (2026-03-17)

**Entry state**: R13 V-05 scores 103.5/103.5 (rubric v9). Rubric v10 adds C-30 and C-31 (0.5 pts each). Baseline = 103.5/104.5.

**What C-30 and C-31 address**:
- R13's COUNT COMPLETENESS CHECK used count-equality (K=N). C-30 requires per-ID key lookup: each cited EG ID is individually confirmed as an actual Step 3b row label. Count equality cannot detect ID substitution (F-07 cited when Step 3b has F-02 — counts match, wrong ID).
- R13 V-05 had one bidirectional annotation (PROMOTION COMPLETENESS GATE → VERDICT EVIDENCE SUMMARY). C-31 extends the pattern to all four forward-referencing blocks, making C-26 through C-29 self-certifying.

---

### Variation Summary

| Variation | Axis | Target | Key structural change |
|-----------|------|--------|-----------------------|
| **V-01** | Lifecycle emphasis | C-30 | PER-ID MEMBERSHIP VERIFICATION table replaces count-equality check: one row per cited EG ID with YES/NOT FOUND; classification BLOCKED on NOT FOUND |
| **V-02** | Output format | C-31 | Expanded bidirectional annotations on all four forward-referencing blocks: EVIDENCE ANCHOR → TRACEABILITY sub-table (and back); VERDICT EVIDENCE SUMMARY → both source blocks (and back) |
| **V-03** | Phrasing register | C-30 (alt) | Inline per-ID membership notation within the EVIDENCE ANCHOR list itself: `[F-NN] (Step 3b row label: confirmed)` at the point of citation; no separate block |
| **V-04** | Combined | C-30 + C-31 | V-01 membership table PLUS V-02 bidirectional annotations |
| **V-05** | Full integration | C-30 + C-31 + inertia | V-04 plus inertia items 11 (ID substitution, closes C-30) and 12 (forward-reference opacity, closes C-31) |

### Key structural difference between V-01 (C-30) and R13's count check

R13 V-05 COUNT COMPLETENESS CHECK: `Step 3b EG rows: K | sub-table rows: N | K = N: COMPLETE` — detects omission, not substitution.

V-01 PER-ID MEMBERSHIP VERIFICATION:
```
| Cited ID | Step 3b row label exists | Membership result |
|----------|--------------------------|------------------|
| F-07     | NOT FOUND                | BLOCKED           |
```
Each key is looked up. F-07 cited, F-07 missing from Step 3b → BLOCKED. Count equality would have passed.

### V-03 hypothesis under rubric v10

V-03 uses inline notation rather than a dedicated table. The C-30 pass condition requires the check to be "auditable ID by ID — enumerating each cited ID and its resolution status." V-03 satisfies the per-ID requirement but not the block-based auditability. Expected scorecard result: C-30 PARTIAL or FAIL depending on whether the rubric treats inline enumeration as sufficient. The scorecard will resolve this.
