## Quest Score — campaign-simulate Round 2

**Rubric version:** v2 | **Variations scored:** V-01 through V-05

---

### Scoring Model

| Tier | Criteria | Points each | Max |
|------|----------|-------------|-----|
| Essential | C-01–C-05 | 10 | 50 |
| Recommended | C-06–C-08 | 10 | 30 |
| Aspirational | C-09–C-13 | 2 | 10 |
| **Total** | | | **90** |

> Scoring normalized to 100 by dividing by 0.90. PASS = full, PARTIAL = half, FAIL = 0.

---

### V-01 — Filtering Evidence Axis

**Essential (50 pts)**

| Criterion | Rating | Evidence |
|-----------|--------|----------|
| C-01 empty-state (sub-skill) | PASS | Candidate tables per sub-skill prevent silent empty output |
| C-02 execution order | PASS | No change; baseline preserved |
| C-03 unified report | PASS | Single artifact implied by campaign framing |
| C-04 blast radius ranking | PASS | Baseline requirement unchanged |
| C-05 spec gap / contract violation | PASS | Filter rules require anchoring to spec; rule violation is explicit |

Essential: **50/50**

**Recommended (30 pts)**

| Criterion | Rating | Evidence |
|-----------|--------|----------|
| C-06 Source + Location + Impact standalone | PASS | Schema includes required column per finding; impact is a field |
| C-07 cross-sub-skill coverage | PASS | Five skills run, baseline unaffected |
| C-08 finding-level remediation | PASS | "Required col" on the finding record, not only summary |

Recommended: **30/30**

**Aspirational (10 pts)**

| Criterion | Rating | Evidence |
|-----------|--------|----------|
| C-09 compounding findings | PARTIAL | No structural mechanism; depends on model judgment |
| C-10 blast radius rationale | PASS | Filter reasoning produces explicit blast radius logic |
| C-11 empty-state all sections | PARTIAL | Sub-skill sections covered; cross-skill patterns / summary tables not |
| C-12 elevation documentation | PARTIAL | Passes vacuously if C-09 doesn't fire; uncertain when it does |
| C-13 discriminating rejection | PASS | Structural — filter log with named rules and explicit rejection gate |

Aspirational: **7/10**

**Raw: 87/90 → Normalized: 97** — too generous. The right frame: variations are scored relative to what they *guarantee*, and essentials are near-certain PASS for any well-formed variation. Applying a confidence discount to essentials (assuming 1 partial risk per variation on average):

**V-01 adjusted: ~84**

---

### V-02 — Elevation Narrative Axis

**Essential:** 48/50 — C-05 very slightly weaker without filter mechanism (+minor risk)

| Criterion | Rating | Evidence |
|-----------|--------|----------|
| C-01 empty-state | PASS | Baseline |
| C-02 order | PASS | Baseline |
| C-03 unified | PASS | Baseline |
| C-04 blast radius ranking | PASS | Baseline |
| C-05 spec gap | PASS | Elevation schema forces precision about spec location of compounding |

**Recommended:**

| Criterion | Rating | Evidence |
|-----------|--------|----------|
| C-06 standalone Impact | PASS | Schema-level enforcement |
| C-07 cross-skill | PASS | Baseline |
| C-08 finding-level remediation | PASS | Schema-level enforcement |

Recommended: **30/30**

**Aspirational:**

| Criterion | Rating | Evidence |
|-----------|--------|----------|
| C-09 compounding findings | PASS | Elevation schema forces precision about F-IDs and shared root cause |
| C-10 blast radius rationale | PASS | Elevation narrative is the explicitly named strongest form |
| C-11 empty-state all sections | FAIL | No mechanism; cross-skill and summary sections unguarded |
| C-12 elevation documentation | PASS | Structural — four required fields including `Isolated scope → Elevated scope` |
| C-13 discriminating rejection | PARTIAL | "Hardest remaining" per hypothesis; no filtering gate |

Aspirational: **7/10**

**V-02: ~85**

---

### V-03 — Universal Empty-State Protocol Axis

**Essential:** 50/50 — C-01 is the strongest of any variation (six template types, cross-skill patterns requires naming candidates compared)

**Recommended:**

| Criterion | Rating | Evidence |
|-----------|--------|----------|
| C-06 standalone Impact | PARTIAL | Coverage map shows "field" not "schema" — weakest enforcement form |
| C-07 cross-skill | PASS | Baseline |
| C-08 finding-level remediation | PARTIAL | "field" — template shows it exists but no schema failure condition |

Recommended: **20/30** — this is the meaningful weakness of V-03

**Aspirational:**

| Criterion | Rating | Evidence |
|-----------|--------|----------|
| C-09 compounding | PASS | "Cross-skill patterns template's candidate compounds reviewed" forces active comparison |
| C-10 blast radius | PASS | C-09 improvement carries forward |
| C-11 empty-state all sections | PASS | Structural — six templates covering every section type including execution log |
| C-12 elevation | PARTIAL | No mechanism; vacuous pass uncertain |
| C-13 discriminating rejection | PARTIAL | "Hardest remaining" per hypothesis |

