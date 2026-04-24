**rhythm-behavior R9 scored.** Scorecard written to `simulations/quest/scorecards/rhythm-behavior-scorecard-R9-2026-03-17.md`.

---

### Results

| Variation | Essential | Recommended | Aspirational | Composite | Golden |
|-----------|-----------|-------------|--------------|-----------|--------|
| V-01 | 4/4 | 3/3 | 17/17 | **100** | YES |
| V-02 | 4/4 | 3/3 | 17/17 | **100** | YES |
| V-03 | 4/4 | 3/3 | 17/17 | **100** | YES |
| V-04 | 4/4 | 3/3 | 17/17 | **100** | YES |
| V-05 | 4/4 | 3/3 | 17/17 | **100** | YES |

**5/5 golden.** All three open questions from R9 resolved:

1. **V-02/V-03 PASS** -- C-24's confirmed list is illustrative, not exhaustive. "Any non-buried position" is the operative clause. The mid-sub-skill divider-flanked slot (between trace-state and trace-contract) qualifies. V-02 and V-03 produce identical verdicts -- position is the variable, label form is neutral.

2. **V-04 PASS** -- Synthesis section body is not a gate body and not an example block. No third disqualifier exists. A standalone labeled paragraph inside a named section body qualifies under "any non-buried position."

3. **V-05 PASS** -- Stripping slot-name definition lines (`[boundary] = ...` etc.) and the enforcement note does not cause C-16 to regress. The template string and inline example are the load-bearing elements.

**Production candidate updated to V-05** (minimal form confirmed golden at 17/17; slot-name definitions and enforcement note confirmed decorative at zero criteria cost).

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-24 confirmed-position list is illustrative not exhaustive -- 'any non-buried position' is the operative clause; a mid-sub-skill divider-flanked slot passes C-22 equivalently to the four explicitly confirmed positions; no proximity to gate blocks is required", "Named section bodies are not disqualifying positions under C-22 -- a standalone labeled paragraph inside the Synthesis section body passes C-22; the disqualifier set is strictly gate body + example block; 'buried' does not extend to named section bodies", "Slot-name definition lines and enforcement note are decorative relative to C-16 -- C-16's load-bearing elements are the 3-slot template string and at least one inline example; stripping explanation lines leaves C-16 fully satisfied"]}
```
ock (V-04: Synthesis section body qualifies).
3. Slot-name definition lines are decorative relative to C-16 (V-05: template + example are the load-bearing elements).

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-24 confirmed-position list is illustrative not exhaustive -- 'any non-buried position' is the operative clause; a mid-sub-skill divider-flanked slot (between trace-state and trace-contract) passes C-22 equivalently to the four explicitly confirmed positions (top-of-prompt, pre-gate preamble, inter-section Synthesis/Consolidated slot, dual placement); no proximity to gate blocks is required", "Named section bodies are not disqualifying positions under C-22 -- a standalone labeled paragraph inside the Synthesis section body (after the If-none terminator, before the closing --- divider) passes C-22; the disqualifier set is strictly gate body + example block; 'buried' does not extend to named section bodies", "Slot-name definition lines and enforcement note are decorative relative to C-16 -- C-16's load-bearing elements are the 3-slot template string ([LEVEL] because [boundary] propagates to [caller/component], [effect]) and at least one inline example; stripping [boundary] = ..., [caller/component] = ..., [effect] = ... explanation lines and the no-generic-phrases note leaves C-16 fully satisfied"]}
```

---

### Per-Criterion Verdicts

#### Essential Criteria

**C-01 -- Declared Execution Sequence**
All five: "Sections in this exact order: flow-lifecycle, flow-conversation, trace-state, trace-contract, trace-permissions, SYNTHESIS, Consolidated Findings." appears before any findings. Order and completeness both present. All PASS.

**C-02 -- Single Unified Report**
All five: "Write everything as one document from start to finish. Do not promise to continue." All PASS.

**C-03 -- Blast Radius Ranking Present**
All five: sort label "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW" structurally adjacent to the sorted table. All PASS.

**C-04 -- Spec Gap and Contract Violation Coverage**
All five define spec-gap and contract-violation in "What to look for." Coverage Axis Gate requires both and fires a correction loop if either is absent. All PASS.

#### Recommended Criteria

**C-05 -- Per-Finding Sub-Skill Attribution**
All five pre-open findings table with Sub-Skill column before flow-lifecycle; rows appended at discovery. Attribution is structural, not retroactive. All PASS.

