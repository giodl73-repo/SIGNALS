**rhythm-behavior R13 scored.** Scorecard written to `simulations/quest/scorecards/rhythm-behavior-scorecard-R13-2026-03-17.md`.

---

### Results

| Variation | Essential | Recommended | Aspirational | Composite | Golden |
|-----------|-----------|-------------|--------------|-----------|--------|
| V-01 | 4/4 | 3/3 | 30/30 | **100** | YES |
| V-02 | 4/4 | 3/3 | 30/30 | **100** | YES |
| V-03 | 4/4 | 3/3 | 30/30 | **100** | YES |
| V-04 | 4/4 | 3/3 | 30/30 | **100** | YES |
| V-05 | 4/4 | 3/3 | 30/30 | **100** | YES |

**5/5 golden** -- all predictions confirmed.

---

### Open Questions Resolved

| Question | V | Result |
|----------|---|--------|
| C-35/C-36/C-37 trivially pass for baseline? | V-01 | YES -- inter-section peer slot; all three criteria fire only on the scorer errors they guard against |
| Descriptive + dual section bodies compose? | V-02 | YES -- C-36+C-33 first joint test; positions 1+3; no restriction |
| C-37 extends to N=4? | V-03 | YES -- first satisfies, three inert; no N-ceiling |
| Descriptive + triple section bodies compose? | V-04 | YES -- C-36+C-37 first joint test; same positions as R12 V-05 |
| C-37 holds at N=5 (structural maximum)? | V-05 | YES -- all five sub-skill bodies; principle holds at structural limit |

---

### New Patterns

1. **C-36+C-33 first joint test (V-02).** Descriptive + dual section-body placement compose without interaction. Position 1 satisfies C-22 in descriptive register; position 3 is inert.

2. **C-36+C-37 first joint test (V-04).** Descriptive + triple section-body placement compose without interaction. Direct counterpart of R12 V-05; register-invariance extends C-37 inertness cleanly.

