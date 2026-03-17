Five complete variations written to `simulations/quest/variations/discover-competitors-alt-variations-R5-2026-03-17.md`.

**Target criteria:** C-18, C-19, C-20 (new in v5 rubric)

**Setup:** R4 established the three patterns; retroactive v5 scoring showed V-05 = 145 (C-18+C-20), V-01/V-03/V-04 = 140 (one new criterion each). R5 asks: which two-criterion combinations reach 145, and does the full stack hit 150?

| # | Axis | Target | Expected |
|---|------|--------|----------|
| V-01 | Symmetric 3-sub-question loop (lifecycle) | C-20 isolation | 145 |
| V-02 | All-table conversion of R4 V-05 (format) | C-19 + carry test | 147.5–150 |
| V-03 | All-table + phase FAILS/PASS (format + phrasing) | C-18 + C-19 | 145 |
| V-04 | All-table + symmetric loop (format + lifecycle) | C-19 + C-20 | 145 |
| V-05 | Full R5 stack (format + phrasing + lifecycle) | C-18 + C-19 + C-20 | **150** |

**The key open question is V-02:** SR-block FAILS/PASS pairs reference table rows rather than labeled slots — does that satisfy C-18, or does C-18 require FAILS/PASS at the actual phase instruction level for C-12 and C-13? If SR-block is sufficient, V-02 = 150. If phase-instruction is required, V-02 = 147.5. V-03 and V-04 isolate the two sides of that question.
led slots to
  3-row mechanism table; Phase 4 dual-line template to 2-row whitespace table. Risk: converting
  slots to tables removes per-slot FAILS/PASS pairs from Phase 2 phase instructions -- C-18 may
  partially fail. SR block FAILS/PASS for SR2 and SR4 updated to reference table rows.
  Key question: does SR-block FAILS/PASS for table rows satisfy C-18, or does C-18 require
  phase-instruction-level FAILS/PASS pairs specifically?

- V-03 base: R4 V-03 (all-table, C-19 PASS = 140). Change: add FAILS/PASS pairs to each table
  phase instruction. Tests C-18 + C-19 path without verification loop.

- V-04 base: R4 V-03 (all-table, C-19 PASS = 140). Change: add symmetric verification loop
  without adding FAILS/PASS to phase instructions. Tests C-19 + C-20 path independently.

- V-05: Combines V-03 (all-table + FAILS/PASS per table) + V-01 (symmetric loop). Ceiling.

---

## V-01 -- Symmetric Verification Loop (C-20)

**Axis:** Lifecycle emphasis -- pre-submission verification loop mirrors opening SR block
**Hypothesis:** R4 V-05's verification loop satisfied C-20 as a side effect, but its sub-questions
are asymmetric: SR2 asks "portability test applied?" while SR1 and SR4 ask "format-failure
declared?" C-20 requires identical sub-questions per constraint. V-01 makes the loop truly
symmetric: the same three sub-questions (format artifact present? format-failure declared?
FAILS/PASS pair present?) are asked for each of SR1, SR2, and SR4. Base: R4 V-04 (C-18 PASS,
C-19 FAIL, C-20 FAIL = 140). The only change is the pre-submission verification block.
Expected: C-18 PASS, C-19 FAIL, C-20 PASS = 145.

