## program:plan — Round 9 Scoring (v9 rubric, 220 pts)

---

## Criterion-by-Criterion Evaluation

### V-01 — Single-axis: C-31

**Essential (all PASS)**
- **C-01**: YAML structurally complete: `program:` + `stages:` + `name:` + `skills:` per stage. **PASS**
- **C-02**: Echo pre-positioned with `auto: true` and `skills: []`. **PASS**
- **C-03**: BAD PLAN labels all bad skill names `# WRONG C-03`; template uses `""` placeholders only. **PASS**
- **C-04**: Template gate annotated `# artifact existence check — not a command`. **PASS**

**Recommended (all PASS)**
- **C-05**: Zone-header `# requires: [artifact(s)] from prior stage` reminders present at dep zones. **PASS**
- **C-06**: Stage-name placeholders annotated `# evidence-intent label`; rules explicitly state evidence goal framing. **PASS**
- **C-07**: Opening: "A program plan is a plan — not an executor." **PASS**

**Aspirational**

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-08 | **FAIL** | No quantified thresholds in any gate example |
| C-09 | **PASS** | Four-stage + echo sequence with explicit dep chain reflects discovery→shape→challenge→validate arc |
| C-10 | **PASS** | BAD PLAN shows C-04 execution gates vs correction table correct forms |
| C-11 | **PASS** | Echo pre-positioned; gate annotated as artifact check, not command |
| C-12 | **PASS** | BAD PLAN provides second anchor for C-01/C-02/C-03/C-04 alongside structural template |
| C-13 | **PARTIAL** | No zone-level section headers in template; arc implied by dep comments but not enforced as structure |
| C-14 | **PARTIAL** | `# final stage — always echo, no skills listed` is descriptive but lacks `# DO NOT REMOVE`-style prohibition |
| C-15 | **PASS** | Complete multi-stage BAD PLAN YAML block present |
| C-16 | **PASS** | BAD PLAN carries `# WRONG C-01` through `# WRONG C-07` tags |
| C-17 | **FAIL** | No per-zone gate contrast pairs in template (no gate_fail/gate_pass fields) |
| C-18 | **PASS** | Correction table with ≥10 wrong-to-correct pairs |
| C-19 | **PASS** | BAD PLAN tags C-05 (`review:design before draft:spec`) and C-06 (namespace label) and C-07 (executor framing) |
| C-20 | **PASS** | `# requires: [artifact(s)] from prior stage` at zone-header position in all dep zones |
| C-21 | **PARTIAL** | `# check correction table: skill names` at skills fields; gate field says `# artifact existence check` but not `# check correction table: gate values` — bridge absent at gate field |
| C-22 | **PASS** | BAD PLAN explicitly tags C-05, C-06, C-07 |
| C-23 | **FAIL** | Dep reminders only at zone-header comment; `skills:` placeholder carries no dep reminder |
| C-24 | **FAIL** | No gate_fail/gate_pass YAML template fields |
| C-25 | **FAIL** | No `Why:` rationale at contrast pairs |
| C-26 | **FAIL** | No structural gate_fail fields at all |
| C-27 | **FAIL** | C-23 prerequisite fails |
| C-28 | **FAIL** | No three-field gate structure |
| C-29 | **FAIL** | Correction table has essential-tier only (no C-05/C-06/C-07 pairs) |
| C-30 | **FAIL** | C-23 prerequisite fails |
| C-31 | **PASS** | BAD PLAN block tags all 7 criteria: C-01 (empty skills), C-02 (missing echo), C-03 (draft:brief), C-04 (execution gate), C-05 (review:design before draft:spec), C-06 (namespace label×2), C-07 (executor framing×2). C-15 prerequisite passes. |
| C-32 | **FAIL** | No three-field gate structure (C-28 prerequisite fails) |
| C-33 | **FAIL** | Multiple prerequisites fail |

**V-01 Score:**
- Essential: 4/4 × 60 = **60 pts**
- Recommended: 3/3 × 30 = **30 pts**
- Aspirational: 11 PASS × 5 + 3 PARTIAL × 2.5 = 55 + 7.5 = **62.5 pts**
- **Composite: 152.5 / 220** ✓ Golden

---

### V-02 — Single-axis: C-32

**Essential (all PASS)**
- **C-01**: Structurally valid. **PASS**
- **C-02**: Echo present with `auto: true` and `skills: []`. **PASS**
- **C-03**: Invented skills labeled WRONG C-03 in BAD PLAN; template uses placeholders. **PASS**
- **C-04**: Three-field structure + correction bridge guide gate authoring. **PASS**

