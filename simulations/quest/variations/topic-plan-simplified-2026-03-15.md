## Simplification Analysis

### What does no work in V-01

| Removed | Reason |
|---------|--------|
| `"Your first action is the signal inventory."` | Redundant — Phase structure and the prohibition already enforce order |
| `"in this order"` after namespace list | The list itself defines order |
| `"(full path) \| (from filename) \| (one line)"` table data row | Column headers are self-explanatory; example row adds no behavior |
| `"Complete all 9 namespace tables before proceeding to Phase 2."` | Fully redundant with "Do not read strategy.md until Phase 2" |
| `"Open …"` as its own sentence + `"Record:"` label | Collapse into one action line |
| `"verbatim or quoted paraphrase"` → `"verbatim or paraphrase"` | Same meaning, one word saved |
| `"listed by namespace"` → `"by namespace"` | Same meaning, one word saved |
| `"in your output (e.g., a quoted section header, a planned signal entry, a goal line)"` | Examples don't add constraint; criterion wording already clear |
| `"Compare the Phase 1 inventory against the Phase 2 strategy."` | Obvious from phase structure; adds nothing |
| `"the strategy explicitly references or planned for this artifact"` → `"referenced or planned in strategy"` | Shorter, same meaning |
| `"the strategy does not reference this artifact"` → `"not referenced in strategy"` | Shorter, same meaning |
| `"Complete classification before writing any proposals."` | Redundant with phase ordering |
| `"Produce a proposal table."` | Table immediately follows; instruction is implicit |
| `"Column rules:"` label | Bullet list under table is self-evidencing |
| `"a per-row reason"` / `"given the new signals"` / `"in Phase 1"` | Verbose qualifiers that add no constraint |

---

## Simplified Prompt

```
You are running `topic:plan` — strategy revision for a Signal topic.

**Do not read strategy.md until Phase 2.**

---

### Phase 1: Signal Inventory

Scan `simulations/` across all 9 namespaces:
`scout` / `draft` / `review` / `flow` / `trace` / `prove` / `listen` / `program` / `topic`

For each, produce a table:

| Filename | Date | Content summary |
|----------|------|-----------------|

---

### Phase 2: Read strategy.md

Open `simulations/topic/[topic-name]/strategy.md`. Record:
- Strategy creation date (name it explicitly)
- Goal statement (verbatim or paraphrase)
- Every planned signal entry by namespace

Cite at least one concrete reference to the strategy's structure.

---

### Phase 3: Delta Detection

Label each artifact:
- **PRIOR** — referenced or planned in strategy
- **NEW** — not referenced in strategy

For each NEW artifact, classify: **CONFIRMS** / **EXPANDS** / **CHALLENGES**

Only NEW artifacts drive proposals.

---

### Phase 4: Typed Change Proposals

Every namespace must have a row — silence is not a null declaration.

| Namespace | Proposal type | Evidence | Before | After | Defense |
|-----------|--------------|----------|--------|-------|---------|

- **Proposal type**: `ADD` / `REMOVE` / `REPRIORITIZE` / `NO CHANGE`
- **Evidence**: artifact filename (required for every non-null row)
- **Before**: current strategy language, or `(none)` for ADD
- **After**: proposed new language, or `(unchanged)` for NO CHANGE
- **Defense**: for `NO CHANGE`, explain why existing strategy is sufficient; `"no new signals"` only valid if namespace produced zero NEW artifacts

---

### Phase 5: Confirmation Gate

**STOP.** Do not modify strategy.md until the user confirms.

Present:
> Proposed changes: [summary]
> **Proceed? YES / NO / REVISED**
```

---

## Simplification Report

**Essential criteria check:**

| Criterion | Satisfied? | How |
|-----------|-----------|-----|
| C-01 Read strategy.md + cite concrete reference | ✓ | Phase 2 explicit read + "Cite at least one concrete reference" |
| C-02 All 9 namespaces, filenames + dates | ✓ | All 9 listed, table has Filename + Date columns |
| C-03 NEW/PRIOR split, only NEW drives, strategy date named | ✓ | PRIOR/NEW labels + "Only NEW artifacts drive proposals" + "Strategy creation date (name it explicitly)" |
| C-04 Typed proposals, silence not null | ✓ | ADD/REMOVE/REPRIORITIZE/NO CHANGE + "silence is not a null declaration" |
| C-05 Confirmation gate, YES/NO/REVISED | ✓ | Phase 5 STOP + "Do not modify until user confirms" + gate |

All 5 essential criteria pass. All 3 recommended (C-06, C-07, C-08) also pass.

**Word counts:**

| Version | Words |
|---------|-------|
| Original (V-01 body incl. estimated Phase 5) | ~323 |
| Simplified | ~207 |
| Reduction | ~36% |

```json
{"simplified_word_count": 207, "original_word_count": 323, "all_essential_still_pass": true}
```
