**campaign-behavior R4 variations written** to `simulations/quest/golden/campaign-behavior-variate-R4-2026-03-17.md`

---

## Round 4 Summary

Five variations generated against the v4 rubric (C-01--C-18):

| Variation | Axis | New criteria targeted |
|-----------|------|-----------------------|
| **V-01** | Output format -- labeled-field prose blocks, no tables | C-15, C-18 inherited |
| **V-02** | Role sequence -- behavior-first (lifecycle+trigger → contract+state+permissions) | C-15, C-18 inherited |
| **V-03** | Inertia framing -- assumption-displacement per phase (not just preamble) | C-15, C-18 inherited |
| **V-04** | Combination -- R3 V-04 skeleton + CONFIRMED/RUNTIME ANOMALY at calibration time | C-15, C-16, C-18 |
| **V-05** | Combination -- all four new criteria simultaneously | C-15, C-16, C-17, C-18 |

**Predicted ranking:** V-05 >= V-04 > V-03 > V-01 > V-02

**Key architectural bets this round:**

- **V-01** tests whether rubric criteria are format-dependent or structure-dependent. If tables are load-bearing, prose will fail; if intent is what scores, prose should pass.
- **V-02** inverts R3 V-02's contract-anchor sequence — observing behavior first then diagnosing root causes. The behavioral leads mechanism is a novel pattern not present in any R3 variation.
- **V-03** makes inertia framing recurrent — each phase gate closes with a confirmed/displaced declaration. R3 V-05 used inertia only as a preamble; this tests whether per-phase framing improves analysis depth.
- **V-04** is the conservative high-scorer: minimum change to R3 V-04 (proven structure) to close C-16. CONFIRMED classification happens at calibration time (step 6b) rather than inline during execution — a structural difference from R3 V-02's mid-phase approach.
- **V-05** is the architectural experiment: the primary unknown is whether C-17 (interrogative calibration) and the formal CALIBRATION BLOCK are mutually exclusive or coexistent. If compatible, V-05 is the first maximum-aspirational-credit candidate on the v4 rubric.
