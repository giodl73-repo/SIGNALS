## program-plan R6 — Score Report

---

### V-01 — Triple-Artifact Recommended Annotation (C-22 axis)

| # | Criterion | Result | Evidence note |
|---|-----------|--------|---------------|
| C-01 | Valid YAML structure | PASS | Template has program:/stages:/name:/skills: |
| C-02 | Echo stage contract | PASS | skills:[], auto:true, REQUIRED annotations at echo slot |
| C-03 | Valid skill names | PASS | Catalog + correction table C-03 entries + BAD block `# WRONG C-03` |
| C-04 | Evidence-state gates | PASS | Correction table (4 C-04 pairs), BAD block WRONG C-04, per-zone gate prohibitions |
| C-05 | Namespace dep order | PASS | BAD block `# WRONG C-05`, correction table C-05 rows, zone-header dep notes, skills-line `# requires draft:spec` at Validation |
| C-06 | Descriptive stage names | PASS | Correction table maps namespace labels to intent names; BAD block WRONG C-06; template name placeholders carry `(WRONG C-06)` |
| C-07 | Plan identity present | PASS | REQUIRED comment in scaffold; correction table C-07 row; BAD block WRONG C-07; opening paragraph |
| C-08 | Quantified gate | PASS | `>= N scout signals present` in gate placeholder |
| C-09 | Deliberate evidence arc | PASS | PM/Architect+PM/Engineering/Team phase labels; zones ordered breadth→depth→synthesis |
| C-10 | Failure-mode contrast pair | PASS | BAD PLAN block + correction table |
| C-11 | Structural enforcement | PASS | Echo pre-positioned with REQUIRED annotation; zone structure embeds dep order |
| C-12 | Dual-anchor reinforcement | PASS | All 4 essentials have ≥2 independent anchors (BAD block + correction table + scaffold) |
| C-13 | Arc as structural spine | PASS | Zone headers `---- PM Phase: Discovery ----` etc. are the top-level structural divisions |
| C-14 | Deletion-resistance annotations | PASS | Echo carries `# REQUIRED: DO NOT add skills here`, `# REQUIRED: empty`, `# REQUIRED: must be present and true` |
| C-15 | Plan-level YAML error artifact | PASS | Complete multi-stage BAD PLAN YAML block |
| C-16 | Criterion-referenced error tagging | PASS | BAD block tags C-07, C-06, C-03, C-05, C-04, C-02 |
| C-17 | Per-zone gate contrast | **FAIL** | Zone headers show prohibition (`NOT "done"`) but no FAIL/PASS pair — no PASS gate example inline per zone |
| C-18 | Wrong-to-correct correction table | PASS | 15 entries covering C-04, C-03, C-06, C-05, C-02, C-07 |
| C-19 | Cross-tier error coverage | PASS | BAD block + correction table cover C-05, C-06, C-07 |
| C-20 | Per-zone dep constraint reminder | PASS | Design: `# review:* cannot appear here; draft:spec must exist first (C-05)` at skills line; Validation/Simulation/Synthesis all have skills-line reminders |
| C-21 | Correction table scaffold integration | **PARTIAL** | Discovery and Design gate fields carry `-- check correction table`; Validation/Simulation/Synthesis gates do not; skills and name fields lack inline bridge |
| C-22 | Complete recommended-tier error annotation | PASS | BAD block tags C-05, C-06, C-07; correction table has all three; template inline carries `(WRONG C-06)`, `(C-05)`, `(WRONG C-04)` tags — three artifact types |
| C-23 | Dual-position zone dep reminder | **FAIL** | Skills-line reminders present, but zone headers use inconsistent framing — not `# requires: <artifact> from Zone: <name> (C-05)` format at both positions |
| C-24 | Template-field gate contrast | **FAIL** | Comment-based prohibitions only; no `gate_fail:`/`gate_pass:` YAML sibling keys |

**Essential**: 4/4 × 60 = **60**
**Recommended**: 3/3 × 30 = **30**
**Aspirational**: 13 PASS + 1 PARTIAL + 3 FAIL = (13 + 0.5)/17 × 85 = **67.5**
**Composite: 157.5 / 175 — Golden: YES**

---

### V-02 — Symmetric Dual-Position Zone Dependency Reminders (C-23 axis)

