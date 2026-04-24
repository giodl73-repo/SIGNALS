**rhythm-behavior R8 scored.**

---

### Results

| Variation | Essential | Recommended | Aspirational | Composite | Golden |
|-----------|-----------|-------------|--------------|-----------|--------|
| V-01 | 4/4 | 3/3 | 15/15 | **100** | YES |
| V-02 | 4/4 | 3/3 | 15/15 | **100** | YES |
| V-03 | 4/4 | 3/3 | 15/15 | **100** | YES |
| V-04 | 4/4 | 3/3 | 15/15 | **100** | YES |
| V-05 | 4/4 | 3/3 | 15/15 | **100** | YES |

All five predicted scores confirmed. **5/5 golden.**

---

**V-01 label-strip verdict: PASS.** The bold label is decorative. `Each gate header names its axis.` as a bare standalone paragraph isolated by blank lines in the pre-gate preamble satisfies C-22's "independent instruction in the preamble" branch. Physical isolation from gate bodies and example blocks is the decisive factor -- not label presence.

**Two new confirmed patterns:**

1. **C-22 bold label is decorative**: Bare standalone sentence = labeled paragraph on all 22 criteria. V-01 = V-04.

2. **C-22 placement envelope is unrestricted within non-buried positions**: Top-of-prompt (V-02), pre-gate preamble (V-01/V-03), inter-section peer slot (V-04), dual placement (V-05) -- all equivalent. No proximity to gate blocks required.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-22 bold label is decorative -- a bare standalone sentence isolated by blank lines in the preamble position qualifies as 'an independent instruction in the preamble' without requiring a named label prefix; physical isolation from gate bodies and example blocks is the decisive factor, not the presence of **Axis-Header Rule**: markup", "C-22 placement envelope is unrestricted within non-buried positions -- top-of-prompt (V-02), pre-gate preamble of Consolidated Findings (V-01/V-03/R7V-04), own inter-section slot between Synthesis and Consolidated Findings (V-04), and dual placement across two sections (V-05) all pass equivalently; no proximity to gate blocks is required"]}
```

**R8 closes the C-22 structural map.** Both disqualifying locations confirmed (R7). All qualifying locations confirmed (R7+R8). C-22 is fully operationally validated. V-04 remains the production candidate.
ix; physical isolation from gate bodies and example blocks is the decisive factor, not the presence of **Axis-Header Rule**: markup", "C-22 placement envelope is unrestricted within non-buried positions -- top-of-prompt (V-02), pre-gate preamble of Consolidated Findings (V-01/V-03/R7V-04), own inter-section slot between Synthesis and Consolidated Findings (V-04), and dual placement across two sections (V-05) all pass equivalently; no proximity to gate blocks is required"]}
```

---

### Per-Criterion Verdicts

#### Essential Criteria

**C-01 -- Declared Execution Sequence**
All five: "Sections in this exact order: flow-lifecycle, flow-conversation, trace-state, trace-contract, trace-permissions" appears before any findings. Order and completeness both present. All PASS.

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
All five declare `[LEVEL] because [boundary] propagates to [caller/component], [effect]` with all three slots named and an inline example in "What to look for." Format re-enforced in Format Axis Gate with a correction loop. All PASS.

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
| V-01 | Bare sentence (no bold label): `Each gate header names its axis.` | Pre-gate preamble of Consolidated Findings, isolated by blank lines | YES -- not gate body, not example; qualifies as "independent instruction in the preamble" | **PASS** |
| V-02 | Labeled paragraph: `**Axis-Header Rule**: Each gate header names its axis.` | Top of prompt, immediately after Output instruction | YES -- canonical prompt preamble; most isolated position tested | **PASS** |
| V-03 | Two-sentence labeled paragraph: `**Axis-Header Rule**: Each gate header names its axis. Do not use positional-only labels such as "Gate 1" or "Check 2."` | Pre-gate preamble of Consolidated Findings, isolated by blank lines (same as R7 V-04) | YES -- standalone dedicated labeled paragraph; sentence count does not affect C-22 | **PASS** |
| V-04 | Labeled paragraph: `**Axis-Header Rule**: Each gate header names its axis.` | Own inter-section slot between Synthesis and Consolidated Findings (flanked by `---` dividers) | YES -- peer section; maximum structural isolation form | **PASS** |
| V-05 | Labeled paragraph: `**Axis-Header Rule**: Each gate header names its axis.` | Dual: (1) "What to look for" pre-table area; (2) Consolidated Findings (R7 V-04 position) | YES -- both appearances are standalone labeled paragraphs; C-22 does not prohibit redundancy | **PASS** |

**V-01 PASS**: The bold label `**Axis-Header Rule**:` is decorative. The bare sentence `Each gate header names its axis.` appears as a standalone paragraph isolated by blank lines in the pre-gate preamble of Consolidated Findings. The C-22 pass condition reads "an independent instruction in the preamble OR a dedicated labeled paragraph." Without the bold label, the paragraph satisfies the first branch: it is an independent instruction (not embedded in any gate body or example) appearing in the preamble (pre-gate area of Consolidated Findings, before any gate block begins). Physical isolation is satisfied; label is not required by the first branch. The decisive factor is location, not label presence.

**V-02 PASS**: Top-of-prompt placement is the canonical prompt preamble -- the most upstream position possible. The rule is a dedicated labeled paragraph appearing before the Sections declaration. Satisfies both branches of C-22's pass condition simultaneously.

