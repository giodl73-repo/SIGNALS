Written to `simulations/quest/golden/topic-retro-variate-R13-2026-03-17.md`.

---

**R13 variations summary:**

| ID | Axis | C-32 mechanism | C-33 mechanism |
|----|------|----------------|----------------|
| V-01 | C-32 single | Phase 8 SEAL: per-field `CHECK:` / `HOW:` blocks with self-contained sources — no item references a sibling | Two-column table unchanged |
| V-02 | C-33 single | Three-field SEAL unchanged | Three-column table adds `Verified in` — converts table from summary to audit map |
| V-03 | Phrasing register | Phase 8 SEAL: `ITEM / VERIFY / SOURCE / FORMAT / RESULT` receipt format | `ENFORCE IN:` inline annotation per row |
| V-04 | C-32 + C-33 combined | V-01 CHECK/HOW blocks | V-02 three-column table |
| V-05 | Full integration | CHECK/HOW in Phase 8 + extended to Phase 1 Echo and Phase 7 slot check | 12-row table splitting Copy guard into three independent rows + trailing DESIGN GUARANTEES section with bidirectional cross-links |

**Key design decision in V-05:** The PRE-EXECUTION CONTRACT splits "Copy guard — SEAL" into three rows (one per field), making the table mechanism-keyed at field granularity. A scorer auditing C-32 finds each Phase 8 SEAL item in its own contract row, and each contract row points back to its SEAL item. The trailing DESIGN GUARANTEES duplicates this structure for post-execution audit.