**C-06 -- Actionable Next Step for Top Finding**
All five: "Top finding: one concrete next step naming the exact spec section, boundary, or component a developer must address before writing implementation code." All PASS.

**C-07 -- Sub-Skill Section Completeness**
All five: "If a phase has no findings, say so briefly" in flow-lifecycle; "If none: say so explicitly" in each subsequent section. All PASS.

#### Aspirational Criteria

**C-08 -- Blast Radius Justification**
All five mandate Blast Radius Rationale column pre-opened with the table, required for every row. 3-slot format excludes generic phrases. All PASS.

**C-09 -- Cross-Sub-Skill Synthesis**
All five: dedicated SYNTHESIS section with CROSS-SKILL label, row insertion into findings table with Sub-Skill = CROSS-SKILL required. All PASS.

**C-10 -- Self-Documenting Ranking Label**
All five: label string "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW" structurally adjacent to the sorted table. All PASS.

**C-11 -- Active Coverage Confirmation**
All five: Coverage Axis Gate checks for spec-gap and contract-violation presence and fires a correction loop if either is absent. All PASS.

**C-12 -- At-Discovery Attribution**
All five: findings table pre-opened with all columns before flow-lifecycle begins; rows appended as findings are discovered. All PASS.

**C-13 -- Dedicated Synthesis Step**
All five: SYNTHESIS section structurally isolated between trace-permissions and Consolidated Findings. All PASS.

**C-14 -- Rationale Column Enforcement**
All five: Blast Radius Rationale column included in pre-opened table definition before flow-lifecycle. All PASS.

**C-15 -- CROSS-SKILL Findings as First-Class Table Citizens**
All five: SYNTHESIS instructs insertion of CROSS-SKILL findings into the main findings table; coverage summary includes CROSS-SKILL row. All PASS.

**C-16 -- 3-Slot Rationale Format**
All five declare `[LEVEL] because [boundary] propagates to [caller/component], [effect]` with all three slots named and an inline example in "What to look for." Format re-enforced in Format Axis Gate with a correction loop.

V-05 note: Slot-name definition lines (`[boundary] = named API boundary...` etc.) and enforcement note ("All three slots must be specific -- no generic phrases.") are stripped. The template string and example are preserved unchanged. C-16 requires the template string and an example -- not the slot-name definitions. PASS.

All PASS.

**C-17 -- CROSS-SKILL Blast Radius Inheritance Rule**
All five: SYNTHESIS declares >= max rule ("no downgrade permitted") and requires "Inherited [LEVEL] from [sub-skill-X] ([F-ID])" provenance annotation. Inheritance Axis Gate enforces with an independent correction loop. All PASS.

**C-18 -- Closing Confirmation Multi-Gate Enforcement**

| V | Gate 1 loop | Gate 2 loop | Gate 3 loop | Result |
|---|------------|------------|------------|--------|
| V-01 | YES (add before Format Axis Gate) | YES (rewrite before Inheritance Axis Gate) | YES (fix before closing) | PASS |
| V-02 | YES (add before Format Axis Gate) | YES (rewrite before Inheritance Axis Gate) | YES (fix before closing) | PASS |
| V-03 | YES (add before Format Axis Gate) | YES (rewrite before Inheritance Axis Gate) | YES (fix before closing) | PASS |
| V-04 | YES (add before Format Axis Gate) | YES (rewrite before Inheritance Axis Gate) | YES (fix before closing) | PASS |
| V-05 | YES (add before Format Axis Gate) | YES (rewrite before Inheritance Axis Gate) | YES (fix before closing) | PASS |

All five have exactly three gates, each covering one axis, each with an independent correction loop. All PASS.

**C-19 -- One-Axis-Per-Gate Rule**

| V | Gate 1 axis | Gate 2 axis | Gate 3 axis | Any compound? | Result |
|---|-------------|-------------|-------------|---------------|--------|
| V-01 | coverage only | format only | inheritance only | NO | PASS |
| V-02 | coverage only | format only | inheritance only | NO | PASS |
| V-03 | coverage only | format only | inheritance only | NO | PASS |
| V-04 | coverage only | format only | inheritance only | NO | PASS |
| V-05 | coverage only | format only | inheritance only | NO | PASS |

All PASS.

**C-20 -- Axis-Named Repair Verb**

