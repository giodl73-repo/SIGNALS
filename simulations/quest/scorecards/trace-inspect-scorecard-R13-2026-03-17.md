## trace-inspect Scorecard — Round 13 (Rubric v9, 103.5 pts)

**Baseline**: R12 V-04 = 102.5/103.5 (C-01 through C-27 all PASS). Two new criteria in play: C-28 (+0.5) and C-29 (+0.5).

---

### V-01 — Single axis: Lifecycle emphasis (C-28 target)

**Essential Criteria**

| ID | Criterion | Result | Evidence note |
|----|-----------|--------|--------------|
| C-01 | Phase completeness | PASS | All four phases structurally present and closed; inherited from R12 V-04 |
| C-02 | Artifact produced | PASS | Phase 2b artifact write at declared path; inherited |
| C-03 | Schema 1 + Schema 2 compliance | PASS | Full Coverage Matrix with both schemas declared; inherited |
| C-04 | Enforcement gates checked | PASS | G-1/G-2/G-3 with GATE CLEARANCE SUMMARY + PHASE 4 GATE CLEARANCE SUMMARY; inherited |
| C-05 | Verdict present and classified | PASS | NEEDS-SPEC-REVISION / NEEDS-REDESIGN / USEFUL with classification rules; inherited |

All essential: PASS.

**Recommended Criteria**

| ID | Result | Evidence note |
|----|--------|--------------|
| C-06 | PASS | SA-TO-SG PROMOTION block with per-gap evaluation + PROMOTES TO SG / REMAINS SA; inherited |
| C-07 | PASS | Per-role relay with all required fields including Schema 2 compliance; inherited |
| C-08 | PASS | Findings table floor check requires >= 3 findings / >= 2 Source types; inherited |

**Aspirational Criteria (new only; C-09 through C-27 all INHERITED PASS)**

| ID | Criterion | Result | Evidence note |
|----|-----------|--------|--------------|
| C-28 | Verdict-to-table traceability | PASS | VERDICT-TO-TABLE TRACEABILITY sub-table explicitly present inside NEEDS-REDESIGN EVIDENCE ANCHOR: `Cited ID \| Step 3b Finding excerpt \| Source \| Severity` for each cited EG ID; traceability check verifies each cited ID has a resolution row; blocks classification if any ID lacks a resolution row |
| C-29 | Promotion count forward-reference | FAIL | V-01 adds only the TRACEABILITY sub-table; no VERDICT EVIDENCE SUMMARY block is present; SA remaining count not co-located with EG count in Phase 5 |

**Composite: 103.0 / 103.5**

---

### V-02 — Single axis: Output format (C-29 target)

**Essential Criteria**: all PASS (inherited)
**Recommended Criteria**: all PASS (inherited)
**Aspirational C-09 through C-27**: all PASS (inherited)

**New criteria:**

| ID | Criterion | Result | Evidence note |
|----|-----------|--------|--------------|
| C-28 | Verdict-to-table traceability | FAIL | No per-ID resolution sub-table; EVIDENCE ANCHOR lists EG finding IDs but does not resolve each to a Step 3b row; V-02 axis is output format (C-29), not traceability |
| C-29 | Promotion count forward-reference | PASS | VERDICT EVIDENCE SUMMARY block present in Phase 5 with two rows: EG count (sourced from EVIDENCE ANCHOR list) and SA remaining (sourced from PROMOTION COMPLETENESS GATE); both classification inputs co-located; no Phase 2 re-read required; PROMOTION COMPLETENESS GATE also carries "SA remaining (certified): R — forward-referenced in Phase 5 VERDICT EVIDENCE SUMMARY" annotation creating bidirectional link |

**Composite: 103.0 / 103.5**

---

### V-03 — Single axis: Phrasing register (C-28 alternative — count-reconciliation check)

**Essential Criteria**: all PASS (inherited)
**Recommended Criteria**: all PASS (inherited)
**Aspirational C-09 through C-27**: all PASS (inherited)

**New criteria:**

| ID | Criterion | Result | Evidence note |
|----|-----------|--------|--------------|
| C-28 | Verdict-to-table traceability | FAIL | COUNT RECONCILIATION CHECK compares Step 3b EG row count vs EVIDENCE ANCHOR list length; confirms no surplus IDs, but does not resolve each ID to its Step 3b row content (Finding excerpt / Source / Severity); a model can write F-03 when Step 3b has F-02 — counts match but IDs are wrong; C-28 requires per-ID resolution auditable from the block alone; count-check alone is insufficient |
| C-29 | Promotion count forward-reference | FAIL | No VERDICT EVIDENCE SUMMARY block; SA remaining not co-located with EG count in Phase 5 |

The COUNT RECONCILIATION CHECK is a weaker mechanism that detects ID count overflow but cannot detect ID substitution (wrong IDs that happen to number correctly). It closes one attack vector (fabricated-ID surplus) but not the other (incorrect IDs, wrong content references).

**Composite: 102.5 / 103.5** (baseline — no new criteria met)

---

### V-04 — Combined: C-28 + C-29

**Essential Criteria**: all PASS (inherited)
**Recommended Criteria**: all PASS (inherited)
**Aspirational C-09 through C-27**: all PASS (inherited)

**New criteria:**

