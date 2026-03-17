---

# flow-integration R8 Variations — V-01 through V-05

Saved to `simulations/quest/rubrics/flow-integration-rubric-v8-variations-R8-2026-03-14.md`

---

## Variation Summary

| ID | Axis | C-24 | C-25 | Probes | Prediction |
|----|------|------|------|--------|------------|
| **V-01** | Role sequence | 4-row obligation table | Inventory table column headers = obligation row terms; VOCABULARY RULE reinforces | — | 177/177 |
| **V-02** | Full-table format | 4-row obligation table | Schema-only — VOCABULARY RULE **dropped**; column headers are obligation row terms by instruction alone | — | 177/177 |
| **V-03** | Mixed-format probe (table obligation + pipe inventory) | 4-row obligation table | **NO column headers** in pipe-delimited inventory — C-22 via VOCABULARY RULE, but no schema comparison possible | **Q2**: does C-25 require actual column header cells? | 172/177 (C-25 FAIL predicted) |
| **V-04** | Phase architecture + corrected terminal coda | 4-row obligation table in Phase 1 | Inventory table column headers = obligation row terms | **Q1**: terminal-position constraint definitive verdict | 177/177 |
| **V-05** | Non-standard terms + C-24/C-25 + canonical prohibition | 4-row obligation table (shadow-call, taken-for-granted, fog-system, relay-chain) | Inventory column headers = non-standard row terms; canonical substitution explicitly prohibited | — | 177/177 |

---

## Key design decisions

**V-01 vs R7 V-01**: Two surgical additions — prose obligation list → 4-row table (C-24), pipe-delimited inventory → Markdown table with column headers defined as obligation row term cells (C-25). VOCABULARY RULE retained but now points to table schema as the canonical evidence surface. All prior structural guarantees intact.

**V-02** drops the VOCABULARY RULE entirely. The schema alignment between obligation table row terms and inventory column headers is the only enforcement mechanism. This tests whether the schema-only path scores the same as the schema+declarative path.

**V-03** is the Q2 probe. The obligation table is present (C-24 satisfied), but the inventory is pipe-delimited — inline flag tokens, no column header cells. C-22 is satisfied by VOCABULARY RULE (token identity declared). C-25 requires column header comparison, which is impossible without a Markdown table. Predicted score: 172/177.

**V-04** is the Q1 definitive probe. R7 V-04 placed the coda *between* Phase 2 and Phase 3 and failed C-23. R8 V-04 places the coda *after Phase 3* (terminal position) and adds explicit language: "appended after Phase 3 — the last numbered phase." Combined with C-24/C-25.

**V-05** extends R7 V-05's non-standard vocabulary into the C-24/C-25 mechanism. The 4-row obligation table uses non-standard Obligation Terms; the inventory column headers match those exact tokens. Canonical substitution is prohibited by explicit rule AND is structurally visible as a header/row-term mismatch. Strongest C-22 enforcement for non-canonical vocabulary.
