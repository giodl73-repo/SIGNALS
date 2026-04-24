Now I have enough to evaluate all 5 variations. Let me score each one.

---

## program-plan — R13 Score Report (v13 Rubric, 270 pts)

### Basis

All 5 R13 variations are built on the full R12 C-01–C-40 foundation, which the preamble confirms was demonstrated in the R12 variates. The R13 design constraint adds C-41/C-42/C-43 to every variation. Evaluation below confirms each criterion for all five.

---

## Per-Variation Evaluation

### Shared C-01–C-40 Baseline (all 5 variations)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| **C-01** Valid YAML | PASS | PASS | PASS | PASS | PASS | `program:` top-level, `stages:` list; BAD PLAN intentionally omits for teaching |
| **C-02** Echo contract | PASS | PASS | PASS | PASS | PASS | Pre-positioned at template end, `auto: true`, `skills: []`, 3× `# REQUIRED` annotations |
| **C-03** Valid skill names | PASS | PASS | PASS | PASS | PASS | Catalog provided; invented names only in BAD PLAN, tagged `# WRONG C-03` |
| **C-04** Evidence-state gates | PASS | PASS | PASS | PASS | PASS | `gate_fail:` shows execution-state; `gate_pass:/gate:` shows artifact-state |
| **C-05** Namespace dep order | PASS | PASS | PASS | PASS | PASS | Construction order enforces scout/draft → review/prove → flow/trace → listen |
| **C-06** Descriptive stage names | PASS | PASS | PASS | PASS | PASS | PASS/FAIL examples; correction table has 3 C-06 pairs |
| **C-07** Plan identity | PASS | PASS | PASS | PASS | PASS | `strategy:` pre-populated (C-43 enforces this structurally) |
| **C-08** Quantified gate thresholds | PASS | PASS | PASS | PASS | PASS | `>= N` in compound gate template at Step 5a |
| **C-09** Deliberate evidence arc | PASS | PASS | PASS | PASS | PASS | Breadth/depth/synthesis zones declared before catalog opens |
| **C-10** Failure-mode contrast pair | PASS | PASS | PASS | PASS | PASS | `gate_fail:/gate_pass:` in Step 5a template targets C-04 |
| **C-11** Structural enforcement | PASS | PASS | PASS | PASS | PASS | Echo pre-positioned; `strategy:` pre-populated (C-43) |
| **C-12** Dual-anchor reinforcement | PASS | PASS | PASS | PASS | PASS | Template scaffold + BAD PLAN block = 2 independent anchors per essential criterion |
| **C-13** Arc as structural spine | PASS | PASS | PASS | PASS | PASS | Breadth/depth/synthesis zone headers ARE the structural divisions |
| **C-14** Deletion-resistance annotations | PASS | PASS | PASS | PASS | PASS | Echo carries `# REQUIRED: DO NOT add skills here. DO NOT move echo…`, `# REQUIRED: must be true`, `# REQUIRED: empty` |
| **C-15** Plan-level YAML error artifact | PASS | PASS | PASS | PASS | PASS | BAD PLAN = multi-stage, multi-field, explicitly labeled wrong plan |
| **C-16** Criterion-referenced error tagging | PASS | PASS | PASS | PASS | PASS | `# WRONG C-XX` throughout BAD PLAN and template |
| **C-17** Per-zone gate contrast | PASS | PASS | PASS | PASS | PASS | `gate_fail:/gate_pass:` as template keys at every non-echo zone |
| **C-18** Wrong-to-correct correction table | PASS | PASS | PASS | PASS | PASS | All tables have ≥16 pairs covering C-01–C-07 |
| **C-19** Cross-tier error coverage | PASS | PASS | PASS | PASS | PASS | Tables include C-05, C-06, C-07 pairs |
| **C-20** Per-zone dep constraint reminder | PASS | PASS | PASS | PASS | PASS | `# requires: <artifact> from Zone: <name> (C-05)` at skills: positions |
| **C-21** Correction table scaffold integration | PASS | PASS | PASS | PASS | PASS | `# check correction table: skill names`, `# check correction table: gate values`, `# check correction table: stage names` |
| **C-22** Complete recommended-tier error annotation | PASS | PASS | PASS | PASS | PASS | BAD PLAN tags C-05 (dep order), C-06 (namespace labels), C-07 (no strategy:) |
| **C-23** Dual-position zone dep reminder | PASS | PASS | PASS | PASS | PASS | `# requires:` at both zone-header position and skills: placeholder in Step 5a |
| **C-24** Template-field gate contrast | PASS | PASS | PASS | PASS | PASS | `gate_fail:` and `gate_pass:` as actual YAML keys in template skeleton |
| **C-25** Gate contrast rationale annotation | PASS | PASS | PASS | PASS | PASS | `Why: execution-history check, not artifact-verifiable` on every `gate_fail:` |
| **C-26** Criterion-tagged structural gate values | PASS | PASS | PASS | PASS | PASS | `# WRONG C-04` inline at every `gate_fail:` field in template zones |
| **C-27** Uniform dep reminder syntax | PASS | PASS | PASS | PASS | PASS | `# requires: <artifact> from Zone: <name> (C-05)` used uniformly across all zones and positions |
| **C-28** Production gate field co-location | PASS | PASS | PASS | PASS | PASS | `gate:` present as named sibling alongside `gate_fail:/gate_pass:` |
| **C-29** Correction table recommended-tier pairs | PASS | PASS | PASS | PASS | PASS | Each table has C-05 (3 pairs), C-06 (3 pairs), C-07 (1 pair) |
| **C-30** Dep-reminder + correction-bridge independence | PASS | PASS | PASS | PASS | PASS | Both `# requires:` AND `# check correction table` at every dependent skills: line |
| **C-31** Complete BAD-YAML cross-criterion coverage | PASS | PASS | PASS | PASS | PASS | BAD PLAN carries `# WRONG C-01` through `# WRONG C-07` |
| **C-32** Production gate correction bridge | PASS | PASS | PASS | PASS | PASS | `gate:` field carries `# check correction table: gate values` |
| **C-33** Maximal zone teaching density | PASS | PASS | PASS | PASS | PASS | All 4 mechanisms coexist at every dep-bearing zone: C-28+C-26, C-32, C-27 dual-position, C-30 coexistence |
| **C-34** Compound gate_fail: annotation | PASS | PASS | PASS | PASS | PASS | `# WRONG C-04: Why: execution-history check, not artifact-verifiable` co-located at every `gate_fail:` |
| **C-35** Dual error-format recommended coverage | PASS | PASS | PASS | PASS | PASS | C-31 + C-29 both pass; both formats independently cover C-05/C-06/C-07 |
| **C-36** BAD PLAN header label accuracy | PASS | PASS | PASS | PASS | PASS | Headers say "all 7 criteria (C-01 through C-07)" — no false essential-only restriction |
| **C-37** BAD PLAN stage name field-level annotation | PASS | PASS | PASS | PASS | PASS | `# WRONG C-06` at every wrong-format `name:` field in BAD PLAN |
| **C-38** BAD PLAN header affirmative coverage claim | PASS | PASS | PASS | PASS | PASS | "all 7 criteria (C-01 through C-07) indexed below" |
| **C-39** BAD PLAN skills-field criterion-tag co-location | PASS | PASS | PASS | PASS | PASS | `# WRONG C-03` at every invalid skills entry line |
| **C-40** Compound annotation + correction-table recommended conjunction | PASS | PASS | PASS | PASS | PASS | C-34 + C-29 both pass independently |

