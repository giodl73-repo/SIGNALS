## program-plan — Round 8 Score

---

## Scoring Approach

**Base (all variates share from R7 V-05 foundation):**
- C-01/C-02/C-03/C-04 (Essential, 15 pts ea): All 5 variates produce valid YAML, correct echo contract, valid skill names, artifact-state gates → **60/60 for all**
- C-05/C-06/C-07 (Recommended, 10 pts ea): All 5 variates respect layer ordering, use descriptive stage names, carry `strategy:` framing → **30/30 for all**

All variates begin at **90 pts** before aspirational scoring.

---

## Aspirational Criteria — V-01 Through V-05

### V-01 — Structural Three-Field Gate Zone

**Axis**: `gate_fail:` / `gate_pass:` / `gate:` as YAML sibling keys at all 5 non-echo zones; `gate_fail:` carries `# WRONG C-04`; `gate_pass:` carries `# Why:`. No correction table. No dep reminders at `skills:` lines.

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-08 Quantified gate thresholds | PASS | `gate_pass:` values include `">= 2 scout signals"` at Zone 1 |
| C-09 Deliberate evidence arc | PASS | Three-layer narrative + zone headers enforce arc |
| C-10 Failure-mode contrast pair | PASS | BAD YAML opening has `gate: "done"` (C-04 target) |
| C-11 Structural enforcement | PASS | Echo pre-positioned + REQUIRED; `gate_fail:` / `gate_pass:` structurally enforce C-04 |
| C-12 Dual-anchor reinforcement | PASS | C-01: BAD YAML + template; C-02: REQUIRED annotations + pre-position; C-03: catalog + template; C-04: three-field gate keys + BAD YAML |
| C-13 Arc as structural spine | PASS | `# ---- Layer 1/2/3 ----` zone headers make arc the structural skeleton |
| C-14 Deletion-resistance annotations | PASS | Echo carries `# REQUIRED: empty`, `# REQUIRED: must be present and true`, `# REQUIRED: preserve this comment` |
| C-15 Plan-level YAML error artifact | PASS | Opening BAD YAML is a complete wrong plan (all skills in one stage, `gate: "done"`) |
| C-16 Criterion-referenced error tagging | PASS | `gate_fail:` fields carry `# WRONG C-04` at all 5 zones |
| C-17 Per-zone gate contrast | PASS | `gate_fail:` (wrong) and `gate_pass:` (correct) present as YAML keys at each zone |
| C-18 Correction table | FAIL | No correction table present |
| C-19 Cross-tier error coverage | FAIL | Error artifacts only cover C-04; no C-05/C-06/C-07 entries anywhere |
| C-20 Per-zone dep constraint reminder | PARTIAL | Layer narration in zone headers names ordering rationale, but `skills:` placeholder lines lack `# requires:` annotation |
| C-21 Correction table scaffold integration | FAIL | No correction table to integrate |
| C-22 Complete recommended-tier error annotation | FAIL | No C-05/C-06/C-07 error coverage |
| C-23 Dual-position zone dep reminder | FAIL | Zone headers only; no dep reminder at `skills:` lines |
| C-24 Template-field gate contrast | PASS | `gate_fail:` / `gate_pass:` as actual YAML keys (not just comments) at all 5 zones |
| C-25 Gate contrast rationale annotation | PASS | Both `gate_fail:` and `gate_pass:` carry `# Why:` explanation at all zones |
| C-26 Criterion-tagged structural gate values | PASS | `gate_fail:` carries `# WRONG C-04` at all 5 zones |
| C-27 Uniform dep reminder syntax | FAIL | C-23 fails; no skills-line dep reminders |
| C-28 Structural gate target field co-location | PASS | `gate:` present as sibling alongside `gate_fail:` / `gate_pass:` at all 5 zones |
| C-29 Correction table recommended-tier pairs | FAIL | No correction table |
| C-30 Dep-reminder and correction-bridge independence | FAIL | No dep reminders at `skills:` lines; C-23 fails |