| V | Gate 1 verb | Gate 2 verb | Gate 3 verb | C-20 verdict |
|---|-------------|-------------|-------------|--------------|
| V-01 | **add** | **rewrite** | **fix** | PASS |
| V-02 | **add** | **rewrite** | **fix** | PASS |
| V-03 | **add** | **rewrite** | **fix** | PASS |
| V-04 | **add** | **rewrite** | **fix** | PASS |
| V-05 | **add** | **rewrite** | **fix** | PASS |

All PASS.

**C-21 -- Axis-Labeled Gate Header Encoding**

| V | Gate 1 header | Gate 2 header | Gate 3 header | Axis word in header? | C-21 verdict |
|---|---------------|---------------|---------------|----------------------|--------------|
| V-01 | Coverage Axis Gate | Format Axis Gate | Inheritance Axis Gate | YES | PASS |
| V-02 | Coverage Axis Gate | Format Axis Gate | Inheritance Axis Gate | YES | PASS |
| V-03 | Coverage Axis Gate | Format Axis Gate | Inheritance Axis Gate | YES | PASS |
| V-04 | Coverage Axis Gate | Format Axis Gate | Inheritance Axis Gate | YES | PASS |
| V-05 | Coverage Axis Gate | Format Axis Gate | Inheritance Axis Gate | YES | PASS |

All PASS.

**C-22 -- Explicit Axis-Header Preamble Rule**

| V | Rule form | Rule location | Standalone? | C-22 verdict |
|---|-----------|---------------|-------------|--------------|
| V-01 | Labeled paragraph: `**Axis-Header Rule**: Each gate header names its axis.` | Own inter-section slot between Synthesis and Consolidated Findings (flanked by `---` dividers) | YES -- peer section; confirmed qualifying position (R8 V-04) | **PASS** |
| V-02 | Labeled paragraph: `**Axis-Header Rule**: Each gate header names its axis.` | Mid-sub-skill inter-section slot between trace-state and trace-contract (flanked by `---` dividers) | YES -- not gate body, not example block; C-24's "any non-buried" operative clause applies | **PASS** |
| V-03 | Bare sentence: `Each gate header names its axis.` | Mid-sub-skill inter-section slot between trace-state and trace-contract (flanked by `---` dividers) | YES -- bare form + qualifying position; C-23 isolation primacy holds | **PASS** |
| V-04 | Labeled paragraph: `**Axis-Header Rule**: Each gate header names its axis.` | Synthesis section body (after "If none" terminator, before closing `---` divider) | YES -- dedicated labeled paragraph inside named section body; not gate body, not example block | **PASS** |
| V-05 | Labeled paragraph: `**Axis-Header Rule**: Each gate header names its axis.` | Own inter-section slot between Synthesis and Consolidated Findings (minimal form) | YES -- identical to V-01; stripping elsewhere does not affect rule placement | **PASS** |

**V-02 PASS**: The mid-sub-skill slot (between trace-state and trace-contract, flanked by `---` dividers) is not a gate body and not an example block. C-24's operative clause "any non-buried position within the prompt is a qualifying placement" governs. The confirmed list in C-24 documents positions that have been tested -- it is not a whitelist. A divider-flanked inter-section slot at any point in the prompt satisfies "any non-buried position." No proximity constraint to the gate blocks was invented.

**V-03 PASS**: Bare form in the same mid-sub-skill position as V-02. C-23 establishes that physical isolation is the decisive factor -- not label presence. The position qualifies (V-02). The bare form qualifies (C-23 + R8 V-01). V-02 and V-03 produce identical criterion verdicts; the label variable is confirmed neutral when the position variable is already qualifying.

**V-04 PASS**: The Synthesis section body is not a gate body and not an example block. C-22's pass condition reads "an independent instruction in the preamble or a dedicated labeled paragraph." The rule in V-04 IS a dedicated labeled paragraph (`**Axis-Header Rule**:` prefix, physically isolated by line breaks within the section body). The fact that it sits inside the Synthesis section rather than in its own inter-section slot does not disqualify it -- C-22 names two disqualifying positions (gate body, example block) and no others. C-24 confirms: "The only failing positions are those explicitly disqualified by C-22." Third disqualifier does not exist.

**C-23 -- Axis-Header Rule Isolation Primacy**

