## rhythm-behavior R3 Scorecard

**All 5 variations score 100. All golden.**

R3 probes quality dimensions within passing criteria, not new pass/fail targets. Here's what the round found:

---

### Scores

| Variation | Essential | Recommended | Aspirational | Composite | Golden |
|-----------|-----------|-------------|--------------|-----------|--------|
| V-01 | 4/4 | 3/3 | 8/8 | **100** | YES |
| V-02 | 4/4 | 3/3 | 8/8 | **100** | YES |
| V-03 | 4/4 | 3/3 | 8/8 | **100** | YES |
| V-04 | 4/4 | 3/3 | 8/8 | **100** | YES |
| V-05 | 4/4 | 3/3 | 8/8 | **100** | YES |

---

### Quality Axis Ranking (the real R3 differentiator)

| Variation | C-08 Rationale Quality | C-09 Inheritance Quality | Both Axes | Footprint |
|-----------|----------------------|------------------------|-----------|-----------|
| **V-05** | AUDITABLE (3-slot) | CONSTRAINED (inheritance) | **YES** | **MINIMAL** |
| V-04 | AUDITABLE (3-slot) | CONSTRAINED (inheritance) | YES | Full |
| V-01 | AUDITABLE (3-slot) | UNDERCONSTRAINED | Partial | Full |
| V-02 | PASSABLE (open) | CONSTRAINED (inheritance) | Partial | Full |
| V-03 | PASSABLE (open) | UNDERCONSTRAINED | NO | MINIMAL |

---

### Hypothesis Verdicts

- **V-01 confirmed**: 3-slot format forces three separate named elements; a model cannot write "because multiple downstream callers are affected" when it must fill `[boundary]`, `[caller/component]`, and `[effect]` as distinct slots.
- **V-02 confirmed**: max() floor + no-downgrade + provenance annotation ("Inherited [LEVEL] from [sub-skill-X] ([F-ID])") prevents CROSS-SKILL scope underassignment and makes any violation visible.
- **V-03 confirmed**: Per-section rationale reminders are noise. Column pressure + closing confirmation are the two load-bearing enforcement sites.
- **V-05 confirmed**: Both quality upgrades survive at minimal footprint. Matches V-04 on scoring.

---

