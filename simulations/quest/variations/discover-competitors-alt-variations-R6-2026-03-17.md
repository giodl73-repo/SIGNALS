Five complete variations written to `simulations/quest/variations/discover-competitors-alt-variations-R6-2026-03-17.md`.

**R6 setup:** R5 V-05 achieved 160/160 (full triple synthesis). R6 tests whether that achievement is robust across structural variations or whether R5 V-05's specific form is load-bearing.

| # | Axis | Hypothesis | Expected |
|---|------|------------|----------|
| V-01 | Inertia framing | Dual-table inertia (summary + mechanism tables); C-13 constraint is mechanism table; summary is additional framing | 160 |
| V-02 | Lifecycle emphasis | Pre-generation integrity check + post-generation PRE-SUBMISSION loop; tests whether C-20 "closing" requires end-of-prompt placement | 160 |
| V-03 | Phrasing register | Active imperative throughout (DO NOT / DO instead of FAILS / PASS); tests whether the specific label format is load-bearing for C-18 | 160 |
| V-04 | Role sequence | SR block eliminated entirely; constraints declared inline per phase; tests whether C-17 ("unified numbered block") fails without SR preamble, and whether C-21/C-22 survive C-17 failing | **155** |
| V-05 | Inertia framing + phrasing register | Conversational lead paragraph in Phase 2 + technical apparatus; tests whether narrative framing before the mechanism table weakens C-13 or C-14 | 160 |

**The two open questions for R6:**
1. **V-03 boundary:** Does C-18's "FAILS/PASS rejection example pair" require the specific `FAILS: ... PASS: ...` label format, or does a functionally equivalent `DO NOT: ... DO: ...` pair satisfy it?
2. **V-04 boundary:** Does C-17 require an opening SR preamble block specifically, or are phase-embedded declarations that produce identical output structure sufficient? If C-17 fails, do C-21 and C-22 survive independently?
phase-level instructions." Does removing the SR block preamble fail C-17 (and cascade to C-14), or do phase-embedded declarations satisfy it? If C-17 fails, does C-21/C-22 still pass from C-18+C-19+C-20?

---

## V-01 -- Elevated Inertia Framing (Dual-Table Inertia Apparatus)

**Axis:** Inertia framing -- Phase 2 inertia gets an Inertia Summary Table preceding the mechanism table
**Hypothesis:** R5 V-05 uses a single mechanism table for C-13 (Phase 2). V-01 adds an INERTIA SUMMARY TABLE (3 rows: Adoption Barrier, Abandonment Trigger, Competitive Hedge) as a strategic overview before the mechanism table. The mechanism table remains the C-13 structural constraint; the summary table is additional depth. SR block item 2 explicitly identifies the mechanism table as the C-13 constraint artifact. The verification loop still checks SR2 against the mechanism table. Tests whether dual-table inertia apparatus maintains C-19 (apparatus uniformity -- C-13 constraint apparatus is still a table), C-18 (phase-instruction FAILS/PASS pair on the mechanism table unchanged), C-21 (C-18+C-19), and C-22 (C-19+C-20). Risk: scoring agent may classify the summary table as the C-13 apparatus, potentially confusing C-19 uniformity if the structural separation is not clear.

