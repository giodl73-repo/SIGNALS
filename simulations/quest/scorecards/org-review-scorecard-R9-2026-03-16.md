**E-04 — Consistent bracket dimension format** (continued)
V-05 (and V-04) use Dimension format throughout: opening → domain re-score → closing aggregation. V-02 broke this by leaving the bracket closing in A/B/C option format, triggering a C-16 regression. V-05 confirms the dimension approach is the canonical format for the full bracket.

**E-05 — §17 + §18 paired in preamble**
Co-locating both protocols in the preamble establishes the C-33 → C-34 dependency at declaration time. §17 creates the applicability ratings; §18 references those ratings as its source. The preamble declares the full pipeline before any reviewer executes.

---

## Ranking

1. **V-05** — 225/225 — canonical perfect: all three new criteria, consistent format, strict dependency chain
2. **V-04** — 220/225 — strong two-axis: C-33 + C-35, correct format throughout, C-34 absent
3. **V-01** — 215/225 — clean single-axis: C-33 only, no regressions
4. **V-02** — 210/225 — C-35 earned but C-16 regressed; net zero gain over base
5. **V-03** — 210/225 — gap-check machinery present but C-34 fails on proxy criterion; net zero gain over base

---

```json
{"top_score": 225, "all_essential_pass": true, "new_patterns": ["C-34 gap-check uses C-33 applicability tier as direct source: COVERED requires HIGH-applicability + ADDRESSED, not ADDRESSED alone — C-33 data is necessary for C-34 to pass", "§1 scope annotation serves dual downstream consumers: §5.5 scope-coverage reconciliation and §5.7 domain gap-check — scope inventory exhaustiveness now enforced by two sections", "§5.7 domain gap-check explicitly excluded from gate ledger in §8 — non-verdict exclusion pattern extended to new section, preventing C-21 ambiguity"]}
```
