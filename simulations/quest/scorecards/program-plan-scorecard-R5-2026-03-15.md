## program-plan — R5 Score Report (v5 Rubric, Round 5)

---

### V-01 — Cross-Tier Error Coverage (C-19 axis)

**Foundation**: R4 V-01 (criterion-tagged BAD block + lifecycle phases). Axis: comprehensive `# WRONG C-NN` tags extending to C-05/C-06/C-07 in the BAD PLAN block.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **C-01** | PASS | Valid YAML template + BAD PLAN block both structurally complete |
| **C-02** | PASS | Echo pre-positioned; `# REQUIRED: DO NOT add skills here. DO NOT move echo before other stages. (WRONG C-02 if violated)` |
| **C-03** | PASS | Skill catalog provided; BAD PLAN has `# WRONG C-03: "scout:analysis" does not exist` |
| **C-04** | PASS | BAD PLAN `# WRONG C-04` + per-zone inline `# NOT "done" / "complete" / "proceed" (WRONG C-04)` at gate fields |
| **C-05** | PASS | Canonical order stated; BAD PLAN `# WRONG C-05: review:design before draft:spec — dependency violated` |
| **C-06** | PASS | BAD PLAN `# WRONG C-06` on `name: scout` and `name: draft`; template inline `NOT "scout" (WRONG C-06)` |
| **C-07** | PASS | Opening statement; template `# REQUIRED: ...plan, not an executor`; BAD PLAN `# WRONG C-07` |
| **C-08** | PASS | Numeric threshold guidance per zone; template gate hint `'>= N scout signals present'` |
| **C-09** | PASS | Four-phase arc (Discovery → Design → Validation → Synthesis) plus echo |
| **C-10** | PASS | BAD PLAN block + template PASS form — contrast pair anchored to C-04 |
| **C-11** | PASS | Echo pre-positioned in template; lifecycle phase headers enforce arc structure |
| **C-12** | PASS | C-01: template + BAD PLAN level block; C-02: template REQUIRED + BAD PLAN `# WRONG C-02`; C-03: catalog + BAD PLAN tag; C-04: BAD PLAN + per-zone inline — all 4 dual-anchored |
| **C-13** | PASS | `# ---- PM Phase: Discovery ----` / `Design` / `Validation` / `Synthesis` section headers organize the prompt |
| **C-14** | PASS | Echo slot: three REQUIRED annotations naming prohibition explicitly |
| **C-15** | PASS | BAD PLAN covers 3 stages with wrong gates, wrong echo, invented skill name — plan-level |
| **C-16** | PASS | `# WRONG C-02`, `# WRONG C-03`, `# WRONG C-04`, `# WRONG C-05`, `# WRONG C-06`, `# WRONG C-07` on each wrong field |
| **C-17** | PARTIAL | Per-zone: gate placeholder shows PASS form; inline `# NOT "done"` shows FAIL — substance present but not the labeled `FAIL gate: / PASS gate:` format; simulation zone not covered |
| **C-18** | FAIL | No correction table |
| **C-19** | PASS | BAD PLAN block annotates all three recommended criteria (`# WRONG C-05`, `# WRONG C-06`, `# WRONG C-07`) alongside essential-tier tags |
| **C-20** | FAIL | Dependency notes appear at zone header comments (e.g., `# review:* requires draft:spec — this zone MUST precede the Validation phase`) but NOT at the `skills:` placeholder line |
| **C-21** | FAIL | No correction table; prerequisite not met |

**Scoring Worksheet:**
```
Essential:    C-01 [P]  C-02 [P]  C-03 [P]  C-04 [P]
              4/4  →  4/4 * 60 = 60 pts

Recommended:  C-05 [P]  C-06 [P]  C-07 [P]
              3/3  →  3/3 * 30 = 30 pts

Aspirational: C-08 [P]  C-09 [P]  C-10 [P]  C-11 [P]
              C-12 [P]  C-13 [P]  C-14 [P]  C-15 [P]
              C-16 [P]  C-17 [½]  C-18 [F]  C-19 [P]
              C-20 [F]  C-21 [F]
              10 PASS (50) + 1 PARTIAL (2.5) + 3 FAIL (0) = 52.5 pts

Composite: 60 + 30 + 52.5 = 142.5 / 160
Golden: all essential PASS AND composite 142.5 >= 80 → YES
```

---

### V-02 — Per-Zone Dependency Constraint at Skill Position (C-20 axis)