```
SETUP: Auto-detect product domain from README, CLAUDE.md, package.json, Glob. Do not prompt.

STRUCTURAL REQUIREMENTS -- hard format constraints. All three primary structural requirements
(SR1, SR2, SR4) enforce via table schema. An absent table or empty table row/cell is an
observable format failure. Confirm all five before submitting output:

  [ ] 1. PHASE 1 pre-map table present and fully populated before any competitor entry.
         Required when focus is provided.
         FAILS: Prose paragraph listing segments or categories; absent table; table with empty
           cells.
         PASS: Markdown table with named schema, all cells populated, present before Phase 2.

  [ ] 2. PHASE 2 inertia: summary table (3 rows) AND mechanism table (3 rows) both present.
         C-13 structural constraint is the mechanism table specifically. Summary table is
         additional strategic framing and does not substitute for the mechanism table.
         FAILS (C-13): mechanism table absent; any mechanism row empty; any mechanism row
           content that reads correctly for payroll software, a photo editor, or a scheduling
           tool -- portability test passes.
         PASS (C-13): mechanism table present with all three rows, each populated with content
           recognizably wrong in any other product category.

  [ ] 3. PHASE 3 competitor table: Map Position column populated for every row including
         inertia. Verbatim Phase 1 row labels only.
         FAILS: Empty Map Position cell; paraphrased or generalized Phase 1 row label.
         PASS: Exact Phase 1 row label in every cell; no paraphrasing.

  [ ] 4. PHASE 4 whitespace table: both rows (Competitive gap, Focus gap) populated and
         grounded. Required when focus is provided.
         FAILS: Whitespace table absent; single-row table; either row not grounded in Phase 1
           data or Map Position column values; combined paragraph absent.
         PASS: Both rows present and grounded; combined paragraph below table names the
           dual-axis position with explicit Phase 1 and Map Position references.

  [ ] 5. ENFORCEMENT SYMMETRY: SR1 (C-11), SR2 (C-13), and SR4 (C-12) each carry a named
         format artifact (pre-map table / mechanism table / whitespace table), a format-failure
         declaration, and a FAILS/PASS rejection example pair. No constraint enforces via prose
         instruction alone.
         FAILS: Any of the three lacks a named format artifact, a format-failure declaration,
           or a FAILS/PASS pair.
         PASS: All three carry all three components in identical structure.

Structural Requirements 1, 3, 4, and 5 apply only when focus is provided.

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

PHASE 2 -- PRIMARY THREAT: STATUS QUO (Structural Requirement 2; two tables required):

Competitor 0: "None / status quo." Threat level: HIGH. State explicitly.
If Phase 1 was completed: record Phase 1 row in the Phase 3 table below.

INERTIA OVERVIEW (strategic framing; not the C-13 structural constraint):

| Dimension | Assessment | Strategic Implication |
|-----------|------------|-----------------------|
| Adoption Barrier | [the primary reason teams do not evaluate alternatives in this domain -- name the specific friction, not a generic claim] | [what this means for any entrant trying to displace status quo] |
| Abandonment Trigger | [the specific event or accumulation that finally drives teams to seek alternatives -- quantify if possible] | [how to position against this trigger] |
| Competitive Hedge | [the specific capability the workaround provides better than any dedicated solution in this domain] | [which features must beat this] |

INERTIA MECHANISMS (C-13 structural constraint; mechanism table required):

| Mechanism | Domain-Exclusive Content |
|-----------|--------------------------|
| WORKAROUND SATISFACTION | [the specific tool, template, script, or duct-taped combination teams use instead of a dedicated solution; why it satisfies enough need that teams feel no pain and do not seek alternatives] |
| SWITCHING COST | [the concrete cost: specific format, role, process, or contract a team must lose or redo when adopting something new; quantify if possible -- hours, days, FTE cycles, budget range] |
| HABIT LOCK-IN | [the specific repeated behavior -- artifact, ritual, sprint cadence, or shared convention -- that makes the workaround feel normal in this product context] |

FAILS: Mechanism table absent; any mechanism row empty; any mechanism row content that reads
  correctly for payroll software, a photo editor, or a scheduling tool.
PASS: All three mechanism rows present, each populated with content recognizably wrong in any
  other product category -- specific tool, process, artifact, or ritual named.

Apply portability test to each mechanism row. Use WebSearch if needed. Cite inline.

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
   mechanism row in Phase 2. Reference at least one Phase 1 data point per item.

3. COMPETITIVE MATRIX -- top 3 by threat level, one recommendation sentence each, sorted
   high to low.

PRE-SUBMISSION VERIFICATION -- symmetric enforcement check, same three sub-questions per
constraint. Answer each before submitting. Any NO requires revision.

  SR1 (C-11): format artifact present (pre-map table)?
              format-failure declared ("absent table / empty cells fail")?
              FAILS/PASS pair present?

  SR2 (C-13): format artifact present (mechanism table, 3 rows)?
              format-failure declared ("empty row / portability-passing content fails")?
              FAILS/PASS pair present?

  SR4 (C-12): format artifact present (whitespace table, 2 rows)?
              format-failure declared ("absent table / single-row table fails")?
              FAILS/PASS pair present?

Also confirm SR3: Map Position column has no empty or paraphrased cells. Portability test
applied to each Phase 2 mechanism row.

AMEND: Exactly 3 items. Input change + output change. Specific.

Write artifact: simulations/discover/competitors/{topic}-competitors-alt-{date}.md
Frontmatter: skill, topic, date, skill_version, input, focus.
```

