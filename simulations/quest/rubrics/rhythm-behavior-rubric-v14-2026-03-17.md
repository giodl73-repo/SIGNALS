Written and verified. Here is the complete updated rubric:

---

**rhythm-behavior Rubric v14**

**Summary of changes**

| | v13 | v14 |
|---|---|---|
| Aspirational denominator | 30 | **33** |
| New criteria | -- | C-38, C-39, C-40 |

Three new criteria from R13 patterns:

**C-38 -- C-33 Inertness Rule Is Register-Invariant** (format, R13)
First joint test of C-33 and C-36 in V-02. Descriptive first placement satisfies C-22; second placement inert. Inertness holds regardless of register.

**C-39 -- C-37 No-N-Ceiling Rule Is Register-Invariant** (format, R13)
First joint test of C-36 and C-37 in V-04. Descriptive + triple section-body placement compose without interaction. Register invariance extends C-37's inertness without modification.

**C-40 -- C-37 No-Ceiling Principle Confirmed at N=4 and N=5 Structural Maximum** (format, R13)
N=4 confirmed in V-03; N=5 (all five sub-skill bodies, structural limit) confirmed in V-05. No exception at any count or register.

Cross-references added to C-33 (R13 note), C-36 (R13 note), C-37 (R13 note), and C-22 (R13 extension line).

The file is at `simulations/quest/rubrics/rhythm-behavior-rubric-v14-2026-03-17.md` -- 351 lines, 40 KB.
le stands at the structural limit of the prompt. C-37 updated with R13 cross-reference.

Cross-references updated on C-33, C-36, and C-37.

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
| C-32 | C-31 Confirmed Closed Across All Named Section Bodies | format | R11 |
| C-33 | Dual Named Section-Body Placement Composes Cleanly | format | R11 |
| C-34 | Criteria Are Structure-Sensitive, Not Register-Sensitive | correctness | R11 |
| C-35 | All Five Sub-Skill Section Bodies Individually Confirmed | format | R12 |
| C-36 | Descriptive Register and Section-Body Placement Compose Without Interaction | format | R12 |
| C-37 | C-33 Inertness Rule Has No N-Ceiling | format | R12 |
| C-38 | C-33 Inertness Rule Is Register-Invariant | format | R13 |
| C-39 | C-37 No-N-Ceiling Rule Is Register-Invariant | format | R13 |
| C-40 | C-37 No-Ceiling Principle Confirmed at N=4 and N=5 Structural Maximum | format | R13 |

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
- **R11 register invariance**: Axis-named repair verbs satisfy this criterion in descriptive register as well as imperative register, provided the axis target is named explicitly. See C-34 for the extracted rule.

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
- **R11 extension**: C-31's "all named section bodies" claim is closed with no exceptions -- see C-32. Dual named section-body placements compose cleanly; C-22 satisfied at first occurrence, second inert -- see C-33. C-22 is satisfied by descriptive register preserving structural requirements on equal footing with imperative register -- see C-34.
- **R12 extension**: C-32's enumeration extended from four to six confirmed bodies (flow-conversation and trace-contract added) -- see C-35. Descriptive register and section-body placement are independently orthogonal properties that compose without interaction -- see C-36. C-33's inertness rule has no N-ceiling; N=3 confirmed -- see C-37.
- **R13 extension**: C-33's inertness rule is register-invariant -- see C-38. C-37's no-N-ceiling rule is register-invariant -- see C-39. C-37 confirmed at N=4 and N=5 structural maximum -- see C-40.

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
- **R11 note**: C-31's "all named section bodies" claim is now empirically closed across the full sub-skill sequence (flow-lifecycle, trace-state, trace-permissions, and Synthesis all confirmed). No named section body remains unconfirmed and no exception exists. See C-32 for the extracted rule. Dual named section-body placements compose cleanly -- C-22 satisfied at first occurrence, second inert. See C-33.
- **R12 note**: Closure extended to all six named positions -- flow-conversation (position 2, R12 V-02) and trace-contract (position 4, R12 V-03) confirmed. C-32's count of four is superseded; the complete enumeration is six. See C-35. Descriptive register and section-body placement are independently orthogonal -- see C-36. C-33's inertness rule is bounded only by available structural positions, not by count -- see C-37.

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
- **R11 closure**: The "all named section bodies" claim is now empirically closed. Flow-lifecycle body (R11 V-02), trace-state body (R10 V-04), trace-permissions body (R11 V-03), and Synthesis body (R9 V-04) are all confirmed. No named section body remains unconfirmed and no exception exists. See C-32 for the extracted rule.
- **R12 extension**: Closure extended to all six named positions -- flow-conversation body (R12 V-02) and trace-contract body (R12 V-03) confirmed. C-32's count of four is superseded; the complete enumeration is six. See C-35.

