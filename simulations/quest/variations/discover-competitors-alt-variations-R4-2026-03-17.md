## R4 Variations — `discover-competitors-alt`

Five complete variations written to `simulations/quest/variations/discover-competitors-alt-variations-R4-2026-03-17.md`.

**Target criterion:** C-17 — Symmetric structural enforcement signature (new in v4)

**Setup:** R3 V-05 retroactively scores 135/135 under v4 because its meta-constraint block satisfies C-17 as a side effect. R4 asks: what are the minimal and alternative mechanisms that *reliably* produce symmetric enforcement?

| # | Axis | Mechanism | C-17 path |
|---|------|-----------|-----------|
| V-01 | Symmetric FAILS/PASS rejection pairs | Identical format per constraint | Implicit — symmetry emerges from format pattern |
| V-02 | Explicit C-17 as SR #5 | Names enforcement symmetry as a checklist item | Direct — same declaration mechanism that proved load-bearing for C-14 in R3 V-03 |
| V-03 | All-table structural apparatus | Table schema for C-11, C-12, and C-13 | Structural — apparatus type uniformity rather than enforcement rigor symmetry |
| V-04 | SR #5 + symmetric pairs | V-02 + V-01 combined | Combined — tests which mechanism is load-bearing |
| V-05 | Full R4 stack | R3 V-05 base + SR5 + symmetric pairs + symmetric verification | Composite ceiling; 135/135 expected |

**Key design decision:** V-03 is the most structurally novel variation — converting C-12 (whitespace) and C-13 (inertia slots) to table schema creates a 2-row and 3-row table respectively, making all three constraints visible as empty-cell failures rather than absent text fields. V-01 and V-02 stay closer to the R3 V-05 structure and vary the enforcement declaration surface. V-04 is the cleaner load-bearing test since it excludes V-03's all-table rewrite.
tisfied as hard format requirements. C-17 requires all three to be satisfied through the
  *same structural mechanism* — not just all three satisfied. A C-14 pass with one table-schema
  constraint and two prose-instruction constraints fails C-17. The enforcement rigor must be
  symmetric, not merely universal.

- **Observable test for C-17:** C-11 pre-map uses a table schema; C-12 whitespace uses a two-slot
  template with both lines declared mandatory; C-13 has three labeled slots with named rejection
  examples. The question R4 asks: what prompt mechanisms reliably produce this fingerprint across
  all three simultaneously?

- **Three candidate mechanisms from R3 signals:**
  1. Meta-constraint declaration (V-03 pattern) — names all requirements as a unified block
  2. Symmetric rejection examples — identical FAILS/PASS format per constraint creates observable symmetry
  3. Apparatus uniformity — using the same structural type (table/slot/template) for all three

- **V-01 isolation:** Tests whether symmetric rejection examples alone achieve C-17 without
  explicitly naming it. If FAILS/PASS pairs produce identical enforcement fingerprints across
  all three constraints, C-17 should pass as a structural consequence.

- **V-02 isolation:** Tests whether explicitly adding C-17 as SR #5 in the meta-constraint
  checklist changes model behavior, the same way SR1-4 changed C-11 to C-14 compliance in R3 V-03.

- **V-03 isolation:** Tests whether converting all three constraints to table schema achieves C-17
  through mechanism uniformity — apparatus type is the symmetry signal, not enforcement rigor level.

**Recommended test order:** V-01 → V-02 → V-03 → V-04 → V-05.

---

## V-01 — Symmetric FAILS/PASS Rejection Pairs (C-17)

**Axis:** Rejection example format symmetry
**Hypothesis:** Adding an identical FAILS/PASS labeled rejection pair to each of the three
structural constraints (C-11 pre-map, C-13 inertia slots, C-12 whitespace) creates
symmetric enforcement rigor without explicitly naming C-17 or naming a unified enforcement
apparatus. When each constraint carries the same format — named format artifact + format-failure
declaration + FAILS/PASS example pair — the output shows identical enforcement fingerprints
across all three. This is the output-observable test for C-17: identical apparatus, identical
rigor level, no weaker-mechanism outlier. The hypothesis is that the symmetric format of the
prompt instructions transfers directly to symmetric enforcement in the output, without requiring
the model to be told "all constraints use the same apparatus." The rejection pair itself is
the apparatus declaration. If V-01 achieves C-17, it is a more minimal mechanism than R3 V-03's
meta-declaration — simpler, more portable to other skills.

