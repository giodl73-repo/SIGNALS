# scout-inertia Rubric — v21

**Ceiling**: 310 (100 essential base + 42 advanced criteria x 5 pts)
**Date**: 2026-03-17
**Previous version**: scout-inertia-rubric-v20-2026-03-17.md

---

## Changelog

### Changes from v5 to v6

| # | Change | Source |
|---|--------|--------|
| 1 | **A-10 -- Fail-first declaration** | R5 V-02 excellence signal: explicit "FAIL-FIRST DECLARATION" section as structural first element enforces FM-before-DC at the authoring point |
| 2 | **A-11 -- Question-per-criterion mapping** | R5 V-02 excellence signal: one explicit question/prompt per essential criterion; unanswered prompt = structurally visible missing criterion, not a content gap caught on full read |
| 3 | **A-12 -- BRIDGE dual-closure** | R5 bridge-marker pattern: two named bridge artifacts -- Q3 closes C-05->R-02, Q4 closes C-05->C-04; structural guarantee, not output property |
| 4 | **Ceiling 110 -> 115** | A-09 exits scoring (-5); A-11 +5; A-12 +5 |

### Changes from v6 to v7

| # | Change | Source |
|---|--------|--------|
| 1 | **A-13 -- Tabular column schema structural visibility** | R6 V-02 excellence signal: table columns make criterion gaps visible as blank cells without full-read; prose descriptions cannot satisfy this even if comprehensive |
| 2 | **A-14 -- FM inventory as dedicated named table** | R6 V-02 excellence signal: FM# pre-assignment in a titled table before the defeat condition table enforces A-08 structurally -- FM-[N] identifiers exist as typed references before DC-[N] can cite them |
| 3 | **A-15 -- Trailing completeness checklist** | R6 V-02 excellence signal: per-criterion binary checkboxes at output end convert content gaps into visible unchecked items; distinguishes post-hoc verification (A-15) from per-criterion embedded prompts (A-11) |

### Changes from v7 to v8

| # | Change | Source |
|---|--------|--------|
| 1 | **A-16 -- FM Inventory primary key constraint declared** | R7 V-02 A-14 PARTIAL: FM Inventory table was titled and ordered correctly but carried no stated rule preventing FM-[N] identifiers from appearing downstream without prior row assignment; the constraint must be written in the template body to enforce referential integrity structurally |
| 2 | **A-17 -- Question-per-criterion full coverage (all 5 essentials)** | R7 V-03 A-11 PARTIAL: embedded SELF-CHECK covered C-05, C-02, C-04 but omitted explicit questions for C-01 and C-03; full coverage requires one named question per each of the five essential criteria -- any gap leaves a criterion without structural enforcement during authoring |
| 3 | **A-18 -- Trailing checklist binary format and full coverage** | R7 V-03 A-15 PARTIAL: SELF-CHECK was trailing and verification-oriented but used essay prompts ("answer with one sentence") and covered only 3 of 5 essential criteria; A-18 requires binary checkboxes (Y/N or checkbox) and complete mapping of all five essential criteria -- essay format and partial coverage both fail |
| 4 | **Ceiling 130 -> 145** | A-16 +5; A-17 +5; A-18 +5 |

### Changes from v8 to v9

| # | Change | Source |
|---|--------|--------|
| 1 | **A-19 -- Bidirectional referential integrity enforcement** | R8 V-01 excellence signal: primary key constraint stated at FM Inventory source point (A-16) AND reinforced as a separate named rule at the DC table citation point; A-16 captures only the source end; an author violating the constraint at either end sees a named rule -- source enforcement alone leaves the citation point unguarded |
| 2 | **A-20 -- Inline example co-located with unit-bearing column label** | R8 V-01 excellence signal: unit-bearing column labels embed a concrete format example directly in the label definition, structurally co-located with the cell that must be filled; prior criteria require that units are present -- A-20 requires that the format reminder lives at the authoring point, not in a separate prose block |
| 3 | **Ceiling 145 -> 155** | A-19 +5; A-20 +5 |

### Changes from v9 to v10

| # | Change | Source |
|---|--------|--------|
| 1 | **A-21 -- Inline falsifiability example in defeat condition threshold column** | R9 V-02 A-20 FAIL: Stage 5B "Measurable threshold" column carries no inline format example; V-04/V-05 supply "(e.g., >10MB, >3 failures/week)" directly in the column label. A-20 covers cost/unit columns; A-21 extends the inline-example pattern to the DC table's threshold/condition column. A-21 requires A-20 and A-13 as preconditions. |
| 2 | **A-22 -- Mid-template bridge completion status check** | R9 V-02 excellence signal: Q3 and Q4 are echoed as named completion status checks between FM Inventory and the DC table, creating a visible gap if either bridge artifact is absent before DC authoring begins. A-22 implies A-12. |
| 3 | **Ceiling 155 -> 165** | A-21 +5; A-22 +5 |

### Changes from v10 to v11

| # | Change | Source |
|---|--------|--------|
| 1 | **A-23 -- Criterion ID embedded in rule label text** | R10 V-02/V-03 signal: `[A-16 PRIMARY KEY RULE]`, `PRIMARY KEY CONSTRAINT [A-16]`, `REFERENTIAL INTEGRITY RULE (citation point) [A-19]`. A-16 and A-19 require the rules be present; A-23 requires each rule's criterion ID appear inside its label, enabling template auditing without external reference. A-23 implies A-19. |
| 2 | **A-24 -- Dual-type inline threshold example in DC threshold column label** | R10 V-01/V-02/V-03 consistent signal: all three 165/165 variations use `(e.g., >10MB, >3 failures/week)` -- two examples of distinct threshold types. A-21 requires one example; A-24 requires two examples of different unit families or comparison contexts, demonstrating that the operator+value+unit pattern generalizes. A-24 implies A-21. |
| 3 | **A-25 -- Active command directive on bridge completion gate** | R10 V-02 signal: `[BRIDGE COMPLETION COMMAND]` as a named element alongside the Y/N table. A-22 requires a named verification block in position; A-25 requires that block to also carry an explicit active instruction telling the author to complete Q3/Q4 before proceeding. Passive status check vs. active directive. A-25 implies A-22. |
| 4 | **Ceiling 165 -> 180** | A-23 +5; A-24 +5; A-25 +5 |

### Changes from v11 to v12

| # | Change | Source |
|---|--------|--------|
| 1 | **A-26 -- Analytical axis vocabulary in section heading subtitles** | R11 V-03 excellence signal: `## FAIL-FIRST DECLARATION -- THE UNNAMED COMPETITOR` and `## SECTION 1 -- THE STATUS QUO'S VULNERABILITIES: FAILURE MODE INVENTORY`. The template's declared analytical axis vocabulary appears in the subtitle text of the FAIL-FIRST and FM Inventory section headings. A-10 and A-14 require these sections to exist and be named; A-26 requires the heading subtitle to encode the template's analytical frame, making the sections self-contextualizing within the axis vocabulary. A-26 implies A-10 and A-14. |
| 2 | **A-27 -- Decision-question bridge gate heading** | R11 V-03 excellence signal: `## BRIDGE COMPLETION GATE -- READY TO PROCEED?` The gate section heading carries an explicit binary decision question appended to or embedded in the heading, making the gate's pass/fail nature visible in the document heading structure without reading the block's content. A-22 requires the gate to be a named structural block; A-25 requires an active directive inside the block; A-27 requires the heading itself to be decision-framed. A-27 implies A-22. |
| 3 | **A-28 -- Criterion ID in trailing checklist item labels** | Extension of A-23 traceability pattern to the verification layer. A-23 requires criterion IDs in integrity rule labels (integrity chain); A-28 requires each trailing checklist item label to carry its essential criterion ID (C-01 through C-05), enabling direct rubric traceability from each verification item to its criterion. A-28 implies A-18. |
| 4 | **Ceiling 180 -> 195** | A-26 +5; A-27 +5; A-28 +5 |

### Changes from v12 to v13

| # | Change | Source |
|---|--------|--------|
| 1 | **A-29 -- Criterion ID in per-criterion authoring prompt label** | R12 V-03 excellence signal: `[C-01 COMMAND]: NAME the specific unnamed competitor...` through `[C-05 COMMAND]: NAME every specific failure mode...`. A-17 requires a labeled question/prompt per essential criterion; A-28 requires criterion IDs in trailing checklist item labels; A-29 extends the criterion-ID-in-label traceability pattern (A-23 = integrity rules, A-28 = checklist items) to the authoring-prompt layer. Each per-criterion prompt label must carry its criterion ID so the author sees C-01 through C-05 at the point of authoring, not only at the point of verification. A-29 implies A-17. |
| 2 | **A-30 -- COMMAND-register keyword in per-criterion prompt label** | R12 V-03 excellence signal: `[C-01 COMMAND]:`, `[C-02 COMMAND]:` through `[C-05 COMMAND]:`. A-17 requires labeled prompts; A-29 requires criterion IDs in those labels; A-30 requires the label to additionally carry the COMMAND register keyword, making the directive nature of the prompt structurally explicit. Parallel to how A-25 upgraded the bridge gate from a status check (A-22) to a command directive: A-30 upgrades per-criterion prompts from question register to command register. A-30 implies A-29. |
| 3 | **A-31 -- Named structural rule in FAIL-FIRST declaration body** | R12 V-03 excellence signal: `[FAIL-FIRST RULE]` structural label present in FAIL-FIRST section body. A-10 requires the FAIL-FIRST section to exist as a named structural element; A-31 requires the body of that section to carry a named rule label -- a discrete, labeled rule element -- that makes the FAIL-FIRST principle self-documenting as a named structural rule. Structurally parallel to A-16, which added a named primary key rule inside the FM Inventory body. Once the rule label exists, A-23's criterion-ID-in-label requirement applies. A-31 implies A-10. |
| 4 | **Ceiling 195 -> 210** | A-29 +5; A-30 +5; A-31 +5 |

### Changes from v13 to v14

