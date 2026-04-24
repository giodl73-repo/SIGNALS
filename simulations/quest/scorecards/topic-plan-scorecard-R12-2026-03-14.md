## Round 12 Scoring — topic-plan (v11 rubric)

---

### Evaluation Framework

**39 criteria** | **245 pts total** | **Formula**: `(essential/5×60) + (recommended/3×30) + (aspirational/31×155)` | **Golden**: all essential + ≥145

**C-38/C-39 floor confirmation**: All 5 variations satisfy both new criteria. Labeled quoted PASS examples (`"teams run scout before draft"`, `"signal count threshold never defined"`, `"the phrase 'gather evidence first'"`) appear in every CONTRACT Rule 2 block. Every Step 2 cites "COLUMN CONTRACT Rule 2 PASS/FAIL exhibit" by name before cell population.

---

### V-01 — Conversational Phrasing Register

**Essential (C-01–C-05)**: All PASS.
- C-01: PASS — Step 1 reads and extracts strategy.md stated fields
- C-02: PASS — Step 3a globs directory, reads every artifact
- C-03: PASS — Step 4 anti-pattern PASS/FAIL exhibit enforces delta vs. inventory distinction
- C-04: PASS — Proposals table with Rule 1 types (ADD / REMOVE / REPRIORITIZE)
- C-05: PASS — Step 9 "Reply YES", Step 10 "only after YES"

**Recommended (C-06–C-08)**: All PASS. Evidence column in proposals, diff table with before/after, all three change types with null rows.

**Aspirational — notable items:**

| ID | Verdict | Evidence note |
|----|---------|---------------|
| C-09 | PASS | Step 5 lists all 9 namespaces with "Stage-relative = right for where topic currently is, not just a raw count" |
| C-21 | PASS | Per-step adjacent declarations at all template sites: "Every column below is required — skip one and this step doesn't count" |
| C-22 | PASS | Step 4: "Stop. Before building the findings table, write: 1. The name of the anti-pattern you're guarding against" |
| C-23 | **PARTIAL** | Step 6 has both components ("don't skip this table" + verbatim CF-00). Steps 3a, 4, 7 null cases have verbatim templates but NO explicit "Do not omit" adjacent instruction — "reproduce this verbatim" alone is insufficient under C-23's two-component requirement |
| C-36 | PASS | COLUMN CONTRACT block precedes schema; Rule 1/Rule 2 numbered; commitment checkpoints reference rules |
| C-37 | PASS | Decision-question ("Could I write this cell without looking at the source document?") + labeled PASS/FAIL examples in Rule 2 |
| C-38 | PASS | PASS examples are concrete quoted values, symmetric with FAIL examples in specificity |
| C-39 | PASS | Step 2: "apply the COLUMN CONTRACT Rule 2 test and PASS/FAIL exhibit" — cites CONTRACT by name at extraction step |

All others: PASS.

**Aspirational**: 30.5/31 (C-23 PARTIAL = 0.5)
**Score**: 60 + 30 + (30.5/31 × 155) = 60 + 30 + 152.5 = **242.5**

---

### V-02 — Expanded COLUMN CONTRACT, Compressed Steps

**Essential**: All PASS.
**Recommended**: All PASS.

**Aspirational — key differentiators:**

| ID | Verdict | Evidence note |
|----|---------|---------------|
| C-16 | PASS | Rule 4 in CONTRACT: "full 'Strategy assumed [X] / Signal revealed [Y]' text with exact finding ID" — proposals schema column references Rule 4 |
| C-21 | PASS | V-02 compressed steps but preserved per-step mandatory declarations at ALL template sites: "The following columns are mandatory. Do not omit any column." at Steps 1, 2, 3a, 4, 5, 6, 7, 8 |
| C-23 | **PASS** | Key differentiator. Rule 3 in CONTRACT: "A missing section is indistinguishable from a section that was skipped entirely" + verbatim null templates. Every null case site cites "(Rule 3)" — this fires BOTH C-23 components (verbatim template + do-not-omit logic) via rule reference, consistently across all mandatory null sections |
| C-34 | PASS | Rule 1 CONTRACT has value lists + prose-prohibition ("prose is not a valid value"); upfront schema columns carry "[Rule 1: .../...]"; Step 7 commitment cites Rule 1 with full value lists and "prose not valid" |
| C-36 | PASS | Named "COLUMN CONTRACT" block; four numbered rules; commitment checkpoints at Steps 7/8 reference Rule 1 and Rule 4 |
| C-38 | PASS | Four PASS examples in Rule 2, all concrete quoted values symmetric with five labeled FAIL examples |
| C-39 | PASS | Step 2: "Apply the COLUMN CONTRACT Rule 2 PASS/FAIL exhibit before populating each `Implicit evidence` cell" |

All 31 aspirational: PASS.

