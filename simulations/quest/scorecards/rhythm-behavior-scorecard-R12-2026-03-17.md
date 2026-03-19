**rhythm-behavior R12 scored.** Scorecard written to `simulations/quest/scorecards/rhythm-behavior-scorecard-R12-2026-03-17.md`.

---

### Results

| Variation | Essential | Recommended | Aspirational | Composite | Golden |
|-----------|-----------|-------------|--------------|-----------|--------|
| V-01 | 4/4 | 3/3 | 27/27 | **100** | YES |
| V-02 | 4/4 | 3/3 | 27/27 | **100** | YES |
| V-03 | 4/4 | 3/3 | 27/27 | **100** | YES |
| V-04 | 4/4 | 3/3 | 27/27 | **100** | YES |
| V-05 | 4/4 | 3/3 | 27/27 | **100** | YES |

**5/5 golden** -- all predictions confirmed.

---

### Open Questions Resolved

| Question | V | Result |
|----------|---|--------|
| C-32 closure to flow-conversation body? | V-02 | YES -- empirically confirmed |
| C-32 closure to trace-contract body? | V-03 | YES -- fifth sub-skill body confirmed |
| Descriptive register + section body (C-34 + C-31)? | V-04 | YES -- orthogonal, compose cleanly |
| C-33 inertness extends to N=3? | V-05 | YES -- no N-ceiling exists |

---

### New Patterns

1. **All six named section positions individually confirmed.** Flow-conversation (V-02) and trace-contract (V-03) close the only gaps in C-32's enumeration. Positions 1-5 (all sub-skill section bodies) + Synthesis body = complete. No named section body has ever failed. Disqualifier set remains strictly gate body + example block.

2. **Descriptive register + section body compose without interaction.** C-34 and C-31 are orthogonal. The descriptive standalone sentence in a qualifying section body passes C-22 identically to the labeled imperative form.

3. **C-33 N-ceiling does not exist.** N=3 triple body placement confirmed. Pattern generalizes: first qualifying occurrence satisfies C-22; all subsequent are inert regardless of count.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["All five sub-skill section bodies individually confirmed -- flow-conversation (V-02) and trace-contract (V-03) close C-32 enumeration gaps; all six named positions confirmed with no exception", "Descriptive register + section-body placement compose cleanly -- C-34 and C-31 are orthogonal; first combined test scores identically to either property in isolation", "C-33 inertness rule has no N-ceiling -- N=3 triple body placement confirmed; first qualifying occurrence satisfies C-22, all subsequent inert without bound"]}
```
 confirm section bodies are qualifying. The three criteria are independent and compose without interaction.

3. **C-33's inertness rule has no N-ceiling.** V-05 extends the dual section-body pattern (R11 V-04, N=2) to N=3. Three qualifying body placements (flow-lifecycle, trace-state, trace-permissions) produce clean composition: C-22 satisfied at the first, second and third inert. The principle "no criterion penalizes multiple qualifying placements" is bounded only by the prompt's structural positions, not by a count ceiling.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["All five sub-skill section bodies now individually confirmed as qualifying positions -- flow-conversation (V-02) and trace-contract (V-03) close the only gaps in C-32's enumeration; every named section body in the sub-skill sequence has been tested and confirmed; C-32 empirically closed with no exceptions", "Descriptive register composes cleanly with named section-body placement -- C-34 (register-invariance) and C-31 (section body qualifies) are independent criteria; descriptive standalone declarative sentence in a qualifying section body satisfies C-22 identically to imperative form; first composition test of both properties simultaneously", "C-33 inertness rule has no N-ceiling -- triple section-body placement (N=3, positions 1/3/5) composes cleanly; C-22 satisfied at first occurrence, second and third inert; principle extends beyond the N=2 dual-body pattern confirmed in R11 V-04 without bound"]}
```

---

### Per-Criterion Verdicts

#### Essential Criteria

**C-01 -- Declared Execution Sequence**
All five: section order "flow-lifecycle, flow-conversation, trace-state, trace-contract, trace-permissions, SYNTHESIS, Consolidated Findings" declared before any findings appear. V-04 uses descriptive phrasing ("The report proceeds through these sections in sequence: ...") which is order-complete and pre-findings. All PASS.