```
SETUP: Auto-detect product domain from README, CLAUDE.md, package.json, Glob. Do not prompt.

STRUCTURAL REQUIREMENTS -- hard format constraints. All constraints enforce via the same
apparatus: named format artifact + format-failure declaration + FAILS/PASS rejection example
pair. Any one absent or failing is an observable format failure. Confirm all five before
submitting output:

  [ ] 1. PHASE 1 pre-map table present and fully populated before any competitor entry.
         Required when focus is provided.
         FAILS: Prose paragraph listing segments; absent table; table with empty cells.
         PASS: Markdown table with named schema, all cells populated, present before Phase 2.

  [ ] 2. PHASE 2 inertia: all three slots (WORKAROUND SATISFACTION, SWITCHING COST, HABIT
         LOCK-IN) populated with domain-exclusive content.
         FAILS: Content that reads correctly for payroll software, a photo editor, or a
           scheduling tool -- regardless of whether mechanism names are present.
         PASS: Every slot names a specific tool, step, artifact, or ritual recognizably wrong
           for any other product category.

  [ ] 3. PHASE 3 competitor table: Map Position column populated for every row including
         inertia. Verbatim Phase 1 row labels only.
         FAILS: Empty Map Position cell; paraphrased or generalized Phase 1 row label.
         PASS: Exact Phase 1 row label in every cell; no paraphrasing.

  [ ] 4. PHASE 4 whitespace: both Competitive gap line and Focus gap line present in one
         paragraph. Required when focus is provided.
         FAILS: Single-axis whitespace; two separate paragraphs; missing either label;
           combined statement not grounded in Phase 1 row labels.
         PASS: One paragraph with "Competitive gap:" and "Focus gap:" both labeled, both
           grounded in Phase 1 data and Map Position column values.

  [ ] 5. ENFORCEMENT SYMMETRY: SR1 (C-11), SR2 (C-13), and SR4 (C-12) each carry the same
         three-component enforcement fingerprint -- named format artifact + format-failure
         declaration + FAILS/PASS rejection example pair. No constraint enforces via prose
         instruction alone.
         FAILS: Any of the three lacks a named format artifact, a format-failure declaration,
           or a FAILS/PASS rejection example pair.
         PASS: All three constraints carry all three components in identical structure.

Structural Requirements 1, 3, 4, and 5 apply only when focus is provided.

PORTABILITY TEST (apply to every PHASE 2 slot before accepting it):
"If I copied this slot content unchanged into a competitor analysis for a clearly different
product -- payroll software, a photo editor, a scheduling tool -- would it still make sense?"
If yes, rewrite until recognizably wrong for any other product category.

PHASE 1 -- FOCUS LENS PRE-MAP (Structural Requirement 1):

If focus = market:
| Segment | Size Estimate | Growth Stage | Current Leader |
|---------|--------------|--------------|----------------|
3-5 rows. Fill all columns. Growth stage: emerging / growth / mature.
Current leader: named competitor or default behavior most dominant in this segment.
This is the competitive frame. Every competitor including inertia maps to exactly one row.

If focus = positioning:
| Positioning Category | Current Owner(s) | Vacancy Status |
|---------------------|-----------------|----------------|
3-5 rows. Fill all columns. Vacancy: open / contested / owned.
This is the competitive frame. Every competitor including inertia maps to exactly one row.

If no focus: skip Phase 1. SR1, SR3, SR4, and SR5 are not applicable.

PHASE 2 -- INERTIA FIRST (Structural Requirement 2; all three slots mandatory):

Competitor 0: "None / status quo." Threat level: HIGH. State explicitly.
If Phase 1 was completed: record Phase 1 row in the Phase 3 table below.

WORKAROUND SATISFACTION:
Name the exact substitution -- the specific tool, template, script, or duct-taped combination
of tools -- that teams use instead of adopting a dedicated solution in this domain. Explain
why it satisfies enough need that teams feel no pain and do not seek alternatives.
FAILS: "Teams use workarounds" / naming a generic category without the specific tool, template
  name, or combination unique to this product domain.
PASS: Names the exact template, combination, or step recognizably specific to this product's
  competitive context. Fails portability for any other product category.

SWITCHING COST:
Name the concrete thing a team must lose or redo when they adopt something new in this
product context. Name the specific format, role, process, or contract at stake. Quantify if
possible (hours, days, FTE cycles, budget range).
FAILS: "Switching has a cost" / "migration effort required" without specifying what migrates
  from what to what in this domain.
PASS: Names the domain-specific format or workflow at stake -- detail inapplicable in any
  other product category.

HABIT LOCK-IN:
Name the specific repeated behavior -- the artifact, ritual, sprint cadence, or shared
convention -- that makes the workaround feel normal in this product context.
FAILS: "Teams develop habits around their tools" without naming the specific behavior as it
  exists in this product's workflow.
PASS: Names the habit -- artifact, ritual, or routine -- recognizably wrong for any other
  domain.

Portability test applied to each slot. Use WebSearch if needed. Cite inline.

PHASE 3 -- COMPETITOR TABLE (Structural Requirement 3; Map Position column required):

| # | Competitor | Threat | Overlap | Map Position |
|---|------------|--------|---------|--------------|
| 0 | None / status quo | HIGH | -- | [exact Phase 1 row label] |
| 1 | [name] | H/M/L | H/M/L | [exact Phase 1 row label] |
| 2 | [name] | H/M/L | H/M/L | [exact Phase 1 row label] |
...

Map Position: exact Phase 1 row label this competitor primarily occupies or contests.
Use Phase 1 row labels verbatim -- do not paraphrase or generalize. An empty cell or
paraphrased label is a format failure. When no focus is provided, omit Map Position column.
Add one sentence per competitor on threat relative to inertia and Map Position context.
Verify at least one major competitor claim via WebSearch. Cite inline.

PHASE 4 -- FINDINGS (Structural Requirement 4; dual-line template required when focus provided):

1. DUAL-AXIS WHITESPACE (both lines required; both labels mandatory):
   Competitive gap: No named competitor owns [X] because [reason]. Name which competitors
     come closest and which Map Position cells they occupy.
   Focus gap: Phase 1 row [Y -- use exact Phase 1 row label] is unaddressed / unoccupied
     because [reason]. Reference Phase 1 table data.
   Combined: [the position simultaneously [X] and [Y] -- where a new entrant faces neither
     a dominant named competitor nor inertia's strongest foothold. Ground in Map Position
     column values].
   FAILS: Single-axis finding; two paragraphs; missing "Competitive gap:" or "Focus gap:"
     label; combined not grounded in Phase 1 row labels or Map Position values.
   PASS: One paragraph with both labels present, both grounded, combined statement explicit.

2. TABLE STAKES -- minimum requirements to be taken seriously over the WORKAROUND SATISFACTION
   substitute named in Phase 2. Reference at least one Phase 1 data point per item.

3. COMPETITIVE MATRIX -- top 3 by threat level, one recommendation sentence each, sorted
   high to low.

PRE-SUBMISSION VERIFICATION -- symmetric enforcement check, same three sub-questions per
constraint. Answer each before submitting. Any NO requires revision.

  SR1 (C-11): format artifact present (pre-map table)?
              format-failure declared ("absent table / empty cells fail")?
              FAILS/PASS pair present?

  SR2 (C-13): format artifact present (three labeled slots)?
              format-failure declared ("generic restatements fail")?
              FAILS/PASS pair present (per slot)?

  SR4 (C-12): format artifact present (dual-line template)?
              format-failure declared ("single-axis / missing label fails")?
              FAILS/PASS pair present?

Also confirm SR3: Map Position column has no empty or paraphrased cells.

AMEND: Exactly 3 items. Input change + output change. Specific.

Write artifact: simulations/discover/competitors/{topic}-competitors-alt-{date}.md
Frontmatter: skill, topic, date, skill_version, input, focus.
```

---

## V-02 -- All-Table Apparatus (C-19)

**Axis:** Output format -- apparatus type uniformity via all-table schema
**Hypothesis:** R4 V-05 scores 145/150 (C-18 PASS + C-20 PASS, C-19 FAIL). The sole gap is
C-19: Phase 2 uses labeled text slots and Phase 4 uses a dual-line template -- mixed apparatus.
V-02 converts both to table schema: Phase 2 becomes a 3-row mechanism table; Phase 4 becomes a
2-row whitespace table. The SR block FAILS/PASS for SR2 and SR4 are updated to reference table
rows. The verification loop sub-questions are adapted for table apparatus but remain symmetric.
Central question: does the all-table conversion preserve C-18 (via SR-block FAILS/PASS for table
rows) and C-20 (via adapted symmetric loop), pushing from 145 to 150? If SR-block FAILS/PASS
pairs for table rows satisfy C-18 equivalently to phase-instruction pairs for labeled slots, this
is a clean 150 path. If C-18 requires phase-instruction-level FAILS/PASS specifically, V-02
scores 147.5 (C-18 PARTIAL from SR-block-only coverage).