---

## V-02 -- Dual Loop: Pre-generation + Post-generation (Lifecycle Emphasis)

**Axis:** Lifecycle emphasis -- symmetric verification loop appears at BOTH the opening (pre-generation integrity check) and closing (pre-submission verification)
**Hypothesis:** R5 V-05 places one symmetric loop at the end (pre-submission). C-20 requires "a closing pre-submission verification checklist." V-02 adds a second identical loop at the opening labeled "PRE-GENERATION INTEGRITY CHECK" -- before any phase runs, the model confirms that the prompt contains all required apparatus. The closing loop (labeled "PRE-SUBMISSION VERIFICATION") remains identical to R5 V-05's loop. The two loops ask identical sub-questions but serve different purposes: the opening loop confirms prompt completeness before generation, the closing loop confirms output completeness before submission. Tests: (1) does having two loops confuse C-20's "closing" requirement; (2) does the pre-generation loop add observable enforcement value; (3) does C-20's "closing pre-submission" strictly require end-of-prompt placement. Expected: 160/160 -- the closing loop is present, symmetric, and labeled "PRE-SUBMISSION VERIFICATION." C-18/C-19 apparatus unchanged. Risk: scoring agent reads the opening loop as THE loop satisfying C-20, then finds the closing loop redundant, potentially marking C-20 ambiguous or PARTIAL.

```
PRE-GENERATION INTEGRITY CHECK -- before generating any output, confirm the following
structural requirements exist in this prompt. If any NO, re-read the prompt before proceeding.

  SR1 (C-11): format artifact declared in prompt (pre-map table schema)?
              format-failure declared in prompt?
              FAILS/PASS pair present in prompt?

  SR2 (C-13): format artifact declared in prompt (mechanism table, 3 rows)?
              format-failure declared in prompt?
              FAILS/PASS pair present in prompt?

  SR4 (C-12): format artifact declared in prompt (whitespace table, 2 rows)?
              format-failure declared in prompt?
              FAILS/PASS pair present in prompt?

All YES: proceed to SETUP.

SETUP: Auto-detect product domain from README, CLAUDE.md, package.json, Glob. Do not prompt.

STRUCTURAL REQUIREMENTS -- hard format constraints. All three primary structural requirements
(SR1, SR2, SR4) enforce via table schema. An absent table or empty table row/cell is an
observable format failure. Confirm all four before submitting output:

  [ ] 1. PHASE 1 pre-map table present and fully populated before any competitor entry.
         Required when focus is provided.
         FAILS: Prose paragraph listing segments or categories; absent table; table with empty
           cells.
         PASS: Markdown table with named schema, all cells populated, present before Phase 2.

  [ ] 2. PHASE 2 inertia mechanism table: all three rows (WORKAROUND SATISFACTION, SWITCHING
         COST, HABIT LOCK-IN) populated with domain-exclusive content.
         FAILS: Mechanism table absent; any row empty; any row content that reads correctly
           for payroll software, a photo editor, or a scheduling tool.
         PASS: All three rows present, each populated with content recognizably wrong in any
           other product category.

  [ ] 3. PHASE 3 competitor table: Map Position column populated for every row including
         inertia. Verbatim Phase 1 row labels only.
         FAILS: Empty Map Position cell; paraphrased or generalized Phase 1 row label.
         PASS: Exact Phase 1 row label in every cell; no paraphrasing.

  [ ] 4. PHASE 4 whitespace table: both rows (Competitive gap, Focus gap) populated and
         grounded. Required when focus is provided.
         FAILS: Whitespace table absent; single-row table; either row not grounded in Phase 1
           data or Map Position column values; combined paragraph absent.
         PASS: Both rows present and grounded; combined paragraph below table names the
           dual-axis position with explicit Phase 1 and Map Position references.

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

PRE-SUBMISSION VERIFICATION -- symmetric enforcement check, same three sub-questions per
constraint. Answer each before submitting output. Any NO requires revision.

  SR1 (C-11): format artifact present (pre-map table)?
              format-failure declared ("absent table / empty cells fail")?
              FAILS/PASS pair present?

  SR2 (C-13): format artifact present (mechanism table, 3 rows)?
              format-failure declared ("empty row / portability-passing content fails")?
              FAILS/PASS pair present?

  SR4 (C-12): format artifact present (whitespace table, 2 rows)?
              format-failure declared ("absent table / single-row table fails")?
              FAILS/PASS pair present?

Also confirm SR3: Map Position column has no empty or paraphrased cells. Portability test
applied to each Phase 2 mechanism row.

AMEND: Exactly 3 items. Input change + output change. Specific.

Write artifact: simulations/discover/competitors/{topic}-competitors-alt-{date}.md
Frontmatter: skill, topic, date, skill_version, input, focus.
```

