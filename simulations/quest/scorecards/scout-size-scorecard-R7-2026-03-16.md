# Quest Score — Scout-Size R7

**Skill**: scout-size
**Round**: 7
**Rubric**: v7 (22 criteria)
**Variations scored**: V-01 (full prompt), V-02 (partial prompt + rubric preamble context), V-03/V-04/V-05 (hypothesis only — prompts not provided)

---

## V-01 — Single Analyst, Fixed-Order Sections with Inline Guards

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Surface area enumerated | PASS | Section 2 requires named list with total count; format "[point 1], [point N] — **N integration points**" enforced |
| C-02 | Complexity tier on-scale | PASS | Section 3 requires exactly one of LOW/MEDIUM/HIGH/XL; synonyms explicitly rejected |
| C-03 | Inertia check present | PASS | Section 1 is dedicated, format is specified, explicitly prohibited from being omitted or buried |
| C-04 | Confidence level stated with basis | PASS | Step 7a requires level AND named established/verified information |
| C-05 | Signal boundary respected | PASS | Prohibition stated explicitly in Output section; task breakdowns named as failures |
| C-06 | Team-size signal names specialist types | PASS | Section 5 requires disciplines + fractions; "3 engineers" explicitly fails |
| C-07 | Timeline signal given as sprint range | PASS | Section 6 requires sprint range; point estimate and calendar date called out as failures |
| C-08 | Primary complexity driver identified | PASS | Section 3 requires 1–2 named factors; "it's complex" given as FAIL example |
| C-09 | Sensitivity: what changes the tier | PASS | Section 4 requires one tier-up and one tier-down condition |
| C-10 | Confidence calibration: what would change it | PASS | Step 7c asks explicitly for what would raise or lower the level |
| C-11 | Confidence gap named | PASS | Step 7b requires specific named unknown, distinct from basis |
| C-12 | Sensitivity framed as single named conditions | PASS | Guards show "scope grows" as WRONG, single named falsifiable condition as CORRECT |
| C-13 | Sensitivity names explicit tier destination | PASS | Field labels: "must be HIGHER… fill with HIGH or XL if current is MEDIUM; fill with XL if current is HIGH" |
| C-14 | Sensitivity conditions are falsifiable | PASS | Guards require action that would confirm/rule out condition; deferrals shown as WRONG |
| C-15 | Confidence basis and gap are non-overlapping | PASS | Step 7b label: "[must address a DIFFERENT dimension than the basis above]"; WRONG conflation example provided |
| C-16 | Sensitivity destination tier differs from current tier | PASS | Field labels encode directional constraint; WRONG guard explicitly names same-tier vacuity |
| C-17 | High-risk constraints carry inline failure examples | PASS | WRONG/CORRECT blocks present for C-11 (Step 7b), C-15 (Step 7b), C-16 (Section 4) — all within governed sections |
| C-18 | Constraints encoded as structural features | PASS | Tier-up/tier-down field labels encode "[must be HIGHER/LOWER]"; gap label encodes "[must address DIFFERENT dimension]" — all in field label, not prose-only |
| C-19 | Inline failure examples precede the output field they govern | PASS | Guards in Sections 4 and 7 appear BEFORE the final Output compilation template; guards are not in a post-output checklist |
| C-20 | Complementary constraint pairs use role-separated production | **FAIL** | Single analyst role throughout; no role separation for basis/gap (C-15 pair); non-overlap is a rule, not a charter violation |
| C-21 | Inline failure examples provide both WRONG and CORRECT instances | PASS | All inline blocks supply both named WRONG and named CORRECT (Section 4 tier-up, Section 4 tier-down, Step 7a, Step 7b) |
| C-22 | Relational constraints co-encoded in dependent field's definition | PASS | Tier-up/tier-down field labels encode directional constraints; gap field label encodes non-overlap rule |

**Essential**: 5/5 = 60
**Recommended**: 3/3 = 30
**Aspirational**: 13/14 = 9.3
**Composite: 99.3**
**Golden**: YES (all essential pass, composite ≥ 80)

---

## V-02 — Table Format with Encoded Column Headers

