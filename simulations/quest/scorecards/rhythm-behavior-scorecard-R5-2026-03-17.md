**rhythm-behavior R5 scored.**

---

### Results

| Variation | Essential | Recommended | Aspirational | Composite | Golden |
|-----------|-----------|-------------|--------------|-----------|--------|
| V-01 | 4/4 | 3/3 | 13/13 | **100** | YES |
| V-02 | 4/4 | 3/3 | 12/13 | **99.2** | YES |
| V-03 | 4/4 | 3/3 | 13/13 | **100** | YES |
| V-04 | 4/4 | 3/3 | 13/13 | **100** | YES |
| V-05 | 4/4 | 3/3 | 13/13 | **100** | YES |

**V-02 fails C-20 exactly as predicted.** Three properly isolated axis-labeled gates pass C-19 — but all three fire "correct," a generic verb that provides no structural cue distinguishing insertion (coverage axis), transformation (format axis), or recalculation (inheritance axis). C-20 FAIL.

---

### Key Findings

**C-19 and C-20 are orthogonal test sites.**
- C-19 tests gate isolation: one axis per gate, no compound merging
- C-20 tests repair verb specificity: the verb must name the axis target
- V-02 confirms they fail independently — proper gate structure is insufficient if the verb gives no axis cue

**R4's C-18 vs R5's C-20 relationship confirmed.** C-18 counts gates by axis independence (did the correction loops separate?). C-20 tests verb quality (does the verb name the repair type?). A prompt can pass all of C-18 with three independent "correct" loops and still fail C-20.

