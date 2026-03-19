**rhythm-behavior R6 scored.**

---

### Results

| Variation | Essential | Recommended | Aspirational | Composite | Golden |
|-----------|-----------|-------------|--------------|-----------|--------|
| V-01 | 4/4 | 3/3 | 14/14 | **100** | YES |
| V-02 | 4/4 | 3/3 | 13/14 | **99.2** | YES |
| V-03 | 4/4 | 3/3 | 14/14 | **100** | YES |
| V-04 | 4/4 | 3/3 | 14/14 | **100** | YES |
| V-05 | 4/4 | 3/3 | 14/14 | **100** | YES |

All five predicted scores confirmed. V-02 fails C-21 exactly as predicted.

---

**C-21 verdict**: Header location is independently load-bearing. "Gate 1" with axis in the body `(coverage axis)` fails. `**Coverage Axis Gate**` or `**Gate 1 -- Coverage Axis Gate**` both pass. The axis word must be in the header token itself.

**Three confirmed patterns:**

1. **C-21 is location-specific** — axis word in gate body does not substitute for axis word in gate header, same structural-location principle as C-19 (axis per gate) and C-20 (axis verb).

2. **Positional prefix "Gate N --" is decorative** — V-03 scores identically to V-01 across all 21 criteria. The numbered prefix carries zero criteria weight; gate sequencing is recoverable from order or name-reference alone.

3. **Structural encoding sufficient for C-21** — V-03 passes all 21 criteria with no explicit preamble rule. The rule in V-05 adds redundancy but does not unlock new criteria coverage.

