# Quest Score — org-scan R1

> **Warning**: Input truncated — only V-01 and V-02 were received. V-03 through V-05 are absent. Scoring the two available variations against all 10 rubric criteria.

---

## Rubric Weights

| Band | Criteria | Points Each | Total |
|---|---|---|---|
| Essential | C-01 – C-05 | 12 | 60 |
| Recommended | C-06 – C-08 | 10 | 30 |
| Aspirational | C-09 – C-10 | 5 | 10 |

PASS = full points · PARTIAL = half points · FAIL = 0

Golden threshold: all 5 essential PASS **and** composite ≥ 80.

---

## V-01 — Breadth-First Scan Loop

| Criterion | Result | Evidence Note |
|---|---|---|
| C-01 Areas grounded in scan evidence | **PASS** | Phase 2 states explicitly: "each area must be traceable to at least one source artifact from Phase 1. Do not invent areas that have no evidence basis." |
| C-02 Multi-source scan (3+ of 7) | **PASS** | Phase 1 mandates all 7 source types in order, with "complete all before drawing conclusions" hard gate. |
| C-03 Headcount signals estimated with rationale | **PASS** | Phase 4 dedicated, requires a range *and* "at least one observation from the scan as supporting rationale." |
| C-04 Cross-cutting concerns with boundary note | **PASS** | Phase 3 dedicated, requires naming areas spanned and explaining why single-team ownership fails. |
| C-05 Raw analysis, not an org chart | **PASS** | "This is NOT an org chart. Do not produce reporting lines, role boxes, or hierarchy." Stated in preamble and repeated in output format instructions. |
| C-06 Team boundary candidates with seam rationale | **PASS** | Phase 5 dedicated: boundary name + scan evidence for seam + coupling risk note. |
| C-07 Org shape named and justified | **PASS** | Phase 6 dedicated: named shape choices given, justification required "using specific scan findings." |
| C-08 Evidence gaps flagged explicitly | **PASS** | Phase 7 dedicated: missing source types, ambiguous signals, and absent artifacts all enumerated. |
| C-09 5+ file paths cited | **PARTIAL** | Phase 1 requires "at least one file path or path pattern per source" — if all 7 sources found that's 7 paths, but the "at least one" floor per source can still be met with fewer if sources are absent. Likely to reach 5+, not guaranteed. |
| C-10 Current vs recommended state separated | **PARTIAL** | Phases are sequenced (scan → synthesis → recommendation) but the prompt never names a "current state" section or explicitly labels the recommended state as distinct from the scan observations. |

### V-01 Score

| Band | Points Available | Points Earned |
|---|---|---|
| Essential (C-01–05) | 60 | 60 |
| Recommended (C-06–08) | 30 | 30 |
| Aspirational C-09 | 5 | 2.5 |
| Aspirational C-10 | 5 | 2.5 |
| **Total** | **100** | **95** |

**All essential: PASS. Composite: 95. Meets golden threshold.**

---

## V-02 — Table-Driven, Evidence-Linked Rows

> Note: V-02 input was truncated after Step 4. Steps 5+ (which likely contain team boundary candidates, org shape recommendation, and gap flags) are absent. C-06, C-07, C-08 scored PARTIAL to reflect possible presence in missing content.

