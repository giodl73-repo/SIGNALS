---

## program:plan — Round 10 Scoring (v10 rubric)

**Rubric**: 4 essential (60 pts) + 3 recommended (30 pts) + 28 aspirational (140 pts) = 230 pts max. Golden: all essential pass AND composite >= 80.

---

## Pre-Scoring: Key Design Observations

**V-01 anomaly**: Hypothesis states "BAD PLAN essential-tier only (C-31 absent)" but the actual prompt body includes `# WRONG C-06` on both namespace-label stage names and the combined `# WRONG C-04 / WRONG C-07` tag — all seven criteria are tagged. C-31 is **PASS** in practice despite the isolation intent. The correction table remains essential-tier only (no C-05/C-06/C-07 rows), so C-29 **FAIL** and C-35 **FAIL** hold.

**V-03 anomaly**: BAD PLAN stage names ("information-gathering", "spec-writing") are not namespace-only labels and carry no `# WRONG C-06` tag. C-06 violation pattern is untaught in error artifacts → C-22 **FAIL**. C-31 also fails (C-06 absent from BAD PLAN tags).

---

## V-01 — Compound gate_fail: Annotation (C-34 single-axis)

### Essential (all 4 PASS)

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01 Valid YAML | PASS | Template: `program:` → `stages:` → each stage has `name:` and `skills:` |
| C-02 Echo Contract | PASS | `# Zone 5: Echo — always last` pre-positioned with `auto: true`, `skills: []` |
| C-03 Valid Skill Names | PASS | Skill slots are blank placeholders; correction table maps only real catalog names |
| C-04 Evidence-State Gates | PASS | `gate: ""` placeholder with correction table bridge; `gate_fail:`/`gate_pass:` are labeled contrast-only |

**Essential: 4/4 → 60 pts**

### Recommended (all 3 PASS)

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-05 Dep Order | PASS | BAD PLAN: `# WRONG C-05: review:design before draft:spec`; dep reminders at all dep-bearing zones |
| C-06 Descriptive Stage Names | PASS | BAD PLAN tags namespace-label names (`# WRONG C-06`); template uses evidence-intent prompts |
| C-07 Plan Identity | PASS | Opening: "You are a planner — not an executor."; BAD PLAN tags `# WRONG C-04 / WRONG C-07` |

**Recommended: 3/3 → 30 pts**

