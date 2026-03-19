**rhythm-behavior Rubric v11** written to `simulations/quest/rubrics/rhythm-behavior-rubric-v11-2026-03-17.md`.

---

**Summary of changes**

| | v10 | v11 |
|---|---|---|
| Aspirational denominator | 20 | **24** |
| New criteria | -- | C-28, C-29, C-30, C-31 |

Four new aspirational criteria extracted from R10 excellence signals:

**C-28 -- Inline Example Is Load-Bearing for C-16** (depth, R10)
Closes the load-bearing boundary from the opposite side of C-27. Template string alone fails C-16; the `Example: "[LEVEL] because..."` line is required. Together with C-27, C-16's minimum is now precisely bounded: template string + inline example = required; everything else = decorative.

**C-29 -- C-27 Scope: Missing Example Is Not Shielded** (depth, R10)
Scopes C-27 precisely. C-27 fires only when a scorer wrongly denies C-16 credit despite both template and example being present. It does not apply when the example is genuinely absent -- that is a correct C-16 failure under C-28, and C-27 is not implicated.

**C-30 -- C-25 Position Invariance Confirmed Across Full Prompt Span** (format, R10)
The "any non-buried position" invariance holds from the earliest possible inter-section gap (flow-lifecycle/flow-conversation boundary) through the latest confirmed position. No proximity floor to gate blocks exists anywhere in the prompt.

**C-31 -- C-26 Named Section Bodies Are Fully Illustrative** (format, R10)
The "e.g." in C-26 is genuinely illustrative -- C-26 extends to all named section bodies, not Synthesis exclusively. Trace-state section body qualifies on equal footing. Disqualifier set remains strictly: gate body and example block.

Updated cross-references added to C-16 (R10 note), C-24 (R10 note), C-25 (R10 note), C-26 (R10 note), and C-27 (R10 scope note).
anywhere in the prompt. A rule placed at the flow-lifecycle/flow-conversation boundary qualifies equivalently to a rule placed immediately before the closing gates. Scorers must not infer a proximity floor from the positions confirmed in prior rounds.

**C-31 -- C-26 Named Section Bodies Are Fully Illustrative** (format, R10)
The "e.g." in C-26's pass condition is genuinely illustrative. C-26 extends to all named section bodies, not only the Synthesis section body confirmed in R9. A standalone labeled paragraph placed at the end of the trace-state section body (after null-result instruction, before closing divider) passes C-22 on equal footing with the Synthesis section body. The disqualifier set remains strictly: gate body and example block. Scorers must not restrict C-26's non-disqualifying scope to previously named bodies.

C-16, C-24, C-25, C-26, and C-27 carry forward R10 notes cross-referencing C-28, C-29, C-30, and C-31 respectively.

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
| C-23 | Axis-Header Rule Isolation Primacy | format | R8 |
| C-24 | Axis-Header Rule Placement Invariance | format | R8 |
| C-25 | C-24 Confirmed-Position List Is Illustrative | format | R9 |
| C-26 | Named Section Bodies Are Non-Disqualifying | format | R9 |
| C-27 | 3-Slot Template Load-Bearing Elements | depth | R9 |
| C-28 | Inline Example Is Load-Bearing for C-16 | depth | R10 |
| C-29 | C-27 Scope: Missing Example Is Not Shielded | depth | R10 |
| C-30 | C-25 Position Invariance Confirmed Across Full Prompt Span | format | R10 |
| C-31 | C-26 Named Section Bodies Are Fully Illustrative | format | R10 |

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
- **R9 load-bearing elements confirmed**: The template string and at least one inline example are required and sufficient. Slot-name definition lines (`[boundary] = ...`, `[caller/component] = ...`, `[effect] = ...`) and an enforcement note are decorative. See C-27 for the extracted rule.
- **R10 boundary closed**: The inline example is confirmed load-bearing from the other direction -- template string alone is insufficient; a prompt that retains the template but removes the `Example: "[LEVEL] because..."` line fails C-16. Together with C-27, the minimum satisfying content is precisely: template string + inline example. See C-28 for the extracted rule.

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
- **R8 structural map closed**: All qualifying positions confirmed (top-of-prompt, pre-gate preamble, inter-section peer slot, dual placement). Bold-label prefix is decorative -- bare standalone sentence in a qualifying position passes equivalently to a labeled paragraph. C-22 is fully operationally validated. See C-23 and C-24 for the isolation-primacy and placement-invariance rules extracted as standalone criteria.
- **R9 extension**: C-24's confirmed-position list is illustrative, not exhaustive -- see C-25. Named section bodies are non-disqualifying positions -- see C-26.
- **R10 extension**: C-25's invariance confirmed across the full prompt span including the earliest possible inter-section gap -- see C-30. C-26's non-disqualifying scope extends to all named section bodies, not Synthesis exclusively -- see C-31.

