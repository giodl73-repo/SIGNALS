Written to `simulations/quest/rubrics/topic-plan-rubric-v9-R9-2026-03-15.md`.

---

## Round 9 — topic-plan — 5 Variations

**What R8 left open:**

| Criterion | R8 V-05 mechanism | Gap |
|-----------|-------------------|-----|
| C-32 | `★ Reversibility` in upfront schema; three values in prose block *below* the Step 6 table | Enum defined below-table, not in-column-header; prose fill not structurally blocked |
| C-33 | 5-col assumption table in upfront schema | Missing "Implicit evidence" column — cites the strategy.md *phrase* that implies each assumption; R8's five columns are ID + assumption + back-fill + delta-relevance + candidate |

**Design notes on C-33:** The five columns C-33 requires are: *extracted assumption, implicit evidence (the strategy text that reveals the assumption existed), back-fill, delta-relevance, delta-candidate.* R8 V-05 has `Assumption ID` (a row key, not a content column) + four content columns, with no "implicit evidence" column. The archaeology citation is the new content.

---

### Variation table

| ID | Axis | Type | C-32 | C-33 |
|----|------|------|------|------|
| **V-01** | Output format — closed-enum in column header | Single | PASS | FAIL |
| **V-02** | Lifecycle emphasis — Implicit evidence column at extraction | Single | FAIL | PASS |
| **V-03** | Phrasing register — decision-question [A/B/C] reversibility | Single | PASS | FAIL |
| **V-04** | Output format + Lifecycle — enum lock + implicit evidence + schema-first | Combination | PASS | PASS |
| **V-05** | Full stack — R8 V-05 + enum lock + implicit evidence + archaeology obligation | Combination | PASS | PASS |

---

### Key structural distinctions

**C-32 mechanisms — V-01 vs V-03 (both pass, different register):**
- V-01 puts the three-value enum *inside the column header* as `[(1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible — select one; prose is not a valid value]`. The model fills the cell next to its own constraint.
- V-03 replaces the taxonomy label with a decision question: "Can we defer this safely? Select [A] Yes, same cost / [B] Yes, but harder / [C] No, window closes permanently." Same forced choice, different activation frame.
- If V-03 proposals show richer temporal reasoning, decision-question framing is not equivalent to label selection — the phrasing register difference is real and worth extracting.

**C-33 isolation — V-02:**
V-02 is the only variation with the implicit evidence column but no enum constraint. If V-02 assumptions are more auditable (each tied to a strategy phrase) but proposals are no better than R8 V-05, C-33 is a *provenance* criterion (traceability), not a *quality* criterion (proposal reasoning). That's a meaningful finding about which new criterion does more work.

**V-04 vs V-05 (both C-32+C-33 pass):**
V-04 uses R8 V-04 base (no cascade checkpoints). V-05 uses R8 V-05 base (Step 6 commitment checkpoint names all three reversibility values). If both produce indistinguishable proposals, the at-step commitment adds no reinforcement beyond the pre-reading schema — the schema-first contract is sufficient. If V-05 proposals are more temporally precise, the double-declaration (upfront + Step 6) matters under execution pressure.