**V-03 PASS**: Two sentences within the rule paragraph are additive. C-22 tests standalone presence and location -- not sentence count. The second sentence ("Do not use positional-only labels such as 'Gate 1' or 'Check 2.'") provides declarative reinforcement of C-21 but affects no criterion. All 22 criteria pass identically to R7 V-04.

**V-04 PASS**: Own-section isolation between Synthesis and Consolidated Findings is the maximum structural independence form. The rule is flanked by `---` dividers and is a peer to the named sub-skill sections. C-22 does not require the rule to appear inside Consolidated Findings -- "preamble or dedicated labeled paragraph" is satisfied at the inter-section level.

**V-05 PASS**: Dual placement does not break C-22 or any other criterion. Both appearances are standalone labeled paragraphs in non-buried, non-inlined positions. The early appearance in "What to look for" may improve model compliance in long-context runs where the closing section is distant.

---

### Hypothesis Verdicts

| Hypothesis | Verdict | Evidence |
|------------|---------|----------|
| V-01: Bold label is decorative -- bare standalone paragraph is an "independent instruction" under C-22 | CONFIRMED | Bare sentence in pre-gate preamble position passes C-22; physical isolation is decisive, not label presence |
| V-02: "preamble" includes top-of-prompt canonical preamble; proximity to gates not required | CONFIRMED | Top-of-prompt dedicated labeled paragraph passes C-22 equivalently to pre-gate position |
| V-03: Two-sentence form is neutral for all 22 criteria | CONFIRMED | Sentence expansion within a standalone labeled paragraph is additive; no criterion is affected |
| V-04: Own-section isolation between Synthesis and Consolidated Findings still passes C-22 | CONFIRMED | Inter-section peer slot satisfies C-22; C-22 does not require intra-section placement |
| V-05: Dual placement does not cause any criteria to fail | CONFIRMED | Both appearances standalone and non-buried; C-22 does not prohibit redundancy; 15/15 aspirational |

---

### C-22 Structural Map (cumulative through R8)

| Form | Location | C-22 result | Round confirmed |
|------|----------|-------------|-----------------|
| Inside gate body (any sentence form) | Gate body | FAIL | R7 V-01 |
| Parenthetical in example block | Example block | FAIL | R7 V-02 |
| Sentence appended to preamble paragraph | Preamble-chain (attached) | PASS | R7 V-03 |
| Dedicated labeled paragraph | Pre-gate preamble of Consolidated Findings | PASS | R7 V-04 |
| Dedicated labeled paragraph with positional prefix headers | Pre-gate preamble | PASS | R7 V-05 |
| Bare standalone paragraph (no bold label) | Pre-gate preamble of Consolidated Findings | PASS | **R8 V-01** |
| Dedicated labeled paragraph | Top of prompt (canonical preamble) | PASS | **R8 V-02** |
| Two-sentence dedicated labeled paragraph | Pre-gate preamble of Consolidated Findings | PASS | **R8 V-03** |
| Dedicated labeled paragraph | Own inter-section slot (Synthesis / Consolidated Findings boundary) | PASS | **R8 V-04** |
| Dedicated labeled paragraph (dual: early + late) | "What to look for" + Consolidated Findings | PASS | **R8 V-05** |

**Disqualifying locations** (confirmed R7, still operative): gate body; example block (parenthetical annotation).
**Qualifying locations** (confirmed R7+R8): any non-buried, non-inlined standalone position.
**Structural requirement**: physical isolation from gate bodies and example blocks. Bold label is recommended for scannability; not required for C-22 compliance.

---

### Excellence Signals

From R8 (five-way 100/100 confirmation):

1. **Bold label is decorative under C-22**: `**Axis-Header Rule**:` adds structural clarity and scannability but is not required by the pass condition. A bare standalone sentence in the preamble position is sufficient. Prompt engineers can omit the label at no criteria cost; the label is recommended for human readability, not model compliance.

2. **Placement envelope is wide and non-proximity-gated**: C-22 passes at any non-buried, non-inlined location in the prompt. Top-of-prompt (V-02), pre-gate preamble (V-01/V-03), inter-section slot (V-04), and dual placement (V-05) are all equivalent under the rubric. The rule does not need to be near the gate blocks.

3. **Dual placement is the robustness ceiling at zero criteria cost**: V-05 places the rule in two locations -- early ("What to look for") and late (before the gate blocks). Both pass C-22. This form provides maximum long-context compliance assurance at the cost of one repeated sentence. No criterion penalizes redundancy.

---

### Composite Score Formula (confirmed)

Score = 100 - (0.8 x failed aspirational criteria)
Essential and recommended are threshold gates (all must pass for golden status).

R8: 15 aspirational criteria. All five variations fail 0 = **100**.

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
| **R8** | **v8** | **100** | **5/5** | **V-04 (bold label decorative confirmed; bare-preamble equivalent)** |

**R8 decision**: Label-strip probe (V-01) confirmed: bold label is decorative. Bare standalone sentence in preamble position passes C-22 equivalently to the labeled form. V-04 remains the production candidate (maximum scannability at minimal prompt mass), but any non-buried standalone placement now has an operationally confirmed equivalence proof. R8 closes the C-22 structural map: both disqualifying locations confirmed (R7), all qualifying locations confirmed (R7-R8). C-22 is fully operationally validated.