---

### New Criteria: C-41 / C-42 / C-43

#### C-41 — BAD PLAN Header Per-Criterion Annotation-Type Index

**Pass condition**: Header maps ≥3 of 4 annotation types (C-26/gate_fail:, C-37/name:, C-39/skills:, C-38/header) to criterion numbers. C-38 prerequisite met (all headers make affirmative claim).

| Variation | Evidence | Result |
|-----------|----------|--------|
| **V-01** | Header: `### C-26: gate_fail: field -- inline # WRONG C-04 at structural gate line` / `### C-37: name: field -- inline # WRONG C-06 at stage-name line` / `### C-39: skills: entry -- inline # WRONG C-03 at skills-list line` / `### C-38: this header -- affirmative full-criterion coverage claim` — all 4 types enumerated as section-level subheaders | **PASS** |
| **V-02** | Header inline: `# Annotation-type index (C-41): C-26 gate_fail: | C-37 name: | C-39 skills: | C-38 header` — compact 4-type enumeration | **PASS** |
| **V-03** | Header: `# Annotation-type index (C-41): # C-26: gate_fail: field carries # WRONG C-04 / # C-37: name: field carries # WRONG C-06 / # C-39: skills: entries carry # WRONG C-03 / # C-38: this header` — all 4 types | **PASS** |
| **V-04** | Header: `# Annotation-type index (C-41) -- see FIELD CO-LOCATION PRINCIPLE section above: # C-26: gate_fail: … / # C-37: name: … / # C-39: skills: … / # C-38: this header` — all 4 types + cross-reference | **PASS** |
| **V-05** | Header: `# Annotation-type index (C-41) -- co-location family complete (see FIELD CO-LOCATION PRINCIPLE): # C-26 / gate_fail: … / # C-37 / name: … / # C-39 / skills: … / # C-38 / this header` + footer verification comment `# Co-location family verified (C-41 index above)` — all 4 types, bidirectional coupling, verification marker | **PASS** |