**C-02 -- Single Unified Report**
V-01 through V-03, V-05: "Write everything as one document from start to finish. Do not promise to continue." V-04: "The entire report is produced as one document from start to finish, without any promise of continuation." All PASS.

**C-03 -- Blast Radius Ranking Present**
All five: sort label `"Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW"` structurally adjacent to the sorted table in Consolidated Findings. V-04 uses equivalent descriptive form. All PASS.

**C-04 -- Spec Gap and Contract Violation Coverage**
All five define spec-gap and contract-violation in "What to look for." Coverage Axis Gate checks for both and fires a correction loop if either is absent. All PASS.

---

#### Recommended Criteria

**C-05 -- Per-Finding Sub-Skill Attribution**
All five: table pre-opened with Sub-Skill column; each sub-skill section instructs appending rows with attribution at discovery time ("Sub-Skill = flow-lifecycle, classify, assign blast radius" or descriptive equivalent). All PASS.

**C-06 -- Actionable Next Step for Top Finding**
All five: "Top finding: one concrete next step naming the exact spec section, boundary, or component a developer must address before writing implementation code." V-04: "a concrete next step naming the exact spec section, boundary, or component a developer must address before writing any implementation code." Both forms name the axis target; neither is generic. All PASS.

**C-07 -- Sub-Skill Section Completeness**
All five: each section includes an explicit null-result instruction ("If a phase has no findings, say so briefly." or "If none: say so explicitly." or descriptive equivalent in V-04: "Any phase that produces no findings is noted as such." / "If this section produces no findings, that is stated explicitly."). C-34 confirms descriptive form is equivalent. All PASS.

---

#### Aspirational Criteria

**C-08 -- Blast Radius Justification**
All five: Blast Radius Rationale column pre-declared in the findings table header; "Blast Radius Rationale is required for every row" (or structural equivalent in V-04). All PASS.

**C-09 -- Cross-Sub-Skill Synthesis**
All five: SYNTHESIS section present with CROSS-SKILL label; instructions to insert into findings table with Sub-Skill = CROSS-SKILL; coverage summary includes CROSS-SKILL row. All PASS.

**C-10 -- Self-Documenting Ranking Label**
All five: `Label: "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW"` adjacent to sorted table. All PASS.

**C-11 -- Active Coverage Confirmation**
All five: Coverage Axis Gate checks for spec-gap AND contract-violation; fires correction instruction if either is absent. V-04: "If either category is absent, add the missing finding before proceeding to the Format Axis Gate." All PASS.

**C-12 -- At-Discovery Attribution**
All five: table opened before flow-lifecycle begins; each sub-skill section instructs appending rows as findings are discovered. V-04: "The findings table is opened before flow-lifecycle begins. Rows are appended as each finding is discovered." All PASS.

**C-13 -- Dedicated Synthesis Step**
All five: SYNTHESIS section structurally isolated between trace-permissions and Consolidated Findings by `---` dividers. Not embedded in a sub-skill section or appended to the report end. All PASS.

**C-14 -- Rationale Column Enforcement**
All five: table definition includes Blast Radius Rationale column before flow-lifecycle runs; empty cell would be structurally visible as omission. V-04: "The Blast Radius Rationale column is populated for every row." All PASS.

**C-15 -- CROSS-SKILL Findings as First-Class Table Citizens**
All five: SYNTHESIS instructs insertion into findings table with Sub-Skill = CROSS-SKILL; coverage summary carries CROSS-SKILL row. All PASS.

**C-16 -- 3-Slot Rationale Format**
All five: template string `[LEVEL] because [boundary] propagates to [caller/component], [effect]` present; inline example "WIDE because session-sequence-number contract propagates to flow-conversation routing and trace-contract pre-check, producing stale-state errors at both." present; Format Axis Gate enforces 3-slot format as Gate 2. Both load-bearing elements (C-27/C-28) confirmed present. All PASS.

**C-17 -- CROSS-SKILL Blast Radius Inheritance Rule**
All five: SYNTHESIS declares "CROSS-SKILL blast radius >= max(contributing sub-skills); no downgrade permitted"; requires "Inherited [LEVEL] from [sub-skill-X] ([F-ID])" provenance annotation; Inheritance Axis Gate enforces with independent correction loop. V-04: descriptive equivalents preserve all structural requirements. All PASS.

