Both files written:

- `simulations/quest/golden/campaign-evidence-variate-R20-2026-03-17.md` — 5 complete runnable prompt bodies
- `simulations/quest/variations/campaign-evidence-variations-R20-2026-03-17.md` — variation plan + isolation matrix

---

**Round 20 summary:**

Three new criteria from R19-V-05's excellence signals, with a clean discrimination:

| | C-48 | C-49 | C-50 |
|---|---|---|---|
| V-01 | PASS | FAIL | FAIL |
| V-02 | FAIL | PASS | FAIL |
| V-03 | FAIL | FAIL | PASS |
| V-04 | PASS | PASS | FAIL |
| V-05 | PASS | PASS | PASS |

**Key discrimination logic:**

- **C-48 vs C-50** — The distinction is strictness in the binary tier. C-48 PASS requires `[IB-ATTR]` as the sole annotation (no English name). C-50 PASS allows English+ID in binary cells (`no attribution collapse [IB-ATTR]`) — the requirement is that the N/A tier also carries IB-IDs and the uniformity is declared as the HOMOGENEITY INVARIANT.

- **C-49** — Isolated to the audit table only. The `Antipattern (IB-ID FK)` column turns the audit table into a reference table: values are IB-IDs, join-auditable against the fixture without name-string interpretation.

- **V-05 closing property** — With all three active, every cell in the apparatus (binary form cells, N/A cells, audit table cells) is machine-verifiable by `[IB-XXX]` identifier-syntax scan. No name-matching required at any point.