| # | Criterion | Result | Evidence note |
|---|-----------|--------|---------------|
| C-01 | Valid YAML structure | PASS | |
| C-02 | Echo stage contract | PASS | REQUIRED annotations; echo last |
| C-03 | Valid skill names | PASS | Catalog + BAD block WRONG C-03 |
| C-04 | Evidence-state gates | PASS | Per-zone FAIL/PASS gate pairs + BAD block WRONG C-04 |
| C-05 | Namespace dep order | PASS | Dual-position `# requires:` + BAD block WRONG C-05 + dep order stated |
| C-06 | Descriptive stage names | PASS | BAD block WRONG C-06; zone header name examples `NOT "scout"` etc. |
| C-07 | Plan identity present | PASS | Opening paragraph + BAD block WRONG C-07 + REQUIRED comment in scaffold |
| C-08 | Quantified gate | PASS | PASS gate examples: `>= 2 signals reviewed`; gate placeholder instructs numeric threshold |
| C-09 | Deliberate evidence arc | PASS | Zone sequence: Discovery→Design→Validation→Simulation→Synthesis |
| C-10 | Failure-mode contrast pair | PASS | BAD PLAN block |
| C-11 | Structural enforcement | PASS | Echo pre-positioned; zone structure enforces dep order |
| C-12 | Dual-anchor reinforcement | PASS | BAD block (1) + per-zone FAIL/PASS contrast (2) for each essential criterion |
| C-13 | Arc as structural spine | PASS | Zone headers `==== Zone: Discovery ====` are the structural spine |
| C-14 | Deletion-resistance annotations | PASS | Echo: REQUIRED DO NOT add/move annotations |
| C-15 | Plan-level YAML error artifact | PASS | Complete BAD PLAN block |
| C-16 | Criterion-referenced error tagging | PASS | BAD block tags C-07, C-06, C-03, C-05, C-04, C-02 |
| C-17 | Per-zone gate contrast | PASS | Every zone header has `# FAIL gate: "..." Why: ...` and `# PASS gate: "..." Why: ...` |
| C-18 | Correction table | **FAIL** | No correction table (by design) |
| C-19 | Cross-tier error coverage | PASS | BAD block covers C-05, C-06, C-07 alongside essential |
| C-20 | Per-zone dep constraint reminder | PASS | Design/Validation/Simulation/Synthesis all have skills-line `# requires: <artifact> from Zone: <name> (C-05)` |
| C-21 | Correction table scaffold integration | **FAIL** | No correction table — C-18 prerequisite fails |
| C-22 | Complete recommended-tier error annotation | PASS (side-effect) | BAD block tags all three: WRONG C-07, WRONG C-06, WRONG C-05 |
| C-23 | Dual-position zone dep reminder | PASS | All four dependent zones: `# requires:` at zone header AND `# requires:` at skills line in same format |
| C-24 | Template-field gate contrast | **FAIL** | Comment-based FAIL/PASS in zone headers; no YAML sibling keys |

**Essential**: 60 | **Recommended**: 30
**Aspirational**: 14 PASS + 0 PARTIAL + 3 FAIL = 14/17 × 85 = **70**
**Composite: 160 / 175 — Golden: YES**

---

### V-03 — Template-Field Gate Contrast (C-24 axis)

