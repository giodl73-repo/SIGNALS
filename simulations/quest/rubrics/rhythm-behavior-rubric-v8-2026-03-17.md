**rhythm-behavior Rubric — v8** written to `simulations/quest/rubrics/rhythm-behavior-rubric-v8-2026-03-17.md`.

---

**What changed and why**

| | v7 | v8 |
|---|---|---|
| Aspirational denominator | 15 | **15** |
| New criteria | — | **none** |

All three R7 patterns are **confirmatory, not generative** — same classification logic that held for R6's Pattern 1 and Pattern 2:

- **Pattern 1** (gate-body disqualifier): validates the existing "not buried inside a gate body" clause already in C-22's pass condition. The decisive factor was already named; R7 confirms it fires.
- **Pattern 2** (example-block disqualifier): validates the existing "not inlined within an example" clause. The parenthetical annotation form is exactly what that clause was written to exclude.
- **Pattern 3** (positional prefix decorative): design principle observation, third consecutive confirmation. No pass condition.

The one substantive change: **C-22's pass condition is updated** to record the two confirmed disqualifier forms from R7 (gate-body burial, example-block parenthetical annotation) and name V-04 as the confirmed production form — so future scorers have the operational evidence inline rather than only in the scorecard.
- gate-body burial and example-block annotation -- were both tested against live variations for the first time in R7 and both fired correctly. C-22 is now operationally validated. The production candidate is V-04: dedicated labeled paragraph (`**Axis-Header Rule**: Each gate header names its axis.`) at minimal prompt mass. C-22's pass condition is updated below to record the confirmed disqualifier forms.

---

## Essential Criteria

| # | Name | Category |
|---|------|----------|
| C-01 | Declared Execution Sequence | format |
| C-02 | Single Unified Report | format |
| C-03 | Blast Radius Ranking Present | correctness |
| C-04 | Spec Gap and Contract Violation Coverage | coverage |

## Recommended Criteria

| # | Name | Category |
|---|------|----------|
| C-05 | Per-Finding Sub-Skill Attribution | correctness |
| C-06 | Actionable Next Step for Top Finding | depth |
| C-07 | Sub-Skill Section Completeness | coverage |

## Aspirational Criteria

| # | Name | Category | Origin |
|---|------|----------|--------|
| C-08 | Blast Radius Justification | depth | -- |
| C-09 | Cross-Sub-Skill Synthesis | depth | -- |
| C-10 | Self-Documenting Ranking Label | format | R1 V-05 |
| C-11 | Active Coverage Confirmation | coverage | R1 V-05 |
| C-12 | At-Discovery Attribution | correctness | R1 V-05 |
| C-13 | Dedicated Synthesis Step | depth | R2 |
| C-14 | Rationale Column Enforcement | depth | R2 |
| C-15 | CROSS-SKILL Findings as First-Class Table Citizens | correctness | R2 |
| C-16 | 3-Slot Rationale Format | depth | R3 |
| C-17 | CROSS-SKILL Blast Radius Inheritance Rule | correctness | R3 |
| C-18 | Closing Confirmation Multi-Gate Enforcement | format | R3 |
| C-19 | One-Axis-Per-Gate Rule | correctness | R4 |
| C-20 | Axis-Named Repair Verb | depth | R4 |
| C-21 | Axis-Labeled Gate Header Encoding | format | R5 |
| C-22 | Explicit Axis-Header Preamble Rule | format | R6 |

---

## Criterion Definitions

### Essential Criteria

#### C-01 -- Declared Execution Sequence
- **Weight**: essential
- **Category**: format
- **Pass condition**: The output names the five sub-skills in declared order before any findings appear (flow-lifecycle -> flow-conversation -> trace-state -> trace-contract -> trace-permissions). Order and completeness must both be present.

#### C-02 -- Single Unified Report
- **Weight**: essential
- **Category**: format
- **Pass condition**: The output is one continuous document with no promise to continue in a later response. Any split across responses is an automatic fail.

#### C-03 -- Blast Radius Ranking Present
- **Weight**: essential
- **Category**: correctness
- **Pass condition**: All findings in the consolidated report are sorted by blast radius (WIDE first, NARROW last). The sort must be labeled. Findings in unsorted or unlabeled order fail this criterion.

