**rhythm-behavior R7 scored.**

---

### Results

| Variation | Essential | Recommended | Aspirational | Composite | Golden |
|-----------|-----------|-------------|--------------|-----------|--------|
| V-01 | 4/4 | 3/3 | 14/15 | **99.2** | YES |
| V-02 | 4/4 | 3/3 | 14/15 | **99.2** | YES |
| V-03 | 4/4 | 3/3 | 15/15 | **100** | YES |
| V-04 | 4/4 | 3/3 | 15/15 | **100** | YES |
| V-05 | 4/4 | 3/3 | 15/15 | **100** | YES |

All five predicted scores confirmed.

---

**C-22 verdict**: Both disqualifying locations confirmed. Rule in gate body (V-01) FAIL. Rule as parenthetical inside example block (V-02) FAIL. Preamble-chain sentence (V-03), dedicated labeled paragraph (V-04), and dedicated paragraph + positional headers (V-05) all PASS.

**Three confirmed patterns:**

1. **C-22 burial disqualifier is gate-body-specific** — same sentence in a different structural position fails. Physical location (gate body vs. preamble) is decisive.

2. **C-22 example disqualifier fires for parenthetical annotation** — grammatically complete sentence appended as commentary to an example block is not a governing rule.

3. **V-04 = V-05 on all 22 criteria; positional prefix decorative for the third consecutive round** (R5, R6, R7 all confirm).