**Foundation**: R4 V-02 (arc-zone structure + per-zone FAIL/PASS gate examples). Axis: PREREQUISITE reminders moved to the `skills:` placeholder line itself.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **C-01** | PASS | Valid YAML template with structural completeness |
| **C-02** | PASS | Echo pre-positioned; `# REQUIRED: DO NOT add skills here. DO NOT move echo before other stages.` + REQUIRED on `skills: []` and `auto: true` |
| **C-03** | PASS | Skill catalog provided; template uses namespace-qualified placeholders only |
| **C-04** | PASS | Per-zone labeled `FAIL gate: "..."` / `PASS gate: "..."` pairs at each zone cover execution-state failure |
| **C-05** | PASS | Canonical order stated explicitly at top; per-zone PREREQUISITE reminders reinforce it |
| **C-06** | PASS | Template inline `NOT "scout"`, `NOT "draft"`, `NOT "review"`, `NOT "listen"` per zone |
| **C-07** | PASS | Opening statement `is a plan, not an executor`; template `# REQUIRED: preserve this comment — this program is a plan, not an executor` |
| **C-08** | PASS | Numeric threshold in dependency order note; gate placeholder hint |
| **C-09** | PASS | Five arc zones (Discovery/Design/Validation/Simulation/Synthesis) plus echo |
| **C-10** | PASS | Per-zone FAIL/PASS gate contrast anchored to C-04 — qualifies as BAD/GOOD pair |
| **C-11** | PASS | Echo pre-positioned; zone section headers enforce dependency arc structurally |
| **C-12** | PARTIAL | C-01 has only the template as anchor (no BAD PLAN level block); C-02/C-03/C-04 all dual-anchored. 3 of 4 essential criteria fully covered |
| **C-13** | PASS | `# ==== Zone: Discovery ====` / `Design` / `Validation` / `Simulation` / `Synthesis` are first-class section dividers |
| **C-14** | PASS | Echo: `# REQUIRED: DO NOT add skills here. DO NOT move echo before other stages.` + `# REQUIRED: empty` + `# REQUIRED: must be present and true` |
| **C-15** | FAIL | No plan-level BAD YAML block; per-zone FAIL gate examples are gate strings only, not a complete wrong plan |
| **C-16** | FAIL | Per-zone FAIL examples say "execution state" but carry no `# WRONG C-NN` criterion tags; no BAD PLAN block with criterion tags |
| **C-17** | PASS | All 5 non-echo zones carry labeled `FAIL gate: "..."` / `PASS gate: "..."` pairs directly in the template skeleton |
| **C-18** | FAIL | No correction table |
| **C-19** | FAIL | FAIL gate examples target C-04 only; no error artifact covers C-05/C-06/C-07 |
| **C-20** | PASS | All dependency-bearing zones carry PREREQUISITE comment at zone header AND `# requires: ...` at the `skills:` placeholder line: Design (`skills: # requires: scout signals from Discovery zone`), Validation (`skills: # requires: draft:spec artifact from Design zone`), Simulation (`skills: # requires: review:* artifact from Validation zone`), Synthesis (`skills: # requires: at least one flow/trace or review artifact`) |
| **C-21** | FAIL | No correction table; prerequisite not met |

**Scoring Worksheet:**
```
Essential:    C-01 [P]  C-02 [P]  C-03 [P]  C-04 [P]
              4/4  →  60 pts

Recommended:  C-05 [P]  C-06 [P]  C-07 [P]
              3/3  →  30 pts

Aspirational: C-08 [P]  C-09 [P]  C-10 [P]  C-11 [P]
              C-12 [½]  C-13 [P]  C-14 [P]  C-15 [F]
              C-16 [F]  C-17 [P]  C-18 [F]  C-19 [F]
              C-20 [P]  C-21 [F]
              9 PASS (45) + 1 PARTIAL (2.5) + 4 FAIL (0) = 47.5 pts

Composite: 60 + 30 + 47.5 = 137.5 / 160
Golden: all essential PASS AND composite 137.5 >= 80 → YES
```

---

### V-03 — Correction Table Scaffold Integration (C-21 axis)