---

## V-03 -- Active Imperative Register

**Axis:** Phrasing register -- all instructions converted from declarative/passive to active imperative
**Hypothesis:** R5 V-05 uses formal declarative register: "All three primary structural requirements enforce via table schema. An absent table or empty table row/cell is an observable format failure." V-03 rewrites every instruction in direct command form. The apparatus is identical to R5 V-05 (all-table, phase-instruction FAILS/PASS pairs, symmetric loop). The structural components (named format artifact + failure declaration + FAILS/PASS pair) are all present. The register change is surface only. Tests whether declarative vs. imperative framing is neutral for C-18, C-19, C-20, C-21, and C-22. Expected: 160/160 -- register is a surface property; structural components are present regardless of phrasing style. Risk: if the scoring agent interprets "FAILS/PASS pair" as requiring the specific label format ("FAILS: ... PASS: ..."), converting to imperative ("DO NOT: X. DO: Y instead.") might break C-18 even though the rejection example is present in substance. Secondary risk: C-17 language ("observable signature of a prompt that declared all structural requirements") may be read as requiring declarative SR block language specifically.

```
SETUP: Detect the product domain. Read README, CLAUDE.md, package.json, Glob-discoverable
files. Do not ask the user. Infer everything.

STRUCTURAL REQUIREMENTS: Use table schema for every structural constraint. Do not use prose
blocks, labeled-slot text, or dual-line templates for SR1, SR2, or SR4. Build every required
table. Leave no row or cell empty. Verify all five before submitting output:

  [ ] 1. Build the PHASE 1 pre-map table before writing any competitor entry. Required when
         focus is provided.
         DO NOT: Write a prose paragraph listing segments. Leave any cell empty. Place this
           table after Phase 2.
         DO: Build a Markdown table with named columns. Fill every cell. Place it before Phase 2.

  [ ] 2. Build the PHASE 2 mechanism table with all three rows. Fill every row with
         domain-exclusive content.
         DO NOT: Omit any row. Write row content that a reader could copy into a payroll,
           photo editor, or scheduling tool analysis without it sounding wrong.
         DO: Name the specific tool, process, artifact, or ritual tied to this product domain.
           Make every row fail the portability test.

  [ ] 3. Build the PHASE 3 competitor table. Include a Map Position column when focus is
         provided. Use verbatim Phase 1 row labels -- no paraphrasing, no generalizing.
         DO NOT: Leave any Map Position cell empty. Paraphrase Phase 1 row labels.
         DO: Copy the exact Phase 1 row label into every Map Position cell.

  [ ] 4. Build the PHASE 4 whitespace table with both rows filled. Required when focus is
         provided. Write the combined paragraph immediately after the table.
         DO NOT: Omit the table. Build only one row. Leave either row ungrounded. Omit the
           combined paragraph below the table.
         DO: Fill both rows with findings grounded in Phase 1 data and Phase 3 Map Position
           values.

  [ ] 5. Check enforcement symmetry. Confirm SR1 (C-11), SR2 (C-13), and SR4 (C-12) each
         carry a named format artifact, a failure statement, and a rejection example pair.
         DO NOT: Accept a constraint where the format artifact is unnamed, the failure mode is
           unstated, or no rejection example pair (DO NOT / DO) exists.
         DO: Confirm all three components are present for each of the three constraints.

Apply structural requirements 1, 3, 4, and 5 only when focus is provided.

PORTABILITY TEST: For every Phase 2 mechanism row, ask: "Could I copy this row unchanged into
a competitor analysis for payroll software, a photo editor, or a scheduling tool and have it
still make sense?" If yes, rewrite. Stop only when the answer is clearly no.

PHASE 1 -- FOCUS LENS PRE-MAP: Build this table before writing any competitor entry. (SR1;
required when focus is provided.)

For market focus, build:
| Segment | Size Estimate | Growth Stage | Current Leader |
|---------|--------------|--------------|----------------|
Use 3-5 rows. Fill every column. Growth stage: emerging / growth / mature. Name the current
leader as the specific competitor or default behavior dominating this segment. Every competitor
including inertia must map to exactly one row in this table.
DO NOT: List segments in prose. Leave any cell empty. Place this table after Phase 2.
DO: Build the table. Fill every cell. Place it before Phase 2.

For positioning focus, build:
| Positioning Category | Current Owner(s) | Vacancy Status |
|---------------------|-----------------|----------------|
Use 3-5 rows. Fill every column. Vacancy choices: open / contested / owned.
DO NOT: List categories in prose. Leave any cell empty. Place this table after Phase 2.
DO: Build the table. Fill every cell. Place it before Phase 2.

No focus: skip Phase 1 entirely.

PHASE 2 -- INERTIA FIRST: Assess the status quo before any named competitor. (SR2.)

Name Competitor 0 as "None / status quo." State threat level HIGH explicitly.
If Phase 1 ran: note which Phase 1 row inertia occupies for entry in Phase 3.

Build this mechanism table:
| Mechanism | Domain-Exclusive Content |
|-----------|--------------------------|
| WORKAROUND SATISFACTION | [the specific tool, template, script, or duct-taped combination teams use instead of a dedicated solution; explain why it satisfies enough need that teams feel no pain and do not seek alternatives] |
| SWITCHING COST | [the concrete cost: name the specific format, role, process, or contract a team must lose or redo when adopting something new; quantify if possible] |
| HABIT LOCK-IN | [the specific repeated behavior -- artifact, ritual, sprint cadence, or shared convention -- that makes the workaround feel normal in this product context] |

DO NOT: Omit the mechanism table. Leave any row empty. Write row content that passes the
  portability test.
DO: Fill all three rows with content so domain-specific it would be obviously wrong in any
  other product context.

Run the portability test on every row. Use WebSearch if needed. Cite inline.

PHASE 3 -- COMPETITOR TABLE: Build this table. Include Map Position column when focus is
provided. (SR3.)

| # | Competitor | Threat | Overlap | Map Position |
|---|------------|--------|---------|--------------|
| 0 | None / status quo | HIGH | -- | [exact Phase 1 row label] |
| 1 | [name] | H/M/L | H/M/L | [exact Phase 1 row label] |
| 2 | [name] | H/M/L | H/M/L | [exact Phase 1 row label] |
...

Map Position: copy the exact Phase 1 row label. Do not paraphrase. Do not generalize. An empty
cell or paraphrased label fails. When no focus is provided, omit Map Position column entirely.
Write one sentence per competitor on threat relative to inertia and Map Position context.
Verify at least one major competitor claim via WebSearch. Cite inline.

PHASE 4 -- FINDINGS: Build the whitespace table and write the combined paragraph. (SR4;
required when focus is provided.)

1. DUAL-AXIS WHITESPACE: Build this table, then write the combined paragraph immediately below.

| Axis | Finding |
|------|---------|
| Competitive gap | No named competitor owns [X] because [reason]. Name which competitors come closest and which Map Position cells they occupy. |
| Focus gap | Phase 1 row [Y -- use the exact row label from Phase 1] is unaddressed / unoccupied because [reason]. Reference Phase 1 table data. |

DO NOT: Build only one row. Leave either row without Phase 1 or Map Position grounding. Omit
  the combined paragraph.
DO: Fill both rows with grounded findings. Write the combined paragraph immediately after.

Combined (paragraph immediately below the table): name the position simultaneously [X]
(competitive gap) and [Y] (focus gap) -- where a new entrant faces neither a dominant named
competitor nor inertia's strongest foothold from Phase 2. Ground in named Map Position values
from Phase 3.

2. TABLE STAKES: List minimum requirements to displace the WORKAROUND SATISFACTION row from
   Phase 2. Reference at least one Phase 1 data point per item.

3. COMPETITIVE MATRIX: List the top 3 competitors by threat level, sorted high to low, one
   recommendation sentence each.

PRE-SUBMISSION VERIFICATION -- same three questions per constraint. Answer all before
submitting. Any NO requires revision.

  SR1 (C-11): format artifact present (pre-map table)?
              format-failure declared ("absent table / empty cells fail")?
              rejection example pair present (DO NOT/DO)?

  SR2 (C-13): format artifact present (mechanism table, 3 rows)?
              format-failure declared ("empty row / portability-passing content fails")?
              rejection example pair present (DO NOT/DO)?

  SR4 (C-12): format artifact present (whitespace table, 2 rows)?
              format-failure declared ("absent table / single-row fails")?
              rejection example pair present (DO NOT/DO)?

Confirm SR3: Map Position column has no empty or paraphrased cells.

AMEND: Exactly 3 items. Input change + output change. Specific.

Write artifact: simulations/discover/competitors/{topic}-competitors-alt-{date}.md
Frontmatter: skill, topic, date, skill_version, input, focus.
```