| # | Criterion | Result | Evidence note |
|---|-----------|--------|---------------|
| C-01 | Valid YAML | PASS | |
| C-02 | Echo contract | PASS | REQUIRED at echo; correction table C-02 |
| C-03 | Valid skill names | PASS | Catalog + correction table C-03 entries |
| C-04 | Evidence-state gates | PASS | `gate_fail:`/`gate_pass:` YAML keys show wrong+right; correction table (4 pairs); BAD block |
| C-05 | Namespace dep order | PASS | Layer 2 header note; correction table C-05; BAD block WRONG C-05 ×2 |
| C-06 | Descriptive stage names | PASS | Correction table (4 C-06 pairs); template name comments `NOT "scout"/"draft"/"review"/"listen"` |
| C-07 | Plan identity present | PASS | REQUIRED comment; correction table C-07; opening statement |
| C-08 | Quantified gate | PASS | `gate_pass: "... >= 2 signals reviewed"`; gate placeholder: "include numeric threshold" |
| C-09 | Deliberate evidence arc | PASS | Layer 1: Breadth / Layer 2: Depth / Layer 3: Synthesis |
| C-10 | Failure-mode contrast pair | PASS | BAD block + gate_fail/gate_pass per zone |
| C-11 | Structural enforcement | PASS | Echo pre-positioned; gate_fail/gate_pass forces structural engagement with wrong form |
| C-12 | Dual-anchor reinforcement | PASS | All 4 essentials: gate_fail/gate_pass (1) + correction table (2) + BAD block (3) |
| C-13 | Arc as structural spine | PASS | Layer 1/Layer 2/Layer 3 headers are the top-level structural divisions |
| C-14 | Deletion-resistance annotations | PASS | Echo: REQUIRED annotations ×3 with correction table pointer |
| C-15 | Plan-level YAML error artifact | PASS | BAD block present |
| C-16 | Criterion-referenced error tagging | PASS | BAD block: WRONG C-05 ×2, WRONG C-04; gate_fail fields: `# WRONG C-04` |
| C-17 | Per-zone gate contrast | PASS | `gate_fail:` / `gate_pass:` YAML fields at every non-echo zone |
| C-18 | Correction table | PASS | 15 entries, criteria C-04/C-03/C-06/C-05/C-02/C-07 covered |
| C-19 | Cross-tier error coverage | PASS | Correction table covers C-05, C-06, C-07 |
| C-20 | Per-zone dep constraint reminder | **PARTIAL** | Validation: `# requires draft:spec (C-05)` at skills; Simulation: `# requires review:* (C-05)` at skills; Design and Synthesis skills lines only have `# check correction table: skill names` — no dep reminder |
| C-21 | Correction table scaffold integration | **PARTIAL** | Name fields: `# check correction table: stage names`; skills fields: `# check correction table: skill names`; gate fields: use gate_fail/gate_pass structural mechanism instead of `# check correction table` — not all covered field types use the bridge annotation |
| C-22 | Complete recommended-tier annotation | PASS | Correction table covers C-05, C-06, C-07 — all three recommended criteria in error artifact |
| C-23 | Dual-position zone dep reminder | **FAIL** | No zone-header `# requires:` in consistent format; skills-line dep notes only for Validation and Simulation; Design and Synthesis absent |
| C-24 | Template-field gate contrast | PASS | `gate_fail:` / `gate_pass:` / `gate:` as actual YAML sibling keys at all 5 non-echo zones |

**Essential**: 60 | **Recommended**: 30
**Aspirational**: 14 PASS + 2 PARTIAL + 1 FAIL = (14 + 1)/17 × 85 = **75**
**Composite: 165 / 175 — Golden: YES**

---

### V-04 — C-22 + C-23 Combined

| # | Criterion | Result | Evidence note |
|---|-----------|--------|---------------|
| C-01 | Valid YAML | PASS | |
| C-02 | Echo contract | PASS | REQUIRED annotations ×3; correction table C-02 |
| C-03 | Valid skill names | PASS | Catalog + correction table C-03 + BAD block WRONG C-03 |
| C-04 | Evidence-state gates | PASS | Per-zone `# FAIL gate:` / `# PASS gate:` in zone headers; correction table (4 pairs); BAD block |
| C-05 | Namespace dep order | PASS | Dual-position `# requires:` + BAD block WRONG C-05 + correction table C-05 rows |
| C-06 | Descriptive stage names | PASS | BAD block WRONG C-06; correction table (4 C-06 pairs); template name comments `(WRONG C-06)` |
| C-07 | Plan identity present | PASS | Opening paragraph; BAD block WRONG C-07; correction table C-07; REQUIRED comment |
| C-08 | Quantified gate | PASS | PASS gate examples have `>= 2 signals reviewed`; gate placeholder prompts quantified condition |
| C-09 | Deliberate evidence arc | PASS | Zone sequence Discovery→Design→Validation→Simulation→Synthesis |
| C-10 | Failure-mode contrast pair | PASS | BAD PLAN block |
| C-11 | Structural enforcement | PASS | Echo pre-positioned; zone structure; correction table at every field |
| C-12 | Dual-anchor reinforcement | PASS | All 4 essentials: BAD block + correction table + scaffold = ≥3 anchors each |
| C-13 | Arc as structural spine | PASS | `==== Zone: Discovery / Design / Validation / Simulation / Synthesis ====` headers are the structural spine |
| C-14 | Deletion-resistance annotations | PASS | Echo: `# REQUIRED: DO NOT add skills here. DO NOT move echo before other stages. (WRONG C-02 if violated)` + two more REQUIRED lines |
| C-15 | Plan-level YAML error artifact | PASS | Complete BAD PLAN YAML block |
| C-16 | Criterion-referenced error tagging | PASS | BAD block tags C-07, C-06, C-03, C-05, C-04, C-02 |
| C-17 | Per-zone gate contrast | PASS | Every zone header: `# FAIL gate: "..." <-- WRONG C-04` + `# PASS gate: "..."`|
| C-18 | Correction table | PASS | 15+ entries covering all 7 criteria |
| C-19 | Cross-tier error coverage | PASS | BAD block + correction table cover all three recommended |
| C-20 | Per-zone dep constraint reminder | PASS | All four dependent zones have `# requires: <artifact> from Zone: <name> (C-05)` at skills line |
| C-21 | Correction table scaffold integration | PASS | Name fields: `# check correction table: stage names -- NOT "draft" (WRONG C-06)`; skills fields: `# check correction table: skill names; requires: ...`; gate fields: `# check correction table: gates -- NOT "done" (WRONG C-04)` |
| C-22 | Complete recommended-tier annotation | PASS | BAD block tags C-07, C-06, C-05 (all three); correction table has C-07/C-06/C-05 rows |
| C-23 | Dual-position zone dep reminder | PASS | All four dependent zones: `# requires:` at zone-header comment AND `# requires:` at skills line, consistent format |
| C-24 | Template-field gate contrast | **FAIL** | Comment-based FAIL/PASS annotations in zone headers; no `gate_fail:`/`gate_pass:` YAML sibling keys |

