Written to `simulations/quest/golden/flow-throttle-variate-R19-2026-03-16.md`.

---

## flow-throttle Variate — Round 19

**R18 gaps under v19:**

| Variant | C-49 | C-50 | C-51 | C-52 | Score |
|---------|------|------|------|------|-------|
| V-01 | FAIL | FAIL | FAIL | FAIL | 290/310 |
| V-02 | PASS | FAIL | FAIL | FAIL | 295/310 |
| V-03 | FAIL | PASS | FAIL | FAIL | 295/310 |
| V-04 | FAIL | PASS | PASS | FAIL | 300/310 |
| V-05 | FAIL | FAIL | FAIL | PASS | 295/310 |

All five R19 variations target 310/310. Axes and mechanisms:

---

**V-01 — Output format (single)**
All four criteria expressed as typed tables/fill-blocks. C-51: 5-column header table with `SHALL NOT activate if` column. C-52: non-conflation statement quotes `"That Section C annotation count = declared count of 7"` verbatim + falsifiability instruction. C-50: G-1 through G-4 each with individual SHALL instruction, concludes with 3-field VERIFICATION STATUS RECORD. C-49: 8-row typed audit table (Item | Criterion | Evidence required | Status) in Field 5.

**V-02 — Role sequence (single)**
Role 1.5 splits into GATE-A (signal distinction + bypass register + bypass gate field) and GATE-B (G-1–G-4 + VERIFICATION STATUS RECORD), both appearing as distinct rows with bypass conditions in the header table. C-52's verbatim quote in GATE-A is explicitly labeled a "quoted-artifact citation." C-49's audit rows follow role-chain activation order.

**V-03 — Lifecycle emphasis (single)**
Phase 0 splits into P0-A through P0-D micro-checkpoints. C-51: `GATE CONDITION — blocked if` column in lifecycle stage overview. C-52: Phase 0.1 entry statement quotes the cell verbatim at the micro-checkpoint where the signal is consumed. C-49: audit rows named as lifecycle phase gate artifacts.

**V-04 — Phrasing register + inertia framing (combined)**
SHALL-contract language throughout. C-51: SHALL NOT ACTIVATE WHEN column (caps). C-52: SHALL reproduce verbatim + blockquote labeled "the SHALL-authoritative cell value." C-50: V-1 through V-4 each with SHALL NOT PROCEED IF condition + MANDATORY STATUS DECLARATION. C-49: `SHALL cite` fourth column in audit table.

**V-05 — Role sequence + output format + inertia framing (combined)**
Maximum density. C-51: 5-column header with all three role-contract facts co-located. C-52: verbatim quote + "string equality is the verification method." C-50: G-1–G-4 each with "Cannot skip because" structural clause. C-49: 9-row audit table adds inertia-bypass confirmation row (C-44/C-47/C-48 combined evidence check).
