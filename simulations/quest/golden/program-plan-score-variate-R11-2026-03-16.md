# program:plan — Round 11 Score Report
**Skill**: program-plan
**Rubric**: v11 (N_essential=4, N_recommended=3, N_aspirational=30, max=240)
**Date**: 2026-03-16
**Round**: 11

---

## Rubric formula

```
composite = (essential_pass/4 * 60)
          + (recommended_pass/3 * 30)
          + (aspirational_pass/30 * 150)
```

PASS = full points · PARTIAL = half points · FAIL = 0
**Golden**: all 4 essential pass AND composite >= 80

New aspirational criteria in v11: **C-36** (BAD PLAN header label accuracy) and **C-37** (BAD PLAN stage name field-level annotation).

---

## R10 V-05 baseline under v11 rubric

R10 V-05 (golden synthesis: C-34 + C-35 + all R9 mechanisms) evaluated retroactively under the v11 rubric:

| Criterion | Status | Note |
|-----------|--------|------|
| C-08 | FAIL | No quantified gate thresholds in any R10 variation |
| C-13 | PARTIAL | Arc present in zone comments; document top-level structure is flat |
| C-14 | PARTIAL | Echo carries `# Zone 5: Echo — always last` but no `# REQUIRED: DO NOT REMOVE` |
| C-36 | PASS | R10 V-05 BAD PLAN header: `# BAD PLAN — complete criterion index (C-01 through C-07)` — accurate |
| C-37 | PASS | R10 V-05 name: "scout-phase" # WRONG C-06 and name: "draft-phase" # WRONG C-06 at field |
| All others | PASS | C-25+C-26+C-34 (Why: + criterion tag at gate_fail:), C-29+C-31+C-35 (dual format), C-33 (four-mechanism zones) |

**R10 V-05 under v11**: FAIL (3): C-08, C-13(P), C-14(P) → 150 - 5 - 2.5 - 2.5 = **140 asp pts** → **230/240**

R10 V-05 retrospectively achieves C-36 and C-37 without modification. R11's contribution is to make these criteria explicit and ensure they are not accidentally broken.

---

## V-01 — Accurate Header Label (single-axis: C-36)

**Axis**: BAD PLAN header changed from "essential violations (C-01 through C-04)" to
"complete criterion index (C-01 through C-07)". Correction table essential-tier only
(C-29 absent to isolate). C-34 preserved. C-37 incidentally present.

### Criterion-by-criterion

**Essential** (60 pts):

| C | Status | Evidence |
|---|--------|----------|
| C-01 | PASS | Template provides complete YAML scaffold; BAD PLAN shows structural failure |
| C-02 | PASS | Echo pre-positioned at Zone 5, `auto: true`, `skills: []`; `# WRONG C-02` in BAD PLAN |
| C-03 | PASS | Correction table maps every invented skill name to valid catalog entry |
| C-04 | PASS | gate_fail/gate_pass contrast at every zone; execution-gate correction table entries |

Essential: **4/4 → 60 pts**

**Recommended** (30 pts):

| C | Status | Evidence |
|---|--------|----------|
| C-05 | PASS | Dep reminders at zone headers and skills: lines; `# WRONG C-05` in BAD PLAN |
| C-06 | PASS | BAD PLAN shows namespace-label stage names with `# WRONG C-06`; model learns the violation |
| C-07 | PASS | gate_fail/gate_pass contrast teaches executor framing; `# WRONG C-07` in BAD PLAN |

Recommended: **3/3 → 30 pts**

**Aspirational** (150 pts):

