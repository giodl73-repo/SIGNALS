Written to `simulations/quest/golden/campaign-simulate-variate-R13-2026-03-17.md`.

---

**Round 13 summary:**

| Variation | Axis | New Target | SAD Rows | Key Mechanism |
|-----------|------|-----------|----------|---------------|
| V-01 | Output format | C-26 | 8 | REMEDIATION QUALITY GATE: Verb/Target/Location/Conformance per F-ID; Verb constrained by Type |
| V-02 | Correctness | C-27 | 8 | TOPIC ENTITY MANIFEST + ENTITY COVERAGE MATRIX: COVERED/CLEAN/SKIPPED per entity; SKIPPED = execution gap |
| V-03 | Phrasing register | C-28 | 8 | BLAST RADIUS RE-ASSESSMENT GATE after Step 3; ELEVATED inline on Updated Ranked Findings; re-sort |
| V-04 | Output + phrasing | C-26 + C-28 | 9 | Remediation Quality Gate gains 5th column (Blast Status = ORIGINAL or REASSESSED:P-ID); closed verification loop |
| V-05 | Full integration | C-26 + C-27 + C-28 | 15 | R12 V-05 12-axis base + 3 new axes; Row Count Assertion counts to 15; C-44 preserved at 15-axis scope |

**Three architectural decisions in V-05 to watch in scoring:**
1. **Blast Status column in Remediation Quality Gate** — creates a third C-28 verification path (column scan) independent of the Re-Assessment Gate section and the Updated Ranked Findings section
2. **Type-verb dual-column check** — Findings Table Verb field AND Remediation Quality Gate Verb column must agree; adds a cross-artifact C-31 verification path
3. **15-axis Row Count Assertion** — C-44's dual-property zero-scan (self-reference + count inline) is preserved at the new scope of 15, not just 12