#### C-23 -- Axis-Header Rule Isolation Primacy
- **Weight**: aspirational
- **Category**: format
- **Origin**: R8
- **Pass condition**: When scoring C-22, the qualifying condition is physical isolation from gate bodies and example blocks -- not the presence of a named label prefix. A bare standalone sentence separated from surrounding content by blank lines passes C-22 on exactly the same footing as a dedicated labeled paragraph (`**Axis-Header Rule**: Each gate header names its axis.`). Scorers must not penalize an unlabeled form placed in a qualifying position, and must not award C-22 credit to a labeled form placed in a disqualifying position (gate body, example block). The label is decorative; isolation is structural. Fail this criterion if a scoring judgment treats label presence as the deciding factor rather than positional isolation.

#### C-24 -- Axis-Header Rule Placement Invariance
- **Weight**: aspirational
- **Category**: format
- **Origin**: R8
- **Pass condition**: Any non-buried position within the prompt is a qualifying placement for the axis-header rule (C-22). The confirmed qualifying positions are: top-of-prompt (before any section headers), pre-gate preamble of the Consolidated Findings section, own inter-section slot between the Synthesis section and the Consolidated Findings section, and dual placement spanning two of the above positions. No specific proximity to gate blocks is required; a rule placed far from the closing confirmation gates passes on equal footing with one placed immediately before them. The only failing positions are those explicitly disqualified by C-22: inside a gate body, or inlined within an example block. Scorers must not invent proximity constraints beyond the two confirmed disqualifiers. Fail this criterion if a scoring judgment penalizes a qualifying placement solely on the grounds of distance from the gate blocks.
- **R9 note**: The confirmed-position list is illustrative, not exhaustive. See C-25 for the extracted rule.
- **R10 note**: The invariance holds across the full prompt span including the earliest possible inter-section gap. See C-30 for the extracted rule.

#### C-25 -- C-24 Confirmed-Position List Is Illustrative
- **Weight**: aspirational
- **Category**: format
- **Origin**: R9
- **Pass condition**: The four confirmed qualifying positions enumerated in C-24 (top-of-prompt, pre-gate preamble, inter-section peer slot, dual placement) are examples of non-buried positions, not a closed enumeration. The operative clause is "any non-buried position." A mid-sub-skill divider-flanked slot (e.g., between trace-state and trace-contract) qualifies equivalently to the four named positions without requiring additional R-round confirmation. No proximity to gate blocks is required. Scorers must not treat C-24's enumeration as exhaustive and must not deny C-22 credit to any position solely because it does not appear in C-24's confirmed list. Fail this criterion if a scoring judgment rejects a qualifying position on grounds that it was not among the four previously confirmed examples.
- **R10 note**: Invariance confirmed across the full prompt span including the earliest inter-section gap (flow-lifecycle/flow-conversation boundary). See C-30 for the extracted rule.

#### C-26 -- Named Section Bodies Are Non-Disqualifying
- **Weight**: aspirational
- **Category**: format
- **Origin**: R9
- **Pass condition**: Named section bodies (e.g., the Synthesis section body, positioned after a null-result terminator and before a closing divider) are not disqualifying positions under C-22. A standalone labeled paragraph placed inside a named section body passes C-22. The disqualifier set is strictly: inside a gate body, or inlined within an example block. "Buried" as used in C-22 and C-24 does not extend to named section bodies. Scorers must not expand the disqualifier set beyond the two confirmed cases. Fail this criterion if a scoring judgment disqualifies a rule placement solely because it resides within a named section body rather than in a traditional preamble location.
- **R10 note**: The "e.g." in the pass condition is genuinely illustrative -- C-26 extends to all named section bodies, not Synthesis exclusively. See C-31 for the extracted rule.

