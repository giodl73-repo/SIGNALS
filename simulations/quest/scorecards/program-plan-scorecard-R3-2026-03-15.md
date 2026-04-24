Now I have everything needed to score all five variations. Let me apply the v3 rubric systematically.

---

## program-plan R3 Scoring — Rubric v3 (130 pts max)

### Scoring Legend
PASS = full pts | PARTIAL = half pts | FAIL = 0

---

## V-01 — Arc-as-Spine

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **C-01** YAML valid | PASS | Template has `program:`, `stages:`, proper structure; parseable |
| **C-02** Echo contract | PASS | Echo last in template; `skills: []`, `auto: true`, 4x `# REQUIRED` annotations |
| **C-03** Valid skills | PASS | Zone catalogs list only real namespaced skills; template uses `scout:<skill>` with valid options |
| **C-04** Evidence gates | PASS | Each zone has labeled PASS/FAIL gate examples: `"FAIL: 'discovery done' -- execution state"` |
| C-05 Dependency order | PASS | Arc zone sequence (ZONE 1→2→3→4→5→ECHO) structurally enforces scout→draft→review→flow→listen order |
| C-06 Descriptive names | PASS | Template uses `<discovery-phase-label>` etc.; arc zone headers show intent-based naming |
| C-07 Plan identity | PASS | Opening: `/program:plan is a plan, not an executor`; YAML header: `# This program is a plan, not an executor` |
| C-08 Quantified gate | PASS | Zone 3: `">=2 review artifacts archived; all P0 findings resolved"`; Zone 4: `">=2 flow simulations archived"` |
| C-09 Evidence arc | PASS | 5 zone section headers (DISCOVERY→DESIGN→VALIDATION→SIMULATION→SYNTHESIS→ECHO) form navigable arc |
| C-10 Contrast pair | PASS | Every zone gate has labeled `PASS:` / `FAIL:` examples targeting C-04 |
| C-11 Structural enforcement | PASS | Zone headers structurally enforce dependency order (C-05); echo pre-positioned in YAML template skeleton |
| C-12 Dual-anchor | PARTIAL | C-02/C-03/C-04 dual-anchored (zone guidance + template); C-01 single-anchored (template only, no bad-plan block) |
| **C-13** Arc spine | PASS | Five `## ZONE N -- LABEL` headers ARE the document structure; strip prose → arc still navigable |
| **C-14** Deletion-resist | PARTIAL | Echo fully annotated (`# REQUIRED: empty`, `# REQUIRED: must be present and true`); other template slots (`name`, `skills`, `gate`) have zone labels but no per-slot `# REQUIRED` |
| **C-15** Plan-level error | FAIL | No complete multi-stage wrong-plan YAML block present |

**Worksheet:**
```
Essential:    C-01 PASS  C-02 PASS  C-03 PASS  C-04 PASS
              4/4 → 4/4 * 60 = 60 pts

Recommended:  C-05 PASS  C-06 PASS  C-07 PASS
              3/3 → 3/3 * 30 = 30 pts

Aspirational: C-08 PASS  C-09 PASS  C-10 PASS  C-11 PASS
              C-12 PARTIAL  C-13 PASS  C-14 PARTIAL  C-15 FAIL
              sum = 1+1+1+1+0.5+1+0.5+0 = 6.0 → 6/8 * 40 = 30 pts

Composite: 120 / 130
Golden: YES (all essential pass AND 120 >= 80)
```

---

