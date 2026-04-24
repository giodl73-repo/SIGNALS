Written to `simulations/quest/golden/campaign-evidence-golden-2026-03-17.md`.

**Summary:**

- **Score:** 100.75 — full marks on all 50 criteria (Essential 60 + Recommended 30 + Aspirational 10.75)
- **Source:** Round 20, V-05, QU5-simplified (3070 → 2452 words, 20.1% reduction, all criteria intact)
- **What made it golden** — 4 key patterns:
  1. **Three-tier IB-ID homogeneity (C-50):** HOMOGENEITY INVARIANT named in preamble; N/A cells carry `[IB-XXX]` alongside their structural reason, not English names alone
  2. **FK-typed audit table (C-49):** `Antipattern (IB-ID FK)` column populated exclusively with IB-IDs — join-auditable against the fixture by identifier lookup, no name-string interpretation
  3. **Typed-ID-only binary annotations (C-48):** English antipattern name stripped from cell body; `[IB-ATTR]` alone, not `no attribution collapse [IB-ATTR]`
  4. **All three together:** The combination enables a single `[IB-XXX]` identifier-syntax scan to fully audit every cell in the apparatus — binary, N/A, and audit table — with zero name-matching at any point. No prior variation achieved this