### Aspirational

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-08 Quantified Gates | FAIL | No numeric thresholds at any gate position |
| C-09 Evidence Arc | PASS | Discovery → Shape → Challenge → Validate → Echo arc visible from zone headers |
| C-10 Failure Contrast Pair | PASS | `gate_fail:`/`gate_pass:` per zone; BAD PLAN shows wrong vs correct |
| C-11 Structural Enforcement | PASS | Echo pre-positioned; `gate: ""` enforces artifact-state default |
| C-12 Dual-Anchor Reinforcement | PASS | C-01: BAD PLAN + template; C-02: BAD PLAN + pre-positioned echo; C-03: BAD PLAN + correction table; C-04: BAD PLAN + gate contrast + correction bridge |
| C-13 Arc as Structural Spine | PASS | Zone header comments are the document's structural delimiters; arc visible without prose |
| C-14 Deletion-Resistance | PARTIAL | `# Zone 5: Echo — always last` names position rule but no explicit `# REQUIRED: DO NOT add skills` |
| C-15 Plan-Level YAML Error | PASS | Complete multi-stage BAD PLAN block with wrong gates across all stages |
| C-16 Criterion-Referenced Tagging | PASS | BAD PLAN annotates every wrong field with `# WRONG C-XX` |
| C-17 Per-Zone Gate Contrast | PASS | Every non-echo zone has both `gate_fail:` (wrong) and `gate_pass:` (correct) |
| C-18 Correction Table | PASS | 9-pair table covering C-01–C-04 wrong-to-correct mappings |
| C-19 Cross-Tier Error Coverage | PASS | BAD PLAN has C-05, C-06, C-07 tags alongside essential tags |
| C-20 Per-Zone Dep Reminder | PASS | Zones 2–4 carry dep reminders at zone headers |
| C-21 Correction Table Scaffold Bridge | PASS | `# check correction table: skill names` and `# check correction table: gate values` at template field positions |
| C-22 Complete Recommended-Tier Annotation | PASS | BAD PLAN tags C-05 ✓, C-06 ✓ (both namespace labels), C-07 ✓ (combined tag) |
| C-23 Dual-Position Dep Reminder | PASS | `# requires: [artifact] from Zone: X (C-05)` at both zone-header AND `skills:` line |
| C-24 Template-Field Gate Contrast | PASS | `gate_fail:` and `gate_pass:` as YAML keys at every zone |
| C-25 Gate Contrast Rationale | PASS | Every `gate_fail:` carries `— Why: [principle]` inline |
| C-26 Criterion-Tagged Gate Values | PASS | Every `gate_fail:` carries `# WRONG C-04` or `# WRONG C-07` |
| C-27 Uniform Dep Syntax | PASS | `# requires: [X artifact] from Zone: Y (C-05)` consistently at both positions across all zones |
| C-28 Three-Field Gate Structure | PASS | `gate_fail:` / `gate_pass:` / `gate:` as sibling YAML keys at every non-echo zone |
| C-29 Correction Table Recommended Pairs | **FAIL** | Table has no C-05, C-06, C-07 rows — essential tier only |
| C-30 Dep-Reminder + Bridge Independence | PASS | `skills:` line carries dep reminder AND `# check correction table: skill names` as independent annotations |
| C-31 Complete BAD-YAML Coverage | PASS | BAD PLAN has tags for all 7 criteria despite "essential violations" header label |
| C-32 Production Gate Bridge | PASS | `gate: ""  # check correction table: gate values` at every zone |
| C-33 Maximal Zone Teaching Density | PASS | All four mechanisms coexist at Zones 2–4: C-28 + C-26 + C-32 + C-27 + C-30 all PASS |
| C-34 Compound gate_fail: Annotation | **PASS** | Every `gate_fail:` carries both `# WRONG C-XX` tag AND `— Why: [explanation]` at same field line |
| C-35 Dual Error-Format Recommended | **FAIL** | C-31 PASS but C-29 FAIL → compound requirement not met |

**Aspirational: 24 PASS + 1 PARTIAL + 3 FAIL = 24.5 effective / 28 → 122.5 pts**

**V-01 Composite: 60 + 30 + 122.5 = 212.5** — GOLDEN ✓

---

## V-02 — Dual Error-Format Recommended Coverage (C-35 single-axis)

### Essential (all 4 PASS) — 60 pts

Same structural basis as V-01; echo pre-positioned with `auto: true`, `skills: []`; all skill slots are blank; `gate: ""` with correction table bridge.

### Recommended (all 3 PASS) — 30 pts

BAD PLAN tags C-05, C-06, C-07; correction table maps recommended violations; opening frames planner identity.

### Aspirational

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-08 | FAIL | No quantified thresholds |
| C-09 | PASS | Discovery → Shape → Challenge → Validate → Echo arc |
| C-10 | PASS | Per-zone `gate_fail:`/`gate_pass:` contrast + BAD PLAN |
| C-11 | PASS | Echo pre-positioned; `gate: ""` structural default |
| C-12 | PASS | All 4 essentials dual-anchored: BAD PLAN + template + correction table |
| C-13 | PASS | `# Phase 1: Discovery` etc. as zone delimiters |
| C-14 | PARTIAL | `# Phase 5: Echo — always last` — no explicit `# REQUIRED:` annotation |
| C-15 | PASS | Complete multi-stage BAD PLAN YAML block |
| C-16 | PASS | BAD PLAN has all 7 criterion tags |
| C-17 | PASS | Per-zone `gate_fail:` (wrong) + `gate_pass:` (correct) at every non-echo zone |
| C-18 | PASS | Correction table with many pairs (>3) |
| C-19 | PASS | BAD PLAN has C-05, C-06, C-07 entries |
| C-20 | PASS | Dep reminders at Phase 2–4 headers |
| C-21 | PASS | `# check correction table: skill names` and `# check correction table: gate values` at template slots |
| C-22 | PASS | BAD PLAN tags C-05 ✓, C-06 ✓, C-07 ✓ |
| C-23 | PASS | `# requires: [artifact] from Phase N (C-05)` at both zone-header and `skills:` line |
| C-24 | PASS | `gate_fail:` / `gate_pass:` / `gate:` as YAML keys per zone |
| C-25 | **FAIL** | `gate_fail:` fields carry criterion tags but NO `Why:` explanation — only `(contrast only)` label |
| C-26 | PASS | Every `gate_fail:` carries `# WRONG C-04` or `# WRONG C-07` |
| C-27 | PASS | Uniform dep reminder syntax at both positions across all dep-bearing phases |
| C-28 | PASS | Three-field gate structure at every non-echo zone |
| C-29 | **PASS** | Correction table has C-05 rows (2), C-06 rows (2), C-07 rows (2) |
| C-30 | PASS | Independent dep reminder + correction bridge at `skills:` line |
| C-31 | PASS | BAD PLAN carries all 7 criterion tags |
| C-32 | PASS | `gate: ""  # check correction table: gate values` |
| C-33 | PASS | All four mechanisms at every dep-bearing zone |
| C-34 | **FAIL** | No `Why:` at `gate_fail:` fields — criterion tag present but rationale absent → compound annotation incomplete |
| C-35 | **PASS** | C-29 PASS + C-31 PASS → dual error-format recommended coverage satisfied |