**Essential**: 60 | **Recommended**: 30
**Aspirational**: 16 PASS + 0 PARTIAL + 1 FAIL = 16/17 × 85 = **80**
**Composite: 170 / 175 — Golden: YES**

---

### V-05 — Golden Synthesis (all 24 criteria)

| # | Criterion | Result | Evidence note |
|---|-----------|--------|---------------|
| C-01 | Valid YAML | PASS | |
| C-02 | Echo contract | PASS | REQUIRED annotations ×3; correction table C-02; echo pre-positioned |
| C-03 | Valid skill names | PASS | Catalog + correction table (4 C-03 entries) + BAD block WRONG C-03 + GOOD PLAN uses only real names |
| C-04 | Evidence-state gates | PASS | `gate_fail:`/`gate_pass:` YAML keys per zone; correction table (5 C-04 pairs); BAD block; GOOD PLAN shows passing gates |
| C-05 | Namespace dep order | PASS | Dual-position `# requires:`; BAD block WRONG C-05; correction table C-05; GOOD PLAN shows correct ordering |
| C-06 | Descriptive stage names | PASS | BAD block WRONG C-06 ×2; correction table (4 C-06 pairs); template name comments; GOOD PLAN uses `discovery`/`design`/`expert-review`/`feedback-preview` |
| C-07 | Plan identity present | PASS | Opening paragraph; BAD block WRONG C-07; correction table C-07; REQUIRED comment with C-07 label; GOOD PLAN absence of executor framing |
| C-08 | Quantified gate | PASS | gate_pass examples: `>= 2 signals reviewed`, `0 P0 findings open`; GOOD PLAN: `>= 2 scout signals reviewed` |
| C-09 | Deliberate evidence arc | PASS | Zone arc Discovery→Design→Validation→Simulation→Synthesis; GOOD PLAN demonstrates the arc |
| C-10 | Failure-mode contrast pair | PASS | BAD PLAN + GOOD PLAN paired contrast on essential criteria |
| C-11 | Structural enforcement | PASS | Echo pre-positioned; zone structure; gate_fail/gate_pass; correction table at every field position |
| C-12 | Dual-anchor reinforcement | PASS | All 4 essentials: BAD block + GOOD PLAN + correction table + scaffold ≥3 anchors each |
| C-13 | Arc as structural spine | PASS | `==== Zone: Discovery / Design / Validation / Simulation / Synthesis ====` are the load-bearing structural divisions |
| C-14 | Deletion-resistance annotations | PASS | Echo: `# REQUIRED: DO NOT add skills here. DO NOT move echo before other stages. (WRONG C-02 if violated)` + REQUIRED annotations on skills:[] and auto:true |
| C-15 | Plan-level YAML error artifact | PASS | Complete BAD PLAN YAML block spanning multiple stages with multi-field violations |
| C-16 | Criterion-referenced error tagging | PASS | BAD block: WRONG C-07, C-06, C-03, C-05, C-04, C-02 |
| C-17 | Per-zone gate contrast | PASS | `gate_fail:`/`gate_pass:` YAML keys at all 5 non-echo zones |
| C-18 | Correction table | PASS | 18 entries across all 7 criteria |
| C-19 | Cross-tier error coverage | PASS | BAD block + correction table cover C-05, C-06, C-07 |
| C-20 | Per-zone dep constraint reminder | PASS | All four dependent zones have skills-line `# requires: <artifact> from Zone: <name> (C-05)` |
| C-21 | Correction table scaffold integration | PASS | Name fields: `# check correction table: stage names -- NOT "scout" (WRONG C-06)`; skills fields: `# check correction table: skill names; requires: ...`; gate fields: `# check correction table: gates -- NOT "done" (WRONG C-04)` |
| C-22 | Complete recommended-tier annotation | PASS | BAD block tags C-07, C-06, C-05; correction table has all three — both artifact types, all three recommended criteria |
| C-23 | Dual-position zone dep reminder | PASS | All four dependent zones: zone header `# requires: <artifact> from Zone: <name> (C-05)` AND skills line `# requires: <artifact> from Zone: <name> (C-05)` in identical format |
| C-24 | Template-field gate contrast | PASS | `gate_fail:`/`gate_pass:`/`gate:` as YAML sibling keys at all 5 non-echo zones; instruction: "Write your gate: value using gate_pass as the model" |