**All five hypotheses confirmed.** Production candidate: **V-05** — 20/20 criteria at minimal prompt mass.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Axis-labeled gate headers ('Coverage Axis', 'Format Axis', 'Inheritance Axis') satisfy C-19 structurally -- two headers cannot name the same axis, so the one-axis-per-gate constraint is visible in the label without additional instruction", "Axis-named repair verbs ('add' / 'rewrite' / 'fix') are independently load-bearing for C-20 -- a generic verb ('correct') fails C-20 even when each gate covers exactly one axis, because 'correct' provides no structural cue distinguishing insertion, transformation, or recalculation", "C-19 and C-20 are orthogonal: C-19 tests gate isolation (one axis per gate, no compound merging), C-20 tests repair verb specificity (verb must name the axis target); V-02 confirms they fail independently -- three isolated axis-labeled gates pass C-19 while generic 'correct' fails C-20"]}
```
oth mechanisms |

All five PASS C-19. The one-axis constraint is satisfiable by structural encoding (axis word in header), by declarative rule ("Do not merge axes"), or by their combination.

**C-20 -- Axis-Named Repair Verb**

| V | Gate 1 verb | Gate 2 verb | Gate 3 verb | C-20 verdict |
|---|-------------|-------------|-------------|--------------|
| V-01 | **add** | **rewrite** | **fix** | PASS |
| V-02 | correct | correct | correct | **FAIL** |
| V-03 | **add** | **rewrite** | **fix** | PASS |
| V-04 | **add** | **rewrite** | **fix** | PASS |
| V-05 | **add** | **rewrite** | **fix** | PASS |

V-02 FAIL: "correct" does not name the axis repair target. The model cannot distinguish from "correct" alone whether it must insert a new finding row, transform an existing rationale cell, or recalculate a blast radius level. Each of the three passing variations uses a verb that encodes the repair type: "add" signals insertion (coverage axis), "rewrite" signals transformation (format axis), "fix" signals recalculation (inheritance axis).

---

### Per-Criterion Verdicts

#### Essential Criteria

**C-01 -- Declared Execution Sequence**
All five name the five sub-skills in declared order (flow-lifecycle -> flow-conversation -> trace-state -> trace-contract -> trace-permissions) before any findings appear. All PASS.

**C-02 -- Single Unified Report**
All five: "Write everything as one document from start to finish. Do not promise to continue." All PASS.

**C-03 -- Blast Radius Ranking Present**
All five: sort by blast radius (WIDE first, NARROW last) labeled "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW" adjacent to the sorted table. All PASS.

**C-04 -- Spec Gap and Contract Violation Coverage**
All five define spec-gap and contract-violation in "What to look for" and Gate 1 checks for both with a correction loop. All PASS.

#### Recommended Criteria

**C-05 -- Per-Finding Sub-Skill Attribution**
All five pre-open the findings table with a Sub-Skill column and instruct row append at discovery time. Attribution is structural, not retroactive. All PASS.

**C-06 -- Actionable Next Step for Top Finding**
All five instruct one concrete next step naming the exact spec section, boundary, or component for the top finding. All PASS.

**C-07 -- Sub-Skill Section Completeness**
All five: "If none: say so explicitly" in each sub-skill section. All PASS.

#### Aspirational Criteria

**C-08 -- Blast Radius Justification**
All five mandate a Blast Radius Rationale column pre-opened with the table, required for every row. All PASS.

**C-09 -- Cross-Sub-Skill Synthesis**
All five: dedicated SYNTHESIS section with CROSS-SKILL label, row insertion into findings table required. All PASS.

**C-10 -- Self-Documenting Ranking Label**
All five: sort label structurally adjacent to the sorted table. All PASS.

**C-11 -- Active Coverage Confirmation**
All five: Gate 1 checks spec-gap and contract-violation presence and fires a correction loop if either is absent. All PASS.

**C-12 -- At-Discovery Attribution**
All five: table pre-opened before flow-lifecycle, rows appended as findings are discovered. All PASS.

**C-13 -- Dedicated Synthesis Step**
All five: SYNTHESIS section structurally isolated between trace-permissions and Consolidated Findings. All PASS.

**C-14 -- Rationale Column Enforcement**
All five: Blast Radius Rationale column pre-opened in the findings table definition. Empty cell is structurally visible as omission. All PASS.

**C-15 -- CROSS-SKILL Findings as First-Class Table Citizens**
All five: SYNTHESIS instructs insertion into findings table with Sub-Skill = CROSS-SKILL; coverage summary includes a CROSS-SKILL row. All PASS.

**C-16 -- 3-Slot Rationale Format**
All five declare `[LEVEL] because [boundary] propagates to [caller/component], [effect]` with all slots named and an inline example in "What to look for." All five re-enforce the format in Gate 2 with a correction loop. All PASS.

**C-17 -- CROSS-SKILL Blast Radius Inheritance Rule**
All five: SYNTHESIS declares >= max rule and requires "Inherited [LEVEL] from [sub-skill-X] ([F-ID])" provenance annotation. Gate 3 enforces with an independent correction loop. All PASS.

**C-18 -- Closing Confirmation Multi-Gate Enforcement**

| V | Gate 1 loop | Gate 2 loop | Gate 3 loop | Result |
|---|------------|------------|------------|--------|
| V-01 | YES (add) | YES (rewrite) | YES (fix) | PASS |
| V-02 | YES (correct) | YES (correct) | YES (correct) | PASS |
| V-03 | YES (add) | YES (rewrite) | YES (fix) | PASS |
| V-04 | YES (add) | YES (rewrite) | YES (fix) | PASS |
| V-05 | YES (add) | YES (rewrite) | YES (fix) | PASS |

All five have three gates, each covering one axis, each with an independent correction loop. Unlike R4's V-02 which had a compound Gate 2+3, R5's V-02 carries three properly isolated gates with axis-labeled headers. C-18 tests axis independence and gate count -- not verb quality. That test belongs to C-20. All PASS.

**C-19 -- One-Axis-Per-Gate Rule**
V-01: axis-labeled headers encode the constraint. V-02: same axis-labeled headers. V-03: explicit preamble states the rule. V-04/V-05: both mechanisms combined. All PASS.

**C-20 -- Axis-Named Repair Verb**
V-01, V-03, V-04, V-05: add/rewrite/fix map to coverage/format/inheritance axes respectively. PASS.
V-02: "correct" is a generic verb that does not name an axis target. **FAIL.**

---

### Hypothesis Verdicts

| Hypothesis | Verdict | Evidence |
|------------|---------|----------|
| V-01: Axis-labeled gate headers satisfy C-19 structurally | CONFIRMED | "Coverage Axis" / "Format Axis" / "Inheritance Axis" -- two headers cannot share a name; constraint is visible in the label without additional instruction |
| V-02: Generic repair verb ("correct") fails C-20 even when each gate covers exactly one axis | CONFIRMED | Three properly isolated axis-labeled gates PASS C-19 but FAIL C-20; repair verb is independently load-bearing |
| V-03: Explicit anti-merge rule satisfies C-19 declaratively without axis-labeled headers | CONFIRMED | "Do not merge axes" closes the merge gap at instruction level; function-named headers do not collide |
| V-04: Axis-labeled headers and anti-merge rule are orthogonal, independently load-bearing | CONFIRMED | Combined form scores 100 on both C-19 and C-20; no interference between structural and declarative mechanisms |
| V-05: Both mechanisms survive compression to minimal footprint | CONFIRMED | "One axis per gate. Do not merge." + axis-labeled headers preserved; matches V-04 on all 20 criteria |

---

### Excellence Signals

From V-05 (top-scoring at minimal prompt mass, 20/20):

1. **Repair verb as axis label**: "add" / "rewrite" / "fix" each encode a distinct repair type for a distinct quality axis. The verb alone tells the model what kind of operation to perform, making each gate independently executable without reading the other two.

2. **Compressed anti-merge rule**: "One axis per gate. Do not merge." in five words carries the same constraint force as V-03's "Each gate covers exactly one quality axis. Do not merge axes." -- the compression removes no load-bearing mechanism.

3. **Structural + declarative reinforcement for C-19**: Axis-labeled headers enforce the constraint by structure (two headers cannot name the same axis); the anti-merge rule enforces it by instruction. Both survive compression and neither is redundant.

4. **C-18 and C-20 are orthogonal test sites**: C-18 measures gate count and independence (three loops, one axis each). C-20 measures verb quality (axis-named, not generic). A prompt can pass C-18 with three independent "correct" loops and fail C-20 -- V-02 confirms this. Rubric design must probe both dimensions independently.

---

### JSON

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Axis-labeled gate headers ('Coverage Axis', 'Format Axis', 'Inheritance Axis') satisfy C-19 structurally -- two headers cannot name the same axis, so the one-axis-per-gate constraint is visible in the label without additional instruction", "Axis-named repair verbs ('add' / 'rewrite' / 'fix') are independently load-bearing for C-20 -- a generic verb ('correct') fails C-20 even when each gate covers exactly one axis, because 'correct' provides no structural cue distinguishing insertion, transformation, or recalculation", "C-19 and C-20 are orthogonal: C-19 tests gate isolation (one axis per gate, no compound merging), C-20 tests repair verb specificity (verb must name the axis target); V-02 confirms they fail independently -- three isolated axis-labeled gates pass C-19 while generic 'correct' fails C-20"]}
```

---

### Round History

| Round | Rubric | Top Score | Golden Count | Production Candidate |
|-------|--------|-----------|--------------|---------------------|
| R1 | v1 | 90 | 1/5 (V-05) | V-05 |
| R2 | v2 | 100 | 2/5 (V-04, V-05) | V-04 |
| R3 | v3 | 100 | 5/5 | V-05 (quality + minimal) |
| R4 | v4 | 100 | 4/5 (V-01, V-03, V-04, V-05) | V-05 (18/18 + minimal) |
| **R5** | **v5** | **100** | **4/5 (V-01, V-03, V-04, V-05)** | **V-05 (20/20 + minimal)** |

**R5 decision**: V-02 boundary probe confirmed. Axis-named repair verbs are independently load-bearing -- generic "correct" fails C-20 even when gate isolation (C-19) passes. V-05 carries all R5 upgrades (C-16/C-17/C-18/C-19/C-20) at minimal prompt mass. Ship V-05.
