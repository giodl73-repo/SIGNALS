`sim/simulations/quest/golden/trace-inspect-variate-R13-2026-03-17.md`

---

**Round 13 -- 5 variations targeting C-28 and C-29 (rubric v9, 103.5 pts)**

**Baseline**: R12 V-04 carries C-01 through C-27 PASS (102.5/103.5). Two new criteria from R12 excellence signals:

| Criterion | Pattern | What it requires |
|-----------|---------|-----------------|
| C-28 | VERDICT-TO-TABLE TRACEABILITY | Each EG finding ID cited in the EVIDENCE ANCHOR must resolve to a specific Step 3b row (excerpt, Source, Severity). Fabricated or mis-remembered IDs are structurally blocked. |
| C-29 | PROMOTION COUNT FORWARD-REFERENCE | Phase 5 must carry SA remaining count (from PROMOTION COMPLETENESS GATE) alongside EG count (from EVIDENCE ANCHOR) in a single VERDICT EVIDENCE SUMMARY block. Both classification inputs co-located at verdict time. |

**Variation axes**:

| Var | Axis | Target | Mechanism |
|-----|------|--------|-----------|
| V-01 | Lifecycle emphasis | C-28 | Per-ID resolution sub-table inside EVIDENCE ANCHOR: `Cited ID | Finding excerpt | Source | Severity` for each cited EG ID |
| V-02 | Output format | C-29 | VERDICT EVIDENCE SUMMARY block: two-row table carrying EG count (from EVIDENCE ANCHOR) and SA remaining (from PROMOTION COMPLETENESS GATE) |
| V-03 | Phrasing register | C-28 (alt mechanism) | COUNT RECONCILIATION CHECK: Step 3b EG row count must equal EVIDENCE ANCHOR list length; MISMATCH blocks classification (arithmetic rather than resolution) |
| V-04 | Combined V-01+V-02 | C-28 + C-29 | Resolution sub-table + VERDICT EVIDENCE SUMMARY together |
| V-05 | Full integration | C-28 + C-29 + secondary | V-04 plus V-03's COUNT COMPLETENESS CHECK as a second layer (detects selective citation -- omitting Step 3b EG rows that complicate the verdict), plus expanded inertia block naming inertia behaviors 8, 9, 10 |

**Key design decision in V-05**: The resolution sub-table (V-01) confirms IDs are real. The count-completeness check (V-03) confirms the list is exhaustive. Together they close both attack vectors: fabricated IDs *and* cherry-picked citations. V-04 can only close the fabrication vector; V-05 closes both.
