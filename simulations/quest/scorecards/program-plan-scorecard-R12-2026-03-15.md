## Scoring Report — program-plan R12 (Rubric v12, 255 pts)

---

### Baseline Assessment

All five variates are built on the 240/240 R12-2026-03-15 foundation, meaning C-01 through C-37 are structurally inherited. The scoring focus is: do the new C-38/C-39/C-40 implementations hold, and are there any cracks in the inherited foundation?

**Note on checklist numbering**: The checklists embedded in the variate prompts use stale C-33–C-37 numbering from a pre-v10 rubric. Scoring follows the **rubric file** as authoritative (C-33 = Maximal Zone Teaching Density, C-34 = Compound gate_fail: Annotation, C-35 = Dual Error-Format Recommended Coverage, etc.).

---

### Per-Criterion Grid — New Criteria Only

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-38** BAD PLAN header affirmative full-criterion claim | PASS — `# BAD PLAN -- all 7 criteria (C-01 through C-07) indexed below` | PASS — `"essential and recommended violations (C-01 through C-07), three-field co-location complete"` | PASS — `"all 7 criteria (C-01 through C-07) -- check your work against each tag below"` | PASS — `"SILENT-HEADER COUNTER-MOVE: all 7 criteria (C-01 through C-07) affirmatively indexed"` | PASS — `"essential and recommended violations (C-01 through C-07), all field types annotated (gate_fail:/name:/skills:)"` |
| **C-39** skills: entries in BAD PLAN carry `# WRONG C-03` at field line | PASS — 3 invented skills annotated at line: `gather-requirements`, `make-a-plan`, `run-analysis` | PASS — 3 entries annotated at field: same pattern | PASS — 3 entries annotated at field | PASS — 3 entries annotated at field with `(Failure 3 counter-move: tag at field)` parenthetical | PASS — 3 entries annotated at field |
| **C-40** C-34 AND C-29 both pass independently | PASS — template `gate_fail:` has `# WRONG C-04: Why:` (C-34 ✓); correction table has C-05/C-06/C-07 pairs (C-29 ✓) | PASS — same structure | PASS — DUAL TEACHING MOMENT subsection explicitly names both channels before correction table | PASS — DUAL-COVERAGE REQUIREMENT named in Step 10; both present | PASS — DUAL TEACHING CHANNELS section names C-34 (template-zone) and C-29 (lookup-zone) as independently required |

---

### Inherited Foundation Spot-Check (C-33–C-37)

| Criterion | All Five Status | Notes |
|-----------|-----------------|-------|
| **C-33** Maximal Zone Teaching Density | PASS | All five Step 5a templates carry all four mechanisms: gate_fail:/gate_pass:/gate: (C-28), `# WRONG C-04` on gate_fail: (C-26), correction bridge on gate: (C-32), dep reminder at zone-header + skills-line in uniform `# requires:` syntax (C-27), both dep reminder AND correction bridge coexist at skills: line (C-30) |
| **C-34** Compound gate_fail: Annotation | PASS | All five: `gate_fail: "..."  # WRONG C-04: Why: execution-history check, not artifact-verifiable` at every non-echo zone template slot |
| **C-35** Dual Error-Format Recommended Coverage | PASS | BAD PLAN carries C-05/C-06/C-07 tags (C-31 ✓) + correction table carries C-05/C-06/C-07 pairs (C-29 ✓) |
| **C-36** BAD PLAN Header Label Coverage Accuracy | PASS | All headers assert full coverage; none restrict to essential-tier |
| **C-37** BAD PLAN Stage Name Field-Level Annotation | PASS | All BAD PLANs: `name: scout_and_draft # WRONG C-06` and `name: prove_and_review # WRONG C-06` at field line |

---

### Full Scorecard

**Essential (C-01–C-04): 4/4 PASS = 60/60 pts** — all five variates

| C-01 | C-02 | C-03 | C-04 |
|------|------|------|------|
| PASS | PASS | PASS | PASS |

**Recommended (C-05–C-07): 3/3 PASS = 30/30 pts** — all five variates

| C-05 | C-06 | C-07 |
|------|------|------|
| PASS | PASS | PASS |

**Aspirational (C-08–C-40): 33/33 PASS = 165/165 pts** — all five variates

All C-08 through C-37 inherited at PASS from R12-2026-03-15 240/240 baseline. New criteria C-38, C-39, C-40: PASS across all five (verified above). No PARTIAL verdicts. No criterion gaps found.

---

### Composite Scores

| Variate | Essential | Recommended | Aspirational | **Total** | Golden (≥235)? |
|---------|-----------|-------------|--------------|-----------|----------------|
| V-01 | 60 | 30 | 165 | **255** | YES |
| V-02 | 60 | 30 | 165 | **255** | YES |
| V-03 | 60 | 30 | 165 | **255** | YES |
| V-04 | 60 | 30 | 165 | **255** | YES |
| V-05 | 60 | 30 | 165 | **255** | YES |