**Recommended (all PASS)**
- **C-05**: `# requires: [artifact] from prior stage` at dep zone headers. **PASS**
- **C-06**: Stage-name placeholders with `# evidence-intent stage label`. **PASS**
- **C-07**: "You're building a plan, not a runner." **PASS**

**Aspirational**

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-08 | **FAIL** | No quantified gate thresholds |
| C-09 | **PASS** | Four-stage arc with dep chain |
| C-10 | **PASS** | BAD PLAN shows execution gates for C-04 |
| C-11 | **PASS** | Three-field gate structure structurally enforces gate correctness |
| C-12 | **PASS** | BAD PLAN + template provide dual anchors for C-01/C-02/C-03/C-04 |
| C-13 | **PARTIAL** | No zone-level section headers |
| C-14 | **FAIL** | Echo carries no annotation at its slot |
| C-15 | **PASS** | Complete BAD PLAN block |
| C-16 | **PASS** | BAD PLAN tags C-01, C-02, C-03, C-04, C-07 |
| C-17 | **PASS** | gate_fail + gate_pass at every non-echo zone (4 zones) |
| C-18 | **PASS** | Correction table with ≥10 pairs |
| C-19 | **PASS** | BAD PLAN tags C-07 (`# WRONG C-04: execution gate / WRONG C-07: executor framing`) |
| C-20 | **PASS** | `# requires:` at dep zone headers |
| C-21 | **PASS** | `# check correction table: skill names` at skills; `# check correction table: gate values` at gate field |
| C-22 | **FAIL** | Only C-07 tagged; C-05 and C-06 absent from all artifacts |
| C-23 | **FAIL** | `skills:` line has `# check correction table: skill names` only — no dep reminder at skills position |
| C-24 | **PASS** | gate_fail and gate_pass as actual YAML template keys at all 4 zones |
| C-25 | **FAIL** | `# contrast only — WRONG: execution gate` lacks `Why:` rationale |
| C-26 | **FAIL** | gate_fail fields say `# contrast only — WRONG: execution gate` — no `C-XX` criterion reference |
| C-27 | **FAIL** | C-23 prerequisite fails |
| C-28 | **PASS** | gate_fail/gate_pass/gate three-field structure at all 4 non-echo zones. C-24 prerequisite passes. |
| C-29 | **FAIL** | Correction table has essential-tier only |
| C-30 | **FAIL** | C-23 prerequisite fails |
| C-31 | **FAIL** | BAD PLAN missing C-05 and C-06 tags |
| C-32 | **PASS** | `gate: ""  # check correction table: gate values` at all 4 non-echo zones. C-18 and C-28 both pass. |
| C-33 | **FAIL** | C-26, C-27, C-30 prerequisites fail |

**V-02 Score:**
- Essential: 60 pts
- Recommended: 30 pts
- Aspirational: 14 PASS × 5 + 1 PARTIAL × 2.5 = 70 + 2.5 = **72.5 pts**
- **Composite: 162.5 / 220** ✓ Golden

---

### V-03 — Single-axis: C-33

**Essential (all PASS)** — all four pass; BAD PLAN labels C-01/C-02/C-03/C-04.

**Recommended (all PASS)** — dep reminders, intent-label placeholders, planner framing present.