**Foundation**: R4 V-03 (correction table + inertia opening). Axis: `# check correction table` bridges added at ALL three field types (stage names, gate strings, skill lists).

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **C-01** | PASS | Valid YAML template + BAD PLAN block (single-stage inertia plan) |
| **C-02** | PASS | Echo: `# REQUIRED: DO NOT add skills here. DO NOT move echo before other stages.` + `# REQUIRED: empty -- check correction table (C-02)` |
| **C-03** | PASS | Skill catalog; correction table has 4 C-03 entries mapping invented names to real ones |
| **C-04** | PASS | BAD PLAN `gate: "done"` shown wrong; GOOD plan shows artifact-referencing gates; correction table has 5 C-04 pairs; template `# NOT "done"` per zone |
| **C-05** | PASS | Canonical order stated; Layer 2 header: `review:* requires draft:spec | flow:*/trace:* require review:*` |
| **C-06** | PASS | Correction table has 4 C-06 pairs mapping namespace-label names to intent-label names; template `NOT "scout"` etc. |
| **C-07** | PASS | Opening statement; template `# REQUIRED: ...plan, not an executor` |
| **C-08** | PASS | Gate hint includes numeric threshold; GOOD plan example shows `>= 2 scout signals reviewed` |
| **C-09** | PASS | Three-layer structure (Layer 1: Breadth / Layer 2: Depth / Layer 3: Synthesis); both GOOD plan and template |
| **C-10** | PASS | BAD PLAN (wrong stage, `gate: "done"`) + GOOD plan (three-layer, artifact gates) — contrast pair anchored to C-04 |
| **C-11** | PASS | Echo pre-positioned in template; layer headers enforce arc structure |
| **C-12** | PASS | C-01: template + BAD PLAN level block; C-02: template REQUIRED + correction table C-02 entry; C-03: catalog + correction table C-03 entries; C-04: BAD PLAN `gate: "done"` + per-zone `# NOT "done"` + correction table — all 4 dual-anchored |
| **C-13** | PASS | `# ---- Layer 1: Breadth ----` / `# ---- Layer 2: Depth ----` / `# ---- Layer 3: Synthesis ----` as structural section dividers |
| **C-14** | PASS | Echo: three REQUIRED annotations; `# REQUIRED: empty -- check correction table (C-02)` and `# REQUIRED: must be present and true -- check correction table (C-02)` |
| **C-15** | PASS | BAD PLAN shows complete multi-stage YAML with `gate: "done"`, dependency violation, single-stage flat structure — plan-level |
| **C-16** | PASS | Correction table has `Criterion` column linking every wrong form to a specific criterion (C-04, C-03, C-06, C-02); criterion-referenced format satisfies C-16 |
| **C-17** | PARTIAL | Template layer zones carry inline `# check correction table: gates -- NOT "done" / "complete"` (FAIL marker) and gate placeholder hints (PASS form), but not the clean labeled `FAIL gate: / PASS gate:` format; simulation sub-stage not explicitly contrasted |
| **C-18** | PASS | Correction table has 15 pairs covering C-04 (5), C-03 (4), C-06 (4), C-02 (2) — >= 3 pairs across multiple essential criteria |
| **C-19** | PASS | Correction table has 4 C-06 entries (recommended criterion) alongside essential-criterion entries; cross-tier coverage via table |
| **C-20** | FAIL | Layer 2 header has dependency note (`review:* requires draft:spec | flow:*/trace:* require review:*`) but template skill-list placeholders only say `# check correction table: skill names` — no inline prerequisite statement naming the required artifact at the skills field |
| **C-21** | PASS | Template carries `# check correction table: stage names` at `name:` fields, `# check correction table: gates -- NOT "done"` at `gate:` fields, and `# check correction table: skill names` at `skills:` fields — all three field types covered in the table have navigational bridges |

**Scoring Worksheet:**
```
Essential:    C-01 [P]  C-02 [P]  C-03 [P]  C-04 [P]
              4/4  →  60 pts

Recommended:  C-05 [P]  C-06 [P]  C-07 [P]
              3/3  →  30 pts

Aspirational: C-08 [P]  C-09 [P]  C-10 [P]  C-11 [P]
              C-12 [P]  C-13 [P]  C-14 [P]  C-15 [P]
              C-16 [P]  C-17 [½]  C-18 [P]  C-19 [P]
              C-20 [F]  C-21 [P]
              12 PASS (60) + 1 PARTIAL (2.5) + 1 FAIL (0) = 62.5 pts

Composite: 60 + 30 + 62.5 = 152.5 / 160
Golden: all essential PASS AND composite 152.5 >= 80 → YES
```

---

### V-04 — Cross-Tier Errors + Skill-Position Dependency Reminders (C-19 + C-20)