---

### Ranking (All Tied at 255 — Differentiation by Teaching Density)

**#1 — V-05 (Complete Three-Criteria Integration)**
Full reference implementation. Uniquely provides:
- **SKILLS-FIELD ANNOTATION RULE** as a dedicated named section with a three-row table (gate_fail:/name:/skills: each with their criterion, tag, and criterion reference) — the three-field co-location principle is an explicit named rule with a document home before the BAD PLAN, not implied by the block alone.
- **DUAL TEACHING CHANNELS** as a dedicated named section that explains the temporal distinction (template-zone = mid-authoring, lookup-zone = pre-authoring) before the correction table, with C-40 explicitly named as the conjunction requirement.
- **BAD PLAN header meta-commentary**: the header comment in the BAD PLAN block includes inline per-criterion annotation (`# C-38: affirmative header...`, `# C-39: skills entries annotated...`, `# C-37: name entries annotated...`, `# C-26: gate_fail: entries annotated...`) — the block is self-documenting against the rubric.
- **Pre-populated `strategy:` field** in the YAML template — the only variate where C-07 (plan identity) is structurally defaulted rather than author-dependent.

**#2 — V-04 (Failure-Taxonomy Anatomy)**
Inertia-first motivational architecture. Three named failure modes (catalog-first, silent-header gap, untethered-skills-tag gap) make C-38 and C-39 structurally load-bearing — each is a named counter-move against a named failure. The strongest pedagogical motivation for why these criteria exist.

**#3 — V-02 (THREE-FIELD CO-LOCATION RULE Named Rule)**
Declares the co-location principle as a named table before the BAD PLAN, organizing it by field type. The rule makes C-39 feel like pattern completion (third field type in a known rule) rather than an isolated new requirement. BAD PLAN organized by field type with the co-location summary footer.

**#4 — V-03 (DUAL TEACHING MOMENT Discovery)**
Tutorial register that explicitly names and distinguishes the pre-authoring and mid-authoring teaching windows. The DUAL TEACHING MOMENT subsection is the clearest functional motivation for why C-40 requires both channels — a model reading it understands they serve different error windows, not that they're redundant.

**#5 — V-01 (C-38 Affirmative-Header Banner)**
Compact formal register. Correct and fully compliant but the least differentiated from prior R12 variates. BAD PLAN uses plain `gate:` instead of `gate_fail:` (other variates use `gate_fail:` in the BAD PLAN, reinforcing the template field name directly in the error example — marginally stronger teaching but no rubric criterion difference).

---

### Excellence Signals (from V-05)

**1. BAD PLAN block self-documentation via header meta-commentary**
The BAD PLAN header in V-05 includes inline per-criterion commentary identifying which mechanism satisfies which annotation type. This makes the BAD PLAN block a criterion-indexed artifact about itself — a model reading the header sees exactly which rubric criterion each annotation type addresses before scanning the block. Pattern: *header comments in a BAD PLAN block can enumerate which C-XX criterion each annotation type satisfies, converting the block from an example into a criterion-indexed reference.*

**2. Named principle sections for co-location families**
SKILLS-FIELD ANNOTATION RULE and DUAL TEACHING CHANNELS each have dedicated document sections with structured tables. Co-location and teaching-channel requirements become named architectural principles with document homes rather than implied consequences of individual criteria. Pattern: *when two or three criteria share a structural family (e.g., all three field-type co-location criteria C-26/C-37/C-39), naming the family principle in a dedicated section makes future criteria in that family predictable and the prompt extensible.*

**3. Structural defaulting of recommended-tier framing (strategy: pre-population)**
V-05 pre-populates `strategy:` in the YAML template, converting C-07 from a quality bar checked after generation to a structural default baked into the scaffold. Pattern: *recommended criteria that require "at least one framing element" can be enforced structurally — just as echo is pre-positioned for C-02, a strategy: field can be pre-populated for C-07 — converting soft quality requirements into structural enforcement.*

---

```json
{"top_score": 255, "all_essential_pass": true, "new_patterns": ["BAD PLAN block self-documentation: header meta-commentary enumerates which C-XX criterion each annotation type satisfies (C-38 for header, C-39 for skills entries, C-37 for name entries, C-26 for gate_fail entries), making the block a self-indexed criterion reference rather than a bare example", "Named principle sections for co-location families: SKILLS-FIELD ANNOTATION RULE and DUAL TEACHING CHANNELS each get dedicated sections with structured tables — when criteria share a structural family, naming the family principle in a dedicated section makes that family extensible and each member criterion feels like pattern completion rather than an isolated requirement", "Structural defaulting of recommended-tier framing: pre-populating strategy: in the YAML template converts C-07 plan-identity from a post-hoc quality check into a structural default, applying the same scaffold-enforcement logic used for C-02 (echo pre-positioned) to a recommended criterion"]}
```
