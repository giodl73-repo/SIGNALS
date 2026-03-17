Written to `simulations/quest/golden/campaign-evidence-variate-R11-2026-03-16.md`.

---

## Summary

**New baseline for R11** (inherited from prior rounds, now standard): C-22 (binary `[ Yes / No ]`), C-23 (stage-index suffix), C-24 (entry/exit gates), C-27 (blank gate template in preamble), C-30 (named role handoffs), C-31 (negative invocations at non-applicable stages).

**Checksum arithmetic for all 5 variates:** 4 rules × 5 stages = 20 cells → 12 positive + 8 negative.

---

### Variation axes

| Variate | Axis | Primary target | Structural differentiator |
|---------|------|---------------|--------------------------|
| V-01 | Role Sequence (single) | C-30, C-32 | Access scope is an information boundary: scope violation = role charter violation, detectable without parsing stage order |
| V-02 | Output Format (single) | C-33, C-26 | Running audit table with append-per-invocation instruction; checksum is an arithmetic verification cell in the final output |
| V-03 | Lifecycle Emphasis (single) | C-17, C-19, C-27 | Phase 0 / Phases 1-5 / Phase 6 lifecycle; Phase 0 is a commitment ledger that must be fully populated before Stage 1 begins |
| V-04 | Role Sequence + Output Format (combined) | C-32, C-33 | Roles produce signed artifacts; handoffs transfer artifact custody; audit table uses artifact names not just stage numbers |
| V-05 | Lifecycle Emphasis + Phrasing Register (combined) | All governance rules | SHALL/MUST throughout; "compliant if and only if" frame; delivery gate as a hard constraint not a suggestion |

**C-32 placement:** Role roster table in preamble for all variates; repeated as role declaration header at each stage boundary.

**C-33 placement:** Coverage map table with positive/negative column totals; pre-declared derivable expression `20 = 12 + 8 = 4 × 5`; verified as arithmetic cell at output close.
