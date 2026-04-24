Three new patterns from the scorecard evidence, each appearing in at least one PASS cell with no matching criterion in C-01–C-20:

1. **Named-violation enumeration in vocabulary contract** (V-01, C-17 PASS) — "three named violations" alongside token definitions; the contract doesn't just define tokens, it pre-enumerates specific misuse conditions

2. **Row-number cross-reference in defense citation** (V-02, C-08/C-18 PASS) — proposals must cite the Phase 0 row number they defeated, making linkage independently verifiable without re-reading prose

3. **Verbatim-quoted banned forms** (V-02 C-16 + V-03 C-16 PASS) — banned phrases appear in quoted form exactly as they'd appear in output ("no change needed", "compelling reason"), making violations pattern-matchable

---

## Rubric — topic:plan (v5)

**5 essential / 3 recommended / 15 aspirational — 23 criteria total**

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
| C-17 | **Two-tier sentinel vocabulary** — two distinct tokens are defined and used: `??` for an open obligation (unknown or not yet filled) vs `--` for a closed decision (deliberately absent/not applicable); gap *type* is machine-distinguishable, not only gap *presence* | format |
| C-18 | **Pre-signal defense register** — before reading any artifact, a defense register table is committed listing each potential change dimension alongside the current strategy's active defense argument; each subsequent proposal must name the specific defense it defeated, making inertia linkage evidence-based rather than post-hoc | depth |
| C-19 | **Integer-enforcement gate language** — beyond requiring the templated delta sentence (C-15), an explicit gate-failure rule names the banned non-integer forms: *"writing 'a few', 'several', 'some', or any non-integer value is a gate failure"*; fuzziness is a named failure condition, not a quality concern | correctness |
| C-20 | **Sequential phase-linked stop gates** — stop gate instructions reference the next phase number explicitly (*"Do not advance to Phase N without passing this gate"*), creating a linked sequential chain where no phase can be skipped without encountering a named, numbered gate | behavior |
| C-21 | **Vocabulary contract violation enumeration** — the vocabulary contract block not only defines tokens (`??`, `--`) but enumerates specific named violation conditions (e.g., *"leaving a cell blank when `--` would be correct is a violation"*); misuse modes are as explicitly defined as the tokens themselves, making the contract self-enforcing | format |
| C-22 | **Row-number anchor citation in defense linkage** — each proposal row cites the specific row number or ID of the defense register entry it defeated (e.g., *"Defense defeated: Row 3"*), making inertia linkage independently verifiable as a cross-reference without re-reading prose; a named defense without a row number does not satisfy this criterion | depth |
| C-23 | **Verbatim-quoted banned forms** — banned phrases in any disqualification rule are listed in quoted form exactly as they would appear in model output (e.g., `"no change needed"`, `"clearly warranted"`, `"several artifacts"`), making violations pattern-matchable without interpretive judgment; described paraphrases do not satisfy this criterion | behavior |

**Formula**: `(essential/5 × 60) + (recommended/3 × 30) + (aspirational/15 × 10)`
**Golden**: all essential pass + composite ≥ 80 (requires ≥ 2/3 recommended)
**Max**: 100
