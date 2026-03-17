Written to `simulations/quest/rubrics/flow-dataflow-rubric-v18-R18-2026-03-15.md`.

---

## Round 18 Variations — Summary

**5 complete prompt bodies produced.**

### Variation axes

| | Axis | Scenario | Role Order | Skip-Level |
|--|------|----------|-----------|------------|
| **V-01** | DETECTABILITY INDEX (standalone) + C-53 full dual-slot | B2B wholesale order-to-cash | F→O→C (natural) | Commerce cites Finance [A-04] |
| **V-02** | Non-natural role sequence | F&B manufacturing ingredient procurement | O→F→C | Commerce cites Operations [A-04] |
| **V-03** | Prose format + SC-14 | SaaS metered billing → deferred revenue | F→O→C (natural) | Commerce cites Finance [A-04] |
| **V-04** | Max incumbent (≥5 steps) + non-natural | Retail cash reconciliation → GL | C→F→O | Operations cites Commerce [A-04] |
| **V-05** | Phase Gate 0 + SC-0 (14 SCs) + non-natural | Telecom CDR-to-billing-to-GL | O→C→F | Finance cites Operations [A-04] |

### C-52 implementation per variation
- **V-01/V-02/V-04**: Standalone DETECTABILITY INDEX table, 13 rows, placed before STRUCTURAL CONSTRAINTS. Row count = SC count asserted explicitly.
- **V-03**: DETECTABILITY INDEX as numbered prose enumeration (14 items including SC-14).
- **V-05**: DETECTABILITY INDEX table with 14 rows (SC-0 through SC-13); Phase Gate 0 [A-00] includes an explicit checklist item requiring the model to verify row count = 14 before Role 1 begins.

### C-53 implementation
All SCs that reference any `[A-xx]` token name those tokens in **both** the governed-artifact slot and the enforcement clause throughout all five variations — not limited to [A-01]-bearing SCs. SC-2 names all six stage/boundary tokens in its enforcement clause; SC-6 names [A-05]/[A-08]; SC-7 names [A-03]/[A-06]/[A-09]; SC-1 names [A-06]/[A-09].
