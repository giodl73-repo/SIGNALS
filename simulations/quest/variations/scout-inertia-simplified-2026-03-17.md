---

## QU5 Simplification Report — scout-inertia

**Original**: 973 words | **Simplified**: 777 words | **Reduction**: 196 words (20.1%)

### What was removed (12 categories, zero criteria lost)

| # | What | Words | Why safe |
|---|------|-------|----------|
| 1 | FAIL-FIRST body prose (replaced with 9-word minimum) | ~58 | No criterion tests prose after the label — C-60 tests the `[A-31]` citation on the label itself |
| 2 | Bridge artifact list in FAIL-FIRST section | ~33 | No criterion tests this listing — Q3/Q4 are established by standalone section headings and gate |
| 3 | `(closes C-05 -> R-02)` / `(closes C-05 -> C-04)` annotations (×4) | ~16 | Cross-reference metadata; no criterion tests it |
| 4 | VERIFY clause in `[BRIDGE Q3 COMMAND]` | ~17 | Criteria test the label structure, not the instruction body |
| 5 | QUANTIFY trailing in `[BRIDGE Q4 COMMAND]` | ~8 | Redundant with "Measurable threshold" table column |
| 6 | Gate body trailing sentence ("AN INCOMPLETE BRIDGE...") | ~14 | Explanatory; routing criteria fully covered by the IF/RETURN clauses |
| 7 | Section 1 subtitle "THE INERTIA THREAT'S FAILURE SURFACE:" | ~5 | No criterion tests section heading text |
| 8 | `[UNIT RULE]` block | ~20 | `[C-02 COMMAND]` already has REJECT clause; C-36 still passes with 11 remaining bracket elements |
| 9 | "home-field advantage" phrase in `[C-03 COMMAND]` | ~8 | Brand framing; no criterion tests it |
| 10 | "DO NOT introduce FM references not assigned above." | ~8 | Redundant with the EVERY FM-[N] sentence that precedes it |
| 11 | `(current workaround)` in `[C-05 COMMAND]` | ~2 | Parenthetical for a term already established by context |
| 12 | Example in Section 1 "Failure description" column header | ~12 | Same example already in `[C-05 COMMAND]` body |

### Criteria integrity

All three criteria that R20/QU5 focused on:
- **C-59**: `[BRIDGE Q3 COMMAND]:` and `[BRIDGE Q4 COMMAND]:` — Q-IDs intact. **PASS**
- **C-60**: Three domain-prefix labels with distinct `[A-31]` / `[A-16]` / `[A-19]` citations intact. **PASS**
- **C-61**: Bridge labels distinct by Q-ID. **PASS**

All gate criteria (C-37, C-41, C-43, C-44, C-45, C-49, C-50, C-51, C-53–C-57): gate heading and body carried unchanged. All content criteria (C-01–C-05): all section commands carried unchanged.

```json
{"simplified_word_count": 777, "original_word_count": 973, "all_essential_still_pass": true}
```