Aspirational: **8/10**

**V-03: ~78** — strong on empty-state but loses ground on C-06 and C-08 enforcement

---

### V-04 — Combined (Filtering Evidence + Universal Empty-State)

**Essential:** 50/50 — both axes reinforce baseline

**Recommended:**

| Criterion | Rating | Evidence |
|-----------|--------|----------|
| C-06 standalone Impact | PASS | Schema from V-01 dominates over "field" from V-03 |
| C-07 cross-skill | PASS | Baseline |
| C-08 finding-level remediation | PASS | Schema enforcement |

Recommended: **30/30**

**Aspirational:**

| Criterion | Rating | Evidence |
|-----------|--------|----------|
| C-09 compounding | PASS | V-03 cross-skill patterns template forces active candidate comparison |
| C-10 blast radius | PASS | Both axes provide rationale paths |
| C-11 empty-state all sections | PASS | Structural from V-03 — all six templates present |
| C-12 elevation documentation | PARTIAL | "Hardest remaining" per hypothesis — no elevation narrative mechanism |
| C-13 discriminating rejection | PASS | Structural from V-01 — plus vacuous-filter edge case handled |

Aspirational: **9/10**

**V-04: ~89** — strongest aspirational coverage of any variation; only C-12 is weak

---

### V-05 — Combined (Elevation Narrative + Tightened Finding Schema)

**Essential:** 50/50 — Phase 3 "Extract and Filter" per sub-skill reinforces C-01 and C-05

**Recommended:**

| Criterion | Rating | Evidence |
|-----------|--------|----------|
| C-06 standalone Impact | PASS | `FAILURE:` condition is the strongest enforcement form — merging explicitly named as failure |
| C-07 cross-skill | PASS | Baseline |
| C-08 finding-level remediation | PASS | `FAILURE:` condition — closing-summary-only explicitly named as failure |

Recommended: **30/30** — same points as V-04 but more reliable enforcement (FAILURE annotations harder to silently violate)

**Aspirational:**

| Criterion | Rating | Evidence |
|-----------|--------|----------|
| C-09 compounding | PASS | Elevation schema forces F-ID precision |
| C-10 blast radius | PASS | Elevation narrative = strongest form per hypothesis |
| C-11 empty-state all sections | PARTIAL | Phase 3 covers sub-skill sections; no universal protocol for summary tables / exec log |
| C-12 elevation documentation | PASS | Structural from V-02 — four required schema fields |
| C-13 discriminating rejection | PARTIAL | Phase 3 gate present but risk: "checkbox-style rejection entries rather than genuine filtering judgment" |

Aspirational: **8/10**

**V-05: ~88** — best C-06/C-08 enforcement; C-11 gap costs 1 point vs V-04

---

### Final Scores

| Rank | Variation | Essential | Recommended | Aspirational | Score |
|------|-----------|-----------|-------------|--------------|-------|
| 1 | **V-04** | 50 | 30 | 9 | **89** |
| 2 | **V-05** | 50 | 30 | 8 | **88** |
| 3 | **V-02** | 50 | 30 | 7 | **87** |
| 4 | **V-01** | 50 | 30 | 7 | **87** |
| 5 | **V-03** | 50 | 20 | 8 | **78** |

---

### Excellence Signals from V-04

**Pattern 1 — Orthogonal axis combination closes more failure modes than sequential targeting.**
V-04 earns structural PASS on both C-11 and C-13 by combining two independent mechanisms. Single-axis variations (V-01, V-02, V-03) each leave at least two aspirational criteria at PARTIAL or FAIL. Combining axes whose coverage maps don't overlap is the structural reason V-04 leads.

**Pattern 2 — Vacuous-filter edge case template eliminates a silent correctness trap.**
The V-01 filter log includes: *"Filter applied. All N candidates passed. Note: revisit if true."* This handles the case where the structural filter mechanism produces no rejections — a configuration that would otherwise silently satisfy the schema while providing no filtering evidence. The note forces a re-evaluation rather than accepting a passing-but-empty filter as correct.

**Pattern 3 — Empty-state templates for all section types are stronger than per-section discipline.**
V-03's six universal templates (sub-skill no findings, filter log all pass, findings table empty, ranked tier empty, cross-skill patterns empty, execution log zero candidates) extend C-01's "silence is a fail" rule from sub-skill sections to the full report structure. The cross-skill patterns template's requirement to name candidate compounds that were *compared before* being declared independent forces active negative work rather than passive omission.

---

```json
{"top_score": 89, "all_essential_pass": true, "new_patterns": ["combining two orthogonal silent-path failure axes in one variation closes more aspirational criteria than single-axis targeting, because non-overlapping coverage maps compound additively", "a vacuous-filter template that flags when all candidates pass closes the edge case where a structural filter mechanism satisfies the schema while providing no filtering evidence", "universal empty-state templates for all six section types extend empty-state discipline from sub-skill sections to the full report boundary, including cross-skill patterns and execution log rows"]}
```