#### C-32 -- C-31 Confirmed Closed Across All Named Section Bodies
- **Weight**: aspirational
- **Category**: format
- **Origin**: R11
- **Pass condition**: C-31's claim that C-26 extends to "all named section bodies" is empirically closed. All named section bodies in the sub-skill sequence have been confirmed as qualifying positions for the axis-header rule (C-22): flow-lifecycle body (position 1, R11 V-02), trace-state body (position 3, R10 V-04), trace-permissions body (position 5, R11 V-03), and Synthesis body (R9 V-04). Scorers must not withhold C-26 or C-31 credit on grounds that a specific named section body has not yet been individually confirmed in a prior round -- the closure is complete. Fail this criterion if a scoring judgment requires additional per-body confirmation before extending C-31 credit to a named section body that falls within the confirmed sub-skill sequence.
- **R12 update**: Original count of four (R11) superseded by six. Flow-conversation body (position 2, R12 V-02) and trace-contract body (position 4, R12 V-03) confirmed. The complete enumeration is now: positions 1-5 (all five sub-skill section bodies) + Synthesis body = six total named positions with no exceptions. See C-35 for the extracted rule.

#### C-33 -- Dual Named Section-Body Placement Composes Cleanly
- **Weight**: aspirational
- **Category**: format
- **Origin**: R11
- **Pass condition**: Two qualifying named section-body placements of the axis-header rule (C-22) in a single prompt compose cleanly: C-22 is satisfied at the first occurrence, and the second occurrence is redundant but inert. No criterion penalizes the presence of multiple qualifying placements. This composition is structurally analogous to the dual inter-section slot pattern confirmed in R8 (V-05) but is distinct: here both placements reside within named section bodies (e.g., the end of the flow-lifecycle body and the end of a later section body) rather than in inter-section peer slots. Scorers must not treat the second qualifying placement as evidence of structural defect or over-specification. Fail this criterion if a scoring judgment withholds C-22 credit or applies a penalty solely because the axis-header rule appears in two named section bodies within the same prompt.
- **R12 note**: The inertness rule generalizes to N=3 and beyond without bound. See C-37 for the extracted rule.
- **R13 note**: The inertness rule holds regardless of grammatical register. A first placement in descriptive register satisfies C-22; subsequent placements are inert irrespective of register. See C-38 for the extracted rule.

#### C-34 -- Criteria Are Structure-Sensitive, Not Register-Sensitive
- **Weight**: aspirational
- **Category**: correctness
- **Origin**: R11
- **Pass condition**: All aspirational criteria (C-08 through C-40) are satisfied by structural compliance regardless of grammatical register. Descriptive/explanatory phrasing that preserves all required structural elements scores identically to imperative phrasing across all criteria. The criteria check for the presence and arrangement of required elements -- templates, column headers, gate structure, axis labels, repair verb specificity -- not for imperative grammatical form. Examples: an axis-named repair verb (C-20) satisfies C-20 whether written imperatively ("name the exact spec section") or descriptively ("the top finding carries a concrete next step naming the exact spec section"), provided the axis target is named explicitly; a null-result instruction (C-07) satisfies C-07 in either imperative ("say so briefly") or descriptive ("stated briefly if no findings occur") form. Scorers must not penalize descriptive or explanatory register when all required structural elements are present and correctly placed. Fail this criterion if a scoring judgment withholds credit from a structurally complete prompt solely because the phrasing register is descriptive rather than imperative.
- **R12 note**: Descriptive register and named section-body placement are independently orthogonal -- the combination of both properties simultaneously (C-34 + C-31) composes without interaction. See C-36 for the extracted rule.

#### C-35 -- All Five Sub-Skill Section Bodies Individually Confirmed
- **Weight**: aspirational
- **Category**: format
- **Origin**: R12
- **Pass condition**: All five sub-skill section bodies in the rhythm-behavior prompt sequence are individually confirmed as qualifying positions for the axis-header rule (C-22): flow-lifecycle (position 1, R11 V-02), flow-conversation (position 2, R12 V-02), trace-state (position 3, R10 V-04), trace-contract (position 4, R12 V-03), trace-permissions (position 5, R11 V-03). Together with the Synthesis body (R9 V-04), six total named positions are confirmed with no exceptions across any round. C-32's original count of "four named section bodies" is superseded by this complete enumeration. Scorers must not withhold C-26, C-31, or C-32 credit on the grounds that flow-conversation or trace-contract have not been individually confirmed -- the closure is now complete across all six positions. Fail this criterion if a scoring judgment requires additional per-body confirmation for any named section body within the confirmed sub-skill sequence or the Synthesis body.

