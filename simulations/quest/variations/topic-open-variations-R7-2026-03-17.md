Written to `simulations/quest/golden/topic-open-variate-R7-2026-03-17.md`.

---

# topic-open — Round 7 Variations

**Rubric**: v7 (C-01–C-30, denominator 22)
**Base**: R6 V-05 (passes C-25, C-26, C-27 + all prior criteria)

---

## Variation axes

| V | Axis | Hypothesis |
|---|------|------------|
| V-01 | **C-28** — Declared schema | Add a `DECISION TABLE SCHEMA` block before Phase 1 that explicitly names Path/Action/Consequence and defines each column. Converts column consistency from an *observed* property to an *asserted* one — auditable and pre-loaded for any table that follows. |
| V-02 | **C-29** — Enforcement mechanism | Every gate and checklist citation adds the field reference + operation: `topic-status F-01 exact string match`, `topic-status F-01 essential-row count`, `topic-scanner F-04 pattern glob`, `topic-status F-05 unique-value count`. Mechanism-level citations close the inferential gap between "this tool enforces it" and "this is exactly how." |
| V-03 | **C-30** — Self-contained if/if | All `(see Phase X Decision above)` delegation removed from instruction bodies. Phase 1, 2, 3, and 5 instructions now carry their own if/if directly in the instruction text. Decision tables remain — they are structural pre-phase elements — but the instruction body no longer depends on the reader having internalized the preceding table. |
| V-04 | **C-28 + C-29** | Schema declaration + mechanism citations simultaneously. Two independent precision layers: column grammar declared once at document level, enforcement contracts specified at field level in every gate and checklist item. |
| V-05 | **C-28 + C-29 + C-30** | Full integration. Schema declared, mechanisms cited, all instructions self-contained. The three axes operate at distinct structural depths (table frame, enforcement annotations, instruction body) and stack without interference. |

---

## Key structural decisions

**V-01 vs V-03 on delegation**: V-01 keeps `(see Phase X Decision above)` references (failing C-30). V-03 removes all of them but adds no schema block. This isolates the C-30 axis cleanly.

**V-02 ordering**: Phase 1 Setup appears before Phase 1 Decision in V-02 (intentional single-axis isolation of C-29; ordering unchanged from how R6 V-02 handled structure). All other variations use decision-table-before-instruction ordering.

**C-23 coverage**: All five variations place decision tables immediately before their corresponding phase instruction (Phase 1 Decision → Phase 1 Setup, etc.), satisfying C-23 and C-27. V-02 is the only variation where Phase 2 Decision precedes Phase 1 Setup — a minor ordering anomaly that should not affect C-23 since Phase 1 still has a decision table.

**Mechanism format (C-29)**: Citations follow `tool` + `what` + `via` + field reference + operation. Examples: `topic-status F-01 exact string match (tests each F-01 priority cell against {essential, recommended, optional})`, `topic-scanner F-04 pattern glob (matches F-04 item names against {topic}-*-YYYY-MM-DD.md)`. The parenthetical specifies the mechanism that C-25's two-slot format does not require.