## V-02 — Full Deletion-Resistance

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **C-01** YAML valid | PASS | Template valid; `# REQUIRED: preserve this comment` at header; `program:` top-level key enforced |
| **C-02** Echo contract | PASS | Five `# REQUIRED` annotations on echo: `DO NOT RENAME`, `DO NOT ADD any skills here`, `DO NOT SET to false`, `DO NOT move echo`, `DO NOT add a gate field` |
| **C-03** Valid skills | PASS | Full skill catalog table; `namespace:skill` comments in template list valid options per layer |
| **C-04** Evidence gates | PASS | Per-slot `# REQUIRED: DO NOT write "done", "complete", "all skills run"` + `# EXAMPLE:` + `# BETTER:` at every gate field; rules checklist item 2 |
| C-05 Dependency order | PASS | Explicit `scout -> draft -> review/prove -> flow/trace -> listen/topic -> echo` section; `# DEPENDENCY:` annotation in layer 2 |
| C-06 Descriptive names | PASS | `# REQUIRED: phase-intent label -- DO NOT use namespace name ("scout")` + `# REQUIRED: DO NOT use generic index` on every name field |
| C-07 Plan identity | PASS | Opening sentence + `# REQUIRED: preserve this comment -- program is a plan, not an executor; skills run standalone` in YAML |
| C-08 Quantified gate | PASS | Layer 1: `# BETTER: ">=2 scout signals archived"`; rules checklist item 3: `"At least one gate is quantified: >=N signals, 0 P0 findings"` |
| C-09 Evidence arc | PASS | `# --- Layer 1: Breadth`, `# --- Layer 2: Focus`, etc. are YAML layer-divider comments in template; arc ordering in numbered instructions |
| C-10 Contrast pair | PASS | `# REQUIRED: DO NOT write "done"` (wrong) paired with `# EXAMPLE: "scout-feasibility artifact present"` (correct) at every gate field |
| C-11 Structural enforcement | PASS | Every YAML field carries `# REQUIRED` annotation — model filling template without reading prose rules still encounters requirements at each field |
| C-12 Dual-anchor | PARTIAL | C-02/C-03/C-04 dual-anchored (rules checklist + template annotations); C-01 single-anchored (template only, no bad-plan block) |
| **C-13** Arc spine | PARTIAL | Arc visible in `# --- Layer N` template dividers, but document structure is intro → catalog table → 6 numbered steps → template; numbered steps are the primary document axis, not arc zones |
| **C-14** Deletion-resist | PASS | Every structural slot annotated: `program:` key, `topic:`, `strategy:`, `name:`, `skills:`, `gate:`, echo fields — all carry explicit `# REQUIRED: DO NOT ...` prohibitions |
| **C-15** Plan-level error | FAIL | No complete multi-stage wrong-plan YAML block |

**Worksheet:**
```
Essential:    C-01 PASS  C-02 PASS  C-03 PASS  C-04 PASS
              4/4 → 60 pts

Recommended:  C-05 PASS  C-06 PASS  C-07 PASS
              3/3 → 30 pts

Aspirational: C-08 PASS  C-09 PASS  C-10 PASS  C-11 PASS
              C-12 PARTIAL  C-13 PARTIAL  C-14 PASS  C-15 FAIL
              sum = 1+1+1+1+0.5+0.5+1+0 = 6.0 → 6/8 * 40 = 30 pts

Composite: 120 / 130
Golden: YES (all essential pass AND 120 >= 80)
```

---

## V-03 — Plan-Level YAML Error Block

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **C-01** YAML valid | PASS | Template has correct structure; BAD PLAN block is a full parseable (but semantically wrong) YAML document |
| **C-02** Echo contract | PASS | BAD PLAN shows `skills: [listen:feedback, listen:support]` + `auto: false` with `# WRONG C-02` annotations; template echo has `# REQUIRED: echo must be last` |
| **C-03** Valid skills | PASS | BAD PLAN shows `scout:analysis` and `draft:outline` with `# WRONG C-03: invented skill name`; correction table maps wrong→correct; skill catalog table present |
| **C-04** Evidence gates | PASS | BAD PLAN has `gate: "done"`, `gate: "complete"`, `gate: "all tasks finished"` all marked `# WRONG C-04`; template gate comment: `"<artifact-referencing condition>"` |
| C-05 Dependency order | PASS | BAD PLAN shows `flow:lifecycle` before any `review:*` with `# Ordering violation`; instructions step 2 shows explicit ordering |
| C-06 Descriptive names | PASS | BAD PLAN shows `name: scout` and `name: stage2` as wrong; correction table: `name: market-research`; instructions step 3 |
| C-07 Plan identity | PASS | Opening: `/program:plan is a plan, not an executor`; template header: `# This program is a plan, not an executor -- every skill runs standalone` |
| C-08 Quantified gate | PASS | Instructions step 4: `"At least one gate must include a numeric threshold (>=N, 0 open, count)"`; template layer 3 comment: `"include >=N count"` |
| C-09 Evidence arc | PASS | Template has `# Layer 1: Breadth`, `# Layer 2: Focus`, `# Layer 3: Validation`, `# Layer 4: Simulation`, `# Layer 5: Synthesis` — YAML layer-divider comments showing arc |
| C-10 Contrast pair | PASS | BAD PLAN block shows all 4 failure modes; correction table maps each wrong pattern to correct form — multiple contrast pairs anchored to essential criteria |
| C-11 Structural enforcement | PASS | BAD PLAN shows wrong echo with `# WRONG C-02` — structural demonstration; template pre-positions echo with `# REQUIRED: echo must be last`; instructions step 5 |
| C-12 Dual-anchor | **PASS** | C-01: BAD PLAN (structural violations) + template (correct structure). C-02: BAD PLAN echo + template echo `# REQUIRED`. C-03: BAD PLAN invented skills + skill catalog. C-04: BAD PLAN gates + instructions. All 4 dual-anchored. |
| **C-13** Arc spine | PARTIAL | Arc visible in template layer dividers; document structure is intro → catalog → bad-plan study → numbered instructions → template; not arc-first organization |
| **C-14** Deletion-resist | PARTIAL | Template echo: `# REQUIRED: echo must be last`, `# REQUIRED: empty`, `# REQUIRED: must be present and true`; other template slots (`name`, `skills`, `gate`) use layer comments but no per-slot `# REQUIRED` annotations |
| **C-15** Plan-level error | PASS | Complete 4-stage BAD PLAN YAML block; labeled `# BAD PLAN -- fails C-01, C-02, C-03, C-04 simultaneously`; all four essential failure modes present with wrong annotations; exceeds R2 V-04's single-stage block |