**Foundation**: R4 V-04 (criterion-tagged BAD block + per-zone FAIL/PASS gate contrast). Axes: C-19 comprehensive cross-tier coverage + C-20 PREREQUISITE at skills-line position.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **C-01** | PASS | Valid YAML template + BAD PLAN block; GOOD plan example |
| **C-02** | PASS | Echo: `# REQUIRED: DO NOT add skills here. DO NOT move echo before other stages. (WRONG C-02 if violated)` + REQUIRED on fields |
| **C-03** | PASS | Skill catalog; BAD PLAN `# WRONG C-03: "scout:analysis" does not exist` |
| **C-04** | PASS | BAD PLAN `# WRONG C-04` + per-zone labeled `FAIL gate: <-- WRONG C-04: execution state` + PASS gate per zone |
| **C-05** | PASS | Canonical order; BAD PLAN `# WRONG C-05: review:design before draft:spec`; PREREQUISITE at skill lines |
| **C-06** | PASS | BAD PLAN `# WRONG C-06` on `name: scout/draft`; template `NOT "review" -- WRONG C-06` per zone |
| **C-07** | PASS | Opening paragraph; template `# REQUIRED: preserve this comment — ...plan, not an executor` with identity rationale |
| **C-08** | PASS | Gate guidance + verification checklist item; GOOD plan example shows numeric threshold |
| **C-09** | PASS | Five-zone arc (Discovery/Design/Validation/Simulation/Synthesis) in correct order |
| **C-10** | PASS | BAD PLAN block (essential failures) + GOOD plan (correct) — contrast pair on C-04 |
| **C-11** | PASS | Echo pre-positioned; `# ==== Zone: ... ====` headers enforce arc structurally |
| **C-12** | PASS | C-01: template + BAD PLAN level block; C-02: template REQUIRED + BAD PLAN `# WRONG C-02`; C-03: catalog + BAD PLAN; C-04: BAD PLAN + per-zone FAIL/PASS labels — all 4 dual-anchored |
| **C-13** | PASS | Five `# ==== Zone: ... ====` headers as first-class structural divisions |
| **C-14** | PASS | Echo: `# REQUIRED: DO NOT add skills here. DO NOT move echo before other stages. (WRONG C-02 if violated)` + `# REQUIRED: empty -- adding skills violates C-02` + `# REQUIRED: must be present and true` |
| **C-15** | PASS | BAD PLAN covers 3 stages with wrong gates, wrong echo, invented skill, dependency violation |
| **C-16** | PASS | BAD PLAN: `# WRONG C-02/C-03/C-04/C-05/C-06/C-07` on each wrong field; per-zone FAIL examples tag `<-- WRONG C-04:` |
| **C-17** | PASS | All 5 non-echo zones carry labeled `FAIL gate: "..." <-- WRONG C-04` / `PASS gate: "..."` pairs embedded in the template skeleton |
| **C-18** | FAIL | No correction table |
| **C-19** | PASS | BAD PLAN annotates C-05 (`review:design before draft:spec`), C-06 (namespace-label names), C-07 (no plan-identity marker) alongside essential-tier tags |
| **C-20** | PASS | All dependency-bearing zones: Design (`PREREQUISITE: scout signals from Discovery zone` + `skills: # requires: sufficient scout signal`), Validation (`PREREQUISITE: review:* requires draft:spec` + `skills: # requires: draft:spec from Design zone`), Simulation (`PREREQUISITE: flow:*/trace:* require review:design` + `skills: # requires: review:* artifact`), Synthesis (`PREREQUISITE: listen:* requires at least one prior signal` + `skills: # requires: flow/trace or review artifact`) |
| **C-21** | FAIL | No correction table; prerequisite not met |

**Scoring Worksheet:**
```
Essential:    C-01 [P]  C-02 [P]  C-03 [P]  C-04 [P]
              4/4  →  60 pts

Recommended:  C-05 [P]  C-06 [P]  C-07 [P]
              3/3  →  30 pts

Aspirational: C-08 [P]  C-09 [P]  C-10 [P]  C-11 [P]
              C-12 [P]  C-13 [P]  C-14 [P]  C-15 [P]
              C-16 [P]  C-17 [P]  C-18 [F]  C-19 [P]
              C-20 [P]  C-21 [F]
              12 PASS (60) + 0 PARTIAL + 2 FAIL (0) = 60 pts

Composite: 60 + 30 + 60 = 150 / 160
Golden: all essential PASS AND composite 150 >= 80 → YES
```

