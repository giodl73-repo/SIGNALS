Written to `simulations/quest/rubrics/topic-new-rubric-v18-variate-R20-2026-03-15.md`.

---

## R20 Variation Map

| ID | Axis | Single/Combined | Key change |
|----|------|-----------------|------------|
| **V-01** | Inertia framing | Single (C-58 only) | Replace description column with instrument-class column (`gate / schema`) — two-column map. Minimal R19 V-01 base, no BEFORE/AFTER, no PCR FER citations, no C-59. |
| **V-02** | Output format | Single (C-59 only) | Upgrade PCR header from prohibition form ("Silent omission is not permitted") to present-tense declaration ("FER coverage **is** auditable by structural inspection of this table, not by content inference"). R19 V-04 base, no C-58. |
| **V-03** | Phrasing register | Single (C-58 supplement form) | Add instrument-class as THIRD column to existing description table — three-column OVERRIDE MISSION. R19 V-05 base (C-59 already present). Tests whether description + instrument-class is stronger than instrument-class-only. |
| **V-04** | Combined | C-58 (replace) + C-59 | Instrument-class-only table (two-column, replace form) + auditability declaration. R19 V-04 base. Tests whether losing the description column creates a C-49 regression. |
| **V-05** | Full integration | C-58 (supplement) + C-59 | Three-column OVERRIDE MISSION (description + instrument class). R19 V-05 base. C-59 already present. Closes the only remaining gap (C-58) in R19 V-05. |

**Key structural finding**: R19 V-05 already satisfies C-59 — its PCR header contains the exact auditability phrase. The only new gap from R19 V-05 is C-58's instrument-class column requirement. V-04 vs. V-03/V-05 tests the critical design question: replace the description column (loses C-49 narrative purpose) vs. supplement it (preserves C-49, satisfies C-58).