**Worksheet:**
```
Essential:    C-01 PASS  C-02 PASS  C-03 PASS  C-04 PASS
              4/4 → 60 pts

Recommended:  C-05 PASS  C-06 PASS  C-07 PASS
              3/3 → 30 pts

Aspirational: C-08 PASS  C-09 PASS  C-10 PASS  C-11 PASS
              C-12 PASS  C-13 PARTIAL  C-14 PARTIAL  C-15 PASS
              sum = 1+1+1+1+1+0.5+0.5+1 = 7.0 → 7/8 * 40 = 35 pts

Composite: 125 / 130
Golden: YES (all essential pass AND 125 >= 80)
```

---

## V-04 — Arc-as-Spine + Full Deletion-Resistance

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **C-01** YAML valid | PASS | Template valid; zone-separator comments in YAML output; `program:` top-level key enforced |
| **C-02** Echo contract | PASS | `# ECHO -- Reflection (mandatory final zone)` section + template: `# REQUIRED: echo must be LAST -- DO NOT ADD stages after this`, `# REQUIRED: "echo" exactly -- DO NOT RENAME`, `# REQUIRED: empty -- DO NOT ADD skills`, `# REQUIRED: present and true -- DO NOT REMOVE`, `# REQUIRED: DO NOT add a gate field to echo` |
| **C-03** Valid skills | PASS | Each zone has "Available skills for Zone N" list with all real namespaced names; template zone skill comments |
| **C-04** Evidence gates | PASS | Each zone's gate requirement block: `# REQUIRED: gate must name artifact types or count signals -- DO NOT write "done" or "complete"`; template: `# REQUIRED: artifact names or counts, not "done"` |
| C-05 Dependency order | PASS | Zone section ordering (1→2→3→4→5→ECHO) enforces dependency; each zone has `**Dependency**: Requires Zone N artifacts` |
| C-06 Descriptive names | PASS | Template every zone: `# REQUIRED: phase intent, not "scout"` etc. on name field |
| C-07 Plan identity | PASS | Opening + `# REQUIRED: preserve -- this program is a plan, not an executor; skills run standalone` in YAML |
| C-08 Quantified gate | PASS | Zone 1: `# EXAMPLE: ">=2 scout signals archived"`; Zone 3: `"P0 findings resolved or accepted"`; template: `# REQUIRED: at least ONE gate in plan must be quantified` |
| C-09 Evidence arc | PASS | Five `# ZONE N: LABEL` section headers organize document; arc zones are first-class document sections |
| C-10 Contrast pair | PASS | Each zone gate section has `# REQUIRED: DO NOT write "done"` (wrong) + `# EXAMPLE:` (correct) — contrast pairs at every gate position |
| C-11 Structural enforcement | PASS | Zone section headers structurally enforce arc ordering (C-05); echo section header + pre-positioned template slot enforce C-02; per-slot `# REQUIRED` on all fields |
| C-12 Dual-anchor | PARTIAL | C-02/C-03/C-04 dual-anchored (zone requirement blocks + template annotations); C-01 single-anchored (no bad-plan block → template is the only structural anchor) |
| **C-13** Arc spine | PASS | Five `# ZONE N: LABEL` headers ARE the document structure; model navigates arc zones to reach skill lists; strip prose → zone headers remain → arc navigable |
| **C-14** Deletion-resist | PASS | Every template slot: name → `# REQUIRED: phase intent, not "scout"`, skills → `# REQUIRED: from Zone N catalog above`, gate → `# REQUIRED: artifact names or counts, not "done"`, strategy → `# REQUIRED: DO NOT OMIT`, echo → 4x `# REQUIRED` |
| **C-15** Plan-level error | FAIL | No complete multi-stage wrong-plan YAML block |