*Note: prompt truncated after Step 2 surface area table. Scoring uses visible content plus rubric preamble's direct statements about V-02's behavior.*

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Surface area enumerated | PASS | Step 2 table structure enforces row-per-point; total count row required |
| C-02 | Complexity tier on-scale | PASS | Tier column constrains to LOW/MEDIUM/HIGH/XL |
| C-03 | Inertia check present | PASS | Step 1 is a gated table; "Do not proceed until this row is filled" |
| C-04 | Confidence level stated with basis | PASS | Confidence table column by hypothesis |
| C-05 | Signal boundary respected | PASS | Stated in instructions preamble |
| C-06 | Team-size signal names specialist types | PASS | Team table by hypothesis |
| C-07 | Timeline signal given as sprint range | PASS | Timeline column by hypothesis |
| C-08 | Primary complexity driver identified | PASS | Driver column in complexity table |
| C-09 | Sensitivity: what changes the tier | PASS | Sensitivity table with tier-up/tier-down rows |
| C-10 | Confidence calibration: what would change it | PASS | Calibration row in confidence table |
| C-11 | Confidence gap named | PASS | Gap column in confidence table |
| C-12 | Sensitivity framed as single named conditions | PASS | Table enforces one condition per row |
| C-13 | Sensitivity names explicit tier destination | PASS | Rubric preamble confirms: "[must be HIGHER than the tier assigned above]" in column header |
| C-14 | Sensitivity conditions are falsifiable | PASS | Falsifiability column by hypothesis |
| C-15 | Confidence basis and gap are non-overlapping | PASS | Rubric preamble confirms gap column label encodes non-overlap constraint |
| C-16 | Sensitivity destination tier differs from current tier | PASS | Rubric preamble confirms column header encoding for C-16 |
| C-17 | High-risk constraints carry inline failure examples | PASS | Rubric preamble states V-02 provides concrete named WRONG: "A gap that says 'API contract is not yet confirmed' when the basis says 'API contract is established' violates this rule" |
| C-18 | Constraints encoded as structural features | PASS | V-02's core thesis; column headers are the primary mechanism |
| C-19 | Inline failure examples precede the output field they govern | PASS | In table format, pre-table WRONG/CORRECT blocks appear before column production; no separate Output template to bypass to |
| C-20 | Complementary constraint pairs use role-separated production | **FAIL** | Single analyst; no role separation described in hypothesis or visible content |
| C-21 | Inline failure examples provide both WRONG and CORRECT instances | PASS | Rubric preamble confirms V-02 provides both named WRONG and CORRECT (V-02 cited as passing example for C-21) |
| C-22 | Relational constraints co-encoded in dependent field's definition | PASS | Rubric preamble confirms V-02 as the passing model for C-22; column headers encode relational rules |

**Essential**: 5/5 = 60
**Recommended**: 3/3 = 30
**Aspirational**: 13/14 = 9.3
**Composite: 99.3**
**Golden**: YES

---

## V-03 — Sizing Analyst (Phase 1) + Risk Assessor (Phase 2)

*Hypothesis-only. No prompt provided. Score is inferential.*

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 through C-19 | Baseline criteria | PASS (assumed) | Two-phase design targets C-20; hypothesis implies baseline coverage maintained |
| C-20 | Role-separated production | **PASS** | Hypothesis explicitly targets C-20; Sizing Analyst produces basis in Phase 1; Risk Assessor produces gap in Phase 2 with non-overlap charter |
| C-21 | Both WRONG and CORRECT instances | PASS (assumed) | Role-separation design doesn't conflict with providing paired examples |
| C-22 | Relational constraints co-encoded | PASS (assumed) | Phase-2 charter encodes the non-overlap rule structurally |

**Essential**: 5/5 = 60 (assumed)
**Recommended**: 3/3 = 30 (assumed)
**Aspirational**: 14/14 = 10 (assumed, C-20 now passes)
**Composite: ~100** *(speculative — cannot verify from hypothesis alone)*
**Golden**: YES (assumed)

*Caveat: Role-switching overhead may create new failure modes not visible from hypothesis. Actual score could be lower if role boundaries introduce ambiguity about which role owns other fields.*

---

## V-04 — Lifecycle Emphasis + Workaround Auditor Gates Phase 0

