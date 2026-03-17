## Round 7 Scoring — program-plan (Rubric v7, 27 criteria, 190 pts max)

---

### V-01 — Gate Contrast Rationale Annotation (C-25 axis)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Valid YAML | PASS | program:, stages:, name:, skills: all present |
| C-02 Echo contract | PASS | echo last, skills:[], auto: true, REQUIRED annotations |
| C-03 Valid skill names | PASS | catalog-only entries in all placeholder slots |
| C-04 Evidence-state gates | PASS | PASS gate examples are artifact-state conditions |
| C-05 Namespace dep order | PASS | scout → draft → review → flow → listen arc enforced |
| C-06 Descriptive stage names | PASS | phase-label placeholders, WRONG C-06 annotations |
| C-07 Plan identity | PASS | `# REQUIRED: ...plan, not an executor` at top |
| C-08 Quantified threshold | PASS | `>= 2 signals reviewed` in Discovery PASS gate |
| C-09 Evidence arc | PASS | 5-zone arc visible from zone headers |
| C-10 Failure-mode contrast | PASS | FAIL/PASS gate examples target C-04 at every zone |
| C-11 Structural enforcement | PASS | echo pre-positioned with REQUIRED annotations |
| C-12 Dual-anchor | PASS | template + BAD PLAN block for all 4 essential |
| C-13 Arc as structural spine | PASS | zone headers ARE document structure |
| C-14 Deletion-resistance | PASS | echo: `# DO NOT add skills here. DO NOT move echo before other stages.` |
| C-15 Plan-level YAML error | PASS | BAD PLAN block shows multi-field failure |
| C-16 Criterion-tagged errors | PASS | `# WRONG C-02/C-03/C-04/C-05/C-06/C-07` in BAD PLAN |
| C-17 Per-zone gate contrast | PASS | FAIL/PASS at all 5 non-echo zones in zone-header comments |
| C-18 Correction table | **FAIL** | no correction table present |
| C-19 Cross-tier error coverage | PASS | C-05 and C-06 tagged in BAD PLAN |
| C-20 Per-zone dep reminder at skills | PASS | `# requires:` at skills line for all 4 dep zones |
| C-21 Correction table scaffold | **FAIL** | no table (C-18 fails) |
| C-22 Complete recommended-tier errors | PASS | C-05, C-06, C-07 all tagged in BAD PLAN |
| C-23 Dual-position dep reminders | PASS | zone header + skills line for all 4 dep zones |
| C-24 Template-field gate contrast | **FAIL** | comment-based only, no gate_fail:/gate_pass: YAML keys |
| C-25 Gate contrast rationale (Why:) | PASS | `Why:` for FAIL and PASS at all 5 non-echo zones |
| C-26 Criterion-tagged structural gates | **FAIL** | C-24 prerequisite fails |
| C-27 Uniform dep syntax | **FAIL** | Synthesis zone: "at least one flow/trace or review artifact from prior zones" — natural-language variation from `# requires: <artifact> from Zone: <name> (C-05)` |

**Scoring:**
- Essential: 4/4 × 60 = **60**
- Recommended: 3/3 × 30 = **30**
- Aspirational: 15 PASS × 5 = **75** (FAIL: C-18, C-21, C-24, C-26, C-27)
- **Total: 165 / 190 — Golden (all essential pass, composite >= 80)**

---