**Aspirational**

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-08 | **FAIL** | No quantified thresholds |
| C-09 | **PASS** | Evidence arc visible through Zone 1–4 structure |
| C-10 | **PASS** | BAD PLAN shows essential-criterion contrast pairs |
| C-11 | **PASS** | Three-field structure + echo pre-positioned |
| C-12 | **PASS** | BAD PLAN + template dual anchors for C-01/C-02/C-03/C-04 |
| C-13 | **PASS** | `# Zone 1: Discovery`, `# Zone 2: Shape`, `# Zone 3: Challenge`, `# Zone 4: Validate`, `# Zone 5: Echo` as embedded zone-delimiter comments in YAML skeleton — arc navigable from structure alone |
| C-14 | **PARTIAL** | `# Zone 5: Echo — always last` zone comment is descriptive label, not prohibition annotation |
| C-15 | **PASS** | Complete BAD PLAN block |
| C-16 | **PASS** | BAD PLAN tags C-01/C-02/C-03/C-04 |
| C-17 | **PASS** | gate_fail/gate_pass at every zone |
| C-18 | **PASS** | Correction table with ≥9 pairs |
| C-19 | **FAIL** | BAD PLAN covers essential tier only; correction table has no C-05/C-06/C-07 entries; dep reminder `(C-05)` tags are prerequisite annotations, not error artifacts |
| C-20 | **PASS** | `# requires:` reminders at skills-line position in Zones 2–4 |
| C-21 | **PASS** | `# check correction table: skill names` at skills fields; `# check correction table: gate values` at all gate fields including Zone 1 |
| C-22 | **FAIL** | No recommended-tier error coverage in any artifact |
| C-23 | **PASS** | Zone-header comment `# requires: [X] from Zone: Y (C-05)` AND skills-line `# requires: [X] from Zone: Y (C-05)` at Zones 2/3/4 |
| C-24 | **PASS** | gate_fail/gate_pass as YAML template keys at all zones |
| C-25 | **FAIL** | No `Why:` rationale |
| C-26 | **PASS** | Zone 1 gate_fail: `# WRONG C-04`; Zones 2–4 gate_fail: `# WRONG C-07` — all carry specific `C-XX` criterion reference |
| C-27 | **PASS** | Uniform syntax `# requires: [X artifact] from Zone: Y (C-05)` used consistently across all dep zones and both positions |
| C-28 | **PASS** | gate_fail/gate_pass/gate three-field structure at all 4 non-echo zones |
| C-29 | **FAIL** | Correction table covers essential tier only |
| C-30 | **PASS** | Zones 2–4 skills line: `# requires: [X] from Zone: Y (C-05)` AND `# check correction table: skill names` coexist independently. C-21 and C-23 prerequisites pass. |
| C-31 | **FAIL** | BAD PLAN missing C-05/C-06/C-07 tags (by design; essential-only to isolate C-33 axis) |
| C-32 | **PASS** | `gate: ""  # check correction table: gate values` at all 4 non-echo zones including Zone 1 |
| C-33 | **PASS** | Zones 2–4 each carry all four mechanisms: (a) gate_fail with `# WRONG C-07` + gate_pass + gate (C-28+C-26), (b) `gate:` with correction bridge (C-32), (c) dual dep reminders in uniform syntax at zone-header AND skills line (C-27), (d) dep reminder + correction bridge independently at skills line (C-30). All five prerequisite criteria pass. |

**V-03 Score:**
- Essential: 60 pts
- Recommended: 30 pts
- Aspirational: 19 PASS × 5 + 1 PARTIAL × 2.5 = 95 + 2.5 = **97.5 pts**
- **Composite: 187.5 / 220** ✓ Golden

---

### V-04 — Combination: C-31 + C-32

**Essential (all PASS)** — all four pass.

**Recommended (all PASS)** — dep zone headers, intent labels, plan framing.

**Aspirational**

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-08 | **FAIL** | No quantified thresholds |
| C-09 | **PASS** | Four-phase arc with explicit dep chain |
| C-10 | **PASS** | BAD PLAN shows essential-criterion contrast pairs |
| C-11 | **PASS** | Three-field structure + pre-positioned echo |
| C-12 | **PASS** | BAD PLAN + template dual anchors for all four essential criteria |
| C-13 | **PASS** | `# Phase 1: Discovery` through `# Phase 5: Echo` as zone-delimiter comments in YAML skeleton |
| C-14 | **PARTIAL** | `# Phase 5: Echo — always last` is descriptive, not prohibition annotation |
| C-15 | **PASS** | Complete BAD PLAN block |
| C-16 | **PASS** | BAD PLAN carries C-01/C-02/C-03/C-04/C-05/C-06/C-07 tags |
| C-17 | **PASS** | gate_fail/gate_pass at every non-echo zone |
| C-18 | **PASS** | Correction table with 11 pairs |
| C-19 | **PASS** | BAD PLAN tags C-05 (`# WRONG C-05`), C-06 (`# WRONG C-06`), C-07 (`# WRONG C-07`) |
| C-20 | **PASS** | `# requires: [artifact] from Phase N` at dep zone headers |
| C-21 | **PASS** | `# check correction table: skill names` at skills; `# check correction table: gate values` at gate fields |
| C-22 | **PASS** | BAD PLAN explicitly tags C-05, C-06, C-07 |
| C-23 | **FAIL** | `skills:` placeholder carries only `# check correction table: skill names` — no dep reminder at skills position |
| C-24 | **PASS** | gate_fail/gate_pass as YAML template keys at all zones |
| C-25 | **FAIL** | No `Why:` rationale |
| C-26 | **FAIL** | gate_fail fields carry `# contrast only — WRONG: execution gate` / `# contrast only — WRONG: executor framing` — no `C-XX` criterion number |
| C-27 | **FAIL** | C-23 prerequisite fails |
| C-28 | **PASS** | Three-field gate structure at all 4 non-echo phases |
| C-29 | **FAIL** | Correction table has essential-tier only (no C-05/C-06/C-07 table pairs) |
| C-30 | **FAIL** | C-23 prerequisite fails |
| C-31 | **PASS** | BAD PLAN tags all 7 criteria: C-01 (empty skills), C-02 (missing echo), C-03 (draft:brief), C-04/C-07 (execution gate + executor framing), C-05 (review:design before draft:spec), C-06 (namespace label×2). C-15 passes. |
| C-32 | **PASS** | `gate: ""  # check correction table: gate values` at all 4 non-echo phases. C-18 and C-28 pass. |
| C-33 | **FAIL** | C-26, C-27, C-30 prerequisites fail |