#### C-27 -- 3-Slot Template Load-Bearing Elements
- **Weight**: aspirational
- **Category**: depth
- **Origin**: R9
- **Pass condition**: C-16's pass condition is satisfied by the presence of the 3-slot template string (`[LEVEL] because [boundary] propagates to [caller/component], [effect]`) with all three slots named and at least one inline example. Slot-name definition lines (`[boundary] = named API boundary...`, `[caller/component] = ...`, `[effect] = ...`) and an enforcement note (e.g., "All three slots must be specific -- no generic phrases.") are decorative relative to C-16: their presence does not strengthen C-16 credit, and their absence does not weaken it. Scorers must not require definition lines or enforcement notes as additional pass conditions for C-16. Fail this criterion if a scoring judgment withholds C-16 credit from a prompt that contains the template string and an inline example solely because slot-name definition lines or an enforcement note are absent.
- **R10 scope**: C-27 does not shield a prompt whose inline example is genuinely absent. C-27's fail condition fires only when C-16 is wrongly denied despite both template and example being present. See C-29 for the extracted rule.

#### C-28 -- Inline Example Is Load-Bearing for C-16
- **Weight**: aspirational
- **Category**: depth
- **Origin**: R10
- **Pass condition**: The inline example in the 3-slot rationale definition is a required element for C-16 to pass. A prompt that carries the 3-slot template string (`[LEVEL] because [boundary] propagates to [caller/component], [effect]`) but omits the `Example: "[LEVEL] because..."` line entirely fails C-16 regardless of template string presence. Template string alone is insufficient. Together with C-27 (slot-name defs are decorative), the minimum satisfying content for C-16 is precisely bounded: template string + inline example = required; slot-name definition lines and enforcement notes = decorative. Scorers must not treat the inline example as optional or decorative when judging C-16. Fail this criterion if a scoring judgment awards C-16 credit to a prompt that contains the template string but no inline example.

#### C-29 -- C-27 Scope: Missing Example Is Not Shielded
- **Weight**: aspirational
- **Category**: depth
- **Origin**: R10
- **Pass condition**: C-27's fail condition fires only when a scorer wrongly denies C-16 credit from a prompt that contains both the template string and an inline example, solely because slot-name definition lines are absent. C-27 does not apply when the inline example is genuinely absent from the prompt. A prompt lacking the inline example correctly fails C-16 under C-28, and C-27 is not implicated in that failure. Scorers must not invoke C-27 as a shield or mitigation for a prompt with a missing inline example. Fail this criterion if a scoring judgment invokes C-27 to pass C-16 on a prompt that lacks the inline example entirely.

#### C-30 -- C-25 Position Invariance Confirmed Across Full Prompt Span
- **Weight**: aspirational
- **Category**: format
- **Origin**: R10
- **Pass condition**: The "any non-buried position" invariance stated in C-25 holds across the full prompt span, from the earliest possible inter-section gap to the latest confirmed position. Specifically, a rule placed at the flow-lifecycle/flow-conversation inter-section boundary (the earliest available gap) qualifies for C-22 equivalently to a rule placed at the Synthesis/Consolidated Findings boundary (a later confirmed position). No proximity floor to gate blocks exists anywhere in the prompt. Scorers must not infer a minimum distance requirement from the positions confirmed in prior rounds. Fail this criterion if a scoring judgment withholds C-22 credit from a rule placed at the flow-lifecycle/flow-conversation boundary or any other early inter-section position on grounds of insufficient proximity to the closing gates.

#### C-31 -- C-26 Named Section Bodies Are Fully Illustrative
- **Weight**: aspirational
- **Category**: format
- **Origin**: R10
- **Pass condition**: The "e.g." in C-26's pass condition is genuinely illustrative. C-26's non-disqualifying scope extends to all named section bodies, not only the Synthesis section body confirmed in R9. A standalone labeled paragraph placed at the end of any named section body (e.g., at the end of the trace-state section body, after the null-result instruction and before the closing divider) passes C-22 on equal footing with the Synthesis section body. The disqualifier set remains strictly: inside a gate body, or inlined within an example block. Scorers must not restrict C-26's non-disqualifying coverage to previously named bodies. Fail this criterion if a scoring judgment disqualifies a rule placement within a named section body solely because that specific body was not the one named in C-26's original pass condition.