```
SETUP: Auto-detect product domain from README, CLAUDE.md, package.json, Glob. Do not prompt.

STRUCTURAL REQUIREMENTS -- hard format constraints. All three primary structural requirements
(SR1, SR2, SR4) enforce via table schema. An absent table or empty table row/cell is an
observable format failure. Confirm all four before submitting output:

  [ ] 1. PHASE 1 pre-map table present and fully populated before any competitor entry.
         Required when focus is provided.
         FAILS: Prose paragraph; absent table; table with empty cells.
         PASS: Markdown table with named schema, all cells populated, present before Phase 2.

  [ ] 2. PHASE 2 inertia mechanism table: all three rows (WORKAROUND SATISFACTION, SWITCHING
         COST, HABIT LOCK-IN) populated with domain-exclusive content.
         FAILS: Absent table; empty table row; row content that passes the portability test
           (reads correctly for payroll software, a photo editor, or a scheduling tool).
         PASS: All three rows present, each populated with content that fails portability --
           specific tool names, workflow steps, artifact names wrong for any other domain.

  [ ] 3. PHASE 3 competitor table: Map Position column populated for every row including
         inertia. Verbatim Phase 1 row labels only.
         FAILS: Empty Map Position cell; paraphrased or generalized Phase 1 row label.
         PASS: Exact Phase 1 row label in every cell; no paraphrasing.

  [ ] 4. PHASE 4 whitespace table: both rows (Competitive gap, Focus gap) populated and
         grounded. Required when focus is provided.
         FAILS: Absent table; single-row table; row not grounded in Phase 1 data or Map
           Position column values; combined paragraph absent.
         PASS: Both rows present and grounded; combined paragraph names the dual-axis position
           with explicit reference to Phase 1 data and Map Position values from Phase 3.

Structural Requirements 1, 3, and 4 apply only when focus is provided.

PORTABILITY TEST (apply to every PHASE 2 mechanism row before accepting it):
"If I copied this row content unchanged into a competitor analysis for a clearly different
product -- payroll software, a photo editor, a scheduling tool -- would it still make sense?"
If yes, rewrite until recognizably wrong for any other product category.

PHASE 1 -- FOCUS LENS PRE-MAP (Structural Requirement 1):

If focus = market:
| Segment | Size Estimate | Growth Stage | Current Leader |
|---------|--------------|--------------|----------------|
3-5 rows. Fill all columns. Growth stage: emerging / growth / mature.
Current leader: named competitor or default behavior most dominant in this segment.
This is the competitive frame. Every competitor including inertia maps to exactly one row.

If focus = positioning:
| Positioning Category | Current Owner(s) | Vacancy Status |
|---------------------|-----------------|----------------|
3-5 rows. Fill all columns. Vacancy: open / contested / owned.
This is the competitive frame. Every competitor including inertia maps to exactly one row.

If no focus: skip Phase 1.

PHASE 2 -- INERTIA FIRST (Structural Requirement 2; mechanism table required):

Competitor 0: "None / status quo." Threat level: HIGH. State explicitly.
If Phase 1 was completed: record Phase 1 row in the Phase 3 table below.

| Mechanism | Domain-Exclusive Content |
|-----------|--------------------------|
| WORKAROUND SATISFACTION | [the specific tool, template, script, or duct-taped combination teams use instead of a dedicated solution; why it satisfies enough need that teams feel no pain and do not seek alternatives] |
| SWITCHING COST | [the concrete cost: specific format, role, process, or contract a team must lose or redo when adopting something new; quantify if possible -- hours, days, FTE cycles, budget range] |
| HABIT LOCK-IN | [the specific repeated behavior -- artifact, ritual, sprint cadence, or shared convention -- that makes the workaround feel normal in this product context] |

An empty row fails. Content that passes the portability test fails. Apply portability test to
each row. Use WebSearch if needed. Cite inline.

PHASE 3 -- COMPETITOR TABLE (Structural Requirement 3; Map Position column required):

| # | Competitor | Threat | Overlap | Map Position |
|---|------------|--------|---------|--------------|
| 0 | None / status quo | HIGH | -- | [exact Phase 1 row label] |
| 1 | [name] | H/M/L | H/M/L | [exact Phase 1 row label] |
| 2 | [name] | H/M/L | H/M/L | [exact Phase 1 row label] |
...

Map Position: exact Phase 1 row label. Verbatim -- do not paraphrase. Empty cell or paraphrased
label is a format failure. When no focus is provided, omit Map Position column entirely.
Add one sentence per competitor on threat relative to inertia and Map Position context.
Verify at least one major competitor claim via WebSearch. Cite inline.

PHASE 4 -- FINDINGS (Structural Requirement 4; whitespace table required when focus provided):

1. DUAL-AXIS WHITESPACE TABLE:

| Axis | Finding |
|------|---------|
| Competitive gap | No named competitor owns [X] because [reason]. Name which competitors come closest and which Map Position cells they occupy. |
| Focus gap | Phase 1 row [Y -- use exact row label from Phase 1 table] is unaddressed / unoccupied because [reason]. Reference Phase 1 table data (size, growth stage, or vacancy status). |

Combined (one paragraph below the table): the position simultaneously [X] (competitive gap)
and [Y] (focus gap) -- where a new entrant faces neither a dominant named competitor nor
inertia's strongest foothold from Phase 2. Ground in named Map Position values from Phase 3.

2. TABLE STAKES -- minimum requirements to be taken seriously over the WORKAROUND SATISFACTION
   row in the Phase 2 mechanism table. Reference at least one Phase 1 data point per item.

3. COMPETITIVE MATRIX -- top 3 by threat level, one recommendation sentence each, sorted
   high to low.

PRE-SUBMISSION VERIFICATION -- symmetric enforcement check, same three sub-questions per
constraint. Answer each before submitting. Any NO requires revision.

  SR1 (C-11): format artifact present (pre-map table)?
              format-failure declared ("absent table / empty cells fail")?
              enforcement apparatus present (FAILS/PASS pair)?

  SR2 (C-13): format artifact present (mechanism table, 3 rows)?
              format-failure declared ("empty row / generic row content fails")?
              enforcement apparatus present (FAILS/PASS pair)?

  SR4 (C-12): format artifact present (whitespace table, 2 rows)?
              format-failure declared ("absent table / single-row table fails")?
              enforcement apparatus present (FAILS/PASS pair)?

Also confirm SR3: Map Position column has no empty or paraphrased cells. Portability test
applied to each Phase 2 mechanism row.

AMEND: Exactly 3 items. Input change + output change. Specific.

Write artifact: simulations/discover/competitors/{topic}-competitors-alt-{date}.md
Frontmatter: skill, topic, date, skill_version, input, focus.
```