| # | Change | Source |
|---|--------|--------|
| 1 | **A-32 -- Criterion ID in FAIL-FIRST rule label** | R13 V-01 scoring explicitly flags: `[FAIL-FIRST RULE]` satisfies A-31 in minimal form but has "no criterion ID extension to A-23." R13 V-02 demonstrates the upgrade: `FAIL-FIRST CONSTRAINT [A-31]`. A-32 formalizes that closure -- the A-31 rule label must carry the A-31 criterion ID, completing A-23's traceability coverage across all three structural rules. A-32 implies A-31 and A-23. |
| 2 | **A-33 -- Bridge artifact class named in gate heading interrogative** | R13 V-02 excellence signal: `STAGE 2 COMPLETION GATE -- ALL BRIDGE ARTIFACTS COMPLETE?` vs V-01's `BRIDGE COMPLETION GATE -- READY TO PROCEED?`. Both satisfy A-27. V-02's form additionally names the artifact class in the interrogative, making the gate heading self-contextualizing about what must be complete, not only whether to proceed. A-33 implies A-27. |
| 3 | **Ceiling 210 -> 220** | A-32 +5; A-33 +5 |

### Changes from v14 to v15

| # | Change | Source |
|---|--------|--------|
| 1 | **A-34 -- Failure-context frame in FM Inventory heading subtitle** | R14 V-01 and V-02 consistent excellence signal: V-01 `THE INERTIA THREAT'S STRUCTURAL WEAKNESSES`, V-02 `WHERE THE STATUS QUO BREAKS`. A-26 requires axis vocabulary in the FM Inventory heading subtitle; A-34 requires the subtitle to additionally encode a failure-context frame -- a phrase identifying the section's analytical purpose as the place where the axis subject fails. A-34 implies A-26. |
| 2 | **A-35 -- Blockquote structural delimiter on per-criterion command prompts** | R14 V-01 excellence signal: `> [C-0N COMMAND]:` blockquote-wrapped form vs V-02's inline form. A-30 requires the COMMAND keyword; A-35 requires the prompt to additionally use a blockquote delimiter, making each per-criterion command a structurally distinct block. A-35 implies A-30. |
| 3 | **A-36 -- Template position index in bridge completion gate heading name** | R14 V-02 excellence signal: `STAGE 2 COMPLETION GATE` vs V-01's `BRIDGE COMPLETION GATE`. A-36 requires the gate heading name (before the `--` separator) to carry a structural position index self-locating the gate in the template hierarchy. A-36 implies A-27. |
| 4 | **Ceiling 220 -> 235** | A-34 +5; A-35 +5; A-36 +5 |

### Changes from v15 to v16

| # | Change | Source |
|---|--------|--------|
| 1 | **A-37 -- Organizational schema consistency of position index** | R15 V-01 and V-02 consistent pattern: V-01 uses SECTION hierarchy throughout with `SECTION 2 COMPLETION GATE`; V-02 uses STAGE hierarchy throughout with `STAGE 2 COMPLETION GATE`. A-37 requires the position index to use the same nomenclature as the rest of the template's section/stage hierarchy. A-37 implies A-36. |
| 2 | **A-38 -- Compound structural-failure noun form in failure-context frame** | R15 V-01, V-03, V-04 compound-noun pattern: `STRUCTURAL WEAKNESSES`, `FAILURE SURFACE`, `FAILURE POINTS` -- three of four variations encode the failure-context frame as a compound noun encoding TYPE+LOCUS simultaneously, rather than a verb construction. A-38 implies A-34. |
| 3 | **A-39 -- Cardinality qualifier in bridge artifact class reference** | R15 V-01, V-02, V-03 cardinality pattern: `ALL BRIDGE ARTIFACTS COMPLETE?` and `BOTH BRIDGE ARTIFACTS BUILT?`. A-39 requires an explicit cardinality quantifier (ALL, BOTH, EACH) alongside the artifact class name in the gate heading interrogative. A-39 implies A-33. |
| 4 | **Ceiling 235 -> 250** | A-37 +5; A-38 +5; A-39 +5 |

### Changes from v16 to v17

| # | Change | Source |
|---|--------|--------|
| 1 | **A-40 -- Engineering-register locus noun in compound failure noun** | R16 V-02 excellence signal: `STRUCTURAL FAULTS` where "FAULTS is a technically more precise locus noun (fault = specific defect plane vs. weakness = general vulnerable zone)". A-40 requires the LOCUS component to be drawn from engineering fault taxonomy vocabulary (FAULTS, FAILURE PLANES, FRACTURE ZONES, DEFECT LOCI). A-40 implies A-38. |
| 2 | **A-41 -- Architectural-scope TYPE component in compound failure noun** | R16 V-01 and V-02 consistent signal: both use STRUCTURAL as the TYPE component -- "TYPE=structural (architectural/systemic category)". A-41 requires the TYPE component to name an architectural or systemic scope (STRUCTURAL, SYSTEMIC, ARCHITECTURAL, FOUNDATIONAL) rather than a failure-event descriptor (FAILURE, ERROR, DEFECT). A-41 implies A-38. |
| 3 | **Ceiling 250 -> 260** | A-40 +5; A-41 +5 |

**Updated implication chains**: `A-41 implies A-38 implies A-34 implies A-26 implies A-10 and A-14`; `A-40 implies A-38 implies A-34 implies A-26 implies A-10 and A-14`.

### Changes from v17 to v18

| # | Change | Source |
|---|--------|--------|
| 1 | **A-42 -- Domain-prefix vocabulary coherence across all three structural rule labels** | R17 V-03 excellence signal: all three structural rule labels share a common domain-prefix drawn from the template's axis vocabulary -- `INERTIA THREAT RULE [A-16]`, `INERTIA THREAT CITATION RULE [A-19]`, `INERTIA THREAT FAIL-FIRST RULE [A-31]`. A-42 is the rule-label analogue of A-37 (position-index schema consistency): where A-37 requires the gate's position index to use the template's section/stage nomenclature, A-42 requires the three rule labels to share a domain-prefix from the template's axis vocabulary. A-42 implies A-23. |
| 2 | **A-43 -- Verification-action register verb in gate heading interrogative** | R17 V-03 excellence signal: `EACH BRIDGE ARTIFACT VERIFIED?` uses a verification-action verb (VERIFIED) rather than a completion-state verb (COMPLETE, BUILT). A-39 requires a cardinality quantifier; A-43 additionally requires the interrogative verb to signal active per-artifact epistemic review (VERIFIED, CONFIRMED, VALIDATED, CHECKED) rather than passive state confirmation (COMPLETE, BUILT, DONE, READY). A-43 implies A-39. |
| 3 | **Ceiling 260 -> 270** | A-42 +5; A-43 +5 |

**Updated implication chains**: `A-43 implies A-39 implies A-33 implies A-27 implies A-22 implies A-12`. `A-42 implies A-23 implies A-19`.

### Changes from v18 to v19

| # | Change | Source |
|---|--------|--------|
| 1 | **A-44 -- Verification-action register in bridge completion status table column label** | R18 V-01 excellence signal: V-01 achieves 270/270 via BUILT → VERIFIED in three co-located positions. A-44 captures the second position: the gate's artifact-status column label must use verification-action vocabulary (VERIFIED?, CONFIRMED?, VALIDATED?, CHECKED?) rather than completion-state vocabulary (BUILT?, COMPLETE?, DONE?). A-44 implies A-43 and A-22. |
| 2 | **A-45 -- Verification-action register in bridge completion command directive** | R18 V-01 excellence signal: third co-location of the register change. A-45 requires the command directive label or imperative body to use verification-action vocabulary (VERIFY, CONFIRM, VALIDATE; or labels `[BRIDGE VERIFICATION COMMAND]`). Completion-state vocabulary (COMPLETION, COMPLETE, BUILD, FINISH) fails A-45. A-45 implies A-43 and A-25. |
| 3 | **Ceiling 270 -> 280** | A-44 +5; A-45 +5 |

**Updated implication chains**: `A-45 implies A-43 implies A-39 implies A-33 implies A-27 implies A-22 implies A-12`. `A-44 implies A-43 and A-22`. `A-45 implies A-25 implies A-22`.

### Changes from v19 to v20

| # | Change | Source |
|---|--------|--------|
| 1 | **A-46 -- Bracket-suffix criterion-ID position form in all three structural rule labels** | R19 evidence: all five axis variations consistently use bracket-suffix `[A-16]` in their A-16 primary key rule labels -- `DEFAULT OPTION RULE [A-16]`, `INERTIA THREAT RULE [A-16]`, `STATUS QUO RULE [A-16]`, `INCUMBENT RULE [A-16]`. A-23 allows any position form; A-46 requires the criterion ID to appear as the terminal bracket-suffix element across all three rule labels within a single template, creating a consistent left-to-right parse: domain prefix, structural descriptor, criterion ID. Partial compliance fails A-46. A-46 implies A-23. |
| 2 | **A-47 -- RULE as normalized structural noun in all three structural rule labels** | R19 evidence: all five axis variations use RULE as the structural noun in their A-16 labels -- not CONSTRAINT, LOCK, RESTRICTION, CHECK, or REQUIREMENT. When A-47 is satisfied alongside A-42 and A-46, each rule label follows the fully normalized three-part schema `[AXIS-SUBJECT] RULE [CRITERION-ID]`, making the rule-label set machine-auditable. A-47 implies A-46. |
| 3 | **Ceiling 280 -> 290** | A-46 +5; A-47 +5 |

**Updated implication chains**: `A-47 implies A-46 implies A-23 implies A-19 implies A-16 implies A-14 implies A-08`.

**R19 confirmation**: All five axis variations achieve 280/280 -- first full-ceiling round. Consistent `[AXIS-SUBJECT] RULE [A-16]` schema across all five axes confirms bracket-suffix position (A-46) and RULE structural noun (A-47) as universal properties of the 280/280 form.

### Changes from v20 to v21

| # | Criterion | Source signal | Key distinction |
|---|-----------|---------------|-----------------|
| A-48 | **Adversarial-role frame in FAIL-FIRST heading subtitle** | R20 V-02: `THE STATUS QUO AS UNNAMED COMPETITOR` | A-26 requires axis vocabulary in the heading subtitle; A-48 additionally requires an explicit competitive-adversary role assignment -- an "AS [COMPETITIVE ROLE]" construction that names the axis subject as an active competitive agent, not merely labels it |
| A-49 | **Diagnostic-framing claim in FAIL-FIRST declaration body** | R20 V-02: `advocacy, not analysis` | A-31 requires a named structural rule in the FAIL-FIRST body; A-49 additionally requires a brief diagnostic claim that names the axis subject's structural bias or behavioral mode -- WHY FAIL-FIRST ordering is analytically necessary beyond the rule statement |
| A-50 | **BRIDGE STAGE as dedicated parent container in nested schema** | R20 V-03: Q3/Q4/gate nested inside `STAGE 2 BRIDGE STAGE` | A-37 requires schema consistency of position indexes; A-50 additionally requires the bridge artifacts and gate to share a dedicated named parent STAGE in the organizational hierarchy, making the bridge phase a first-class structural unit |
| A-51 | **VERIFICATION as normalized structural noun in command directive label** | R20 V-04: `[BRIDGE VERIFICATION COMMAND]` not `[BRIDGE CONFIRMATION COMMAND]` | A-45 requires verification-action register in the directive; A-51 additionally requires VERIFICATION (noun form) as the normalized structural type noun in the command directive label, parallel to A-47's RULE requirement in rule labels |