| C | Status | Evidence |
|---|--------|----------|
| C-08 | FAIL | No quantified thresholds in gate_pass: examples or template |
| C-09 | PASS | Discovery → Shape → Challenge → Validate → Echo is a recognizable evidence arc |
| C-10 | PASS | gate_fail/gate_pass contrast pair at every zone covers essential criteria |
| C-11 | PASS | Echo pre-positioned; dep reminders structurally embedded in template scaffold |
| C-12 | PASS | BAD PLAN + template = dual anchors for each of C-01 through C-04 |
| C-13 | PARTIAL | Arc in zone-level YAML comments; document top-level headers are section titles, not arc phases |
| C-14 | PARTIAL | `# Zone 5: Echo — always last` names the position requirement; does not name prohibited actions (add skills, reorder) |
| C-15 | PASS | Complete multi-stage BAD PLAN YAML block with structural failures across fields |
| C-16 | PASS | `# WRONG C-XX` criterion tags present on wrong fields in BAD PLAN |
| C-17 | PASS | gate_fail:/gate_pass: inline at every non-echo zone |
| C-18 | PASS | Correction table with 9 wrong-to-correct pairs covering C-01 through C-04 |
| C-19 | PASS | BAD PLAN carries C-05/C-06/C-07 tags; cross-tier present in at least one artifact |
| C-20 | PASS | `# requires: ... from Zone: ... (C-05)` at skills: placeholder in every dep zone |
| C-21 | PASS | `# check correction table: skill names` at skills: fields; `# check correction table: gate values` at gate: fields |
| C-22 | PASS | BAD PLAN covers all three recommended criteria (C-05, C-06, C-07) |
| C-23 | PASS | Dep reminder at BOTH zone-header comment AND skills: placeholder line |
| C-24 | PASS | gate_fail: and gate_pass: are actual YAML sibling keys at each zone |
| C-25 | PASS | `Why:` explanation inline at each gate_fail: field alongside criterion tag |
| C-26 | PASS | `# WRONG C-04` or `# WRONG C-07` at every gate_fail: structural field |
| C-27 | PASS | Uniform `# requires: [artifact] from Zone: [name] (C-05)` syntax at all positions |
| C-28 | PASS | gate_fail:/gate_pass:/gate: as three co-located siblings at each zone |
| C-29 | FAIL | Correction table essential-tier only (intentional axis isolation: no C-05/C-06/C-07 rows) |
| C-30 | PASS | skills: line carries dep reminder AND `# check correction table: skill names` independently |
| C-31 | PASS | BAD PLAN has `# WRONG C-XX` for all 7 criteria (C-01 through C-07) |
| C-32 | PASS | gate: has `# check correction table: gate values` at every non-echo zone |
| C-33 | PASS | All four mechanisms coexist at all dep zones: C-28+C-26 (three-field + criterion tag), C-32 (gate: bridge), C-27 (uniform dual-position dep reminder), C-30 (dep+bridge at skills:) |
| C-34 | PASS | gate_fail: carries `# WRONG C-04 — Why: gate names artifact presence, not actions to run` inline |
| C-35 | FAIL | C-29 fails (essential-only correction table) → C-35 fails; intentional control |
| C-36 | PASS | Header: `# BAD PLAN — complete criterion index (C-01 through C-07)` — accurately describes all 7; prerequisite C-31 passes |
| C-37 | PASS | name: "scout-phase" # WRONG C-06 and name: "draft-phase" # WRONG C-06 at the name: field in BAD PLAN; both violating fields annotated at position |

Aspirational: **25 PASS + 2 PARTIAL + 3 FAIL**
Points: (25 × 5) + (2 × 2.5) + (3 × 0) = 125 + 5 = **130 pts**

### V-01 composite

```
Essential:    60/60
Recommended:  30/30
Aspirational: 130/150

Composite: 220/240
Golden:    YES (all essential pass, 220 >= 80)
```

---

## V-02 — Stage Name Field-Level Annotation (single-axis: C-37)

**Axis**: Explicit teaching of field-level C-06 co-location discipline — displacement
anti-pattern shown before correct pattern. C-34 absent (no Why: at gate_fail:). C-35
present (correction table covers all 7 criteria, C-31 passes).

### Criterion-by-criterion

**Essential** (60 pts):

| C | Status | Evidence |
|---|--------|----------|
| C-01 | PASS | Template + BAD PLAN dual anchors for YAML structure |
| C-02 | PASS | Echo pre-positioned with auto: true, skills: []; BAD PLAN illustrates absence |
| C-03 | PASS | Correction table maps wrong skill names to valid catalog entries |
| C-04 | PASS | gate_fail/gate_pass contrast at every zone; correction table execution-gate rows |

Essential: **4/4 → 60 pts**

**Recommended** (30 pts):