---

### V-05 — Golden Synthesis (all 21 criteria)

**Foundation**: All prior R4 excellence signals + all three new axes (C-19 + C-20 + C-21). Arc-as-spine, deletion-resistance, criterion-tagged BAD block, per-zone FAIL/PASS contrast, correction table, PREREQUISITE at skills lines, scaffold bridges at all field types.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **C-01** | PASS | Valid YAML template + BAD PLAN block + GOOD plan example — three independent structural demonstrations |
| **C-02** | PASS | Echo: `# REQUIRED: DO NOT add skills here. DO NOT move echo before other stages. (WRONG C-02 if violated)` + `# REQUIRED: empty -- DO NOT add skills here; check correction table (C-02)` + `# REQUIRED: must be present and true; check correction table (C-02)` + BAD PLAN `# WRONG C-02` + correction table entry |
| **C-03** | PASS | Skill catalog + BAD PLAN `# WRONG C-03` + correction table 4 C-03 entries |
| **C-04** | PASS | BAD PLAN `# WRONG C-04` + per-zone labeled `FAIL gate: <-- WRONG C-04` + correction table 5 C-04 pairs + template `# NOT "done" (WRONG C-04)` |
| **C-05** | PASS | Canonical order; BAD PLAN `# WRONG C-05`; correction table C-05 entries (2 rows); PREREQUISITE at all 4 dependency-bearing skills lines |
| **C-06** | PASS | BAD PLAN `# WRONG C-06`; correction table 4 C-06 entries; template `NOT "scout" (WRONG C-06)` per zone |
| **C-07** | PASS | Opening paragraph; correction table C-07 entry; template `# REQUIRED: preserve this comment — ...plan, not an executor`; BAD PLAN `# WRONG C-07` |
| **C-08** | PASS | Gate guidance + GOOD plan shows `>= 2 scout signals reviewed` + verification checklist item |
| **C-09** | PASS | Five-zone arc in both GOOD plan and template; stage sequencing visible |
| **C-10** | PASS | BAD PLAN + GOOD plan — contrast pair on C-04 essential failures |
| **C-11** | PASS | Echo pre-positioned; five `# ==== Zone: ... ====` headers as structural enforcement |
| **C-12** | PASS | Every essential criterion has 3+ independent anchors; C-04 alone has BAD PLAN, per-zone FAIL labels, correction table, and inline gate markers |
| **C-13** | PASS | Five `# ==== Zone: ... ====` arc-layer headers organize the entire template; model encounters arc before reaching any skill list |
| **C-14** | PASS | Three REQUIRED annotations on echo slot; each names the prohibited action and cites the criterion |
| **C-15** | PASS | BAD PLAN: complete 3-stage YAML with wrong gates, wrong echo, invented skill, dependency violation across multiple fields |
| **C-16** | PASS | BAD PLAN: `# WRONG C-02/C-03/C-04/C-05/C-06/C-07` on every wrong field; per-zone FAIL gates tag `<-- WRONG C-04` |
| **C-17** | PASS | All 5 non-echo zones carry labeled `FAIL gate:` / `PASS gate:` pairs in the template skeleton |
| **C-18** | PASS | Correction table: 17 pairs covering C-04 (5), C-03 (3), C-06 (4), C-02 (2), C-05 (2), C-07 (1) — all 4 essential criteria + all 3 recommended criteria |
| **C-19** | PASS | BAD PLAN tags C-05/C-06/C-07; correction table has C-05/C-06/C-07 rows; cross-tier coverage in TWO independent error artifacts |
| **C-20** | PASS | All 4 dependency-bearing zones: zone-header PREREQUISITE + skills-line `# check correction table: skill names; requires: [artifact]` at each `skills:` placeholder |
| **C-21** | PASS | Template carries `# check correction table: stage names`, `# check correction table: gates -- NOT "done" (WRONG C-04)`, and `# check correction table: skill names` at the respective field types — all three field types covered in the correction table have navigational bridges |

**Scoring Worksheet:**
```
Essential:    C-01 [P]  C-02 [P]  C-03 [P]  C-04 [P]
              4/4  →  60 pts

Recommended:  C-05 [P]  C-06 [P]  C-07 [P]
              3/3  →  30 pts

Aspirational: C-08 [P]  C-09 [P]  C-10 [P]  C-11 [P]
              C-12 [P]  C-13 [P]  C-14 [P]  C-15 [P]
              C-16 [P]  C-17 [P]  C-18 [P]  C-19 [P]
              C-20 [P]  C-21 [P]
              14 PASS (70) + 0 PARTIAL + 0 FAIL = 70 pts

Composite: 60 + 30 + 70 = 160 / 160
Golden: all essential PASS AND composite 160 >= 80 → YES (perfect score)
```

