**rhythm-behavior R10 scored.** Scorecard written to `simulations/quest/scorecards/rhythm-behavior-scorecard-R10-2026-03-17.md`.

---

### Results

| Variation | Essential | Recommended | Aspirational | Composite | Golden |
|-----------|-----------|-------------|--------------|-----------|--------|
| V-01 | 4/4 | 3/3 | 20/20 | **100** | YES |
| V-02 | 4/4 | 3/3 | 19/20 | **99.2** | NO |
| V-03 | 4/4 | 3/3 | 20/20 | **100** | YES |
| V-04 | 4/4 | 3/3 | 20/20 | **100** | YES |
| V-05 | 4/4 | 3/3 | 20/20 | **100** | YES |

**4/5 golden.** All five open questions resolved:

1. **C-16 load-bearing boundary closed**: Stripping the inline example causes C-16 to FAIL (V-02). Together with R9 V-05 (stripping slot-name defs does not fail C-16), the exact minimum is now known: template string + inline example = required; everything else = decorative.

2. **C-27 not implicated when example is genuinely absent** (V-02): C-27 only fires when a scorer wrongly denies C-16 credit despite both template and example being present. It does not shield a prompt that truly lacks the example.

3. **C-25 confirmed across full prompt span** (V-03): The earliest possible inter-section gap (flow-lifecycle/flow-conversation boundary) is a qualifying position. No proximity floor to gate blocks exists.

4. **C-26 extends to all named section bodies** (V-04): "e.g." in C-26 is genuinely illustrative. The trace-state section body qualifies on equal footing with the Synthesis section body confirmed in R9.