| ID | Criterion | Result | Evidence note |
|----|-----------|--------|--------------|
| C-28 | Verdict-to-table traceability | PASS | VERDICT-TO-TABLE TRACEABILITY sub-table present (identical to V-01): each cited EG finding ID resolved to its Step 3b row; classification blocked if any cited ID lacks a resolution row |
| C-29 | Promotion count forward-reference | PASS | VERDICT EVIDENCE SUMMARY block present (identical to V-02): EG count and SA remaining co-located in Phase 5; PROMOTION COMPLETENESS GATE lacks the "certified: R — forward-referenced" annotation present in V-02, but the EVIDENCE SUMMARY block itself satisfies C-29 |

Both new criteria pass. Phase 5 verdict section is fully self-contained: EVIDENCE ANCHOR lists EG IDs, TRACEABILITY sub-table resolves each ID, EVIDENCE SUMMARY co-locates both classification inputs.

**Composite: 103.5 / 103.5** (perfect under v9)

---

### V-05 — Full integration: C-28 + C-29 + COUNT COMPLETENESS CHECK + expanded inertia

**Essential Criteria**: all PASS (inherited)
**Recommended Criteria**: all PASS (inherited)
**Aspirational C-09 through C-27**: all PASS (inherited)

**New criteria:**

| ID | Criterion | Result | Evidence note |
|----|-----------|--------|--------------|
| C-28 | Verdict-to-table traceability | PASS | VERDICT-TO-TABLE TRACEABILITY sub-table present; AND COUNT COMPLETENESS CHECK layered after it: Step 3b EG row count K must equal TRACEABILITY sub-table row count N; K ≠ N blocks classification; this closes the selective-citation attack vector V-01/V-04 leave open (a model could list only 3 of 5 EG IDs — all 3 resolve correctly, but 2 EG findings are silently omitted; count-check catches this) |
| C-29 | Promotion count forward-reference | PASS | VERDICT EVIDENCE SUMMARY present; PROMOTION COMPLETENESS GATE carries "SA remaining certified: R — forward-referenced in Phase 5 VERDICT EVIDENCE SUMMARY" annotation |

V-05 exceeds V-04 structurally: per-ID resolution proves IDs are real; COUNT COMPLETENESS CHECK proves the list is exhaustive. Together they provide mutual verification covering both fabrication (V-01/V-04 mechanism) and selective omission (V-05 addition). Inertia block extended to 10 behaviors, explicitly naming fabricated-ID citation (item 8), selective citation (item 9), and disconnected verdict/promotion data (item 10).

No new rubric criteria are activated beyond C-28 and C-29 (V-05 strengthens C-28 mechanism but does not unlock a new criterion slot under v9). Score is identical to V-04.

**Composite: 103.5 / 103.5** (perfect under v9)

---

## Ranking

| Rank | Variation | Score | C-28 | C-29 | Notes |
|------|-----------|-------|------|------|-------|
| 1 | V-05 | 103.5 / 103.5 | PASS | PASS | Per-ID resolution + COUNT COMPLETENESS CHECK + VERDICT EVIDENCE SUMMARY + expanded inertia |
| 1 | V-04 | 103.5 / 103.5 | PASS | PASS | Per-ID resolution + VERDICT EVIDENCE SUMMARY; no completeness guard |
| 3 | V-01 | 103.0 / 103.5 | PASS | FAIL | Per-ID resolution only |
| 3 | V-02 | 103.0 / 103.5 | FAIL | PASS | VERDICT EVIDENCE SUMMARY + forward-certification annotation only |
| 5 | V-03 | 102.5 / 103.5 | FAIL | FAIL | Count-reconciliation insufficient for C-28; no C-29 |

**Top variation**: V-05 (with V-04 tied on score; V-05 is structurally stronger within C-28 but does not yield additional points under v9).

---

## Excellence Signals from V-05

**Signal 1 — COUNT COMPLETENESS CHECK**
After the VERDICT-TO-TABLE TRACEABILITY sub-table, V-05 adds: Step 3b EG row count K must equal TRACEABILITY sub-table row count N; K ≠ N = INCOMPLETE; classification blocked. This closes the selective-citation attack vector: a model can satisfy C-28 (all cited IDs resolve correctly) while omitting inconvenient EG findings from the verdict citation. Per-ID resolution and count-completeness are mutual verification: resolution proves IDs are real; completeness proves the list is exhaustive. Neither check alone closes both vectors.

**Signal 2 — FORWARD-CERTIFICATION ANNOTATION AT SOURCE**
Both V-02 and V-05 annotate the PROMOTION COMPLETENESS GATE with: "SA remaining certified: R — forward-referenced in Phase 5 VERDICT EVIDENCE SUMMARY." This creates a bidirectional link: Phase 5 pulls SA remaining from Stage 2 (via the EVIDENCE SUMMARY), and Stage 2 declares where its certified value will appear. A scorer reading either section knows the data flow without searching. This annotation pattern generalizes: any block that produces a value consumed downstream should declare its consumer at the point of production.

---

```json
{"top_score": 103.5, "all_essential_pass": true, "new_patterns": ["COUNT COMPLETENESS CHECK — Step 3b EG row count must equal TRACEABILITY sub-table row count; INCOMPLETE blocks classification; closes the selective-citation attack vector where per-ID resolution alone passes (all cited IDs are real) but EG findings inconvenient to the verdict are silently omitted", "FORWARD-CERTIFICATION ANNOTATION AT SOURCE — PROMOTION COMPLETENESS GATE labels SA remaining as certified and declares its Phase 5 VERDICT EVIDENCE SUMMARY consumer at the point of production, creating a bidirectional traceable link between Stage 2 and Phase 5"]}
```