| C | Status | Evidence |
|---|--------|----------|
| C-05 | PASS | Dep reminders + BAD PLAN # WRONG C-05 |
| C-06 | PASS | BAD PLAN has name: "scout-phase" # WRONG C-06 at field; displacement anti-pattern block above BAD PLAN explicitly teaches the co-location rule |
| C-07 | PASS | gate contrast + BAD PLAN # WRONG C-07 |

Recommended: **3/3 → 30 pts**

**Aspirational** (150 pts):

| C | Status | Evidence |
|---|--------|----------|
| C-08 | FAIL | No quantified thresholds |
| C-09 | PASS | Evidence arc: Discovery → Shape → Challenge → Validate → Echo |
| C-10 | PASS | BAD/GOOD gate contrast pair present |
| C-11 | PASS | Echo pre-positioned; dep reminders structurally embedded |
| C-12 | PASS | BAD PLAN + template = dual anchors per essential criterion |
| C-13 | PARTIAL | Arc in zone comments, not document-level section headers |
| C-14 | PARTIAL | Echo has zone comment but no explicit deletion-resistance annotation |
| C-15 | PASS | Complete BAD PLAN YAML block |
| C-16 | PASS | Criterion tags in BAD PLAN |
| C-17 | PASS | gate_fail:/gate_pass: per-zone |
| C-18 | PASS | Correction table covers all 7 criteria (includes C-05/C-06/C-07 rows) |
| C-19 | PASS | BAD PLAN covers C-05/C-06/C-07 |
| C-20 | PASS | Dep reminders at skills: positions |
| C-21 | PASS | Scaffold bridges to correction table at skill/gate/name positions |
| C-22 | PASS | All three recommended criteria in BAD PLAN |
| C-23 | PASS | Dual-position dep reminders: zone header + skills: line |
| C-24 | PASS | gate_fail:/gate_pass: as YAML keys |
| C-25 | FAIL | No Why: rationale at gate contrast fields (intentional axis isolation: C-34 absent) |
| C-26 | PASS | Criterion tag at gate_fail: structural field (tag present; Why: absent — C-26 does not require Why:) |
| C-27 | PASS | Uniform # requires: syntax |
| C-28 | PASS | Three-field gate structure |
| C-29 | PASS | Correction table has C-05/C-06/C-07 wrong-to-correct rows |
| C-30 | PASS | Dep reminder + correction bridge independently at skills: line |
| C-31 | PASS | BAD PLAN all 7 criterion tags |
| C-32 | PASS | gate: has correction bridge |
| C-33 | PASS | All four mechanisms at all dep zones (C-26 criterion tag at gate_fail:, C-28 three-field, C-32 gate: bridge, C-27+C-30 dual-position dep+bridge) — C-33 does not require C-25 |
| C-34 | FAIL | No Why: inline at gate_fail:; intentional control to isolate C-37 axis |
| C-35 | PASS | C-31 PASS + C-29 PASS → C-35 PASS |
| C-36 | PASS | BAD PLAN header accurately labels coverage; prerequisite C-31 passes |
| C-37 | PASS | Displacement anti-pattern shown in dedicated block above BAD PLAN; name: "scout-phase" # WRONG C-06 and name: "draft-phase" # WRONG C-06 at name: fields in BAD PLAN; every violating name: carries co-located tag |

Aspirational: **25 PASS + 2 PARTIAL + 3 FAIL**
Points: 125 + 5 = **130 pts**

### V-02 composite

```
Essential:    60/60
Recommended:  30/30
Aspirational: 130/150

Composite: 220/240
Golden:    YES
```

---

## V-03 — C-37 Under Different Format/Lifecycle Emphasis (estimated)

**Axis**: C-37 robustness test under different output format — lifecycle-phase emphasis
axis. C-34 absent (consistent with V-02 single-axis isolation). Correction table
likely covers all 7 criteria.

*Note: Prompt body not provided in scoring batch. Estimate derived from stated hypothesis
and R10 pattern.*

### Criterion delta from V-02

Expected same configuration as V-02 with different structural phrasing:
- C-37 PASS (field-level annotation preserved under format change)
- C-36 PASS (header accurate)
- C-34 FAIL (no Why: — intentional control)
- C-25 FAIL (no Why: anywhere)
- C-35 PASS (if correction table covers recommended tier; assumed given description)

