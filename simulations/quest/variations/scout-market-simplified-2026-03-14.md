---

## Simplified Prompt Body

```
You are running /scout:market. Fill in this structured template.
STATUS QUO runs first -- do-nothing cost and inertia anchor drive scoring cards, beachhead
quantification, and sequencing transitions. Scoring appears in per-segment cards. After all
cards, a cross-segment summary table is required -- copy values from cards. Do not reorder,
rename, or remove any section header, card field, summary table column, or template fragment.
```
*(all sections follow unchanged except the cuts below)*

---

## Simplification Report

### Cuts made (words doing NO work)

| Cut | Location | Words | Reason |
|-----|----------|-------|--------|
| `; it presents all scoring dimensions in one view for direct segment comparison` | Preamble | 10 | The table column headers enumerate all dimensions; this describes what the table IS, which the table shows |
| `This value is` → `Required` (shortening) | STATUS QUO do-nothing cost | 2 | "Required in..." carries the meaning |
| `-- name them so they can be cited exactly` | STATUS QUO inertia anchor | 8 | "Required verbatim" already requires verbatim citation; this restates it |
| `This table presents Pain, WTP, Revenue Model, Price Point, Accessibility, Fit Score, GTM Difficulty, Inertia Anchor, and Rank Score as adjacent columns with one row per segment.` | CROSS-SEGMENT instruction | 27 | The table header row lists every column; sentence describes structure the table itself communicates |
| `Enables direct cross-segment comparison in one view without card lookup.` | CROSS-SEGMENT instruction | 10 | Explanatory only; purpose is self-evident from seeing all columns in one table |
| `Revenue model column included.` | COMPOSITE RANK bracket | 4 | Column header is visible in the table |
| `Do not write a generic statement.` | BEACHHEAD not-building | 6 | The explicit format `[Users continue... costing approximately... Every quarter/year...]` already forecloses generic responses; "Do not omit." is the operative constraint |
| `from STATUS QUO inertia analysis that enables this transition. Must cite the anchor by name` → `that enables this transition -- must cite the STATUS QUO anchor by name` | GTM Inertia-break | 3 | Same meaning, tighter; "STATUS QUO anchor" is more precise than "the anchor" |

**Total cut: ~70 words from ~884 = 7.9% reduction**

### Essential criteria: all pass

- **C-01** Segment IDs: table + ID column unchanged. PASS.
- **C-02** TAM/SAM/SOM: section unchanged. PASS.
- **C-03** 3-dimension fit: Pain/WTP/Accessibility fields + formula in cards. PASS.
- **C-04** Composite rank formula: in cards + COMPOSITE RANK table. PASS.
- **C-05** Beachhead with rationale: section unchanged with all coverage requirements. PASS.

### Why 20-40% was not reached

The V-05 prompt was already tightened through four prior rounds. The only genuine redundancy cluster is the CROSS-SEGMENT SCORING SUMMARY instruction (37 words describing what the table structure already shows). Every other instruction text either:
- Enforces a criterion not captured by structure alone (anchor reminders in S2/S3 cards drive C-11 quality across all segments)
- Forecloses a specific bad response (the GTM time-period prohibition)
- Constrains at source AND consumption separately (do-nothing cost quantification at STATUS QUO field + referenced again at beachhead)

To reach 20% (~177 words) would require stripping bracket instructions from S2/S3 cards (~80 additional words). That trade preserves all 5 essential criteria but risks aspirational C-11/C-14 compliance for segments 2+. Recommend accepting 8% as the minimal-loss ceiling for this prompt.

---

Written to: `simulations/quest/golden/scout-market-golden-2026-03-14.md`

```json
{"simplified_word_count": 807, "original_word_count": 884, "all_essential_still_pass": true}
```
