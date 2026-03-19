**rhythm-behavior R15 scored.** Scorecard written to `simulations/quest/scorecards/rhythm-behavior-scorecard-R15-2026-03-17.md`.

---

### Results

| Variation | Essential | Recommended | Aspirational | Composite | Golden |
|-----------|-----------|-------------|--------------|-----------|--------|
| V-01 | 4/4 | 3/3 | 29/29 | **100** | YES |
| V-02 | 4/4 | 3/3 | 29/29 | **100** | YES |
| V-03 | 4/4 | 3/3 | 29/29 | **100** | YES |
| V-04 | 4/4 | 3/3 | 29/29 | **100** | YES |
| V-05 | 4/4 | 3/3 | 29/29 | **100** | YES |

**5/5 golden** -- all predictions confirmed.

---

### Open Questions Resolved

| Question | V | Result |
|----------|---|--------|
| Does descriptive register at the inter-section peer slot satisfy C-22? | V-02 | YES |
| Does C-38 cover the cross-register case (descriptive first, imperative subsequent)? | V-03 | YES |
| Does C-33 + C-34 cover imperative first + descriptive subsequent? | V-04 | YES |
| Does inertness extend across position types? | V-05 | YES |

---

### New Criteria Confirmed (R15)

- **C-44** (V-02): Descriptive register at the inter-section peer slot is a qualifying position for C-22 -- closes the last untested cell in the position-type x register matrix.
- **C-45** (V-03): Mixed-register dual section-body (descriptive first, imperative subsequent) composes without interaction -- C-38's "any subsequent" clause is register-unrestricted.
- **C-46** (V-04): Mixed-register dual section-body (imperative first, descriptive subsequent) composes without interaction -- C-33 + C-34 cover the reverse complement.
- **C-47** (V-05): Cross-type dual placement (section body + inter-section peer slot, descriptive) composes without interaction -- inertness principle is position-type-agnostic.