| Criterion | Result | Evidence Note |
|---|---|---|
| C-01 Areas grounded in scan evidence | **PASS** | Step 2 table requires evidence column per row. "If you cannot fill the evidence column, do not add the row." Structural enforcement — fabricated rows cannot be completed. |
| C-02 Multi-source scan (3+ of 7) | **PASS** | Step 1 table has all 7 source types pre-populated. ABSENT marker required if not found. All 7 must be visited before Step 2. |
| C-03 Headcount signals estimated with rationale | **PASS** | Step 4 table exists with Source column and implied domain count. Summary line "Estimated distinct expertise domains: [N-M]" required. |
| C-04 Cross-cutting concerns with boundary note | **PASS** | Step 3 table: "Why It Cannot Be Owned By One Team" column mandated. At least 1 row required. |
| C-05 Raw analysis, not an org chart | **PASS** | "not an org chart. No reporting lines. No role hierarchy." Stated in preamble. |
| C-06 Team boundary candidates | **PARTIAL** | Not present in available content. May exist in missing steps — Step 4 is the last visible. |
| C-07 Org shape named and justified | **PARTIAL** | Not present in available content. May exist in missing steps. |
| C-08 Evidence gaps flagged | **PARTIAL** | ABSENT rows in Step 1 serve as a structural gap flag, but no dedicated gap-flagging step visible. Partial credit for structural inference. |
| C-09 5+ file paths cited | **PASS** | Step 1 "File Path Evidence" column × 7 sources = up to 7 paths. Step 2 "Evidence Path" column × 3+ rows = additional paths. Table structure makes this a floor, not a ceiling. |
| C-10 Current vs recommended state separated | **FAIL** | Tables don't separate current-state observations from recommended-state proposals. No explicit labeling in visible content. |

### V-02 Score

| Band | Points Available | Points Earned |
|---|---|---|
| Essential (C-01–05) | 60 | 60 |
| Recommended C-06 | 10 | 5 |
| Recommended C-07 | 10 | 5 |
| Recommended C-08 | 10 | 5 |
| Aspirational C-09 | 5 | 5 |
| Aspirational C-10 | 5 | 0 |
| **Total** | **100** | **80** |

**All essential: PASS. Composite: 80. Meets golden threshold (exactly at floor).**

> If missing steps are recovered and contain C-06/C-07/C-08 content, score rises to 95. If missing steps are absent from the actual skill output, score stays at 80.

---

## Ranking

| Rank | Variation | Composite | All Essential | Golden? |
|---|---|---|---|---|
| 1 | **V-01** (breadth-first phases) | **95** | PASS | YES |
| 2 | **V-02** (table-driven) | **80** | PASS | YES (floor) |
| — | V-03 | — | — | Missing |
| — | V-04 | — | — | Missing |
| — | V-05 | — | — | Missing |

---

## Excellence Signals from V-01

**What made V-01 score 95:**

1. **Breadth-first lock before synthesis** — Mandating all 7 sources visited before any conclusions drawn prevents the most common failure mode: anchoring on the first interesting source and never surfacing weaker signals. This directly protects C-01 and C-02.

2. **Dedicated phase per criterion** — Each rubric criterion maps to a named phase (Phase 3 = C-04, Phase 4 = C-03, Phase 5 = C-06, Phase 6 = C-07, Phase 7 = C-08). This is a structural guarantee: the LLM cannot complete the prompt without visiting every required output.

3. **Evidence negation rule** — "Do not invent areas that have no evidence basis" and "If a source type is absent from the repo, note it explicitly" together create a forcing function that converts absence into signal rather than letting absence become silence.

4. **C-05 stated in two locations** — The not-an-org-chart constraint appears in both the preamble ("This is NOT an org chart") and the output format instructions. Double placement reduces the risk of late-phase drift where LLMs produce a hierarchy anyway after reasoning into org shape territory.

---

## Gaps to Address in R2

1. **C-10 weakness** — Neither variation explicitly separates current state (what the scan found) from recommended state (what should change). A dedicated "Current State Summary / Recommended State Contrast" section would close this gap.

2. **C-09 floor risk in V-01** — "At least one file path per source" still allows V-01 to pass C-09 with only 3 paths if 4 sources are absent. Tighten to: "cite the 5 most specific file paths found across all sources."

3. **V-02 truncation** — Recover V-02 Steps 5+ before comparing table-driven vs phase-driven approaches. The truncated score of 80 vs 95 may reverse if V-02's missing steps handle C-06/C-07/C-08 well.

---

```json
{"top_score": 95, "all_essential_pass": true, "new_patterns": ["breadth-first source lock before synthesis prevents anchor bias and guarantees multi-source coverage", "one dedicated phase per rubric criterion is a structural guarantee — the LLM cannot skip a required output", "evidence negation rule converts source absence into an explicit signal rather than silence"]}
```