---

## V-04 -- SR-Free Phase-Embedded Declarations (Role Sequence)

**Axis:** Role sequence -- opening SR block eliminated; each phase carries full apparatus declaration inline
**Hypothesis:** R5 V-05 uses an upfront SR block that (a) declares all three constraints simultaneously in one numbered list, (b) establishes the all-table apparatus meta-requirement, and (c) names the enforcement symmetry criterion explicitly. V-04 removes this SR block entirely. Each phase header carries its full apparatus inline: named format artifact + format-failure declaration + FAILS/PASS pair. The verification loop at the end mirrors the phase declarations. Tests whether C-14 (hard-stacked: output simultaneously satisfies C-11+C-12+C-13 as visible format constraints) and C-17 (symmetric enforcement signature: "the output-observable signature of a prompt that declared all structural requirements in a unified numbered block") require the SR block meta-declaration, or whether phase-embedded declarations satisfy them. If C-17 fails (no unified SR block), expected cascade: C-17 FAIL (-5). C-14 may survive -- it requires all three format constraints visible in the output, not necessarily co-declared in the prompt. C-18, C-19, C-20 remain independently satisfied; C-21 and C-22 should hold. Expected: 155/160 if C-17 fails. 160/160 if phase-embedded declarations satisfy C-17. The finding clarifies whether C-17 is a prompt-structure criterion (SR preamble required) or an output-structure criterion.