**Production candidate: V-04** — dedicated `**Axis-Header Rule**: Each gate header names its axis.` paragraph at minimal prompt mass. Ship V-04.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-22 burial disqualifier is gate-body-specific -- the rule sentence in any gate block's body fails C-22 regardless of grammatical form; preamble-chain vs. gate-body location is the decisive factor", "C-22 example disqualifier fires for parenthetical annotation -- a grammatically complete sentence appended as commentary to the rationale example block is not an independent governing instruction under C-22", "Dedicated labeled paragraph (**Axis-Header Rule**: ...) is the maximally standalone C-22 form at minimal mass; V-04 = V-05 on all 22 criteria confirms positional prefix 'Gate N --' is decorative for the third consecutive round"]}
```
ders. 15/15 aspirational at minimum prompt mass. Ship V-04.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-22 burial disqualifier is gate-body-specific -- the rule sentence in any gate block's body fails C-22 regardless of grammatical form; preamble-chain vs. gate-body location is the decisive factor", "C-22 example disqualifier fires for parenthetical annotation -- a grammatically complete sentence appended as commentary to the rationale example block is not an independent governing instruction under C-22", "Dedicated labeled paragraph (**Axis-Header Rule**: ...) is the maximally standalone C-22 form at minimal mass; V-04 = V-05 on all 22 criteria confirms positional prefix 'Gate N --' is decorative for the third consecutive round"]}
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
All five define spec-gap and contract-violation in "What to look for." Coverage Axis Gate (or equivalent) requires both and fires a correction loop if either is absent. All PASS.

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
All five: Coverage Axis Gate (or equivalent) checks for spec-gap and contract-violation presence and fires a correction loop if either is absent. All PASS.

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
| V-05 | YES (add before Gate 2) | YES (rewrite before Gate 3) | YES (fix before closing) | PASS |

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
| V-05 | Gate 1 -- Coverage Axis Gate | Gate 2 -- Format Axis Gate | Gate 3 -- Inheritance Axis Gate | YES | PASS |

All PASS. R7 provides no new C-21 probe; all variations carry axis words in headers.

**C-22 -- Explicit Axis-Header Preamble Rule**

| V | Rule location | Standalone? | C-22 verdict |
|---|---------------|-------------|--------------|
| V-01 | Inside Coverage Axis Gate body, between check and correction loop | NO -- buried in gate body | **FAIL** |
| V-02 | "(Gate headers name their axis.)" parenthetical inside rationale example block | NO -- inlined within example | **FAIL** |
| V-03 | "Every closing confirmation gate header must explicitly name its quality axis." appended to "Three gates before closing..." preamble paragraph | YES -- not in gate body, not in example | PASS |
| V-04 | "**Axis-Header Rule**: Each gate header names its axis." isolated dedicated paragraph with blank lines | YES -- maximally standalone, labeled | PASS |
| V-05 | "**Axis-Header Rule**: Each gate header names its axis." isolated dedicated paragraph (identical to V-04) | YES -- maximally standalone, labeled | PASS |

**V-01 FAIL**: The sentence "Each gate header names its axis." appears mid-block in the Coverage Axis Gate, between the gate check ("spec-gap present? contract-violation present?") and the correction instruction ("Missing: **add** one before Format Axis Gate."). C-22 explicitly disqualifies rules "buried inside a gate body." The sentence is contextualized as part of the gate's check/repair sequence, not as a governing preamble rule.

**V-02 FAIL**: "(Gate headers name their axis.)" appears immediately after the inline rationale example text ("All three slots must be specific -- no generic phrases."), at the same indentation level as the example lines. C-22 explicitly disqualifies rules "inlined within an example." Parenthetical placement within the example block makes it a commentary annotation, not a governing structural instruction.

---

### Hypothesis Verdicts

| Hypothesis | Verdict | Evidence |
|------------|---------|----------|
| V-01: Rule buried in Coverage Axis Gate body fails C-22 | CONFIRMED | "not buried in a gate body" is the disqualifying location; preamble-chain vs. gate-body position is decisive regardless of sentence form |
| V-02: Rule as parenthetical in example block fails C-22 | CONFIRMED | "not inlined within an example" disqualifier fires; parenthetical inside example block is commentary, not a governing rule |
| V-03: Extended standalone sentence passes C-22 identically to compressed form | CONFIRMED | C-22 tests standalone presence, not phrasing; modal "must" and scope qualifier "closing confirmation" add no criteria coverage |
| V-04: Dedicated labeled paragraph is maximally standalone C-22 form at minimal mass | CONFIRMED | Blank-line isolation + bold label makes rule independently scannable; 15/15 aspirational |
| V-05: V-04 = V-05 on all 22 criteria; positional prefix decorative for third consecutive round | CONFIRMED | Both score 100; "Gate N --" adds no criteria coverage under any of the 22 criteria |

---

### C-22 Boundary Analysis

The V-01 and V-02 probes jointly map the two disqualifying locations named in the C-22 pass condition:

- **Gate body (V-01)**: The sentence is structurally within the gate's instruction block. A model reading the gate processes it as part of the gate's check/repair sequence, not as a governing preamble rule. Even if the model notices the sentence, it is contextualized as part of Coverage Axis Gate -- not as an axis-independent instruction.

- **Example block (V-02)**: The parenthetical appears at the same indentation as the example text. Structurally it reads as a footnote on the rationale example, not as a rule about gate headers. A model reading the rationale block processes it as commentary -- not as a structural rule governing all subsequent gate headers.

The preamble-chain location (V-03) and the dedicated labeled paragraph (V-04) both avoid both disqualifiers. V-04's dedicated paragraph adds a bold label and blank-line isolation that makes the rule structure self-evident without reading gate content. This is a stronger encoding of C-22 but carries no criteria advantage over V-03 under the current rubric.

C-22 is orthogonal to C-21: C-21 tests whether the axis word appears in each gate header token. C-22 tests whether a standalone declarative rule instructs this. V-01 and V-02 both pass C-21 (their gate headers carry axis words) while failing C-22 (no standalone rule exists outside a gate body or example).

---

### Excellence Signals

From V-04 (production candidate, 15/15 aspirational at minimal mass):

1. **Named-rule paragraph pattern eliminates C-22 location ambiguity**: The `**Axis-Header Rule**: ...` bold label creates a scannable structural landmark. The rule is independently identifiable without reading any gate block -- zero ambiguity about whether it is in a gate body or preamble.

2. **Three-site enforcement pattern: template + gate + preamble rule**: C-16 established two-site enforcement (format template in "What to look for" + gate check). C-22 adds a third site (preamble rule). The pattern: format rule in "What to look for" section, gate check in closing confirmation, structural rule in preamble -- three independent enforcement sites across the prompt structure.

3. **V-04 = V-05 confirms positional prefix decorative for three consecutive rounds**: R5, R6, and R7 all produce identical scores for "Gate N -- Axis Gate" and "Axis Gate" forms. The numbered prefix adds no criteria coverage under any of the 22 current criteria. V-04 is the minimal satisfying form.

---

### Composite Score Formula (confirmed)

Score = 100 - (0.8 x failed aspirational criteria)
Essential and recommended are threshold gates (all must pass for golden status).

R7: 15 aspirational criteria. V-01 and V-02 each fail 1 = 100 - 0.8 = **99.2**.

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
| **R7** | **v7** | **100** | **3/5 (V-03, V-04, V-05)** | **V-04 (22/22 + minimal)** |

**R7 decision**: Both boundary probes confirmed. C-22 disqualifies the rule in a gate body (V-01) and in an example block (V-02). The dedicated `**Axis-Header Rule**` paragraph (V-04) is the maximally standalone C-22 form at minimal prompt mass. V-04 = V-05 confirms positional prefix decorative for the third consecutive round. Ship V-04.