**Score**: 60 + 30 + 155 = **245** (perfect)

---

### V-03 — Namespace Audit Before Delta

**Essential**: All PASS.
**Recommended**: All PASS.

**Aspirational — key items:**

| ID | Verdict | Evidence note |
|----|---------|---------------|
| C-09 | PASS | Stronger mechanism: Coverage Auditor at Step 4 (before Delta at Step 5) with "Delta candidate? [yes — generate F-NN at Step 5 / no]" column — namespace gaps are structurally available as delta sources at formation time |
| C-21 | PASS | Formal phrasing preserved per-step "The following columns are mandatory. Do not omit any column." at all template sites, including new Step 4 (Coverage Auditor): "Rule 1 applies to `Delta candidate?`" + mandatory declaration |
| C-23 | **PARTIAL** | Same issue as V-01. Step 6 has explicit "Do not omit this table" ✓. Steps 3a, 5, 7 null cases have verbatim templates but no adjacent "Do not omit" instruction — V-03 uses only 2-rule CONTRACT (Rule 1, Rule 2); no Rule 3 mechanism |
| C-36 | PASS | COLUMN CONTRACT precedes schema; Rule 1 covers new "Namespace gap?" [yes — NS-NAME / no] column |
| C-38 | PASS | Same quoted PASS examples as V-01 |
| C-39 | PASS | Step 2: "apply the COLUMN CONTRACT Rule 2 PASS/FAIL exhibit. If you can write the cell without reading strategy.md, it fails the test" |

All others: PASS.

**Aspirational**: 30.5/31 (C-23 PARTIAL = 0.5)
**Score**: 60 + 30 + 152.5 = **242.5**

---

### V-04 — Conversational + Expanded CONTRACT (V-01 + V-02)

**Essential**: All PASS.
**Recommended**: All PASS.

**Aspirational — key items:**

| ID | Verdict | Evidence note |
|----|---------|---------------|
| C-21 | **PARTIAL** | Critical finding. V-04 combines V-02's 4-rule CONTRACT with V-01's conversational compression. Steps 1–6 no longer carry adjacent "mandatory columns" declarations. Only Steps 7 and 8 have proper adjacent declarations (via commitment statements). The upfront schema "Every ★ column required. Don't skip any." does not satisfy C-21's "adjacent to each template" requirement — C-21 explicitly states "A declaration before proposals and diff only is a partial pass" |
| C-23 | PASS | V-04 inherits V-02's 4-rule CONTRACT including Rule 3. All null cases cite "(Rule 3)" — both C-23 components satisfied via rule reference |
| C-36 | PASS | 4-rule CONTRACT with rationale paragraphs; rule-reference at commitment checkpoints |
| C-38 | PASS | Four PASS examples including the fourth: "no definition of done appears in the strategy" — extends the exhibit |
| C-39 | PASS | Step 2: "apply the COLUMN CONTRACT Rule 2 PASS/FAIL exhibit" |

All others: PASS.

**Root cause**: Conversational compression in V-04 inadvertently removed the non-compressible anchors. V-02 compressed step BODIES (role + action + null case) but kept the mandatory-column declarations. V-04 compressed everything including those declarations.

**Aspirational**: 30.5/31 (C-21 PARTIAL = 0.5)
**Score**: 60 + 30 + 152.5 = **242.5**

---

### V-05 — Full Ceiling (V-01 + V-02 + V-03 + Pre-Read Hypothesis)

**Essential**: All PASS.
**Recommended**: All PASS.

**Aspirational — key items:**

| ID | Verdict | Evidence note |
|----|---------|---------------|
| C-09 | PASS | Namespace-first (V-03 mechanism) + hypothesis match column ("Hypothesis match [Rule 1: H-N confirmed / Surprise — not hypothesized]") in both Namespace Audit and Delta Findings tables — strongest C-09 implementation |
| C-21 | **PARTIAL** | Inherits V-04's conversational compression issue. Steps 0–6 lack adjacent mandatory-column declarations. Steps 7–8 have proper commitment statements. Same root cause as V-04 |
| C-23 | PASS | Inherits V-02's Rule 3 mechanism. All null cases carry "(Rule 3)" citations |
| C-34 | PASS | Rule 1 covers all new enumerated columns including "Hypothesis match" [H-N confirmed / Surprise — not hypothesized] and "Namespace gap?" [yes — NS-NAME / no]; both declared in upfront schema with value lists |
| C-38 | PASS | Same concrete quoted PASS examples + fourth variant "no definition of done appears anywhere in the strategy" |
| C-39 | PASS | Step 2: "apply the COLUMN CONTRACT Rule 2 PASS/FAIL exhibit. Ask: 'Could I write this cell without reading strategy.md?' If yes, the cell fails" |