### V-02 — Criterion-Tagged Structural Gate Values (C-26 axis)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-04 | PASS ×4 | Valid YAML, echo correct, catalog skills, structural gate_pass: values are artifact-state |
| C-05–C-07 | PASS ×3 | Dep order, descriptive names, plan-identity comment |
| C-08 | PASS | `>= 2 signals reviewed` in Breadth gate_pass |
| C-09 | PASS | Layer 1 Breadth → Layer 2 Design/Validation/Simulation → Layer 3 Synthesis arc |
| C-10 | PASS | gate_fail:/gate_pass: at every zone targets C-04 |
| C-11 | PASS | echo pre-positioned with REQUIRED |
| C-12 | PASS | template + BAD PLAN + correction table covers all 4 essential |
| C-13 | PASS | Layer 1/Layer 2/Layer 3 section headers ARE arc structure |
| C-14 | PASS | echo carries deletion-resistance annotations |
| C-15 | PASS | BAD PLAN block |
| C-16 | PASS | `# WRONG C-02/C-03/C-04/C-05/C-06/C-07` in BAD PLAN |
| C-17 | PASS | gate_fail:/gate_pass: at all 5 non-echo zones (also satisfies C-24) |
| C-18 | PASS | correction table with 13 rows covering C-02/C-03/C-04/C-05/C-06/C-07 |
| C-19 | PASS | C-05 and C-06 rows in table and BAD PLAN |
| C-20 | **PARTIAL** | Design zone skills line has `# check correction table: skill names` only — no dep reminder; Validation/Simulation/Synthesis have it (3/4) |
| C-21 | PASS | `# check correction table` at name:, skills:, gate: positions throughout |
| C-22 | PASS | C-05, C-06, C-07 all in BAD PLAN and table |
| C-23 | **PARTIAL** | Design zone: header has dep note, skills line missing dep reminder; 3/4 dep zones have both positions |
| C-24 | PASS | gate_fail:/gate_pass:/gate: as actual YAML sibling keys at all 5 non-echo zones |
| C-25 | **FAIL** | no Why: rationale on gate_fail:/gate_pass: pairs |
| C-26 | PASS | `# WRONG C-04` inline at every gate_fail: field position |
| C-27 | **FAIL** | dep syntax varies across zones (different phrasings at zone headers vs skills lines) |

**Scoring:**
- Essential: 60, Recommended: 30
- Aspirational: 16 PASS × 5 + 2 PARTIAL × 2.5 = 80 + 5 = **85**
- **Total: 175 / 190 — Golden**

---

### V-03 — Uniform Dependency Reminder Syntax (C-27 axis)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-04 | PASS ×4 | Valid YAML, echo correct, catalog skills, evidence-state gates in zone PASS examples |
| C-05–C-07 | PASS ×3 | Dep order enforced, descriptive names, plan-identity comment |
| C-08 | PASS | `>= N scout signals present` in Discovery gate placeholder |
| C-09 | PASS | 5-zone arc |
| C-10 | PASS | FAIL gate / PASS gate comments target C-04 at every zone |
| C-11 | PASS | echo pre-positioned with REQUIRED |
| C-12 | PASS | template + BAD PLAN + correction table covers all 4 essential |
| C-13 | PASS | zone section headers ARE arc structure |
| C-14 | PASS | echo deletion-resistance annotations |
| C-15 | PASS | BAD PLAN block |
| C-16 | PASS | criterion tags throughout BAD PLAN |
| C-17 | PASS | FAIL/PASS gate examples at all 5 non-echo zone headers |
| C-18 | PASS | correction table with 15 rows |
| C-19 | PASS | C-05, C-06, C-07 all covered |
| C-20 | PASS | `# requires: <artifact> from Zone: <name> (C-05)` at skills line for ALL 4 dep zones |
| C-21 | PASS | `# check correction table` annotation at all covered field types |
| C-22 | PASS | all three recommended criteria in error artifacts |
| C-23 | PASS | zone-header + skills-line dep reminders for ALL 4 dep zones |
| C-24 | **FAIL** | comment-based zone-header contrast only; no gate_fail:/gate_pass: YAML keys |
| C-25 | **FAIL** | no Why: rationale (comment format FAIL/PASS examples, no rationale) |
| C-26 | **FAIL** | C-24 prerequisite fails; no structural gate fields to tag |
| C-27 | PASS | `# requires: <artifact> from Zone: <name> (C-05)` identically at zone header AND skills line for Design, Validation, Simulation, Synthesis |

**Scoring:**
- Essential: 60, Recommended: 30
- Aspirational: 17 PASS × 5 = **85** (FAIL: C-24, C-25, C-26)
- **Total: 175 / 190 — Golden**