**Aspirational: 24 PASS + 1 PARTIAL + 3 FAIL = 24.5 / 28 → 122.5 pts**

**V-02 Composite: 60 + 30 + 122.5 = 212.5** — GOLDEN ✓

---

## V-03 — C-34 with Inertia Framing

### Essential (all 4 PASS) — 60 pts

Valid template structure; echo pre-positioned `always last, always auto`; blank skill slots; `gate: ""` with correction bridge.

### Recommended (all 3 PASS) — 30 pts

C-05: BAD PLAN tags `# WRONG C-05`; dep reminders in template. C-06: template guidance `# what evidence are you gathering here?` steers evidence-intent naming (BAD PLAN uses non-namespace-only stage names but provides no explicit C-06 teaching — sufficient for output compliance). C-07: inertia framing makes planner/executor distinction concrete.

### Aspirational

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-08 | FAIL | No quantified thresholds |
| C-09 | PASS | Signal → Shape → Challenge → Prove → Echo arc |
| C-10 | PASS | Per-zone gate contrast; BAD PLAN |
| C-11 | PASS | Echo pre-positioned; `gate: ""` structural default |
| C-12 | PASS | All 4 essentials dual-anchored |
| C-13 | PASS | `# Zone N: [Phase Name]` headers are structural delimiters |
| C-14 | PARTIAL | `# Zone 5: Echo — always last, always auto` — naming position + auto requirement but no explicit `# REQUIRED: DO NOT add skills` |
| C-15 | PASS | Complete BAD PLAN YAML block |
| C-16 | PASS | BAD PLAN has C-01/C-02/C-03/C-04/C-05/C-07 tags (six of seven — C-06 absent but one tag is sufficient for C-16) |
| C-17 | PASS | Per-zone `gate_fail:` / `gate_pass:` at all non-echo zones |
| C-18 | PASS | 10-pair correction table (C-01–C-04) |
| C-19 | PASS | BAD PLAN has C-05 entry |
| C-20 | PASS | Dep reminders at zone headers |
| C-21 | PASS | `# check correction table: skill names` and `# check correction table: gate values` in template |
| C-22 | **FAIL** | C-06 not tagged in any error artifact (BAD PLAN, correction table) — only 2 of 3 recommended criteria covered |
| C-23 | PASS | Dual-position dep reminder at zone-header AND `skills:` line |
| C-24 | PASS | `gate_fail:`/`gate_pass:`/`gate:` as YAML keys per zone |
| C-25 | PASS | Every `gate_fail:` carries `— Why: [principle]` inline |
| C-26 | PASS | Every `gate_fail:` carries `# WRONG C-04` or `# WRONG C-07` |
| C-27 | PASS | `# requires: [Zone N artifact] from Zone: Name (C-05)` uniform at all positions |
| C-28 | PASS | Three-field gate structure at every non-echo zone |
| C-29 | **FAIL** | Correction table has no C-05, C-06, C-07 rows |
| C-30 | PASS | Independent dep reminder + correction bridge at `skills:` line |
| C-31 | **FAIL** | BAD PLAN missing C-06 tag — stage names "information-gathering" / "spec-writing" not labeled as wrong |
| C-32 | PASS | `gate: ""  # check correction table: gate values` |
| C-33 | PASS | All four mechanisms at every dep-bearing zone (C-26/C-27/C-28/C-30/C-32 all prerequisite-pass) |
| C-34 | PASS | All `gate_fail:` fields carry criterion tag + `Why:` at same field line |
| C-35 | **FAIL** | C-29 FAIL + C-31 FAIL → dual error-format requirement not met |