```
SETUP: Auto-detect product domain from README, CLAUDE.md, package.json, Glob. Do not prompt.

STRUCTURAL REQUIREMENTS — hard format constraints. Any one absent or failing the stated
rejection criteria is an observable format failure. Confirm all four before submitting:

  [ ] 1. PHASE 1 pre-map table present and fully populated before any competitor entry.
         Required when focus is provided.
         FAILS: Prose paragraph listing segments; absent table; partially populated table.
         PASS: Markdown table with named schema, all cells populated, present before Phase 2.

  [ ] 2. PHASE 2 inertia: all three slots (WORKAROUND SATISFACTION, SWITCHING COST, HABIT
         LOCK-IN) populated with domain-exclusive content.
         FAILS: Any slot containing content that reads correctly for a clearly different product —
           payroll software, a photo editor, or a scheduling tool.
         PASS: Every slot names a specific tool, workflow step, artifact, or ritual recognizably
           wrong for any other product category.

  [ ] 3. PHASE 3 competitor table: Map Position column populated for every row including
         inertia. Exact Phase 1 row labels only.
         FAILS: Empty Map Position cell; paraphrased or generalized Phase 1 row label.
         PASS: Verbatim Phase 1 row label in every Map Position cell; no paraphrasing.

  [ ] 4. PHASE 4 whitespace finding: both Competitive gap line and Focus gap line present
         in one paragraph. Required when focus is provided.
         FAILS: Single-axis whitespace; two separate paragraphs for the two axes; missing label.
         PASS: One paragraph with "Competitive gap:" and "Focus gap:" both labeled and grounded.

Structural Requirements 1, 3, and 4 apply only when focus is provided.

PORTABILITY TEST (apply to every PHASE 2 slot before accepting it):
"If I copied this slot content unchanged into a competitor analysis for a clearly different
product — payroll software, a photo editor, a scheduling tool — would it still make sense?"
If yes, the content is too generic. Rewrite until it is recognizably wrong for any other
product category. Specific tool names, workflow steps, artifact names, and process details
anchor content to the domain; abstract mechanism names do not.

PHASE 1 — FOCUS LENS PRE-MAP (Structural Requirement 1):

If focus = market:
| Segment | Size Estimate | Growth Stage | Current Leader |
|---------|--------------|--------------|----------------|
3-5 rows. Fill all columns. Growth stage: emerging / growth / mature.
Current leader: the named competitor or default behavior most dominant in this segment.
This is the competitive frame. Every competitor including inertia maps to exactly one row.

If focus = positioning:
| Positioning Category | Current Owner(s) | Vacancy Status |
|---------------------|-----------------|----------------|
3-5 rows. Fill all columns. Vacancy: open / contested / owned.
This is the competitive frame. Every competitor including inertia maps to exactly one row.

If no focus: skip Phase 1.

PHASE 2 — INERTIA FIRST (Structural Requirement 2; all three slots mandatory):

Competitor 0: "None / status quo." Threat level: HIGH. State explicitly.
If Phase 1 was completed: record Phase 1 row in the Phase 3 table below.

WORKAROUND SATISFACTION:
Name the exact substitution — the specific tool, template, script, or duct-taped combination
of tools — that teams use instead of adopting a dedicated solution in this domain. Explain
why it satisfies enough need that teams feel no pain and do not seek alternatives.
FAILS: "Teams use workarounds" / naming a generic category (e.g., "spreadsheets") without the
  specific tool, template name, or combination unique to this product domain.
PASS: Names the exact template, duct-taped combination, or manual step that is recognizably
  specific to this product's competitive context and fails portability for any other product.

SWITCHING COST:
Name the concrete thing a team must lose or redo when they adopt something new in this
product context. Name the specific format, role, process, or contract at stake. Quantify if
possible (hours, days, FTE cycles, budget range).
FAILS: "Switching has a cost" / "migration effort required" without specifying what migrates
  from what to what in this domain.
PASS: Names the domain-specific format or workflow that must change — detail that would be
  obviously inapplicable in any other product category.

HABIT LOCK-IN:
Name the specific repeated behavior — the daily check, the weekly template, the sprint
artifact, the shared convention, the team ritual — that makes the workaround feel normal
in this product context. It does not need to be a conscious decision; it needs to be repeated.
FAILS: "Teams develop habits around their tools" / abstract habit description without naming
  the specific behavior as it exists in this product's workflow.
PASS: Names the habit — artifact, ritual, or routine — that would be recognizably wrong for
  any other domain and would not appear in a competitor analysis for a different product.

Portability test applied to each slot. Use WebSearch if needed. Cite inline.

PHASE 3 — COMPETITOR TABLE (Structural Requirement 3; Map Position column required):

| # | Competitor | Threat | Overlap | Map Position |
|---|------------|--------|---------|--------------|
| 0 | None / status quo | HIGH | — | [exact Phase 1 row label] |
| 1 | [name] | H/M/L | H/M/L | [exact Phase 1 row label] |
| 2 | [name] | H/M/L | H/M/L | [exact Phase 1 row label] |
...

Map Position: the exact Phase 1 row label this competitor primarily occupies or contests.
Use Phase 1 row labels verbatim — do not paraphrase or generalize. An empty cell or a
paraphrased label is a format failure. If a competitor spans multiple rows, name the primary
one and note the secondary in the following row's threat sentence. When no focus is provided,
omit the Map Position column entirely.

Add one sentence per competitor explaining threat level relative to inertia and Map Position context.

Verify at least one major competitor claim via WebSearch. Cite inline.

PHASE 4 — FINDINGS (Structural Requirement 4):

1. DUAL-AXIS WHITESPACE (both lines required when focus is provided):
   Competitive gap: No named competitor owns [X] because [reason]. Name which competitors
     come closest and which Map Position cells they occupy.
   Focus gap: Phase 1 row [Y — use exact Phase 1 row label from table] is unaddressed /
     unoccupied because [reason]. Reference Phase 1 table data.
   Combined: [the position simultaneously [X] and [Y] — where a new entrant faces neither
     a dominant named competitor nor inertia's strongest foothold. Ground in Map Position values].
   FAILS: Single-axis whitespace only; two separate paragraphs; "Focus gap:" label absent;
     combined statement not grounded in Phase 1 row labels or Map Position column values.
   PASS: One paragraph with "Competitive gap:" and "Focus gap:" both labeled, both grounded,
     combined statement naming the dual-axis position explicitly.

2. TABLE STAKES — minimum requirements to be taken seriously over the WORKAROUND SATISFACTION
   substitute named in Phase 2. Reference at least one Phase 1 data point per item.

3. COMPETITIVE MATRIX — already in Phase 3. Highlight top 3 by threat level with one
   recommendation sentence each, sorted high to low.

Before submitting: verify all four Structural Requirements are met. Check each Phase 2 slot
against the portability test. Confirm Phase 3 Map Position column has no empty or paraphrased cells.

AMEND: Exactly 3 items. Input change + output change. Specific.

Write artifact: simulations/discover/competitors/{topic}-competitors-alt-{date}.md
Frontmatter: skill, topic, date, skill_version, input, focus.
```

---

## V-02 — Explicit C-17 as Structural Requirement (C-17)

**Axis:** Checklist scope expansion — C-17 named as SR #5
**Hypothesis:** R3 V-03 established that naming structural requirements as observable format
failures in a numbered checklist before execution changes model behavior independently of
phase-level mechanisms. The C-14 jump (V-02→V-03 in R3) came entirely from the declaration,
not from changing individual phase instructions. V-02 extends this pattern: if C-14 compliance
was driven by explicitly naming C-11/C-12/C-13 as format requirements, C-17 compliance should
follow the same mechanism when C-17 itself is explicitly named as SR #5 — "all three structural
constraints use the same enforcement apparatus." The hypothesis is that naming the meta-property
(enforcement symmetry) in the checklist propagates the meta-property into the output, same as
naming each individual requirement propagated each individual constraint. If V-02 achieves C-17
where R3 V-05 does not add the explicit C-17 naming, it confirms that declarative completeness
in the SR block is the generative mechanism for compliance.