**V-04 Score:**
- Essential: 60 pts
- Recommended: 30 pts
- Aspirational: 17 PASS × 5 + 1 PARTIAL × 2.5 = 85 + 2.5 = **87.5 pts**
- **Composite: 177.5 / 220** ✓ Golden

---

### V-05 — Golden Synthesis: C-31 + C-32 + C-33 + C-29

**Essential (all PASS)** — all four pass.

**Recommended (all PASS)** — all three pass.

**Aspirational**

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-08 | **FAIL** | No quantified thresholds in gate examples |
| C-09 | **PASS** | Four-zone + echo sequence reflects deliberate evidence arc |
| C-10 | **PASS** | BAD PLAN shows essential-criterion contrast pairs |
| C-11 | **PASS** | Three-field gate structure + echo pre-positioned |
| C-12 | **PASS** | BAD PLAN + template dual anchors for all four essential criteria |
| C-13 | **PASS** | `# Zone 1: Discovery` through `# Zone 5: Echo` zone-delimiter comments in YAML skeleton — arc navigable from structure |
| C-14 | **PARTIAL** | `# Zone 5: Echo — always last` is descriptive label; no explicit `# REQUIRED: DO NOT REMOVE` prohibition |
| C-15 | **PASS** | Complete BAD PLAN block present |
| C-16 | **PASS** | BAD PLAN carries C-01 through C-07 criterion tags |
| C-17 | **PASS** | gate_fail/gate_pass at all 4 non-echo zones |
| C-18 | **PASS** | Correction table with 15 wrong-to-correct pairs |
| C-19 | **PASS** | BAD PLAN + correction table both tag C-05/C-06/C-07 |
| C-20 | **PASS** | Dep reminders at skills positions in Zones 2–4 |
| C-21 | **PASS** | `# check correction table: skill names` at skills; `# check correction table: gate values` at gate fields at all zones |
| C-22 | **PASS** | BAD PLAN explicitly tags C-05/C-06/C-07; correction table also carries C-05/C-06/C-07 pairs |
| C-23 | **PASS** | Zones 2–4 carry dep reminder at both zone-header comment position AND `skills:` placeholder line — `# requires: [X] from Zone: Y (C-05)` at both positions |
| C-24 | **PASS** | gate_fail/gate_pass as YAML template keys at all zones |
| C-25 | **FAIL** | No explicit `Why:` rationale alongside gate contrast pairs |
| C-26 | **PASS** | Zone 1 gate_fail: `# WRONG C-04`; Zones 2–4 gate_fail: `# WRONG C-07` — all carry `C-XX` criterion reference at the structural field position |
| C-27 | **PASS** | Uniform syntax `# requires: [X artifact] from Zone: Y (C-05)` across all dep zones and both positions |
| C-28 | **PASS** | gate_fail/gate_pass/gate three-field structure at all 4 non-echo zones |
| C-29 | **PASS** | Correction table includes C-05 (`review:design before draft:spec → draft:spec must precede review:design`), C-06 (`name: "scout-phase" → "Surface signals"`, `name: "draft-phase" → "Shape the concept"`), C-07 (`gate: "execute..." → "[artifact] present — plan identity"`). All three recommended criteria covered. |
| C-30 | **PASS** | Zones 2–4 skills line carries dep reminder `# requires: [X] from Zone: Y (C-05)` AND correction bridge `# check correction table: skill names` independently. C-21 and C-23 prerequisites pass. |
| C-31 | **PASS** | BAD PLAN block tags all 7 criteria: C-01 (empty skills), C-02 (no echo), C-03 (draft:brief), C-04 (execution gate), C-05 (review:design before draft:spec), C-06 (namespace label×2), C-07 (executor framing×2+gate). C-15 passes. |
| C-32 | **PASS** | `gate: ""  # check correction table: gate values` at all 4 non-echo zones including Zone 1. C-18 and C-28 pass. |
| C-33 | **PASS** | Zones 2–4 each carry full four-mechanism coexistence: (a) three-field gate + criterion-tagged gate_fail (`# WRONG C-07`) (C-28+C-26); (b) production gate with correction bridge (C-32); (c) dual dep reminders in uniform syntax at zone-header and skills line (C-27); (d) independent dep reminder + correction bridge at skills line (C-30). All five prerequisite criteria pass. |