---

#### C-42 — Co-Location Family as Named Document Section

**Pass condition**: Named section before BAD PLAN with structured table mapping all 3 field types (gate_fail:, name:, skills:) to criterion and annotation tag. C-26/C-37/C-39 prerequisites met (all pass above).

| Variation | Evidence | Result |
|-----------|----------|--------|
| **V-01** | `## FIELD CO-LOCATION PRINCIPLE` section with 3-column table (Field type / Criterion / Required annotation) mapping all 3 field types before BAD PLAN. Brief intro paragraph states co-location rule. | **PASS** |
| **V-02** | `## FIELD CO-LOCATION PRINCIPLE` section with full 4-column table (Field type / Criterion addressed / Required annotation tag / Co-location rule) + prose extending the principle to future field types. | **PASS** |
| **V-03** | `## FIELD CO-LOCATION PRINCIPLE` section with 3-column table embedding rule in the annotation column (`# WRONG C-04: Why: ...` at field line / `# WRONG C-06` at field line / `# WRONG C-03` at entry line). | **PASS** |
| **V-04** | `## FIELD CO-LOCATION PRINCIPLE` section with full 4-column table + subheader: "The header in the BAD PLAN section below claims full coverage of these three annotation types." Bidirectional coupling explicit. | **PASS** |
| **V-05** | `## FIELD CO-LOCATION PRINCIPLE` section with full 4-column table using criterion-number pairs (C-04 / C-26, C-06 / C-37, C-03 / C-39) + prose cross-referencing STRUCTURAL ENFORCEMENT PRINCIPLE in Step 8 as the plan-level analogue. Subheaders: "All three co-location criteria (C-26/C-37/C-39) form a named structural family. See also: STRUCTURAL ENFORCEMENT PRINCIPLE in Step 8 (plan-level analogue). The BAD PLAN header below claims full coverage." | **PASS** |

---

#### C-43 — strategy: Field Structurally Pre-Populated in YAML Template

**Pass condition**: YAML template scaffold contains `strategy:` with non-empty placeholder string. C-07 and C-11 prerequisites met.

| Variation | Evidence | Result |
|-----------|----------|--------|
| **V-01** | `strategy: "why this feature is worth the investment and what signal-gathering decision this plan resolves"` in YAML template at Step 8 | **PASS** |
| **V-02** | Same non-empty placeholder string in YAML template at Step 8 | **PASS** |
| **V-03** | Same non-empty placeholder string + explicit **STRUCTURAL ENFORCEMENT NOTE (C-43/C-07)** in Step 8 naming the echo analogy: *"just as echo is pre-positioned at the template end to enforce C-02 structurally, `strategy:` is pre-populated for exactly the same reason applied to C-07"* | **PASS** |
| **V-04** | Same non-empty placeholder string in YAML template at Step 8 | **PASS** |
| **V-05** | Same non-empty placeholder string + **STRUCTURAL ENFORCEMENT PRINCIPLE** sidebar in Step 8 explicitly pairing echo (C-02/C-11) and strategy: (C-07/C-43) as the two plan-level scaffold-enforced fields: *"Both follow the same principle: pre-populate the required element so compliance is default, not model-attention-dependent. See FIELD CO-LOCATION PRINCIPLE section for the field-level equivalent."* | **PASS** |

---

## Score Summary