#### C-04 -- Spec Gap and Contract Violation Coverage
- **Weight**: essential
- **Category**: coverage
- **Pass condition**: The consolidated report contains at least one finding classified as a spec gap (missing, ambiguous, or underspecified requirement) and at least one classified as a contract violation (a behavior that breaks a declared interface, pre/post condition, or permission boundary). These categories must be distinguishable by label, section, or explicit classification. Fail if all findings are of a single type or the two categories are indistinguishable.

---

### Recommended Criteria

#### C-05 -- Per-Finding Sub-Skill Attribution
- **Weight**: recommended
- **Category**: correctness
- **Pass condition**: The consolidated findings table includes a Sub-Skill column and every row names the producing sub-skill. Attribution must be structural (column present from table open) rather than retroactive (added in summary). Fail if any row omits attribution or if attribution is only present in prose.

#### C-06 -- Actionable Next Step for Top Finding
- **Weight**: recommended
- **Category**: depth
- **Pass condition**: The highest-ranked finding (first row after blast radius sort) carries a concrete, specific next step that a developer can execute before writing the first line of implementation code. The step must name an exact spec section, boundary, or component -- not a generic directive such as "clarify the spec" or "add a test."

#### C-07 -- Sub-Skill Section Completeness
- **Weight**: recommended
- **Category**: coverage
- **Pass condition**: Each of the five sub-skill sections includes an explicit null-result statement when no findings are produced (e.g., "no findings," "PHASE: no findings"). Sections that are silently absent or that trail off without a null-result statement fail this criterion.

---

### Aspirational Criteria

#### C-08 -- Blast Radius Justification
- **Weight**: aspirational
- **Category**: depth
- **Pass condition**: The consolidated findings table includes a Blast Radius Rationale column and every row carries a non-empty rationale. Generic phrases (e.g., "affects many components," "broad impact") fail; every cell must name a specific element from the topic under review.

#### C-09 -- Cross-Sub-Skill Synthesis
- **Weight**: aspirational
- **Category**: depth
- **Pass condition**: The output contains a dedicated SYNTHESIS section with a CROSS-SKILL label. The section identifies at least one finding that spans two or more sub-skills and inserts it into the findings table with Sub-Skill = CROSS-SKILL.

#### C-10 -- Self-Documenting Ranking Label
- **Weight**: aspirational
- **Category**: format
- **Origin**: R1 V-05
- **Pass condition**: The blast radius sort is labeled with the explicit string "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW" (or equivalent arrow notation) structurally adjacent to the sorted table -- not only in a preamble or legend.

#### C-11 -- Active Coverage Confirmation
- **Weight**: aspirational
- **Category**: coverage
- **Origin**: R1 V-05
- **Pass condition**: The closing confirmation includes a gate that checks for the presence of at least one spec-gap finding and at least one contract-violation finding, and fires a correction loop (instructs the model to go back and find the missing category) if either is absent.

#### C-12 -- At-Discovery Attribution
- **Weight**: aspirational
- **Category**: correctness
- **Origin**: R1 V-05
- **Pass condition**: The findings table is opened (with all columns present) before the first sub-skill runs, and rows are appended as findings are discovered during each sub-skill section. Attribution must happen at discovery time -- not assembled retroactively in a final summary step.

#### C-13 -- Dedicated Synthesis Step
- **Weight**: aspirational
- **Category**: depth
- **Origin**: R2
- **Pass condition**: The SYNTHESIS section is structurally isolated between the trace-permissions section and the Consolidated Findings section. It is not embedded inside a sub-skill section or appended to the end of the report.

#### C-14 -- Rationale Column Enforcement
- **Weight**: aspirational
- **Category**: depth
- **Origin**: R2
- **Pass condition**: The findings table pre-opens with a Blast Radius Rationale column before any sub-skill runs. An empty cell is structurally visible as an omission. Fail if the column is added retroactively or omitted from the table definition.

#### C-15 -- CROSS-SKILL Findings as First-Class Table Citizens
- **Weight**: aspirational
- **Category**: correctness
- **Origin**: R2
- **Pass condition**: Every CROSS-SKILL finding produced in the SYNTHESIS section is inserted into the main findings table with Sub-Skill = CROSS-SKILL. The coverage summary includes a CROSS-SKILL row. CROSS-SKILL findings that appear only in prose or only in the SYNTHESIS section fail this criterion.

#### C-16 -- 3-Slot Rationale Format
- **Weight**: aspirational
- **Category**: depth
- **Origin**: R3
- **Pass condition**: The prompt declares the rationale format `[LEVEL] because [boundary] propagates to [caller/component], [effect]` with all three slots named and at least one inline example. The format must be enforced at two sites: in the "What to look for" section and in the closing confirmation (Gate 2 or equivalent axis). A rationale column mandate without the 3-slot template fails this criterion.