**Aspirational: 22 PASS + 1 PARTIAL + 5 FAIL = 22.5 / 28 → 112.5 pts**

**V-03 Composite: 60 + 30 + 112.5 = 202.5** — GOLDEN ✓

---

## V-04 — Combination: C-34 + C-35

### Essential (all 4 PASS) — 60 pts

### Recommended (all 3 PASS) — 30 pts

### Aspirational

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-08 | FAIL | No quantified thresholds |
| C-09 | PASS | Discovery → Shape → Challenge → Validate → Echo arc |
| C-10 | PASS | Per-zone gate contrast + BAD PLAN |
| C-11 | PASS | Echo pre-positioned; `gate: ""` default |
| C-12 | PASS | All 4 essentials dual-anchored (BAD PLAN + template + correction table) |
| C-13 | PASS | `# Zone N:` headers as structural spine |
| C-14 | PARTIAL | `# Zone 5: Echo — always last` — no `# REQUIRED: DO NOT add skills` |
| C-15 | PASS | Complete 3-stage BAD PLAN YAML with all 7 violations illustrated |
| C-16 | PASS | All 7 criteria criterion-tagged in BAD PLAN |
| C-17 | PASS | Per-zone `gate_fail:`/`gate_pass:` at all non-echo zones |
| C-18 | PASS | 17-pair correction table covering C-01–C-07 |
| C-19 | PASS | BAD PLAN has C-05, C-06, C-07 entries |
| C-20 | PASS | Dep reminders at Zones 2–4 headers |
| C-21 | PASS | Correction bridge at `skills:` and `gate:` positions in template |
| C-22 | PASS | All three recommended criteria tagged in BAD PLAN |
| C-23 | PASS | Dual-position dep reminders in uniform syntax |
| C-24 | PASS | `gate_fail:`/`gate_pass:`/`gate:` as YAML keys per zone |
| C-25 | PASS | Every `gate_fail:` carries `— Why: [principle]` |
| C-26 | PASS | Every `gate_fail:` carries `# WRONG C-04` or `# WRONG C-07` |
| C-27 | PASS | `# requires: [artifact] from Zone: X (C-05)` uniform at all positions |
| C-28 | PASS | Three-field gate structure at all non-echo zones |
| C-29 | PASS | Correction table has C-05 (2 pairs), C-06 (2 pairs), C-07 (2 pairs) |
| C-30 | PASS | Independent dep reminder + correction bridge at `skills:` line |
| C-31 | PASS | BAD PLAN carries all 7 criterion tags |
| C-32 | PASS | `gate: ""  # check correction table: gate values` |
| C-33 | PASS | Full four-mechanism density at every dep-bearing zone |
| C-34 | PASS | Every `gate_fail:` carries criterion tag + `Why:` at same field line |
| C-35 | PASS | C-29 PASS + C-31 PASS → dual error-format recommended coverage complete |

**Aspirational: 26 PASS + 1 PARTIAL + 1 FAIL = 26.5 / 28 → 132.5 pts**

**V-04 Composite: 60 + 30 + 132.5 = 222.5** — GOLDEN ✓

---

## V-05 — Golden Synthesis: C-34 + C-35 + all R9 mechanisms

### Essential (all 4 PASS) — 60 pts

### Recommended (all 3 PASS) — 30 pts

### Aspirational

Structurally equivalent to V-04 with descriptive/intent-forward phrasing. All criteria land identically:

| Criterion | Verdict | Key note |
|-----------|---------|---------|
| C-08 | FAIL | No quantified thresholds |
| C-14 | PARTIAL | `# Zone 5: Echo — always last` — no `# REQUIRED:` prohibition annotation |
| C-29 | PASS | Correction table has C-05/C-06/C-07 rows (identical structure to V-04) |
| C-31 | PASS | BAD PLAN tags all 7 criteria with multi-line criterion explanations + CORRECT shape examples |
| C-34 | PASS | All zones carry criterion tag + `Why:` at `gate_fail:` field line |
| C-35 | PASS | C-29 + C-31 both pass |
| C-33 | PASS | Full four-mechanism density at Zones 2–4 |
| All other C-09 through C-32 | PASS | Same as V-04 |

