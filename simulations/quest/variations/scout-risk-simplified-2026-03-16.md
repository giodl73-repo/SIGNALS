**Simplification Report**

---

**Original V-05 prompt body**: ~1,765 words
**Simplified prompt body**: ~1,394 words
**Reduction**: ~371 words (~21%)

---

**What was removed and why** (25 items):

| # | Location | Removed | Words | Reason |
|---|----------|---------|-------|--------|
| 1 | AMEND check | Full phase-by-phase label list → "all subsequent phases (Phase 0 through Phase 4)" | 37 | Phase numbers identify scope; function labels are orientation only |
| 2 | Phase 0a | "Phase 0a is mandatory when an AMEND directive is present." | 12 | Covered by preamble "execute Phase 0a first" |
| 3 | Phase 0a | "This phase is the only precondition phase." | 9 | Covered by heading "Role-Activation Gate" |
| 4 | Phase 0a | "No table is seeded, no role activates, no register phase begins until..." | 23 | Covered by AMEND check preamble |
| 5 | Phase 0a | "Phase 0a is complete." | 5 | Trivial state announcement |
| 6 | Phase 0 intro | "This block is a pre-phase reference block of equal structural weight to Phase 0c — both declare a closed vocabulary before any generation phase executes." | 28 | Pure meta-commentary; no constraint |
| 7 | Phase 0 intro | "Taxonomy is complete and closed." | 5 | Redundant with canonical closure sentence at block end |
| 8 | Phase 0b intro | "No row in Table 1 (Phase 1) or Table 2 (Phase 1b and Phase 2) is written before this phase completes." | 22 | Redundant with "Declare the row schema before any row is populated" |
| 9 | Phase 0b FRCD | Parenthetical schema descriptions per phase | 29 | Phase names alone identify scope |
| 10 | Phase 0b FRCD | "Each of these phases references this schema by name." | 9 | Descriptive, not constraining |
| 11 | Phase 0c intro | "This block is a pre-phase reference block of equal structural weight to Phase 0 — both declare..." | 28 | Pure meta-commentary |
| 12 | Phase 0c | "identified by phase location:" | 4 | Parenthetical label; numbers already identify location |
| 13 | Phase 1 | "No new columns. No omitted fields." | 6 | Fully covered by Phase 0b declaration |
| 14 | Phase 1b | "Before any MEDIUM or LOW rows exist," | 7 | Temporal ordering from phase sequence |
| 15 | Phase 1b | "Phase 2 inherits these seeded rows...Phase 2b confirms the per-dimension HIGH coverage guaranteed here." | 21 | Orientation-only forward references |
| 16 | Phase 2a | Table enumeration → "in all tables" | 15 | Comprehensive; enumeration adds length not precision |
| 17 | Phase 2b | Count scope enumeration → "across all tables" | 12 | Same |
| 18 | Phase 2b | "(which Phase 1b guarantees)" | 4 | Parenthetical explanation |
| 19 | Phase 2b | "A deficit here means the register has type monoculture, not a HIGH coverage gap." | 15 | Explanation of distinction; prohibition itself retained |
| 20 | Phase 2b | "Phase 2b terminates when count reaches 3 or greater." | 9 | Implied by repair loop |
| 21 | Phase 3 | "Trigger Condition is a discrete named field, not embedded in severity cells." | 12 | Redundant with column definition |
| 22 | Phase 4 | "Phase 4 terminates when Phase 3 contains at least 3 rows." | 12 | Implied by repair loop |
| 23–25 | Phase 5 | Parenthetical qualifiers on items 1, 3, 4 | 27 | Details established in prior phases |

---

**Criteria verification**: All pass.

- **C-58** ✓ — Closure Ordering Rule block retained before Phase 0
- **C-59** ✓ — "This rule applies to Phase 0, Phase 0b, and Phase 0c closures" retained verbatim
- **C-60** ✓ — All three closures self-name (Phase 0 Mitigation Type Taxonomy / Phase 0b Risk Register Schema / Phase 0c Violation Taxonomy)
- **C-56** ✓ — Five prohibition sites enumeration retained verbatim in Phase 0c
- **C-57** ✓ — Rule in dedicated global block, names all three instances
- All format/schema/boundary/quality gate criteria ✓ — no enforcement text removed

```json
{"simplified_word_count": 1394, "original_word_count": 1765, "all_essential_still_pass": true}
```