```
SETUP: Auto-detect product domain from README, CLAUDE.md, package.json, Glob. Do not prompt.

All three structural constraints (C-11 pre-map, C-13 inertia mechanisms, C-12 whitespace)
enforce via table schema. An absent table or empty row/cell is an observable format failure.

PORTABILITY TEST (apply to every PHASE 2 mechanism row):
"If I copied this row content unchanged into a competitor analysis for a clearly different
product -- payroll software, a photo editor, a scheduling tool -- would it still make sense?"
If yes, rewrite until recognizably wrong for any other product category.

PHASE 1 -- FOCUS LENS PRE-MAP

C-11 structural constraint. Apparatus: table schema. Required when focus is provided.

If focus = market:
| Segment | Size Estimate | Growth Stage | Current Leader |
|---------|--------------|--------------|----------------|
3-5 rows. Fill all columns. Growth stage: emerging / growth / mature.
Current leader: named competitor or default behavior most dominant in this segment.
Every competitor including inertia maps to exactly one row. This is the competitive frame.
FAILS: Prose paragraph listing segments; absent table; table with empty cells.
PASS: Markdown table with named schema, all cells populated, placed before Phase 2.

If focus = positioning:
| Positioning Category | Current Owner(s) | Vacancy Status |
|---------------------|-----------------|----------------|
3-5 rows. Fill all columns. Vacancy: open / contested / owned.
FAILS: Prose paragraph listing categories; absent table; table with empty cells.
PASS: Markdown table with named schema, all cells populated, placed before Phase 2.

If no focus: skip Phase 1.

PHASE 2 -- INERTIA FIRST

C-13 structural constraint. Apparatus: table schema. An absent table or empty row fails.

Competitor 0: "None / status quo." Threat level: HIGH. State explicitly.
If Phase 1 was completed: record Phase 1 row in the Phase 3 table below.

| Mechanism | Domain-Exclusive Content |
|-----------|--------------------------|
| WORKAROUND SATISFACTION | [the specific tool, template, script, or duct-taped combination teams use instead of a dedicated solution; why it satisfies enough need that teams feel no pain and do not seek alternatives] |
| SWITCHING COST | [the concrete cost: specific format, role, process, or contract a team must lose or redo when adopting something new; quantify if possible -- hours, days, FTE cycles, budget range] |
| HABIT LOCK-IN | [the specific repeated behavior -- artifact, ritual, sprint cadence, or shared convention -- that makes the workaround feel normal in this product context] |

FAILS: Mechanism table absent; any row empty; any row content that reads correctly for
  payroll software, a photo editor, or a scheduling tool -- portability test passes.
PASS: All three rows present, each populated with content recognizably wrong in any other
  product category -- specific tool, process, artifact, or ritual named.

Apply portability test to each row. Use WebSearch if needed. Cite inline.

PHASE 3 -- COMPETITOR TABLE

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

PHASE 4 -- FINDINGS

C-12 structural constraint. Apparatus: table schema. Required when focus is provided.

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
   mechanism row in Phase 2. Reference at least one Phase 1 data point per item.

3. COMPETITIVE MATRIX -- top 3 by threat level, one recommendation sentence each, sorted
   high to low.

PRE-SUBMISSION VERIFICATION -- symmetric enforcement check, same three sub-questions per
constraint. Answer each before submitting. Any NO requires revision.

  C-11 (Phase 1 pre-map): format artifact present (pre-map table)?
                          format-failure declared ("absent table / empty cells fail")?
                          FAILS/PASS pair present?

  C-13 (Phase 2 mechanism): format artifact present (mechanism table, 3 rows)?
                             format-failure declared ("empty row / portability-passing fails")?
                             FAILS/PASS pair present?

  C-12 (Phase 4 whitespace): format artifact present (whitespace table, 2 rows)?
                              format-failure declared ("absent table / single-row fails")?
                              FAILS/PASS pair present?

Confirm Map Position column has no empty or paraphrased cells. Portability test applied to
each Phase 2 mechanism row.

AMEND: Exactly 3 items. Input change + output change. Specific.

Write artifact: simulations/discover/competitors/{topic}-competitors-alt-{date}.md
Frontmatter: skill, topic, date, skill_version, input, focus.
```

