**rhythm-behavior R4 scored.**

---

### Results

| Variation | Essential | Recommended | Aspirational | Composite | Golden |
|-----------|-----------|-------------|--------------|-----------|--------|
| V-01 | 4/4 | 3/3 | 11/11 | **100** | YES |
| V-02 | 4/4 | 3/3 | 10/11 | **99.1** | YES |
| V-03 | 4/4 | 3/3 | 11/11 | **100** | YES |
| V-04 | 4/4 | 3/3 | 11/11 | **100** | YES |
| V-05 | 4/4 | 3/3 | 11/11 | **100** | YES |

**V-02 fails C-18 exactly as predicted.** The compound gate merging Gates 2+3 yields two gates, not three. C-18's "each triggers a correction loop on failure" requires three independent loops — one per axis. Combining format + inheritance into one block collapses them.

**Key boundary finding**: C-18 tests *axis independence*, not *block structure*. V-03's flat bullet list passes because each bullet has its own conditional ("if X, rewrite / fix"). The format (labeled block vs. flat bullet) is irrelevant — what matters is whether each of the three axes has a correction instruction that fires independently.

**All five hypotheses confirmed.**

**Production recommendation**: V-05 — carries all three R4 upgrades (C-16, C-17, C-18) at minimal prompt mass. 18/18 criteria.
L** | Merging format and inheritance into one compound gate yields two gates, not three; C-18 requires three axes each triggering an independent correction loop |
| V-03 | Three flat bullet items, each with distinct repair verb (add / rewrite / fix) | PASS | Three separate conditional items, each fires independently; function matches three-gate requirement even without block structure |
| V-04 | Three labeled blocks + distinct repair verbs (V-01 + V-03) | PASS | Structure + verb precision together; both axes independently load-bearing |
| V-05 | Three labeled blocks + distinct repair verbs at minimal footprint | PASS | Structural mechanisms survive compression; identical to V-04 on all 18 criteria |

**Boundary conclusion**: C-18 counts gates by axis, not by block count. A compound gate that covers two axes (format + inheritance) under one correction instruction collapses them -- the model has no structural cue to fire two separate repairs. V-03's flat bullets satisfy C-18 because each bullet carries its own conditional: the test is independence, not structure.

---

### Per-Criterion Verdicts

#### Essential Criteria

**C-01 -- Declared Execution Sequence**
All five name the five sub-skills in declared order (flow-lifecycle -> flow-conversation -> trace-state -> trace-contract -> trace-permissions) before any findings appear. V-05 uses compressed list syntax but completeness and order are preserved. All PASS.

**C-02 -- Single Unified Report**
All five open with "Write everything as one document from start to finish. Do not promise to continue." All PASS.

**C-03 -- Blast Radius Ranking Present**
All five: sort by blast radius (WIDE first, NARROW last) with label "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW" structurally attached to the table. All PASS.

**C-04 -- Spec Gap and Contract Violation Coverage**
All five define spec-gap and contract-violation explicitly in "What to look for." Gate 1 / checklist item 1 in every variation requires at least one of each and fires a correction loop if either is absent. All PASS.

#### Recommended Criteria

**C-05 -- Per-Finding Sub-Skill Attribution**
All five pre-open the findings table with a Sub-Skill column and instruct appending rows at discovery time with the producing sub-skill named. Attribution is structural, not retroactive. All PASS.

**C-06 -- Actionable Next Step for Top Finding**
All five: "The first finding in the sorted list gets one concrete, specific next step that a developer can execute before writing the first line of implementation code. Name the exact spec section, boundary, or component -- not a generic directive." All PASS.

**C-07 -- Sub-Skill Section Completeness**
All five require explicit null-result statement per section ("say so explicitly" / "PHASE: no findings" / "If none: say so explicitly"). All PASS.

#### Aspirational Criteria

**C-08 -- Blast Radius Justification**
All five mandate a Blast Radius Rationale column in the pre-opened table with "required for every row." V-01, V-03, V-04, V-05 include "Do not use generic phrases -- every slot must name a specific element from this topic." V-02 omits that line but retains the column mandate + format + example. All PASS.

**C-09 -- Cross-Sub-Skill Synthesis**
All five: dedicated SYNTHESIS section, CROSS-SKILL label required, row insertion into findings table with Sub-Skill = CROSS-SKILL. All PASS.

**C-10 -- Self-Documenting Ranking Label**
All five: "Label the sort: 'Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW'" adjacent to the sorted table. All PASS.

**C-11 -- Active Coverage Confirmation**
All five: closing checklist (Gate 1 or first bullet) checks spec-gap + contract-violation and fires a correction loop if either is absent. All PASS.

**C-12 -- At-Discovery Attribution**
All five: table pre-opened before flow-lifecycle, rows appended as findings are discovered. V-05: "Open this table before flow-lifecycle. Append rows as findings are discovered." All PASS.

**C-13 -- Dedicated Synthesis Step**
All five declare a SYNTHESIS section structurally isolated between trace-permissions and Consolidated Findings. All PASS.