**Aspirational**: 14 PASS × 5 + 1 PARTIAL × 2.5 = **72.5 pts**
**V-01 Composite: 60 + 30 + 72.5 = 162.5 / 205** | Golden: YES

---

### V-02 — Correction Table with Full Recommended-Tier Coverage

**Axis**: 13-row correction table covering C-02/C-03/C-04 (essential) + C-05/C-06/C-07 (all recommended). Correction bridges at stage-name, skills, and gate positions. Simple `gate:` placeholders (no three-field structure). Dep reminders at zone headers only.

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-08 | PASS | Gate design table + numeric threshold hints in gate placeholder |
| C-09 | PASS | Three-layer arc enforced |
| C-10 | PASS | BAD YAML `gate: "done"` targets C-04 |
| C-11 | PASS | Echo REQUIRED; simple gate placeholder is structural enforcement for C-04 |
| C-12 | PASS | C-01: BAD YAML + template; C-02: REQUIRED echo + correction table echo row; C-03: correction table wrong-skill rows + catalog; C-04: BAD YAML + correction table gate rows |
| C-13 | PASS | Layer zone headers as structural spine |
| C-14 | PASS | Echo REQUIRED annotations |
| C-15 | PASS | Opening BAD YAML is plan-level wrong example |
| C-16 | FAIL | BAD YAML block has no `# WRONG C-XX` criterion tags; correction table has Criterion column but that is lookup format, not inline error annotation |
| C-17 | PARTIAL | Central gate design table provides BAD/GOOD contrast, not per-zone inline structural contrast |
| C-18 | PASS | 13-row table with >= 3 pairs covering essential criteria |
| C-19 | PASS | Correction table has C-05, C-06, C-07 entries alongside essential rows |
| C-20 | PARTIAL | Layer 2 zone header `# draft:* produced here | review:* requires draft-spec` present; `skills:` lines carry only correction bridges, not `# requires:` dep reminders |
| C-21 | PASS | Template carries `# check correction table: stage names`, `# check correction table: skill names`, `# check correction table: gates` at all covered field types |
| C-22 | PASS | Correction table covers C-05 (dep order), C-06 (namespace stage names), C-07 (executor framing) — all three |
| C-23 | FAIL | Skills: lines carry correction bridges only, not dep reminders; no dual-position |
| C-24 | FAIL | No `gate_fail:` / `gate_pass:` YAML keys; simple `gate:` placeholder only |
| C-25 | FAIL | No structural gate contrast fields to annotate with Why: |
| C-26 | FAIL | No structural gate-contrast fields |
| C-27 | FAIL | C-23 fails; no skills-line dep reminders to apply uniform syntax to |
| C-28 | FAIL | No `gate_fail:` / `gate_pass:` base; C-24 fails |
| C-29 | PASS | Correction table includes C-05, C-06, C-07 rows individually |
| C-30 | FAIL | Skills: lines carry correction bridges only; no dep reminders; C-23 fails |

**Aspirational**: 13 PASS × 5 + 2 PARTIAL × 2.5 = **70 pts**
**V-02 Composite: 60 + 30 + 70 = 160 / 205** | Golden: YES

---

### V-03 — Dual-Position Dep Reminders + Criterion-Tagged BAD YAML