---

## V-03 -- All-Table + Phase-Level FAILS/PASS Pairs (C-18 + C-19)

**Axis:** Output format + phrasing register -- apparatus uniformity with explicit FAILS/PASS per
table phase instruction
**Hypothesis:** R4 V-03 (all-table, C-19 PASS = 140) missed C-18 because table phase instructions
used declarative failure language ("empty row fails") rather than labeled FAILS/PASS pairs. V-03
adds explicit FAILS/PASS pairs to each table's phase instruction: the mechanism table in Phase 2
gets its own pair; the whitespace table in Phase 4 gets its own pair. The Phase 1 table FAILS/PASS
pair was already present in the SR block. This tests whether phase-instruction-level FAILS/PASS
pairs on table apparatus satisfy C-18 in the same way that per-slot FAILS/PASS pairs did for
labeled-slot apparatus in R4. Expected: C-18 PASS, C-19 PASS, C-20 FAIL = 145.

```
SETUP: Auto-detect product domain from README, CLAUDE.md, package.json, Glob. Do not prompt.

STRUCTURAL REQUIREMENTS -- hard format constraints. All three primary structural requirements
(SR1, SR2, SR4) enforce via table schema. An absent table or empty table row/cell is an
observable format failure. Confirm all four before submitting output:

  [ ] 1. PHASE 1 pre-map table present and fully populated before any competitor entry.
         Required when focus is provided.
  [ ] 2. PHASE 2 inertia mechanism table: all three rows populated with domain-exclusive
         content. Empty row or generic row content fails.
  [ ] 3. PHASE 3 competitor table: Map Position column populated for every row including
         inertia. Empty cells and paraphrased Phase 1 row labels fail.
  [ ] 4. PHASE 4 whitespace table: both rows present and populated. Required when focus
         is provided. Missing row or single-row table fails.

Structural Requirements 1, 3, and 4 apply only when focus is provided.

PORTABILITY TEST (apply to every PHASE 2 mechanism row before accepting it):
"If I copied this row content unchanged into a competitor analysis for a clearly different
product -- payroll software, a photo editor, a scheduling tool -- would it still make sense?"
If yes, rewrite until recognizably wrong for any other product category.

PHASE 1 -- FOCUS LENS PRE-MAP (Structural Requirement 1; table schema required):

If focus = market:
| Segment | Size Estimate | Growth Stage | Current Leader |
|---------|--------------|--------------|----------------|
3-5 rows. Fill all columns. Growth stage: emerging / growth / mature.
Current leader: named competitor or default behavior most dominant in this segment.
This is the competitive frame. Every competitor including inertia maps to exactly one row.
FAILS: Prose paragraph listing segments; absent table; table with empty cells.
PASS: Markdown table with named schema, all cells populated, placed before Phase 2.

If focus = positioning:
| Positioning Category | Current Owner(s) | Vacancy Status |
|---------------------|-----------------|----------------|
3-5 rows. Fill all columns. Vacancy: open / contested / owned.
FAILS: Prose paragraph listing categories; absent table; table with empty cells.
PASS: Markdown table with named schema, all cells populated, placed before Phase 2.

If no focus: skip Phase 1.

PHASE 2 -- INERTIA FIRST (Structural Requirement 2; mechanism table required):

Competitor 0: "None / status quo." Threat level: HIGH. State explicitly.
If Phase 1 was completed: record Phase 1 row in the Phase 3 table below.

| Mechanism | Domain-Exclusive Content |
|-----------|--------------------------|
| WORKAROUND SATISFACTION | [the specific tool, template, script, or duct-taped combination teams use instead of a dedicated solution; why it satisfies enough need that teams feel no pain and do not seek alternatives] |
| SWITCHING COST | [the concrete cost: specific format, role, process, or contract a team must lose or redo when adopting something new; quantify if possible -- hours, days, FTE cycles, budget range] |
| HABIT LOCK-IN | [the specific repeated behavior -- artifact, ritual, sprint cadence, or shared convention -- that makes the workaround feel normal in this product context] |

FAILS: Mechanism table absent; any row empty; any row content that reads correctly for a
  clearly different product -- payroll software, a photo editor, or a scheduling tool.
PASS: All three rows present, each populated with content recognizably wrong in any other
  product category -- specific tool, process, artifact, or ritual named.

Apply portability test to each row. Use WebSearch if needed. Cite inline.

PHASE 3 -- COMPETITOR TABLE (Structural Requirement 3; Map Position column required):

| # | Competitor | Threat | Overlap | Map Position |
|---|------------|--------|---------|--------------|
| 0 | None / status quo | HIGH | -- | [exact Phase 1 row label] |
| 1 | [name] | H/M/L | H/M/L | [exact Phase 1 row label] |
| 2 | [name] | H/M/L | H/M/L | [exact Phase 1 row label] |
...

Map Position: exact Phase 1 row label. Verbatim -- do not paraphrase. Empty or paraphrased
cell is a format failure. When no focus is provided, omit Map Position column entirely.
Add one sentence per competitor on threat relative to inertia and Map Position context.
Verify at least one major competitor claim via WebSearch. Cite inline.

PHASE 4 -- FINDINGS (Structural Requirement 4; whitespace table required when focus provided):

1. DUAL-AXIS WHITESPACE TABLE:

| Axis | Finding |
|------|---------|
| Competitive gap | No named competitor owns [X] because [reason]. Name which competitors come closest and which Map Position cells they occupy. |
| Focus gap | Phase 1 row [Y -- use exact row label from Phase 1 table] is unaddressed / unoccupied because [reason]. Reference Phase 1 table data (size, growth stage, or vacancy status). |

FAILS: Whitespace table absent; single-row table; either row not grounded in Phase 1 data
  or Map Position column values; combined paragraph absent.
PASS: Both rows present and grounded; combined paragraph below table names the dual-axis
  position explicitly, referencing Phase 1 data and Map Position values from Phase 3.

Combined (one paragraph below the table): the position simultaneously [X] (competitive gap)
and [Y] (focus gap) -- where a new entrant faces neither a dominant named competitor nor
inertia's strongest foothold from Phase 2. Ground in named Map Position values from Phase 3.

2. TABLE STAKES -- minimum requirements to be taken seriously over the WORKAROUND SATISFACTION
   row in the Phase 2 mechanism table. Reference at least one Phase 1 data point per item.

3. COMPETITIVE MATRIX -- top 3 by threat level, one recommendation sentence each, sorted
   high to low.

Before submitting: verify all four Structural Requirements are met. Each of SR1, SR2, and SR4
must be a populated table -- not a prose block. SR1 table must precede Phase 2. SR2 mechanism
table must have all three rows filled with domain-exclusive content. SR4 whitespace table must
have both rows filled and grounded. Confirm SR3 Map Position column has no empty or paraphrased
cells. Check every Phase 2 mechanism row against the portability test.

AMEND: Exactly 3 items. Input change + output change. Specific.

Write artifact: simulations/discover/competitors/{topic}-competitors-alt-{date}.md
Frontmatter: skill, topic, date, skill_version, input, focus.
```

