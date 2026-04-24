Looking at the R6 scorecard, the excellence signal is structural: V-05 achieves all three point-of-production blocking checks simultaneously, creating a qualitatively different architecture where violations cannot be produced and then caught — they are blocked at each write surface. C-24/C-25/C-26 test each mechanism individually; the new criterion captures the meta-property that all three are present together, leaving no write surface unguarded.

---

## Rubric — topic:plan (v7)

**5 essential / 3 recommended / 19 aspirational — 27 criteria total**

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
| C-24 | **Cell-level banned-forms check instruction** — each column or phase that defines banned forms includes an explicit point-of-production instruction directing the model to check the cell against the banned forms list before writing (e.g., *"check this cell against the BANNED FORMS list before presenting; any match disqualifies the row"*); a defined banned forms list without a cell-level check instruction does not satisfy this criterion | behavior |
| C-25 | **Banned-forms scope propagation** — the banned forms constraint applies to every free-text justification cell including null declaration reason cells, not only proposal rows; null declarations that can use hedge phrases represent a scope exemption and do not satisfy this criterion | behavior |
| C-26 | **Gate-0 pre-signal stop gate** — the pre-signal phase (defense register or equivalent Phase 0) has its own numbered stop gate (Gate 0) in the sequential chain, explicitly blocking any artifact reads until the gate passes; a Phase 0 that lacks a named, numbered gate does not satisfy this criterion even if all later gates are correctly linked | behavior |
| C-27 | **Write-surface enforcement completeness** — all three point-of-production blocking mechanisms are present and fire at their respective write surfaces: (1) a read-barrier declaration before Phase 0 actions (Gate 0), (2) a labeled cell-level check block before proposal column fill (Schema E/F boundary), and (3) an inline banned-forms check instruction embedded inside each null declaration template; having any two of three does not satisfy this criterion; completeness requires C-24, C-25, and C-26 to all pass | behavior |

**Formula**: `(essential/5 × 60) + (recommended/3 × 30) + (aspirational/19 × 10)`
**Golden**: all essential pass + composite ≥ 80 (requires ≥ 2/3 recommended)
**Max**: 100

---

**What C-27 adds over C-24 + C-25 + C-26 individually:** Each of those three criteria tests one enforcement site in isolation. A variation can satisfy all three individually with the checks scattered across the skill — buried in phase fill lists, referenced in a preamble, implied by earlier rules — without them composing into a coherent write-surface architecture. C-27 tests the architectural property: every free-text production site has a blocking check that fires before output, with no site relying solely on downstream auditing. The V-05 pattern that triggers C-27 is the placement discipline — a labeled block at the schema boundary, an inline instruction inside the template, a PRE-COMMIT BLOCK before Phase 0 — that makes the three checks structurally unavoidable rather than present-but-skippable.