### Excellence Signals (JSON)

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["3-slot rationale format ([LEVEL] because [boundary] propagates to [caller/component], [effect]) enforced once in What to look for + once in closing confirmation eliminates vague rationales without per-section repetition", "CROSS-SKILL blast radius inheritance rule (max(contributors) floor) with provenance annotation (Inherited [LEVEL] from [sub-skill-X] ([F-ID])) makes scope assignment auditable and verifiable in the closing confirmation gate", "Closing confirmation as multi-gate quality enforcer: concentrating coverage checks + format compliance + inheritance compliance in one checklist is the minimal-surface-area enforcement pattern"]}
```

**R3 decision: Ship V-05.** Both quality axes upgraded, minimal prompt mass, all 15 criteria pass.
re unambiguous. All PASS.

### C-02 -- Single Unified Report
All five open with "Write everything as one document from start to finish. Do not break it into separate responses." (V-03/V-05: shortened to "Do not promise to continue.") All PASS.

### C-03 -- Blast Radius Ranking Present
All five instruct: sort by blast radius (WIDE first, NARROW last) and label the sort. Column structure in the pre-opened table enforces blast radius on every row. All PASS.

### C-04 -- Spec Gap and Contract Violation Coverage
All five define spec-gap and contract-violation explicitly in the "What to look for" section. Closing confirmation checklist requires both categories; correction loop fires if either is absent. All PASS.

### C-05 -- Per-Finding Sub-Skill Attribution
All five pre-open the findings table with a Sub-Skill column before flow-lifecycle and instruct "append rows as findings are discovered." Sub-Skill label is structurally mandatory at the row level. All PASS.

### C-06 -- Actionable Next Step for Top Finding
All five: "The first finding in the sorted list gets one concrete, specific next step that a developer can execute before writing the first line of implementation code. Name the exact spec section, boundary, or component -- not a generic directive." All PASS.

### C-07 -- Sub-Skill Section Completeness
All five have explicit null-result fallback per section ("say so explicitly" / "PHASE: no findings" / "If none: say so explicitly"). All PASS.

### C-08 -- Blast Radius Justification
**Pass/fail**: all five require Blast Radius Rationale on every row via the table column mandate. All PASS structurally.

**Quality differential (primary R3 finding)**:

| Variation | Rationale Instruction | Quality |
|-----------|----------------------|---------|
| V-01 | 3-slot format: `[LEVEL] because [boundary] propagates to [caller/component], [effect]` with slot-by-slot spec + anti-placeholder warning | AUDITABLE -- 3 mandatory named elements; generic phrases cannot fill the format |
| V-02 | Open: "one sentence naming the specific flows, contracts, or permission boundaries affected" | PASSABLE -- evidence present but slot content unconstrained; generic phrases survive |
| V-03 | Same open instruction as V-02; per-section reminders removed | PASSABLE -- column enforces presence; no slot structure constrains specificity |
| V-04 | 3-slot format (same as V-01) | AUDITABLE -- also includes inheritance provenance requirement for CROSS-SKILL rows |
| V-05 | 3-slot format (same quality as V-04) at minimal footprint | AUDITABLE -- format mandate in "What to look for" + closing confirmation format gate |

V-01, V-04, V-05 produce auditable rationales. V-02, V-03 produce passable rationales that may use generic phrases without detection.

### C-09 -- Cross-Sub-Skill Synthesis
**Pass/fail**: all five have a SYNTHESIS section that names contributing sub-skills, requires CROSS-SKILL labeling, and instructs table row insertion. All PASS.

**Quality differential (primary R3 finding)**:

| Variation | CROSS-SKILL Blast Radius Instruction | Quality |
|-----------|-------------------------------------|---------|
| V-01 | "Assign a blast radius reflecting the combined scope" | UNDERCONSTRAINED -- model can assign NARROW even when contributors were MEDIUM + WIDE |
| V-02 | Inheritance rule: CROSS-SKILL >= max(contributors); rationale: "Inherited [LEVEL] from [sub-skill-X] ([F-ID])..." | CONSTRAINED + AUDITABLE -- no downgrade; derivation traceable to F-ID |
| V-03 | "Assign a blast radius reflecting the combined scope" (same as V-01) | UNDERCONSTRAINED -- same gap as V-01 |
| V-04 | Inheritance rule (same as V-02) + 3-slot format applied to CROSS-SKILL rationale | CONSTRAINED + AUDITABLE -- correct floor + traceable derivation + named slots |
| V-05 | Inheritance rule + provenance annotation in minimal form | CONSTRAINED + AUDITABLE -- matches V-04 quality |

V-02, V-04, V-05 prevent CROSS-SKILL scope underassignment. V-01, V-03 allow it silently.

### C-10 -- Self-Documenting Ranking Label
All five: "Label the sort: 'Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW'" adjacent to the sorted table. All PASS.

### C-11 -- Active Coverage Confirmation
All five: closing checklist confirms spec-gap and contract-violation coverage; correction loop fires if either absent. All PASS.

V-04 and V-05 extend the closing checklist to also confirm format compliance and inheritance compliance:
- "Every Blast Radius Rationale uses the '[LEVEL] because [boundary]...' format with named boundary and named caller/component"
- "Every CROSS-SKILL finding's blast radius is >= the highest contributing sub-skill's blast radius"

This turns the closing confirmation into a 4-gate mechanical check vs the baseline 2-gate check.

### C-12 -- At-Discovery Attribution
All five: pre-open findings table, instruct append-throughout / "add each finding immediately." Sub-Skill, Finding Type, Blast Radius are structural at discovery time. All PASS.

### C-13 -- Dedicated Synthesis Step
All five declare a SYNTHESIS section between trace-permissions and Consolidated Findings. All PASS.

### C-14 -- Rationale Column Enforcement
All five have "Blast Radius Rationale" as a named table column in the pre-opened findings table, with "required for every row." Empty cell is structurally visible as omission. All PASS.

### C-15 -- CROSS-SKILL Findings as First-Class Table Citizens
All five: SYNTHESIS instructs "Add it to the findings table with Sub-Skill = CROSS-SKILL." Coverage summary table includes a CROSS-SKILL row. All PASS.

---

## Quality Axis Ranking

R3 probes two quality dimensions. Pass/fail is identical across all variations.

| Variation | C-08 Rationale Quality | C-09 Inheritance Quality | Both Quality Axes | Footprint |
|-----------|----------------------|------------------------|------------------|-----------|
| V-05 | AUDITABLE (3-slot) | CONSTRAINED (inheritance) | YES | MINIMAL |
| V-04 | AUDITABLE (3-slot) | CONSTRAINED (inheritance) | YES | Full |
| V-01 | AUDITABLE (3-slot) | UNDERCONSTRAINED | Partial | Full |
| V-02 | PASSABLE (open) | CONSTRAINED (inheritance) | Partial | Full |
| V-03 | PASSABLE (open) | UNDERCONSTRAINED | NO | MINIMAL |

**V-05 is the production candidate**: matches V-04 on both quality axes at V-03's footprint.

---

## Hypothesis Verdicts

| Hypothesis | Verdict | Evidence |
|------------|---------|----------|
| V-01: 3-slot format produces auditable rationales | CONFIRMED | Format forces three named elements; "multiple downstream callers" is not a valid [boundary] or [caller/component] slot fill |
| V-02: Inheritance rule prevents CROSS-SKILL scope underassignment | CONFIRMED | max() floor + no-downgrade + provenance annotation closes the gap and makes violations visible |
| V-03: Per-section rationale reminders are noise | CONFIRMED | V-03 passes all 15 criteria without them; column pressure + closing confirmation are the load-bearing sites |
| V-04: Combining format + inheritance upgrades both quality axes | CONFIRMED | Axes are orthogonal; V-04 captures both without interference |
| V-05: Full quality upgrades survive in minimal footprint | CONFIRMED | Scores identical to V-04; closing confirmation enforces both quality gates |

---

## Excellence Signals from V-05

**ES-01 -- 3-slot rationale format as enforceable contract**
`[LEVEL] because [boundary] propagates to [caller/component], [effect]` acts as a mini-contract with three separately named slots. A model filling this format must produce three distinct evidentiary claims. Defined once in "What to look for" and confirmed once in the closing checklist -- no per-section repetition required.

**ES-02 -- Inheritance provenance annotation in CROSS-SKILL rationale**
"Inherited [LEVEL] from [sub-skill-X] ([F-ID])" appended to the CROSS-SKILL rationale makes blast radius derivation auditable: the reader can trace the assigned level back to the exact contributor finding. The closing confirmation gate "Every CROSS-SKILL finding's blast radius is >= the highest contributing sub-skill's blast radius" provides active verification.

**ES-03 -- Closing confirmation as multi-gate quality enforcer**
V-05's closing checklist carries four independent gates: (1) spec-gap coverage, (2) contract-violation coverage, (3) format compliance -- 3-slot format with named boundary and caller/component, (4) inheritance compliance -- CROSS-SKILL blast radius >= max(contributors). Concentrating all structural and quality checks in one closing inspection point is the minimal-surface-area enforcement pattern: fewer total instructions, equal or higher compliance.

---

## Open Questions Answered

| Question | Answer |
|----------|--------|
| Does 3-slot format produce more specific rationales than open instruction? | YES -- structure forces named boundary, caller, effect as separate mandatory elements |
| Does inheritance rule prevent CROSS-SKILL scope underassignment? | YES -- max() floor + no-downgrade + provenance annotation prevents it and makes any violation visible |
| Are per-section rationale reminders load-bearing? | NO -- V-03 passes all 15 criteria without them |
| Does combining format + inheritance produce better quality than either alone? | YES -- axes are orthogonal; V-04/V-05 capture both without interference |
| Does V-05 match V-04 on scoring? | YES -- identical; V-05 is the deployment recommendation |

---

## Round History

| Round | Rubric | Top Score | Golden Count | Production Candidate |
|-------|--------|-----------|-------------|---------------------|
| R1 | v1 | 90 | 1/5 (V-05) | V-05 |
| R2 | v2 | 100 | 2/5 (V-04, V-05) | V-04 |
| R3 | v3 | 100 | 5/5 | **V-05** (quality + minimal) |

**R3 decision**: All five variations golden. V-05 is the production candidate. Ship V-05.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["3-slot rationale format ([LEVEL] because [boundary] propagates to [caller/component], [effect]) enforced once in What to look for + once in closing confirmation eliminates vague rationales without per-section repetition", "CROSS-SKILL blast radius inheritance rule (max(contributors) floor) with provenance annotation (Inherited [LEVEL] from [sub-skill-X] ([F-ID])) makes scope assignment auditable and verifiable in the closing confirmation gate", "Closing confirmation as multi-gate quality enforcer: concentrating coverage checks + format compliance + inheritance compliance in one checklist is the minimal-surface-area enforcement pattern"]}
```