---

## V-05 -- Conversational Inertia Framing + Technical Apparatus (Combined)

**Axis:** Inertia framing + phrasing register -- Phase 2 inertia section uses conversational narrative framing; SR block and all enforcement apparatus remain fully technical
**Hypothesis:** R5 V-05 uses uniform formal-technical register throughout. V-05 introduces a register split: Phase 2 opens with a plain-language lead paragraph naming inertia as the primary threat ("The real competitor here is not a named product -- it is the team's existing way of doing things"), followed by the standard all-table mechanism apparatus with technical FAILS/PASS pairs. The SR block, portability test, Phase 1, Phase 3, Phase 4, and verification loop remain identical to R5 V-05. Tests whether the narrative framing in Phase 2 affects C-06 (inertia stickiness reasoning -- does plain language strengthen mechanism specificity signal?), C-13 (three labeled mechanism slots -- mechanism table unchanged, PASS expected), C-16 (domain-exclusive -- mechanism rows still portability-tested), and C-18 (phase-instruction fingerprint -- FAILS/PASS pair on mechanism table unchanged). Register mixing should be neutral for C-19, C-20, C-21, and C-22. Expected: 160/160. Risk: the conversational lead paragraph in Phase 2 may appear to function as a prose substitute for the mechanism table, weakening C-13 or C-14 if the scoring agent reads the narrative as the primary C-13 compliance artifact rather than the table.