#### C-17 -- CROSS-SKILL Blast Radius Inheritance Rule
- **Weight**: aspirational
- **Category**: correctness
- **Origin**: R3
- **Pass condition**: The SYNTHESIS section declares that a CROSS-SKILL finding's blast radius must be greater than or equal to the maximum blast radius of its contributing sub-skill findings. No downgrade from the highest contributor is permitted. The CROSS-SKILL rationale cell must carry a provenance annotation in the form "Inherited [LEVEL] from [sub-skill] ([F-ID])." The closing confirmation enforces this with an independent correction loop.

#### C-18 -- Closing Confirmation Multi-Gate Enforcement
- **Weight**: aspirational
- **Category**: format
- **Origin**: R3
- **Pass condition**: The closing confirmation contains exactly three gates, each covering one axis: (1) coverage -- at least one spec-gap and one contract-violation finding present; (2) rationale format -- every rationale cell uses the 3-slot format; (3) inheritance -- every CROSS-SKILL blast radius is >= max of contributors. Each gate must trigger an independent correction loop on failure. Fail if fewer than three gates are present or if any gate is compound (absorbing two axes under one correction instruction).

#### C-19 -- One-Axis-Per-Gate Rule
- **Weight**: aspirational
- **Category**: correctness
- **Origin**: R4
- **Pass condition**: Each closing confirmation gate covers exactly one axis. A compound gate that absorbs two axes (e.g., rationale format + inheritance) under a single correction instruction counts as one gate, not two, regardless of how the block is labeled or structured. Pass requires three gates with one axis each. Fail if any gate's correction instruction is written so that a single trigger fires a repair that spans two distinct axes.

#### C-20 -- Axis-Named Repair Verb
- **Weight**: aspirational
- **Category**: depth
- **Origin**: R4
- **Pass condition**: Each closing confirmation gate uses a repair verb that explicitly names its axis target -- not a generic directive. Examples of passing repair verbs: "add at least one [spec-gap / contract-violation] finding" (coverage axis), "rewrite every rationale cell using the [LEVEL] / [boundary] / [effect] slots" (format axis), "fix the CROSS-SKILL blast radius to match the highest contributing sub-skill" (inheritance axis). Generic verbs such as "correct this," "fix the section," or "revise as needed" that do not name the axis fail this criterion.

#### C-21 -- Axis-Labeled Gate Header Encoding
- **Weight**: aspirational
- **Category**: format
- **Origin**: R5
- **Pass condition**: Each closing confirmation gate carries a header that names its axis (e.g., "Coverage Axis Gate," "Format Axis Gate," "Inheritance Axis Gate"). The axis label must appear in the header token itself -- not only in the repair verb or the body of the correction instruction, and not only in a parenthetical within the gate body (e.g., "(coverage axis)" in the body does not satisfy this criterion). Pass on this criterion makes C-19 structurally self-enforcing: two headers cannot share the same axis label, so the one-axis-per-gate constraint is visible at a glance without additional verification. Fail if any gate header omits the axis name or uses a positional label only (e.g., "Gate 1," "Check 2").

#### C-22 -- Explicit Axis-Header Preamble Rule
- **Weight**: aspirational
- **Category**: format
- **Origin**: R6
- **Pass condition**: The prompt contains a concise standalone declarative sentence that instructs all gate headers to name their axis (e.g., "Each gate header names its axis."). The rule must appear as an independent instruction in the preamble or a dedicated labeled paragraph -- not buried inside a gate body, not inlined within an example (including as a parenthetical annotation appended to an example block), and not paraphrasable only by reading a structural pattern. This declarative redundancy guards against model drift: a model that de-emphasizes structural gate encoding still has an explicit rule to observe. Fail if the axis-header constraint exists only implicitly through the gate structure, with no standalone declarative rule.
- **R7 operational validation**: Both written disqualifiers confirmed against live variations. A rule sentence inside any gate block's body fails regardless of grammatical completeness (V-01: gate-body burial). A grammatically complete rule sentence appended as parenthetical commentary to an example block fails (V-02: example-block annotation). Physical preamble location -- not grammatical form -- is the decisive factor. Production form: dedicated labeled paragraph (`**Axis-Header Rule**: Each gate header names its axis.`) confirmed as the maximally standalone form at minimal prompt mass (V-04).