---

## V-04 -- All-Table + Symmetric Verification Loop (C-19 + C-20)

**Axis:** Output format + lifecycle emphasis -- apparatus uniformity with symmetric verification
**Hypothesis:** V-03 tests C-18 + C-19 (FAILS/PASS per table + all-table = 145). V-04 tests the
alternative two-criterion path: C-19 + C-20 (all-table + symmetric verification) without
phase-instruction FAILS/PASS pairs. The SR block carries failure language ("empty row fails") but
no labeled FAILS/PASS examples at the Phase 2 or Phase 4 instruction level -- those appear only in
the SR checklist items as declarative failure statements. The verification loop asks the same three
sub-questions per constraint (format artifact present? format-failure declared? enforcement apparatus
present?) for SR1, SR2, and SR4 in their table forms. This isolates whether C-18 truly requires
phase-instruction-level FAILS/PASS pairs, or whether "empty row fails" declarative language in the
SR block satisfies C-18 when the verification loop confirms it per constraint. If C-18 passes here,
C-18 does not require the labeled pair format specifically. Expected: C-18 FAIL, C-19 PASS, C-20
PASS = 145. If C-18 passes here, V-04 scores 150 and the labeled pair format is not load-bearing.

```
SETUP: Auto-detect product domain from README, CLAUDE.md, package.json, Glob. Do not prompt.

STRUCTURAL REQUIREMENTS -- hard format constraints. All three primary structural requirements
(SR1, SR2, SR4) enforce via table schema. An absent table or empty table row/cell is an
observable format failure. Confirm all four before submitting output:

  [ ] 1. PHASE 1 pre-map table present and fully populated before any competitor entry.
         Required when focus is provided. Absent table or empty cells fail.

  [ ] 2. PHASE 2 inertia mechanism table: all three rows (WORKAROUND SATISFACTION, SWITCHING
         COST, HABIT LOCK-IN) populated with domain-exclusive content. Empty row or content
         that passes the portability test fails.

  [ ] 3. PHASE 3 competitor table: Map Position column populated for every row including
         inertia. Empty cells and paraphrased Phase 1 row labels fail.

  [ ] 4. PHASE 4 whitespace table: both rows (Competitive gap, Focus gap) present and
         populated. Required when focus is provided. Absent table or single-row table fails.

Structural Requirements 1, 3, and 4 apply only when focus is provided.

PORTABILITY TEST (apply to every PHASE 2 mechanism row before accepting it):
"If I copied this row content unchanged into a competitor analysis for a clearly different
product -- payroll software, a photo editor, a scheduling tool -- would it still make sense?"
If yes, rewrite until recognizably wrong for any other product category.

PHASE 1 -- FOCUS LENS PRE-MAP (Structural Requirement 1; table schema required):

If focus = market:
| Segment | Size Estimate | Growth Stage | Current Leader |
|---------|--------------|--------------|----------------|
3-5 rows. Fill all columns. Growth stage: emerging / growth / mature.
Current leader: named competitor or default behavior most dominant in this segment.
This is the competitive frame. Every competitor including inertia maps to exactly one row.

If focus = positioning:
| Positioning Category | Current Owner(s) | Vacancy Status |
|---------------------|-----------------|----------------|
3-5 rows. Fill all columns. Vacancy: open / contested / owned.
This is the competitive frame. Every competitor including inertia maps to exactly one row.

If no focus: skip Phase 1.

PHASE 2 -- INERTIA FIRST (Structural Requirement 2; mechanism table required):

Competitor 0: "None / status quo." Threat level: HIGH. State explicitly.
If Phase 1 was completed: record Phase 1 row in the Phase 3 table below.

| Mechanism | Domain-Exclusive Content |
|-----------|--------------------------|
| WORKAROUND SATISFACTION | [the specific tool, template, script, or duct-taped combination teams use instead of a dedicated solution; why it satisfies enough need that teams feel no pain and do not seek alternatives] |
| SWITCHING COST | [the concrete cost: specific format, role, process, or contract a team must lose or redo when adopting something new; quantify if possible -- hours, days, FTE cycles, budget range] |
| HABIT LOCK-IN | [the specific repeated behavior -- artifact, ritual, sprint cadence, or shared convention -- that makes the workaround feel normal in this product context] |

An empty row fails. Content that passes the portability test fails. Apply portability test to
each row. Use WebSearch if needed. Cite inline.

PHASE 3 -- COMPETITOR TABLE (Structural Requirement 3; Map Position column required):

| # | Competitor | Threat | Overlap | Map Position |
|---|------------|--------|---------|--------------|
| 0 | None / status quo | HIGH | -- | [exact Phase 1 row label] |
| 1 | [name] | H/M/L | H/M/L | [exact Phase 1 row label] |
| 2 | [name] | H/M/L | H/M/L | [exact Phase 1 row label] |
...

Map Position: exact Phase 1 row label. Verbatim -- do not paraphrase. Empty or paraphrased
cell is a format failure. When no focus is provided, omit Map Position column entirely.
Add one sentence per competitor on threat relative to inertia and Map Position context.
Verify at least one major competitor claim via WebSearch. Cite inline.

PHASE 4 -- FINDINGS (Structural Requirement 4; whitespace table required when focus provided):

1. DUAL-AXIS WHITESPACE TABLE:

| Axis | Finding |
|------|---------|
| Competitive gap | No named competitor owns [X] because [reason]. Name which competitors come closest and which Map Position cells they occupy. |
| Focus gap | Phase 1 row [Y -- use exact row label from Phase 1 table] is unaddressed / unoccupied because [reason]. Reference Phase 1 table data (size, growth stage, or vacancy status). |

Combined (one paragraph below the table): the position simultaneously [X] (competitive gap)
and [Y] (focus gap) -- where a new entrant faces neither a dominant named competitor nor
inertia's strongest foothold from Phase 2. Ground in named Map Position values from Phase 3.

2. TABLE STAKES -- minimum requirements to be taken seriously over the WORKAROUND SATISFACTION
   row in the Phase 2 mechanism table. Reference at least one Phase 1 data point per item.

3. COMPETITIVE MATRIX -- top 3 by threat level, one recommendation sentence each, sorted
   high to low.

PRE-SUBMISSION VERIFICATION -- symmetric enforcement check, same three sub-questions per
constraint. Answer each before submitting. Any NO requires revision.

  SR1 (C-11): format artifact present (pre-map table)?
              format-failure declared ("absent table / empty cells fail")?
              enforcement apparatus present (table schema with named columns)?

  SR2 (C-13): format artifact present (mechanism table, 3 rows)?
              format-failure declared ("empty row / generic content fails")?
              enforcement apparatus present (table schema with named row labels)?

  SR4 (C-12): format artifact present (whitespace table, 2 rows)?
              format-failure declared ("absent table / single-row fails")?
              enforcement apparatus present (table schema with Competitive gap / Focus gap rows)?

Also confirm SR3: Map Position column has no empty or paraphrased cells. Portability test
applied to each Phase 2 mechanism row.

AMEND: Exactly 3 items. Input change + output change. Specific.

Write artifact: simulations/discover/competitors/{topic}-competitors-alt-{date}.md
Frontmatter: skill, topic, date, skill_version, input, focus.
```

