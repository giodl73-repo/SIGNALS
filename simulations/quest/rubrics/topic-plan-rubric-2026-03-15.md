---

## Rubric — topic:plan (v1)

**5 essential / 3 recommended / 2 aspirational — 10 criteria total**

### Essential (must all pass)

| ID | Criterion | Category |
|----|-----------|----------|
| C-01 | **Read strategy.md** — output cites at least one concrete reference to existing strategy structure | correctness |
| C-02 | **Signal inventory** — all 9 namespaces explicitly assessed with artifact filenames + dates | coverage |
| C-03 | **Delta detection** — NEW vs PRIOR split, only NEW drives proposals, strategy date named | correctness |
| C-04 | **Typed change proposals** — ADD / REMOVE / REPRIORITIZE; silence is not a null declaration | behavior |
| C-05 | **Confirmation gate** — stops before modifying strategy.md, presents visible YES/NO/REVISED gate | behavior |

### Recommended (need 2/3 for golden)

| ID | Criterion | Category |
|----|-----------|----------|
| C-06 | **Evidence citation** — artifact filename in every non-null proposal row | depth |
| C-07 | **Before/after diff** — Before/After structure present for each proposal | format |
| C-08 | **Inertia justification** — per-row reason why NO CHANGE is insufficient | depth |

### Aspirational

| ID | Criterion | Category |
|----|-----------|----------|
| C-09 | **Type-labeled null declarations** — separate labeled declaration per absent change type | format |
| C-10 | **Conflict detection** — cross-artifact contradiction audit, typed null when empty | depth |

**Formula**: `(essential/5 × 60) + (recommended/3 × 30) + (aspirational/2 × 10)`  
**Golden**: all essential pass + composite ≥ 80 (requires ≥ 2/3 recommended)  
**Max**: 100

Written to `simulations/quest/rubrics/topic-plan-rubric-v1-2026-03-15-new.md`.
