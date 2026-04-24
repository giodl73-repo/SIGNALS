Reading the scorecard, there is one explicitly flagged new pattern not yet captured:

> **Distinctive V-02 pattern**: TABLE SCHEMAS section before Phase 0 commits all table schemas (A, B, C, D) as an upfront contract — including the calibration column — before any phase executes. This is not yet captured as a rubric criterion.

That yields one new criterion: **C-35**.

---

## Rubric — topic:plan (v10)

**5 essential / 3 recommended / 27 aspirational — 35 criteria total**

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
| C-28 | **Write-surface blocks as first-class section headers** — each of the three write-surface enforcement blocks (WS-1, WS-2, WS-3) is titled and positioned as a standalone section header in the skill structure, not embedded as a bullet or sub-item within a phase description, schema definition, or inline list; a block whose label appears only inside a list or as part of surrounding instructions does not satisfy this criterion even if the check instruction is present and fires at the correct site | format |
| C-29 | **Write-surface register** — an upfront register table (positioned before Phase 0 and before any artifact read) explicitly lists all three write surfaces by identifier, type, and trigger condition, creating an independently verifiable contract against which each block's presence can be confirmed without reading phase content; a skill that satisfies C-27 through scattered inline instructions without a pre-phase register declaration does not satisfy this criterion | depth |
| C-30 | **Register-milestone linkage** — each write-surface enforcement block includes an explicit citation to its register entry (by row number or identifier, e.g., *"WS-2 MILESTONE — fulfills Register Row 2"*), closing the loop between the upfront contract (C-29) and the delivery site; a block that fires at the correct location but does not cite its register entry does not satisfy this criterion even when C-29 is present | depth |
| C-31 | **Named phase lifecycle template** — each phase is structured with three explicitly labeled slots: ENTRY (preconditions for this phase), JOB (work instructions), and EXIT (completion gate); the EXIT slot is the structural home for the in-phase stop gate required by C-12, making cell-fill enforcement a named architectural position rather than a trailing instruction appended to narrative; a phase that contains stop gate language without named ENTRY/JOB/EXIT slots does not satisfy this criterion even if C-12 passes | format |
| C-32 | **Artifact-to-register calibration column** — the signal inventory or artifact classification table includes a dedicated calibration column mapping each artifact row to the specific defense register row number(s) it implicates; the column makes C-22 compliance a structured table-fill operation rather than a discretionary inline citation; an artifact table that achieves C-22 through prose notes or embedded parentheticals without a dedicated named column does not satisfy this criterion | depth |
| C-33 | **Inverted artifact sequence with upfront calibration** — new artifacts are sorted before prior artifacts in the inventory phase, and the calibration column (C-32) is completed for all new-artifact rows before any proposal row is opened; the ordering creates a hard architectural dependency — register-row binding precedes proposal writing rather than occurring simultaneously or post-hoc; a skill that processes artifacts in any order where proposals can be opened before calibration is complete does not satisfy this criterion | behavior |
| C-34 | **Compound audit structure (spine + lifecycle)** — the skill uses both a pre-phase write-surface register (C-29) and named per-phase lifecycle slots (C-31), yielding two independent completeness audit paths: (1) scan section headers to verify write-surface coverage, (2) scan EXIT slots to verify per-phase cell-fill enforcement; neither path is redundant with the other; a skill with only one structural layer does not satisfy this criterion even if C-28, C-29, C-12, and C-31 each pass individually | format |
| C-35 | **Upfront table schema register** — all table schemas used across the skill are declared as named schemas (e.g., Schema A, Schema B, Schema C, Schema D) in a dedicated TABLE SCHEMAS section positioned before Phase 0 and before any artifact read; the section commits column structure, mandatory column labels, and sentinel token usage for every table the skill will produce, making schema definitions a pre-phase declared contract rather than emergent definitions embedded within individual phase instructions; a skill where table schemas — including mandatory columns such as the calibration column — are defined inline within phase descriptions does not satisfy this criterion even if every mandatory column is present and correctly labeled | depth |

**Formula**: `(essential/5 × 60) + (recommended/3 × 30) + (aspirational/27 × 10)`
**Golden**: all essential pass + composite ≥ 80 (requires ≥ 2/3 recommended)
**Max**: 100

---

**What C-28 adds over C-27:** C-27 tests that all three blocks exist and fire at correct sites. C-28 tests structural elevation — a block buried inside a bulleted phase list is harder to audit, easier to skip on skim, and can be silently omitted when the surrounding list is reordered. First-class section headers are independently navigable: a reviewer can verify write-surface coverage by scanning section titles without reading phase content.

**What C-29 adds over C-27:** C-27 is verified by reading each phase and confirming the block is present. C-29 tests contract-first discipline — the register commits to all three sites *before* any phase is written, making the architecture a declared obligation rather than an emergent property. A register makes completeness auditable at the document level: three register rows, three delivery milestones, no prose-reading required.

**What C-30 adds over C-28 + C-29:** Having a register (C-29) and having first-class blocks (C-28) does not prove the register and blocks are linked. C-30 tests the closed loop: each block must name which register row it fulfills, making it impossible for the register to list a site that has no corresponding block, or for a block to fire without an acknowledged obligation. The citation is the audit trail; its absence leaves the contract and the delivery as parallel structures that happen to agree, rather than a verified chain.

**What C-31 adds over C-12:** C-12 tests that a stop gate instruction is present somewhere in each phase. C-31 tests structural position — an EXIT slot is a named architectural home for the stop gate, making it impossible to silently omit on revision without removing a labeled slot. A phase with stop gate language in running text satisfies C-12 but the gate can drift, be merged into adjacent instructions, or be dropped when the phase is edited. A named EXIT slot is load-bearing structure: its absence is visually obvious from the section skeleton alone.

**What C-32 adds over C-22:** C-22 tests that each proposal row cites a defense register row number. A proposal can satisfy C-22 by adding a parenthetical anywhere in the row. C-32 tests structural commitment — a dedicated calibration column is completed before proposals are written, meaning row-number binding is an input to the proposal phase rather than an embellishment of it. A column forces completeness (every row must have a value) in a way that inline citation does not.

**What C-33 adds over C-32:** C-32 tests that the calibration column exists and is filled. C-33 tests the ordering constraint that makes C-32 structurally prior to proposal writing. Without the inverted sequence, calibration can be filled retroactively — after proposals are written, with row numbers retrofitted to match. The inverted sequence closes that escape: new artifacts are classified and calibrated before the first proposal row opens, making row-number binding causally upstream of proposal content.

**What C-35 adds over C-32 + C-29:** C-32 tests that the calibration column exists as a named column in the inventory table. C-29 tests that write-surface blocks are declared upfront as a register. C-35 tests that all table schemas — including the calibration column's parent table — are declared together in a dedicated section before any phase executes. A skill with C-32 can define the calibration column inline when the inventory table is first constructed in Phase 1 or Phase 2; the column is present but its schema was never pre-committed. C-35 enforces the same contract-first discipline for table structure that C-29 enforces for write-surface blocks: every table's column structure is declared before any phase that would use it, making completeness auditable without reading phase content. A TABLE SCHEMAS section is to column structure what the WRITE SURFACE REGISTER is to enforcement blocks — a single pre-phase declaration that makes per-phase omissions visually detectable from the document skeleton alone.