---

## V-05 -- Full R5 Stack (C-18 + C-19 + C-20)

**Axes:** Output format + phrasing register + lifecycle emphasis
**Hypothesis:** The three R5 mechanisms are independent and additive. All-table apparatus (C-19)
achieves enforcement surface uniformity -- empty-cell failures are structurally identical across
all three constraints. Phase-level FAILS/PASS pairs per table instruction (C-18) add explicit
labeled rejection pairs at each constraint's phase instruction -- the named format artifact +
format-failure declaration + FAILS/PASS pair fingerprint is present at the table level, not just
the SR block. Symmetric verification loop (C-20) closes the bracket -- the same three sub-questions
are asked per constraint before submission, mirroring the opening SR block. None of the three
mechanisms interferes with the others: C-19 and C-18 combine at the phase instruction level; C-20
operates at pre-submission. V-05 is the R5 ceiling attempt. If 150/150 is not achieved, the gap
identifies which mechanism combination creates interference or which criterion requires something
not yet present in this stack.

```
SETUP: Auto-detect product domain from README, CLAUDE.md, package.json, Glob. Do not prompt.

STRUCTURAL REQUIREMENTS -- hard format constraints. All three primary structural requirements
(SR1, SR2, SR4) enforce via table schema. An absent table or empty table row/cell is an
observable format failure. Confirm all four before submitting output:

  [ ] 1. PHASE 1 pre-map table present and fully populated before any competitor entry.
         Required when focus is provided.
         FAILS: Prose paragraph; absent table; table with empty cells.
         PASS: Markdown table with named schema, all cells populated, placed before Phase 2.

  [ ] 2. PHASE 2 inertia mechanism table: all three rows (WORKAROUND SATISFACTION, SWITCHING
         COST, HABIT LOCK-IN) populated with domain-exclusive content.
         FAILS: Mechanism table absent; any row empty; any row content that reads correctly
           for payroll software, a photo editor, or a scheduling tool.
         PASS: All three rows present, each populated with content recognizably wrong in any
           other product category -- specific tool, process, artifact, or ritual named.

  [ ] 3. PHASE 3 competitor table: Map Position column populated for every row including
         inertia. Verbatim Phase 1 row labels only.
         FAILS: Empty Map Position cell; paraphrased or generalized Phase 1 row label.
         PASS: Exact Phase 1 row label in every cell; no paraphrasing.

  [ ] 4. PHASE 4 whitespace table: both rows (Competitive gap, Focus gap) present, populated,
         and grounded. Required when focus is provided.
         FAILS: Whitespace table absent; single-row table; row not grounded in Phase 1 data
           or Map Position values; combined paragraph absent.
         PASS: Both rows present and grounded; combined paragraph names the dual-axis position
           explicitly, referencing Phase 1 data and Map Position values from Phase 3.

Structural Requirements 1, 3, and 4 apply only when focus is provided.

PORTABILITY TEST (apply to every PHASE 2 mechanism row before accepting it):
"If I copied this row content unchanged into a competitor analysis for a clearly different
product -- payroll software, a photo editor, a scheduling tool -- would it still make sense?"
If yes, rewrite until recognizably wrong for any other product category.

PHASE 1 -- FOCUS LENS PRE-MAP (Structural Requirement 1):

If focus = market:
| Segment | Size Estimate | Growth Stage | Current Leader |
|---------|--------------|--------------|----------------|
3-5 rows. Fill all columns. Growth stage: emerging / growth / mature.
Current leader: named competitor or default behavior most dominant in this segment.
This is the competitive frame. Every competitor including inertia maps to exactly one row.
FAILS: Prose paragraph or absent table.
PASS: Markdown table, named schema, all cells populated, placed before Phase 2.

If focus = positioning:
| Positioning Category | Current Owner(s) | Vacancy Status |
|---------------------|-----------------|----------------|
3-5 rows. Fill all columns. Vacancy: open / contested / owned.
FAILS: Prose paragraph or absent table.
PASS: Markdown table, named schema, all cells populated, placed before Phase 2.

If no focus: skip Phase 1.

PHASE 2 -- INERTIA FIRST (Structural Requirement 2; mechanism table required):

Competitor 0: "None / status quo." Threat level: HIGH. State explicitly.
If Phase 1 was completed: record Phase 1 row in the Phase 3 table below.

| Mechanism | Domain-Exclusive Content |
|-----------|--------------------------|
| WORKAROUND SATISFACTION | [the specific tool, template, script, or duct-taped combination teams use instead of a dedicated solution; why it satisfies enough need that teams feel no pain and do not seek alternatives] |
| SWITCHING COST | [the concrete cost: specific format, role, process, or contract a team must lose or redo when adopting something new; quantify if possible -- hours, days, FTE cycles, budget range] |
| HABIT LOCK-IN | [the specific repeated behavior -- artifact, ritual, sprint cadence, or shared convention -- that makes the workaround feel normal in this product context] |

FAILS: Mechanism table absent; any row empty; any row content passing the portability test.
PASS: All three rows present with domain-exclusive content failing portability -- specific
  tool, workflow step, artifact name, or ritual recognizably wrong for any other domain.

Apply portability test to each row. Use WebSearch if needed. Cite inline.

PHASE 3 -- COMPETITOR TABLE (Structural Requirement 3; Map Position column required):

| # | Competitor | Threat | Overlap | Map Position |
|---|------------|--------|---------|--------------|
| 0 | None / status quo | HIGH | -- | [exact Phase 1 row label] |
| 1 | [name] | H/M/L | H/M/L | [exact Phase 1 row label] |
| 2 | [name] | H/M/L | H/M/L | [exact Phase 1 row label] |
...

Map Position: exact Phase 1 row label this competitor primarily occupies or contests.
Use Phase 1 row labels verbatim -- do not paraphrase or generalize. An empty cell or
paraphrased label is a format failure. When no focus is provided, omit Map Position column.
Add one sentence per competitor on threat relative to inertia and Map Position context.
Verify at least one major competitor claim via WebSearch. Cite inline.

PHASE 4 -- FINDINGS (Structural Requirement 4; whitespace table required when focus provided):

1. DUAL-AXIS WHITESPACE TABLE:

| Axis | Finding |
|------|---------|
| Competitive gap | No named competitor owns [X] because [reason]. Name which competitors come closest and which Map Position cells they occupy. |
| Focus gap | Phase 1 row [Y -- use exact row label from Phase 1 table] is unaddressed / unoccupied because [reason]. Reference Phase 1 table data (size, growth stage, or vacancy status). |

FAILS: Whitespace table absent; single-row table; either row not grounded in Phase 1 data or
  Map Position values; combined paragraph absent.
PASS: Both rows present and grounded; combined paragraph below table names the dual-axis
  position explicitly, grounded in Phase 1 data and Map Position column values from Phase 3.

Combined (one paragraph below the table): the position simultaneously [X] (competitive gap)
and [Y] (focus gap) -- where a new entrant faces neither a dominant named competitor nor
inertia's strongest foothold from Phase 2. Ground in named Map Position values from Phase 3.

2. TABLE STAKES -- minimum requirements to be taken seriously over the WORKAROUND SATISFACTION
   row in the Phase 2 mechanism table. Reference at least one Phase 1 data point per item.

3. COMPETITIVE MATRIX -- top 3 by threat level, one recommendation sentence each, sorted
   high to low.

PRE-SUBMISSION VERIFICATION -- symmetric enforcement check, same three sub-questions per
constraint. Answer each before submitting. Any NO requires revision.

  SR1 (C-11): format artifact present (pre-map table)?
              format-failure declared ("absent table / empty cells fail")?
              FAILS/PASS pair present?

  SR2 (C-13): format artifact present (mechanism table, 3 rows)?
              format-failure declared ("absent table / empty row / generic content fails")?
              FAILS/PASS pair present?

  SR4 (C-12): format artifact present (whitespace table, 2 rows)?
              format-failure declared ("absent table / single-row / ungrounded row fails")?
              FAILS/PASS pair present?

Also confirm SR3: Map Position column has no empty or paraphrased cells. Portability test
applied to each Phase 2 mechanism row. Combined paragraph present below Phase 4 table.

AMEND: Exactly 3 items. Input change + output change. Specific.

Write artifact: simulations/discover/competitors/{topic}-competitors-alt-{date}.md
Frontmatter: skill, topic, date, skill_version, input, focus.
```