| Variation | Essential (60) | Recommended (30) | Aspirational (180) | **Composite (/270)** | **%** | Golden |
|-----------|---------------|-----------------|-------------------|---------------------|-------|--------|
| **V-01** | 60 | 30 | 180 | **270** | 100% | YES |
| **V-02** | 60 | 30 | 180 | **270** | 100% | YES |
| **V-03** | 60 | 30 | 180 | **270** | 100% | YES |
| **V-04** | 60 | 30 | 180 | **270** | 100% | YES |
| **V-05** | 60 | 30 | 180 | **270** | 100% | YES |

Aspirational detail: 36/36 criteria pass for all variations. PARTIAL credit was not triggered on any criterion.

---

## Ranking

All 5 variations score 270/270. Within a tied set, V-05 is the most architecturally integrated: it is the only variation where C-41, C-42, and C-43 are explicitly unified under a single two-level enforcement philosophy declared upfront, with all three mechanisms cross-referencing each other bidirectionally.

Ranking by integration depth (score identical across all):

1. **V-05** — Complete three-criteria integration; introductory two-level table; STRUCTURAL ENFORCEMENT PRINCIPLE names both echo and strategy: as plan-level enforcement; FIELD CO-LOCATION PRINCIPLE section cross-references Step 8; BAD PLAN footer verification comment
2. **V-04** — C-41/C-42 bidirectional coupling; header points to named section; named section confirms header's coverage claim
3. **V-02** — Strongest standalone C-42 (4-column table with co-location rules + future-extensibility prose)
4. **V-03** — Strongest standalone C-43 (STRUCTURAL ENFORCEMENT NOTE with explicit echo analogy)
5. **V-01** — Minimal clean implementation; strongest standalone C-41 header (4-type subheaders as document-level markers)

---

## Excellence Signals

Patterns from V-05 (top by integration depth) that were not explicitly required by any single criterion:

**1. Two-level enforcement philosophy declared as a structural preamble table**

V-05 opens with:

```
| Level | Mechanism | Criterion(s) enforced |
|-------|-----------|----------------------|
| Plan level | Pre-positioned scaffold fields: echo at template end, strategy: at template top | C-02, C-07 |
| Field level | Co-located criterion tags at violating field lines in BAD PLAN | C-04 at gate_fail:, C-06 at name:, C-03 at skills: entries |
```

This converts C-41/C-42/C-43 from three independent additions into one named architectural principle. A model reading the preamble arrives at every subsequent mechanism already primed with the unifying theory.

**2. BAD PLAN footer verification comment**

V-05 ends the BAD PLAN YAML block with:
```yaml
# Co-location family verified (C-41 index above):
# gate_fail: lines carry # WRONG C-04 at field (C-26)
# name: lines carry # WRONG C-06 at field (C-37)
# skills: lines carry # WRONG C-03 at entry (C-39)
```

This is a self-verification terminal marker inside the YAML block — the block audits its own co-location completeness as the last act. A model scanning quickly gets a summary of what the block demonstrates without having to trace all three field types individually.

**3. Criterion-number pairing in FIELD CO-LOCATION PRINCIPLE table**

V-05's table uses `C-04 / C-26`, `C-06 / C-37`, `C-03 / C-39` in the Criterion column — explicitly showing the field criterion and the co-location criterion together. Other variations name only the field criterion (C-04, C-06, C-03). The paired form makes the relationship between "the rule the field violates" and "the criterion requiring the annotation" legible at a single table cell.

**4. Triangulated cross-referencing (STRUCTURAL ENFORCEMENT PRINCIPLE ↔ FIELD CO-LOCATION PRINCIPLE ↔ BAD PLAN header)**

Each named section explicitly points to both others. No section is an island. A model entering at any of the three reference points is directed to the other two, eliminating the attention gap where one mechanism is read and the others are forgotten by generation time.

---

```json
{"top_score": 270, "all_essential_pass": true, "new_patterns": ["two-level enforcement philosophy declared as structural preamble table unifying plan-level pre-positioning and field-level co-location under one named principle", "BAD PLAN YAML footer verification comment auditing co-location family completeness as a self-check within the block", "criterion-number pairing in co-location table showing field criterion and annotation criterion together (e.g. C-04/C-26) to make the relationship explicit at a single cell"]}
```