3. **C-37 at N=4 and N=5 structural maximum.** No exception found at any count or register. Principle confirmed at the structural limit of the prompt.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Descriptive register + dual section-body placement compose without interaction (C-36+C-33 first joint test, V-02) -- position 1 satisfies C-22 in descriptive register, position 3 inert; no restriction emerges from combining both independently confirmed properties", "Descriptive register + triple section-body placement compose without interaction (C-36+C-37 first joint test, V-04) -- direct counterpart of R12 V-05 at same positions 1/3/5; register-invariance extends C-37 inertness to descriptive form without modification", "C-37 no-ceiling principle confirmed at N=4 (V-03) and N=5 structural maximum (V-05) -- all five sub-skill bodies tested; first qualifying occurrence satisfies, all subsequent inert; no exception found at any count or register"]}
```
 |
| C-06 Actionable Next Step for Top Finding | PASS | "Top finding: one concrete next step naming the exact spec section, boundary, or component a developer must address before writing implementation code." |
| C-07 Sub-Skill Section Completeness | PASS | flow-lifecycle: "If a phase has no findings, say so briefly." All others: "If none: say so explicitly." |
| C-08 Blast Radius Justification | PASS | Rationale column pre-opened; "Blast Radius Rationale is required for every row"; 3-slot template enforced. |
| C-09 Cross-Sub-Skill Synthesis | PASS | SYNTHESIS section with full CROSS-SKILL instructions and insertion into table. |
| C-10 Self-Documenting Ranking Label | PASS | Label: "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW" structurally adjacent to sort instruction. |
| C-11 Active Coverage Confirmation | PASS | Coverage Axis Gate: "spec-gap present? contract-violation present? Missing: add one before Format Axis Gate." |
| C-12 At-Discovery Attribution | PASS | "Open this table before flow-lifecycle. Append rows as findings are discovered." Table has all columns from open. |
| C-13 Dedicated Synthesis Step | PASS | SYNTHESIS isolated between trace-permissions `---` divider and Consolidated Findings `---` divider. |
| C-14 Rationale Column Enforcement | PASS | "Blast Radius Rationale" column in table header pre-opened before first sub-skill. |
| C-15 CROSS-SKILL Findings as First-Class Table Citizens | PASS | "Add to findings table with Sub-Skill = CROSS-SKILL" in Synthesis; Coverage summary has CROSS-SKILL row. |
| C-16 3-Slot Rationale Format | PASS | Template string "[LEVEL] because [boundary] propagates to [caller/component], [effect]" + inline Example present in "What to look for". |
| C-17 CROSS-SKILL Blast Radius Inheritance Rule | PASS | "CROSS-SKILL blast radius >= max(contributing sub-skills); no downgrade permitted" + provenance form + Inheritance Axis Gate. |
| C-18 Closing Confirmation Multi-Gate Enforcement | PASS | Three gates (Coverage, Format, Inheritance) each with independent correction loop. |
| C-19 One-Axis-Per-Gate Rule | PASS | Three separate gates; each covers exactly one axis; none merged. |
| C-20 Axis-Named Repair Verb | PASS | Coverage: "add one"; Format: "rewrite those cells"; Inheritance: "fix blast radius and annotation" -- each names axis target. |
| C-21 Axis-Labeled Gate Header Encoding | PASS | "Coverage Axis Gate", "Format Axis Gate", "Inheritance Axis Gate" -- axis in header token. |
| C-22 Explicit Axis-Header Preamble Rule | PASS | Labeled paragraph in inter-section peer slot between Synthesis and Consolidated Findings -- confirmed qualifying position (R6/R7/R8). |
| C-23 Axis-Header Rule Isolation Primacy | PASS | Inter-section peer slot is physically isolated; not gate body, not example block. |
| C-24 Axis-Header Rule Placement Invariance | PASS | Inter-section peer slot is a confirmed qualifying position; no proximity constraint violated. |
| C-25 C-24 Confirmed-Position List Is Illustrative | PASS | Rule in confirmed position; C-25 trivially inapplicable. |
| C-26 Named Section Bodies Are Non-Disqualifying | PASS | Rule not in section body; C-26 trivially inapplicable (fires only when scorer wrongly rejects section-body placement). |
| C-27 3-Slot Template Load-Bearing Elements | PASS | Template + inline example present; no slot-name def lines required per C-27. |
| C-28 Inline Example Is Load-Bearing for C-16 | PASS | Inline Example present; C-28 inapplicable (fires only when example absent). |
| C-29 C-27 Scope: Missing Example Is Not Shielded | PASS | Example present; C-29 inapplicable. |
| C-30 C-25 Position Invariance Confirmed Across Full Prompt Span | PASS | Rule not at earliest inter-section gap; C-30 inapplicable. |
| C-31 C-26 Named Section Bodies Are Fully Illustrative | PASS | Rule not in section body; C-31 trivially inapplicable. |
| C-32 C-31 Confirmed Closed Across All Named Section Bodies | PASS | Trivially inapplicable; closure confirmed by R12; scorer cannot require additional per-body confirmation. |
| C-33 Dual Named Section-Body Placement Composes Cleanly | PASS | Single placement; dual-body inertness rule trivially inapplicable. |
| C-34 Criteria Are Structure-Sensitive, Not Register-Sensitive | PASS | Imperative register; all structural elements present. |
| C-35 All Five Sub-Skill Section Bodies Individually Confirmed | PASS | Rule not in any section body; C-35 fires only when scorer withholds C-26/C-31/C-32 credit for section bodies. Trivially inapplicable. |
| C-36 Descriptive Register and Section-Body Placement Compose Without Interaction | PASS | Neither descriptive register nor section-body placement in use; C-36 trivially inapplicable. |
| C-37 C-33 Inertness Rule Has No N-Ceiling | PASS | Single placement; inertness rule (N>=2) trivially inapplicable. |

**V-01 score: 30/30 = 100. GOLDEN.**

---

#### V-02 -- Descriptive Register + Dual Section Bodies (positions 1, 3; C-36+C-33 first composition)

Rule form: `"The closing confirmation gates are each labeled with a header that names the axis they check."` (descriptive) placed at end of flow-lifecycle body (position 1) and trace-state body (position 3). No rule in any inter-section slot or other section body. All other elements in descriptive register per R12 V-04 form.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | "The report proceeds through these sections in sequence: flow-lifecycle, flow-conversation, trace-state, trace-contract, trace-permissions, SYNTHESIS, Consolidated Findings." |
| C-02 | PASS | "produced as one document from start to finish, without any promise of continuation." |
| C-03 | PASS | Sort instruction + Label "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW" in Consolidated Findings. |
| C-04 | PASS | Both types defined; Coverage Axis Gate confirms both with correction loop. |
| C-05 | PASS | Sub-Skill column in pre-opened table; "Rows are appended as each finding is discovered." |
| C-06 | PASS | "a concrete next step naming the exact spec section, boundary, or component a developer must address before writing any implementation code." |
| C-07 | PASS | "Any phase that produces no findings is noted as such." / "that is stated explicitly." -- descriptive form satisfies per C-34. |
| C-08 | PASS | "The Blast Radius Rationale column is populated for every row"; 3-slot template defined. |
| C-09 | PASS | Synthesis section with full CROSS-SKILL instructions present. |
| C-10 | PASS | Label present. |
| C-11 | PASS | Coverage Axis Gate: "Confirms that at least one spec-gap finding and at least one contract-violation finding are present... If either category is absent, add the missing finding." |
| C-12 | PASS | "The findings table is opened before flow-lifecycle begins. Rows are appended as each finding is discovered." |
| C-13 | PASS | Synthesis isolated between trace-permissions divider and Consolidated Findings divider. |
| C-14 | PASS | "Blast Radius Rationale" column in pre-opened table before first sub-skill. |
| C-15 | PASS | "The finding is inserted into the findings table with Sub-Skill = CROSS-SKILL"; Coverage summary CROSS-SKILL row. |
| C-16 | PASS | Template string + inline Example present in "What to look for". |
| C-17 | PASS | "The CROSS-SKILL blast radius is >= max(contributing sub-skills); no downgrade"; provenance form specified; Inheritance Axis Gate checks. |
| C-18 | PASS | Three gates with independent correction loops (descriptive form per C-34). |
| C-19 | PASS | Three gates, one axis each, not merged. |
| C-20 | PASS | Coverage: "add the missing finding"; Format: "is rewritten using the [LEVEL]/[boundary]/[caller/component]/[effect] structure"; Inheritance: "has its CROSS-SKILL blast radius and provenance annotation corrected" -- all name axis target per C-34. |
| C-21 | PASS | "Coverage Axis Gate", "Format Axis Gate", "Inheritance Axis Gate" headers present. |
| C-22 | PASS | Descriptive sentence in flow-lifecycle body (position 1) = qualifying per C-26, C-31, C-35, C-36. First occurrence satisfies. Second occurrence in trace-state body (position 3) is inert per C-33. |
| C-23 | PASS | Flow-lifecycle body is physically isolated from gate bodies and example blocks. |
| C-24 | PASS | Named section body confirmed qualifying position per C-26. |
| C-25 | PASS | C-24's list is illustrative; section bodies qualify without being in confirmed-position list. |
| C-26 | PASS | Flow-lifecycle body (position 1) and trace-state body (position 3) are named section bodies; non-disqualifying per C-26. |
| C-27 | PASS | Template + inline example present; slot-name def lines absent and not required. |
| C-28 | PASS | Inline example present. |
| C-29 | PASS | Inline example present; C-29 inapplicable. |
| C-30 | PASS | Rule not at earliest inter-section gap; C-30 inapplicable. |
| C-31 | PASS | Flow-lifecycle and trace-state bodies covered by C-31's "all named section bodies" scope. |
| C-32 | PASS | Positions 1 and 3 both in C-35's confirmed enumeration; C-32 closure complete. |
| C-33 | PASS | Dual section-body placement composes cleanly: position 1 satisfies C-22, position 3 is inert. N=2 confirmed R11 V-04; descriptive register extends cleanly per C-34. |
| C-34 | PASS | Descriptive register; all structural elements (template, columns, gate structure, axis labels, repair specificity) present per C-34's pass condition. |
| C-35 | PASS | Positions 1 and 3 individually confirmed in C-35's enumeration. |
| C-36 | PASS | **First joint test of C-36+C-33.** Descriptive register (C-36 confirmed R12 V-04) + dual section-body placement (C-33 confirmed R11 V-04) compose without interaction. Position 1 satisfies C-22 in descriptive register; position 3 is inert. Neither property restricts the other. |
| C-37 | PASS | N=2; first qualifying occurrence (position 1) satisfies C-22; second (position 3) is inert. Inertness rule holds at N=2 in descriptive register per C-34. No N-ceiling. |

**V-02 score: 30/30 = 100. GOLDEN.**

---

#### V-03 -- Quad Named Section-Body Placement (positions 1, 2, 3, 4; imperative; C-37 N=4 extension)

Rule form: `**Axis-Header Rule**: Each gate header names its axis.` placed at end of flow-lifecycle (position 1), flow-conversation (position 2), trace-state (position 3), and trace-contract (position 4). No rule elsewhere. All other elements identical to V-01.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | "Sections in this exact order: flow-lifecycle, flow-conversation, trace-state, trace-contract, trace-permissions, SYNTHESIS, Consolidated Findings." |
| C-02 | PASS | "Write everything as one document from start to finish. Do not promise to continue." |
| C-03 | PASS | Sort instruction + label present. |
| C-04 | PASS | Both types defined; Coverage Axis Gate checks both. |
| C-05 | PASS | Sub-Skill column pre-opened; at-discovery appending. |
| C-06 | PASS | Concrete next step instruction present. |
| C-07 | PASS | "If a phase has no findings, say so briefly." / "If none: say so explicitly." |
| C-08 | PASS | Rationale column; "Blast Radius Rationale is required for every row." |
| C-09 | PASS | SYNTHESIS section with CROSS-SKILL instructions. |
| C-10 | PASS | Label present. |
| C-11 | PASS | Coverage Axis Gate with correction loop. |
| C-12 | PASS | "Open this table before flow-lifecycle. Append rows as findings are discovered." |
| C-13 | PASS | SYNTHESIS structurally isolated. |
| C-14 | PASS | Rationale column pre-opened. |
| C-15 | PASS | CROSS-SKILL in table; Coverage summary CROSS-SKILL row. |
| C-16 | PASS | Template + inline Example present. |
| C-17 | PASS | Inheritance rule + provenance form + Inheritance Axis Gate. |
| C-18 | PASS | Three gates, each with correction loop. |
| C-19 | PASS | Three gates, one axis each. |
| C-20 | PASS | "add", "rewrite", "fix" -- axis-named repair verbs. |
| C-21 | PASS | "Coverage Axis Gate", "Format Axis Gate", "Inheritance Axis Gate". |
| C-22 | PASS | Rule in flow-lifecycle body (position 1) = first qualifying occurrence; satisfies C-22. Positions 2, 3, 4 are subsequent qualifying occurrences; all inert per C-37. |
| C-23 | PASS | Named section bodies are isolated from gate bodies and example blocks. |
| C-24 | PASS | Named section bodies are confirmed qualifying positions. |
| C-25 | PASS | C-24's list is illustrative. |
| C-26 | PASS | All four bodies (positions 1-4) are named section bodies; non-disqualifying. |
| C-27 | PASS | Template + inline example; no slot-name defs required. |
| C-28 | PASS | Inline example present. |
| C-29 | PASS | Example present; inapplicable. |
| C-30 | PASS | Inapplicable. |
| C-31 | PASS | All four bodies within C-31's "all named section bodies" scope. |
| C-32 | PASS | Positions 1, 2, 3, 4 all in C-35's confirmed enumeration. |
| C-33 | PASS | N=4 quad placement; C-22 satisfied at position 1; positions 2, 3, 4 inert. C-33 dual-body principle extends to N=4 per C-37. |
| C-34 | PASS | Imperative register; all structural elements present. |
| C-35 | PASS | Positions 1, 2, 3, 4 all individually confirmed in C-35's enumeration. |
| C-36 | PASS | Imperative register; descriptive+section-body combination not in play. Trivially inapplicable. |
| C-37 | PASS | **C-37 N=4 extension.** N=3 confirmed R12 V-05; N=4 is next empirical step. First qualifying occurrence (position 1) satisfies C-22; positions 2, 3, 4 redundant but inert. No criterion penalizes N=4. C-37's no-ceiling principle confirmed at N=4. |

**V-03 score: 30/30 = 100. GOLDEN.**

---

#### V-04 -- Descriptive Register + Triple Section Bodies (positions 1, 3, 5; C-36+C-37 first composition)

Rule form: `"The closing confirmation gates are each labeled with a header that names the axis they check."` (descriptive) placed at end of flow-lifecycle (position 1), trace-state (position 3), and trace-permissions (position 5). No rule elsewhere. All other elements in descriptive register per R12 V-04 form. Direct counterpart of R12 V-05 in descriptive register.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Section sequence declared at prompt opening. |
| C-02 | PASS | Single continuous document; no promise of continuation. |
| C-03 | PASS | Sort + label present. |
| C-04 | PASS | Both types defined; Coverage Axis Gate checks both. |
| C-05 | PASS | Sub-Skill column pre-opened; rows appended at discovery. |
| C-06 | PASS | Concrete next step instruction present. |
| C-07 | PASS | Null-result instruction in descriptive form per C-34. |
| C-08 | PASS | Rationale column; 3-slot template defined. |
| C-09 | PASS | SYNTHESIS section with CROSS-SKILL instructions. |
| C-10 | PASS | Label present. |
| C-11 | PASS | Coverage Axis Gate with correction loop. |
| C-12 | PASS | "The findings table is opened before flow-lifecycle begins." |
| C-13 | PASS | Synthesis structurally isolated. |
| C-14 | PASS | Rationale column pre-opened. |
| C-15 | PASS | CROSS-SKILL in table; Coverage summary row present. |
| C-16 | PASS | Template + inline Example present. |
| C-17 | PASS | Inheritance rule + provenance form + Inheritance Axis Gate. |
| C-18 | PASS | Three gates, each with correction loop (descriptive form per C-34). |
| C-19 | PASS | Three gates, one axis each, not merged. |
| C-20 | PASS | Descriptive axis-named repair verbs satisfying C-20 per C-34. |
| C-21 | PASS | "Coverage Axis Gate", "Format Axis Gate", "Inheritance Axis Gate". |
| C-22 | PASS | Descriptive sentence in flow-lifecycle body (position 1) = first qualifying occurrence; satisfies C-22 per C-36. Positions 3 and 5 are inert per C-37 (N=3, no ceiling). |
| C-23 | PASS | Named section bodies are isolated from gate bodies and example blocks. |
| C-24 | PASS | Named section bodies are confirmed qualifying positions. |
| C-25 | PASS | C-24's list is illustrative. |
| C-26 | PASS | Positions 1, 3, 5 are all named section bodies; non-disqualifying. |
| C-27 | PASS | Template + inline example present. |
| C-28 | PASS | Inline example present. |
| C-29 | PASS | Example present; inapplicable. |
| C-30 | PASS | Inapplicable. |
| C-31 | PASS | All three bodies within C-31's "all named section bodies" scope. |
| C-32 | PASS | Positions 1, 3, 5 all in C-35's confirmed enumeration. |
| C-33 | PASS | N=3 triple placement; C-22 satisfied at position 1; positions 3 and 5 inert. R12 V-05 confirmed N=3 in imperative; C-34 ensures register-invariance. |
| C-34 | PASS | Descriptive register; all structural elements present and correctly placed per C-34. |
| C-35 | PASS | Positions 1, 3, 5 individually confirmed. |
| C-36 | PASS | **First joint test of C-36+C-37.** Descriptive register (C-36 confirmed R12 V-04) + triple section-body placement (C-37 N=3 confirmed R12 V-05) compose without interaction. R12 V-04 = descriptive + N=1; R12 V-05 = imperative + N=3; V-04 = descriptive + N=3. First qualifying occurrence (position 1) satisfies C-22 in descriptive register; positions 3 and 5 are inert. |
| C-37 | PASS | N=3; positions 1, 3, 5. First satisfies; positions 3 and 5 inert. C-34 extends register-invariance to C-37: no-ceiling principle holds in descriptive register identical to imperative. |

**V-04 score: 30/30 = 100. GOLDEN.**

---

#### V-05 -- All Five Sub-Skill Bodies (positions 1-5; imperative; C-37 maximum N=5)

Rule form: `**Axis-Header Rule**: Each gate header names its axis.` placed at end of ALL FIVE sub-skill bodies: flow-lifecycle (1), flow-conversation (2), trace-state (3), trace-contract (4), trace-permissions (5). No rule in any inter-section slot or Synthesis body. All other elements identical to V-01.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | "Sections in this exact order: flow-lifecycle, flow-conversation, trace-state, trace-contract, trace-permissions, SYNTHESIS, Consolidated Findings." |
| C-02 | PASS | "Write everything as one document from start to finish. Do not promise to continue." |
| C-03 | PASS | Sort + label present. |
| C-04 | PASS | Both types defined; Coverage Axis Gate checks both. |
| C-05 | PASS | Sub-Skill column pre-opened; at-discovery appending. |
| C-06 | PASS | Concrete next step instruction present. |
| C-07 | PASS | "If a phase has no findings, say so briefly." / "If none: say so explicitly." |
| C-08 | PASS | Rationale column; "Blast Radius Rationale is required for every row." |
| C-09 | PASS | SYNTHESIS section with CROSS-SKILL instructions. |
| C-10 | PASS | Label: "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW". |
| C-11 | PASS | Coverage Axis Gate with correction loop. |
| C-12 | PASS | "Open this table before flow-lifecycle. Append rows as findings are discovered." |
| C-13 | PASS | SYNTHESIS structurally isolated. |
| C-14 | PASS | Rationale column pre-opened. |
| C-15 | PASS | CROSS-SKILL in table; Coverage summary CROSS-SKILL row. |
| C-16 | PASS | Template + inline Example present. |
| C-17 | PASS | Inheritance rule + provenance form + Inheritance Axis Gate. |
| C-18 | PASS | Three gates, each with correction loop. |
| C-19 | PASS | Three gates, one axis each. |
| C-20 | PASS | "add", "rewrite", "fix" -- axis-named repair verbs. |
| C-21 | PASS | "Coverage Axis Gate", "Format Axis Gate", "Inheritance Axis Gate". |
| C-22 | PASS | Rule in flow-lifecycle body (position 1) = first qualifying occurrence; satisfies C-22. Positions 2, 3, 4, 5 are subsequent qualifying occurrences; all inert per C-37. |
| C-23 | PASS | Named section bodies isolated from gate bodies and example blocks. |
| C-24 | PASS | Named section bodies are confirmed qualifying positions. |
| C-25 | PASS | C-24's list is illustrative. |
| C-26 | PASS | All five bodies are named section bodies; non-disqualifying. |
| C-27 | PASS | Template + inline example; no slot-name defs required. |
| C-28 | PASS | Inline example present. |
| C-29 | PASS | Example present; inapplicable. |
| C-30 | PASS | Inapplicable. |
| C-31 | PASS | All five bodies within C-31's "all named section bodies" scope. |
| C-32 | PASS | All five positions in C-35's confirmed enumeration. |
| C-33 | PASS | N=5; C-22 satisfied at position 1; positions 2, 3, 4, 5 inert. C-33 dual-body principle extends to N=5 per C-37. |
| C-34 | PASS | Imperative register; all structural elements present. |
| C-35 | PASS | All five positions (1-5) individually confirmed -- complete closure. |
| C-36 | PASS | Imperative register; descriptive+section-body combination not in play. Trivially inapplicable. |
| C-37 | PASS | **C-37 maximum N=5.** N=2 (R11 V-04), N=3 (R12 V-05), N=4 (V-03 this round) all confirmed. N=5 is the structural maximum -- bounded only by the five available sub-skill section bodies. First qualifying occurrence (position 1) satisfies C-22; positions 2, 3, 4, 5 redundant but inert. No criterion penalizes any count. Structural limit reached with no exception found. |

**V-05 score: 30/30 = 100. GOLDEN.**

---

### Ranking

All variations tied at 100 (30/30 aspirational, 4/4 essential, 3/3 recommended). Ranked by novelty:

| Rank | Variation | Novel Test |
|------|-----------|-----------|
| 1 | V-04 | C-36+C-37 first joint composition (descriptive + N=3) |
| 2 | V-02 | C-36+C-33 first joint composition (descriptive + N=2) |
| 3 | V-05 | C-37 at structural maximum N=5 |
| 4 | V-03 | C-37 N=4 extension |
| 5 | V-01 | Denominator transition reconfirmation (27->30) |

---

### New Patterns

1. **Descriptive register + dual section-body placement compose without interaction (C-36+C-33 first joint test).** V-02 is the first prompt combining descriptive register with dual section-body placement (positions 1 and 3). R11 V-04 confirmed dual body in imperative; R12 V-04 confirmed descriptive in single body; V-02 is the composition of both. The descriptive sentence in position 1 satisfies C-22; position 3 is inert. C-36 and C-33 are independently confirmed and compose cleanly without new restriction.

2. **Descriptive register + triple section-body placement compose without interaction (C-36+C-37 first joint test).** V-04 is the direct descriptive-register counterpart of R12 V-05 (positions 1, 3, 5). First qualifying occurrence (position 1) satisfies C-22 in descriptive register; positions 3 and 5 are inert. C-34 confirms register-invariance extends to C-37. The combination of C-36 (descriptive+body orthogonal) and C-37 (N=3 inertness) produces no restriction beyond either property in isolation.

3. **C-37 N-ceiling does not exist at N=4 or N=5.** V-03 advances C-37's empirical confirmation from N=3 (R12 V-05) to N=4 (positions 1-4). V-05 presses to the structural maximum N=5 (all five sub-skill bodies). In both cases, first qualifying occurrence satisfies C-22 and all subsequent are inert. No exception found across any count or register. C-37's no-ceiling principle is now confirmed at the structural limit of the prompt.

---

### Excellence Signals

V-04 and V-02 are the highest-novelty variations this round. Excellence signals:

- **Register-invariance composes with placement-cardinality invariance.** When C-36 (register+body orthogonal) and C-37 (N-ceiling absent) both apply simultaneously, neither introduces constraints on the other. The composition is additive: first qualifying occurrence satisfies; all subsequent are inert; register does not affect this count.

- **N=5 structural maximum confirms unbounded principle at its limit.** C-37's claim ("bounded only by available structural positions") is now verified at the upper bound within the sub-skill sequence. Not merely extrapolated from small N -- held at the limit where no further positions are available.

- **Trivial passing of new criteria is informative.** V-01's trivial passes on C-35, C-36, C-37 confirm correct criterion scoping: they fire only on the specific scorer errors they were designed to prevent; they do not burden prompts using previously confirmed designs.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Descriptive register + dual section-body placement compose without interaction (C-36+C-33 first joint test, V-02) -- position 1 satisfies C-22 in descriptive register, position 3 inert; no restriction emerges from combining both independently confirmed properties", "Descriptive register + triple section-body placement compose without interaction (C-36+C-37 first joint test, V-04) -- direct counterpart of R12 V-05 at same positions 1/3/5; register-invariance extends C-37 inertness to descriptive form without modification", "C-37 no-ceiling principle confirmed at N=4 (V-03) and N=5 structural maximum (V-05) -- all five sub-skill bodies tested; first qualifying occurrence satisfies, all subsequent inert; no exception found at any count or register"]}
```