**C-18 -- Closing Confirmation Multi-Gate Enforcement**
All five: exactly three gates -- Coverage Axis Gate, Format Axis Gate, Inheritance Axis Gate -- each with an independent correction loop. V-04 uses descriptive correction language but preserves the three-gate structure and loop independence. All PASS.

**C-19 -- One-Axis-Per-Gate Rule**
All five: each gate covers one axis (coverage / format / inheritance). Three gates, one axis each. No compound gate. All PASS.

**C-20 -- Axis-Named Repair Verb**
- V-01 through V-03, V-05: Coverage = "**add** one before Format Axis Gate"; Format = "**rewrite** those cells before Inheritance Axis Gate"; Inheritance = "**fix** blast radius and annotation before closing." All name axis targets explicitly. PASS.
- V-04 (descriptive): Coverage = "add the missing finding before proceeding to the Format Axis Gate" (names coverage axis target); Format = "rewritten using the [LEVEL] / [boundary] / [caller/component] / [effect] structure" (names format axis target); Inheritance = "has its CROSS-SKILL blast radius and provenance annotation corrected before closing" (names inheritance axis target). C-34: descriptive register is register-invariant. PASS.

**C-21 -- Axis-Labeled Gate Header Encoding**
All five: "**Coverage Axis Gate**", "**Format Axis Gate**", "**Inheritance Axis Gate**" -- axis label in the header token itself, not only in the body. All PASS.

**C-22 -- Explicit Axis-Header Preamble Rule**
- V-01: `**Axis-Header Rule**: Each gate header names its axis.` in the inter-section peer slot between Synthesis and Consolidated Findings, flanked by `---` dividers. Confirmed qualifying position. PASS.
- V-02: Same labeled sentence at the end of the flow-conversation section body, after "If none: say so explicitly.", before the closing `---`. flow-conversation body is a named section body. Per C-26 (named section bodies are non-disqualifying) and C-31 (scope extends to all named section bodies), this position qualifies. Disqualifiers (gate body, example block) not met. C-32 says the closure is complete and scorers must not require additional per-body confirmation. PASS.
- V-03: Same labeled sentence at the end of the trace-contract section body, after "If none: say so explicitly.", before the closing `---`. trace-contract body has identical structural properties to all confirmed bodies. Same C-26/C-31/C-32 reasoning applies. PASS.
- V-04: Descriptive form "The closing confirmation gates are each labeled with a header that names the axis they check." -- a standalone declarative sentence placed in the flow-conversation section body (qualifying position per C-26/C-31). C-23 confirms isolation is the deciding factor; C-34 confirms register is not a deciding factor. Structurally isolated (standalone sentence before closing ---). PASS.
- V-05: `**Axis-Header Rule**: Each gate header names its axis.` in three section bodies (flow-lifecycle, trace-state, trace-permissions). C-22 satisfied at the first qualifying occurrence (flow-lifecycle body, confirmed position per R11 V-02). Second and third occurrences inert per C-33. PASS.

**C-23 -- Axis-Header Rule Isolation Primacy**
All five: the deciding factor is physical isolation from gate bodies and example blocks, not label presence. V-01 inter-section slot; V-02 flow-conversation body; V-03 trace-contract body; V-04 flow-conversation body (descriptive form, standalone sentence); V-05 three section bodies (all isolated by blank lines and `---` dividers). No position is disqualifying. All PASS.