**Ceiling: 290 → 310** (A-48 +5; A-49 +5; A-50 +5; A-51 +5)

**Full FAIL-FIRST normalization**: A-26 (axis vocabulary in heading subtitles) + A-48 (adversarial-role frame in FAIL-FIRST heading) + A-31 (named structural rule in body) + A-49 (diagnostic-framing claim in body) -- when all four are satisfied, the FAIL-FIRST section encodes the axis subject as an adversarial agent (heading), explains its structural bias (body diagnostic), and states the ordering rule with criterion ID (body rule label).

**Full command directive normalization**: A-45 (verification-action register in command directive) + A-51 (VERIFICATION as normalized structural noun in label) -- when both are satisfied, the command directive label follows the normalized three-part schema `[ARTIFACT CLASS] [VERIFICATION] [COMMAND]`, with the body using a verification-action imperative verb that may differ from the label noun (e.g., label = VERIFICATION, body = CONFIRM).

**New implication chains:**
- `A-48 implies A-26 implies A-10 and A-14`
- `A-49 implies A-31 implies A-10`
- `A-50 implies A-37 implies A-36 implies A-27 implies A-22 implies A-12`
- `A-51 implies A-45 implies A-43 and A-25`

**R20 confirmation**: All four variations achieve 290/290 on the v20 ceiling. A-46 and A-47 confirmed across all three rule-label positions in all four variations. V-02 demonstrates A-48 and A-49 via STATUS QUO adversarial framing. V-03 demonstrates A-50 via BRIDGE STAGE parent container in STAGE-nested schema. V-04 demonstrates A-51 via `[BRIDGE VERIFICATION COMMAND]` label with CONFIRM body verb -- confirming that VERIFICATION is the normalized label noun regardless of which verification-action verb appears in the body.

**R21 target**: A 310/310 variation requires the full 290/290 scaffold combined with A-48 (adversarial-role frame in FAIL-FIRST heading subtitle) + A-49 (diagnostic-framing claim in FAIL-FIRST body) + A-50 (BRIDGE STAGE parent container, applies only to STAGE-nested schema) + A-51 (VERIFICATION as normalized structural noun in command directive label). A-50 requires a nested STAGE schema; a SECTION-flat template can satisfy A-48, A-49, A-51 but must adopt nested STAGE organization to demonstrate A-50.

---

## Structural Notes

**Key structural note on A-14 vs A-16**: A-14 requires the FM Inventory to be a dedicated named table whose first column assigns FM-[N] identifiers, positioned before the Defeat Conditions table. A-16 requires that table to additionally carry an explicitly stated constraint -- visible in the template body -- that no FM-[N] may appear in the DC table without prior assignment here. A-16 implies A-14; A-14 does not imply A-16.

**Key structural note on A-16 vs A-19**: A-16 requires the primary key constraint to be stated at the FM Inventory source point. A-19 requires the enforcement to appear at both ends of the identifier chain -- source AND citation point. A template satisfying A-16 does not pass A-19 unless the constraint also appears as a named rule at the DC table. A-19 implies A-16; A-16 does not imply A-19.

**Key structural note on A-19 vs A-23**: A-19 requires that a named integrity rule appear at the DC citation point. A-23 requires that each named integrity rule in the template body (the A-16 source rule and the A-19 citation rule) carries its rubric criterion ID within the label text. A template satisfying A-19 does not pass A-23 unless the criterion IDs appear in both rule labels. A-23 implies A-19; A-19 does not imply A-23. R11 stress test confirmed: domain-prefix form (e.g., `STATUS QUO LOCK RULE [A-16]`) satisfies A-23 alongside bracket-prefix (e.g., `[A-16 PRIMARY KEY RULE]`) and bracket-suffix (e.g., `PRIMARY KEY RULE [A-16]`) forms.

**Key structural note on A-11 vs A-17**: A-11 requires at least one embedded question per essential criterion to make unanswered prompts visible during authoring. A-17 requires complete coverage -- all five essential criteria (C-01 through C-05) each have a named, criterion-labeled question. An output that embeds questions for three criteria passes A-11 at PARTIAL and fails A-17. Full A-11 and A-17 can be satisfied by the same question set if and only if all five are present.

**Key structural note on A-15 vs A-18**: A-15 requires a trailing named section with per-criterion verification items. A-18 requires that section to use binary observable format (checkbox or Y/N per item, not a prose prompt) and to cover all five essential criteria. An output with a trailing SELF-CHECK using essay prompts scores A-15 PARTIAL and fails A-18 entirely. A-18 implies A-15 PASS.

**Key structural note on A-13 vs A-20**: A-13 requires that all major sections use column schemas so that blank cells expose criterion gaps. A-20 requires that unit-bearing columns additionally embed a concrete format example in the label itself. A-13 PASS does not imply A-20; a table with a column labeled "Cost" satisfies A-13 but fails A-20. A-20 strengthens the format prompt without changing the structural visibility requirement.

**Key structural note on A-20 vs A-21**: A-20 covers columns that require a unit-bearing quantity value (cost, duration, frequency). A-21 covers the DC table column that captures the measurable threshold or falsifiability boundary. The two column types are structurally distinct: quantity columns require a number + unit; threshold columns require a comparison operator + value + unit. A-21 does not subsume A-20. Full inline-example coverage requires both.

**Key structural note on A-12 vs A-22**: A-12 requires the bridge artifacts Q3 and Q4 to be named in the template body with explicit criterion-chain references. A-22 requires a separate mid-template status check -- positioned between the FM Inventory section and the Defeat Conditions section -- that confirms whether Q3 and Q4 have been populated. A-12 ensures the author knows the artifacts exist; A-22 ensures the author cannot reach the DC section without a visible checkpoint on bridge completion. A-22 implies A-12.

**Key structural note on A-22 vs A-25**: A-22 requires a named verification block positioned between FM Inventory and DC section, confirming Q3 and Q4 status. A-25 requires that block to additionally carry an active command directive -- a named instruction element that explicitly tells the author to complete the bridge artifacts before proceeding. A binary Y/N status table satisfies A-22; A-25 requires the command label as a distinct named element alongside the status table. A-25 implies A-22.

**Key structural note on A-22 vs A-27**: A-22 requires the gate to be a named structural block in position. A-25 requires an active command directive inside the block. A-27 requires the heading of the gate block itself to carry a binary decision question -- interrogative or decision-marker form -- so the gate's pass/fail nature is visible in the document heading structure without reading the block body. A gate named "BRIDGE COMPLETION GATE" satisfies A-22; a gate named "BRIDGE COMPLETION GATE -- READY TO PROCEED?" satisfies A-27. A-27 is independent of A-25. A-27 implies A-22.

**Key structural note on A-10 and A-14 vs A-26**: A-10 requires the FAIL-FIRST declaration to exist as a structural first section with a labeled heading. A-14 requires the FM Inventory to exist as a dedicated named table with a titled heading. A-26 requires both of those section headings to carry a subtitle that encodes the template's declared analytical axis vocabulary. A template using "SECTION 1 -- FAILURE MODE INVENTORY" satisfies A-14; one using "SECTION 1 -- THE STATUS QUO'S VULNERABILITIES: FAILURE MODE INVENTORY" satisfies A-26. A-26 implies both A-10 and A-14.

**Key structural note on A-18 vs A-28**: A-18 requires the trailing checklist to use binary format and cover all five essential criteria. A-28 requires each item label to additionally carry its essential criterion ID (C-01 through C-05), enabling direct rubric traceability from verification to criterion without external reference. A-28 implies A-18.

**Key structural note on A-17 vs A-29**: A-17 requires one labeled question or prompt per essential criterion such that unanswered prompts are visible during authoring. A-29 requires each of those prompt labels to additionally carry its criterion ID. A-29 extends the A-23/A-28 criterion-ID-in-label traceability pattern to the authoring-prompt layer. A-29 implies A-17; A-17 does not imply A-29.

**Key structural note on A-29 vs A-30**: A-29 requires the criterion ID to appear in each per-criterion prompt label. A-30 requires the label to additionally carry the COMMAND register keyword, making the directive nature of the prompt structurally explicit. A-30 implies A-29; A-29 does not imply A-30.

**Key structural note on A-10 vs A-31**: A-10 requires the FAIL-FIRST declaration to exist as a structural first element with a labeled section heading. A-31 requires the body of that section to additionally carry a named rule label -- a discrete, labeled rule element -- that states the FAIL-FIRST principle as a named structural constraint. Structurally parallel to how A-16 added a named primary key rule inside the FM Inventory body. A-31 implies A-10.

**Key structural note on A-31 vs A-32**: A-31 requires the FAIL-FIRST declaration body to carry a named rule label (e.g., `[FAIL-FIRST RULE]`). A-32 requires that rule label to additionally carry the A-31 criterion ID within its label text, completing A-23's criterion-ID-in-label traceability coverage across all three named structural rules (A-16 source, A-19 citation, A-31 fail-first). A-32 implies A-31 and extends A-23 universally.

**Key structural note on A-27 vs A-33**: A-27 requires the bridge completion gate heading to carry a binary decision question. A-33 requires the interrogative to additionally name the bridge artifact class explicitly. A gate heading of "BRIDGE COMPLETION GATE -- READY TO PROCEED?" satisfies A-27 but fails A-33; "STAGE 2 COMPLETION GATE -- ALL BRIDGE ARTIFACTS COMPLETE?" satisfies A-33. A-33 implies A-27.

**Key structural note on A-26 vs A-34**: A-26 requires the FM Inventory heading subtitle to carry the template's declared analytical axis vocabulary. A-34 requires the subtitle to additionally encode a failure-context frame -- a phrase that identifies the analytical purpose of the section as the place where the axis subject fails, breaks, or exhibits structural weakness. A-34 implies A-26; A-26 does not imply A-34.