**Axis**: `# WRONG C-XX` criterion tags on all wrong fields in BAD YAML. Dep reminders at BOTH zone headers AND `skills:` placeholder lines in uniform `# requires: <artifact> from Zone: <name> (C-05)` syntax. Skills: lines carry dep reminder AND correction bridge independently. Minimal 7-row correction table (essential-only: C-02/C-03/C-04). Simple `gate:` placeholders.

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-08 | PASS | Gate design table + threshold hints in gate placeholder |
| C-09 | PASS | Three-layer arc |
| C-10 | PASS | BAD YAML has `gate: "done"` (C-04 essential target) |
| C-11 | PASS | Echo REQUIRED; gate placeholder enforces C-04 structurally |
| C-12 | PASS | C-01: BAD YAML + template; C-02: `# WRONG C-02` in BAD YAML + REQUIRED echo; C-03: `# WRONG C-03` in BAD YAML + correction table; C-04: `# WRONG C-04` in BAD YAML + gate design table |
| C-13 | PASS | Layer zone headers as structural arc spine |
| C-14 | PASS | Echo REQUIRED annotations |
| C-15 | PASS | BAD YAML is a complete plan-level wrong example with 7 criterion-tagged violations |
| C-16 | PASS | BAD YAML carries `# WRONG C-06`, `# WRONG C-05` (×2), `# WRONG C-03`, `# WRONG C-04`, `# WRONG C-02` (×2) |
| C-17 | PARTIAL | Gate design table provides central BAD/GOOD contrast; no per-zone inline gate contrast in template |
| C-18 | PASS | 7-row correction table (>= 3 pairs, covering C-02/C-03/C-04) |
| C-19 | PASS | BAD YAML carries `# WRONG C-05` and `# WRONG C-06` — recommended-tier coverage in error artifact |
| C-20 | PASS | Skills: lines carry `# (no upstream dep)` or `# requires: <artifact> from Zone: <name> (C-05)` at all dep-bearing zones |
| C-21 | PASS | Template carries `# check correction table: skill names` and `# check correction table: gates` at all field types covered by table |
| C-22 | FAIL | BAD YAML covers C-05 and C-06 but lacks `# WRONG C-07`; correction table has no C-07 rows; C-07 not covered in any error artifact |
| C-23 | PASS | Zone headers AND skills: lines both carry dep reminders at all dep-bearing zones |
| C-24 | FAIL | No `gate_fail:` / `gate_pass:` YAML keys; simple `gate:` only |
| C-25 | FAIL | No structural gate contrast fields; C-24 fails |
| C-26 | FAIL | No structural gate-contrast fields |
| C-27 | PASS | Uniform `# requires: <artifact> from Zone: <name> (C-05)` syntax across all dep zones at both positions |
| C-28 | FAIL | C-24 fails; no three-field gate structure |
| C-29 | FAIL | Correction table is essential-only (C-02/C-03/C-04); no C-05/C-06/C-07 rows |
| C-30 | PASS | Skills: lines carry `# requires: <artifact> (C-05)` AND `# check correction table: skill names` as independent annotations at all dep zones |

**Aspirational**: 16 PASS × 5 + 1 PARTIAL × 2.5 = **82.5 pts**
**V-03 Composite: 60 + 30 + 82.5 = 172.5 / 205** | Golden: YES

---

### V-04 — Three-Field Gates + Full Correction Table (Combo)

**Axis**: V-01's three-field gate structure + V-02's 13-row correction table covering all recommended criteria. Correction bridges at all three field types. Dep reminders at zone headers only (no skills-line reminders — C-23/C-27/C-30 excluded by design).

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-08 | PASS | `gate_pass:` values quantified; gate design table |
| C-09 | PASS | Three-layer arc |
| C-10 | PASS | BAD YAML `gate: "done"` + `gate_fail:` fields |
| C-11 | PASS | Echo REQUIRED + three-field gate structure structurally enforces C-04 |
| C-12 | PASS | C-01: BAD YAML + template; C-02: REQUIRED echo + correction table; C-03: correction table wrong-skill rows + catalog; C-04: three-field gates + BAD YAML |
| C-13 | PASS | Layer zone headers as structural spine |
| C-14 | PASS | Echo REQUIRED annotations |
| C-15 | PASS | Opening BAD YAML is plan-level wrong example |
| C-16 | PASS | `gate_fail:` fields carry `# WRONG C-04` at all 5 zones |
| C-17 | PASS | `gate_fail:` (wrong) and `gate_pass:` (correct) as YAML keys at all 5 non-echo zones |
| C-18 | PASS | 13-row correction table with essential + recommended tier coverage |
| C-19 | PASS | Correction table covers C-05/C-06/C-07; `gate_fail:` tags cover C-04 |
| C-20 | PARTIAL | Zone headers carry `# requires: <artifact> from Zone: <name> (C-05)`; skills: lines carry only `# check correction table: skill names`, no dep reminder |
| C-21 | PASS | Correction bridges at stage-name, skills, and gate positions |
| C-22 | PASS | Correction table covers C-05, C-06, C-07 individually |
| C-23 | FAIL | Dep reminders at zone headers only; skills: lines lack `# requires:` |
| C-24 | PASS | `gate_fail:` / `gate_pass:` as YAML keys at all 5 non-echo zones |
| C-25 | PASS | `gate_fail:` carries `# WRONG C-04: execution state -- unverifiable`; `gate_pass:` carries `# Why: artifact name + threshold -- inspectable` at all zones |
| C-26 | PASS | `gate_fail:` carries `# WRONG C-04` at all 5 zones |
| C-27 | FAIL | C-23 fails; no skills-line dep reminders to apply uniform syntax to |
| C-28 | PASS | `gate:` present as sibling to `gate_fail:` / `gate_pass:` at all 5 zones |
| C-29 | PASS | Correction table has C-05 (dep order), C-06 (namespace names), C-07 (executor framing) rows |
| C-30 | FAIL | Skills: lines carry correction bridges only; C-23 fails |