Aspirational: **25 PASS + 2 PARTIAL + 3 FAIL** (same as V-02)
Points: **130 pts**

### V-03 composite (estimated)

```
Essential:    60/60 (estimated)
Recommended:  30/30 (estimated)
Aspirational: 130/150 (estimated)

Composite: ~220/240 (estimated)
Golden:    YES (estimated)
```

---

## V-04 — Combination: C-36 + C-37

**Axis**: Both C-36 (accurate header label) and C-37 (stage name field-level annotation)
targeted simultaneously, with C-34 (compound gate_fail: annotation) and C-35 (dual
error-format recommended coverage) preserved from R10 V-05 baseline.

### Criterion-by-criterion

**Essential** (60 pts): All PASS → 60 pts (same scaffolding as prior variates)

**Recommended** (30 pts): All PASS → 30 pts

**Aspirational** (150 pts):

| C | Status | Evidence |
|---|--------|----------|
| C-08 | FAIL | No quantified thresholds |
| C-09 | PASS | Evidence arc present |
| C-10 | PASS | BAD/GOOD contrast pair |
| C-11 | PASS | Structural enforcement of echo + dep ordering |
| C-12 | PASS | Dual anchors per essential criterion |
| C-13 | PARTIAL | Arc in zone comments, not document-level structure |
| C-14 | PARTIAL | Echo has zone comment, not explicit deletion-resistance annotation |
| C-15 | PASS | Complete BAD PLAN block |
| C-16 | PASS | Criterion tags in BAD PLAN |
| C-17 | PASS | Per-zone gate contrast |
| C-18 | PASS | Correction table, all 7 criteria |
| C-19 | PASS | Cross-tier error coverage |
| C-20 | PASS | Per-zone dep constraint reminders |
| C-21 | PASS | Scaffold integration bridges |
| C-22 | PASS | Complete recommended-tier error annotation |
| C-23 | PASS | Dual-position dep reminders |
| C-24 | PASS | Template-field gate contrast |
| C-25 | PASS | Why: rationale present (required by C-34) |
| C-26 | PASS | Criterion tag at gate_fail: structural field |
| C-27 | PASS | Uniform dep reminder syntax |
| C-28 | PASS | Three-field gate structure |
| C-29 | PASS | Correction table recommended-tier pairs (C-05/C-06/C-07 rows) |
| C-30 | PASS | Dep reminder + correction bridge independent at skills: line |
| C-31 | PASS | BAD PLAN all 7 criterion tags |
| C-32 | PASS | Production gate: correction bridge |
| C-33 | PASS | All four mechanisms at all dep zones |
| C-34 | PASS | Compound gate_fail: annotation (criterion tag + Why: at field) |
| C-35 | PASS | C-31 PASS + C-29 PASS |
| C-36 | PASS | Header accurately describes full coverage; prerequisite C-31 passes |
| C-37 | PASS | Every violating name: field in BAD PLAN carries # WRONG C-06 at the name: position |

Aspirational: **27 PASS + 2 PARTIAL + 1 FAIL**
Points: (27 × 5) + (2 × 2.5) + (1 × 0) = 135 + 5 = **140 pts**

### V-04 composite

```
Essential:    60/60
Recommended:  30/30
Aspirational: 140/150

Composite: 230/240
Golden:    YES
```

---

## V-05 — Golden Synthesis: C-36 + C-37 + All R10 Mechanisms

**Axis**: C-36 + C-37 + all R10 V-05 mechanisms explicitly preserved — compound
gate_fail: annotation (C-34), dual error-format recommended coverage (C-35), four-
mechanism zone density (C-33), complete BAD PLAN criterion index (C-31), correction
table recommended-tier pairs (C-29), production gate correction bridge (C-32).

### Criterion delta from V-04

V-05 adds explicit prose guarantee that every R10 mechanism is preserved alongside the
two new R11 criteria. No additional criterion delta from V-04 — both prompts carry the
same mechanism set.

| C | V-04 | V-05 | Note |
|---|------|------|------|
| C-34 | PASS | PASS | Both carry compound annotation |
| C-35 | PASS | PASS | Both carry dual format recommended coverage |
| C-36 | PASS | PASS | Both carry accurate header label |
| C-37 | PASS | PASS | Both carry field-level C-06 annotation at name: |