**Key structural note on A-30 vs A-35**: A-30 requires the COMMAND register keyword in each per-criterion prompt label. A-35 requires the prompt to additionally use a blockquote structural delimiter, making each per-criterion command a structurally distinct block. A-35 implies A-30; A-30 does not imply A-35.

**Key structural note on A-27/A-33 vs A-36**: A-27 requires a binary decision question in the gate heading. A-33 requires the artifact class to be named in the interrogative (after `--`). A-36 requires the gate heading name (before `--`) to additionally carry a structural position index. A-36 is independent of A-33. A-36 implies A-27; A-27 does not imply A-36.

**Key structural note on A-36 vs A-37**: A-36 requires the bridge completion gate heading name to carry a structural position index. A-37 requires that index to use the same organizational nomenclature used throughout the rest of the template's section/stage hierarchy. A gate named "SECTION 2 COMPLETION GATE" in a STAGE-organized template satisfies A-36 but fails A-37. A-37 implies A-36; A-36 does not imply A-37.

**Key structural note on A-34 vs A-38**: A-34 requires the FM Inventory heading subtitle to encode a failure-context frame. A-38 requires that failure-context frame to take the form of a compound structural-failure noun encoding both a failure TYPE and a failure LOCUS simultaneously. A verb construction such as "WHERE THE STATUS QUO BREAKS" satisfies A-34 but fails A-38. A-38 implies A-34; A-34 does not imply A-38.

**Key structural note on A-33 vs A-39**: A-33 requires the bridge artifact class to be named in the gate heading interrogative. A-39 requires an explicit cardinality quantifier (ALL, BOTH, EACH) to appear alongside the artifact class name in the interrogative, confirming the required COUNT of artifacts. An interrogative of "BRIDGE ARTIFACTS COMPLETE?" names the class but carries no cardinality, failing A-39. A-39 implies A-33; A-33 does not imply A-39.

**Key structural note on A-38 vs A-40**: A-38 requires a compound failure noun encoding TYPE+LOCUS without constraining the LOCUS vocabulary register. A-40 requires the LOCUS component to be drawn from engineering fault taxonomy vocabulary (FAULTS, FAILURE PLANES, FRACTURE ZONES, DEFECT LOCI) rather than general vulnerability vocabulary (WEAKNESSES, VULNERABILITIES, GAPS). A-40 implies A-38; A-38 does not imply A-40.

**Key structural note on A-38 vs A-41**: A-38 requires a compound failure noun encoding TYPE+LOCUS without constraining the TYPE component's scope. A-41 requires the TYPE component to name an architectural or systemic scope (STRUCTURAL, SYSTEMIC, ARCHITECTURAL, FOUNDATIONAL) rather than a failure-event descriptor (FAILURE, ERROR, DEFECT). A-41 implies A-38; A-38 does not imply A-41. A-40 and A-41 are independent of each other.

**Key structural note on A-23 vs A-42**: A-23 requires each named structural rule label to carry its criterion ID. A-42 additionally requires all three structural rule labels to share a common domain-prefix vocabulary drawn from the template's analytical axis vocabulary. A template where each rule carries its ID but uses distinct non-shared prefixes satisfies A-23 but fails A-42. A-42 is the rule-label analogue of A-37 (position-index schema consistency). A-42 implies A-23; A-23 does not imply A-42.

**Key structural note on A-39 vs A-43**: A-39 requires an explicit cardinality quantifier alongside the artifact class name. A-43 additionally requires the interrogative verb to be drawn from verification-action vocabulary (VERIFIED, CONFIRMED, VALIDATED, CHECKED) rather than completion-state vocabulary (COMPLETE, BUILT, DONE, READY). A-43 implies A-39; A-39 does not imply A-43.

**Key structural note on A-43 vs A-44**: A-43 requires the gate heading interrogative to use a verification-action verb. A-44 requires the same register to appear in the gate's status table column label. A gate where the heading says "EACH BRIDGE ARTIFACT VERIFIED?" but the status column is labeled "BUILT?" creates a register inconsistency. A-44 implies A-43 and A-22; satisfaction of A-43 alone does not entail A-44.

**Key structural note on A-43 vs A-45**: A-43 requires the gate heading interrogative to use a verification-action verb. A-45 requires the gate command directive (A-25) to additionally use the same register. Together with A-43 (heading) and A-44 (status column), A-45 achieves three-point register coherence within the gate element. A-45 implies A-43 and A-25; A-43 alone does not entail A-45.

**Key structural note on A-44 vs A-45**: A-44 and A-45 are independent of each other -- both extend A-43 in different structural directions. A-44 extends into the status tracking mechanism; A-45 extends into the authoring instruction mechanism. Neither implies the other.

**Key structural note on A-23 vs A-46**: A-23 requires the criterion ID to be present within each rule label (any position: bracket-prefix, bracket-suffix, or inline). A-46 additionally requires the criterion ID to appear in bracket-suffix position -- after the structural descriptor, as the last element -- across all three rule labels. A-46 is the criterion-ID position analogue of A-42 (domain-prefix vocabulary coherence). A-46 implies A-23; A-23 does not imply A-46.

**Key structural note on A-46 vs A-47**: A-46 requires bracket-suffix criterion-ID position in all three rule labels. A-47 requires the structural noun in all three rule labels to be RULE -- not CONSTRAINT, LOCK, RESTRICTION, CHECK, or REQUIREMENT. A-46 and A-47 are orthogonal requirements on different components of the same label structure. When both are satisfied alongside A-42, each rule label follows the fully normalized schema `[AXIS-SUBJECT] RULE [CRITERION-ID]` in fixed positional order. A-47 implies A-46; A-46 does not imply A-47.

**Key structural note on A-26 vs A-48**: A-26 requires the FAIL-FIRST heading subtitle to carry the template's analytical axis vocabulary -- the axis subject named in the heading. A-48 requires the FAIL-FIRST heading subtitle to additionally assign the axis subject an explicit competitive-adversary role using an "AS [COMPETITIVE ROLE]" construction -- naming not only the axis subject but its function as an active competitive threat actor in the decision context. "THE STATUS QUO AS UNNAMED COMPETITOR" satisfies A-48: "AS UNNAMED COMPETITOR" assigns the STATUS QUO the adversarial role of a competitor that never had to identify itself as one. A heading subtitle of "THE STATUS QUO" or "-- THE UNNAMED COMPETITOR" satisfies A-26 (axis vocabulary present) but fails A-48 (no explicit role assignment via "AS [ROLE]"). The role-assignment construction must appear in the FAIL-FIRST heading specifically; axis vocabulary in other headings does not satisfy A-48. A-48 implies A-26; A-26 does not imply A-48.