**Aspirational**: 19 PASS × 5 + 1 PARTIAL × 2.5 = **97.5 pts**
**V-04 Composite: 60 + 30 + 97.5 = 187.5 / 205** | Golden: YES

---

### V-05 — Golden Synthesis

**Axis**: All five clusters simultaneously. Zone-labeled template (`Zone 1` through `Zone 5`). Three-field gate structure with `# WRONG C-04: Why:` on `gate_fail:` and `# Why:` on `gate_pass:`. Full 13-row correction table covering C-02–C-07. Uniform `# requires: <artifact> from Zone: <name> (C-05)` at BOTH zone headers AND `skills:` lines at all dep zones. `# check correction table: skill names` independently alongside dep reminders at every dep-bearing `skills:` line. BAD YAML carries `# WRONG C-XX` on every wrong field (C-02 × 2, C-03, C-04, C-05 × 2, C-06). Echo carries three REQUIRED annotations plus displacement prohibition.

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-08 | PASS | `gate_pass:` quantified at all zones; gate design table |
| C-09 | PASS | Five-zone arc (Breadth → Design → Validation → Simulation → Synthesis → Echo) |
| C-10 | PASS | BAD YAML `gate: "done"` (C-04 essential target) |
| C-11 | PASS | Echo pre-positioned with REQUIRED + three-field gate structure structurally enforces C-04 |
| C-12 | PASS | All 4 essential criteria have >= 2 independent anchors each |
| C-13 | PASS | Zone 1–5 headers + echo are the structural document spine |
| C-14 | PASS | Echo has `# REQUIRED: preserve this comment`, `# REQUIRED: preserve this name`, `# REQUIRED: empty`, `# REQUIRED: must be present and true`, `# REQUIRED: DO NOT add skills. DO NOT move echo.` — 5 annotations across 4 fields |
| C-15 | PASS | Opening BAD YAML is multi-field multi-stage wrong plan |
| C-16 | PASS | BAD YAML tags all wrong fields (`# WRONG C-02` × 2, `# WRONG C-03`, `# WRONG C-04`, `# WRONG C-05` × 2, `# WRONG C-06`); `gate_fail:` fields also carry `# WRONG C-04` |
| C-17 | PASS | `gate_fail:` / `gate_pass:` as YAML keys at all 5 non-echo zones |
| C-18 | PASS | 13-row correction table covering essential + recommended |
| C-19 | PASS | BAD YAML covers C-05/C-06; correction table covers C-05/C-06/C-07 |
| C-20 | PASS | Skills: lines carry `# requires: <artifact> from Zone: <name> (C-05)` at all dep-bearing zones |
| C-21 | PASS | Correction bridges at stage-name, skills, and gate positions throughout template |
| C-22 | PASS | BAD YAML covers C-05/C-06; correction table covers C-05/C-06/C-07 — all three recommended criteria in error artifacts |
| C-23 | PASS | Zone headers AND skills: lines both carry dep reminders at Zones 2, 3, 4, 5 |
| C-24 | PASS | `gate_fail:` / `gate_pass:` as YAML keys at all 5 non-echo zones |
| C-25 | PASS | `gate_fail:` carries `# WRONG C-04: Why: ...` and `gate_pass:` carries `# Why:` at all 5 zones |
| C-26 | PASS | `gate_fail:` carries `# WRONG C-04` at all 5 zones |
| C-27 | PASS | Uniform `# requires: <artifact> from Zone: <name> (C-05)` syntax at both positions across all dep zones |
| C-28 | PASS | `gate:` as sibling to `gate_fail:` / `gate_pass:` at all 5 non-echo zones |
| C-29 | PASS | Correction table has C-05 (dep-order), C-06 (namespace stage names), C-07 (executor framing) rows — all three recommended |
| C-30 | PASS | Skills: lines carry `# requires: <artifact> (C-05)` AND `# check correction table: skill names` independently at all 4 dep-bearing zones |

