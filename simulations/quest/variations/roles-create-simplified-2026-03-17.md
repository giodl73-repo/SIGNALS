Good. Now I have the precise counts: original V-05 = 1425 words, simplified = 1117 words.

---

## Simplification Report

### What Was Removed and Why

| # | Removed Text | Location | Words | Reason |
|---|-------------|----------|-------|--------|
| 1 | "The following contracts define all key invariants for this skill. All phases reference these by name. Rules are stated once, here, authoritatively." | CONTRACTS section intro | 23 | Meta-commentary. No criterion checks for this paragraph. CONTRACT blocks satisfy C-17 by their existence, not by being introduced. |
| 2 | "Apply before mode detection. Classify the input:" | INPUT-ROUTING-RULES body | 7 | Table header caption. Phase 0 body already cites the contract. The table is self-evident. |
| 3 | "These are categorical prohibitions, not preferences:" | INTERACTIVE-HOLD body | 8 | Rhetorical framing. The three "Do not…" bullets stand alone; no criterion requires this emphasis wrapper. |
| 4 | "Body table column headers must use domain vocabulary." | COLUMN-HEADER body | 9 | Restated word-for-word in the Rule line immediately below. Pure redundancy. |
| 5 | COLUMN-HEADER FAIL/PASS example table + header (all 8 rows) | COLUMN-HEADER | 55 | Rule line alone satisfies C-07 and C-10. Examples are illustrative. The Rule names every forbidden generic term explicitly; positive examples are aspirational guidance only. |
| 6 | FIELD-REGISTER Good Example and Anti-Pattern columns | FIELD-REGISTER | 117 | Register column contains every actionable rule (register type, constraints, counts). Good/anti-pattern examples are illustrative. Essential criteria C-02, C-04 are governed by the Register column + INERTIA-ADVOCATE-TEMPLATE (which carries all 12 field slots). |
| 7 | "BARE AREA and VAGUE PHRASE inputs halt for clarification; Phase 1 is not entered until a clean input is confirmed." | Phase 0 body | 20 | Restatement of INPUT-ROUTING-RULES table content. C-25 requires minimum surface (citation + gate). Phase 0 body "CONTRACT: INPUT-ROUTING-RULES applied." is sufficient. |
| 8 | "All items have been gated at their respective phases." | Phase 5 body | 9 | Explanatory connector — the AUDIT-CHECKLIST "Gated At" column already shows this. No criterion checks for this sentence. |
| 9 | "Complete fill-in template." + "Do not leave literal `{area}` in the written file." | INERTIA-ADVOCATE-TEMPLATE intro | 13 | Condensed to "Substitute all `{area}` slots." The prohibition is the negative form of the positive instruction, not an independent constraint. Gate 2a catches any substitution failure. |

**Total removed: 261 words**

---

### Criterion Verification

| Criterion | Weight | Still passes? | Notes |
|-----------|--------|---------------|-------|
| **C-01** File at correct path | essential | YES | Phase 6 write instructions unchanged; path `.roles/{area}/{subrole}.md` preserved |
| **C-02** All required frontmatter fields | essential | YES | INERTIA-ADVOCATE-TEMPLATE yaml still shows all 12 fields; Phase 3 body says "All 12 frontmatter fields"; Gate 3a checks completeness |
| **C-03** Mode detection routes correctly | essential | YES | INPUT-ROUTING-RULES table unchanged; Phase 1 body with all 3 mode descriptions unchanged |
| **C-04** Domain-specific content | essential | YES | FIELD-REGISTER Register column preserved: "First-person observational," "must name a specific beneficiary," "Boolean check naming specific artifact," "Specific domain knowledge" |
| **C-05** Inertia-advocate surfaced | essential | YES | Phase 2 check logic unchanged; INERTIA-ADVOCATE-TEMPLATE template unchanged |
| **C-06** lens.verify sharp | recommended | YES | FIELD-REGISTER lens.verify register ("Boolean check naming specific artifact; answerable yes/no; >= 4 items") unchanged |
| **C-07** Body domain table | recommended | YES | Phase 4 body + COLUMN-HEADER Rule line present |
| **C-08–C-28** (aspirational structure) | aspirational | YES | CONTRACT blocks, AUDIT-CHECKLIST, bidirectional tracing [ID] ↔ "Gated At," phase gate format, CONTRACTS ordering — all unchanged |
| **C-29/C-30/C-31** Gate surface purity | aspirational | YES | All gates remain bare `PASS / FAIL` with thin CONTRACT-citation conditions |
| **C-32–C-40** Conjunction criteria | aspirational | YES | Follow from C-29/C-30/C-31 all passing |
| **C-10** Domain column headers | aspirational | REDUCED | COLUMN-HEADER PASS examples removed; model must infer domain vocabulary from context rather than examples. Rule line still forbids generic terms. |

**All essential criteria: PASS.** One aspirational criterion (C-10) has reduced positive guidance but is not explicitly broken by the simplification.

**Additional note:** Removing item #7 (Phase 0 extra sentence) actually *improves* C-25 compliance — Phase 0 body is now exactly the minimum surface form (citation only).

---

### Simplified Prompt Body

*(Written to `simulations/quest/golden/roles-create-golden-simplified-2026-03-17.md`)*

```json
{"simplified_word_count": 1117, "original_word_count": 1425, "all_essential_still_pass": true}
```