```
SETUP: Auto-detect product domain from README, CLAUDE.md, package.json, Glob. Do not prompt.

STRUCTURAL REQUIREMENTS — hard format constraints. Any one absent is an observable format
failure, not a quality gap. Confirm all five before submitting output:

  [ ] 1. PHASE 1 pre-map table present and fully populated before any competitor entry.
         Required when focus is provided. Absent or partially populated table fails.

  [ ] 2. PHASE 2 inertia: all three slots (WORKAROUND SATISFACTION, SWITCHING COST, HABIT
         LOCK-IN) populated with domain-exclusive content. Generic restatements fail.

  [ ] 3. PHASE 3 competitor table: Map Position column populated for every row including
         inertia. Empty cells and paraphrased Phase 1 row labels fail.

  [ ] 4. PHASE 4 whitespace: both Competitive gap line and Focus gap line in one paragraph.
         Required when focus is provided. Single-axis observation fails.

  [ ] 5. ENFORCEMENT SYMMETRY: SR1 (PHASE 1) enforces via table schema with a format-failure
         declaration; SR2 (PHASE 2) enforces via three labeled mandatory slots with named
         rejection criteria; SR4 (PHASE 4) enforces via dual-line template with both lines
         declared mandatory. All three use the same apparatus: a named format artifact plus
         a format-failure declaration. A constraint enforced only by prose instruction —
         without a named schema, labeled slots, or a dual-line template — fails this requirement.
         Required when focus is provided.

Structural Requirements 1, 3, 4, and 5 apply only when focus is provided.

PORTABILITY TEST (apply to every PHASE 2 slot before accepting it):
"If I copied this slot content unchanged into a competitor analysis for a clearly different
product — payroll software, a photo editor, a scheduling tool — would it still make sense?"
If yes, the content is too generic. Rewrite until it is recognizably wrong for any other
product category. Specific tool names, workflow steps, artifact names, and process details
anchor content to the domain; abstract mechanism names do not.

PHASE 1 — FOCUS LENS PRE-MAP (Structural Requirement 1; table schema required):

If focus = market:
| Segment | Size Estimate | Growth Stage | Current Leader |
|---------|--------------|--------------|----------------|
3-5 rows. Fill all columns. Growth stage: emerging / growth / mature.
Current leader: the named competitor or default behavior most dominant in this segment.
This is the competitive frame. Every competitor including inertia maps to exactly one row.

If focus = positioning:
| Positioning Category | Current Owner(s) | Vacancy Status |
|---------------------|-----------------|----------------|
3-5 rows. Fill all columns. Vacancy: open / contested / owned.
This is the competitive frame. Every competitor including inertia maps to exactly one row.

If no focus: skip Phase 1. SR1, SR3, SR4, and SR5 are not applicable.

PHASE 2 — INERTIA FIRST (Structural Requirement 2; labeled mandatory slots required):

Competitor 0: "None / status quo." Threat level: HIGH. State explicitly.
If Phase 1 was completed: record Phase 1 row in the Phase 3 table below.

WORKAROUND SATISFACTION: [the specific tool, template, or process teams use instead of a
dedicated solution in this domain; why it satisfies enough need that teams feel no pain]

SWITCHING COST: [the concrete cost — the specific format, role, process, or contract a team
must lose or redo when they adopt something new; quantify if possible]

HABIT LOCK-IN: [the specific repeated behavior — the artifact, ritual, or routine — that
makes the workaround feel normal in this product context; named as it exists in this workflow]

Each slot requires domain-exclusive content. Portability test applied per slot.
Generic restatements ("teams use workarounds," "switching has a cost," "habits form") fail.

Use WebSearch if needed. Cite inline.

PHASE 3 — COMPETITOR TABLE (Structural Requirement 3; Map Position column required):

| # | Competitor | Threat | Overlap | Map Position |
|---|------------|--------|---------|--------------|
| 0 | None / status quo | HIGH | — | [exact Phase 1 row label] |
| 1 | [name] | H/M/L | H/M/L | [exact Phase 1 row label] |
| 2 | [name] | H/M/L | H/M/L | [exact Phase 1 row label] |
...

Map Position: the exact Phase 1 row label this competitor primarily occupies or contests.
Use Phase 1 row labels verbatim — do not paraphrase. An empty cell or paraphrased label fails.
Add one sentence per competitor on threat relative to inertia and Map Position context.
When no focus is provided, omit the Map Position column.

Verify at least one major competitor claim via WebSearch. Cite inline.

PHASE 4 — FINDINGS (Structural Requirement 4; dual-line template required when focus is provided):

1. DUAL-AXIS WHITESPACE (both lines required; both labels mandatory):
   Competitive gap: No named competitor owns [X] because [reason]. Name which competitors
     come closest and which Map Position cells they occupy.
   Focus gap: Phase 1 row [Y — use exact Phase 1 row label from table] is unaddressed /
     unoccupied because [reason]. Reference Phase 1 table data.
   Combined: [the position simultaneously [X] and [Y] — where a new entrant faces neither
     a dominant named competitor nor inertia's strongest foothold from Phase 2. Ground in
     named Map Position column values from Phase 3].
   Both lines in one paragraph. Do not split into separate observations.

2. TABLE STAKES — minimum requirements to be taken seriously over the WORKAROUND SATISFACTION
   substitute named in Phase 2. Reference at least one Phase 1 data point per item.

3. COMPETITIVE MATRIX — top 3 by threat level, one recommendation sentence each, sorted high to low.

Before submitting: verify all five Structural Requirements are met. Check each Phase 2 slot
against the portability test. Confirm Phase 3 Map Position column has no empty or paraphrased cells.
Verify SR5 explicitly: does SR1 (PHASE 1) use a table schema with a failure declaration? Does SR2
(PHASE 2) use three labeled slots with named rejection criteria? Does SR4 (PHASE 4) use a dual-line
template with both lines declared mandatory? Any prose-only enforcement of any constraint fails SR5.

AMEND: Exactly 3 items. Input change + output change. Specific.

Write artifact: simulations/discover/competitors/{topic}-competitors-alt-{date}.md
Frontmatter: skill, topic, date, skill_version, input, focus.
```