**Aspirational**: 23/23 PASS × 5 = **115 pts**
**V-05 Composite: 60 + 30 + 115 = 205 / 205** | Golden: YES

---

## Rankings

| Rank | Variation | Composite | Essential | Aspirational PASS | Aspirational PARTIAL | Aspirational FAIL | Golden |
|------|-----------|-----------|----------|-------------------|----------------------|-------------------|--------|
| 1 | **V-05** (golden synthesis) | **205.0** | 4/4 | 23/23 | 0 | 0 | YES |
| 2 | **V-04** (combo: gates + table) | **187.5** | 4/4 | 19/23 | 1 | 3 | YES |
| 3 | **V-03** (dep reminders + criterion tags) | **172.5** | 4/4 | 16/23 | 1 | 6 | YES |
| 4 | **V-01** (three-field gate structure) | **162.5** | 4/4 | 14/23 | 1 | 8 | YES |
| 5 | **V-02** (correction table + recommended tier) | **160.0** | 4/4 | 13/23 | 2 | 8 | YES |

---

## Excellence Signals from V-05

**What made V-05 decisively better than V-04 (the next-best, -17.5 pts):**

V-04 had C-23/C-27/C-30 as its remaining gap. V-05 closed all three by adding dual-position dep reminders in uniform syntax, each carrying an independent correction bridge at the `skills:` line. No other cluster was missing. The synthesis was strictly additive — the three-field gate structure did not interfere with the dep annotation cluster, and the correction table did not interfere with the gate contrast.

**Two patterns from V-05 not yet captured as rubric criteria:**

**Pattern 1 — Named-zone cross-reference in dep annotations.** V-05 explicitly indexes zones as `Zone 1: Layer 1 Breadth`, `Zone 2: Layer 2 Design`, etc. and the dep reminders use zone names as lookup keys: `# requires: scout-feasibility artifact from Zone: Layer 1 Breadth (C-05)`. Earlier variates used "Layer 1" / "Layer 2" informally; V-05 makes zone names indexable identifiers that both headers and `skills:` annotations reference by the same token. This creates a closed pointer system within the template — any zone can reference any prior zone unambiguously without prose disambiguation.

**Pattern 2 — Echo multi-REQUIRED annotation redundancy.** V-05 places REQUIRED annotations on five distinct echo touch points: the section comment, `name:`, `skills:`, `auto:`, and adds a displacement prohibition (`# REQUIRED: DO NOT add skills to echo. DO NOT move echo before other stages.`). C-14 requires at least one; V-05 saturates all echo fields. The displacement prohibition introduces a qualitatively different annotation class — prohibiting structural MOVEMENT vs. prohibiting content addition — that C-14 does not distinguish.

---

```json
{"top_score": 205, "all_essential_pass": true, "new_patterns": ["Named-zone cross-reference in dep annotations: explicitly indexing zones as Zone N labels and using those labels as lookup keys in dep reminders creates a closed pointer system within the template where any zone can reference any upstream zone unambiguously", "Echo multi-REQUIRED annotation redundancy: saturating all echo fields with REQUIRED annotations and adding a displacement-prohibition class (DO NOT move echo) distinct from content-prohibition (DO NOT add skills) creates five independent friction points on a single structural element"]}
```