---

## Rubric Criterion Coverage by Variation (R5)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 inertia-first | explicit | explicit | explicit | explicit | explicit |
| C-02 focus woven | pre-map + sequence | pre-map + sequence | pre-map + sequence | pre-map + sequence | pre-map + sequence |
| C-03 threat levels | explicit | explicit | explicit | explicit | explicit |
| C-04 whitespace | dual-line FAILS/PASS | 2-row table SR-FAILS/PASS | 2-row table + phase FAILS/PASS | 2-row table (no pairs) | 2-row table + phase FAILS/PASS |
| C-05 auto-detect | SETUP | SETUP | SETUP | SETUP | SETUP |
| C-06 inertia stickiness | labeled slots + FAILS/PASS | mechanism table SR-FAILS/PASS | mechanism table + phase FAILS/PASS | mechanism table (no pairs) | mechanism table + phase FAILS/PASS |
| C-07 web-verified | WebSearch + cite | WebSearch + cite | WebSearch + cite | WebSearch + cite | WebSearch + cite |
| C-08 AMEND | explicit | explicit | explicit | explicit | explicit |
| C-09 cross-dimensional | strong | strong | strong | strong | strong |
| C-10 table stakes | Phase 1 data per item | Phase 1 data per item | Phase 1 data per item | Phase 1 data per item | Phase 1 data per item |
| C-11 pre-map | table + FAILS/PASS (SR) | table + FAILS/PASS (SR) | table + FAILS/PASS (phase) | table (SR only) | table + FAILS/PASS (phase) |
| C-12 whitespace | dual-line + FAILS/PASS | 2-row table + SR-FAILS/PASS | 2-row table + phase FAILS/PASS | 2-row table (no pairs) | 2-row table + phase FAILS/PASS |
| C-13 inertia | labeled slots + FAILS/PASS | mechanism table + SR-FAILS/PASS | mechanism table + phase FAILS/PASS | mechanism table (no pairs) | mechanism table + phase FAILS/PASS |
| C-14 hard-stacked | meta-declaration + FAILS/PASS | meta-declaration + apparatus | all-table apparatus | all-table apparatus | all-table apparatus + FAILS/PASS |
| C-15 map position | Map Position column | Map Position column | Map Position column | Map Position column | Map Position column |
| C-16 domain-exclusive | portability test | portability test per row | portability test per row | portability test per row | portability test per row |
| C-17 symmetric enforcement | FAILS/PASS pairs (strong) | all-table apparatus | all-table apparatus | all-table apparatus | all-table + FAILS/PASS |
| **C-18 phase-level fingerprint** | **PASS** | **? (SR-block FAILS/PASS)** | **PASS** | **FAIL** | **PASS** |
| **C-19 apparatus uniformity** | **FAIL (mixed)** | **PASS (all tables)** | **PASS (all tables)** | **PASS (all tables)** | **PASS (all tables)** |
| **C-20 symmetric loop** | **PASS (symmetric 3-Q)** | **PASS (symmetric 3-Q adapted)** | **FAIL (no loop)** | **PASS (symmetric 3-Q adapted)** | **PASS (symmetric 3-Q adapted)** |

