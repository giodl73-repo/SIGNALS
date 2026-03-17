**R6 variations written** to `simulations/quest/golden/listen-support-variate-R6-2026-03-16.md`.

---

## Summary

**5 complete variations targeting C-21 + C-22 under rubric v6:**

| Variation | Axis | C-21 mechanism | C-22 mechanism | Confidence |
|-----------|------|---------------|---------------|------------|
| **V-01** | Output format | Gap IDs + discrete traceability table (Step 9B) + ORPHAN-GAP CHECK with halt | — | C-21 HIGH / C-22 FAIL |
| **V-02** | Lifecycle emphasis | — | Step 9B CONSEQUENCE FIELDS with Prohibited sentinel + SENTINEL COMPLIANCE CHECK | C-21 FAIL / C-22 HIGH |
| **V-03** | Phrasing register | Inline `Supporting ticket(s)` column + orphan count in coverage block | Inline Prohibited note in consequence column header | C-21 PARTIAL / C-22 PARTIAL |
| **V-04** | V-01 + V-02 combined | Traceability table + orphan check (Step 9C) | Sentinel-protected consequence step (Step 9B) | Both HIGH |
| **V-05** | Full synthesis | Gap IDs in table + inline citation column + traceability table + orphan check | Inline Prohibited column note + per-gap narrative step + compliance check | Both HIGH |

**Key design decisions:**
- **C-21** requires a two-lookup chain: gap table → traceability table → ticket body. V-01/V-04/V-05 all create this via a discrete `GAP-TICKET TRACEABILITY TABLE` step with Gap IDs as the shared key.
- **C-22** requires sentinel prohibitions on consequence fields AND a post-generation compliance check. V-02/V-04/V-05 add a named `SENTINEL COMPLIANCE CHECK` block that quotes each fill verbatim.
- **V-05** is the betting favorite: belt-and-suspenders on both criteria (inline columns survive if the dedicated steps are compressed; dedicated steps satisfy the scorer if inline columns are deemed insufficient), plus an explicit `FINAL VERIFICATION` spine that names C-21 and C-22 by criterion ID.