---

## V-03 — All-Table Structural Apparatus (C-17)

**Axis:** Structural mechanism uniformity via uniform table schema for all three constraints
**Hypothesis:** C-17 requires that all three constraints use "a table schema, labeled mandatory
slots, or dual-line template" — one of three apparatus types. R3 V-05 used mixed apparatus: C-11
got a table schema, C-13 got labeled slots, C-12 got a dual-line template. V-03 tests whether
converting all three to a single apparatus type — table schema — achieves C-17 with greater
enforcement surface than the mixed approach. C-13 becomes a 3-row mechanism table (one row per
mechanism); C-12 becomes a 2-row whitespace table (one row per axis). All three constraints then
render as tables in the output, creating structural symmetry through apparatus uniformity rather
than through meta-declaration or rejection pairs. An empty table cell is visible in rendered
markdown regardless of which table it appears in — the enforcement surface is identical across
all three. The hypothesis is that uniformity of apparatus type is a sufficient condition for
C-17 pass and may produce higher compliance than mixed apparatus because the model applies the
same format pattern repeatedly rather than switching between three different enforcement formats.

```
SETUP: Auto-detect product domain from README, CLAUDE.md, package.json, Glob. Do not prompt.

STRUCTURAL REQUIREMENTS — hard format constraints. All three primary structural requirements
(SR1, SR2, SR4) enforce via table schema. An absent table or empty table cell is an observable
format failure. Confirm all four before submitting output:

  [ ] 1. PHASE 1 pre-map table present and fully populated before any competitor entry.
         Required when focus is provided.
  [ ] 2. PHASE 2 inertia mechanism table present with all three rows populated with
         domain-exclusive content. An empty row or generic row content fails.
  [ ] 3. PHASE 3 competitor table: Map Position column populated for every row including
         inertia. Empty cells and paraphrased Phase 1 row labels fail.
  [ ] 4. PHASE 4 whitespace table present with both rows populated. Required when focus is
         provided. A missing row or single-axis table fails.

Structural Requirements 1, 3, and 4 apply only when focus is provided.

PORTABILITY TEST (apply to every PHASE 2 mechanism row before accepting it):
"If I copied this row content unchanged into a competitor analysis for a clearly different
product — payroll software, a photo editor, a scheduling tool — would it still make sense?"
If yes, the content is too generic. Rewrite until recognizably wrong for any other product
category. Specific tool names, workflow steps, artifact names, and process details anchor
content to the domain; abstract mechanism names do not.

PHASE 1 — FOCUS LENS PRE-MAP (Structural Requirement 1; table schema required):

If focus = market:
| Segment | Size Estimate | Growth Stage | Current Leader |
|---------|--------------|--------------|----------------|
3-5 rows. Fill all columns. Growth stage: emerging / growth / mature.
Current leader: the named competitor or default behavior most dominant in this segment.
This is the competitive frame. Every competitor including inertia maps to exactly one row.

If focus = positioning:
| Positioning Category | Current Owner(s) | Vacancy Status |
|---------------------|-----------------|----------------|
3-5 rows. Fill all columns. Vacancy: open / contested / owned.
This is the competitive frame. Every competitor including inertia maps to exactly one row.

If no focus: skip Phase 1.

PHASE 2 — INERTIA FIRST (Structural Requirement 2; mechanism table required):

Competitor 0: "None / status quo." Threat level: HIGH. State explicitly.
If Phase 1 was completed: record Phase 1 row in the Phase 3 table below.

| Mechanism | Domain-Exclusive Content |
|-----------|--------------------------|
| WORKAROUND SATISFACTION | [the specific tool, template, script, or duct-taped combination of tools teams use instead of a dedicated solution; why it satisfies enough need that teams feel no pain and do not seek alternatives] |
| SWITCHING COST | [the concrete cost: the specific format, role, process, or contract a team must lose or redo when adopting something new; quantify if possible — hours, days, FTE cycles, budget range] |
| HABIT LOCK-IN | [the specific repeated behavior — the artifact, ritual, sprint cadence, or shared convention — that makes the workaround feel normal in this product context] |

An empty row fails. Content that passes the portability test fails (too generic). Domain-exclusive:
the content would be recognizably wrong if transplanted to a different product category. Generic
formulations ("teams face switching costs," "habit lock-in is common") fail regardless of row presence.

Use WebSearch if needed. Cite inline.

PHASE 3 — COMPETITOR TABLE (Structural Requirement 3; Map Position column required):

| # | Competitor | Threat | Overlap | Map Position |
|---|------------|--------|---------|--------------|
| 0 | None / status quo | HIGH | — | [exact Phase 1 row label] |
| 1 | [name] | H/M/L | H/M/L | [exact Phase 1 row label] |
| 2 | [name] | H/M/L | H/M/L | [exact Phase 1 row label] |
...

Map Position: the exact Phase 1 row label this competitor primarily occupies or contests.
Use Phase 1 row labels verbatim — do not paraphrase or generalize. An empty cell or paraphrased
label is a format failure. If a competitor spans multiple rows, name the primary one and note the
secondary in the following row's threat sentence. When no focus is provided, omit Map Position column.

Add one sentence per competitor on threat level relative to inertia and Map Position context.

Verify at least one major competitor claim via WebSearch. Cite inline.

PHASE 4 — FINDINGS (Structural Requirement 4; whitespace table required when focus is provided):

1. DUAL-AXIS WHITESPACE TABLE:

| Axis | Finding |
|------|---------|
| Competitive gap | No named competitor owns [X] because [reason]. Name which competitors come closest and which Map Position cells they occupy. |
| Focus gap | Phase 1 row [Y — use exact row label from Phase 1 table] is unaddressed / unoccupied because [reason]. Reference Phase 1 table data (size, growth stage, or vacancy status). |

Combined (one paragraph below the table): the position that is simultaneously [X] (competitive
gap) and [Y] (focus gap) — where a new entrant faces neither a dominant named competitor nor
inertia's strongest foothold from Phase 2. Ground in named Map Position column values from Phase 3.

2. TABLE STAKES — minimum requirements to be taken seriously over the WORKAROUND SATISFACTION
   row in the Phase 2 mechanism table. Reference at least one Phase 1 data point per item.

3. COMPETITIVE MATRIX — already in Phase 3. Highlight top 3 by threat level with one
   recommendation sentence each, sorted high to low.

Before submitting: verify all four Structural Requirements are met. Each of SR1, SR2, and SR4 must
be a populated table — not a prose block. SR1 table must precede Phase 2. SR2 mechanism table must
have all three rows filled. SR4 whitespace table must have both rows filled. Confirm Phase 3 Map
Position column has no empty or paraphrased cells. Check every Phase 2 mechanism row against the
portability test.

AMEND: Exactly 3 items. Input change + output change. Specific.

Write artifact: simulations/discover/competitors/{topic}-competitors-alt-{date}.md
Frontmatter: skill, topic, date, skill_version, input, focus.
```