---

### V-04 — Gate Rationale + Criterion-Tagged Structural Fields (C-25 + C-26)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-04 | PASS ×4 | Structural gate_pass: values are artifact-state conditions |
| C-05–C-07 | PASS ×3 | Dep order, descriptive names, plan-identity |
| C-08 | PASS | quantified threshold in Discovery gate |
| C-09 | PASS | 5-zone evidence arc |
| C-10 | PASS | gate_fail:/gate_pass: pairs target C-04 |
| C-11 | PASS | echo pre-positioned with REQUIRED |
| C-12 | PASS | template + BAD PLAN + correction table |
| C-13 | PASS | zone headers ARE arc structure |
| C-14 | PASS | echo deletion-resistance |
| C-15 | PASS | BAD PLAN block |
| C-16 | PASS | criterion-tagged errors throughout |
| C-17 | PASS | structural gate fields satisfy per-zone contrast |
| C-18 | PASS | correction table present |
| C-19 | PASS | cross-tier coverage |
| C-20 | **PARTIAL** | Design zone skills line: `# check correction table: skill names` — no dep reminder; Validation/Simulation/Synthesis have dep reminders at skills line (3/4) |
| C-21 | PASS | `# check correction table` at all field types |
| C-22 | PASS | C-05, C-06, C-07 all in BAD PLAN and table |
| C-23 | **PARTIAL** | Design zone missing skills-line dep reminder; 3/4 dep zones have dual position |
| C-24 | PASS | gate_fail:/gate_pass:/gate: as YAML sibling keys at all 5 non-echo zones |
| C-25 | PASS | `# Why FAIL:` / `# Why PASS:` explanation after every gate_fail:/gate_pass: pair across all 5 zones |
| C-26 | PASS | `# WRONG C-04` inline at every gate_fail: field |
| C-27 | **FAIL** | dep syntax varies: "review:* cannot appear here", "review:* requires draft:spec", "listen:*/topic:* require prior flow/trace" — different sentence forms across zones |

**Scoring:**
- Essential: 60, Recommended: 30
- Aspirational: 17 PASS × 5 + 2 PARTIAL × 2.5 = 85 + 5 = **90**
- **Total: 180 / 190 — Golden**

---

### V-05 — Golden Synthesis (all 27 criteria)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-04 | PASS ×4 | Full YAML structure, echo correct, catalog skills, all gate_pass: values are artifact-state |
| C-05–C-07 | PASS ×3 | Dep order, descriptive stage names, plan-identity comment |
| C-08 | PASS | `>= 2 signals reviewed` in Discovery gate_pass |
| C-09 | PASS | Discovery → Design → Validation → Simulation → Synthesis → echo |
| C-10 | PASS | gate_fail: targets C-04 at every zone |
| C-11 | PASS | echo pre-positioned + REQUIRED annotations |
| C-12 | PASS | template + BAD PLAN + correction table covers all 4 essential |
| C-13 | PASS | zone section headers ARE the arc structure |
| C-14 | PASS | echo: `# REQUIRED: DO NOT add skills here. DO NOT move echo before other stages.` |
| C-15 | PASS | BAD PLAN block (multi-field) |
| C-16 | PASS | `# WRONG C-02/C-03/C-04/C-05/C-06/C-07` in BAD PLAN; also `# WRONG C-04` at structural fields |
| C-17 | PASS | gate_fail:/gate_pass: at all 5 non-echo zones |
| C-18 | PASS | correction table, 17+ rows, all 7 criteria covered |
| C-19 | PASS | C-05, C-06 in BAD PLAN and table |
| C-20 | PASS | `# requires: <artifact> from Zone: <name> (C-05)` at skills line for all 4 dep zones |
| C-21 | PASS | `# check correction table: stage names` / `# check correction table: skill names` / `# check correction table: gates` inline at every covered field type |
| C-22 | PASS | C-05, C-06, C-07 in BAD PLAN block AND correction table |
| C-23 | PASS | zone-header AND skills-line dep reminders for all 4 dep-bearing zones (Design, Validation, Simulation, Synthesis) |
| C-24 | PASS | gate_fail:/gate_pass:/gate: as actual YAML keys at all 5 non-echo zones |
| C-25 | PASS | `# Why FAIL:` / `# Why PASS:` rationale comments after every gate_fail:/gate_pass: pair across all 5 zones |
| C-26 | PASS | `# WRONG C-04` inline at every gate_fail: field — criterion tag co-located with wrong shape at structural field position |
| C-27 | PASS | `# requires: <artifact> from Zone: <name> (C-05)` used identically at zone-header comment AND skills: line for all four dep zones; correction table bridge placed on SEPARATE continuation line, not concatenated to requires: prefix |