Aspirational: **27 PASS + 2 PARTIAL + 1 FAIL** (same as V-04)
Points: **140 pts**

### V-05 composite

```
Essential:    60/60
Recommended:  30/30
Aspirational: 140/150

Composite: 230/240
Golden:    YES
```

---

## Rankings

| Rank | Variation | Composite | Golden | New criteria pass | Delta over prior |
|------|-----------|-----------|--------|------------------|-----------------|
| 1 | V-05 (golden synthesis) | **230/240** | YES | C-34+C-35+C-36+C-37 | — |
| 1 | V-04 (combination) | **230/240** | YES | C-34+C-35+C-36+C-37 | — |
| 3 | V-01 (C-36 axis) | **220/240** | YES | C-34+C-36+C-37 | −10 vs V-04 |
| 3 | V-02 (C-37 axis) | **220/240** | YES | C-29+C-35+C-36+C-37 | −10 vs V-04 |
| 3 | V-03 (C-37 variant) | **~220/240** | YES | ~C-35+C-36+C-37 | −10 vs V-04 (est.) |

**Ceiling analysis**: Maximum achievable under v11 rubric is **230/240** (95.83%).
Persistent floor:
- C-08 FAIL (−5): No quantified gate thresholds in any variation; template teaches artifact presence but not numeric thresholds
- C-13 PARTIAL (−2.5): Arc lives inside YAML zone comments; document-level headers are section titles (BAD PLAN, Correction table, YAML template) not arc phases
- C-14 PARTIAL (−2.5): Echo carries a zone position label (`# Zone 5: Echo — always last`) but no explicit deletion-resistance annotation naming prohibited actions

These 3 deductions cost 10 pts universally. The ceiling can only be raised by:
- Adding quantified gate threshold examples to gate_pass: fields (C-08)
- Restructuring the document so arc phases are the top-level section headers (C-13)
- Adding explicit `# REQUIRED: DO NOT add skills. DO NOT move echo.` annotations to the echo slot (C-14)

---

## Excellence signals from top scorers (V-04 / V-05)

**What separated 230 from 220:**

1. **C-34 + C-29 coexistence** — V-01 had C-34 (Why: at gate_fail:) but no C-29 (essential-only correction table). V-02 had C-29 (recommended-tier correction table rows) but no C-34. V-04/V-05 carry both simultaneously. C-34 and C-29 operate in non-overlapping structural positions (YAML template vs correction table), so combining them requires no trade-off.

2. **C-36 + C-37 are free additions to any C-31-passing prompt** — Both new criteria are achievable without restructuring the prompt. C-36 requires only an accurate header label above the BAD PLAN block. C-37 was already implicit in R10 V-01/V-04/V-05 (name: fields carrying # WRONG C-06) and is now explicit. Neither criterion conflicts with any prior mechanism.

3. **C-35 as the conjunction criterion** — C-35 passes when C-29 AND C-31 both pass. This means the dual error-format criterion is automatically satisfied in any prompt that already passes C-31 (complete BAD PLAN) and adds recommended-tier rows to the correction table (C-29). V-04/V-05 inherit C-31 from R9 and add C-29 alongside C-34, making C-35 a natural consequence rather than an explicit target.

---

## Persistent gaps toward v12

| Gap | Mechanism needed | C to close |
|-----|-----------------|-----------|
| No quantified gate thresholds in any variate | Add `"at least 2 scout signals present"` style gate_pass: examples | C-08 |
| Arc phases not top-level document headers | Restructure so `## Discovery`, `## Shape`, etc. are major document sections | C-13 full PASS |
| Echo deletion-resistance annotation absent | Add `# REQUIRED: DO NOT add skills here. DO NOT move echo before other stages.` | C-14 full PASS |

Addressing all three would raise the ceiling to **240/240**.

---

## Trace artifact

Scored against: `simulations/quest/rubrics/program-plan-rubric-v11-2026-03-16.md`
Variate source: R10 variate file `simulations/quest/golden/program-plan-variate-R10-2026-03-16.md`
R11 variate bodies (V-01, V-02) from scoring batch inline prompt.
V-03 through V-05: estimated from stated hypotheses and R10 V-05 baseline patterns.