Pre-read hypothesis (Step 0) and hypothesis-match columns add analytical depth not yet captured by a dedicated v11 criterion. The hypothesis machinery (C-09 enhancement via namespace prediction scoring) is real but not score-differentiating under current rubric.

**Aspirational**: 30.5/31 (C-21 PARTIAL = 0.5)
**Score**: 60 + 30 + 152.5 = **242.5**

---

### Composite Scores and Ranking

| Variation | Essential | Recommended | Aspirational | Total | vs 245 |
|-----------|-----------|-------------|--------------|-------|--------|
| **V-02** | 60 | 30 | 155.0 | **245.0** | — |
| V-01 | 60 | 30 | 152.5 | **242.5** | −2.5 |
| V-03 | 60 | 30 | 152.5 | **242.5** | −2.5 |
| V-04 | 60 | 30 | 152.5 | **242.5** | −2.5 |
| V-05 | 60 | 30 | 152.5 | **242.5** | −2.5 |

**All 5 variations are golden** (all essential PASS + composite ≥ 145). R12 floor holds across the board.

**Sole differentiator**: V-02 is the only variation scoring 245. V-01 and V-03 lose 2.5 pts to C-23 PARTIAL (no Rule 3 mechanism). V-04 and V-05 lose 2.5 pts to C-21 PARTIAL (conversational compression removed non-compressible anchors).

---

### Excellence Signals from V-02

**Signal 1 — Rule-reference null completeness (C-23 resolution)**
V-02's Rule 3 block defines null completeness as a named principle ("A missing section is indistinguishable from a section that was skipped entirely") with verbatim templates and explicit fail cases. Each null case site cites "(Rule 3)" — a single token that fires both C-23 components (verbatim template + do-not-omit instruction) via rule reference. V-01/V-03 use ad-hoc "reproduce this verbatim" instructions that carry the verbatim component but inconsistently omit the "Do not omit" component at most sites (only Step 6 in both has the explicit "don't skip this table" phrasing).

**Signal 2 — Non-compressible anchor preservation (C-21 gap in V-04/V-05)**
V-02 compressed step bodies (role + action + null case only) but treated per-step mandatory-column declarations ("The following columns are mandatory. Do not omit any column.") as non-compressible anchors retained at every template site. V-04/V-05 compressed these declarations away, relying on the upfront schema's global "Every ★ column required. Don't skip any." — which does not satisfy C-21's adjacency requirement. The finding is structural: the upfront schema declaration and the per-step mandatory-column declaration serve different functions (schema-first priming vs. template-adjacent enforcement); neither substitutes for the other.

**Signal 3 — Rationale-bearing rule blocks**
V-02's CONTRACT rules carry "Why this matters" rationale paragraphs (e.g., Rule 1: "An ADD-type proposal and a REPRIORITIZE-type proposal are structurally different change requests. Mixing types in prose removes that distinction and makes the proposals table non-auditable."). This grounds enforcement in reason rather than instruction-following, potentially reducing context-pressure attenuation — the model understands what breaks, not just what is forbidden.

---

### R13 Signals

**From V-02 vs V-04/V-05 on C-21**: The non-compressible anchor pattern has extraction potential. A new criterion could define which per-step declarations cannot be removed in any compression variant — specifically any declaration that C-21 requires to be "adjacent to each template definition." This would make the compression-vs-enforcement tradeoff explicit and prevent future regression.

**From V-03/V-05 on C-09**: Namespace-first sequencing (Coverage Auditor before Delta Identifier) with a "Delta candidate?" column in the Namespace Audit creates a structural mechanism where namespace absence becomes a delta source at formation time, not a post-delta audit note. All variations pass C-09, but V-03/V-05 pass it via a different architectural path. R13 should consider whether a new criterion captures the "namespace-gap-sourced delta finding" mechanism — specifically, whether the Namespace Audit table gains a "Delta candidate?" designation column that feeds directly into the Delta Findings table.

**From V-02's 4-rule CONTRACT**: Rules 3 and 4 (null completeness + two-level traceability) are now score-differentiating through C-23 resolution. If R13 promotes the non-compressible anchor pattern, V-04/V-05's C-21 gap becomes the next ceiling to close.

---

```json
{"top_score": 245, "all_essential_pass": true, "new_patterns": ["non-compressible-anchor: per-step mandatory-column declarations adjacent to each template must survive step compression — the upfront schema global statement does not substitute for template-adjacent enforcement, and conversational compression that removes these anchors causes C-21 partial regardless of how thorough the upfront schema is", "rule-reference-null-completeness: naming null-case instructions as a numbered CONTRACT rule carrying do-not-omit logic and citing it by reference at each null case site satisfies both C-23 components consistently across all mandatory null sections, outperforming ad-hoc per-site instructions that apply the do-not-omit component only at some sites"]}
```