**V-05 Score:**
- Essential: 60 pts
- Recommended: 30 pts
- Aspirational: 23 PASS × 5 + 1 PARTIAL × 2.5 = 115 + 2.5 = **117.5 pts**
- **Composite: 207.5 / 220** ✓ Golden

---

## Composite Score Summary

| Rank | Variate | Essential | Recommended | Aspirational | **Composite** | Golden |
|------|---------|-----------|-------------|--------------|---------------|--------|
| 1 | V-05 (C-31+C-32+C-33+C-29) | 60 | 30 | 117.5 | **207.5** | ✓ |
| 2 | V-03 (C-33 single-axis) | 60 | 30 | 97.5 | **187.5** | ✓ |
| 3 | V-04 (C-31+C-32 combo) | 60 | 30 | 87.5 | **177.5** | ✓ |
| 4 | V-02 (C-32 single-axis) | 60 | 30 | 72.5 | **162.5** | ✓ |
| 5 | V-01 (C-31 single-axis) | 60 | 30 | 62.5 | **152.5** | ✓ |

---

## Hypotheses Verified

| Hypothesis | Outcome |
|------------|---------|
| V-01: C-31 passes in isolation | ✓ CONFIRMED |
| V-02: C-32 + C-28 + C-18 pass; C-33 absent | ✓ CONFIRMED |
| V-03: C-33 + 5 prerequisites pass; +6 aspirational delta | ✓ CONFIRMED (18 aspirational PASS vs 11 in V-01) |
| V-04: C-31 and C-32 are additive; C-33 absent confirms non-requirement for zone-density | ✓ CONFIRMED |
| V-05: All three new criteria mutually compatible; near-maximum composite | ✓ CONFIRMED (207.5 — only C-08 and C-25 remain) |

---

## Excellence Signals from V-05

**1. Dual-format cross-tier alignment (C-31 × C-29)**
V-05 is the first variate to align both primary reference artifacts — the illustrative BAD PLAN block (C-31) and the tabular correction table (C-29) — on the full 7-criterion spectrum. This produces dual-format coverage: a model encountering C-05/C-06/C-07 errors can find them illustrated in a concrete wrong-plan *and* listed as scannable lookup pairs. Neither format alone achieves this; the combination enables C-22 (full recommended-tier error annotation) from two independent artifact types.

**2. C-31 + C-32 + C-33 are additively stackable without structural collision**
Each new R9 criterion operates on an orthogonal document section: C-31 upgrades the BAD PLAN block; C-32 adds a pointer at the production `gate:` field inside the three-field structure; C-33 stacks additional zone-local mechanisms at dep-bearing zones. None interferes with the others. V-04 demonstrated C-31+C-32 coexistence; V-05 confirmed C-33 absorbs both without displacing any existing mechanism.

**3. Zone 1 (non-dep) benefits from full gate teaching density**
V-05 applies the three-field gate structure with criterion-tagged `gate_fail:` and production-gate correction bridge to Zone 1 (Discovery) even though Zone 1 has no upstream dependencies. Zone 1 carries `# WRONG C-04` at its gate_fail field (not C-07, which applies only to dep zones). This ensures gate teaching density is uniform across ALL non-echo zones, not just dep-bearing ones — C-32 and C-26 pass at Zone 1 for the right criterion (execution gate = C-04).

---

## Remaining Gap

Only **C-08** (quantified gate thresholds) and **C-25** (gate contrast rationale `Why:` annotations) remain unachieved. C-14 (deletion-resistance at echo) remains PARTIAL across all variates — the zone comment `# Zone N: Echo — always last` is descriptive but lacks explicit prohibition language (`# DO NOT add skills. DO NOT move before other stages.`).

---

```json
{"top_score": 207, "all_essential_pass": true, "new_patterns": ["Complete BAD PLAN criterion index (C-31) combined with full-spectrum correction table (C-29) aligns both illustrative and lookup artifacts on all 7 criteria — each format independently teaches the full criterion set, enabling C-22 to be satisfied across two artifact types simultaneously", "C-31, C-32, and C-33 are additively stackable without structural collision — BAD PLAN block upgrade, production gate field bridge, and zone annotation density stack each operate on orthogonal document sections and can be combined without displacement"]}
```