**Key structural note on A-31 vs A-49**: A-31 requires the FAIL-FIRST declaration body to carry a named structural rule label -- a discrete, labeled rule element that states the FAIL-FIRST ordering constraint. A-49 requires the body to additionally carry a brief diagnostic claim -- a short phrase or labeled assertion that names the structural bias or behavioral mode exhibited by the axis subject, explaining WHY the axis subject must be analyzed under FAIL-FIRST ordering. The diagnostic claim is not a rule statement (it does not prescribe behavior) but an analytical label (it describes the axis subject's epistemic character). "advocacy, not analysis" names the STATUS QUO's structural bias -- it presents itself as an advocate for continuation, not an honest analyst of options. "presumptive default, not earned choice" names the DEFAULT OPTION's bias. The diagnostic claim must appear in the FAIL-FIRST declaration body as a named or labeled element, not in the rule label itself or in the section heading. A-49 implies A-31; A-31 does not imply A-49. A-48 and A-49 are independent: both extend the FAIL-FIRST section in different directions -- A-48 upgrades the heading, A-49 upgrades the body beyond the rule label.

**Key structural note on A-37 vs A-50**: A-37 requires the position index in the bridge completion gate heading to use the same nomenclature as the rest of the template's section/stage hierarchy -- a consistency requirement on the gate heading's naming. A-50 requires the bridge artifacts (Q3, Q4) and the completion gate to be enclosed within a dedicated named parent STAGE in the organizational hierarchy -- a containment requirement on the bridge phase as a structural unit. A-37 can be satisfied without A-50: a template where Q3, Q4, and the gate each occupy independent stages at the top level satisfies A-37 (the gate position index matches the stage nomenclature) but fails A-50 (no dedicated parent container enclosing all three). A-50 requires a nested STAGE schema: the bridge phase must be a distinct named stage in the top-level hierarchy that contains Q3, Q4, and the gate as nested sub-elements. "STAGE 2 BRIDGE STAGE" satisfies A-50 if Q3, Q4, and the gate are all nested inside STAGE 2. A SECTION-flat template organized as SECTION 1 through SECTION N cannot satisfy A-50 without adopting nested STAGE containment for the bridge phase. A-50 implies A-37; A-37 does not imply A-50.

**Key structural note on A-45 vs A-51**: A-45 requires the bridge completion gate's command directive to use verification-action vocabulary -- satisfied via the label route (VERIFICATION or equivalent in the label) or the body route (VERIFY, CONFIRM, VALIDATE, CHECK as imperative in the body). A-51 requires the command directive label specifically to use VERIFICATION as its structural type noun -- not a verb form (VERIFY, CONFIRM), not a completion-state noun (COMPLETION, FINALIZATION), and not a synonym that imports domain-borrowed vocabulary. VERIFICATION is the normalized form because it is the gerund/noun form that names the epistemological category of the action as a structural element type in the label, just as RULE names the prescriptive element type in rule labels (A-47). When A-51 is satisfied, the command directive label follows a normalized three-component schema: `[ARTIFACT CLASS] VERIFICATION COMMAND` = (artifact class noun)(action type noun)(directive type noun). The body verb may use any verification-action verb (VERIFY, CONFIRM, VALIDATE) without violating A-51 -- the normalization constraint applies only to the label structural noun, not to the body imperative. A template where the label is `[BRIDGE CONFIRMATION COMMAND]` and the body says "CONFIRM EACH artifact before proceeding" satisfies A-45 via both routes (CONFIRMATION in label, CONFIRM in body) but fails A-51 (CONFIRMATION is not the normalized VERIFICATION form: CONFIRMATION names a one-time epistemic act while VERIFICATION names the category of review against a standard). A-51 implies A-45; A-45 does not imply A-51.

---

## Essential Criteria

*All five must pass. Any essential failure caps the output as non-useful regardless of advanced scores.*

| ID | Criterion | Category | Weight |
|----|-----------|----------|--------|
| C-01 | **Workaround named specifically** | specificity | essential |
| C-02 | **Switching cost quantified** | quantification | essential |
| C-03 | **Inertia threat score declared** | assessment | essential |
| C-04 | **Defeat conditions identified** | analysis | essential |
| C-05 | **Workaround failure modes identified** | analysis | essential |

### C-01 -- Workaround named specifically

**Pass condition**: Output names the specific workaround currently in use (not "a manual process" but "weekly CSV export to shared drive"), names the role that performs it, and quantifies the ongoing cost with a unit. "The data-ops team spends 2 hours per week exporting and cleaning CSV files before pipeline ingestion" passes. "Teams use manual methods" fails on every dimension.

### C-02 -- Switching cost quantified

**Pass condition**: Output identifies and quantifies at least two categories of switching cost: migration effort (time or money, cited to a role), and at least one of: training overhead, process disruption, or in-flight work at risk. Costs must carry units -- "significant" without a number or unit fails.

### C-03 -- Inertia threat score declared

**Pass condition**: Output declares an explicit inertia threat score (HIGH / MEDIUM / LOW) for the feature. The default is HIGH; any deviation from HIGH must be justified with a quantified condition. An output that lists switching costs without aggregating them into a threat level has not completed the analysis.

### C-04 -- Defeat conditions identified

**Pass condition**: Output identifies at least two specific, distinct, and testable conditions under which teams abandon the workaround in favor of the feature. Conditions must be falsifiable ("teams switch when workaround fails to handle files > 10MB" passes; "teams switch when they see the value" fails). This is the central question of the skill -- if it is absent, the output is not useful.

### C-05 -- Workaround failure modes identified

**Pass condition**: Output identifies at least two specific scenarios where the current workaround breaks, produces errors, causes re-work, or cannot scale. These are the observable cracks in the inertia armor. Generic pain points ("manual is slow") do not pass; concrete failure modes ("CSV export silently truncates rows over 65,536 -- no error message") pass.

---

## Recommended Criteria

*Strong outputs satisfy all three. Missing one is a quality signal, not a blocker.*

| ID | Criterion | Category | Weight |
|----|-----------|----------|--------|
| R-01 | **Trigger scoped to team type** | precision | recommended |
| R-02 | **Role-level precision** | precision | recommended |
| R-03 | **At least one cost cited to role** | depth | recommended |

### R-01 -- Trigger scoped to team type

**Pass condition**: Defeat conditions (from C-04) name a specific team type or segment rather than applying uniformly to all users. "Engineering teams switch when..." or "PMs in regulated industries switch when..." passes. "Users switch when..." fails. Different team types face different inertia profiles; a trigger that ignores team type is underspecified.

### R-02 -- Role-level precision

**Pass condition**: Output names specific roles (not "users" or "the team") when attributing failure modes and switching costs. At minimum, the role that owns the workaround (from C-01) appears again when listing failure modes (C-05) and switching costs (C-02).

### R-03 -- At least one cost cited to role

**Pass condition**: At least one switching cost category is explicitly attributed to the role bearing it. "3 days of migration effort for the data-ops team" passes. "3 days of migration effort" without a role attribution fails.

---

## Advanced Criteria

*Structural excellence markers. Each requires a named structural element in the template -- not an output property.*

| ID | Criterion | Category | Points |
|----|-----------|----------|--------|
| A-08 | **FM before DC** | ordering | 5 |
| A-10 | **Fail-first declaration** | ordering | 5 |
| A-11 | **Question-per-criterion mapping** | completeness | 5 |
| A-12 | **BRIDGE dual-closure** | closure | 5 |
| A-13 | **Tabular column schema structural visibility** | format | 5 |
| A-14 | **FM inventory as dedicated named table** | format | 5 |
| A-15 | **Trailing completeness checklist** | verification | 5 |
| A-16 | **FM Inventory primary key constraint declared** | integrity | 5 |
| A-17 | **Question-per-criterion full coverage (all 5 essentials)** | completeness | 5 |
| A-18 | **Trailing checklist binary format and full coverage** | verification | 5 |
| A-19 | **Bidirectional referential integrity enforcement** | integrity | 5 |
| A-20 | **Inline example co-located with unit-bearing column label** | format | 5 |
| A-21 | **Inline falsifiability example in defeat condition threshold column** | format | 5 |
| A-22 | **Mid-template bridge completion status check** | closure | 5 |
| A-23 | **Criterion ID embedded in rule label text** | traceability | 5 |
| A-24 | **Dual-type inline threshold example in DC threshold column label** | format | 5 |
| A-25 | **Active command directive on bridge completion gate** | closure | 5 |
| A-26 | **Analytical axis vocabulary in section heading subtitles** | coherence | 5 |
| A-27 | **Decision-question bridge gate heading** | closure | 5 |
| A-28 | **Criterion ID in trailing checklist item labels** | traceability | 5 |
| A-29 | **Criterion ID in per-criterion authoring prompt label** | traceability | 5 |
| A-30 | **COMMAND-register keyword in per-criterion prompt label** | register | 5 |
| A-31 | **Named structural rule in FAIL-FIRST declaration body** | integrity | 5 |
| A-32 | **Criterion ID in FAIL-FIRST rule label** | traceability | 5 |
| A-33 | **Bridge artifact class named in gate heading interrogative** | closure | 5 |
| A-34 | **Failure-context frame in FM Inventory heading subtitle** | coherence | 5 |
| A-35 | **Blockquote structural delimiter on per-criterion command prompts** | register | 5 |
| A-36 | **Template position index in bridge completion gate heading name** | closure | 5 |
| A-37 | **Organizational schema consistency of position index** | coherence | 5 |
| A-38 | **Compound structural-failure noun form in failure-context frame** | coherence | 5 |
| A-39 | **Cardinality qualifier in bridge artifact class reference** | closure | 5 |
| A-40 | **Engineering-register locus noun in compound failure noun** | coherence | 5 |
| A-41 | **Architectural-scope TYPE component in compound failure noun** | coherence | 5 |
| A-42 | **Domain-prefix vocabulary coherence across all three structural rule labels** | coherence | 5 |
| A-43 | **Verification-action register verb in gate heading interrogative** | closure | 5 |
| A-44 | **Verification-action register in bridge completion status table column label** | closure | 5 |
| A-45 | **Verification-action register in bridge completion command directive** | closure | 5 |
| A-46 | **Bracket-suffix criterion-ID position form in all three structural rule labels** | traceability | 5 |
| A-47 | **RULE as normalized structural noun in all three structural rule labels** | traceability | 5 |
| A-48 | **Adversarial-role frame in FAIL-FIRST heading subtitle** | coherence | 5 |
| A-49 | **Diagnostic-framing claim in FAIL-FIRST declaration body** | coherence | 5 |
| A-50 | **BRIDGE STAGE as dedicated parent container in nested schema** | coherence | 5 |
| A-51 | **VERIFICATION as normalized structural noun in command directive label** | traceability | 5 |

### A-08 -- FM before DC

**Pass condition**: The template enforces positional ordering such that failure modes (C-05) are authored before defeat conditions (C-04). Role ordering, section numbering, or table sequence all satisfy this -- the mechanism is irrelevant as long as an author following the template cannot write DC rows before FM rows.

### A-10 -- Fail-first declaration

**Pass condition**: The template carries an explicit structural label -- "FAIL-FIRST DECLARATION" or equivalent -- as the first named section or block, followed by a one-sentence statement of why failure modes are enumerated before costs and defeat conditions. The label must be a structural element, not a comment or instruction note. Templates where FM content appears first via role ordering without an explicit declaration do not pass; the label is the criterion, not the ordering alone.

### A-11 -- Question-per-criterion mapping

**Pass condition**: The template body contains at least one explicitly labeled question or prompt per essential criterion such that an unanswered prompt is a visible gap during authoring rather than a content gap caught only on full read. Three or more criteria covered qualifies for PARTIAL; all five covered satisfies A-17, not A-11 alone. A-11 PASS requires coverage of at least three essential criteria with named prompts.

### A-12 -- BRIDGE dual-closure

**Pass condition**: The template names two distinct bridge artifacts -- Q3 (or equivalent) closing the FM->actor chain from C-05 to R-02, and Q4 (or equivalent) closing the FM->trigger chain from C-05 to C-04. Each artifact must be named in the template body with an explicit reference to the criterion chain it closes. Column-level closure (FM->actor and FM->trigger as required columns) does not satisfy A-12; the named artifacts and their chain references are the criterion.

### A-13 -- Tabular column schema structural visibility

**Pass condition**: All major output sections use named column schemas such that a blank cell is a visible criterion gap without requiring a full read of prose. At minimum, the FM section and the DC section must be tables with named columns. An output where criterion gaps require reading complete prose to detect fails A-13 regardless of content quality.

### A-14 -- FM inventory as dedicated named table

**Pass condition**: The template contains a titled FM Inventory table (name visible in the output) whose first column assigns FM-[N] identifiers. This table must appear before the Defeat Conditions table in template structure. FM enumerated only in prose blocks, or FM column in a mixed table not dedicated to inventory, does not pass. A-14 implies A-08.

### A-15 -- Trailing completeness checklist

**Pass condition**: The template contains a named trailing section positioned after all content sections, with one verification item per essential criterion. Items may be prose prompts, essay questions, or binary checkboxes -- format is not a criterion here (see A-18). The section must be structurally last and criterion-labeled. A SELF-CHECK block mid-template does not pass; position is the criterion.

### A-16 -- FM Inventory primary key constraint declared

**Pass condition**: The FM Inventory table (from A-14) carries an explicitly stated rule, written in the template body (not in a comment or instructions section), that no FM-[N] identifier may appear in the Defeat Conditions table without a corresponding row in the FM Inventory. The rule must be visible to an author using the template. Templates where the constraint is implied by ordering but not stated fail A-16. A-16 implies A-14.

### A-17 -- Question-per-criterion full coverage (all 5 essentials)

**Pass condition**: The template body contains one explicitly labeled question or prompt for each of the five essential criteria -- C-01, C-02, C-03, C-04, and C-05 -- such that an unanswered prompt for any criterion is a visible gap during authoring. Coverage of fewer than all five fails A-17 regardless of A-11 result. A-17 implies A-11 PASS.

### A-18 -- Trailing checklist binary format and full coverage

**Pass condition**: The trailing checklist (from A-15) satisfies two independent conditions: (1) each item uses binary observable format -- checkbox or Y/N -- not an essay prompt or open-ended question; and (2) all five essential criteria are mapped, one item each, with no essential criterion absent. Failure on either condition is a full fail. A-18 implies A-15 PASS.

### A-19 -- Bidirectional referential integrity enforcement

**Pass condition**: The template enforces the FM-[N] referential integrity rule at both ends of the identifier chain: (1) the source constraint at the FM Inventory (from A-16 -- no FM-[N] may appear downstream without prior row assignment), AND (2) a separately stated referential integrity rule at the DC table definition point, explicitly requiring that every FM-[N] cited in the DC table must have a prior assigned row in the FM Inventory. Both rules must be visible in the template body. A template satisfying A-16 alone passes only the source end; A-19 requires the citation-point rule to be present as a named, separate statement. A-19 implies A-16.

### A-20 -- Inline example co-located with unit-bearing column label

**Pass condition**: Every column label that requires a unit-bearing quantity value (e.g., "Ongoing cost", "Migration effort", "Training overhead", "Frequency") embeds a concrete format example directly within the label definition -- "(e.g., 2 hours/week)", "(e.g., $4,000)", "(e.g., 3 days)" -- such that the format reminder is structurally co-located with the cell the author must fill. A separate "Rules" or "Instructions" block stating that units are required does not satisfy A-20; the example must live in the label. A-20 requires A-13 as a precondition.

### A-21 -- Inline falsifiability example in defeat condition threshold column

**Pass condition**: The Defeat Conditions table contains a column capturing the measurable threshold or falsifiability boundary, and that column label embeds a concrete format example directly within the label definition -- "(e.g., >10MB)", "(e.g., >3 failures/week)", "(e.g., latency >500ms)". Threshold values require a comparison operator + value + unit; a label without an inline example leaves the format undefined at the authoring point. A-21 requires A-13 and A-20 as preconditions.

### A-22 -- Mid-template bridge completion status check

**Pass condition**: The template contains a named verification block positioned between the FM Inventory section and the Defeat Conditions section that explicitly checks whether Q3 and Q4 have been populated. The check must be a structural element -- a named table, checkbox list, or labeled status section -- not a prose comment or authoring note. Templates where bridge artifacts are named in the FAIL-FIRST declaration (A-12) but carry no mid-template gate before the DC section opens do not satisfy A-22; the position between FM and DC is the criterion. A-22 implies A-12.

### A-23 -- Criterion ID embedded in rule label text

**Pass condition**: Every named integrity rule in the template body that enforces a specific advanced criterion carries that criterion's ID within the label text -- either as a bracket prefix (e.g., "[A-16 PRIMARY KEY RULE]"), a bracket suffix (e.g., "PRIMARY KEY CONSTRAINT [A-16]"), or an inline reference (e.g., "REFERENTIAL INTEGRITY RULE (citation point) [A-19]"). At minimum, the A-16 source rule and the A-19 citation rule must each carry their criterion IDs in the label. A rule label that names the constraint without its criterion ID fails A-23. IDs in comments, footnotes, or a separate mapping table do not satisfy A-23; the ID must be in the label of the rule itself. Domain-prefix form is valid (e.g., `STATUS QUO LOCK RULE [A-16]`): the domain vocabulary prefix does not displace the criterion ID requirement. A-23 requires A-19 as a precondition. A-23 implies A-19.

### A-24 -- Dual-type inline threshold example in DC threshold column label

**Pass condition**: The DC threshold column label (from A-21) embeds at least two inline examples of structurally distinct threshold types -- different units and different comparison contexts -- within the same label definition. For example, "(e.g., >10MB, >3 failures/week)" provides one size-based threshold and one frequency-based threshold. A single example satisfies A-21 but fails A-24; two examples of the same type also fail A-24 -- distinctness requires different unit families or comparison contexts. A-24 requires A-21 as a precondition. A-24 implies A-21.

### A-25 -- Active command directive on bridge completion gate

**Pass condition**: The bridge completion gate block (from A-22) carries an explicit active command directive as a named element -- not only a Y/N status table but also a labeled instruction that tells the author to complete Q3 and Q4 before proceeding. The directive must be a named structural element (e.g., "[BRIDGE COMPLETION COMMAND]", "COMPLETE Q3 AND Q4 BEFORE PROCEEDING", "ACTION REQUIRED: COMPLETE BRIDGE ARTIFACTS") visible at the gate position. A command in a separate prose block, comment, or authoring note does not satisfy A-25 -- the directive must be co-located with the status table at the gate position. A-25 implies A-22.

### A-26 -- Analytical axis vocabulary in section heading subtitles

**Pass condition**: The template's declared analytical axis vocabulary appears in the subtitle text of at least two major section headings -- specifically the FAIL-FIRST declaration heading and the FM Inventory heading. Both headings must carry a subtitle phrase drawn from the axis vocabulary (e.g., a status-quo competitor axis yields "-- THE UNNAMED COMPETITOR" on the FAIL-FIRST heading and "-- THE STATUS QUO'S VULNERABILITIES:" on the FM Inventory heading). A heading that uses only generic structural labels ("FAIL-FIRST DECLARATION", "FAILURE MODE INVENTORY") satisfies A-10 and A-14 respectively but fails A-26. The axis vocabulary must appear in the heading line itself -- not in a prose block, sub-heading, or content cell below the heading. A-26 implies A-10 and A-14.

### A-27 -- Decision-question bridge gate heading

**Pass condition**: The bridge completion gate block's section heading (from A-22) carries an explicit binary decision question as part of the heading line -- appended via separator, colon, or embedded phrasing -- such that the gate's pass/fail nature is visible in the document heading structure without reading the block's body. Interrogative forms satisfy: "-- READY TO PROCEED?", "-- ALL ARTIFACTS COMPLETE?", "-- PASS BEFORE CONTINUING?". The question must be in the heading line of the gate block, not in a sub-element, label, or row inside the block. A gate heading of "BRIDGE COMPLETION GATE" satisfies A-22; a heading of "BRIDGE COMPLETION GATE -- READY TO PROCEED?" satisfies A-27. A-27 is independent of A-25. A-27 implies A-22.

### A-28 -- Criterion ID in trailing checklist item labels

**Pass condition**: Each item in the trailing completeness checklist (from A-18) carries its essential criterion ID (C-01 through C-05) in the item label, enabling direct rubric traceability from each verification item to its criterion without external reference. An item labeled "C-01: Workaround named specifically (Y/N)" satisfies A-28; an item labeled "Workaround named specifically (Y/N)" fails even if all five criteria are covered and binary format is present. The criterion ID must appear in the item label itself -- not in a separate legend, header row, or column annotation. A-28 implies A-18.

### A-29 -- Criterion ID in per-criterion authoring prompt label

**Pass condition**: Each per-criterion authoring prompt (from A-17) carries its essential criterion ID (C-01 through C-05) in the prompt label, so the author sees the criterion ID at the point of authoring. An item labeled `[C-01 COMMAND]: NAME the specific unnamed competitor...` satisfies A-29; an item labeled `> **question**: Name the workaround` fails even if all five prompts are present and labeled. The criterion ID must appear in the prompt label itself. A-29 implies A-17.

### A-30 -- COMMAND-register keyword in per-criterion prompt label

**Pass condition**: Each per-criterion authoring prompt label (from A-29) carries the COMMAND register keyword -- the word "COMMAND" appearing as a named element within the bracket-label form -- making the directive nature of the prompt structurally explicit. A label of `[C-01 COMMAND]:` satisfies A-30; a label of `[C-01 QUESTION]:` or `C-01:` satisfies A-29 but fails A-30. The COMMAND keyword must appear in the prompt label, not in the prompt body text. A-30 implies A-29.

### A-31 -- Named structural rule in FAIL-FIRST declaration body

**Pass condition**: The body of the FAIL-FIRST declaration section (from A-10) carries a named rule label -- a discrete, labeled rule element within the section body (not only the section heading) -- that states the FAIL-FIRST principle as a named structural constraint. A named rule element such as `[FAIL-FIRST RULE]`, `FAIL-FIRST CONSTRAINT [A-31]`, or `[A-31 FAIL-FIRST ORDERING RULE]` satisfies A-31; a FAIL-FIRST section that carries only a heading and prose explanation without a named rule label does not pass. A-31 implies A-10.

### A-32 -- Criterion ID in FAIL-FIRST rule label

**Pass condition**: The named rule label in the FAIL-FIRST declaration body (from A-31) carries the A-31 criterion ID within its label text -- bracket prefix, bracket suffix, or inline form -- completing A-23's criterion-ID-in-label traceability across all three named structural rules: the A-16 FM Inventory primary key rule, the A-19 DC citation rule, and the A-31 FAIL-FIRST rule. A rule labeled `[FAIL-FIRST RULE]` satisfies A-31 but fails A-32; a rule labeled `FAIL-FIRST CONSTRAINT [A-31]` satisfies both. The criterion ID must appear in the rule label itself. A-32 requires A-31 as a precondition. A-32 implies A-31 and extends A-23 universally.

### A-33 -- Bridge artifact class named in gate heading interrogative

**Pass condition**: The gate heading interrogative (from A-27) explicitly names the bridge artifact class within the question text, making the heading self-contextualizing about what must be complete, not only whether to proceed. A heading interrogative of "ALL BRIDGE ARTIFACTS COMPLETE?" satisfies A-33; an interrogative of "READY TO PROCEED?" satisfies A-27 but fails A-33. The artifact class name must appear in the heading line itself. A-33 implies A-27.

### A-34 -- Failure-context frame in FM Inventory heading subtitle

**Pass condition**: The FM Inventory heading subtitle (from A-26) encodes not only the analytical axis vocabulary but also a failure-context frame -- a phrase that identifies the analytical purpose of the section as the place where the axis subject fails, breaks, or exhibits structural weakness. A heading subtitle of "THE INERTIA THREAT'S STRUCTURAL WEAKNESSES" satisfies A-34. A subtitle of "THE STATUS QUO" satisfies A-26 but fails A-34. The failure-context frame must appear in the FM Inventory heading line itself. A-34 applies specifically to the FM Inventory heading; the FAIL-FIRST heading satisfies A-26 with axis vocabulary alone and is not required to carry a failure-context frame. A-34 implies A-26; A-26 does not imply A-34.

### A-35 -- Blockquote structural delimiter on per-criterion command prompts

**Pass condition**: Each per-criterion authoring command prompt (from A-30) uses a blockquote structural delimiter -- Markdown `>` prefix or equivalent visual structural isolation mechanism -- so that the command prompt forms a structurally distinct block in the template document rather than an inline label element. A prompt of `> [C-01 COMMAND]: NAME the specific unnamed competitor...` satisfies A-35; an inline prompt `[C-01 COMMAND]: NAME...` satisfies A-30 but fails A-35. All five per-criterion command prompts (C-01 through C-05) must use the blockquote delimiter; partial blockquote coverage fails A-35. A-35 implies A-30.

### A-36 -- Template position index in bridge completion gate heading name

**Pass condition**: The bridge completion gate heading name -- the portion of the gate heading before any `--` separator -- carries a structural position index that self-locates the gate within the template's organizational hierarchy: a stage number (e.g., "STAGE 2"), a section number (e.g., "SECTION 3"), or equivalent sequence label. A gate named "STAGE 2 COMPLETION GATE -- ALL BRIDGE ARTIFACTS COMPLETE?" satisfies A-36. A gate named "BRIDGE COMPLETION GATE -- ALL BRIDGE ARTIFACTS COMPLETE?" fails A-36. The position index must appear in the gate heading name line itself. A-36 is independent of A-33. A-36 implies A-27; A-27 does not imply A-36.

### A-37 -- Organizational schema consistency of position index

**Pass condition**: The structural position index in the bridge completion gate heading name (from A-36) uses the same organizational nomenclature used throughout the rest of the template's section/stage hierarchy. If the template labels its sections SECTION 1, SECTION 2, ..., SECTION N, the gate heading must carry a "SECTION N" index. If the template labels STAGE 1, STAGE 2, ..., STAGE N, the gate heading must carry a "STAGE N" index. Mixed nomenclature fails A-37. Schema consistency ensures that an author navigating the template by its established organizational vocabulary can locate the gate by its heading name without resolving a naming discrepancy. A-37 requires a whole-template property -- the index nomenclature must match across the heading and all other sections. A-37 implies A-36; A-36 does not imply A-37.

### A-38 -- Compound structural-failure noun form in failure-context frame

**Pass condition**: The failure-context frame in the FM Inventory heading subtitle (from A-34) takes the form of a compound structural-failure noun -- a noun phrase that encodes both a failure TYPE and a failure LOCUS simultaneously. Examples of passing forms: "STRUCTURAL WEAKNESSES" (type = structural, locus = weakness points); "FAILURE SURFACE" (type = failure, locus = surface); "FAILURE POINTS" (type = failure, locus = specific points). A verb construction such as "WHERE THE STATUS QUO BREAKS" satisfies A-34 but fails A-38: the frame uses a verb-clause construction rather than a compound noun. The compound noun must appear in the FM Inventory heading line itself. A-38 implies A-34; A-34 does not imply A-38.

### A-39 -- Cardinality qualifier in bridge artifact class reference

**Pass condition**: The gate heading interrogative (from A-33) carries an explicit cardinality quantifier alongside the bridge artifact class name, confirming the required COUNT of artifacts at the gate. The quantifier must be a universal or dual quantifier: ALL (universal), BOTH (dual), EACH (distributive). An interrogative of "ALL BRIDGE ARTIFACTS COMPLETE?" satisfies A-39; an interrogative of "BRIDGE ARTIFACTS COMPLETE?" names the class but carries no cardinality quantifier. The cardinality quantifier must appear in the gate heading interrogative itself. A-39 implies A-33; A-33 does not imply A-39.

### A-40 -- Engineering-register locus noun in compound failure noun

**Pass condition**: The LOCUS component of the compound structural-failure noun (from A-38) is drawn from engineering fault taxonomy vocabulary -- a term that names the specific defect locus with the precision used in fault-tree analysis or FMEA methodology. Engineering-register locus terms: FAULTS, FAILURE PLANES, FRACTURE ZONES, DEFECT LOCI. General-register locus terms that pass A-38 but fail A-40: WEAKNESSES, VULNERABILITIES, GAPS, PROBLEMS. "STRUCTURAL FAULTS" satisfies A-40 (FAULTS = specific defect planes, engineering register); "STRUCTURAL WEAKNESSES" satisfies A-38 but fails A-40. The LOCUS must appear in the FM Inventory heading compound noun. A-40 implies A-38; A-38 does not imply A-40. Confirmed by R16 V-02.

### A-41 -- Architectural-scope TYPE component in compound failure noun

**Pass condition**: The TYPE component of the compound structural-failure noun (from A-38) names an architectural or systemic scope -- a category that classifies the FM Inventory's contents at the architectural level of abstraction. Architectural-scope TYPE terms: STRUCTURAL, SYSTEMIC, ARCHITECTURAL, FOUNDATIONAL. Event-descriptor TYPE terms that pass A-38 but fail A-41: FAILURE, ERROR, DEFECT, COLLAPSE. "STRUCTURAL FAULTS" satisfies A-41 (STRUCTURAL = architectural scope). "FAILURE SURFACE" fails A-41 (FAILURE = event descriptor). A-41 implies A-38; A-38 does not imply A-41. A-40 and A-41 are independent. Confirmed by R16 V-01 and V-02.

### A-42 -- Domain-prefix vocabulary coherence across all three structural rule labels

**Pass condition**: All three named structural rule labels in the template body -- the A-16 FM Inventory primary key rule, the A-19 DC citation rule, and the A-31 FAIL-FIRST rule -- share a common domain-prefix vocabulary drawn from the template's declared analytical axis vocabulary. The domain prefix must be a noun or noun phrase identifying the analytical subject (e.g., "INERTIA THREAT", "STATUS QUO", "COMPETITOR LOCK"), appearing at the start of all three rule labels before the structural descriptor. Examples of passing forms: `INERTIA THREAT RULE [A-16]`, `INERTIA THREAT CITATION RULE [A-19]`, `INERTIA THREAT FAIL-FIRST RULE [A-31]`. Partial coherence (two of three sharing a prefix, one distinct) fails A-42. A-42 is the rule-label analogue of A-37. A-42 implies A-23; A-23 does not imply A-42. Confirmed by R17 V-03.

### A-43 -- Verification-action register verb in gate heading interrogative

**Pass condition**: The gate heading interrogative (from A-39) uses a verb drawn from verification-action vocabulary -- a verb that signals active per-artifact epistemic review rather than passive confirmation of completion state. Verification-action verbs: VERIFIED, CONFIRMED, VALIDATED, CHECKED. Completion-state verbs that satisfy A-39 but fail A-43: COMPLETE, BUILT, DONE, READY, PRESENT. A gate heading of `ALL BRIDGE ARTIFACTS COMPLETE?` satisfies A-39 but fails A-43. A gate heading of `EACH BRIDGE ARTIFACT VERIFIED?` satisfies A-43. A-43 does not require a specific cardinality quantifier; any valid A-39 quantifier combined with a verification-action verb satisfies A-43. A-43 implies A-39; A-39 does not imply A-43. Confirmed by R17 V-03 and R18 V-01.

### A-44 -- Verification-action register in bridge completion status table column label

**Pass condition**: The bridge completion gate's status table (from A-22) uses a verification-action verb as the column label for the artifact status check column. The column label must be drawn from verification-action vocabulary (VERIFIED?, CONFIRMED?, VALIDATED?, CHECKED?) rather than completion-state vocabulary (BUILT?, COMPLETE?, DONE?, READY?). A status table column labeled "BUILT?" satisfies A-22 but fails A-44. A status table column labeled "VERIFIED?" satisfies A-44. The register requirement applies to the column label itself -- not to the Y/N cell values, the gate block heading, or the command directive. A-44 implies A-43 and A-22; A-22 and A-43 together do not imply A-44. Confirmed by R18 V-01.

### A-45 -- Verification-action register in bridge completion command directive

**Pass condition**: The bridge completion gate's command directive (from A-25) uses a verb or label element drawn from verification-action vocabulary. The register requirement may be satisfied by the command directive label (e.g., "[BRIDGE VERIFICATION COMMAND]", "[VERIFY ARTIFACTS COMMAND]") or by an imperative verification-action verb in the directive body text (e.g., "VERIFY each bridge artifact before proceeding", "CONFIRM Q3 AND Q4 BEFORE CONTINUING"). Completion-state vocabulary fails A-45: a directive labeled "[BRIDGE COMPLETION COMMAND]" satisfies A-25 but fails A-45. A-45 implies A-43 and A-25; A-25 alone does not imply A-45. Confirmed by R18 V-01.

### A-46 -- Bracket-suffix criterion-ID position form in all three structural rule labels

**Pass condition**: All three named structural rule labels in the template body (the A-16 FM Inventory primary key rule, the A-19 DC citation rule, and the A-31 FAIL-FIRST rule) use the bracket-suffix position form for the criterion ID -- the ID appears as the terminal element of each label, in brackets, after the structural descriptor: `[DOMAIN PREFIX] [STRUCTURAL DESCRIPTOR] [CRITERION-ID]`. Examples of passing forms: `INERTIA THREAT RULE [A-16]`, `INERTIA THREAT CITATION RULE [A-19]`, `INERTIA THREAT FAIL-FIRST RULE [A-31]`. Examples of failing forms: `[A-16] INERTIA THREAT RULE` (bracket-prefix); `INERTIA THREAT [A-16] RULE` (inline before structural noun). Partial compliance -- two of three labels using bracket-suffix, one using bracket-prefix -- fails A-46. A-46 implies A-23; A-23 does not imply A-46. Confirmed by R19 evidence.

### A-47 -- RULE as normalized structural noun in all three structural rule labels

**Pass condition**: All three named structural rule labels in the template body (A-16, A-19, A-31) use RULE as the structural noun -- positioned between the domain prefix and the criterion ID. The structural noun RULE is normalized because it is the shortest, most semantically direct single word that names a prescriptive statement without importing domain vocabulary: CONSTRAINT imports relational-database schema vocabulary; LOCK imports concurrency semantics; RESTRICTION imports access-control domain; REQUIREMENT imports requirements-engineering register. A template using `INERTIA THREAT CITATION CONSTRAINT [A-19]` satisfies A-42 and A-46 but fails A-47. When A-47 is satisfied alongside A-42 and A-46, each rule label follows the fully normalized three-part schema: `[AXIS-SUBJECT] [ROLE-DESCRIPTOR] RULE [CRITERION-ID]` in fixed positional order. A-47 implies A-46; A-46 does not imply A-47. Confirmed by R19 evidence.

### A-48 -- Adversarial-role frame in FAIL-FIRST heading subtitle

**Pass condition**: The FAIL-FIRST declaration heading subtitle (from A-26) assigns the axis subject an explicit competitive-adversary role using an "AS [COMPETITIVE ROLE]" construction -- naming not only the axis subject but its function as an active competitive threat actor in the decision context. Examples of passing forms: `-- THE STATUS QUO AS UNNAMED COMPETITOR` (assigns the status quo the role of a competitor that has never had to identify itself as one); `-- THE INCUMBENT AS INVISIBLE COMPETITOR` (assigns the incumbent the role of a competitor whose presence is obscured by familiarity); `-- THE DEFAULT OPTION AS PRESUMPTIVE WINNER` (assigns the default option the role of a competitor that wins by absence of contest rather than merit). A heading subtitle that carries axis vocabulary (satisfying A-26) but omits the role-assignment construction -- e.g., "-- THE STATUS QUO" or "-- THE UNNAMED COMPETITOR" -- fails A-48: the axis subject is named but not assigned an adversarial competitive role. The role-assignment construction must appear in the FAIL-FIRST heading subtitle specifically; axis vocabulary in other headings does not satisfy A-48. The "AS [ROLE]" construction assigns the axis subject a functional identity as a competitive agent, making explicit what the FAIL-FIRST section asserts implicitly: the axis subject is a structural competitor to the feature, not a neutral status indicator. A-48 implies A-26; A-26 does not imply A-48. Confirmed by R20 V-02 (`THE STATUS QUO AS UNNAMED COMPETITOR`).

### A-49 -- Diagnostic-framing claim in FAIL-FIRST declaration body

**Pass condition**: The body of the FAIL-FIRST declaration section (from A-31) carries a brief diagnostic claim -- a short phrase or labeled assertion that names the structural bias or behavioral mode exhibited by the axis subject, explaining WHY it must be analyzed under FAIL-FIRST ordering -- in addition to the structural rule label required by A-31. The diagnostic claim is not a rule statement (it does not prescribe authoring behavior) but an analytical label (it characterizes the axis subject's epistemic character in the decision context). Examples of passing forms: `advocacy, not analysis` (STATUS QUO axis -- names the STATUS QUO's structural bias as self-serving advocacy rather than honest option evaluation); `presumptive default, not earned choice` (DEFAULT OPTION axis -- names the DEFAULT OPTION's structural bias as unexamined continuation rather than a decision actively made); `incumbent protection, not competitive evaluation` (INCUMBENT axis -- names the INCUMBENT's structural bias as institutional self-preservation rather than merit-based comparison). The diagnostic claim must appear as a distinct named or labeled element in the FAIL-FIRST declaration body -- not in the rule label itself, not in the section heading, and not as an unlabeled prose sentence. A template satisfying A-31 (named structural rule in body) may carry a diagnostic claim as part of the rule body text but fails A-49 unless the diagnostic claim is separately identifiable as a structural element alongside the rule label. A-49 implies A-31; A-31 does not imply A-49. A-48 and A-49 are independent: A-48 upgrades the FAIL-FIRST heading subtitle with a role-assignment construction; A-49 upgrades the FAIL-FIRST body with a diagnostic claim beyond the rule label. Both can be satisfied or failed independently. Confirmed by R20 V-02 (`advocacy, not analysis` alongside the STATUS QUO structural rule).

### A-50 -- BRIDGE STAGE as dedicated parent container in nested schema

**Pass condition**: In a STAGE-organized template, the bridge artifacts (Q3 and Q4) and the completion gate all reside within a single dedicated named parent STAGE that serves solely as the bridge phase container -- a STAGE whose structural purpose in the template hierarchy is to contain the bridge phase as a first-class unit. The parent STAGE must be explicitly named as a BRIDGE STAGE (e.g., "STAGE 2 BRIDGE STAGE", "STAGE 3 -- BRIDGE PHASE") and contain Q3, Q4, and the gate as nested sub-elements. Examples of passing form: STAGE 1 (FM Inventory) → STAGE 2 BRIDGE STAGE (contains Q3, Q4, and gate) → STAGE 3 (DC table) -- the bridge phase occupies STAGE 2 as its sole parent, and the STAGE 2 heading identifies it as the bridge phase container. Examples of failing form: Q3 and Q4 appear as independent stages at the top level (STAGE 3: Q3, STAGE 4: Q4) with the gate as a separate subsequent stage -- no dedicated parent container encloses all three. A template where Q3, Q4, and the gate are each independent STAGE-level elements satisfies A-37 (schema consistency of the gate's position index) but fails A-50 (no dedicated parent container). A SECTION-flat template cannot satisfy A-50 without adopting nested STAGE containment for the bridge phase -- A-50 requires the nested STAGE schema as a structural precondition. A-50 implies A-37; A-37 does not imply A-50. Confirmed by R20 V-03 (STAGE 2 BRIDGE STAGE containing Q3/Q4/gate as nested sub-elements).

### A-51 -- VERIFICATION as normalized structural noun in command directive label

**Pass condition**: The bridge completion gate's command directive label (from A-25) uses VERIFICATION as its structural type noun -- the single word that names the epistemological category of the required action in the directive label. The normalized form is `[BRIDGE VERIFICATION COMMAND]`: (artifact class)(action type = VERIFICATION)(directive type = COMMAND). Examples of passing label forms: `[BRIDGE VERIFICATION COMMAND]`, `[ARTIFACT VERIFICATION COMMAND]`, `[Q3/Q4 VERIFICATION COMMAND]` -- all use VERIFICATION as the structural noun naming the action type. Examples of failing label forms: `[BRIDGE CONFIRMATION COMMAND]` (CONFIRMATION names a one-time epistemic act, not the verification category -- fails A-51 even though CONFIRMED is a valid A-43 verification-action verb); `[BRIDGE VERIFY COMMAND]` (VERIFY is an imperative verb form, not a structural noun form appropriate for label vocabulary); `[BRIDGE COMPLETION COMMAND]` (COMPLETION = completion-state, fails A-45 and A-51); `[BRIDGE CHECKING COMMAND]` (CHECKING lacks the same categorical precision as VERIFICATION). VERIFICATION is the normalized form because it is the gerund/noun form of the epistemological category -- active review against a standard -- that names what the gate requires, in a structural noun form appropriate for label vocabulary, without importing action-specific vocabulary that varies by axis (CONFIRM vs. VERIFY vs. VALIDATE). The body of the directive may use any verification-action imperative verb (CONFIRM, VERIFY, VALIDATE, CHECK) without violating A-51 -- the normalization constraint applies only to the structural noun in the label. When A-51 is satisfied, the command directive achieves a label/body split: the label carries the categorical type (VERIFICATION) and the body carries the specific action verb (CONFIRM, VERIFY), creating complementarity rather than redundancy between the two register sites. A-51 is the command-directive analogue of A-47 (RULE as normalized structural noun in rule labels): both require a specific, semantically direct noun to name the element type in its label position, independent of the action-register vocabulary used elsewhere in the element. A-51 implies A-45; A-45 does not imply A-51. Confirmed by R20 V-04 (`[BRIDGE VERIFICATION COMMAND]` with body verb CONFIRM -- label/body register complementarity with VERIFICATION as the normalized label noun regardless of body verb choice).

---

## Implication Chain

| Chain | Direction |
|-------|-----------|
| A-51 implies A-45 implies A-43 implies A-39 implies A-33 implies A-27 implies A-22 implies A-12 | closure chain (normalized VERIFICATION label, command directive) |
| A-51 implies A-45 implies A-25 implies A-22 implies A-12 | command directive chain (extended) |
| A-50 implies A-37 implies A-36 implies A-27 implies A-22 implies A-12 | closure chain (BRIDGE STAGE parent container) |
| A-49 implies A-31 implies A-10 | FAIL-FIRST body diagnostic chain |
| A-48 implies A-26 implies A-10 and A-14 | FAIL-FIRST heading adversarial-role chain |
| A-47 implies A-46 implies A-23 implies A-19 implies A-16 implies A-14 implies A-08 | rule-label normalization chain |
| A-46 implies A-23 implies A-19 implies A-16 implies A-14 implies A-08 | rule-label position chain |
| A-45 implies A-43 implies A-39 implies A-33 implies A-27 implies A-22 implies A-12 | closure chain (verification-action command directive) |
| A-45 implies A-25 implies A-22 implies A-12 | command directive chain (extended) |
| A-44 implies A-43 implies A-39 implies A-33 implies A-27 implies A-22 implies A-12 | closure chain (verification-action status column) |
| A-44 implies A-22 implies A-12 | gate status chain |
| A-43 implies A-39 implies A-33 implies A-27 implies A-22 implies A-12 | closure chain (verification-action gate) |
| A-42 implies A-23 implies A-19 implies A-16 implies A-14 implies A-08 | traceability-to-integrity bridge (domain-prefix coherence) |
| A-41 implies A-38 implies A-34 implies A-26 implies A-10 and A-14 | coherence chain (architectural-scope TYPE) |
| A-40 implies A-38 implies A-34 implies A-26 implies A-10 and A-14 | coherence chain (engineering-register locus) |
| A-39 implies A-33 implies A-27 implies A-22 implies A-12 | closure chain (cardinality-qualified artifact gate) |
| A-38 implies A-34 implies A-26 implies A-10 and A-14 | coherence chain (compound failure noun) |
| A-37 implies A-36 implies A-27 implies A-22 implies A-12 | closure chain (schema-consistent position index) |
| A-36 implies A-27 implies A-22 implies A-12 | closure chain (position-indexed gate) |
| A-35 implies A-30 implies A-29 implies A-17 implies A-11 | authoring-prompt chain (extended) |
| A-34 implies A-26 implies A-10 and A-14 | coherence chain (failure-context frame) |
| A-33 implies A-27 implies A-22 implies A-12 | closure chain (artifact-named heading) |
| A-32 implies A-31 implies A-10 | fail-first traceability chain |
| A-32 implies A-23 implies A-19 | traceability-to-integrity bridge |
| A-30 implies A-29 implies A-17 implies A-11 | authoring-prompt chain |
| A-28 implies A-18 implies A-15 | verification chain |
| A-25 implies A-22 implies A-12 | closure chain (command directive) |
| A-24 implies A-21 implies A-20 and A-13 | format chain |
| A-23 implies A-19 implies A-16 implies A-14 implies A-08 | integrity chain |
| A-26 implies A-10 and A-14 | coherence chain |
| A-17 implies A-11 | completeness chain |