**Scoring:**
- Essential: 60, Recommended: 30
- Aspirational: 20/20 PASS × 5 = **100**
- **Total: 190 / 190 — Golden**

---

## Rankings

| Rank | Variation | Essential | Recommended | Aspirational | Total | Golden |
|------|-----------|-----------|-------------|--------------|-------|--------|
| 1 | V-05 | 60 | 30 | 100 | **190** | YES |
| 2 | V-04 | 60 | 30 | 90 | **180** | YES |
| 3 | V-02 | 60 | 30 | 85 | **175** | YES |
| 3 | V-03 | 60 | 30 | 85 | **175** | YES |
| 5 | V-01 | 60 | 30 | 75 | **165** | YES |

V-02 and V-03 tie at 175 via different paths: V-02 earns C-24 + C-26 (structural gate fields + criterion tagging, 2 new-axis passes) but takes PARTIAL on C-20 and C-23 and fails C-25 + C-27; V-03 earns C-20 + C-23 + C-27 (uniform dep syntax, full coverage) but fails C-24 + C-25 + C-26.

---

## Excellence Signals from V-05

**1. Separated comment lines resolve the dual-concern conflict at skills position.** R6 V-05 failed C-27 because `# check correction table: skill names; requires: ...` fused two concerns on one prefix line. V-05 splits them: `skills:  # requires: <artifact> from Zone: <name> (C-05)` on the first comment position, then `# check correction table: skill names` on a continuation line. This preserves the machine-recognizable `# requires:` form for C-27 while maintaining the table bridge for C-21 — two single-concern comment lines instead of one mixed prefix.

**2. Structural gate field + criterion tag + Why: form a complete 5-element atomic teaching block.** Each zone delivers: wrong shape (`gate_fail: "research done"`), criterion reference (`# WRONG C-04`), FAIL rationale (`# Why FAIL: "research done" names a past action, not an artifact...`), correct shape (`gate_pass: "...artifacts present; >= 2 signals reviewed"`), PASS rationale (`# Why PASS: names specific artifacts + numeric threshold...`) — all co-located in the YAML skeleton. No cross-document lookup required for any element.

**3. `(C-05)` parenthetical on every dep reminder creates a machine-scannable criterion-tagged pattern.** The form `# requires: <artifact> from Zone: <name> (C-05)` embeds both artifact reference and criterion reference in a single line. A model can scan for `# requires:` as a structured assertion prefix rather than parsing natural-language dependency prose.

---

```json
{"top_score": 190, "all_essential_pass": true, "new_patterns": ["Split dual-concern skills-line comment into two single-concern lines: `# requires: <artifact> from Zone: <name> (C-05)` on first line, `# check correction table: skill names` on continuation — resolves C-27/C-21 tension without mixed prefixes", "5-element atomic gate teaching block at each structural field: wrong shape + criterion tag (# WRONG C-04) + Why FAIL rationale + correct shape + Why PASS rationale — all co-located in YAML skeleton with no cross-document lookup", "Criterion reference embedded in dep reminder via `(C-05)` parenthetical makes reminders machine-scannable as structured assertions rather than natural-language notes"]}
```