---

## V-04 — Explicit C-17 + Symmetric FAILS/PASS Pairs (C-17)

**Axes:** Checklist scope expansion (V-02) + rejection example format symmetry (V-01)
**Hypothesis:** V-02 explicitly names C-17 as SR #5 (enforcement symmetry as a format
requirement). V-01 adds symmetric FAILS/PASS rejection pairs to each constraint (identical
enforcement fingerprint per constraint). Together they test whether the declaration mechanism
and the format mechanism are independently necessary, redundant, or synergistic. If V-02 alone
achieves C-17 via the SR #5 declaration, the FAILS/PASS pairs are redundant scaffolding. If
V-01 alone achieves C-17 via rejection pair symmetry, the explicit declaration is decorative.
If neither alone achieves C-17 but their combination does, both mechanisms are load-bearing and
the combination is the generative structure. V-04 is a cleaner test of load-bearing status than
V-05 because it excludes the all-table apparatus from V-03 — any V-04 success isolates the
declaration+pairs combination rather than the apparatus type.

```
SETUP: Auto-detect product domain from README, CLAUDE.md, package.json, Glob. Do not prompt.

STRUCTURAL REQUIREMENTS — hard format constraints. All constraints enforce via the same
apparatus: named format artifact + format-failure declaration + FAILS/PASS rejection example pair.
Any one absent or failing is an observable format failure. Confirm all five before submitting:

  [ ] 1. PHASE 1 pre-map table present and fully populated before any competitor entry.
         Required when focus is provided.
         FAILS: Prose paragraph; absent table; table with empty cells.
         PASS: Markdown table, named schema, all cells populated, placed before Phase 2 begins.

  [ ] 2. PHASE 2 inertia: all three slots (WORKAROUND SATISFACTION, SWITCHING COST, HABIT
         LOCK-IN) populated with domain-exclusive content.
         FAILS: Any slot containing content that reads correctly for a clearly different product —
           payroll software, a photo editor, or a scheduling tool.
         PASS: Every slot names a specific tool, workflow step, artifact, or ritual recognizably
           wrong for any other product category.

  [ ] 3. PHASE 3 competitor table: Map Position column populated for every row including
         inertia. Exact Phase 1 row labels only.
         FAILS: Empty Map Position cell; paraphrased or generalized Phase 1 row label.
         PASS: Verbatim Phase 1 row label in every cell; no paraphrasing.

  [ ] 4. PHASE 4 whitespace finding: both Competitive gap line and Focus gap line present
         in one paragraph. Required when focus is provided.
         FAILS: Single-axis whitespace; two separate paragraphs; missing "Competitive gap:" or
           "Focus gap:" label; combined statement not grounded in Phase 1 row labels.
         PASS: One paragraph with both labels present, both grounded, combined statement naming
           the dual-axis position explicitly.

  [ ] 5. ENFORCEMENT SYMMETRY: SR1 (C-11), SR2 (C-13), and SR4 (C-12) each show the same
         enforcement fingerprint — a named format artifact (table schema / labeled slots /
         dual-line template) plus a format-failure declaration plus a FAILS/PASS rejection
         example pair. No constraint enforces via prose instruction alone.
         FAILS: Any of the three lacks a named schema, labeled slots, or a dual-line template;
           or lacks a format-failure declaration; or lacks a FAILS/PASS rejection example pair.
         PASS: C-11, C-12, and C-13 each carry an identical three-component fingerprint.

Structural Requirements 1, 3, 4, and 5 apply only when focus is provided.

PORTABILITY TEST (apply to every PHASE 2 slot before accepting it):
"If I copied this slot content unchanged into a competitor analysis for a clearly different
product — payroll software, a photo editor, a scheduling tool — would it still make sense?"
If yes, the content is too generic. Rewrite until it is recognizably wrong for any other
product category. Specific tool names, workflow steps, artifact names, and process details
anchor content to the domain; abstract mechanism names do not.

PHASE 1 — FOCUS LENS PRE-MAP (Structural Requirement 1):

If focus = market:
| Segment | Size Estimate | Growth Stage | Current Leader |
|---------|--------------|--------------|----------------|
3-5 rows. Fill all columns. Growth stage: emerging / growth / mature.
Current leader: the named competitor or default behavior most dominant in this segment.
This is the competitive frame. Every competitor including inertia maps to exactly one row.

If focus = positioning:
| Positioning Category | Current Owner(s) | Vacancy Status |
|---------------------|-----------------|----------------|
3-5 rows. Fill all columns. Vacancy: open / contested / owned.
This is the competitive frame. Every competitor including inertia maps to exactly one row.

If no focus: skip Phase 1. SR1, SR3, SR4, and SR5 are not applicable.

PHASE 2 — INERTIA FIRST (Structural Requirement 2; all three slots mandatory):

Competitor 0: "None / status quo." Threat level: HIGH. State explicitly.
If Phase 1 was completed: record Phase 1 row in the Phase 3 table below.

WORKAROUND SATISFACTION:
Name the exact substitution — the specific tool, template, script, or duct-taped combination
of tools — that teams use instead of adopting a dedicated solution in this domain. Explain
why it satisfies enough need that teams feel no pain and do not seek alternatives.
FAILS: "Teams use workarounds" / naming a generic category (e.g., "spreadsheets") without the
  specific tool, template name, or combination unique to this product domain.
PASS: Names the exact template, combination, or step that is recognizably specific to this
  product's competitive context and fails portability for any other product.

SWITCHING COST:
Name the concrete thing a team must lose or redo when they adopt something new in this
product context. Name the specific format, role, process, or contract at stake. Quantify if
possible (hours, days, FTE cycles, budget range).
FAILS: "Switching has a cost" / "migration effort required" without specifying what migrates
  from what to what in this domain.
PASS: Names the domain-specific format or workflow that must change — detail obviously
  inapplicable in any other product category.

HABIT LOCK-IN:
Name the specific repeated behavior — the daily check, the weekly template, the sprint
artifact, the shared convention, the team ritual — that makes the workaround feel normal
in this product context. It does not need to be a conscious decision; it needs to be repeated.
FAILS: "Teams develop habits around their tools" / abstract habit description without naming
  the specific behavior as it exists in this product's workflow.
PASS: Names the habit — artifact, ritual, or routine — that would be recognizably wrong for
  any other domain.

Portability test applied to each slot. Use WebSearch if needed. Cite inline.

PHASE 3 — COMPETITOR TABLE (Structural Requirement 3; Map Position column required):

| # | Competitor | Threat | Overlap | Map Position |
|---|------------|--------|---------|--------------|
| 0 | None / status quo | HIGH | — | [exact Phase 1 row label] |
| 1 | [name] | H/M/L | H/M/L | [exact Phase 1 row label] |
| 2 | [name] | H/M/L | H/M/L | [exact Phase 1 row label] |
...

Map Position: the exact Phase 1 row label this competitor primarily occupies or contests.
Use Phase 1 row labels verbatim — do not paraphrase or generalize. An empty cell or paraphrased
label is a format failure. If a competitor spans multiple rows, name the primary one and note the
secondary in the following row's threat sentence. When no focus is provided, omit Map Position column.

Add one sentence per competitor on threat level relative to inertia and Map Position context.

Verify at least one major competitor claim via WebSearch. Cite inline.

PHASE 4 — FINDINGS (Structural Requirement 4; dual-line template required when focus is provided):

1. DUAL-AXIS WHITESPACE (both lines required when focus is provided):
   Competitive gap: No named competitor owns [X] because [reason]. Name which competitors
     come closest and which Map Position cells they occupy.
   Focus gap: Phase 1 row [Y — use exact Phase 1 row label from table] is unaddressed /
     unoccupied because [reason]. Reference Phase 1 table data.
   Combined: [the position simultaneously [X] and [Y] — where a new entrant faces neither
     a dominant named competitor nor inertia's strongest foothold. Ground in Map Position values].
   FAILS: Single-axis finding; two paragraphs; missing label; combined not grounded in Phase 1 data.
   PASS: One paragraph, both labels present, both grounded, combined statement explicit.

2. TABLE STAKES — minimum requirements to be taken seriously over the WORKAROUND SATISFACTION
   substitute named in Phase 2. Reference at least one Phase 1 data point per item.

3. COMPETITIVE MATRIX — top 3 by threat level, one recommendation sentence each, sorted high to low.

Before submitting: verify all five Structural Requirements are met. Check each Phase 2 slot against
the portability test. Confirm Phase 3 Map Position column has no empty or paraphrased cells.
Verify SR5: SR1 (C-11) has table schema + failure declaration + FAILS/PASS pair; SR2 (C-13) has
three labeled slots + portability test + FAILS/PASS pairs; SR4 (C-12) has dual-line template +
both lines mandatory + FAILS/PASS pair. Any prose-only enforcement of any constraint fails SR5.

AMEND: Exactly 3 items. Input change + output change. Specific.

Write artifact: simulations/discover/competitors/{topic}-competitors-alt-{date}.md
Frontmatter: skill, topic, date, skill_version, input, focus.
```