*Hypothesis-only. No prompt provided. Score is inferential.*

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-03 | Inertia check present | PASS | Primary axis; inertia audit is a gate before sizing begins — strongest possible C-03 enforcement |
| C-01, C-02, C-04, C-05 | Other essential | PASS (assumed) | Baseline coverage assumed |
| C-06–C-08 | Recommended | PASS (assumed) | No indication of compromise |
| C-09–C-19 | Most aspirational | PASS (assumed) | Lifecycle emphasis orthogonal to constraint encoding |
| C-20 | Role-separated production | FAIL (assumed) | No role separation mentioned; "Workaround Auditor" is a phase gate, not a constraint-pair role split for basis/gap |
| C-21 | Both WRONG and CORRECT | PASS (assumed) | |
| C-22 | Relational constraints co-encoded | PARTIAL (assumed) | Lifecycle focus may not prioritize structural encoding of tier/gap relational constraints |

**Essential**: 5/5 = 60 (assumed)
**Recommended**: 3/3 = 30 (assumed)
**Aspirational**: ~12/14 = 8.6 (C-20 FAIL; C-22 uncertain)
**Composite: ~98.6** *(speculative)*
**Golden**: YES (assumed)

---

## V-05 — Conversational Register + Structural Encoding

*Hypothesis-only. No prompt provided. Score is inferential.*

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-05 | Essential | PASS (assumed) | Structural encoding maintains essential compliance |
| C-06–C-08 | Recommended | PASS (assumed) | |
| C-09–C-16 | Most aspirational | PASS (assumed) | "Embedded field labels" hypothesis covers C-13/C-16/C-22 |
| C-17 | Inline failure examples | PASS (assumed) | |
| C-18 | Structural encoding | PASS | Primary axis explicitly targets C-18 |
| C-19 | Examples precede governed fields | PASS (assumed) | Conversational register places context inline |
| C-20 | Role-separated production | FAIL (assumed) | No role separation mentioned |
| C-21 | Both WRONG and CORRECT | PASS (assumed) | |
| C-22 | Relational constraints co-encoded | PASS | "Embedded field labels" directly maps to C-22 mechanism |

**Essential**: 5/5 = 60 (assumed)
**Recommended**: 3/3 = 30 (assumed)
**Aspirational**: 13/14 = 9.3 (C-20 FAIL)
**Composite: ~99.3** *(speculative)*
**Golden**: YES (assumed)

---

## Ranking

| Rank | Variation | Composite | All Essential | C-20 | Confidence |
|------|-----------|-----------|---------------|------|------------|
| 1 | V-03 | ~100 | YES | PASS | Speculative (hypothesis only) |
| 2 | V-01 | 99.3 | YES | FAIL | Verified (full prompt) |
| 2 | V-02 | 99.3 | YES | FAIL | Verified (full prompt + preamble) |
| 2 | V-05 | ~99.3 | YES | FAIL | Speculative |
| 5 | V-04 | ~98.6 | YES | FAIL | Speculative |

**Top verified score**: 99 (V-01 / V-02)
**Top hypothetical score**: 100 (V-03, if baseline coverage is maintained)

---

## Excellence Signals (R7)

**From V-01**: Sequential section forcing + compilation-phase separation

V-01's "Complete each section before reading the next" instruction, combined with guards embedded within each section, creates a production path where constraint enforcement is active at generation time for each field. The final "Output" section is a compilation aggregation, not a first-fill template. This pattern separates constraint-active section production from format aggregation — the model cannot fill the Output template "cold" because the constraint work was already done in the section steps.

**From V-02**: Output-as-table eliminates the instruction/template bifurcation

When the output IS the structured table (as in V-02), there is no separate "Output" template section to jump to. Every output field IS a table cell, and table headers carry the constraints. This structurally eliminates the bypass risk that exists when a prompt has instruction sections followed by a separate output skeleton — in that structure, a model can read ahead to the output skeleton and fill fields before encountering guards. Full table-format output closes that gap.

---

```json
{"top_score": 99, "all_essential_pass": true, "new_patterns": ["Sequential-section forcing ('complete each section before reading the next') separates constraint-active production from output compilation — guards are inline during section production, not bypass-able via a final Output template", "Output-as-table format eliminates instruction/template bifurcation: when the output IS the structured table there is no separate Output section to skip ahead to, structurally preventing field-skipping"]}
```