**Essential**: 60 | **Recommended**: 30
**Aspirational**: 17/17 × 85 = **85**
**Composite: 175 / 175 — Golden: YES — PERFECT SCORE**

---

## Ranking

| Variation | Composite | Golden | Key differentiator |
|-----------|-----------|--------|-------------------|
| V-05 | 175.0 | YES | C-22 + C-23 + C-24 all PASS; GOOD PLAN worked example |
| V-04 | 170.0 | YES | C-22 + C-23 PASS; only C-24 absent |
| V-03 | 165.0 | YES | C-24 PASS; C-23 FAIL; C-20/C-21 PARTIAL |
| V-02 | 160.0 | YES | C-23 PASS; C-18/C-21 FAIL by design |
| V-01 | 157.5 | YES | C-22 PASS (three artifact types); C-17/C-23/C-24 FAIL |

---

## Excellence Signals from V-05

**1. GOOD-PLAN positive anchor alongside BAD-PLAN negative anchor.**
V-05 is the first variation to include a complete, correct multi-stage GOOD PLAN YAML block alongside the BAD PLAN block. The model sees the target output shape before reaching the template — not just what to avoid, but what to produce. This is a positive confirmation anchor not captured by any existing criterion. The BAD block teaches error avoidance; the GOOD block provides the gestalt of the correct structure; together they bracket the solution space.

**2. Meta-directive at the generation moment: "use gate_pass as the model."**
The `gate:` placeholder in V-05 carries the instruction `"<fill in: use gate_pass as model; include numeric threshold; delete gate_fail/gate_pass>"`. This converts the gate_pass field from a passive example into an active generation directive — the model is not just shown the right gate form, it is told at the exact field position to copy from it. Per-zone contrast (C-24) plus this meta-directive close the last gap: seeing the correct form is necessary but not sufficient; being instructed to use it as the model is the final lock.

**3. Zero-gap cross-mechanism completeness.**
In V-05, every mechanism is complete at its level: the correction table covers all 7 criteria, the BAD block tags all 7, dual-position dep reminders cover all 4 dependent zones in consistent format, gate_fail/gate_pass covers all 5 non-echo zones, correction table bridges appear at all three covered field types. No single criterion is left unaddressed by any mechanism that could address it. Prior variations were complete in some mechanisms and partial in others, leaving criteria with single-anchor coverage. V-05 achieves what might be called internal consistency of coverage: removing any one mechanism still leaves every criterion covered by at least one other.

---

```json
{"top_score": 175, "all_essential_pass": true, "new_patterns": ["Complete GOOD-PLAN worked example alongside BAD-PLAN block provides a positive confirmation anchor — the model sees the correct output gestalt before reaching the template, bracketing the solution space between the wrong shape and the right shape", "Meta-directive at the generation point ('use gate_pass as model') converts structural contrast from passive reading into an active copy instruction — per-zone structural contrast plus this directive close the gap between seeing the correct form and being directed to use it"]}
```
