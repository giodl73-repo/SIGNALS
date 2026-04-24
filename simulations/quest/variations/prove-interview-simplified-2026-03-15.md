The simplified body is **1425 words** vs **1641 original** — a 13.2% reduction.

---

## Simplification report

### What was removed and why

| # | Location | Removed | Words |
|---|----------|---------|-------|
| 1 | Phase 0A EXIT GATE item 1 rationale | "without reading through table-completeness conditions" and surrounding padding | ~13 |
| 2 | Phase 0A EXIT GATE contract warning | "and does not close the mid-chain drift gap" — explanatory framing, not a gate check | ~8 |
| 3 | Phase 0B-I body | "-- what pattern of evidence types across subjects places the finding at this level. A level name without a constitutive definition does not satisfy this gate." — first clause rephrases the instruction; second clause duplicates the gate | ~28 |
| 4 | Phase 0B-II body | "-- the specific evidence property that tips the verdict from one level to the other" — describes what a deciding factor is; gate checks its presence | ~16 |
| 5 | Phase 0C EXIT GATE item 1 rationale | "immediately auditable at gate entry without reading through affirmative completion conditions" → "auditable at gate entry" | ~16 |
| 6 | Phase 0C EXIT GATE Phase 1 propagation | "(exact-match required -- a paraphrase does not satisfy the Phase 1 obligation)" → "(exact-match required)" | ~10 |
| 7 | Phase 0C EXIT GATE Phase 2 propagation | "(direct-question required -- referencing the topic without naming the anchor does not satisfy)" → "(direct-question required)" | ~12 |
| 8 | Phase 0C EXIT GATE tail | "These obligations are declared at the source so any chain break is auditable at the phase that names its predecessor rather than requiring inspection of the downstream phase alone." — meta-rationale for the design; the gate obligations themselves are sufficient | ~33 |
| 9 | Phase 1 body Inertia anchor | "(exact-match required per Phase 0C exit gate propagation obligation)" — enforced at gate item 1 | ~10 |
| 10 | Phase 1 body Blind spots | "(non-blank, non-generic)" — enforced at gate item 4 | ~4 |
| 11 | Phase 1 EXIT GATE item 1 rationale | "without reading through card-completeness conditions" padding | ~15 |
| 12 | Phase 2 body INCUMBENT line | "(direct-question required per Phase 0C exit gate propagation obligation)" — enforced at gate item 1 | ~10 |
| 13 | Phase 2 body closing | "All four transcripts must be complete before any hypothesis question section begins." — duplicates Phase 2 opening line | ~14 |
| 14 | Phase 2 EXIT GATE item 1 rationale | "without reading through affirmative completion conditions" padding | ~15 |
| 15 | Phase 3 body PROFILE RELEVANCE | "(STICKINESS \| LIMITATION \| DISPLACEMENT \| EXTERNAL)" — already declared in Phase 0A gate | ~6 |
| 16 | Phase 3 EXIT GATE item 1 rationale | compressed to "-- first gate item: gate-block-first placement makes vocabulary drift auditable at gate entry" | ~18 |
| 17 | Phase 3 EXIT GATE item 4 | "(STICKINESS \| LIMITATION \| DISPLACEMENT \| EXTERNAL)" — already in item 1 | ~6 |

**Total removed: ~234 words**

### Criteria verification

| Criterion | What tests it | Still present? |
|-----------|---------------|----------------|
| **C-49** Gate-block-first ordering | First item in every gate block is chain-critical | YES — all 5 gate blocks preserved |
| **C-50** Propagation obligations at source | Phase 0C EXIT GATE declares Phase 1 + Phase 2 obligations | YES |
| **C-51** Contract source declaration | Phase 0A declares itself authoritative + parallel-contract warning | YES |
| **C-52** Ordering rationale at item | "-- first gate item: gate-block-first placement makes X auditable at gate entry" at all 5 gates | YES — compressed but WHY explanation preserved |
| **C-53** Phase-differentiated propagation | Phase 1: "(exact-match required)" vs Phase 2: "(direct-question required)" — distinct constraints | YES |
| **C-54** Bidirectional contract closure | Phase 3 EXIT GATE item 1 cites "Phase 0A exit gate contract source" + item 4 adds anti-parallel-contract gate item | YES |

**All essential criteria pass: YES**

### Why 20-40% wasn't reached

The V-05 winning prompt was already minimally padded — most of its length is load-bearing criterion text (gate items for C-49–C-54 require specific phrase patterns that cannot be compressed without losing criteria). The gate rationale text (C-52) alone accounts for ~170 words that must be structurally present at each gate entry point.

```json
{"simplified_word_count": 1425, "original_word_count": 1641, "all_essential_still_pass": true}
```
