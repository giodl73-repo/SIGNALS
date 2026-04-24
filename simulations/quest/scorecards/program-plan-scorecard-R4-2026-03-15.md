## R4 Scorecard — `program:plan` — Round 4

---

### V-01 — Criterion-Referenced Error Tagging (C-16 axis)

**Criterion-by-criterion:**

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Valid YAML | PASS | `program:` top-level, `stages:` list, all stages have `name:` and `skills:`. Template complete. |
| C-02 Echo contract | PASS | `# REQUIRED: DO NOT add skills here. DO NOT move echo before other stages.` + `# REQUIRED: empty` + `# REQUIRED: must be present and true` |
| C-03 Valid skill names | PASS | Full 9-namespace catalog provided. Template uses `namespace:<skill>` placeholders. |
| C-04 Evidence-state gates | PASS | Per-phase gate guidance names artifacts. Template placeholder: `"artifacts the Architect needs; numeric threshold"`. BAD block shows `# WRONG C-04`. |
| C-05 Dependency order | PASS | Explicit chain `scout -> draft -> review/prove -> flow/trace -> listen/topic -> echo`. Phase sequence respects it. |
| C-06 Descriptive stage names | PASS | Template hints: `"discovery"`, `"market-scan"`. BAD block tags `# WRONG C-06`. |
| C-07 Plan-not-executor | PASS | Opening line + `# REQUIRED: preserve this comment -- this program is a plan, not an executor; skills run standalone`. |
| C-08 Quantified gate | PASS | `">= 2 scout signals reviewed; no blocking feasibility concerns"` in Phase 1 guidance. |
| C-09 Evidence arc | PASS | Four phases: Discovery → Design → Validation → Synthesis → Echo. Breadth-to-depth-to-synthesis visible. |
| C-10 Failure contrast pair | PASS | BAD PLAN block (wrong shape) + YAML template (correct shape). Contrast targets C-02/C-03/C-04. |
| C-11 Structural enforcement | PASS | Four phase headers in template enforce arc; echo pre-positioned with REQUIRED annotations. |
| C-12 Dual-anchor | PASS | C-01: template + BAD PLAN structure. C-02: REQUIRED annotations + `# WRONG C-02` in BAD block. C-03: catalog + `# WRONG C-03`. C-04: gate guidance prose + `# WRONG C-04`. All four essentials dual-anchored. |
| C-13 Arc as spine | PASS | Template organized by PM/Architect+PM/Engineering/Team phase headers — arc is the scaffold axis. |
| C-14 Deletion-resistance | PASS | Echo carries three `# REQUIRED` annotations including explicit prohibition on skill addition and movement. |
| C-15 Plan-level YAML error | PASS | BAD PLAN block spans two stages with wrong gate, wrong skill, wrong dependency order, wrong echo — multi-field plan-level failure. |
| C-16 Criterion-tagged errors | **PASS** | `# WRONG C-06`, `# WRONG C-03`, `# WRONG C-05`, `# WRONG C-04`, `# WRONG C-02` annotate each wrong field in BAD block. |
| C-17 Per-zone gate contrast | **FAIL** | No FAIL/PASS pair at zone headers. Single central BAD block only. |
| C-18 Correction table | **FAIL** | No structured wrong-to-correct mapping table. |

**Aspirational: 9 PASS, 0 PARTIAL, 2 FAIL → 9/11 × 55 = 45 pts**

```
Essential:    60 + Recommended: 30 + Aspirational: 45 = 135 / 145
Golden: YES (all essential PASS, composite 135 >= 80)
```

---

### V-02 — Per-Zone Gate Contrast (C-17 axis)

