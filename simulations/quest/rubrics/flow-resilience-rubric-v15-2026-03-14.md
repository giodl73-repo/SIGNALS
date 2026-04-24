Written to `simulations/quest/rubrics/flow-resilience-rubric-v15-2026-03-15.md`.

---

**v15 summary — what changed:**

| | v14 | v15 |
|---|---|---|
| Denominator | 35 | **38** |
| New criteria | C-41, C-42, C-43 | **C-44, C-45, C-46** |
| R14 ceiling | 100.00 (35/35) | **99.21 (35/38)** |
| R15 ceiling | open | **99.74 (37/38) — V-05** |

---

**Three new criteria extracted from R15:**

**C-44 — Failure Signature Class Boundary Discriminator** *(E-36)* — The Failure Signature column specification (C-43) includes a named structural element (blockquote or sub-section) specifying operationally distinct fill requirements for Class 2 vs. Class 3: Class 3 must show node-A/node-B diverging state (inter-node divergence); Class 2 must show transaction-level anomaly from a single write path (intra-transaction inconsistency). Closes the Class 2/3 behavioral collapse escape within the Failure Signature context. V-03 and V-05 PASS; V-01, V-02, V-04 FAIL.

**C-45 — SLA Budget Placeholder Negation and Per-Row Invention Prohibition** *(E-37)* — Two enforcement mechanisms beyond C-42's reference-source contract: (1) explicit "TBD fails" placeholder negation making every cell in the 12-cell matrix non-bypassable by deferral; (2) explicit per-row SLA invention named as a contract violation. V-02 PASS (both mechanisms present); V-04 and V-05 have the contract-violation language but lack the TBD negation (FAIL).

**C-46 — Unified Pre-Commitment Document with Four Named Sub-Parts** *(E-38)* — The Inertia Assessment (C-41) and SLA Budget (C-42) are integrated into a single named pre-commitment document with four labeled sub-parts (framing / carrying cost / tipping point / SLA Budget). Row descriptors cross-reference both the carrying-cost sub-part and the SLA Budget sub-part by label in the same row. Two separate sections — even if each has internal labels — fail. V-04 (Acts I–IV) and V-05 (Steps 1a–1d) PASS; V-01, V-02, V-03 FAIL.

---

**R15 per-variation scores under v15:**

| Variation | C-41 | C-42 | C-43 | C-44 | C-45 | C-46 | Total | Composite |
|---|---|---|---|---|---|---|---|---|
| V-01 | PASS | FAIL | FAIL | FAIL | FAIL | FAIL | 33/38 | 98.68 |
| V-02 | FAIL | PASS | FAIL | FAIL | PASS | FAIL | 34/38 | 98.95 |
| V-03 | FAIL | FAIL | PASS | PASS | FAIL | FAIL | 34/38 | 98.95 |
| V-04 | PASS | PASS | FAIL | FAIL | FAIL | PASS | 35/38 | 99.21 |
| V-05 | PASS | PASS | PASS | PASS | FAIL | PASS | 37/38 | **99.74** |

The 100.00 ceiling requires all six post-C-40 axes: C-41 through C-46. No R15 variation achieves it — C-45's TBD placeholder negation remains unimplemented by the two most complete variations.