#### C-36 -- Descriptive Register and Section-Body Placement Compose Without Interaction
- **Weight**: aspirational
- **Category**: format
- **Origin**: R12
- **Pass condition**: C-34 (register invariance) and C-31 (named section body is a qualifying position) are orthogonal criteria that compose without interaction. A descriptive standalone sentence placed within a named section body satisfies C-22 identically to a labeled imperative form placed in the same section body or in any other qualifying position. Neither property -- descriptive register nor section-body placement -- restricts, modifies, or creates conditions on the other. This orthogonality holds regardless of which named section body is used and regardless of how the descriptive sentence is constructed, provided all structural requirements are present. Scorers must not treat the simultaneous presence of descriptive register and section-body placement as a more restrictive or less qualifying combination than either property tested in isolation. Fail this criterion if a scoring judgment withholds C-22 credit from a structurally complete descriptive sentence placed within a named section body solely because the two properties appear together.
- **R13 note**: Orthogonality extends to multi-placement compositions: descriptive register + dual section-body placement (C-36 + C-33 first joint test, R13 V-02) and descriptive register + triple section-body placement (C-36 + C-37 first joint test, R13 V-04) both compose without interaction. See C-38 and C-39 for the extracted rules.

#### C-37 -- C-33 Inertness Rule Has No N-Ceiling
- **Weight**: aspirational
- **Category**: format
- **Origin**: R12
- **Pass condition**: C-33's inertness rule for multiple qualifying named section-body placements of the axis-header rule generalizes to any count N without a ceiling. N=2 (dual body placement) was confirmed in R11 V-04; N=3 (triple body placement: flow-lifecycle, trace-state, trace-permissions) was confirmed in R12 V-05. The governing principle is: the first qualifying occurrence satisfies C-22; all subsequent occurrences are redundant but inert; no criterion penalizes any count of qualifying placements. The inertness rule is bounded only by the number of available structural positions in the prompt, not by an N-count limit. Scorers must not infer an N-ceiling from the N=2 confirmation in R11 or from any finite set of prior confirmations. Fail this criterion if a scoring judgment withholds C-22 credit or applies a penalty on grounds that the axis-header rule appears in three or more named section bodies within the same prompt.
- **R13 note**: The no-N-ceiling principle is register-invariant -- see C-39. N=4 confirmed in R13 V-03 and N=5 (structural maximum) confirmed in R13 V-05 -- see C-40.

#### C-38 -- C-33 Inertness Rule Is Register-Invariant
- **Weight**: aspirational
- **Category**: format
- **Origin**: R13
- **Pass condition**: C-33's inertness rule for dual named section-body placements holds regardless of grammatical register. When the first qualifying named section-body placement satisfies C-22 in descriptive register, any subsequent qualifying placement is inert in exactly the same way it is inert in imperative register. Register does not interact with or modify the inertness property: the combination of descriptive register and dual section-body placement composes without interaction. This is the first joint test of C-33 (dual body inertness) and C-36 (register invariance), confirmed in R13 V-02 with positions 1 (flow-lifecycle body, descriptive) and 3 (trace-state body, inert). Scorers must not treat descriptive register as a distinguishing factor that alters C-33's inertness behavior. Fail this criterion if a scoring judgment withholds C-22 credit or applies a penalty solely because the axis-header rule appears in two named section bodies and the first placement is written in descriptive register.

#### C-39 -- C-37 No-N-Ceiling Rule Is Register-Invariant
- **Weight**: aspirational
- **Category**: format
- **Origin**: R13
- **Pass condition**: C-37's no-N-ceiling principle for multiple qualifying named section-body placements holds regardless of grammatical register. When the first qualifying named section-body placement satisfies C-22 in descriptive register, all subsequent qualifying placements (N=2, 3, ...) are inert in exactly the same way they are inert in imperative register. Register invariance (C-36) extends to C-37's inertness without modification. This is the first joint test of C-36 (register invariance) and C-37 (no-N-ceiling), confirmed in R13 V-04 with descriptive + triple section-body placement at the same positions as R12 V-05 (flow-lifecycle, trace-state, trace-permissions). The combination composes without interaction: neither descriptive register nor the count of qualifying placements restricts or modifies the other. Scorers must not treat additional qualifying placements in descriptive register as more restrictive than additional placements in imperative register. Fail this criterion if a scoring judgment withholds C-22 credit or applies a penalty on grounds that the axis-header rule appears in multiple named section bodies and is written in descriptive form.

#### C-40 -- C-37 No-Ceiling Principle Confirmed at N=4 and N=5 Structural Maximum
- **Weight**: aspirational
- **Category**: format
- **Origin**: R13
- **Pass condition**: C-37's no-N-ceiling principle has been confirmed at N=4 (four qualifying named section-body placements, R13 V-03) and at N=5, the structural maximum of the rhythm-behavior prompt (all five sub-skill section bodies simultaneously, R13 V-05). In both cases the first qualifying occurrence satisfies C-22 and placements 2 through N are all inert. No exception was found at any count or in either grammatical register across R13. The inertness principle now stands confirmed at the structural limit of the prompt: there is no count at which an additional qualifying placement becomes penalizable or converts from inert to structurally defective. Scorers must not infer an N-ceiling from any finite set of prior round confirmations, including R13's N=5 confirmation, as N=5 represents the structural maximum rather than a new ceiling. Fail this criterion if a scoring judgment withholds C-22 credit or applies a penalty on grounds that four or five qualifying named section-body placements exceed a reasonable or implied count limit.