**Criterion-by-criterion:**

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Valid YAML | PASS | Full template with correct structure. |
| C-02 Echo contract | PASS | Three `# REQUIRED` annotations at echo. |
| C-03 Valid skill names | PASS | Catalog + `namespace:<skill>` placeholders + zone-level `# NOT "scout"` hints. |
| C-04 Evidence-state gates | PASS | Every zone has a PASS gate example naming artifacts. Template placeholders guide artifact-referencing. |
| C-05 Dependency order | PASS | `scout -> draft -> review/prove -> flow/trace -> listen/topic -> echo` stated. Design zone note: "`review:*` requires `draft:spec`". |
| C-06 Descriptive stage names | PASS | `# e.g. "discovery", "market-scan"; NOT "scout"` at every zone stage name placeholder. |
| C-07 Plan-not-executor | PASS | Opening line + REQUIRED comment in template. |
| C-08 Quantified gate | PASS | Discovery PASS gate: `">= 2 signals reviewed"`. |
| C-09 Evidence arc | PASS | Five zones: Discovery → Design → Validation → Simulation → Synthesis → Echo. |
| C-10 Failure contrast pair | PASS | Each zone has a FAIL gate (wrong shape) and PASS gate (correct shape). Multiple contrast pairs targeting C-04. |
| C-11 Structural enforcement | PASS | Zone section headers enforce arc structure. Echo REQUIRED annotations. |
| C-12 Dual-anchor | **PARTIAL** | C-02/C-03/C-04 each dual-anchored (REQUIRED + zone examples; catalog + hints; FAIL/PASS + template). C-01 has only one anchor (template only — no BAD PLAN block). Covers 3/4 essentials. |
| C-13 Arc as spine | PASS | Zone headers (Discovery / Design / Validation / Simulation / Synthesis / Echo) ARE the document structure. |
| C-14 Deletion-resistance | PASS | Echo: `# REQUIRED: DO NOT add skills here. DO NOT move echo before other stages.` + `# REQUIRED: empty` + `# REQUIRED: must be present and true`. |
| C-15 Plan-level YAML error | **FAIL** | No BAD PLAN block. FAIL gate examples are single-line strings, not a complete wrong YAML plan. |
| C-16 Criterion-tagged errors | **FAIL** | FAIL gate examples have no `# WRONG C-NN` criterion tags. |
| C-17 Per-zone gate contrast | **PASS** | All 5 non-echo zones carry both FAIL and PASS gate examples: Discovery ✓, Design ✓, Validation ✓, Simulation ✓, Synthesis ✓. |
| C-18 Correction table | **FAIL** | No correction table. |

**Aspirational: 7 PASS, 1 PARTIAL (C-12), 3 FAIL → (7 + 0.5)/11 × 55 = 37.5 pts**

```
Essential:    60 + Recommended: 30 + Aspirational: 37.5 = 127.5 / 145
Golden: YES (all essential PASS, composite 127.5 >= 80)
```

---

### V-03 — Correction Table (C-18 axis)