---

## V-05 — Full R4 Structural Stack (C-17)

**Axes:** R3 V-05 base + explicit C-17 as SR #5 + symmetric FAILS/PASS pairs + symmetric
verification step
**Hypothesis:** The full R4 stack adds three new R4 mechanisms to the R3 V-05 foundation
that already retroactively scores 135/135. First: explicit C-17 as SR #5 in the meta-constraint
checklist makes symmetric enforcement a named requirement rather than an emergent side effect.
Second: symmetric FAILS/PASS rejection pairs on all three constraints (C-11, C-12, C-13) make
the identical enforcement fingerprint structurally visible in the prompt itself — the model
observes identical apparatus format per constraint before producing output. Third: the
pre-submission verification step explicitly checks enforcement symmetry by name — "does SR1
use a table schema + failure declaration? does SR2 use three labeled slots + rejection pairs?
does SR4 use a dual-line template + both mandatory?" — creating a self-audit loop that mirrors
the opening SR block. Together, these mechanisms are not redundant: the declaration names the
requirement, the pairs demonstrate the pattern, the verification confirms it was applied.
Composite 135/135 is the expected result. Any failure below 135 identifies which R4 addition
is not load-bearing and should be dropped from the canonical form.

```
SETUP: Auto-detect product domain from README, CLAUDE.md, package.json, Glob. Do not prompt.

STRUCTURAL REQUIREMENTS — hard format constraints. Any one absent or failing the stated
rejection criteria is an observable format failure, not a quality gap. All constraints enforce
via the same apparatus: named format artifact + format-failure declaration + rejection example pair.
Confirm all five before submitting output:

  [ ] 1. PHASE 1 pre-map table present and fully populated before any competitor entry.
         Required when focus is provided. Partially populated table fails.
         FAILS: Prose paragraph listing segments; absent table; table with empty cells.
         PASS: Markdown table with named schema, all cells populated, present before Phase 2.

  [ ] 2. PHASE 2 inertia: all three slots (WORKAROUND SATISFACTION, SWITCHING COST, HABIT
         LOCK-IN) populated with domain-exclusive content that fails the portability test.
         FAILS: Content that reads correctly for payroll software, a photo editor, or a
           scheduling tool — regardless of whether mechanism names are present.
         PASS: Every slot names a specific tool, step, artifact, or ritual recognizably wrong
           for any other product category.

  [ ] 3. PHASE 3 competitor table: Map Position column populated for every row including
         inertia. Verbatim Phase 1 row labels only.
         FAILS: Empty Map Position cell; paraphrased or generalized Phase 1 row label.
         PASS: Exact Phase 1 row label in every cell; no paraphrasing.

  [ ] 4. PHASE 4 whitespace: both Competitive gap line and Focus gap line present in one
         paragraph. Required when focus is provided. Both labels mandatory.
         FAILS: Single-axis whitespace; two separate paragraphs; missing either label;
           combined statement not grounded in Phase 1 row labels.
         PASS: One paragraph with "Competitive gap:" and "Focus gap:" both labeled, both
           grounded in Phase 1 data and Map Position column values.

  [ ] 5. ENFORCEMENT SYMMETRY: SR1 (C-11), SR2 (C-13), and SR4 (C-12) each show the same
         three-component enforcement fingerprint: (a) named format artifact — table schema
         for SR1, labeled mandatory slots for SR2, dual-line template for SR4; (b) format-
         failure declaration — "absent table fails" / "generic restatements fail" / "single-
         axis observation fails"; (c) FAILS/PASS rejection example pair. No constraint
         enforces via prose instruction alone.
         FAILS: Any of the three lacks any one of the three components — missing format
           artifact, missing failure declaration, or missing FAILS/PASS pair.
         PASS: C-11, C-12, and C-13 each carry all three components with identical structure.

Structural Requirements 1, 3, 4, and 5 apply only when focus is provided.

PORTABILITY TEST (apply to every PHASE 2 slot before accepting it):
"If I copied this slot content unchanged into a competitor analysis for a clearly different
product — payroll software, a photo editor, a scheduling tool — would it still make sense?"
If yes, the content is too generic. Rewrite until it is recognizably wrong for any other
product category. Specific tool names, workflow steps, artifact names, and process details
anchor content to the domain; abstract mechanism names do not.

PHASE 1 — FOCUS LENS PRE-MAP (Structural Requirement 1):

If focus = market:
| Segment | Size Estimate | Growth Stage | Current Leader |
|---------|--------------|--------------|----------------|
3-5 rows. Fill all columns. Growth stage: emerging / growth / mature.
Current leader: the named competitor or default behavior most dominant in this segment.
This is the competitive frame. Every competitor including inertia maps to exactly one row.

If focus = positioning:
| Positioning Category | Current Owner(s) | Vacancy Status |
|---------------------|-----------------|----------------|
3-5 rows. Fill all columns. Vacancy: open / contested / owned.
This is the competitive frame. Every competitor including inertia maps to exactly one row.

If no focus: skip Phase 1. SR1, SR3, SR4, and SR5 are not applicable.

PHASE 2 — INERTIA FIRST (Structural Requirement 2; portability test applied to each slot):

Competitor 0: "None / status quo." Threat level: HIGH. State explicitly.
If Phase 1 was completed: record Phase 1 row in the Phase 3 table below.

WORKAROUND SATISFACTION:
Name the exact substitution — the specific tool, template, script, or duct-taped combination
of tools — that teams use instead of adopting a dedicated solution in this domain. Explain
why it satisfies enough of the need that teams feel no pain and do not seek alternatives.
FAILS: "Teams use workarounds" / naming a generic category ("spreadsheets") without the
  specific tool, template name, or combination unique to this product domain.
PASS: Names the exact template, combination, or step that is recognizably specific to this
  product's competitive context. Fails portability for any other product category.

SWITCHING COST:
Name the concrete thing a team must lose or redo when they adopt something new in this
product context. Name the specific format, role, process, or contract at stake. Quantify if
possible (hours, days, FTE cycles, budget range).
FAILS: "Switching has a cost" / "migration effort required" without specifying what migrates
  from what to what in this domain.
PASS: Names the domain-specific format or workflow at stake — detail obviously inapplicable
  in any other product category.

HABIT LOCK-IN:
Name the specific repeated behavior — the daily check, the weekly template, the sprint
artifact, the shared convention, the team ritual — that makes the workaround feel normal
in this product context. It does not need to be a conscious decision; it needs to be repeated.
FAILS: "Teams develop habits around their tools" / abstract habit description without naming
  the specific behavior as it exists in this product's workflow.
PASS: Names the habit — artifact, ritual, or routine — that would be recognizably wrong for
  any other domain and would not appear in a competitor analysis for a different product.

Use WebSearch if needed. Cite inline.

PHASE 3 — COMPETITOR TABLE (Structural Requirement 3; Map Position column required):

| # | Competitor | Threat | Overlap | Map Position |
|---|------------|--------|---------|--------------|
| 0 | None / status quo | HIGH | — | [exact Phase 1 row label] |
| 1 | [name] | H/M/L | H/M/L | [exact Phase 1 row label] |
| 2 | [name] | H/M/L | H/M/L | [exact Phase 1 row label] |
...

Map Position: the exact Phase 1 row label this competitor primarily occupies or contests.
Use Phase 1 row labels verbatim — do not paraphrase or generalize. An empty cell or a
paraphrased label is a format failure. If a competitor spans multiple rows, name the primary
one and note the secondary in the following row's threat sentence. When no focus is provided,
omit the Map Position column entirely.

Add one sentence per competitor explaining threat level relative to inertia and the Phase 1
context of their Map Position.

Verify at least one major competitor claim via WebSearch. Cite inline.

PHASE 4 — FINDINGS (Structural Requirement 4; dual-line template required when focus is provided):

1. DUAL-AXIS WHITESPACE (both lines required; both labels mandatory):
   Competitive gap: No named competitor owns [X] because [reason]. Name which competitors
     come closest and which Map Position cells they occupy.
   Focus gap: Phase 1 row [Y — use exact Phase 1 row label from table] is unaddressed /
     unoccupied because [reason]. Reference Phase 1 table data (size, growth stage, or
     vacancy status).
   Combined: [the position that is simultaneously [X] and [Y] — where a new entrant faces
     neither a dominant named competitor nor inertia's strongest foothold from Phase 2.
     Ground in named Map Position column values from Phase 3].
   FAILS: Single-axis finding; two paragraphs; missing "Competitive gap:" or "Focus gap:"
     label; combined statement not grounded in Phase 1 row labels or Map Position values.
   PASS: One paragraph with both labels present, both grounded in Phase 1 data and Map
     Position column values, combined statement naming the dual-axis position explicitly.

2. TABLE STAKES — minimum requirements to be taken seriously over the WORKAROUND SATISFACTION
   substitute named in Phase 2. Reference at least one Phase 1 data point per item.

3. COMPETITIVE MATRIX — already in Phase 3. Highlight top 3 by threat level with one
   recommendation sentence each, sorted high to low.

Before submitting: verify all five Structural Requirements are met. Check each Phase 2 slot
against the portability test. Confirm Phase 3 Map Position column has no empty or paraphrased cells.
Verify SR5 explicitly by checking each of the three constraints for all three components:
  SR1 (C-11): table schema present? format-failure declared? FAILS/PASS pair present?
  SR2 (C-13): three labeled slots present? portability test applied? FAILS/PASS pairs present?
  SR4 (C-12): dual-line template present? both lines declared mandatory? FAILS/PASS pair present?
If any component is missing from any constraint, SR5 fails — revise before submitting.

AMEND: Exactly 3 items. Input change + output change. Specific.

Write artifact: simulations/discover/competitors/{topic}-competitors-alt-{date}.md
Frontmatter: skill, topic, date, skill_version, input, focus.
```