```
SETUP: Auto-detect product domain from README, CLAUDE.md, package.json, Glob. Do not prompt.

STRUCTURAL REQUIREMENTS -- hard format constraints. All three primary structural requirements
(SR1, SR2, SR4) enforce via table schema. An absent table or empty table row/cell is an
observable format failure. Confirm all five before submitting output:

  [ ] 1. PHASE 1 pre-map table present and fully populated before any competitor entry.
         Required when focus is provided.
         FAILS: Prose paragraph listing segments or categories; absent table; table with empty
           cells.
         PASS: Markdown table with named schema, all cells populated, present before Phase 2.

  [ ] 2. PHASE 2 inertia mechanism table: all three rows (WORKAROUND SATISFACTION, SWITCHING
         COST, HABIT LOCK-IN) populated with domain-exclusive content.
         FAILS: Mechanism table absent; any row empty; any row content that reads correctly
           for payroll software, a photo editor, or a scheduling tool.
         PASS: All three rows present, each populated with content recognizably wrong in any
           other product category.

  [ ] 3. PHASE 3 competitor table: Map Position column populated for every row including
         inertia. Verbatim Phase 1 row labels only.
         FAILS: Empty Map Position cell; paraphrased or generalized Phase 1 row label.
         PASS: Exact Phase 1 row label in every cell; no paraphrasing.

  [ ] 4. PHASE 4 whitespace table: both rows (Competitive gap, Focus gap) populated and
         grounded. Required when focus is provided.
         FAILS: Whitespace table absent; single-row table; either row not grounded in Phase 1
           data or Map Position column values; combined paragraph absent.
         PASS: Both rows present and grounded; combined paragraph below table names the
           dual-axis position with explicit Phase 1 and Map Position references.

  [ ] 5. ENFORCEMENT SYMMETRY: SR1 (C-11), SR2 (C-13), and SR4 (C-12) each carry a named
         format artifact (pre-map table / mechanism table / whitespace table), a format-failure
         declaration, and a FAILS/PASS rejection example pair. No constraint enforces via prose
         instruction alone.
         FAILS: Any of the three lacks a named format artifact, a format-failure declaration,
           or a FAILS/PASS pair.
         PASS: All three carry all three components in identical structure.

Structural Requirements 1, 3, 4, and 5 apply only when focus is provided.

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

PHASE 2 -- THE REAL COMPETITOR: STATUS QUO (Structural Requirement 2; mechanism table required):

Before assessing any named competitor, understand what you are actually up against. The most
dangerous competitor in almost every product market is not a named vendor -- it is the team's
existing way of doing things. They have already internalized the workaround. They have already
paid the setup cost. They feel no pain. Naming this competitor first is not a formality; it is
the only honest way to frame what displacement actually requires.

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
   mechanism row in Phase 2. Reference at least one Phase 1 data point per item.

3. COMPETITIVE MATRIX -- top 3 by threat level, one recommendation sentence each, sorted
   high to low.

PRE-SUBMISSION VERIFICATION -- symmetric enforcement check, same three sub-questions per
constraint. Answer each before submitting. Any NO requires revision.

  SR1 (C-11): format artifact present (pre-map table)?
              format-failure declared ("absent table / empty cells fail")?
              FAILS/PASS pair present?

  SR2 (C-13): format artifact present (mechanism table, 3 rows)?
              format-failure declared ("empty row / portability-passing content fails")?
              FAILS/PASS pair present?

  SR4 (C-12): format artifact present (whitespace table, 2 rows)?
              format-failure declared ("absent table / single-row table fails")?
              FAILS/PASS pair present?

Also confirm SR3: Map Position column has no empty or paraphrased cells. Portability test
applied to each Phase 2 mechanism row.

AMEND: Exactly 3 items. Input change + output change. Specific.

Write artifact: simulations/discover/competitors/{topic}-competitors-alt-{date}.md
Frontmatter: skill, topic, date, skill_version, input, focus.
```