**Criterion-by-criterion:**

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Valid YAML | PASS | Template has full valid structure with three arc-layer comments. |
| C-02 Echo contract | PASS | REQUIRED annotations + correction table entries for `echo` with skills and missing `auto: true`. |
| C-03 Valid skill names | PASS | Catalog + correction table maps invented names to real ones. |
| C-04 Evidence-state gates | PASS | Correction table has 4 C-04 pairs. Inertia BAD vs GOOD YAML contrast. Template gate placeholders with `# check correction table`. |
| C-05 Dependency order | PASS | Dependency chain stated. GOOD YAML shows correct layer ordering. Layer headers in template enforce sequence. |
| C-06 Descriptive stage names | PASS | Correction table maps namespace labels to intent labels. Template hints `# check correction table -- NOT "scout"`. |
| C-07 Plan-not-executor | PASS | Opening line + REQUIRED comment in template. |
| C-08 Quantified gate | PASS | GOOD YAML gate: `">= 2 scout signals reviewed by PM"`. Template breadth-layer gate: `'>= N signals present'`. |
| C-09 Evidence arc | PASS | Three-layer structure: Breadth → Depth → Synthesis → Echo. GOOD YAML shows all layers. |
| C-10 Failure contrast pair | PASS | Inertia BAD YAML + gated GOOD YAML. Explicit contrast pair targeting C-04 (execution-state vs artifact-referencing gate). |
| C-11 Structural enforcement | PASS | Layer divider headers in template scaffold. Echo REQUIRED annotations with correction table cross-references. |
| C-12 Dual-anchor | PASS | C-01: template (anchor 1) + GOOD YAML block (anchor 2). C-02: REQUIRED annotations + correction table C-02 entries. C-03: catalog + correction table C-03 entries. C-04: inertia contrast + correction table C-04 entries. All four essentials dual-anchored. |
| C-13 Arc as spine | PASS | Template organized by `# ---- Layer 1: Breadth ----`, `# ---- Layer 2: Depth ----`, `# ---- Layer 3: Synthesis ----`. Arc = scaffold backbone. |
| C-14 Deletion-resistance | PASS | Echo: `# REQUIRED: DO NOT add skills here. DO NOT move echo before other stages.` + correction table references at REQUIRED slots. |
| C-15 Plan-level YAML error | PASS | Inertia BAD block shows flat plan with dependency violations (review before draft, flow before review) and execution-state gate — structural key violations across multiple fields. |
| C-16 Criterion-tagged errors | **FAIL** | BAD inertia block labeled `# WRONG: everything in one stage...` — generic label, no `# WRONG C-NN` criterion references. |
| C-17 Per-zone gate contrast | **FAIL** | No per-zone FAIL/PASS at zone/layer headers. Contrast is in a central BAD/GOOD section only. |
| C-18 Correction table | **PASS** | 11 pairs covering C-02 (2 pairs), C-03 (3 pairs), C-04 (4 pairs), C-06 (2 pairs). >= 3 pairs, covers multiple essential criteria. |

**Aspirational: 9 PASS, 0 PARTIAL, 2 FAIL → 9/11 × 55 = 45 pts**

```
Essential:    60 + Recommended: 30 + Aspirational: 45 = 135 / 145
Golden: YES (all essential PASS, composite 135 >= 80)
```

---

### V-04 — Criterion Tags + Per-Zone Contrast (C-16 + C-17 combined)

**Criterion-by-criterion:**

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Valid YAML | PASS | Full template with correct structure. BAD + GOOD YAML blocks both present. |
| C-02 Echo contract | PASS | `# REQUIRED: DO NOT add skills here. DO NOT move echo before other stages. (WRONG C-02 if violated)` + `# REQUIRED: empty -- adding skills violates C-02` + `# REQUIRED: must be present and true -- missing violates C-02`. |
| C-03 Valid skill names | PASS | Catalog + BAD block `# WRONG C-03` + template `namespace:<skill>` format. |
| C-04 Evidence-state gates | PASS | Per-zone FAIL gates with `<-- WRONG C-04` tag + PASS gate examples + BAD block `# WRONG C-04`. Triple coverage. |
| C-05 Dependency order | PASS | Chain stated. Design zone note: `# review:* requires draft:spec -- this zone MUST precede all validation zones (C-05)`. |
| C-06 Descriptive stage names | PASS | Template: `# NOT "scout" -- WRONG C-06`, `# NOT "draft" -- WRONG C-06`, etc. at each name placeholder. |
| C-07 Plan-not-executor | PASS | Opening line + REQUIRED comment in template. |
| C-08 Quantified gate | PASS | Discovery PASS gate: `">= 2 signals reviewed"`. Design template gate includes `ONE gate across the full plan must be quantified`. |
| C-09 Evidence arc | PASS | Zones: Discovery → Design → Validation → Simulation → Synthesis → Echo. Clear breadth-to-depth-to-synthesis arc. |
| C-10 Failure contrast pair | PASS | BAD PLAN block + GOOD YAML block. Both complete. Contrast anchored to C-02/C-03/C-04. |
| C-11 Structural enforcement | PASS | Zone headers enforce arc. Echo REQUIRED annotations with C-02 references. |
| C-12 Dual-anchor | PASS | All four essentials dual-anchored: C-01 (template + BAD + GOOD), C-02 (REQUIRED + WRONG C-02 in BAD + echo annotations), C-03 (catalog + WRONG C-03 in BAD), C-04 (zone FAIL/PASS + WRONG C-04 in BAD). |
| C-13 Arc as spine | PASS | Zone section headers (Discovery / Design / Validation / Simulation / Synthesis / Echo) are the primary structural axis. |
| C-14 Deletion-resistance | PASS | Echo carries three criterion-referenced REQUIRED annotations including explicit C-02 violations. |
| C-15 Plan-level YAML error | PASS | BAD PLAN block spans two stages with `# WRONG C-NN` tags on each failure field. Multi-field plan-level error demonstrated. |
| C-16 Criterion-tagged errors | **PASS** | BAD block: `# WRONG C-06`, `# WRONG C-03`, `# WRONG C-05`, `# WRONG C-04`, `# WRONG C-02`. Zone FAIL examples: `<-- WRONG C-04`. Echo annotations: `(WRONG C-02 if violated)`. |
| C-17 Per-zone gate contrast | **PASS** | All 5 non-echo zones: Discovery ✓, Design ✓, Validation ✓, Simulation ✓, Synthesis ✓ — each carries FAIL + PASS gate example. |
| C-18 Correction table | **FAIL** | No correction table. Deliberate gap. |