| V | Form | Position | Isolation decisive? | C-23 verdict |
|---|------|----------|---------------------|--------------|
| V-01 | Labeled | Inter-section peer slot (confirmed) | YES -- labeled form in confirmed qualifying position; label is decorative | PASS |
| V-02 | Labeled | Mid-sub-skill slot (new) | YES -- labeled form in newly confirmed qualifying position; label did not cause pass | PASS |
| V-03 | Bare | Mid-sub-skill slot (new) | YES -- bare form in qualifying position passes equivalently to labeled form | PASS |
| V-04 | Labeled | Synthesis section body (new) | YES -- labeled form in Synthesis section body; label decorative, position qualifying | PASS |
| V-05 | Labeled | Inter-section peer slot (confirmed) | YES -- identical to V-01; label decorative | PASS |

All PASS. V-03 is the strongest C-23 demonstration in R9: bare form in a new qualifying position confirms isolation primacy at both the form dimension (bare vs. labeled) and the position dimension (mid-sub-skill, newly confirmed). V-02 and V-03 as a controlled pair cleanly separate position from label as the decisive variable.

**C-24 -- Axis-Header Rule Placement Invariance**

| V | Position | In confirmed list? | Non-buried? | Proximity constraint invented? | C-24 verdict |
|---|----------|-------------------|-------------|-------------------------------|--------------|
| V-01 | Inter-section slot (Synthesis/Consolidated boundary) | YES | YES | NO | PASS |
| V-02 | Mid-sub-skill slot (trace-state/trace-contract boundary) | NO (new) | YES -- flanked by dividers, not in gate body or example block | NO | PASS |
| V-03 | Mid-sub-skill slot (same as V-02) | NO (new) | YES | NO | PASS |
| V-04 | Synthesis section body (final element before ---) | NO (new) | YES -- standalone paragraph, not embedded in gate or example | NO | PASS |
| V-05 | Inter-section slot (same as V-01) | YES | YES | NO | PASS |

V-02, V-03, V-04 each test a position not previously in C-24's confirmed list. All three pass because none occupies a gate body or example block, and no scorer invented a proximity constraint. The confirmed list gains three new entries (V-02 and V-03 share the same position; V-04 adds the Synthesis section body). All PASS.

---

### Hypothesis Verdicts

| Hypothesis | Verdict | Evidence |
|------------|---------|----------|
| V-01: R8 V-04 baseline remains golden under v9 (17/17) | CONFIRMED | All new criteria C-23/C-24 pass at the inter-section slot; 17/17 |
| V-02: Mid-sub-skill divider-flanked slot qualifies under C-24's "any non-buried" clause | CONFIRMED | C-24's confirmed list is illustrative; mid-sub-skill inter-section slot is not buried; PASS |
| V-03: Bare form in mid-sub-skill position passes equivalently to labeled form | CONFIRMED | Position variable (V-02) qualifies; label variable is neutral (C-23); V-03 = V-02 on all 17 criteria |
| V-04: Synthesis section body is not a disqualifying position under C-22 | CONFIRMED | C-22 names two disqualifiers (gate body, example block); Synthesis section body is neither; no third disqualifier |
| V-05: Slot-name definition lines are decorative relative to C-16 | CONFIRMED | C-16 load-bearing elements (template string + example) preserved; stripped lines do not appear in C-16 pass condition |

---

### C-22 Structural Map (cumulative through R9)

| Form | Location | C-22 result | Round confirmed |
|------|----------|-------------|-----------------|
| Inside gate body (any sentence form) | Gate body | FAIL | R7 V-01 |
| Parenthetical in example block | Example block | FAIL | R7 V-02 |
| Sentence appended to preamble paragraph | Preamble-chain (attached) | PASS | R7 V-03 |
| Dedicated labeled paragraph | Pre-gate preamble of Consolidated Findings | PASS | R7 V-04 |
| Dedicated labeled paragraph with positional prefix headers | Pre-gate preamble | PASS | R7 V-05 |
| Bare standalone paragraph (no bold label) | Pre-gate preamble of Consolidated Findings | PASS | R8 V-01 |
| Dedicated labeled paragraph | Top of prompt (canonical preamble) | PASS | R8 V-02 |
| Two-sentence dedicated labeled paragraph | Pre-gate preamble of Consolidated Findings | PASS | R8 V-03 |
| Dedicated labeled paragraph | Own inter-section slot (Synthesis / Consolidated Findings boundary) | PASS | R8 V-04 |
| Dedicated labeled paragraph (dual: early + late) | "What to look for" + Consolidated Findings | PASS | R8 V-05 |
| Dedicated labeled paragraph | Mid-sub-skill inter-section slot (trace-state / trace-contract boundary) | PASS | **R9 V-02** |
| Bare standalone sentence | Mid-sub-skill inter-section slot (trace-state / trace-contract boundary) | PASS | **R9 V-03** |
| Dedicated labeled paragraph (inside named section body) | Synthesis section body (final element before closing ---) | PASS | **R9 V-04** |
| Dedicated labeled paragraph (minimal: slot-name defs stripped elsewhere) | Own inter-section slot (minimal form) | PASS | **R9 V-05** |

