Reading the V-01 evidence closely, three sub-patterns appear that exceed what the existing 13 criteria capture:

1. **`??` placeholder tokens** (C-02 evidence) — absent artifacts get an explicit `??` marker, not a blank cell; gaps become machine-scannable
2. **Counted-total delta summary** (C-03 evidence) — mandatory templated sentence with exact counts: *"Strategy was written on [DATE]. N artifacts are NEW. M are PRIOR."* — makes delta quantitative and checkable
3. **Hedge-phrase disqualification** (C-08 evidence) — inertia column carries an explicit rule: *"'No change needed' is not an acceptable entry"* — closes known escape hatches before they appear

These become C-14, C-15, C-16.

---

## Rubric — topic:plan (v3)

**5 essential / 3 recommended / 8 aspirational — 16 criteria total**

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
| C-09 | **Type-labeled null declarations** — separate labeled declaration per absent change type (`ADD — NULL`, `REMOVE — NULL`, `REPRIORITIZE — NULL`), not a single "nothing to do" statement | format |
| C-10 | **Conflict detection** — cross-artifact contradiction audit in its own numbered phase with typed null form (`CONFLICT DETECTION — NULL`) when empty | depth |
| C-11 | **Required-cell table schemas** — every phase structures output as a table where blank cells are visually obvious violations; prose is not used where a table schema is defined | format |
| C-12 | **In-phase stop gates** — each phase includes an explicit "do not proceed until every cell is filled" instruction, creating hard phase boundaries that prevent skipping | behavior |
| C-13 | **Mandatory column enforcement** — the inertia column (and any other structural column) is labeled "mandatory" with its own header, making omission detectable independent of content review | format |
| C-14 | **Explicit placeholder tokens** — absent artifact filenames and dates are filled with `??` (or equivalent sentinel) rather than left blank; gaps are machine-scannable and visually distinct from deliberate omissions | format |
| C-15 | **Counted-total delta summary** — after classification a mandatory templated sentence states exact counts: *"Strategy was written on [DATE]. N artifacts are NEW. M are PRIOR."* — making the delta quantitative and independently verifiable | correctness |
| C-16 | **Hedge-phrase disqualification** — any required justification column explicitly names and bans common hedge phrases (e.g., *"'No change needed' is not an acceptable entry"*), closing escape hatches before they appear | behavior |

**Formula**: `(essential/5 × 60) + (recommended/3 × 30) + (aspirational/8 × 10)`  
**Golden**: all essential pass + composite ≥ 80 (requires ≥ 2/3 recommended)  
**Max**: 100