**C-24 -- Axis-Header Rule Placement Invariance**
- V-01: inter-section peer slot (in C-24's confirmed enumeration). PASS.
- V-02: flow-conversation body -- C-25 governs; "any non-buried position" is operative; not in C-24's four enumerated positions but C-25 says the list is illustrative. PASS.
- V-03: trace-contract body -- same reasoning. PASS.
- V-04: flow-conversation body in descriptive form -- same reasoning; C-34 adds register-invariance. PASS.
- V-05: flow-lifecycle, trace-state, trace-permissions bodies -- all covered by C-25's "any non-buried position." PASS.

**C-25 -- C-24 Confirmed-Position List Is Illustrative**
- V-01: rule in confirmed inter-section position; trivial PASS.
- V-02: flow-conversation body not in C-24's four enumerated positions. C-25 governs: scorer must not deny C-22 credit solely because the position is not among the four named examples. "Any non-buried position" is operative; flow-conversation body is neither a gate body nor an example block. PASS.
- V-03: trace-contract body similarly outside the four-position list. PASS.
- V-04: flow-conversation body outside the list; same reasoning. PASS.
- V-05: flow-lifecycle body (confirmed R11 V-02), trace-state body (R10 V-04), trace-permissions body (R11 V-03) -- all within confirmed range; C-25 trivially PASS.

**C-26 -- Named Section Bodies Are Non-Disqualifying**
- V-01: rule NOT in any section body; trivial PASS.
- V-02: rule in flow-conversation body. C-26 specifies named section bodies are not disqualifying; disqualifier set is strictly gate body and example block. Flow-conversation body is neither. PASS.
- V-03: rule in trace-contract body. Same reasoning. PASS.
- V-04: rule in flow-conversation body in descriptive form. C-26 applies; C-34 adds register-invariance. PASS.
- V-05: rules in flow-lifecycle, trace-state, trace-permissions bodies. All three qualify under C-26. PASS.

**C-27 -- 3-Slot Template Load-Bearing Elements**
All five: template string and inline example both present; slot-name definition lines absent (decorative per C-27). Scorer must not withhold C-16 credit for missing definition lines when template + example are both present. All PASS.

**C-28 -- Inline Example Is Load-Bearing for C-16**
All five: inline example IS present ("WIDE because session-sequence-number contract propagates to flow-conversation routing and trace-contract pre-check, producing stale-state errors at both."). C-28's fail condition does not fire. Trivial PASS for all.

**C-29 -- C-27 Scope: Missing Example Is Not Shielded**
All five: inline example IS present. C-29's fail condition (C-27 invoked to shield a missing example) does not fire. Trivial PASS for all.

**C-30 -- C-25 Position Invariance Confirmed Across Full Prompt Span**
- V-01: rule in late inter-section slot (within confirmed invariant range). PASS.
- V-02: rule at end of flow-conversation body -- within the full prompt span; no proximity floor to gate blocks. PASS.
- V-03: trace-contract body is within the invariant range. PASS.
- V-04: flow-conversation body; same reasoning. PASS.
- V-05: flow-lifecycle body (earliest), trace-state, trace-permissions bodies; all within the confirmed full-span invariant. PASS.

**C-31 -- C-26 Named Section Bodies Are Fully Illustrative**
- V-01: rule NOT in any section body; trivial PASS.
- V-02: rule in flow-conversation body. C-31 says C-26 extends to ALL named section bodies; scorer must not restrict to previously named bodies. Flow-conversation body qualifies. PASS.
- V-03: rule in trace-contract body. C-31 extends to all named section bodies; trace-contract body qualifies. PASS.
- V-04: rule in flow-conversation body in descriptive form. C-31 extends to all named section bodies; C-34 adds register-invariance. PASS.
- V-05: rules in flow-lifecycle, trace-state, trace-permissions bodies. All three qualify under C-31. PASS.

**C-32 -- C-31 Confirmed Closed Across All Named Section Bodies**
- V-01: no section body used; trivial PASS.
- V-02: flow-conversation body is not in C-32's explicit enumeration (flow-lifecycle, trace-state, trace-permissions, Synthesis). C-32's pass condition: "Scorers must not withhold C-26 or C-31 credit on grounds that a specific named section body has not yet been individually confirmed -- the closure is complete." C-31 extends to all named section bodies; flow-conversation body has identical structural properties to all confirmed bodies. V-02 empirically confirms flow-conversation body. PASS.
- V-03: trace-contract body similarly outside C-32's explicit list. Same reasoning: C-32 says the closure is complete; scorer must not require additional per-body confirmation. V-03 empirically confirms trace-contract body. PASS.
- V-04: flow-conversation body; same reasoning as V-02. PASS.
- V-05: flow-lifecycle, trace-state, trace-permissions bodies -- all in C-32's explicit confirmed list. Trivial PASS.

**C-33 -- Dual Named Section-Body Placement Composes Cleanly**
- V-01: single inter-section slot (not a section body placement); trivial PASS.
- V-02: single section body placement (flow-conversation); trivial PASS.
- V-03: single section body placement (trace-contract); trivial PASS.
- V-04: single section body placement (flow-conversation); trivial PASS.
- V-05: three section body placements (flow-lifecycle, trace-state, trace-permissions). C-33 states "no criterion penalizes multiple qualifying placements" with no N-ceiling. First occurrence (flow-lifecycle body) satisfies C-22; second (trace-state) and third (trace-permissions) are redundant but inert. Extends R11 V-04 (N=2) to N=3. PASS.

**C-34 -- Criteria Are Structure-Sensitive, Not Register-Sensitive**
- V-01 through V-03, V-05: imperative register; C-34 confirms imperative register continues to pass (register-invariance holds in both directions). PASS.
- V-04: descriptive/explanatory register throughout. All structural requirements preserved: table pre-opened, at-discovery appending, null-result instructions in each section, 3-slot template + inline example, three axis-labeled gate headers, independent correction loops, axis-named repair language, provenance annotation format, CROSS-SKILL insertion rule, sort label. C-34 confirms descriptive register scores identically to imperative when all structural elements are present. PASS.

---

### Composite Score Summary

| Variation | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 | C-19 | C-20 | C-21 | C-22 | C-23 | C-24 | C-25 | C-26 | C-27 | C-28 | C-29 | C-30 | C-31 | C-32 | C-33 | C-34 | Score |
|-----------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-------|
| V-01 | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | **100** |
| V-02 | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | **100** |
| V-03 | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | **100** |
| V-04 | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | **100** |
| V-05 | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | **100** |

---

### Excellence Signals

**From V-02 + V-03 (C-32 empirical closure)**
C-32 claimed the full sub-skill section body sequence was confirmed, but its explicit enumeration listed only four bodies (flow-lifecycle, trace-state, trace-permissions, Synthesis), leaving flow-conversation (position 2) and trace-contract (position 4) untested. V-02 and V-03 fill both gaps at 27/27. The complete individual confirmation record is now:
- Position 1: flow-lifecycle body (R11 V-02)
- Position 2: flow-conversation body (R12 V-02)
- Position 3: trace-state body (R10 V-04)
- Position 4: trace-contract body (R12 V-03)
- Position 5: trace-permissions body (R11 V-03)
- Synthesis body (R9 V-04)

All six named positions confirmed. The disqualifier set remains strictly: gate body and example block. No named section body has ever failed.

**From V-04 (C-34 + C-31 composition)**
The first test combining descriptive register (C-34, confirmed R11 V-05) with section-body placement (C-31, confirmed R11 V-02/V-03) scores identically to either property in isolation. The descriptive standalone declarative sentence "The closing confirmation gates are each labeled with a header that names the axis they check." in the flow-conversation body satisfies C-22 without any penalty. C-23's isolation primacy, C-34's register-invariance, and C-26/C-31's section-body qualification are orthogonal criteria that compose without interaction.

**From V-05 (C-33 N-ceiling)**
C-33's "no criterion penalizes multiple qualifying placements" has no implicit N-ceiling. The pattern generalizes: N=1 (any single confirmed position), N=2 (R11 V-04, R8 V-05), N=3 (R12 V-05). The first qualifying occurrence satisfies C-22; all subsequent qualifying occurrences are inert. The ceiling is the number of available qualifying positions in the prompt, not an arbitrary count limit.

---

### Design Notes for R13

1. **All sub-skill section bodies individually confirmed.** The C-32 empirical program is complete. No further section-body confirmation probes are needed for existing sub-skills.

2. **C-34 + C-31 composition confirmed.** Descriptive register + section body is a validated combination. Mixed-register variations would yield no new information.

3. **C-33 N-ceiling removed.** N=3 confirmed. N=4 or N=5 would add no new information; C-33 is fully characterized.

4. **Candidate new axes for R13**: The format and placement program is exhausted. Structural stress-tests on correctness and coverage criteria remain open: (a) gate count stress-test -- fewer than three gates (omit one axis gate) targets C-18 and C-19; (b) CROSS-SKILL provenance omission -- targets C-17; (c) table pre-opening delay (table opened after first sub-skill runs) -- targets C-12 and C-14; (d) null-result omission in one section -- targets C-07; (e) 3-slot template with inline example removed -- targets C-16 and C-28.

5. **R12 V-01 reconfirms the production baseline at 27/27 under the expanded v12 rubric.** Three new criteria (C-32, C-33, C-34) all trivially pass for the canonical inter-section peer slot form. The production baseline is stable.