v16 denominator: **40**.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Inertness principle extends across position types: section body (descriptive, first qualifying) + inter-section peer slot (descriptive, second qualifying) composes without interaction -- the general first-qualifying-occurrence satisfies; subsequent are inert principle is position-type-agnostic (V-05)", "Descriptive register at inter-section peer slot is a qualifying first occurrence for C-22 -- C-34 register invariance + C-23 isolation primacy close the last untested cell in the position-type x register matrix (V-02)", "C-38 any-subsequent-qualifying-placement clause is register-unrestricted: descriptive first + imperative subsequent dual section-body composes without interaction (V-03)", "C-33 + C-34 cover the reverse complement: imperative first + descriptive subsequent dual section-body; both register orderings absorbed without new criteria (V-04)"]}
```
 -- Production Baseline at 36/36 (Lifecycle Emphasis, Reconfirmation)

Rule form: `**Axis-Header Rule**: Each gate header names its axis.` in the inter-section peer slot between Synthesis and Consolidated Findings, flanked by `---` dividers. Single placement. All elements in imperative register. Identical to R14 V-01. Purpose: denominator transition verification (33->36) under v15.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | "Sections in this exact order: flow-lifecycle, flow-conversation, trace-state, trace-contract, trace-permissions, SYNTHESIS, Consolidated Findings." Declared before any findings. |
| C-02 | PASS | "Write everything as one document from start to finish. Do not promise to continue." |
| C-03 | PASS | Sort label "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW" structurally adjacent to sort instruction. |
| C-04 | PASS | spec-gap and contract-violation defined; Coverage Axis Gate checks both with correction loop. |
| C-05 | PASS | Table pre-opened with Sub-Skill column; rows appended immediately at discovery. |
| C-06 | PASS | "one concrete next step naming the exact spec section, boundary, or component a developer must address before writing the first line of implementation code." |
| C-07 | PASS | "If a phase has no findings, say so briefly." / "If none: say so explicitly." |
| C-08 | PASS | Rationale column pre-opened; required for every row; 3-slot template + inline example. |
| C-09 | PASS | SYNTHESIS section with full CROSS-SKILL instructions and table insertion. |
| C-10 | PASS | Label structurally adjacent to sorted table. |
| C-11 | PASS | Coverage Axis Gate checks both finding types with correction loop. |
| C-12 | PASS | Table opened before flow-lifecycle; rows appended at discovery. |
| C-13 | PASS | SYNTHESIS isolated between trace-permissions and Consolidated Findings dividers. |
| C-14 | PASS | Rationale column pre-opened before first sub-skill. |
| C-15 | PASS | CROSS-SKILL insertion into table; Coverage summary CROSS-SKILL row. |
| C-16 | PASS | Template + inline Example in "What to look for"; Format Axis Gate reiterates. |
| C-17 | PASS | No-downgrade rule + "Inherited [LEVEL] from [sub-skill-X] ([F-ID])" + Inheritance Axis Gate. |
| C-18 | PASS | Three gates each with independent correction loop. |
| C-19 | PASS | Three gates, one axis each, none merged. |
| C-20 | PASS | "add", "rewrite", "fix" -- each names axis target explicitly. |
| C-21 | PASS | "Coverage Axis Gate", "Format Axis Gate", "Inheritance Axis Gate" -- axis in header token. |
| C-22 | PASS | Labeled paragraph in confirmed inter-section peer slot; flanked by `---` dividers. |
| C-23 | PASS | Inter-section peer slot physically isolated from gate bodies and example blocks. |
| C-24 | PASS | Inter-section peer slot is a confirmed qualifying position. |
| C-25 | PASS | Rule in confirmed position; C-25 trivially inapplicable. |
| C-26 | PASS | Rule not in named section body; C-26 trivially inapplicable. |
| C-27 | PASS | Template + inline example; slot-name def lines absent and not required. |
| C-28 | PASS | Inline example present. |
| C-29 | PASS | Example present; C-29 inapplicable. |
| C-30 | PASS | Rule not at earliest inter-section gap; C-30 inapplicable. |
| C-31 | PASS | Rule not in named section body; C-31 trivially inapplicable. |
| C-32 | PASS | Closure confirmed by R12-R14; no additional per-body confirmation required. |
| C-33 | PASS | Single placement; dual-body inertness trivially inapplicable. |
| C-34 | PASS | Imperative register; all structural elements present. |
| C-35 | PASS | Rule not in any section body; C-35 trivially inapplicable. |
| C-36 | PASS | Neither descriptive register nor section-body placement in use; trivially inapplicable. |
| C-37 | PASS | Single placement; inertness rule (N>=2) trivially inapplicable. |
| C-38 | PASS | No dual section-body descriptive placement; C-38 trivially inapplicable. |
| C-39 | PASS | No multiple section-body placements in descriptive; C-39 trivially inapplicable. |
| C-40 | PASS | Single placement (N=1); C-40 fires on N>=4 confirmations. Trivially inapplicable. |
| C-41 | PASS | No N=6 section-body composition; rule is at inter-section peer slot. C-41 fires only on placements including Synthesis body as 6th section-body position. Trivially inapplicable. |
| C-42 | PASS | No descriptive N=4 or N=5 section-body composition. Trivially inapplicable. |
| C-43 | PASS | No descriptive + N=6 composition. Trivially inapplicable. |

**V-01 score: 36/36 = 100. GOLDEN.**

---

#### V-02 -- Descriptive Register + Inter-Section Peer Slot (Register, Single Axis)

Rule form: bare standalone descriptive sentence "Each closing confirmation gate header names its axis." in the canonical inter-section peer slot between Synthesis and Consolidated Findings, flanked by `---` dividers. Single placement. Entire prompt in descriptive register. First test of descriptive register at the inter-section peer slot.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | "The report proceeds through these sections in sequence: flow-lifecycle, flow-conversation, trace-state, trace-contract, trace-permissions, SYNTHESIS, Consolidated Findings." Declared before findings. |
| C-02 | PASS | "The entire report is produced as one document from start to finish, without any promise of continuation." |
| C-03 | PASS | Sort label "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW" present. |
| C-04 | PASS | spec-gap and contract-violation defined; Coverage Axis Gate confirms both with correction instruction. |
| C-05 | PASS | Table pre-opened; rows appended as discovered; Sub-Skill column present. |
| C-06 | PASS | "Top finding: a concrete next step naming the exact spec section, boundary, or component a developer must address before writing any implementation code." |
| C-07 | PASS | "Any phase that produces no findings is noted as such." / "If this section produces no findings, that is stated explicitly." -- descriptive form per C-34. |
| C-08 | PASS | Rationale column pre-opened; 3-slot template + inline example present. |
| C-09 | PASS | SYNTHESIS section with full CROSS-SKILL instructions and table insertion. |
| C-10 | PASS | Sort label structurally adjacent. |
| C-11 | PASS | Coverage Axis Gate checks both types with correction instruction. |
| C-12 | PASS | Table opened before flow-lifecycle; rows appended at discovery. |
| C-13 | PASS | Synthesis isolated between trace-permissions and Consolidated Findings dividers. |
| C-14 | PASS | Rationale column pre-opened. |
| C-15 | PASS | CROSS-SKILL insertion into table; Coverage summary CROSS-SKILL row. |
| C-16 | PASS | Template string + inline Example present in "What to look for"; Format Axis Gate enforces with slot structure. |
| C-17 | PASS | No-downgrade rule + provenance form "Inherited [LEVEL] from [sub-skill-X] ([F-ID])" + Inheritance Axis Gate. |
| C-18 | PASS | Three gates each with independent correction instruction (descriptive form per C-34). |
| C-19 | PASS | Three gates, one axis each, not merged. |
| C-20 | PASS | Descriptive axis-named repair instructions: "add the missing finding before proceeding to the Format Axis Gate" (coverage), "rewritten using the [LEVEL] / [boundary] / [caller/component] / [effect] structure" (format), "has its CROSS-SKILL blast radius and provenance annotation corrected before closing" (inheritance). All name axis target per C-34. |
| C-21 | PASS | "Coverage Axis Gate", "Format Axis Gate", "Inheritance Axis Gate" -- axis in header token. |
| C-22 | PASS | **First test of descriptive register at inter-section peer slot.** "Each closing confirmation gate header names its axis." -- bare standalone descriptive sentence in the canonical inter-section peer slot, flanked by `---` dividers. C-34: all criteria structure-sensitive not register-sensitive. C-23: qualifying condition is physical isolation from gate bodies and example blocks. Inter-section peer slot confirmed qualifying position (C-24). Descriptive register at this position satisfies C-22 identically to imperative. |
| C-23 | PASS | Inter-section peer slot physically isolated from gate bodies and example blocks by `---` dividers and blank lines. Descriptive register does not alter isolation. |
| C-24 | PASS | Inter-section peer slot is a confirmed qualifying position per C-24. |
| C-25 | PASS | Rule in confirmed position; C-25 trivially inapplicable. |
| C-26 | PASS | Rule not in named section body; C-26 trivially inapplicable. |
| C-27 | PASS | Template + inline example; slot-name def lines absent and not required. |
| C-28 | PASS | Inline example present. |
| C-29 | PASS | Example present; C-29 inapplicable. |
| C-30 | PASS | Rule not at earliest inter-section gap; C-30 inapplicable. |
| C-31 | PASS | Rule not in named section body; C-31 trivially inapplicable. |
| C-32 | PASS | Closure confirmed by R12-R14; no additional per-body confirmation required. |
| C-33 | PASS | Single placement; dual-body inertness trivially inapplicable. |
| C-34 | PASS | Descriptive register throughout; all structural elements present and correctly placed. C-34 pass condition: section sequence, table structure, gate structure, axis labels, repair verb specificity -- all present. |
| C-35 | PASS | Rule not in any section body; C-35 trivially inapplicable. |
| C-36 | PASS | No section-body placement; C-36 trivially inapplicable. |
| C-37 | PASS | Single placement; N-ceiling principle trivially inapplicable. |
| C-38 | PASS | No dual section-body descriptive placement; C-38 trivially inapplicable. |
| C-39 | PASS | Single placement at inter-section peer slot; no multiple section-body placements in descriptive. C-39 trivially inapplicable. |
| C-40 | PASS | Single placement (N=1); C-40 fires on N>=4 confirmations. Trivially inapplicable. |
| C-41 | PASS | No section-body composition; C-41 fires on N=6 including Synthesis body. Trivially inapplicable. |
| C-42 | PASS | No N=4/5 descriptive section-body composition. Trivially inapplicable. |
| C-43 | PASS | No descriptive + N=6 section-body composition. Trivially inapplicable. |

**V-02 score: 36/36 = 100. GOLDEN.**

---

#### V-03 -- Mixed Register N=2: Descriptive at Position 1, Imperative at Position 2 (Register + Lifecycle)

Rule form: (1) end of flow-lifecycle body (position 1) -- descriptive sentence: "The closing confirmation gates are each labeled with a header that names the axis they check." (2) end of flow-conversation body (position 2) -- imperative labeled paragraph: `**Axis-Header Rule**: Each gate header names its axis.` Remaining prompt in imperative register. First test of cross-register dual section-body placement (descriptive first, imperative subsequent).

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | "Sections in this exact order: flow-lifecycle, flow-conversation, trace-state, trace-contract, trace-permissions, SYNTHESIS, Consolidated Findings." |
| C-02 | PASS | "Write everything as one document from start to finish. Do not promise to continue." |
| C-03 | PASS | Sort label "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW" present. |
| C-04 | PASS | spec-gap and contract-violation defined; Coverage Axis Gate confirms both with correction loop. |
| C-05 | PASS | Table pre-opened; at-discovery appending; Sub-Skill column present. |
| C-06 | PASS | Concrete next step instruction present. |
| C-07 | PASS | "If a phase has no findings, say so briefly." / "If none: say so explicitly." |
| C-08 | PASS | Rationale column pre-opened; 3-slot template + inline example. |
| C-09 | PASS | SYNTHESIS section with full CROSS-SKILL instructions. |
| C-10 | PASS | Label present adjacent to sort instruction. |
| C-11 | PASS | Coverage Axis Gate with correction loop. |
| C-12 | PASS | Table opened before flow-lifecycle; rows appended at discovery. |
| C-13 | PASS | SYNTHESIS isolated between trace-permissions and Consolidated Findings. |
| C-14 | PASS | Rationale column pre-opened. |
| C-15 | PASS | CROSS-SKILL insertion into table; Coverage summary CROSS-SKILL row. |
| C-16 | PASS | Template + inline Example; Format Axis Gate enforces. |
| C-17 | PASS | No-downgrade rule + provenance form + Inheritance Axis Gate. |
| C-18 | PASS | Three gates each with independent correction loop. |
| C-19 | PASS | Three gates, one axis each, none merged. |
| C-20 | PASS | "add", "rewrite", "fix" -- each names axis target explicitly. |
| C-21 | PASS | "Coverage Axis Gate", "Format Axis Gate", "Inheritance Axis Gate" in header tokens. |
| C-22 | PASS | Position 1 (flow-lifecycle body, descriptive) = first qualifying occurrence; satisfies C-22 per C-36. Position 2 (flow-conversation body, imperative) = second qualifying occurrence; inert per C-38: "when the first qualifying named section-body placement satisfies C-22 in descriptive register, any subsequent qualifying placement is inert." The "any subsequent qualifying placement" clause is register-unrestricted -- subsequent being imperative covered identically. |
| C-23 | PASS | Both section body positions isolated from gate bodies and example blocks. |
| C-24 | PASS | Named section bodies are confirmed qualifying positions per C-26/C-31/C-35. |
| C-25 | PASS | C-24 list illustrative; section bodies qualify. |
| C-26 | PASS | Both positions are named section bodies; non-disqualifying per C-26. |
| C-27 | PASS | Template + inline example; slot-name defs absent and not required. |
| C-28 | PASS | Inline example present. |
| C-29 | PASS | Example present; inapplicable. |
| C-30 | PASS | Inapplicable. |
| C-31 | PASS | Both bodies within C-31 scope. |
| C-32 | PASS | Positions 1,2 in C-35 confirmed enumeration. |
| C-33 | PASS | N=2; C-22 satisfied at position 1; position 2 inert. C-33 covers dual section-body placement. |
| C-34 | PASS | Descriptive register at position 1; all structural elements present. Imperative for remainder; C-34 applies: structure-sensitive not register-sensitive. |
| C-35 | PASS | Positions 1,2 individually confirmed in C-35 enumeration. |
| C-36 | PASS | Descriptive register + position-1 section-body placement compose without interaction per C-36. |
| C-37 | PASS | N=2; first qualifying occurrence satisfies; position 2 inert. C-37 trivially satisfied. |
| C-38 | PASS | **C-38 first cross-register test: descriptive first, imperative subsequent.** C-38: "any subsequent qualifying placement is inert in exactly the same way it is inert in imperative register." The "any subsequent qualifying placement" clause does not restrict the register of the subsequent placement. Subsequent being imperative is covered identically. First confirmation that C-38's "any subsequent" clause absorbs an imperative subsequent. |
| C-39 | PASS | N=2 section bodies; descriptive at position 1; position 2 is imperative and inert. C-39 trivially inapplicable. |
| C-40 | PASS | N=2; C-40 fires on N>=4. Trivially inapplicable. |
| C-41 | PASS | N=2 bodies; C-41 fires on N=6 including Synthesis body. Trivially inapplicable. |
| C-42 | PASS | N=2; C-42 fires on descriptive N=4/5. Trivially inapplicable. |
| C-43 | PASS | N=2; no N=6 in descriptive. Trivially inapplicable. |

**V-03 score: 36/36 = 100. GOLDEN.**

---

#### V-04 -- Mixed Register N=2: Imperative at Position 1, Descriptive at Position 2 (Register + Lifecycle)

Rule form: (1) end of flow-lifecycle body (position 1) -- imperative labeled paragraph: `**Axis-Header Rule**: Each gate header names its axis.` (2) end of flow-conversation body (position 2) -- descriptive sentence: "The closing confirmation gates are each labeled with a header that names the axis they check." Remaining prompt in imperative register. Reverse complement of V-03.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | "Sections in this exact order: flow-lifecycle, flow-conversation, trace-state, trace-contract, trace-permissions, SYNTHESIS, Consolidated Findings." |
| C-02 | PASS | "Write everything as one document from start to finish. Do not promise to continue." |
| C-03 | PASS | Sort label "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW" present. |
| C-04 | PASS | spec-gap and contract-violation defined; Coverage Axis Gate confirms both with correction loop. |
| C-05 | PASS | Table pre-opened; at-discovery appending; Sub-Skill column present. |
| C-06 | PASS | Concrete next step instruction present. |
| C-07 | PASS | "If a phase has no findings, say so briefly." / "If none: say so explicitly." |
| C-08 | PASS | Rationale column pre-opened; 3-slot template + inline example. |
| C-09 | PASS | SYNTHESIS section with full CROSS-SKILL instructions. |
| C-10 | PASS | Label present adjacent to sort instruction. |
| C-11 | PASS | Coverage Axis Gate with correction loop. |
| C-12 | PASS | Table opened before flow-lifecycle; rows appended at discovery. |
| C-13 | PASS | SYNTHESIS isolated between trace-permissions and Consolidated Findings. |
| C-14 | PASS | Rationale column pre-opened. |
| C-15 | PASS | CROSS-SKILL insertion into table; Coverage summary CROSS-SKILL row. |
| C-16 | PASS | Template + inline Example; Format Axis Gate enforces. |
| C-17 | PASS | No-downgrade rule + provenance form + Inheritance Axis Gate. |
| C-18 | PASS | Three gates each with independent correction loop. |
| C-19 | PASS | Three gates, one axis each, none merged. |
| C-20 | PASS | "add", "rewrite", "fix" -- each names axis target explicitly. |
| C-21 | PASS | "Coverage Axis Gate", "Format Axis Gate", "Inheritance Axis Gate" in header tokens. |
| C-22 | PASS | Position 1 (flow-lifecycle body, imperative) = first qualifying occurrence; satisfies C-22 per confirmed R11 V-02. Position 2 (flow-conversation body, descriptive) = second qualifying occurrence; inert per C-33 + C-34. C-33: dual named section-body placement composes cleanly; second occurrence inert. C-34: criteria are structure-sensitive not register-sensitive; inertness of second placement is register-invariant. |
| C-23 | PASS | Both section body positions isolated from gate bodies and example blocks. |
| C-24 | PASS | Named section bodies are confirmed qualifying positions per C-26/C-31/C-35. |
| C-25 | PASS | C-24 list illustrative; section bodies qualify. |
| C-26 | PASS | Both positions are named section bodies; non-disqualifying per C-26. |
| C-27 | PASS | Template + inline example; slot-name defs absent and not required. |
| C-28 | PASS | Inline example present. |
| C-29 | PASS | Example present; inapplicable. |
| C-30 | PASS | Inapplicable. |
| C-31 | PASS | Both bodies within C-31 scope. |
| C-32 | PASS | Positions 1,2 in C-35 confirmed enumeration. |
| C-33 | PASS | N=2; C-22 satisfied at position 1 (imperative); position 2 inert. C-33 covers dual section-body placement. |
| C-34 | PASS | **C-34 extends inertness to descriptive subsequent.** Imperative register for position 1; descriptive for position 2. C-34: criteria are structure-sensitive not register-sensitive. Second placement is inert structurally; C-34 ensures descriptive register of position 2 does not alter that inertness. |
| C-35 | PASS | Positions 1,2 individually confirmed in C-35 enumeration. |
| C-36 | PASS | Position 2 is descriptive + section-body but structurally inert; no interaction with C-22 satisfaction at position 1 (imperative). C-36 trivially inapplicable as a constraint on the first qualifying occurrence. |
| C-37 | PASS | N=2; first qualifying occurrence satisfies; position 2 inert. C-37 trivially satisfied. |
| C-38 | PASS | C-38 fires on descriptive first placement. Position 1 is imperative; C-38 trivially inapplicable. C-33+C-34 cover the imperative-first case. |
| C-39 | PASS | No multiple descriptive section-body qualifying occurrences (position 2 is inert). C-39 trivially inapplicable. |
| C-40 | PASS | N=2; C-40 fires on N>=4. Trivially inapplicable. |
| C-41 | PASS | N=2 bodies; C-41 fires on N=6 including Synthesis body. Trivially inapplicable. |
| C-42 | PASS | N=2; no descriptive N=4/5 section-body composition. Trivially inapplicable. |
| C-43 | PASS | N=2; no descriptive + N=6. Trivially inapplicable. |

**V-04 score: 36/36 = 100. GOLDEN.**

---

#### V-05 -- Cross-Type Dual Placement: Section Body (Descriptive) + Inter-Section Peer Slot (Descriptive) (Register + Lifecycle)

Rule form: (1) end of flow-lifecycle body (position 1, named section body) -- descriptive sentence: "The closing confirmation gates are each labeled with a header that names the axis they check." (first qualifying occurrence). (2) inter-section peer slot between Synthesis and Consolidated Findings (flanked by `---`) -- bare descriptive sentence: "Each closing confirmation gate header names its axis." (second qualifying occurrence, inert). Entire prompt in descriptive register. First cross-type dual placement test (section body + inter-section peer slot).

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | "The report proceeds through these sections in sequence: flow-lifecycle, flow-conversation, trace-state, trace-contract, trace-permissions, SYNTHESIS, Consolidated Findings." |
| C-02 | PASS | "The entire report is produced as one document from start to finish, without any promise of continuation." |
| C-03 | PASS | Sort label "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW" present. |
| C-04 | PASS | spec-gap and contract-violation defined; Coverage Axis Gate confirms both with correction instruction. |
| C-05 | PASS | Table pre-opened; rows appended at discovery; Sub-Skill column present. |
| C-06 | PASS | "Top finding: a concrete next step naming the exact spec section, boundary, or component a developer must address before writing any implementation code." |
| C-07 | PASS | "Any phase that produces no findings is noted as such." / "If this section produces no findings, that is stated explicitly." -- descriptive form per C-34. |
| C-08 | PASS | Rationale column pre-opened; 3-slot template + inline example present. |
| C-09 | PASS | SYNTHESIS section with full CROSS-SKILL instructions and table insertion. |
| C-10 | PASS | Sort label structurally adjacent. |
| C-11 | PASS | Coverage Axis Gate checks both types with correction instruction. |
| C-12 | PASS | Table opened before flow-lifecycle; rows appended at discovery. |
| C-13 | PASS | Synthesis isolated between trace-permissions and Consolidated Findings dividers. |
| C-14 | PASS | Rationale column pre-opened. |
| C-15 | PASS | CROSS-SKILL insertion into table; Coverage summary CROSS-SKILL row. |
| C-16 | PASS | Template string + inline Example; Format Axis Gate enforces. |
| C-17 | PASS | No-downgrade rule + provenance form + Inheritance Axis Gate. |
| C-18 | PASS | Three gates each with independent correction instruction (descriptive form per C-34). |
| C-19 | PASS | Three gates, one axis each, not merged. |
| C-20 | PASS | Descriptive axis-named repair instructions: "add the missing finding", "rewritten using [LEVEL]/[boundary]/[caller/component]/[effect] structure", "has its CROSS-SKILL blast radius and provenance annotation corrected". All name axis target per C-34. |
| C-21 | PASS | "Coverage Axis Gate", "Format Axis Gate", "Inheritance Axis Gate" -- axis in header token. |
| C-22 | PASS | Position 1 (flow-lifecycle body, descriptive) = first qualifying occurrence; satisfies C-22 per C-36. Position 2 (inter-section peer slot, descriptive) = second qualifying occurrence of a DIFFERENT position type; inert. The general "first qualifying occurrence satisfies; subsequent are inert" principle is position-type-agnostic. C-24 confirms any non-buried position is qualifying; the inertness rule does not restrict subsequent placements by position type. V-02 confirms descriptive at inter-section peer slot qualifies as FIRST; V-05 confirms it is inert as SECOND. |
| C-23 | PASS | Position 1 (section body) isolated from gate bodies and example blocks. Position 2 (inter-section peer slot) flanked by `---` dividers. Both positions satisfy isolation primacy. |
| C-24 | PASS | Both position types are confirmed qualifying positions: section body (C-26/C-31/C-35) and inter-section peer slot (C-24 confirmed positions list). |
| C-25 | PASS | C-24 list illustrative; both position types qualify. |
| C-26 | PASS | Position 1 is a named section body; non-disqualifying per C-26. |
| C-27 | PASS | Template + inline example; slot-name defs absent and not required. |
| C-28 | PASS | Inline example present. |
| C-29 | PASS | Example present; inapplicable. |
| C-30 | PASS | Inapplicable. |
| C-31 | PASS | Position 1 (flow-lifecycle body) within C-31 scope. |
| C-32 | PASS | Position 1 in C-35 confirmed enumeration. |
| C-33 | PASS | C-33 covers dual NAMED SECTION-BODY placements; position 2 here is the inter-section peer slot (not a named section body). C-33 is not directly invoked; the general first-qualifying-occurrence + inertness principle -- which is the foundation of C-33 -- extends beyond same-type placements. C-22 satisfied at position 1; position 2 inert regardless of type. |
| C-34 | PASS | Descriptive register throughout; all structural elements present and correctly placed. |
| C-35 | PASS | Position 1 (flow-lifecycle body) individually confirmed in C-35 enumeration. |
| C-36 | PASS | Descriptive register + section-body placement (position 1) compose without interaction per C-36. |
| C-37 | PASS | N=1 named section body; no N-ceiling considerations for the section-body type. Inter-section peer slot is a different position type; C-37 trivially satisfied. |
| C-38 | PASS | Position 1 (section body, descriptive) is the first qualifying placement in descriptive register. Position 2 (inter-section peer slot, descriptive) is inert. C-38 + C-34 jointly absorb position 2's inertness across position types: subsequent qualifying placements are inert regardless of position type. |
| C-39 | PASS | N=1 named section body in descriptive; C-39 fires on multiple section-body placements in descriptive. Trivially inapplicable. |
| C-40 | PASS | N=1 section body; C-40 fires on N>=4. Trivially inapplicable. |
| C-41 | PASS | N=1 section body + 1 inter-section peer slot. C-41 fires on N=6 section-body composition including Synthesis body. Trivially inapplicable. |
| C-42 | PASS | N=1 section body in descriptive; C-42 fires on descriptive N=4/5 section-body composition. Trivially inapplicable. |
| C-43 | PASS | N=1 section body + 1 inter-section peer slot; no N=6 section-body composition in descriptive. Trivially inapplicable. |

**V-05 score: 36/36 = 100. GOLDEN.**

---

### Ranking

All variations tied at 100 (36/36 = 4/4 essential + 3/3 recommended + 29/29 aspirational). Ranked by novelty:

| Rank | Variation | Novel Test |
|------|-----------|-----------|
| 1 | V-05 | Cross-type dual placement (section body + inter-section peer slot, descriptive) -- first test of inertness across position types |
| 2 | V-02 | Descriptive register + inter-section peer slot -- closes last untested position-type x register cell |
| 3 | V-03 | Mixed-register dual section-body (descriptive first, imperative subsequent) -- first cross-register dual body test |
| 4 | V-04 | Mixed-register dual section-body (imperative first, descriptive subsequent) -- reverse complement of V-03 |
| 5 | V-01 | Denominator transition reconfirmation (33->36) |

---

### Excellence Signals

V-05 is the highest-novelty variation this round. Excellence signals:

- **Inertness principle generalized across position types.** V-05 is the first test combining placements of different position classes (named section body + inter-section peer slot) in a single prompt. The general "first qualifying occurrence satisfies; subsequent are inert" principle -- which C-33 encodes for same-type dual section-body cases -- absorbs cross-type compositions without modification. No new criterion is needed to handle the position-type dimension.

- **V-02 and V-05 form a complementary pair.** V-02 confirms that descriptive register at the inter-section peer slot qualifies as a FIRST (satisfying) occurrence. V-05 confirms it is equally inert as a SECOND occurrence. Together they close the descriptive-register x inter-section-peer-slot cell in both roles.

- **C-38's "any subsequent qualifying placement" clause proved register-unrestricted (V-03).** Prior C-38 confirmations used uniform register across placements. V-03 tests whether "any subsequent qualifying placement is inert" covers the case where the subsequent is imperative. The clause's lack of register restriction absorbs this without qualification.

- **C-33 + C-34 reverse complement confirmed (V-04).** C-38 handles descriptive-first cases. The imperative-first + descriptive-subsequent case is handled by C-33 + C-34. Both register orderings are now confirmed, closing the cross-register dual section-body matrix.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Inertness principle extends across position types: section body (descriptive, first qualifying) + inter-section peer slot (descriptive, second qualifying) composes without interaction -- the general first-qualifying-occurrence satisfies; subsequent are inert principle is position-type-agnostic (V-05)", "Descriptive register at inter-section peer slot is a qualifying first occurrence for C-22 -- C-34 register invariance + C-23 isolation primacy close the last untested cell in the position-type x register matrix (V-02)", "C-38 any-subsequent-qualifying-placement clause is register-unrestricted: descriptive first + imperative subsequent dual section-body composes without interaction (V-03)", "C-33 + C-34 cover the reverse complement: imperative first + descriptive subsequent dual section-body; both register orderings absorbed without new criteria (V-04)"]}
```