**Worksheet:**
```
Essential:    C-01 PASS  C-02 PASS  C-03 PASS  C-04 PASS
              4/4 → 60 pts

Recommended:  C-05 PASS  C-06 PASS  C-07 PASS
              3/3 → 30 pts

Aspirational: C-08 PASS  C-09 PASS  C-10 PASS  C-11 PASS
              C-12 PARTIAL  C-13 PASS  C-14 PASS  C-15 FAIL
              sum = 1+1+1+1+0.5+1+1+0 = 6.5 → 6.5/8 * 40 = 32.5 pts

Composite: 122.5 / 130
Golden: YES (all essential pass AND 122.5 >= 80)
```

---

## V-05 — Golden Synthesis

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **C-01** YAML valid | PASS | WRONG PLAN block (parseable multi-stage YAML with violations) + OUTPUT TEMPLATE (correct `program:` structure); two structural anchors |
| **C-02** Echo contract | PASS | WRONG PLAN shows echo with `skills: [listen:feedback]` and `auto: false` annotated `# WRONG C-02`; ECHO zone section: 4x `# REQUIRED`; template: `# REQUIRED: "echo" exactly -- DO NOT RENAME`, `# REQUIRED: empty list -- DO NOT ADD anything here`, `# REQUIRED: present and true -- DO NOT REMOVE or set false` |
| **C-03** Valid skills | PASS | WRONG PLAN shows `scout:competitive-review` and `draft:outline` with `# WRONG C-03`; pattern map correction table; each zone catalog lists valid skills only |
| **C-04** Evidence gates | PASS | WRONG PLAN has `gate: "done"`, `gate: "complete"`, `gate: "all tasks finished"` all `# WRONG C-04`; pattern map shows corrections; per-zone: `# REQUIRED: DO NOT write "done", "complete", "finished", "all run"` + `# EXAMPLE:` + `# QUANTIFIED:` |
| C-05 Dependency order | PASS | WRONG PLAN shows `flow:lifecycle` before `review:*` annotated as ordering violation; zone section dependencies stated; zone structure enforces order |
| C-06 Descriptive names | PASS | WRONG PLAN: `name: scout`, `name: design` as wrong; pattern map: `name: market-research`; template: `# REQUIRED: phase intent -- DO NOT use "scout"` |
| C-07 Plan identity | PASS | Opening 3-sentence plan identity declaration; template: `# REQUIRED: preserve -- this program is a plan, not an executor; skills run standalone`; plan described as "decision-support artifact" |
| C-08 Quantified gate | PASS | Zone 1: `# QUANTIFIED: ">=2 scout signals archived"`; Zone 3: `# QUANTIFIED: ">=2 review artifacts; all P0 findings resolved"`; Zone 4: `# EXAMPLE: ">=2 flow simulations"`; template: `# REQUIRED: at least ONE gate in plan must be quantified` |
| C-09 Evidence arc | PASS | Five `# ZONE N: LABEL` section headers; ECHO section; arc zones are the document's primary organizational structure |
| C-10 Contrast pair | PASS | WRONG PLAN block (4 failure modes, all annotated) + pattern map correction table = multiple anchored contrast pairs for C-01/C-02/C-03/C-04 |
| C-11 Structural enforcement | PASS | Zone headers enforce arc order; pre-positioned echo with 4x `# REQUIRED` in ECHO section; `# REQUIRED` at every template field means scaffold-following produces correct output |
| C-12 Dual-anchor | **PASS** | C-01: WRONG PLAN (structural failure) + OUTPUT TEMPLATE (correct structure). C-02: WRONG PLAN echo + ECHO section + template annotations. C-03: WRONG PLAN invented skills + zone catalogs. C-04: WRONG PLAN gates + zone gate `# REQUIRED`. All 4 essential criteria dual-anchored. |
| **C-13** Arc spine | PASS | ZONE 1 through ECHO are top-level document sections; model reaches skill catalogs by navigating through zone sections; strip prose → arc headers remain |
| **C-14** Deletion-resist | PASS | ECHO section: `# REQUIRED: echo must be the LAST stage`, `# REQUIRED: DO NOT add any stages after echo`, `# REQUIRED: DO NOT add skills to echo`, `# REQUIRED: auto: true must be present`; template: all name/skills/gate/strategy fields carry per-slot `# REQUIRED: DO NOT ...` annotations |
| **C-15** Plan-level error | PASS | Complete WRONG PLAN YAML block: 4 stages, `scout`/`design`/`simulate`/`echo` stages, multiple failure modes (C-03 invented skills, C-04 execution gates, C-05 ordering, C-02 echo with skills + auto:false); labeled `# WRONG PLAN -- C-01 through C-04 all fail here`; substantially richer than R2 V-04 |