5. **V-05 = V-03 structurally**: The intended two-variable combination was not new -- V-03 already carries minimal form. V-05 is a duplicate confirmation at zero information gain. Design note: verify combination novelty before writing prompts.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Inline example is load-bearing for C-16 -- template alone is insufficient; minimum satisfying content is template string + inline example; slot-name defs and enforcement note are decorative", "C-27 does not shield a missing-example prompt -- C-27 fires only when C-16 is wrongly denied despite both template and example being present; genuinely absent example correctly fails C-16 without implicating C-27", "C-25 'any non-buried position' confirmed across full prompt span -- earliest inter-section gap (flow-lifecycle/flow-conversation boundary) qualifies identically to latest (Synthesis/Consolidated boundary); no proximity floor exists", "C-26 extends to all named section bodies -- 'e.g.' in C-26 is illustrative; trace-state section body qualifies equivalently to Synthesis body; disqualifier set is strictly gate body and example block"]}
```
ine example is the load-bearing element for C-16 -- stripping the example from the 3-slot Blast Radius Rationale definition causes C-16 to fail regardless of template string presence; the load-bearing boundary is template string + inline example; slot-name defs confirmed decorative in R9; example confirmed required in R10; together they define C-16's minimum satisfying content precisely", "C-27 does not shield a missing-example prompt from C-16 failure -- C-27's fail condition fires only when a scorer wrongly denies C-16 credit from a prompt containing BOTH template and example solely because slot-name defs are absent; when the example is genuinely absent the C-16 failure is appropriate and C-27 is not implicated", "C-25 'any non-buried position' invariance confirmed across the full prompt span -- the flow-lifecycle/flow-conversation inter-section gap (earliest possible position) qualifies equivalently to the Synthesis/Consolidated boundary (latest confirmed position); no proximity floor to gate blocks exists anywhere in the prompt", "C-26 extends to all named section bodies not Synthesis exclusively -- the 'e.g.' in C-26 is genuinely illustrative; a standalone labeled paragraph at the end of the trace-state section body (after null-result instruction, before closing divider) passes C-22 on equal footing with the Synthesis section body; the disqualifier set is strictly gate body and example block"]}
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

| V | Template string | Inline example | Slot-name defs | C-16 verdict |
|---|----------------|---------------|----------------|--------------|
| V-01 | PRESENT | PRESENT | ABSENT | PASS |
| V-02 | PRESENT | **ABSENT** | ABSENT | **FAIL** |
| V-03 | PRESENT | PRESENT | ABSENT | PASS |
| V-04 | PRESENT | PRESENT | ABSENT | PASS |
| V-05 | PRESENT | PRESENT | ABSENT | PASS |

**V-02 FAIL**: C-16 requires the template string AND at least one inline example. V-02 retains the template string but removes the `Example: "WIDE because..."` line entirely. Template alone does not satisfy C-16. This is the expected failure closing the R10 load-bearing boundary probe.

All others PASS. Format Axis Gate enforces with a correction loop in all five.

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
| V-01 | Labeled paragraph: `**Axis-Header Rule**: Each gate header names its axis.` | Own inter-section slot between Synthesis and Consolidated Findings (flanked by `---` dividers) | YES -- confirmed qualifying position (R8 V-04) | **PASS** |
| V-02 | Labeled paragraph: `**Axis-Header Rule**: Each gate header names its axis.` | Own inter-section slot between Synthesis and Consolidated Findings (flanked by `---` dividers) | YES -- identical position to V-01; C-16 fail is unrelated to C-22 | **PASS** |
| V-03 | Labeled paragraph: `**Axis-Header Rule**: Each gate header names its axis.` | Earliest inter-section slot: flow-lifecycle/flow-conversation boundary (flanked by `---` dividers) | YES -- not inside any section body, not gate body, not example block; C-25 "any non-buried position" governs | **PASS** |
| V-04 | Labeled paragraph: `**Axis-Header Rule**: Each gate header names its axis.` | trace-state section body (after "If none: say so explicitly", before closing `---` divider) | YES -- standalone labeled paragraph inside named section body; C-26 confirms non-disqualifying | **PASS** |
| V-05 | Labeled paragraph: `**Axis-Header Rule**: Each gate header names its axis.` | Earliest inter-section slot: flow-lifecycle/flow-conversation boundary (flanked by `---` dividers) | YES -- identical position and form to V-03; structural duplicate | **PASS** |

**V-03 PASS**: The flow-lifecycle/flow-conversation inter-section slot is the earliest possible position in the prompt, maximally distant from the closing gate blocks. C-25 states the operative clause is "any non-buried position" with no proximity requirement. The slot is flanked by `---` dividers and sits between two named sections without being embedded in either body. Not a gate body; not an example block. No proximity constraint invented.

**V-04 PASS**: C-26 states "Named section bodies (e.g., the Synthesis section body, positioned after a null-result terminator and before a closing divider) are not disqualifying positions under C-22." The "e.g." signals Synthesis is an example of the class "named section bodies," not an exclusive singleton. The trace-state section has a null-result instruction ("If none: say so explicitly") followed by a closing `---` divider -- exact structural parallel to the Synthesis section body confirmed in R9 V-04. The disqualifier set is strictly gate body + example block; trace-state section body is neither.

**V-05 = V-03 structurally**: Prompt text of V-05 is identical to V-03. The intended distinction (V-03's early position combined with V-01's stripped-definition form) is not present because V-03 already carries minimal form. V-05 is a compositional confirmation at zero new information gain.

**C-23 -- Axis-Header Rule Isolation Primacy**

| V | Form | Position | Isolation decisive? | C-23 verdict |
|---|------|----------|---------------------|--------------|
| V-01 | Labeled | Inter-section peer slot (Synthesis/Consolidated, confirmed R8) | YES -- labeled form in confirmed qualifying position | PASS |
| V-02 | Labeled | Inter-section peer slot (Synthesis/Consolidated, confirmed R8) | YES -- C-16 failure irrelevant to C-22/C-23 | PASS |
| V-03 | Labeled | Earliest inter-section slot (flow-lifecycle/flow-conversation, new) | YES -- labeled form in newly confirmed qualifying position | PASS |
| V-04 | Labeled | trace-state section body (new) | YES -- labeled form in named section body; C-26 governs; isolation from gate body and example block is deciding factor | PASS |
| V-05 | Labeled | Earliest inter-section slot (same as V-03) | YES -- identical to V-03 | PASS |

All PASS.

**C-24 -- Axis-Header Rule Placement Invariance**

| V | Position | In confirmed list? | Non-buried? | Proximity constraint invented? | C-24 verdict |
|---|----------|-------------------|-------------|-------------------------------|--------------|
| V-01 | Inter-section slot (Synthesis/Consolidated boundary) | YES | YES | NO | PASS |
| V-02 | Inter-section slot (Synthesis/Consolidated boundary) | YES | YES | NO | PASS |
| V-03 | Earliest inter-section slot (flow-lifecycle/flow-conversation boundary) | NO (new) | YES -- flanked by dividers, not in gate body or example block; C-25 extends C-24's list | NO | PASS |
| V-04 | trace-state section body (after null-result, before closing ---) | NO (new) | YES -- standalone paragraph in named section body; C-26 confirms; C-25 extends list | NO | PASS |
| V-05 | Earliest inter-section slot (same as V-03) | NO (confirmed by V-03 in this round) | YES | NO | PASS |

V-03 and V-04 each test a position not previously in C-24's confirmed list. Both pass under C-25's "any non-buried position" operative clause without invoking a proximity constraint.

**C-25 -- C-24 Confirmed-Position List Is Illustrative**

| V | C-22 position in confirmed list? | C-25 application | C-25 verdict |
|---|----------------------------------|------------------|--------------|
| V-01 | YES (confirmed R8) | Trivially passes -- no controversy about non-listed position | PASS |
| V-02 | YES (confirmed R8) | Trivially passes | PASS |
| V-03 | NO -- earliest inter-section gap not previously listed | C-25 applies: "any non-buried position" operative clause covers this divider-flanked inter-section slot; list is illustrative, not exhaustive | **PASS** |
| V-04 | NO -- trace-state section body not previously listed | C-25 applies: non-listed position covered by "any non-buried" clause | **PASS** |
| V-05 | NO (same as V-03, confirmed by V-03 in this round) | C-25 applies: list illustrative | PASS |

**V-03 and V-04** are the operative tests for C-25: both use positions not in the confirmed list, and both pass, confirming C-24's enumeration is a documentation of tested positions, not a whitelist.

**C-26 -- Named Section Bodies Are Non-Disqualifying**

| V | Rule inside named section body? | Section body type | C-26 verdict |
|---|--------------------------------|-------------------|--------------|
| V-01 | NO -- rule is in own inter-section slot | N/A | PASS (trivially) |
| V-02 | NO -- rule is in own inter-section slot | N/A | PASS (trivially) |
| V-03 | NO -- rule is in own inter-section slot | N/A | PASS (trivially) |
| V-04 | YES -- rule is inside trace-state section body | Non-Synthesis named section body | **PASS -- C-26 extends to all named section bodies; "e.g." in C-26 confirmed illustrative; disqualifier set is strictly gate body + example block** |
| V-05 | NO -- rule is in own inter-section slot | N/A | PASS (trivially) |

**V-04 is the operative test for C-26**: R9 V-04 confirmed the Synthesis section body. R10 V-04 tests whether C-26's "e.g." is genuinely illustrative by placing the rule in the trace-state section body. The structural pattern is identical (after null-result instruction, before closing divider). C-26 states the disqualifier set is strictly gate body + example block -- not "named section bodies outside of Synthesis." V-04 PASS confirms C-26 extends to the full class of named section bodies.

**C-27 -- 3-Slot Template Load-Bearing Elements**

| V | Template present? | Example present? | Slot-name defs? | C-16 verdict | C-27 verdict |
|---|------------------|-----------------|-----------------|--------------|--------------|
| V-01 | YES | YES | ABSENT | PASS | PASS (no improper C-16 denial) |
| V-02 | YES | **ABSENT** | ABSENT | **FAIL** | **PASS** -- C-16 correctly fails because example genuinely absent; C-27 not implicated |
| V-03 | YES | YES | ABSENT | PASS | PASS |
| V-04 | YES | YES | ABSENT | PASS | PASS |
| V-05 | YES | YES | ABSENT | PASS | PASS |

**V-02 is the operative test for C-27**: C-27's fail condition fires only when a scorer denies C-16 credit from a prompt that has BOTH template AND example, solely because slot-name defs are absent. In V-02, the example is genuinely absent -- the C-16 failure is appropriate and C-27 does not protect V-02. C-27 PASS. This confirms C-27's pass condition is precise: it guards against false C-16 denials, not against true ones.

---

### Hypothesis Verdicts

| Hypothesis | Verdict | Evidence |
|------------|---------|----------|
| V-01: R9 V-05 production form scores 20/20 under v10 denominator | CONFIRMED | All three new criteria (C-25, C-26, C-27) pass trivially for this form; 20/20 |
| V-02: Stripping the inline example causes C-16 to fail | CONFIRMED | C-16 pass condition requires template string AND example; template alone insufficient; C-16 FAIL |
| V-02: Stripping the inline example does NOT cause C-27 to fail | CONFIRMED | C-27 fires only when C-16 is wrongly denied when both template and example present; V-02 lacks the example, so C-16 failure is appropriate; C-27 PASS |
| V-03: Earliest inter-section gap qualifies under C-25 "any non-buried position" | CONFIRMED | flow-lifecycle/flow-conversation boundary slot is flanked by dividers, outside all section bodies and gate blocks; PASS |
| V-04: C-26 extends to non-Synthesis named section bodies | CONFIRMED | trace-state section body is structurally parallel to Synthesis body; C-26's "e.g." confirmed illustrative; disqualifier set unchanged; PASS |
| V-05: V-03 position + minimal form compose without regression | CONFIRMED (trivially) | V-05 prompt is structurally identical to V-03; both carry early position + minimal form; no regression because no new combination was introduced |

---

### C-22 Structural Map (cumulative through R10)

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
| Dedicated labeled paragraph | Mid-sub-skill inter-section slot (trace-state / trace-contract boundary) | PASS | R9 V-02 |
| Bare standalone sentence | Mid-sub-skill inter-section slot (trace-state / trace-contract boundary) | PASS | R9 V-03 |
| Dedicated labeled paragraph (inside named section body) | Synthesis section body (final element before closing ---) | PASS | R9 V-04 |
| Dedicated labeled paragraph (minimal: slot-name defs stripped elsewhere) | Own inter-section slot (Synthesis/Consolidated boundary) | PASS | R9 V-05 |
| Dedicated labeled paragraph (minimal form) | Earliest inter-section slot (flow-lifecycle / flow-conversation boundary) | PASS | **R10 V-03/V-05** |
| Dedicated labeled paragraph (inside non-Synthesis named section body) | trace-state section body (after null-result instruction, before closing ---) | PASS | **R10 V-04** |

**Disqualifying locations** (confirmed R7, still operative): gate body; example block (parenthetical annotation or inlined rule).
**Qualifying locations** (confirmed R7 through R10): any non-buried, non-inlined standalone position across the full prompt span -- including earliest and latest inter-section slots, and any named section body.
**Structural requirement**: physical isolation from gate bodies and example blocks. Position within the prompt (early/mid/late/section-body) is irrelevant. Bold label recommended for scannability; not required for C-22 compliance (C-23).

---

### Excellence Signals

From R10:

1. **C-16 load-bearing boundary is now precisely defined**: Template string = required; inline example = required; slot-name definition lines = decorative (R9 V-05); enforcement note = decorative (R9 V-05). Exactly two load-bearing elements. Prompt engineers can strip all decorative content and remain fully C-16 compliant, but must retain the inline example.

2. **C-27 is a precision guard, not a blanket shield**: C-27 protects against one specific false-negative: a scorer wrongly failing C-16 when the template and example are BOTH present but slot-name defs are absent. It does not protect a prompt that has genuinely omitted the example. The criterion is correctly scoped and does not create a back-door immunity.

3. **C-25's "any non-buried position" confirmed across the full prompt span**: The earliest (flow-lifecycle/flow-conversation boundary) and latest (Synthesis/Consolidated boundary) inter-section slots both score 100. No proximity floor to the gate blocks exists anywhere. Production teams can place the Axis-Header Rule at any structurally isolated position without scoring risk or proximity calculation.

4. **C-26 extends to all named section bodies**: Any named sub-skill section with a null-result instruction and a closing `---` divider qualifies as a non-disqualifying body for the Axis-Header Rule. The disqualifier set remains exactly two entries. Prompt engineers can embed the rule as the final element of any named section body if preamble placement is not preferred.

5. **Variation design note -- verify combination novelty before writing prompts**: R10 V-05 was designed to combine V-03's early position with V-01's minimal form, but V-03 already carried minimal form. This produced a structural duplicate. Future rounds should verify that each "combination" introduces a genuinely new configuration by checking whether the source variations already satisfy both variables.

---

### Composite Score Formula (confirmed)

Score = 100 - (0.8 x failed aspirational criteria)
Essential and recommended are threshold gates (all must pass for golden status).
Golden = composite 100 (zero aspirational failures + all essential + all recommended pass).

R10: 20 aspirational criteria.
- V-01: 0 failures = **100**
- V-02: 1 failure (C-16) = **99.2**
- V-03: 0 failures = **100**
- V-04: 0 failures = **100**
- V-05: 0 failures = **100**

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
| R9 | v9 | 100 | 5/5 | V-05 (minimal form confirmed golden at 17/17; slot-name defs decorative) |
| **R10** | **v10** | **100** | **4/5** | **V-01 (production candidate confirmed at 20/20; V-03/V-05 early-position form is equivalent alternative)** |

**R10 decision**: Two probe goals achieved. (1) Production confirmation: V-01 (R9 V-05 form) scores 20/20 under the expanded v10 denominator -- C-25, C-26, C-27 all pass trivially for the confirmed late inter-section slot form. Production candidate confirmed stable. (2) Boundary closure: the C-16/C-27 load-bearing boundary is precisely defined (template + example required; everything else decorative). C-25 confirmed at full prompt span (earliest gap qualifies). C-26 extended to all named section bodies (not Synthesis-exclusive). One structural issue noted: V-05 is a design duplicate of V-03 (early position + minimal form was already the form of V-03); future rounds should verify combination novelty before writing prompts.

**Production candidate**: V-01 (minimal form, Synthesis/Consolidated inter-section slot) remains the recommended production form for maximum proximity to gate blocks and highest scannability. V-03/V-05 (early inter-section slot) are confirmed equivalent alternatives at minimum positional proximity overhead. All three achieve 20/20.