---

## Predicted Scores Under v5 Rubric

| Variation | Essential (/60) | Recommended (/30) | C-09-C-17 (/45) | C-18 (/5) | C-19 (/5) | C-20 (/5) | Composite (/150) |
|-----------|-----------------|-------------------|--------------------|-----------|-----------|-----------|------------------|
| V-01 | 60 | 30 | 45 | 5 | 0 | 5 | **145** |
| V-02 | 60 | 30 | 45 | 2.5-5 | 5 | 5 | **147.5-150** |
| V-03 | 60 | 30 | 45 | 5 | 5 | 0 | **145** |
| V-04 | 60 | 30 | 45 | 0 | 5 | 5 | **145** |
| V-05 | 60 | 30 | 45 | 5 | 5 | 5 | **150** |

**The key uncertainty is V-02:** Does SR-block FAILS/PASS (for table rows, not labeled slots)
satisfy C-18? C-18 requires "phase-level three-component fingerprint." The SR block precedes all
phases -- does it count as "phase-level" for C-11, C-12, C-13? In R4, the SR-block FAILS/PASS for
C-11 was accepted as C-18-satisfying. But C-12 and C-13 in R4's passing variations had FAILS/PASS
at the actual phase instruction level. V-02 puts FAILS/PASS for C-12 and C-13 only in the SR block.
If SR-block FAILS/PASS satisfies C-18 for all three constraints (as it did for C-11 in R4), V-02
scores 150. If C-18 requires phase-instruction-level pairs specifically for C-12 and C-13, V-02
scores 147.5 (C-18 PARTIAL).

---

## Recommended Test Order

1. **V-05** first -- ceiling attempt; if 150/150 confirmed, the full R5 stack is validated
2. **V-01** second -- C-20 isolation; confirms whether symmetric sub-question loop satisfies C-20
   independently on a C-18-passing base (145 expected)
3. **V-03** third -- C-18 + C-19 without loop; confirms whether phase-level FAILS/PASS on table
   apparatus achieves C-18 as well as labeled-slot FAILS/PASS did in R4 (145 expected)
4. **V-04** fourth -- C-19 + C-20 without pairs; tests C-18 exclusion cost and whether
   SR-block failure declarations satisfy C-18 when confirmed by symmetric loop (145 or 150)
5. **V-02** last -- all-table conversion of R4 V-05; resolves SR-block vs. phase-instruction
   FAILS/PASS equivalence question for C-18 (147.5 or 150)