**Worksheet:**
```
Essential:    C-01 PASS  C-02 PASS  C-03 PASS  C-04 PASS
              4/4 → 60 pts

Recommended:  C-05 PASS  C-06 PASS  C-07 PASS
              3/3 → 30 pts

Aspirational: C-08 PASS  C-09 PASS  C-10 PASS  C-11 PASS
              C-12 PASS  C-13 PASS  C-14 PASS  C-15 PASS
              sum = 8.0 → 8/8 * 40 = 40 pts

Composite: 130 / 130
Golden: YES — PERFECT SCORE
```

---

## Composite Scorecard

| Variation | Essential (60) | Rec (30) | Aspirational (40) | Total | Golden |
|-----------|---------------|----------|-------------------|-------|--------|
| **V-05** Golden synthesis | 60 | 30 | 40.0 | **130** | YES |
| **V-03** Plan-level error block | 60 | 30 | 35.0 | **125** | YES |
| **V-04** Arc + deletion-resist | 60 | 30 | 32.5 | **122.5** | YES |
| **V-01** Arc-as-spine | 60 | 30 | 30.0 | **120** | YES |
| **V-02** Full deletion-resist | 60 | 30 | 30.0 | **120** | YES |

**All five variations pass all essential criteria. All five are Golden.**

---

## C-12 Pivot: Why V-03 Outranks V-04

The key discriminator between V-03 (125) and V-04 (122.5) is C-12: V-03 earns full PASS because the bad-plan block provides the second anchor for C-01 (the only criterion V-04 could not dual-anchor). V-04's superior C-13/C-14 combination (+2.5 pts combined over V-03) is exactly offset by C-12 PARTIAL vs PASS (−2.5 pts). V-05 is the only variation where C-12 PASS and C-13/C-14 PASS coexist.

---

## Excellence Signals from V-05

**E-01 — Wrong plan as document opener, before instructions**
V-05 places the WRONG PLAN before any zone content or instructions. A reader encounters the error artifact first, before reading any rules. This pre-loads failure shapes into working memory and makes every subsequent instruction legible as a correction. Compare V-03 which embeds the bad block mid-document after rules — the error arrives later and with less contrast impact.

**E-02 — Pattern map correction table co-located with wrong block**
V-05 immediately follows the WRONG PLAN with a structured `| Failure | Wrong | Correct |` table. Each row closes one failure loop: wrong → correct. This co-location eliminates the distance between "what not to do" and "what to do instead" — the correction is never more than one scroll away from the error. V-03 included a correction table but it was shorter and less systematically structured.

**E-03 — Zone-level gate guidance with # QUANTIFIED annotation**
Every arc zone in V-05 carries its own `# QUANTIFIED:` example alongside the `# EXAMPLE:`. This moves quantified-gate guidance from a general rules instruction to a per-zone affordance — the model can see what a numeric gate looks like for the specific zone it's filling. Contrast V-04, which had zone examples but relied on a single `# REQUIRED: at least ONE gate must be quantified` in the template rather than per-zone quantified examples.

```json
{"top_score": 130, "all_essential_pass": true, "new_patterns": ["wrong-plan block as document opener before instructions maximizes contrast impact and pre-loads failure shapes before any rules are stated", "pattern-map correction table co-located with wrong block closes each failure loop immediately without distance between error and correction", "per-zone quantified gate examples (# QUANTIFIED:) move numeric threshold guidance from a global rule to a per-zone affordance at the point of authoring"]}
```