**Aspirational: 10 PASS, 0 PARTIAL, 1 FAIL → 10/11 × 55 = 50 pts**

```
Essential:    60 + Recommended: 30 + Aspirational: 50 = 140 / 145
Golden: YES (all essential PASS, composite 140 >= 80)
```

---

### V-05 — Golden Synthesis (all 18 criteria)

**Criterion-by-criterion:**

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Valid YAML | PASS | Full template. GOOD YAML block. BAD PLAN block. Three structural anchors. |
| C-02 Echo contract | PASS | REQUIRED annotations + BAD block `# WRONG C-02` + correction table two C-02 entries + echo note `Violation is WRONG C-02 -- see correction table`. Four independent anchors. |
| C-03 Valid skill names | PASS | Catalog + BAD block `# WRONG C-03` + correction table three C-03 entries. Triple-anchored. |
| C-04 Evidence-state gates | PASS | Correction table four C-04 pairs + BAD block `# WRONG C-04` + per-zone FAIL/PASS + gate design rule table. Four independent anchors. |
| C-05 Dependency order | PASS | Chain stated. Design zone note. GOOD plan shows correct ordering. |
| C-06 Descriptive stage names | PASS | Template `# NOT "scout" -- see correction table (C-06)` at each zone. Correction table has two C-06 pairs. |
| C-07 Plan-not-executor | PASS | Opening paragraph + REQUIRED comment + gate design rule table frame the plan as decision-support artifact. |
| C-08 Quantified gate | PASS | GOOD plan gate: `">= 2 scout signals reviewed by PM"`. Gate design rule table shows `"quantified (best)"`. Per-zone PASS examples include thresholds. |
| C-09 Evidence arc | PASS | Optional second discovery stage + Design + Validation + Simulation + Synthesis + Echo. Robust arc with optional depth expansion. |
| C-10 Failure contrast pair | PASS | BAD PLAN + GOOD YAML blocks present. Contrast anchored to all four essential criteria. |
| C-11 Structural enforcement | PASS | Zone headers enforce arc. REQUIRED annotations. Correction table cross-references in template comments. |
| C-12 Dual-anchor | PASS | All four essentials have >= 3 independent anchors each. Maximum dual-anchor saturation achieved. |
| C-13 Arc as spine | PASS | Zone section headers ARE the primary structural axis. Correction table references and zone gate examples hang off zone headers. |
| C-14 Deletion-resistance | PASS | Echo: `# REQUIRED: DO NOT add skills here. DO NOT move echo before other stages. / # Violation is WRONG C-02 -- see correction table.` + two REQUIRED slot annotations. Full deletion-resistance chain. |
| C-15 Plan-level YAML error | PASS | BAD PLAN block shows two-stage plan with five criterion-tagged field failures across both stages. |
| C-16 Criterion-tagged errors | **PASS** | BAD block: five `# WRONG C-NN` tags. Per-zone FAIL examples: `<-- WRONG C-04`. Echo: `WRONG C-02 if violated`. Cross-level criterion tagging throughout. |
| C-17 Per-zone gate contrast | **PASS** | All 5 non-echo zones have FAIL + PASS: Discovery ✓ (with `<-- WRONG C-04` on FAIL), Design ✓, Validation ✓, Simulation ✓, Synthesis ✓. |
| C-18 Correction table | **PASS** | 11 pairs covering C-02 (2), C-03 (3), C-04 (4), C-06 (2). Placed at document top as pre-generation reference. |