---

## Summary Scorecard

| Variation | Essential | Recommended | Aspirational | **Total** | Golden |
|-----------|-----------|-------------|--------------|-----------|--------|
| V-01 | 60/60 | 30/30 | 52.5/70 | **142.5** | YES |
| V-02 | 60/60 | 30/30 | 47.5/70 | **137.5** | YES |
| V-03 | 60/60 | 30/30 | 62.5/70 | **152.5** | YES |
| V-04 | 60/60 | 30/30 | 60.0/70 | **150.0** | YES |
| V-05 | 60/60 | 30/30 | 70.0/70 | **160.0** | YES |

**Rankings**: V-05 (160) > V-03 (152.5) > V-04 (150) > V-01 (142.5) > V-02 (137.5)

All five variations are golden. V-05 is a perfect score.

---

## Differentiating Gaps

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-12 (dual-anchor) | PASS | **PARTIAL** | PASS | PASS | PASS |
| C-15 (plan-level YAML error) | PASS | **FAIL** | PASS | PASS | PASS |
| C-16 (criterion-tagged errors) | PASS | **FAIL** | PASS | PASS | PASS |
| C-17 (per-zone gate contrast) | PARTIAL | PASS | PARTIAL | PASS | PASS |
| C-18 (correction table) | FAIL | FAIL | PASS | **FAIL** | PASS |
| C-19 (cross-tier error coverage) | PASS | **FAIL** | PASS | PASS | PASS |
| C-20 (skill-position dep reminder) | **FAIL** | PASS | **FAIL** | PASS | PASS |
| C-21 (scaffold integration) | FAIL | FAIL | PASS | **FAIL** | PASS |

V-02's weaknesses stem from skipping the BAD PLAN block — losing C-15, C-16, C-12 partial, and C-19.
V-01 and V-04 both miss C-18+C-21 (no correction table).
V-03 adds the correction table (gaining C-18+C-21) but loses C-20 (dependency reminders only at layer header, not skills line).
V-04 adds C-20 and C-17 but drops C-18+C-21 (no table).
**V-05 is the only variation that holds C-17+C-18+C-19+C-20+C-21 simultaneously.**

---

## Excellence Signals from V-05

**Signal 1 — Bidirectional correction table coupling (C-18 + C-21 combined):** The correction table is built first, then the template routes to it at every covered field type. The table pulls the model in at document level; the `# check correction table: [field type]` bridges push the model back at each decision point. The two-way link ensures the table is consulted during generation, not just read before it. Neither artifact alone achieves this — the table without bridges is passive, bridges without a table are pointers to nothing.

**Signal 2 — Dual-artifact cross-tier error coverage (C-19):** V-05 covers recommended criteria C-05/C-06/C-07 in both the BAD PLAN block (`# WRONG C-05/C-06/C-07`) and the correction table (C-05 and C-06 rows). Two independent error artifacts teaching the same recommended-criterion failures makes the teaching surface redundant — the model encounters cross-tier coverage whether it focuses on the BAD block or the table, without needing to carry the lesson across both.

**Signal 3 — Skill-position dependency constraint fires at authoring moment (C-20):** Moving the prerequisite reminder from the zone-header comment to the `skills:` placeholder line — `# check correction table: skill names; requires: draft:spec from Design zone` — means the constraint is visible exactly when the model selects skills for that zone. Zone-header prerequisites require carrying the note forward across multiple template fields before reaching the decision point; skills-line prerequisites fire immediately at the moment that matters.

---

```json
{"top_score": 160, "all_essential_pass": true, "new_patterns": ["bidirectional-correction-table-coupling: table pulls at document level + template bridges push at each covered field type creates active consultation loop rather than one-time read", "skill-position-dependency-constraint: moving prerequisite reminder from zone-header to skills-placeholder-line fires constraint at exact authoring moment preventing dependency violations at source", "dual-artifact-cross-tier-coverage: encoding recommended-criterion wrong shapes in both criterion-tagged BAD block and correction table rows makes C-05/C-06/C-07 failures visible from two independent angles surviving if either artifact is skimmed"]}
```