---

## Rubric Criterion Coverage by Variation (R4)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 inertia-first | explicit | explicit | explicit | explicit | explicit |
| C-02 focus woven | pre-map + sequence | pre-map + sequence | pre-map + sequence | pre-map + sequence | pre-map + sequence |
| C-03 threat levels | explicit | explicit | explicit | explicit | explicit |
| C-04 whitespace | FAILS/PASS pair (hard) | dual-line template (hard) | 2-row table (hard) | FAILS/PASS pair (hard) | FAILS/PASS pair (hard) |
| C-05 auto-detect | SETUP | SETUP | SETUP | SETUP | SETUP |
| C-06 inertia stickiness | FAILS/PASS in slots (hard+) | labeled slots (hard) | mechanism table (hard) | FAILS/PASS in slots (hard+) | FAILS/PASS in slots (hard+) |
| C-07 web-verified | WebSearch + cite | WebSearch + cite | WebSearch + cite | WebSearch + cite | WebSearch + cite |
| C-08 AMEND (3 items) | explicit | explicit | explicit | explicit | explicit |
| C-09 cross-dimensional | strong | strong | strong | strong | strongest |
| C-10 table stakes + focus | Phase 1 data per item | Phase 1 data per item | Phase 1 data per item | Phase 1 data per item | Phase 1 data per item |
| C-11 pre-map | table schema + FAILS/PASS (hard) | table schema (hard) | table schema (hard) | table schema + FAILS/PASS (hard) | table schema + FAILS/PASS (hard) |
| C-12 dual-axis whitespace | dual-line template + FAILS/PASS (hard) | dual-line template (hard) | 2-row whitespace table (hard) | dual-line template + FAILS/PASS (hard) | dual-line template + FAILS/PASS (hard) |
| C-13 triple inertia | labeled slots + FAILS/PASS (hard+) | labeled slots (hard) | mechanism table (hard) | labeled slots + FAILS/PASS (hard+) | labeled slots + FAILS/PASS (hard+) |
| C-14 hard-stacked | meta-declaration + FAILS/PASS (hard) | meta-declaration (hard) | all-table apparatus (hard) | meta-declaration + FAILS/PASS (hard) | meta-declaration + FAILS/PASS (hard) |
| C-15 map position inline | Map Position column (hard) | Map Position column (hard) | Map Position column (hard) | Map Position column (hard) | Map Position column (hard) |
| C-16 domain-exclusive | portability test in slots (hard) | portability test in slots (hard) | portability test per row (hard) | portability test in slots (hard) | portability test in slots (hard) |
| **C-17 symmetric enforcement** | **symmetric FAILS/PASS pairs (implicit)** | **SR #5 explicit declaration (direct)** | **all-table apparatus uniformity (structural)** | **SR #5 + symmetric pairs (combined)** | **SR #5 + pairs + symmetric verification (full)** |

**Legend:** hard = format itself fails if criterion not met; hard+ = portability test operationalizes the rejection criterion; implicit = C-17 satisfied as consequence of symmetric format, not explicit declaration; direct = C-17 named and declared as SR #5; structural = apparatus uniformity rather than enforcement rigor symmetry.

---

## Recommended Test Order

1. **V-01** first — isolates symmetric FAILS/PASS pairs alone; tests whether identical format per constraint achieves C-17 as a structural consequence without explicit declaration; smallest surface change from R3 V-05
2. **V-02** second — isolates explicit SR #5 declaration alone; tests whether naming C-17 directly in the checklist propagates compliance the same way SR1-4 names propagated C-11 to C-14 in R3 V-03
3. **V-03** third — isolates all-table apparatus alone; tests whether mechanism uniformity (same schema type for all three constraints) achieves C-17 through structural consistency rather than enforcement rigor symmetry
4. **V-04** fourth — V-01 + V-02 combined; tests load-bearing status of each: are both declaration and pairs necessary, or is one redundant when the other is present?
5. **V-05** last — full R4 stack; ceiling benchmark; R3 V-05 foundation + SR5 declaration + symmetric FAILS/PASS pairs + symmetric verification; any failure below 135 identifies which R4 addition is not load-bearing