**Aspirational: 11 PASS, 0 PARTIAL, 0 FAIL → 11/11 × 55 = 55 pts**

```
Essential:    60 + Recommended: 30 + Aspirational: 55 = 145 / 145
Golden: YES (all essential PASS, composite 145 >= 80)
```

---

## Composite Score Table

| Variation | Essential | Recommended | Aspirational | Total | All Essential | Golden |
|-----------|-----------|-------------|--------------|-------|---------------|--------|
| V-01 (C-16) | 60 | 30 | 45.0 | **135** | YES | YES |
| V-02 (C-17) | 60 | 30 | 37.5 | **127.5** | YES | YES |
| V-03 (C-18) | 60 | 30 | 45.0 | **135** | YES | YES |
| V-04 (C-16+C-17) | 60 | 30 | 50.0 | **140** | YES | YES |
| V-05 (all 18) | 60 | 30 | 55.0 | **145** | YES | YES |

**Rank**: V-05 > V-04 > V-01 = V-03 > V-02

V-02 is the weakest because it lacks C-15 (no plan-level BAD YAML block) and C-12 is only PARTIAL (no second anchor for C-01). The per-zone contrast is powerful for C-04 reliability but without the full plan-level error block, the structural learning layer is thinner.

---

## Excellence Signals from V-05

**Three-layer teaching stack as distinct pedagogical modes.** The correction table, criterion-tagged BAD PLAN block, and per-zone FAIL/PASS examples are NOT redundant — they operate at three different moments in model attention: (1) the correction table is consulted before generation (active avoidance); (2) the criterion-tagged BAD block is encountered during BAD/GOOD contrast reading (causal error mapping); (3) per-zone FAIL/PASS is encountered at the authoring decision point (point-of-action feedback). V-04 achieves (2)+(3) but misses (1); any single-axis variation achieves only one mode.

**Cross-reference chains from template back to correction table.** V-05's template comments include `# NOT "scout" -- see correction table (C-06)` and `# NOT "done" / "complete" -- see correction table (C-04)` — inline pointers that keep every teaching mechanism reachable from the generation scaffold without requiring the model to remember section locations.

**Criterion tagging at every structural level.** C-02 is tagged in four independent locations: correction table row (label `C-02`), BAD PLAN block (`# WRONG C-02`), echo zone header note (`WRONG C-02 -- see correction table`), and echo template slots (`WRONG C-02 if violated`). This multi-level tagging means any one of four navigational paths leads to the C-02 requirement — no single-point-of-failure.

**Gate design rule table as standalone quality-level anchor.** The gate design table (`execution state → NO, artifact-referencing → YES, quantified → YES + C-08`) functions as a third lookup artifact orthogonal to the correction table (wrong→correct) and the FAIL/PASS zone examples (good/bad at authoring time). It maps gate quality levels rather than specific error strings, generalizing C-04 beyond the enumerated table entries.

---

```json
{"top_score": 145, "all_essential_pass": true, "new_patterns": ["three-layer teaching stack operates at distinct model-attention moments: correction table (pre-generation avoidance), criterion-tagged BAD block (causal error mapping), per-zone FAIL/PASS (point-of-authoring feedback) — these three modes are non-redundant and combining all three is strictly better than any subset", "cross-reference chains in template comments pointing back to correction table entries keep all teaching mechanisms reachable from the generation scaffold itself", "multi-level criterion tagging at four independent structural locations per essential requirement eliminates single-point-of-failure in requirement recall"]}
```