**C-14 -- Rationale Column Enforcement**
All five pre-open the findings table with a "Blast Radius Rationale" column. Empty cell is structurally visible as omission. All PASS.

**C-15 -- CROSS-SKILL Findings as First-Class Table Citizens**
All five: SYNTHESIS instructs "Add it to the findings table with Sub-Skill = CROSS-SKILL." Coverage summary includes a CROSS-SKILL row. All PASS.

**C-16 -- 3-Slot Rationale Format**
All five declare the `[LEVEL] because [boundary] propagates to [caller/component], [effect]` format in "What to look for" with slots named and an example. All five re-enforce the format in the closing confirmation (Gate 2 labeled block or second bullet). C-16 requires both enforcement sites to be present -- satisfied by all five. All PASS.

**C-17 -- CROSS-SKILL Blast Radius Inheritance Rule**
All five declare in SYNTHESIS: "CROSS-SKILL blast radius >= max(contributing sub-skills). No downgrade from the highest contributor is permitted." All five require the provenance annotation "Inherited [LEVEL] from [sub-skill-X] ([F-ID])" in CROSS-SKILL rationale. All five enforce this in the closing confirmation Gate 3 / third bullet with a correction loop. All PASS.

**C-18 -- Closing Confirmation Multi-Gate Enforcement**

| V | Gate 1 loop | Gate 2 loop | Gate 3 loop | Result |
|---|------------|------------|------------|--------|
| V-01 | YES (go back / find) | YES (rewrite) | YES (fix) | PASS |
| V-02 | YES (go back) | Compound (a)+(b): fix all | -- only 2 gates -- | **FAIL** |
| V-03 | YES (add) | YES (rewrite) | YES (fix) | PASS |
| V-04 | YES (add) | YES (rewrite) | YES (fix) | PASS |
| V-05 | YES (add) | YES (rewrite) | YES (fix) | PASS |

V-02 FAIL: the compound Gate 2 covers "format + inheritance" as a single conditional block. C-18 requires three axes and three independent correction loops. Two gates cannot satisfy "each triggers a correction loop on failure" when one gate absorbs two axes.

---

### Hypothesis Verdicts

| Hypothesis | Verdict | Evidence |
|------------|---------|----------|
| V-01: Labeled blocks make each correction loop syntactically unambiguous | CONFIRMED | Each block has header + condition + correction; model cannot read Gate 3 as "confirm only" |
| V-02: Compound gate (Gates 2+3 merged) fails C-18 | CONFIRMED | Two gates -- format axis and inheritance axis both covered by one correction instruction -- fails C-18's three-loop requirement |
| V-03: Distinct repair verbs (add/rewrite/fix) satisfy C-18 without block structure | CONFIRMED | Flat bullets with independent conditionals satisfy the three-axis requirement; structure is not the test |
| V-04: Structure + verb precision are orthogonal improvements | CONFIRMED | Combined form scores 100; no interference between axes |
| V-05: Full C-18 compliance survives at minimal footprint | CONFIRMED | Matches V-04 on all 18 criteria; three labeled gates + three repair verbs preserved under compression |

---

### Production Candidate: V-05

V-05 matches V-04 on all 18 criteria at minimal prompt mass. The compound gate confirmation in V-02 removes it as a simpler alternative. V-05 is the deployment recommendation.

**What V-05 carries that R3 V-05 did not**:
- Gate 1 -- "add" (coverage)
- Gate 2 -- "rewrite" (format), not generic "go back"
- Gate 3 -- "fix" (inheritance), not absent
- Each gate structurally labeled with header + condition + correction

---

### Excellence Signals (JSON)

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-18 counts gates by axis independence, not by block count -- a compound gate covering two axes under one correction instruction collapses them; each of the three quality axes (coverage, format, inheritance) must have its own independent correction loop", "Flat checklist bullets with distinct repair verbs (add/rewrite/fix) satisfy C-18 without requiring labeled block structure -- the test is independent conditionality per axis, not presentation form", "Distinct repair verbs reduce correction ambiguity: 'add' directs insertion of a missing finding, 'rewrite' directs transformation of an existing cell, 'fix' directs recalculation of a blast radius level -- generic 'go back' is ambiguous about the repair target"]}
```

---

### Round History

| Round | Rubric | Top Score | Golden Count | Production Candidate |
|-------|--------|-----------|--------------|---------------------|
| R1 | v1 | 90 | 1/5 (V-05) | V-05 |
| R2 | v2 | 100 | 2/5 (V-04, V-05) | V-04 |
| R3 | v3 | 100 | 5/5 | V-05 (quality + minimal) |
| R4 | v4 | 100 | 4/5 (V-01, V-03, V-04, V-05) | **V-05** (18/18 + minimal) |

**R4 decision**: V-02 boundary probe confirmed. Three independent correction loops required; compound gate insufficient. Ship V-05 (R3 candidate promoted -- now carries all three C-16/C-17/C-18 upgrades).