**Production candidate: V-05** — axis-gate headers (positional-stripped) + compressed explicit rule "Each gate header names its axis.", 21/21 criteria at minimum prompt mass. Ship V-05.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-21 header location is independently load-bearing -- the axis word must appear in the header token itself; a parenthetical in the gate body ('(coverage axis)') does not satisfy C-21 even when the axis is otherwise unambiguous", "Positional prefix 'Gate N --' is purely decorative across all 21 criteria -- 'Coverage Axis Gate' alone satisfies every criterion that 'Gate 1 -- Coverage Axis Gate' satisfies; gate sequencing is recoverable from order or name-reference, not from the position number", "Structural encoding (axis word in header) is sufficient for C-21 without a declarative preamble rule -- V-03 passes all 21 criteria with no explicit rule; the explicit rule in V-05 adds redundancy against model drift but does not unlock new criteria coverage"]}
```
 four combinations that include the axis word in the header satisfy all 21 criteria. V-05 (no prefix, compressed explicit rule) is production candidate for historical consistency with R5's structural + declarative reinforcement pattern.

---

### Per-Criterion Verdicts

#### Essential Criteria

**C-01 -- Declared Execution Sequence**
All five: "Sections in this exact order: flow-lifecycle, flow-conversation, trace-state, trace-contract, trace-permissions" appears before any findings. Order and completeness both present. All PASS.

**C-02 -- Single Unified Report**
All five: "Write everything as one document from start to finish. Do not promise to continue." All PASS.

**C-03 -- Blast Radius Ranking Present**
All five: sort by blast radius (WIDE first, NARROW last) with label "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW" structurally adjacent to the sorted table. All PASS.

**C-04 -- Spec Gap and Contract Violation Coverage**
All five define spec-gap and contract-violation in "What to look for." Gate 1 (Coverage Axis Gate or equivalent) requires both to be present and fires a correction loop if either is missing. All PASS.

#### Recommended Criteria

**C-05 -- Per-Finding Sub-Skill Attribution**
All five pre-open the findings table with a Sub-Skill column before flow-lifecycle and instruct row append at discovery time. Attribution is structural, not retroactive. All PASS.

**C-06 -- Actionable Next Step for Top Finding**
All five: "Top finding: one concrete next step naming the exact spec section, boundary, or component a developer must address before writing implementation code." All PASS.

**C-07 -- Sub-Skill Section Completeness**
All five: "If a phase has no findings, say so briefly" in flow-lifecycle; "If none: say so explicitly" in each subsequent sub-skill section. All PASS.

#### Aspirational Criteria

**C-08 -- Blast Radius Justification**
All five mandate a Blast Radius Rationale column pre-opened with the table, required for every row. The 3-slot format with slots [boundary], [caller/component], [effect] excludes generic phrases. All PASS.

**C-09 -- Cross-Sub-Skill Synthesis**
All five: dedicated SYNTHESIS section with CROSS-SKILL label, row insertion into findings table with Sub-Skill = CROSS-SKILL required. All PASS.

**C-10 -- Self-Documenting Ranking Label**
All five: label string "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW" structurally adjacent to the sorted table. All PASS.

**C-11 -- Active Coverage Confirmation**
All five: Gate 1 (or Coverage Axis Gate) checks for spec-gap and contract-violation presence and fires a correction loop if either is absent. All PASS.

**C-12 -- At-Discovery Attribution**
All five: findings table pre-opened with all columns before flow-lifecycle begins; rows appended as findings are discovered in each sub-skill section. All PASS.

**C-13 -- Dedicated Synthesis Step**
All five: SYNTHESIS section structurally isolated between trace-permissions and Consolidated Findings. Not embedded inside a sub-skill section. All PASS.

**C-14 -- Rationale Column Enforcement**
All five: Blast Radius Rationale column included in the pre-opened table definition before flow-lifecycle. An empty cell is structurally visible as an omission. All PASS.

**C-15 -- CROSS-SKILL Findings as First-Class Table Citizens**
All five: SYNTHESIS instructs insertion of CROSS-SKILL findings into the main findings table with Sub-Skill = CROSS-SKILL. Coverage summary includes a CROSS-SKILL row. All PASS.

**C-16 -- 3-Slot Rationale Format**
All five declare `[LEVEL] because [boundary] propagates to [caller/component], [effect]` with all three slots named and an inline example in "What to look for." Format re-enforced in Gate 2 (Format Axis Gate or equivalent) with a correction loop. All PASS.

**C-17 -- CROSS-SKILL Blast Radius Inheritance Rule**
All five: SYNTHESIS declares >= max rule ("no downgrade permitted") and requires "Inherited [LEVEL] from [sub-skill-X] ([F-ID])" provenance annotation. Gate 3 (Inheritance Axis Gate or equivalent) enforces with an independent correction loop. All PASS.

**C-18 -- Closing Confirmation Multi-Gate Enforcement**

| V | Gate 1 loop | Gate 2 loop | Gate 3 loop | Result |
|---|------------|------------|------------|--------|
| V-01 | YES (add before Gate 2) | YES (rewrite before Gate 3) | YES (fix before closing) | PASS |
| V-02 | YES (add before Gate 2) | YES (rewrite before Gate 3) | YES (fix before closing) | PASS |
| V-03 | YES (add before Format Axis Gate) | YES (rewrite before Inheritance Axis Gate) | YES (fix before closing) | PASS |
| V-04 | YES (add before Gate 2) | YES (rewrite before Gate 3) | YES (fix before closing) | PASS |
| V-05 | YES (add before Format Axis Gate) | YES (rewrite before Inheritance Axis Gate) | YES (fix before closing) | PASS |

All five have exactly three gates, each covering one axis, each with an independent correction loop. C-18 tests axis independence and gate count -- not header encoding. All PASS.

**C-19 -- One-Axis-Per-Gate Rule**

| V | Gate 1 axis | Gate 2 axis | Gate 3 axis | Any compound? | Result |
|---|-------------|-------------|-------------|---------------|--------|
| V-01 | coverage only | format only | inheritance only | NO | PASS |
| V-02 | coverage only | format only | inheritance only | NO | PASS |
| V-03 | coverage only | format only | inheritance only | NO | PASS |
| V-04 | coverage only | format only | inheritance only | NO | PASS |
| V-05 | coverage only | format only | inheritance only | NO | PASS |

Each gate's correction instruction fires for one axis only. No gate absorbs two axes under a single repair trigger. All PASS.

**C-20 -- Axis-Named Repair Verb**

| V | Gate 1 verb | Gate 2 verb | Gate 3 verb | C-20 verdict |
|---|-------------|-------------|-------------|--------------|
| V-01 | **add** | **rewrite** | **fix** | PASS |
| V-02 | **add** | **rewrite** | **fix** | PASS |
| V-03 | **add** | **rewrite** | **fix** | PASS |
| V-04 | **add** | **rewrite** | **fix** | PASS |
| V-05 | **add** | **rewrite** | **fix** | PASS |

Note: R6 V-02 changed the repair verb from R5 V-02 ("correct" for all three gates). R6 V-02 uses axis-specific verbs (add/rewrite/fix). The boundary probe for R6 targets C-21 header location only, not verb quality. All five PASS C-20.

**C-21 -- Axis-Labeled Gate Header Encoding**

| V | Gate 1 header | Gate 2 header | Gate 3 header | Axis word in header? | C-21 verdict |
|---|---------------|---------------|---------------|----------------------|--------------|
| V-01 | Gate 1 -- Coverage Axis Gate | Gate 2 -- Format Axis Gate | Gate 3 -- Inheritance Axis Gate | YES | PASS |
| V-02 | Gate 1 | Gate 2 | Gate 3 | **NO** | **FAIL** |
| V-03 | Coverage Axis Gate | Format Axis Gate | Inheritance Axis Gate | YES | PASS |
| V-04 | Gate 1 -- Coverage Axis Gate | Gate 2 -- Format Axis Gate | Gate 3 -- Inheritance Axis Gate | YES | PASS |
| V-05 | Coverage Axis Gate | Format Axis Gate | Inheritance Axis Gate | YES | PASS |

V-02 FAIL: "Gate 1" contains no axis word. The axis label "(coverage axis)" appears only in the gate body text. C-21 is header-location-specific -- the axis must appear in the header itself. The parenthetical in the body does not substitute.

---

### Hypothesis Verdicts

| Hypothesis | Verdict | Evidence |
|------------|---------|----------|
| V-01: "Gate N -- Coverage Axis Gate" (axis + role in header) satisfies C-21 | CONFIRMED | Axis word "Coverage" appears in header; two headers cannot share the name; C-19 structurally enforced at header level |
| V-02: Positional-only header ("Gate 1") with axis in body fails C-21 | CONFIRMED | C-21 is location-specific; "Gate 1" contains no axis word; parenthetical "(coverage axis)" in body does not substitute |
| V-03: Stripping positional prefix ("**Coverage Axis Gate**" alone) preserves all 21 criteria | CONFIRMED | V-03 scores 100, identical to V-01; numbered prefix carries zero criteria weight |
| V-04: Structural encoding (header format) and declarative encoding (explicit rule) independently satisfy C-21 | CONFIRMED | V-01/V-03 satisfy C-21 without the explicit rule; V-04 combines both; all score 100 |
| V-05: V-03 headers + explicit rule at minimal footprint matches V-04 on all 21 criteria | CONFIRMED | V-05 scores 100; "Each gate header names its axis." compresses V-04's preamble without criteria loss |

---

### C-21 Boundary Analysis

The V-02 probe answers the central question: C-21's pass condition is about the physical token location of the axis label. The rubric text states "The axis label must appear in the header itself -- not only in the repair verb or the body of the correction instruction." V-02 tests whether a parenthetical qualifies as "header itself" when the structural header tag contains only the position number.

Result: it does not. The header "**Gate 1**" followed by body text "(coverage axis)" fails. The axis word must be part of the header markdown element -- `**Gate 1 -- Coverage Axis Gate**` or `**Coverage Axis Gate**` both qualify; `**Gate 1**` does not, regardless of what appears in the body.

C-21 is orthogonal to C-20: C-21 tests axis encoding at header level, C-20 tests axis encoding at verb level. Both are location-specific constraints at different structural positions of the gate block.

---

### Excellence Signals

From V-05 (top-scoring at minimal prompt mass, 21/21):

1. **Axis-gate names as forward references**: V-03 and V-05 use axis-gate names in forward references ("before Format Axis Gate", "before Inheritance Axis Gate") instead of positional references ("before Gate 2", "before Gate 3"). Gate identity encoded by function -- the name carries enough information to locate the gate without the position number.

2. **Structural encoding is sufficient for C-21**: The axis word in the header alone satisfies the criterion. "Each gate header names its axis." adds a second signal but is not independently necessary. When structural encoding is complete, the declarative rule adds robustness against model drift but does not unlock new criteria.

3. **Minimal explicit rule survives compression**: "Each gate header names its axis." (V-05) vs "Each gate header must name its quality axis." (V-04). Modal "must" and adjective "quality" add no criteria coverage -- the minimal verb form carries the constraint.

4. **R6 boundary probe is cleanly scoped**: R5 V-05 already had the axis word in the header. R6 needed to confirm C-21 is header-location-specific (not gate-block-content-based) and identify the minimal satisfying form. V-02 confirms the location requirement; V-03 identifies the minimal form. Both objectives met in one round.

---

### Composite Score Formula (confirmed)

Score = 100 - (0.8 x failed aspirational criteria)
Essential and recommended are threshold gates (all must pass for golden status).

R6: 14 aspirational criteria. V-02 fails 1 = 100 - 0.8 = **99.2**.

---

### JSON

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-21 header location is independently load-bearing -- the axis word must appear in the header token itself; a parenthetical in the gate body ('(coverage axis)') does not satisfy C-21 even when the axis is otherwise unambiguous", "Positional prefix 'Gate N --' is purely decorative across all 21 criteria -- 'Coverage Axis Gate' alone satisfies every criterion that 'Gate 1 -- Coverage Axis Gate' satisfies; gate sequencing is recoverable from order or name-reference, not from the position number", "Structural encoding (axis word in header) is sufficient for C-21 without a declarative preamble rule -- V-03 passes all 21 criteria with no explicit rule; the explicit rule in V-05 adds redundancy against model drift but does not unlock new criteria coverage"]}
```

---

### Round History

| Round | Rubric | Top Score | Golden Count | Production Candidate |
|-------|--------|-----------|--------------|---------------------|
| R1 | v1 | 90 | 1/5 (V-05) | V-05 |
| R2 | v2 | 100 | 2/5 (V-04, V-05) | V-04 |
| R3 | v3 | 100 | 5/5 | V-05 (quality + minimal) |
| R4 | v4 | 100 | 4/5 (V-01, V-03, V-04, V-05) | V-05 (18/18 + minimal) |
| R5 | v5 | 100 | 4/5 (V-01, V-03, V-04, V-05) | V-05 (20/20 + minimal) |
| **R6** | **v6** | **100** | **4/5 (V-01, V-03, V-04, V-05)** | **V-05 (21/21 + minimal)** |

**R6 decision**: V-02 boundary probe confirmed. C-21 is header-location-specific -- axis word must appear in the header itself; gate body position does not substitute. V-05 carries all R6 upgrades (C-21 via axis-gate headers) at minimal prompt mass. Structural encoding sufficient; explicit rule adds redundancy. Ship V-05.