**Disqualifying locations** (confirmed R7, still operative): gate body; example block (parenthetical annotation).
**Qualifying locations** (confirmed R7+R9): any non-buried, non-inlined standalone position across the full prompt -- including mid-sub-skill inter-section slots and named section bodies.
**Structural requirement**: physical isolation from gate bodies and example blocks. Position within the prompt (early/mid/late) is irrelevant. Bold label is recommended for scannability; not required for C-22 compliance.

---

### Excellence Signals

From R9 (five-way 100/100 confirmation under v9 denominator):

1. **C-24's "any non-buried position" clause is unconditional**: The confirmed-position list in C-24 documents positions that have been tested -- it is not a whitelist. Any divider-flanked inter-section slot anywhere in the prompt qualifies. Proximity to the gate blocks is irrelevant. Prompt engineers can place the Axis-Header Rule at any structurally isolated location without scoring risk.

2. **Named section bodies are qualifying positions when the rule is standalone**: A dedicated labeled paragraph at the end of the Synthesis section body (after the "If none" terminator, before the closing divider) passes C-22. The disqualifier set is strictly gate body + example block. Embedding the rule as the final element of any named section works as long as it remains a standalone paragraph, not embedded in a narrative sentence or list item.

3. **Controlled pair design (V-02/V-03) efficiently closes multi-variable uncertainty**: By holding position constant and varying label form, the R9 design confirms both variables independently with two variations instead of four. V-02 PASS isolates the position variable; V-03 PASS confirms label-neutrality at that position. This pair architecture is the minimum-variation design for two-variable uncertainty resolution.

4. **Slot-name definitions are decorative overhead for C-16**: The template string and the inline example are the full load-bearing content of C-16. The `[boundary] = named API boundary...` explanation lines and the "All three slots must be specific" enforcement note can be stripped from production prompts at zero criteria cost, reducing prompt mass while preserving full rubric compliance.

---

### Composite Score Formula (confirmed)

Score = 100 - (0.8 x failed aspirational criteria)
Essential and recommended are threshold gates (all must pass for golden status).

R9: 17 aspirational criteria. All five variations fail 0 = **100**.

---

### Round History

| Round | Rubric | Top Score | Golden Count | Production Candidate |
|-------|--------|-----------|--------------|---------------------|
| R1 | v1 | 90 | 1/5 (V-05) | V-05 |
| R2 | v2 | 100 | 2/5 (V-04, V-05) | V-04 |
| R3 | v3 | 100 | 5/5 | V-05 (quality + minimal) |
| R4 | v4 | 100 | 4/5 (V-01, V-03, V-04, V-05) | V-05 (18/18 + minimal) |
| R5 | v5 | 100 | 4/5 (V-01, V-03, V-04, V-05) | V-05 (20/20 + minimal) |
| R6 | v6 | 100 | 4/5 (V-01, V-03, V-04, V-05) | V-05 (21/21 + minimal) |
| R7 | v7 | 100 | 3/5 (V-03, V-04, V-05) | V-04 (22/22 + minimal) |
| R8 | v8 | 100 | 5/5 | V-04 (bold label decorative confirmed; bare-preamble equivalent) |
| **R9** | **v9** | **100** | **5/5** | **V-05 (minimal form confirmed golden at 17/17; slot-name defs decorative)** |

**R9 decision**: Post-closure consolidation confirmed. All three open questions resolved: (1) C-24's confirmed list is non-exhaustive -- "any non-buried" is operative and extends to mid-sub-skill slots and named section bodies; (2) Synthesis section body is not a disqualifying position; (3) slot-name definition lines are decorative relative to C-16. V-05 (minimal form) is elevated to production candidate: it achieves 17/17 at minimum prompt mass, confirming that the slot-name definitions and enforcement note were decorative overhead. V-01/V-04 (inter-section labeled) remain valid alternatives for teams that prefer maximum scannability. The C-22 structural map is now exhaustive -- every tested form-position combination is documented and no new disqualifiers exist beyond gate body and example block.