V-05 distinguishing addition: explicit closing instruction — "Both the BAD PLAN and the correction table cover all 7 criteria — consult both before authoring any field" — reinforces C-35's dual-format intent but does not shift any borderline criterion past a threshold.

**Aspirational: 26 PASS + 1 PARTIAL + 1 FAIL = 26.5 / 28 → 132.5 pts**

**V-05 Composite: 60 + 30 + 132.5 = 222.5** — GOLDEN ✓

---

## Rankings

| Rank | Variate | Score | Golden | Delta from prev |
|------|---------|-------|--------|-----------------|
| 1 (tie) | **V-04** | **222.5** | ✓ | — |
| 1 (tie) | **V-05** | **222.5** | ✓ | 0 |
| 3 (tie) | V-01 | 212.5 | ✓ | −10 |
| 3 (tie) | V-02 | 212.5 | ✓ | 0 |
| 5 | V-03 | 202.5 | ✓ | −10 |

**All variates golden.** Score spread: 20 pts from best to worst.

---

## Criterion Pass Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-08 | F | F | F | F | F |
| C-14 | P/2 | P/2 | P/2 | P/2 | P/2 |
| C-22 | ✓ | ✓ | **F** | ✓ | ✓ |
| C-25 | ✓ | **F** | ✓ | ✓ | ✓ |
| C-29 | **F** | ✓ | **F** | ✓ | ✓ |
| C-31 | ✓ | ✓ | **F** | ✓ | ✓ |
| C-34 | **✓** | **F** | **✓** | **✓** | **✓** |
| C-35 | **F** | **✓** | **F** | **✓** | **✓** |

---

## Excellence Signals from V-04/V-05 (Top Score)

**Signal 1 — C-34 and C-35 operate on non-overlapping sections.** C-34 targets the YAML template's `gate_fail:` field lines (adding `Why:` inline). C-35 targets the BAD PLAN block and correction table (adding recommended-tier coverage). They share no structural surface — neither displaces the other. The combination is purely additive over C-33.

**Signal 2 — Compound gate_fail: creates a self-contained atomic teaching unit.** When `gate_fail: "drafts complete"   # WRONG C-07 — Why: plan identity disallows completion-state gates; name the artifact instead` is readable in isolation, the wrong form, the criterion violated, and the principle reason are co-located. A model filling the structural field encounters all three without scanning header context.

**Signal 3 — BAD PLAN + correction table dual-format closure eliminates access asymmetry.** When both formats independently cover all 7 criteria (C-31 + C-29 = C-35), a model that consults either artifact is equally equipped. A model that reads the BAD PLAN finds example-based recommended error patterns; a model that scans the correction table before authoring finds lookup-based recommended patterns. Neither format is primary.

**Signal 4 — V-01's "essential-only" control was not achieved.** Despite the label "essential violations (C-01 through C-04)", the BAD PLAN carried C-05/C-06 tags on namespace-label stage names. This means C-22 and C-31 accidentally PASS in V-01 — confirming that recommended-criterion violations (namespace labels, dep order) are difficult to exclude from a realistic BAD PLAN because they naturally co-occur with essential violations in wrong plans.

---

## C-08 as the Persistent Ceiling

C-08 (Quantified Gate Thresholds) fails in all five variates. At R10, the prompt architecture is fully saturated for structural teaching quality — the only systematic gain left at the next round is closing C-08 with quantified gate conditions, and potentially closing C-14 with explicit `# REQUIRED: DO NOT add skills here` echo annotations.

---

```json
{"top_score": 222.5, "all_essential_pass": true, "new_patterns": ["Compound gate_fail: annotation (criterion tag + Why: at the same field line) makes gate_fail a self-contained atomic teaching unit — wrong form, criterion violated, and principle reason co-located so a model filling the structural slot encounters all three without scanning adjacent header context", "Dual error-format recommended coverage (BAD PLAN + correction table both independently covering C-05/C-06/C-07) eliminates access asymmetry — a model consulting either artifact is equally equipped against recommended-tier violations regardless of which format it reads first"]}
```
